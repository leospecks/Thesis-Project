"""
futures_series.py
=================

Construct clean return and feature series from raw individual-contract
futures data.

Design principle
----------------
Never difference a spliced *price* series. A futures price series is a
sequence of different assets; the price gap at a roll is the basis, not a
return. This module builds:

    1. a roll calendar          -> which contract is held on each date
    2. a spliced return series  -> the label y(t), causal, no roll artefacts
    3. a causal price index     -> for technical indicators only
    4. a constant-maturity curve-> for basis / term-structure FEATURES only
    5. a stale-price screen     -> liquidity filter for thin EM contracts

Input format
------------
A long DataFrame with one row per (date, contract):

    date              datetime64
    contract          str      contract identifier, e.g. "WMAZ_2024H"
    expiry            datetime64  last trading day of that contract
    settle            float    settlement price
    volume            float    optional, needed for stale screen
    open_interest     float    optional, needed for OI-based rolls

Author: data pipeline for cross-market commodity transfer learning thesis
"""

from __future__ import annotations

import numpy as np
import pandas as pd

REQUIRED_COLS = ["date", "contract", "expiry", "settle"]


# ---------------------------------------------------------------------------
# 0. Validation
# ---------------------------------------------------------------------------

def validate(df: pd.DataFrame) -> pd.DataFrame:
    """Check required columns exist, coerce dtypes, sort, drop exact dupes."""
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    out = df.copy()
    out["date"] = pd.to_datetime(out["date"])
    out["expiry"] = pd.to_datetime(out["expiry"])
    out["settle"] = pd.to_numeric(out["settle"], errors="coerce")

    n_before = len(out)
    out = out.drop_duplicates(subset=["date", "contract"])
    if len(out) < n_before:
        print(f"[validate] dropped {n_before - len(out)} duplicate rows")

    out = out.dropna(subset=["settle"])
    out = out[out["settle"] > 0]  # log returns require strictly positive
    out["days_to_expiry"] = (out["expiry"] - out["date"]).dt.days
    out = out[out["days_to_expiry"] >= 0]

    return out.sort_values(["date", "days_to_expiry"]).reset_index(drop=True)


# ---------------------------------------------------------------------------
# 1. Stale price screen
# ---------------------------------------------------------------------------

def flag_stale(df: pd.DataFrame, max_run: int = 3) -> pd.DataFrame:
    """
    Flag settlements that are likely carried forward rather than traded.

    A row is stale if volume == 0 (where available) OR the settle is
    unchanged from the previous observation of the same contract.
    `stale_run` counts consecutive stale days, so you can drop or
    down-weight long runs.

    Returns df with added columns: is_stale, stale_run.
    """
    out = df.copy()
    unchanged = out.groupby("contract")["settle"].diff().eq(0)

    if "volume" in out.columns:
        no_trade = out["volume"].fillna(0).eq(0)
        out["is_stale"] = unchanged | no_trade
    else:
        out["is_stale"] = unchanged

    def _run(s: pd.Series) -> pd.Series:
        # length of the current consecutive True-run, reset on False
        grp = (~s).cumsum()
        return s.groupby(grp).cumsum()

    out["stale_run"] = out.groupby("contract")["is_stale"].transform(_run)
    out["drop_stale"] = out["stale_run"] > max_run
    return out


def liquidity_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    Per contract-year summary used for the data audit table.
    Anything above ~15-20% stale days is not usable as a target series.
    """
    d = flag_stale(df)
    d["year"] = d["date"].dt.year
    rep = d.groupby(["contract", "year"]).agg(
        n_obs=("settle", "size"),
        pct_stale=("is_stale", "mean"),
        mean_volume=("volume", "mean") if "volume" in d.columns else ("settle", "size"),
    )
    rep["pct_stale"] = (rep["pct_stale"] * 100).round(1)
    return rep.reset_index()


# ---------------------------------------------------------------------------
# 2. Roll calendar
# ---------------------------------------------------------------------------

def build_roll_calendar(
    df: pd.DataFrame,
    method: str = "days_before_expiry",
    days_before: int = 5,
    min_days_to_expiry: int = 2,
) -> pd.DataFrame:
    """
    Decide which contract is the 'active' one on each date.

    method='days_before_expiry'
        Hold the nearest contract until `days_before` business days before
        its expiry, then move to the next. Fully reproducible, no extra data.

    method='open_interest'
        Hold the contract with the highest open interest, subject to having
        at least `min_days_to_expiry` days left. Better for thin markets
        where the nominal front contract can be effectively dead.
        Decision is made on day t and EXECUTED on t+1 (see splice_returns),
        so there is no look-ahead.

    Returns DataFrame [date, active_contract].
    """
    d = df.copy()

    if method == "days_before_expiry":
        eligible = d[d["days_to_expiry"] > days_before]
        picked = (
            eligible.sort_values(["date", "days_to_expiry"])
            .groupby("date", as_index=False)
            .first()[["date", "contract"]]
        )

    elif method == "open_interest":
        if "open_interest" not in d.columns:
            raise ValueError("open_interest column required for this method")
        eligible = d[d["days_to_expiry"] >= min_days_to_expiry].copy()
        eligible = eligible.dropna(subset=["open_interest"])
        picked = (
            eligible.sort_values(
                ["date", "open_interest", "days_to_expiry"],
                ascending=[True, False, True],
            )
            .groupby("date", as_index=False)
            .first()[["date", "contract"]]
        )

    else:
        raise ValueError(f"Unknown method: {method}")

    picked = picked.rename(columns={"contract": "active_contract"})
    picked = picked.sort_values("date").reset_index(drop=True)

    # Suppress roll-flapping: once we move to a later contract, never move back
    seen_order = {}
    for i, row in picked.iterrows():
        seen_order.setdefault(row["active_contract"], i)
    picked["_rank"] = picked["active_contract"].map(seen_order)
    picked["_rank"] = picked["_rank"].cummax()
    rank_to_contract = {v: k for k, v in seen_order.items()}
    picked["active_contract"] = picked["_rank"].map(rank_to_contract)

    return picked[["date", "active_contract"]]


def roll_log(calendar: pd.DataFrame) -> pd.DataFrame:
    """Audit artefact: one row per roll, listing date, from- and to-contract."""
    c = calendar.copy()
    c["prev"] = c["active_contract"].shift(1)
    rolls = c[c["prev"].notna() & (c["prev"] != c["active_contract"])]
    return rolls.rename(
        columns={"prev": "from_contract", "active_contract": "to_contract"}
    )[["date", "from_contract", "to_contract"]].reset_index(drop=True)


# ---------------------------------------------------------------------------
# 3. Spliced returns  -- THIS IS YOUR LABEL
# ---------------------------------------------------------------------------

def splice_returns(df: pd.DataFrame, calendar: pd.DataFrame) -> pd.DataFrame:
    """
    Log return over [t-1, t] on the contract actually held across that
    interval. Both prices come from the same contract, so no roll gap
    ever enters the return.

    The contract held over [t-1, t] is the one active as of t-1: the
    decision is made at the close of t-1 and executed into t.

    Returns DataFrame [date, contract_held, ret, is_roll_day].
    """
    prices = df.set_index(["date", "contract"])["settle"]
    cal = calendar.sort_values("date").reset_index(drop=True)

    # contract chosen at t-1 is the one held into t
    cal["held"] = cal["active_contract"].shift(1)
    cal["prev_date"] = cal["date"].shift(1)
    cal = cal.dropna(subset=["held", "prev_date"])

    rows = []
    for _, r in cal.iterrows():
        key_now = (r["date"], r["held"])
        key_prev = (r["prev_date"], r["held"])
        if key_now in prices.index and key_prev in prices.index:
            ret = np.log(prices[key_now] / prices[key_prev])
        else:
            ret = np.nan  # held contract did not trade on both days
        rows.append(
            {
                "date": r["date"],
                "contract_held": r["held"],
                "ret": ret,
                "is_roll_day": r["held"] != r["active_contract"],
            }
        )

    out = pd.DataFrame(rows)
    n_missing = out["ret"].isna().sum()
    if n_missing:
        print(f"[splice_returns] {n_missing} dates with no usable price pair")
    return out


def causal_index(returns: pd.DataFrame, base: float = 100.0) -> pd.Series:
    """
    Cumulate spliced returns into a level series anchored at the START of
    the sample. Equivalent to a ratio-adjusted series, but nothing is ever
    revised when a new roll happens. Use for moving averages, RSI, realised
    vol -- NOT as a tradeable price.
    """
    r = returns.set_index("date")["ret"].fillna(0.0)
    return base * np.exp(r.cumsum())


# ---------------------------------------------------------------------------
# 4. Curve features
# ---------------------------------------------------------------------------

def basis(df: pd.DataFrame, calendar: pd.DataFrame, annualise: bool = True) -> pd.DataFrame:
    """
    Log spread between the active contract and the next-deferred one.
    Optionally annualised by the maturity difference, which makes it
    comparable across markets with different delivery calendars -- worth
    doing for a cross-market study.

    Returns DataFrame [date, basis, days_gap].
    """
    cal = calendar.set_index("date")["active_contract"]
    rows = []
    for date, grp in df.groupby("date"):
        if date not in cal.index:
            continue
        active = cal.loc[date]
        g = grp.sort_values("days_to_expiry")
        if active not in set(g["contract"]):
            continue
        pos = g.index[g["contract"] == active][0]
        loc = g.index.get_loc(pos)
        if loc + 1 >= len(g):
            continue
        front, deferred = g.iloc[loc], g.iloc[loc + 1]
        gap = deferred["days_to_expiry"] - front["days_to_expiry"]
        if gap <= 0:
            continue
        b = np.log(deferred["settle"] / front["settle"])
        rows.append(
            {
                "date": date,
                "basis": b * (365.0 / gap) if annualise else b,
                "days_gap": gap,
                "days_to_expiry": front["days_to_expiry"],
            }
        )
    return pd.DataFrame(rows)


def constant_maturity(df: pd.DataFrame, target_days: int = 90) -> pd.DataFrame:
    """
    Interpolate the curve to a fixed horizon, in log price, using the two
    contracts bracketing `target_days`.

    This removes the sawtooth in time-to-maturity caused by seasonal
    delivery calendars (SAFEX maize lists only Mar/May/Jul/Sep/Dec, CBOT
    corn lists Mar/May/Jul/Sep/Dec too but CME energy lists all twelve),
    making source and target features far more comparable.

    WARNING: differences in this series are NOT tradeable returns -- they
    mix price movement with roll-down. Use for FEATURES only.

    Returns DataFrame [date, cm_price, cm_log_price].
    """
    rows = []
    for date, grp in df.groupby("date"):
        g = grp.sort_values("days_to_expiry")
        below = g[g["days_to_expiry"] <= target_days]
        above = g[g["days_to_expiry"] > target_days]
        if below.empty or above.empty:
            continue
        lo, hi = below.iloc[-1], above.iloc[0]
        span = hi["days_to_expiry"] - lo["days_to_expiry"]
        if span == 0:
            continue
        w = (target_days - lo["days_to_expiry"]) / span
        log_p = (1 - w) * np.log(lo["settle"]) + w * np.log(hi["settle"])
        rows.append({"date": date, "cm_log_price": log_p, "cm_price": np.exp(log_p)})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# 5. End-to-end convenience wrapper
# ---------------------------------------------------------------------------

def build_series(
    raw: pd.DataFrame,
    roll_method: str = "days_before_expiry",
    days_before: int = 5,
    cm_horizon: int = 90,
    max_stale_run: int = 3,
) -> dict:
    """
    Run the whole pipeline. Returns a dict of DataFrames:

        clean      validated + stale-flagged contract panel
        calendar   date -> active contract
        rolls      audit log of every roll
        returns    THE LABEL: date, ret, is_roll_day
        index      causal price index for technical indicators
        basis      annualised term-structure slope
        cm         constant-maturity curve point
        liquidity  per contract-year stale/volume report
    """
    clean = flag_stale(validate(raw), max_run=max_stale_run)
    usable = clean[~clean["drop_stale"]]

    calendar = build_roll_calendar(usable, method=roll_method, days_before=days_before)
    returns = splice_returns(usable, calendar)

    return {
        "clean": clean,
        "calendar": calendar,
        "rolls": roll_log(calendar),
        "returns": returns,
        "index": causal_index(returns),
        "basis": basis(usable, calendar),
        "cm": constant_maturity(usable, target_days=cm_horizon),
        "liquidity": liquidity_report(clean),
    }


if __name__ == "__main__":
    # Minimal smoke test with synthetic two-contract data in contango.
    dates = pd.bdate_range("2024-01-01", "2024-06-28")
    rng = np.random.default_rng(0)

    def path(start, n):
        return start * np.exp(np.cumsum(rng.normal(0, 0.012, n)))

    a = pd.DataFrame(
        {
            "date": dates[:100],
            "contract": "TEST_H24",
            "expiry": pd.Timestamp("2024-05-24"),
            "settle": path(100.0, 100),
            "volume": 1000.0,
            "open_interest": 5000.0,
        }
    )
    b = pd.DataFrame(
        {
            "date": dates[60:],
            "contract": "TEST_N24",
            "expiry": pd.Timestamp("2024-07-26"),
            "settle": path(112.0, len(dates) - 60),
            "volume": 800.0,
            "open_interest": 4000.0,
        }
    )
    out = build_series(pd.concat([a, b], ignore_index=True))

    print("\nRolls:\n", out["rolls"])
    print("\nReturn stats:\n", out["returns"]["ret"].describe())
    print("\nMax abs return:", out["returns"]["ret"].abs().max().round(4))
    print("(should be a normal daily move, NOT a ~12% roll jump)")
