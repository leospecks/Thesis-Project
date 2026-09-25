"""STUB -- feature engineering and forecasting-target construction.

Not yet designed. This module is responsible for:

1. Defining the forecasting target r_{t+h} for a specific, decided horizon h
   (Chapter 4.1 notation) from each domain's panel's return column. Blocked
   on `cfg.horizon_h` being set in configs/global_config.yaml (Section 3.6
   sample-size justification) -- see run_pair.py, which refuses to call this
   module while horizon_h is None.
2. Constructing predictor features (lags, rolling windows, technical
   indicators) from each domain's aligned panel (Section 4.2.2), using ONLY
   information available at each forecast origin t -- any lookback window
   must not reach across the train/validation/test boundary once that
   boundary is defined in splits.py.
3. Producing the shared-core feature matrix and the target-only local
   feature matrix separately (so Tier B-restricted vs. B-full in
   evaluate.py can select which one to use), per the 2026-09-12 decision
   that local-equity-return is target-only, not shared-core.

Intended interface (subject to change once actually designed):

    def build_target_features(panel: pd.DataFrame, horizon_h: int) -> pd.DataFrame: ...
    def build_source_features(panel: pd.DataFrame, horizon_h: int) -> pd.DataFrame: ...

Do not call this module until horizon_h is decided -- constructing r_{t+h}
for a placeholder h and forgetting to redo it later is a silent
methodological error, not a convenience.
"""


def build_target_features(panel, horizon_h: int):
    raise NotImplementedError(
        "features.build_target_features: feature engineering and target-horizon "
        "construction have not been designed yet (deferred from Notebook 01; see "
        "this module's docstring). Requires horizon_h to be decided first."
    )


def build_source_features(panel, horizon_h: int):
    raise NotImplementedError(
        "features.build_source_features: not yet designed. See module docstring."
    )
