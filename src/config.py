"""Resolve one pair_id into a fully-specified PairConfig.

Merges three layers, in this precedence order (later overrides earlier only
where a per-pair/per-country override actually exists -- there is currently
no mechanism for a pair to override a *global* default; that would need a
deliberate extension plus a decision-log entry, not a silent config field):

  1. configs/global_config.yaml  -- fixed source-domain paths + defaults
  2. configs/countries_registry.yaml -- target-country local-feature specifics
  3. configs/pairs_registry.csv  -- per-pair target specifics

This is the single place that turns "corn_china" into every path and
parameter the rest of the pipeline needs, so that adding a new pair is a
matter of adding rows to the two registries, never editing pipeline code.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import yaml

from src import registry as reg

PROJECT_ROOT = reg.PROJECT_ROOT
GLOBAL_CONFIG_PATH = PROJECT_ROOT / "configs" / "global_config.yaml"


@dataclass
class PairConfig:
    # --- identity ---
    pair_id: str
    target_country: str
    target_commodity: str
    target_exchange: str
    source_commodity: str
    inclusion_status: str
    selection_rationale: str

    # --- resolved absolute paths ---
    target_series_path: Path
    source_series_path: Path
    shared_global_path: Path
    local_features_path: Path
    model_ready_dir: Path
    results_db_path: Path

    # --- source-series column ---
    source_column: str

    # --- local-feature role -> actual column name for this country ---
    local_columns: dict  # {"fx": ..., "cpi": ..., "policy_rate": ..., "equity": ...}

    # --- alignment / lag parameters ---
    cpi_publication_lag_days: int
    shared_ffill_limits: dict
    default_shared_ffill_limit: int
    local_ffill_limits_by_role: dict

    # --- not-yet-decided global parameters (may be None) ---
    target_eval_window_start: Optional[str]
    horizon_h: Optional[int]

    seed: int = 42

    def local_ffill_limits(self) -> dict:
        """Map role-keyed ffill limits onto this country's actual column names."""
        return {
            self.local_columns[role]: limit
            for role, limit in self.local_ffill_limits_by_role.items()
        }

    def pair_out_dir(self) -> Path:
        d = self.model_ready_dir / self.pair_id
        d.mkdir(parents=True, exist_ok=True)
        return d


def _resolve(path_str: str) -> Path:
    return PROJECT_ROOT / path_str


def load_global_config(path: Path = GLOBAL_CONFIG_PATH) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def load_pair_config(pair_id: str) -> PairConfig:
    global_cfg = load_global_config()
    pairs_df = reg.load_pairs_registry()
    countries = reg.load_countries_registry()

    pair_row = reg.get_pair_row(pair_id, pairs_df)
    country_entry = reg.get_country_entry(pair_row["target_country"], countries)

    paths = global_cfg["project_paths"]
    defaults = global_cfg["defaults"]

    return PairConfig(
        pair_id=pair_id,
        target_country=pair_row["target_country"],
        target_commodity=pair_row["target_commodity"],
        target_exchange=pair_row["target_exchange"],
        source_commodity=pair_row["source_commodity"],
        inclusion_status=pair_row["inclusion_status"],
        selection_rationale=pair_row["selection_rationale"],
        target_series_path=_resolve(pair_row["target_series_path"]),
        source_series_path=_resolve(paths["source_series_path"]),
        shared_global_path=_resolve(paths["shared_global_path"]),
        local_features_path=_resolve(country_entry["local_features_path"]),
        model_ready_dir=_resolve(paths["model_ready_dir"]),
        results_db_path=_resolve(paths["results_db_path"]),
        source_column=pair_row["source_column"],
        local_columns=country_entry["columns"],
        cpi_publication_lag_days=country_entry["cpi_publication_lag_days"],
        shared_ffill_limits=defaults["shared_ffill_limits"],
        default_shared_ffill_limit=defaults["default_shared_ffill_limit"],
        local_ffill_limits_by_role=defaults["local_ffill_limits_by_role"],
        target_eval_window_start=defaults["target_eval_window_start"],
        horizon_h=defaults["horizon_h"],
        seed=defaults["seed"],
    )
