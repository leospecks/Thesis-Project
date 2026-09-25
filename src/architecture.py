"""STUB -- model architecture definition, sized once and shared across tiers.

Not yet implemented. Responsible for:

1. Defining the single model architecture class used across every tier that
   needs a trainable network (A family, C, D, E) -- per the 2026-09-16
   decision-log entry ("architecture capacity fixed once and shared across
   tiers", Section 4.2.1/4.7.2), so that a performance difference between
   tiers cannot simply reflect one tier getting a bigger/smaller model.
2. Justifying the architecture's capacity against the SMALLER of the two
   domains' available sample sizes (m, target), not the larger (n, source) --
   per the project's model-complexity instructions: "always consider whether
   sample size supports the proposed architecture," "prefer parsimonious
   architectures when target data are limited."
3. Providing hooks for Stage B's domain-adaptation mechanism (e.g. a
   penultimate feature layer for MMD, or a gradient-reversal layer for DANN,
   depending on which adaptation method is eventually chosen -- see
   stage_b.py) without those hooks changing the base architecture's capacity
   for the tiers that do not use them.

Intended interface (subject to change once actually designed):

    def build_model(input_dim: int, config: dict): ...
"""


def build_model(input_dim: int, config: dict):
    raise NotImplementedError(
        "architecture.build_model: not yet designed. Architecture capacity must "
        "be justified against the target (smaller) sample size m, not the source "
        "sample size n -- see module docstring."
    )
