"""STUB -- Stage B: unsupervised domain adaptation on the target training partition.

Not yet implemented, and the specific adaptation mechanism (MMD discrepancy
minimization, adversarial/DANN, parameter regularization toward the Stage A
parameters, or another candidate from the project's transfer-learning-methods
list) has not been chosen. Whichever is chosen must be justified against the
5-point checklist in the project instructions for every proposed method:
(1) what knowledge is being transferred, (2) why it is economically
transferable, (3) what source-target differences could cause negative
transfer, (4) how this adaptation step addresses those differences, (5) what
empirical comparison (Tier D vs. Tier E) would demonstrate its value added.

Restricted, by construction, to the TARGET TRAINING partition only (never
validation or test) -- this is unsupervised adaptation to the target's
feature DISTRIBUTION, not fitting to target labels, so it must not leak
information from the target evaluation window either.

Intended interface (subject to change once a method is chosen):

    def adapt_stage_b(pretrained_model, target_train_features, method_config, seed) -> AdaptedModel: ...
"""


def adapt_stage_b(pretrained_model, target_train_features, method_config, seed):
    raise NotImplementedError(
        "stage_b.adapt_stage_b: domain-adaptation method has not been chosen or "
        "implemented yet (candidates: MMD, DANN, parameter regularization toward "
        "source -- see module docstring). Must be justified via the project's "
        "5-point transfer-method checklist before implementation."
    )
