"""Loaders and light validation for the two registry files.

pairs_registry.csv    -- one row per commodity pair (target country/commodity/
                          exchange/paths, source commodity/column, inclusion
                          status, ex-ante selection rationale).
countries_registry.yaml -- one entry per target country (local-feature file
                          path, role -> column-name mapping, CPI publication
                          lag). Local features are country-level, not
                          commodity-level, which is why this is a separate
                          registry rather than columns on pairs_registry.csv.

Both registries are the ex-ante record required by the project's
source/pair-selection-discipline instructions: a pair's `inclusion_status`
and `selection_rationale` are set when the row is added, not derived from
test-set performance.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import pandas as pd
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PAIRS_REGISTRY_PATH = PROJECT_ROOT / "configs" / "pairs_registry.csv"
COUNTRIES_REGISTRY_PATH = PROJECT_ROOT / "configs" / "countries_registry.yaml"

REQUIRED_PAIR_COLUMNS = [
    "pair_id", "target_country", "target_commodity", "target_exchange",
    "target_series_path", "source_commodity", "source_column",
    "inclusion_status", "min_overlap_years", "selection_rationale", "date_added",
]
VALID_INCLUSION_STATUSES = {"included", "candidate", "excluded", "test_fixture"}
VALID_COUNTRY_STATUSES = {"included", "candidate", "test_fixture"}
REQUIRED_COUNTRY_ROLES = {"fx", "cpi", "policy_rate", "equity"}


def load_pairs_registry(path: Path = PAIRS_REGISTRY_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = set(REQUIRED_PAIR_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"{path}: pairs_registry.csv is missing required column(s): {missing}")
    if df["pair_id"].duplicated().any():
        dupes = df.loc[df["pair_id"].duplicated(), "pair_id"].tolist()
        raise ValueError(f"{path}: duplicate pair_id(s): {dupes}")
    bad_status = set(df["inclusion_status"]) - VALID_INCLUSION_STATUSES
    if bad_status:
        raise ValueError(f"{path}: unrecognized inclusion_status value(s): {bad_status}")
    return df.set_index("pair_id", drop=False)


def load_countries_registry(path: Path = COUNTRIES_REGISTRY_PATH) -> dict:
    with open(path) as f:
        registry = yaml.safe_load(f) or {}
    for country, entry in registry.items():
        missing_keys = {"status", "local_features_path", "columns", "cpi_publication_lag_days"} - set(entry)
        if missing_keys:
            raise ValueError(f"countries_registry.yaml[{country}]: missing key(s) {missing_keys}")
        if entry["status"] not in VALID_COUNTRY_STATUSES:
            raise ValueError(f"countries_registry.yaml[{country}]: unrecognized status '{entry['status']}'")
        missing_roles = REQUIRED_COUNTRY_ROLES - set(entry["columns"])
        if missing_roles:
            raise ValueError(f"countries_registry.yaml[{country}]: columns missing role(s) {missing_roles}")
    return registry


def get_pair_row(pair_id: str, pairs_df: Optional[pd.DataFrame] = None) -> pd.Series:
    pairs_df = pairs_df if pairs_df is not None else load_pairs_registry()
    if pair_id not in pairs_df.index:
        raise KeyError(f"pair_id '{pair_id}' not found in pairs_registry.csv. "
                        f"Available: {list(pairs_df.index)}")
    return pairs_df.loc[pair_id]


def get_country_entry(country: str, countries: Optional[dict] = None) -> dict:
    countries = countries if countries is not None else load_countries_registry()
    if country not in countries:
        raise KeyError(f"country '{country}' not found in countries_registry.yaml. "
                        f"Available: {list(countries)}")
    return countries[country]


def list_pairs(status: Optional[str] = None, pairs_df: Optional[pd.DataFrame] = None) -> list:
    """List pair_ids, optionally filtered to one inclusion_status.

    Real cross-pair analysis should filter to status == "included" (or
    "candidate") explicitly, so a "test_fixture" row used only to validate
    the pipeline's plumbing can never silently leak into a results table.
    """
    pairs_df = pairs_df if pairs_df is not None else load_pairs_registry()
    if status is None:
        return list(pairs_df.index)
    return list(pairs_df.index[pairs_df["inclusion_status"] == status])
