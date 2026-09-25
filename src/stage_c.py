"""STUB -- Stage C: supervised fine-tuning on target training data.

Not yet implemented. Takes either the raw Stage A pretrained model (-> Tier D,
"fine-tuned") or the Stage B domain-adapted model (-> Tier E, "domain-adapted
+ fine-tuned") and continues training on the target TRAINING partition's
labels, using a layer-freezing / partial-vs-full fine-tuning strategy that
has not yet been decided (see the project's transfer-learning-methods list:
"layer freezing / partial fine-tuning" vs. "full fine-tuning" are both
candidates, to be treated as one of the robustness dimensions -- "different
transfer intensity/freezing strategies" -- rather than assumed a priori).

Intended interface (subject to change once actually designed):

    def fine_tune(base_model, target_train_features, target_train_labels,
                  freezing_config, seed) -> FineTunedModel: ...
"""


def fine_tune(base_model, target_train_features, target_train_labels, freezing_config, seed):
    raise NotImplementedError(
        "stage_c.fine_tune: supervised fine-tuning has not been implemented yet, "
        "and the freezing/fine-tuning-intensity strategy has not been decided. "
        "See module docstring."
    )
