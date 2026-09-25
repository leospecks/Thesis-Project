"""Build the two model-ready panels (target-domain, source-domain) for one pair.

This is Notebook 01's Sections 1.2-1.7 and 1.11-1.12, generalized so it runs
identically for any pair_id in pairs_registry.csv. It deliberately stops
where Notebook 01 stopped: no feature engineering, no forecasting-target
construction for a specific horizon h (Notebook 02's job, once h is decided),
no scaler fitting. This module's only job is a leakage-safe, per-domain-
calendar-aligned panel of raw predictors plus each domain's own return series.

Local-feature publication-lag correction is currently applied to the CPI role
only (matching the one lag identified and logged so far -- decision log,
2026-09-12, "LOCAL CPI PUBLICATION-LAG ADJUSTMENT"). If a future target
country needs a lag on a different local series (e.g. a policy-rate decision
announced but not effective until later), extend `LAG_ROLES` below and add a
corresponding decision-log entry -- do not add ad hoc lags silently.
"""
from __future__ import annotations

import warnings
from dataclasses import dataclass

import numpy as np
import pandas as pd

from src.config import PairConfig
from src.calendar_align import align_to_calendar, apply_publication_lag
from src.data_sources import (
    load_local_features,
    load_shared_global,
    load_source_commodity_return,
    load_target_price,
)

LAG_ROLES = {"cpi"}  # roles that get a publication-lag shift before alignment


@dataclass
class PanelResult:
    target_panel: pd.DataFrame
    source_panel: pd.DataFrame
    n_source: int
    m_target: int

    @property
    def n_over_m(self) -> float:
        return self.n_source / self.m_target if self.m_target else float("nan")


def _apply_local_lags(local_features_raw: pd.DataFrame, cfg: PairConfig) -> pd.DataFrame:
    lagged = local_features_raw.copy()
    for role in LAG_ROLES:
        col = cfg.local_columns.get(role)
        if col is None or col not in lagged.columns:
            continue
        shifted = apply_publication_lag(local_features_raw[col], cfg.cpi_publication_lag_days)
        lagged[col] = np.nan
        common = lagged.index.intersection(shifted.index)
        lagged.loc[common, col] = shifted.reindex(common)
        dropped = shifted.index.difference(lagged.index)
        if len(dropped):
            warnings.warn(
                f"[{cfg.pair_id}] {len(dropped)} lagged '{role}' observation(s) fall outside the "
                f"loaded local-feature panel's date range and were dropped: {list(dropped)}"
            )
    return lagged


def build_domain_panels(cfg: PairConfig, save: bool = True) -> PanelResult:
    # --- target domain ---
    target_price_index = load_target_price(cfg.target_series_path)
    target_return = np.log(target_price_index).diff().dropna()
    target_return.name = "target_return"

    local_features_raw = load_local_features(cfg.local_features_path)
    local_features_lagged = _apply_local_lags(local_features_raw, cfg)

    shared_global_raw = load_shared_global(cfg.shared_global_path)

    target_calendar = target_return.index
    target_shared_aligned = align_to_calendar(
        shared_global_raw, target_calendar, cfg.shared_ffill_limits, cfg.default_shared_ffill_limit
    )
    target_local_aligned = align_to_calendar(
        local_features_lagged, target_calendar, cfg.local_ffill_limits(), cfg.default_shared_ffill_limit
    )
    target_panel = pd.concat([target_return, target_shared_aligned, target_local_aligned], axis=1)

    # --- source domain ---
    source_return = load_source_commodity_return(cfg.source_series_path, cfg.source_column)
    source_return = source_return.rename("source_return")
    source_calendar = source_return.index
    source_shared_aligned = align_to_calendar(
        shared_global_raw, source_calendar, cfg.shared_ffill_limits, cfg.default_shared_ffill_limit
    )
    source_panel = pd.concat([source_return, source_shared_aligned], axis=1)

    _run_sanity_checks(target_panel, f"{cfg.pair_id}: target_panel")
    _run_sanity_checks(source_panel, f"{cfg.pair_id}: source_panel")

    if cfg.target_eval_window_start is not None:
        assert source_panel.index.min() < pd.Timestamp(cfg.target_eval_window_start), (
            f"[{cfg.pair_id}] source_panel does not extend before target_eval_window_start -- "
            "required for Section 4.1.4 (Stage A pre-training must use only source data dated "
            "before the target evaluation window starts)."
        )
    else:
        warnings.warn(
            f"[{cfg.pair_id}] target_eval_window_start not set -- the 4.1.4 pre-training-cutoff "
            "check was skipped and must be re-run once it is fixed by Chapter 3."
        )

    if save:
        out_dir = cfg.pair_out_dir()
        target_panel.to_csv(out_dir / "target_panel.csv")
        source_panel.to_csv(out_dir / "source_panel.csv")

    return PanelResult(
        target_panel=target_panel,
        source_panel=source_panel,
        n_source=len(source_panel),
        m_target=len(target_panel),
    )


def _run_sanity_checks(df: pd.DataFrame, name: str):
    assert df.index.is_monotonic_increasing, f"{name}: index is not sorted"
    assert not df.index.duplicated().any(), f"{name}: duplicate timestamps found"
