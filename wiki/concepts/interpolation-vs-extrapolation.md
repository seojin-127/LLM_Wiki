---
title: "Interpolation vs Extrapolation in Single-Cell Perturbation Modelling"
type: concept
created: 2026-04-25
category: concepts
tags: [interpolation, extrapolation, OOD, generalization, convex-hull, evaluation, perturbation-prediction]
used_in:
  - single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of
  - single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of
  - single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses
  - single-cell-dl/he-2026-squidiff-predicting-cellular-development
---

## Strict ML Definition

Given training data points $\{x_1, x_2, \ldots, x_n\}$ in some feature space:

- **Interpolation**: query point $x_*$ lies *inside* the convex hull of training data
- **Extrapolation**: query point $x_*$ lies *outside* the convex hull

```
                                    ┌──── extrapolation
        x ────── x                   │
       /          \      x*  ←──────┘
      x   x*       x  
     /              \
    x ──── x ─────── x  
                ↑
                interpolation
```

Convex hull = the smallest convex region enclosing all training points.

## Why "Interpolation" Is Almost Never Useful in Single-Cell

In high-dimensional spaces (single-cell readouts have ~20,000 gene dimensions), the convex hull is **extremely sparse**. Almost every new observation lies outside it. So "interpolation" as a strict concept rarely applies — what looks like interpolation in low-dim visualizations (UMAP) is actually extrapolation in the underlying high-dim space.

Practical consequence: **almost all prediction tasks in single-cell perturbation modelling are extrapolation**, regardless of what the paper calls them.

## Five Scenarios in Single-Cell Perturbation

Given axes (perturbation × cell_type × donor × time × drug × ...), test scenarios fall into these categories:

| Scenario | Strict label | Common name in lit |
|----------|-------------|-------------------|
| Seen perturb × seen context | Trivial reconstruction | "Reconstruction" / "in-distribution" |
| Seen perturb × **new** context (cell type, donor) | Extrapolation | **Context transfer** |
| **New** perturb × seen context | Extrapolation | **Unseen perturbation** |
| **New** perturb × **new** context | Hard extrapolation | **Full OOD** |
| Seen single perturbs → predict their **combination** | Extrapolation | **Combinatorial** ([[concepts/combinatorial-perturbation-prediction]]) |

[[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] Table 2 splits the perturbation-prediction task as Seen / Unseen / Combinatorial / Context — all of these are forms of extrapolation along different axes.

## Why It Matters: The Evaluation Trap

A model evaluated on "interpolation" (in-distribution test set, random split) often looks great. The same model evaluated on extrapolation (held-out cell type, donor, or perturbation) often degrades sharply.

The **generalization gap** flagged in [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] — simple baselines beating SOTA on unseen perturbations — is fundamentally an extrapolation phenomenon. Models that learn confounder-correlated representations during training can match the training distribution perfectly but fail when the test distribution shifts.

## Practical Reading Tip

When a paper claims "our model predicts perturbation effects":

1. **Check the test split.** Random split → mostly interpolation. Cell-type / donor / perturbation holdout → real extrapolation.
2. **Read the holdout strategy carefully.** "Held-out genes" can mean two things — held out at training time entirely, or held out only from the test query (with training data still containing them). The first is real extrapolation; the second is closer to interpolation.
3. **Look for OOD evaluation.** If a paper only reports random-split metrics, it has not tested generalization.

See [[concepts/perturbation-evaluation-design]] for full discussion of split designs and metrics.

---

*Used in: [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] (review's central evaluation framing), [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] (GEARS, unseen perturbation extrapolation), [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] (PerturbNet, unseen drug/genetic perturbation), [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] (Squidiff, unseen condition prediction)*
