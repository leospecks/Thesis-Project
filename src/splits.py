"""STUB -- chronological train/validation/test splitting and the rolling-origin scheme.

Not yet implemented. Responsible for:

1. Chronological (never shuffled) train/validation/test partitioning of the
   target-domain feature matrix, respecting cfg.target_eval_window_start
   once it is fixed by Chapter 3 -- nothing at or after that date may
   influence any modeling choice (project instruction: time-series validity).
2. The nested rolling-origin (expanding- or rolling-window) validation
   scheme referenced in Chapter 4.7.1, used for hyperparameter selection
   without touching the final test window.
3. The data-scarcity experiment design (Chapter 4's data-scarcity section):
   several TARGET TRAINING-HISTORY LENGTHS defined chronologically (shorter
   training windows, never a random subsample of rows -- randomly
   subsampling time-series observations would break temporal structure and
   is explicitly disallowed by the project instructions).
4. Enforcing that Stage A (source pretraining, see stage_a.py) only uses
   source-domain observations dated strictly before
   cfg.target_eval_window_start (Section 4.1.4), and that Stage B (domain
   adaptation, see stage_b.py) only uses the target TRAINING partition, never
   validation or test.

Intended interface (subject to change once actually designed):

    def make_target_splits(features: pd.DataFrame, eval_window_start) -> SplitIndices: ...
    def make_scarcity_variants(train_index: pd.DatetimeIndex) -> dict[str, pd.DatetimeIndex]: ...
    def make_rolling_origin_folds(train_index: pd.DatetimeIndex, ...) -> list[Fold]: ...
"""


def make_target_splits(features, eval_window_start):
    raise NotImplementedError(
        "splits.make_target_splits: chronological split design has not been "
        "implemented yet. See module docstring for the required properties."
    )


def make_scarcity_variants(train_index):
    raise NotImplementedError(
        "splits.make_scarcity_variants: data-scarcity training-history variants "
        "have not been designed yet. Must use chronologically shorter training "
        "histories, never a random row subsample (project instruction)."
    )


def make_rolling_origin_folds(train_index, **kwargs):
    raise NotImplementedError(
        "splits.make_rolling_origin_folds: the nested rolling-origin validation "
        "scheme (Chapter 4.7.1) has not been implemented yet."
    )
