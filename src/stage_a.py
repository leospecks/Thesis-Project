"""STUB -- Stage A: source-domain pretraining.

Not yet implemented. Trains the shared architecture (architecture.py) on the
SOURCE domain's features/target only, using ONLY source observations dated
strictly before cfg.target_eval_window_start (Section 4.1.4 pre-training
cutoff -- enforced structurally in splits.py, not just by convention here).

Produces the pretrained weights consumed by:
  - Tier C (zero-shot: applied directly to target, no further training),
  - Tier D (fine-tuned: further trained on target data),
  - Tier E (domain-adapted + fine-tuned: Stage B's adaptation applied first).

Intended interface (subject to change once actually designed):

    def train_stage_a(source_features, source_target, architecture_config, seed) -> PretrainedModel: ...
"""


def train_stage_a(source_features, source_target, architecture_config, seed):
    raise NotImplementedError(
        "stage_a.train_stage_a: source-domain pretraining has not been "
        "implemented yet. Requires features.py, splits.py, scaling.py, and "
        "architecture.py to be implemented first."
    )
