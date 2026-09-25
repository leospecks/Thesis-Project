"""Generic loaders for the four raw inputs every pair needs.

These are Notebook 01's loaders (Sections 1.2, 1.4, 1.5/1.6), generalized to
take a target commodity's price-index path and a source column name as
parameters instead of hardcoding corn/China. The defensive "date"/"data"
column handling is preserved as-is: 00_data_prep.ipynb's per-commodity export
still has that typo (see decision log / open items in Notebook 01) as of
2026-09-17, and this loader must keep working whether or not it's been fixed
upstream.
"""
from __future__ import annotations

import warnings
from pathlib import Path

import pandas as pd


def load_target_price(path: Path) -> pd.Series:
    """Load a target commodity's continuous return-index level series.

    Accepts either a "date" or "data" date-column name (see module docstring).
    Returns a Series named by its own index ("date"), values are the
    constructed return-index level (base 100), NOT a raw settlement price.
    """
    df = pd.read_csv(path)
    date_col = "date" if "date" in df.columns else "data" if "data" in df.columns else None
    if date_col is None:
        raise ValueError(f"{path}: expected a 'date' (or 'data') column, found {list(df.columns)}")
    if date_col == "data":
        warnings.warn(
            f"{path}: reading the 'data' column as the date column -- this is very likely a typo "
            "in 00_data_prep.ipynb's rename step ('date' -> 'data'). Consider fixing it upstream."
        )
    df[date_col] = pd.to_datetime(df[date_col])
    s = df.set_index(date_col)["value"].sort_index()
    s.index.name = "date"
    return s


def load_source_commodity_return(path: Path, column: str) -> pd.Series:
    """Load one commodity's log-return column out of the shared source_series.csv."""
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    if column not in df.columns:
        raise ValueError(f"{path}: column '{column}' not found. Available: {list(df.columns)}")
    s = df[column].dropna().sort_index()
    s.index.name = "date"
    return s


def load_shared_global(path: Path) -> pd.DataFrame:
    """Load the shared-core global block (GSCI/DFF/DTB3/DTWEXBGS/VIXCLS), dense daily index."""
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    df.index.name = "date"
    return df


def load_local_features(path: Path) -> pd.DataFrame:
    """Load one target country's raw local-feature block, dense daily index."""
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    df.index.name = "date"
    return df
