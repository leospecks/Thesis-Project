"""STUB -- out-of-sample forecast evaluation and result-row production.

Not yet implemented. This is the module that eventually writes rows into
results_store.py's `results` table. Responsible for:

1. Computing genuine out-of-sample metrics on the target TEST partition only
   (never validation, never train) for every tier: MAE, RMSE, out-of-sample
   R^2 (defined relative to a stated benchmark, per the project's forecast-
   evaluation instructions -- "do not claim... significantly better merely
   because RMSE is numerically lower"), and directional accuracy.
2. Diebold-Mariano-type pairwise forecast-comparison statistics between a
   given transfer tier and its comparable target-only baseline (the "crucial
   comparison" per the project's core-empirical-principle), after checking
   whether DM's assumptions (e.g. on forecast-error stationarity/dependence)
   are appropriate for this forecast design -- not applied mechanically.
3. Packaging each (pair_id, tier, seed, horizon_h, metric_name, metric_value)
   combination as a row for results_store.upsert_result / upsert_results_batch,
   including a config_hash so a rerun with different settings never silently
   overwrites a genuinely different result.
4. Never selecting which specification's numbers to report based on which
   looks most favorable (project instruction: "never selectively report
   favorable specifications").

Intended interface (subject to change once actually designed):

    def evaluate_tier(model_or_forecast, test_features, test_labels,
                       benchmark_forecast=None) -> dict: ...
    def diebold_mariano(errors_a, errors_b, **kwargs) -> dict: ...
    def build_result_rows(pair_id, tier, seed, horizon_h, metrics: dict, config_hash_val) -> list[dict]: ...
"""


def evaluate_tier(model_or_forecast, test_features, test_labels, benchmark_forecast=None):
    raise NotImplementedError(
        "evaluate.evaluate_tier: out-of-sample evaluation has not been "
        "implemented yet. Requires a trained model/forecast from stage_a/b/c "
        "or baselines, and a decided primary metric."
    )


def diebold_mariano(errors_a, errors_b, **kwargs):
    raise NotImplementedError(
        "evaluate.diebold_mariano: not yet implemented. Verify DM's assumptions "
        "against this forecast design before implementing (project instruction)."
    )


def build_result_rows(pair_id, tier, seed, horizon_h, metrics: dict, config_hash_val):
    raise NotImplementedError("evaluate.build_result_rows: not yet implemented.")
