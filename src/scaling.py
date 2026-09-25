"""STUB -- feature/target scaling, fit on training data only.

Not yet implemented. Responsible for:

1. Implementing both candidate scalers from Section 4.2.3 (robust vs.
   standard) so the SCALER_TYPE diagnostic computed in Notebook 01 (Section
   1.8, pre-evaluation-window descriptive stats + QQ-plots + Jarque-Bera) can
   actually be applied, once that diagnostic has produced a decision.
2. Fitting every scaler on the TRAINING partition only (per pair, per
   scarcity variant, per rolling-origin fold where applicable) and applying
   the fitted transform to validation/test -- never fitting on the full
   sample. This is one of the most common leakage vectors named in the
   project's data-leakage-audit checklist ("normalization leakage").
3. Keeping the source-fit scaler frozen through Tiers A/C/D/E (source-trained
   family) distinct from the target-fit scaler used for Tier B (trained from
   scratch on target data only) -- these two scaler fits must not be
   conflated, since which scaler a tier uses is itself part of what the
   experiment is testing (does the transferred representation's own scaling
   matter?).

Intended interface (subject to change once actually designed):

    def fit_scaler(train_features: pd.DataFrame, scaler_type: str): ...
    def apply_scaler(scaler, features: pd.DataFrame) -> pd.DataFrame: ...
"""


def fit_scaler(train_features, scaler_type: str):
    raise NotImplementedError(
        "scaling.fit_scaler: not yet implemented. SCALER_TYPE has not been "
        "decided yet (Notebook 01, Section 1.8) -- resolve that diagnostic "
        "against real data before implementing this."
    )


def apply_scaler(scaler, features):
    raise NotImplementedError("scaling.apply_scaler: not yet implemented.")
