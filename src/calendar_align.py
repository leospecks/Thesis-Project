"""Publication-lag shifting and own-calendar alignment.

This is the tested logic from 01_domain_consolidation_eda.ipynb (built and
verified against synthetic data on 2026-09-16/17), generalized to take its
forward-fill limits as parameters rather than hardcoded corn/China constants.
Do not change the two-step order inside align_to_calendar without re-reading
its docstring below -- two more "obvious" approaches were tried and rejected
during that debugging session.
"""
from __future__ import annotations

import warnings

import pandas as pd


def apply_publication_lag(series: pd.Series, lag_days: int) -> pd.Series:
    """Shift a sparse/step-like series' observations forward by lag_days calendar days.

    Only non-null observations are shifted (so this works correctly on a series
    that is NaN on most days and carries a real value only on print dates), and
    duplicate resulting dates (possible if lag_days pushes two prints onto the
    same day) keep the later print.

    Must be applied BEFORE align_to_calendar's reindex/ffill step -- doing it
    after would defeat the purpose of the lag (Notebook 01, Section 1.4).
    """
    obs = series.dropna()
    shifted_index = obs.index + pd.Timedelta(days=lag_days)
    shifted = pd.Series(obs.values, index=shifted_index).sort_index()
    shifted = shifted[~shifted.index.duplicated(keep="last")]
    return shifted


def align_to_calendar(df: pd.DataFrame, calendar: pd.DatetimeIndex,
                       limits: dict, default_limit) -> pd.DataFrame:
    """Carry each column's last known value forward, then subset onto `calendar`.

    Two things went wrong with more obvious-looking approaches during the
    original Notebook 01 build, worth recording so they don't get reintroduced:

    1. reindex(calendar) THEN .ffill(limit=N): a plain reindex(calendar) only
       pulls values for labels that are exact matches. `df`'s own index is
       already a dense daily calendar, so this step doesn't lose values
       directly -- but the *next* reindex, onto a business-day-only calendar,
       does: if a sparse observation (e.g. a lag-shifted CPI print) happens to
       fall on a weekend, that date is never one of the requested labels, so
       the value is invisible to the business-day series entirely, and
       ffill's limit -- measured in business-day row-count, not calendar
       days -- then runs out before the next (visible) print. Net effect:
       some prints vanish for up to ~2 reporting periods.
    2. reindex(calendar, method='ffill', limit=N) as a single step:
       method='ffill' during reindex fills *missing labels* by borrowing the
       nearest earlier existing label's value -- it does NOT skip over NaN
       *values* sitting on labels that already exist. Since `df`'s index here
       is already a complete daily calendar (mostly NaN, sparsely populated),
       almost every label already "exists", so this is close to a no-op: it
       does not propagate real values across the NaN gaps at all, and NaN
       counts got worse, not better, when this was tried.

    The correct order: forward-fill each column on its OWN dense native index
    first (this is where a limit expressed in calendar days is actually
    meaningful, and plain Series.ffill correctly skips over NaNs to find the
    last real value) -- then subset the now-filled series onto the target
    trading calendar, which is a lossless plain reindex since every target
    date is already a label in the source's daily index.

    Parameters
    ----------
    df : DataFrame indexed by a dense calendar-day DatetimeIndex.
    calendar : the target domain's own trading-day index to subset onto.
    limits : {column_name: max_calendar_days_to_carry_forward or None}.
             None means fill indefinitely -- appropriate only for a variable
             that is genuinely constant between updates (e.g. a policy rate),
             not a data gap being papered over.
    default_limit : fallback limit for any column not present in `limits`.
    """
    df_sorted = df.sort_index()
    filled_native = pd.DataFrame(index=df_sorted.index)
    for col in df_sorted.columns:
        filled_native[col] = df_sorted[col].ffill(limit=limits.get(col, default_limit))
    aligned = filled_native.reindex(calendar)
    remaining_na = aligned.isna().sum()
    problem_cols = remaining_na[remaining_na > 0]
    if len(problem_cols):
        warnings.warn(
            "Columns with unresolved gaps after reindex+ffill (per-column limits applied) -- "
            "inspect before modeling (a column whose real-world history starts later than the "
            "calendar's first date will legitimately show gaps here; anything else needs a look):\n"
            f"{problem_cols.to_string()}"
        )
    return aligned
