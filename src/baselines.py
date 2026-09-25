"""STUB -- baseline / benchmark models (Tier A family + supplementary RF).

Not yet implemented. Per the project's core-empirical-principle and baselines
instructions, the transfer models must never be compared only against weak
baselines. This module owns the full Tier A family plus the supplementary
non-neural benchmark:

  - naive/simple forecasting benchmarks (e.g. historical mean, random walk --
    applicability depends on whether the target is a return or a price level;
    see Chapter 4.1's prices-vs-returns distinction, already fixed for this
    pipeline: the target is a log-return, not a level),
  - AR/ARIMA-type or linear predictive-regression benchmarks trained on
    target data only,
  - the same shared architecture (architecture.py) trained FROM SCRATCH on
    target data only, using EITHER the shared-core-only feature set
    (Tier B-restricted) OR the full target-only feature set including local
    variables (Tier B-full) -- these two variants isolate whether local
    features (FX/CPI/policy rate/local-equity-return) add value independent
    of transfer,
  - a supplementary Random Forest, per the project's baseline-families list.

Each of these is a "model trained from scratch using target-market data
only" (baseline family B, per the project's core-empirical-principle) and
therefore also the answer to whether Tier D/E's improvement (if any) comes
from TRANSFER rather than simply from a better model class.

Intended interface (subject to change once actually designed):

    def naive_benchmark(target_train_series, method="historical_mean"): ...
    def ar_benchmark(target_train_features, target_train_labels, order): ...
    def train_target_only(target_train_features, target_train_labels,
                           feature_set, architecture_config, seed): ...
    def random_forest_benchmark(target_train_features, target_train_labels, seed): ...
"""


def naive_benchmark(target_train_series, method: str = "historical_mean"):
    raise NotImplementedError("baselines.naive_benchmark: not yet implemented.")


def ar_benchmark(target_train_features, target_train_labels, order):
    raise NotImplementedError("baselines.ar_benchmark: not yet implemented.")


def train_target_only(target_train_features, target_train_labels, feature_set,
                       architecture_config, seed):
    raise NotImplementedError(
        "baselines.train_target_only: Tier B (restricted/full) has not been "
        "implemented yet. Requires features.py, splits.py, scaling.py, and "
        "architecture.py to be implemented first."
    )


def random_forest_benchmark(target_train_features, target_train_labels, seed):
    raise NotImplementedError("baselines.random_forest_benchmark: not yet implemented.")
