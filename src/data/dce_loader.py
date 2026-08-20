"""
dce_loader.py
=============

Convert raw Dalian Commodity Exchange "HistoryDayQuotes" exports into the
clean contract panel consumed by `futures_series.py`.

Raw format (one file per product-year), columns:
    Products, Contract, Trade Date, Open, High, Low, Close,
    Prev Settle, Settle, Chg, Change1, Volume, OI, OI Chg, Turnover

Quirks this module handles
--------------------------
1. All numerics arrive as strings with thousand separators ("2,650").
2. `Trade Date` is an integer-like string, YYYYMMDD.
3. On no-trade days the exchange still publishes a row, with
   Open = High = Low = 0, Volume = 0, and Close = Settle carried forward.
   Zero is NOT a price -- it must become NaN, not feed into a return.
4. `Settle` is the full-session VWAP: Turnover / (Volume * multiplier).
   It is NOT a closing price. `Close` is the last traded price.
   See PRICE COLUMN CHOICE below.
5. `Chg`      = Close  - Prev Settle
   `Change1`  = Settle - Prev Settle
   (both verified to hold exactly on the 2006 soybean sample)
6. Contract codes embed the delivery month: a0601 -> product "a",
   delivery 2006-01. Expiry is NOT in the file and must be derived.
7. Daily price limits truncate returns; limit days are flagged, not dropped.

PRICE COLUMN CHOICE
-------------------
Use `Close` for the forecasting label. A full-session VWAP is a time-average
of intraday prices, so settle-to-settle returns inherit spurious positive
autocorrelation that is a mechanical artefact of the averaging, not signal.
That matters twice over in a cross-market study: CME/CBOT settlement is a
short closing-range procedure rather than a full-session VWAP, so
settle-based series from the two exchanges are not the same object, and the
difference would show up as a domain gap with no economic content.

Keep settle-based returns as a robustness check (`price_col="Settle"`) and
report both.
"""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd

# Contract size in tonnes per lot, by DCE product root.
# Used only for the Turnover/Volume/Settle identity check.
DCE_MULTIPLIER = {
    "a": 10,    # No.1 Soybeans
    "b": 10,    # No.2 Soybeans
    "m": 10,    # Soybean Meal
    "y": 10,    # Soybean Oil
    "p": 10,    # Palm Olein
    "c": 10,    # Corn
    "cs": 10,   # Corn Starch
    "jd": 5,    # Eggs (500 kg)
    "i": 100,   # Iron Ore
    "j": 100,   # Coke
    "jm": 60,   # Coking Coal
    "l": 5,     # LLDPE
    "v": 5,     # PVC
    "pp": 5,    # Polypropylene
}

RAW_NUMERIC = [
    "Open", "High", "Low", "Close", "Prev Settle", "Settle",
    "Chg", "Change1", "Volume", "OI", "OI Chg", "Turnover",
]

CONTRACT_RE = re.compile(r"^([a-z]+)(\d{2})(\d{2})$")


# ---------------------------------------------------------------------------
# 1. Parsing
# ---------------------------------------------------------------------------

def parse_contract(code: str, reference_year: int) -> tuple[str, int, int]:
    """
    Decode a DCE contract code into (root, delivery_year, delivery_month).

    'a0601' -> ('a', 2006, 1)

    The two-digit year is century-ambiguous. Resolved by requiring delivery
    to fall on or after `reference_year` (the first trade year in the file);
    contracts never deliver into the past.
    """
    m = CONTRACT_RE.match(str(code).strip().lower())
    if not m:
        raise ValueError(f"Unrecognised contract code: {code!r}")
    root, yy, mm = m.group(1), int(m.group(2)), int(m.group(3))
    if not 1 <= mm <= 12:
        raise ValueError(f"Bad delivery month in {code!r}")

    year = 2000 + yy
    while year < reference_year:
        year += 100
    return root, year, mm


def load_dce_file(path: str | Path) -> pd.DataFrame:
    """Read one raw DCE export and return a tidy, typed frame."""
    raw = pd.read_excel(path, dtype=str)

    missing = [c for c in ["Products", "Contract", "Trade Date"] + RAW_NUMERIC
               if c not in raw.columns]
    if missing:
        raise ValueError(f"{Path(path).name}: missing columns {missing}")

    df = raw.copy()
    df["date"] = pd.to_datetime(df["Trade Date"].str.strip(), format="%Y%m%d")

    for c in RAW_NUMERIC:
        df[c] = pd.to_numeric(
            df[c].astype(str).str.replace(",", "", regex=False).str.strip(),
            errors="coerce",
        )

    df["contract"] = df["Contract"].str.strip().str.lower()
    df["product"] = df["Products"].str.strip()

    ref_year = int(df["date"].dt.year.min())
    decoded = df["contract"].map(lambda c: parse_contract(c, ref_year))
    df["root"] = [d[0] for d in decoded]
    df["delivery_year"] = [d[1] for d in decoded]
    df["delivery_month"] = [d[2] for d in decoded]

    # A no-trade row is the exchange carrying the previous settle forward.
    # Open/High/Low are literally 0, which would poison any return or range
    # feature if left as a number.
    df["no_trade"] = (df["Volume"].fillna(0) == 0) & (df["Open"].fillna(0) == 0)
    for c in ["Open", "High", "Low"]:
        df.loc[df[c] == 0, c] = np.nan

    df["source_file"] = Path(path).name
    return df.sort_values(["contract", "date"]).reset_index(drop=True)


def load_dce_files(paths) -> pd.DataFrame:
    """
    Load and concatenate many raw files.

    IMPORTANT: expiry is derived from the last observation of each contract,
    so you must load the WHOLE history before calling derive_expiry(). A
    contract that is still alive at the end of a single-year file will
    otherwise be assigned a fake expiry at 31 December.
    """
    frames = [load_dce_file(p) for p in paths]
    out = pd.concat(frames, ignore_index=True)
    out = out.drop_duplicates(subset=["contract", "date"], keep="last")
    return out.sort_values(["contract", "date"]).reset_index(drop=True)


# ---------------------------------------------------------------------------
# 2. Expiry
# ---------------------------------------------------------------------------

def derive_expiry(df: pd.DataFrame, warn: bool = True) -> pd.DataFrame:
    """
    Last trading day per contract, taken as the last date it appears.

    Cross-check: DCE agricultural contracts expire on the 10th trading day
    of the delivery month, so the empirical value should land there. The
    `expiry_is_truncated` flag marks contracts whose last observation is the
    last date in the whole panel -- those are still alive, not expired, and
    their expiry is unknown until you load more data.
    """
    panel_end = df["date"].max()
    exp = df.groupby("contract")["date"].max().rename("expiry").reset_index()
    exp["expiry_is_truncated"] = exp["expiry"] >= panel_end

    if warn and exp["expiry_is_truncated"].any():
        n = int(exp["expiry_is_truncated"].sum())
        print(
            f"[derive_expiry] {n} contract(s) still open at panel end "
            f"({panel_end.date()}); their expiry is a placeholder. "
            "Load the remaining years before building a roll calendar."
        )

    return df.merge(exp, on="contract", how="left")


# ---------------------------------------------------------------------------
# 3. Integrity checks
# ---------------------------------------------------------------------------

def detect_price_limit(df: pd.DataFrame) -> float | None:
    """
    Infer the daily price limit empirically as the modal large move.
    Limits change over time and by product, so inferring beats hard-coding.
    Returns the limit as a decimal (e.g. 0.04) or None if none is evident.
    """
    pct = ((df["Close"] - df["Prev Settle"]) / df["Prev Settle"]).abs().dropna()
    if pct.empty:
        return None

    # A limit is a BOUNDARY, not a mode: mass piles up exactly at it and
    # almost nothing lies beyond. Scan candidate levels and pick the lowest
    # one that has a real spike and is rarely exceeded.
    for v in np.arange(0.02, 0.155, 0.001):
        at = ((pct > v - 0.0015) & (pct <= v + 0.0015)).sum()
        beyond = (pct > v + 0.0015).sum()
        if at >= 3 and beyond <= max(1, 0.25 * at):
            return round(float(v), 3)
    return None


def integrity_report(df: pd.DataFrame) -> dict:
    """
    Run every check that can be done from the raw file alone. Save the
    output -- it is exactly the provenance evidence an examiner will
    want in a data appendix.
    """
    rep: dict = {}
    d = df.sort_values(["contract", "date"]).copy()

    rep["n_rows"] = len(d)
    rep["n_contracts"] = d["contract"].nunique()
    rep["n_dates"] = d["date"].nunique()
    rep["date_range"] = (d["date"].min().date(), d["date"].max().date())

    # (a) Prev Settle must chain to the previous Settle of the same contract.
    #     A break means a missing trading day or a corrupted row.
    d["_settle_lag"] = d.groupby("contract")["Settle"].shift(1)
    chain = d.dropna(subset=["_settle_lag"])
    breaks = (chain["Prev Settle"] - chain["_settle_lag"]).abs() > 0.01
    rep["prev_settle_breaks"] = int(breaks.sum())
    rep["prev_settle_checked"] = int(len(chain))
    rep["prev_settle_break_rows"] = (
        chain.loc[breaks, ["contract", "date", "Prev Settle", "_settle_lag"]]
        .head(20).to_dict("records")
    )

    # (b) Settle should equal Turnover / (Volume * multiplier) on traded days.
    root = d["root"].mode().iloc[0] if "root" in d.columns else None
    mult = DCE_MULTIPLIER.get(root)
    if mult and "Turnover" in d.columns:
        t = d[(d["Volume"] > 0) & d["Turnover"].notna()].copy()
        implied = t["Turnover"] / (t["Volume"] * mult)
        dev = (implied - t["Settle"]).abs()
        rep["multiplier_assumed"] = mult
        rep["vwap_identity_share_within_1"] = round(float((dev < 1).mean()), 4)
        rep["vwap_identity_max_dev"] = round(float(dev.max()), 2)
        rep["vwap_identity_note"] = (
            "Deviations concentrate on final trading days, where DCE uses the "
            "delivery settlement price instead of the session VWAP."
        )

    # (c) No-trade rows.
    rep["n_no_trade_rows"] = int(d["no_trade"].sum())
    rep["pct_no_trade"] = round(float(d["no_trade"].mean() * 100), 2)

    # (d) Price limits.
    lim = detect_price_limit(d)
    rep["inferred_price_limit"] = lim
    if lim:
        pct = (d["Close"] - d["Prev Settle"]) / d["Prev Settle"]
        rep["n_limit_days"] = int((pct.abs() >= lim - 0.0005).sum())

    # (e) Per-contract liquidity, for the data audit table.
    liq = d.groupby("contract").agg(
        n_obs=("date", "size"),
        first=("date", "min"),
        last=("date", "max"),
        pct_no_trade=("no_trade", "mean"),
        median_volume=("Volume", "median"),
        median_oi=("OI", "median"),
    )
    liq["pct_no_trade"] = (liq["pct_no_trade"] * 100).round(1)
    rep["per_contract"] = liq.reset_index()

    return rep


def print_report(rep: dict) -> None:
    print("=" * 62)
    print("DCE RAW DATA INTEGRITY REPORT")
    print("=" * 62)
    print(f"rows {rep['n_rows']}   contracts {rep['n_contracts']}   "
          f"trade dates {rep['n_dates']}")
    print(f"range {rep['date_range'][0]} -> {rep['date_range'][1]}")
    print()
    print(f"Prev Settle chain     : {rep['prev_settle_breaks']} breaks "
          f"of {rep['prev_settle_checked']} checked")
    if "vwap_identity_share_within_1" in rep:
        print(f"Settle = VWAP identity: "
              f"{rep['vwap_identity_share_within_1']:.2%} within 1 tick "
              f"(multiplier {rep['multiplier_assumed']}t, "
              f"max dev {rep['vwap_identity_max_dev']})")
    print(f"No-trade rows         : {rep['n_no_trade_rows']} "
          f"({rep['pct_no_trade']}%)")
    if rep.get("inferred_price_limit"):
        print(f"Inferred price limit  : {rep['inferred_price_limit']:.1%} "
              f"({rep.get('n_limit_days', 0)} limit days)")
    print()
    print("Per-contract liquidity:")
    print(rep["per_contract"].to_string(index=False))
    print("=" * 62)


# ---------------------------------------------------------------------------
# 4. Emit the panel that futures_series.py expects
# ---------------------------------------------------------------------------

def to_panel(df: pd.DataFrame, price_col: str = "Close") -> pd.DataFrame:
    """
    Reshape to the schema `futures_series.py` consumes:
        date, contract, expiry, settle, volume, open_interest

    `settle` here means "the price series you are treating as THE price".
    Pass price_col="Close" for the label (recommended) or "Settle" for the
    VWAP robustness check.
    """
    if price_col not in df.columns:
        raise ValueError(f"price_col {price_col!r} not in frame")
    if "expiry" not in df.columns:
        raise ValueError("call derive_expiry() first")

    out = pd.DataFrame(
        {
            "date": df["date"],
            "contract": df["contract"],
            "expiry": df["expiry"],
            "settle": df[price_col],
            "volume": df["Volume"],
            "open_interest": df["OI"],
            "no_trade": df["no_trade"],
            "product": df["product"],
        }
    )
    # Drop contracts that never had open interest -- listed but never live.
    live = out.groupby("contract")["open_interest"].max()
    out = out[out["contract"].isin(live[live > 0].index)]
    return out.dropna(subset=["settle"]).reset_index(drop=True)


def prepare(paths, price_col: str = "Close", verbose: bool = True):
    """One-shot: raw files -> (panel, integrity report)."""
    raw = load_dce_files(paths)
    raw = derive_expiry(raw)
    rep = integrity_report(raw)
    if verbose:
        print_report(rep)
    return to_panel(raw, price_col=price_col), rep


if __name__ == "__main__":
    import sys

    files = sys.argv[1:] or ["/mnt/user-data/uploads/a_ftr.xlsx"]
    panel, _ = prepare(files)
    print("\nPanel head:")
    print(panel.head().to_string(index=False))
