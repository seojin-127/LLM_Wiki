---
title: "Perturbation Model Evaluation: Split Design and Metrics"
type: concept
created: 2026-04-25
category: concepts
tags: [evaluation, benchmarking, holdout, train-test-split, metrics, MMD, Wasserstein, Pearson, generalization-gap]
used_in:
  - single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of
  - single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of
  - single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses
  - single-cell-dl/nadig-2025-transcriptome-wide-analysis-of
---

## Two Decisions That Define an Evaluation

Every perturbation-modelling paper makes two methodological choices that, together, determine how meaningful its claimed performance is:

1. **Split design** — *which* axis is held out at training time
2. **Metric** — *how* predicted vs. observed are compared

Both can hide weaknesses if chosen permissively. Both can expose them if chosen strictly.

## Split Design Hierarchy

Sorted from easy (less generalization tested) to hard (more):

```
Random       → Cell-type   → Donor       → Perturbation → Cross-     → Cross-    → Cross-
cell split     holdout       holdout       holdout         tissue       species     modality
                                                                                         
(no split-     train: A,B,C  train: 1-7    train: P1..80   train:       train:      train:
 specific      test: D       test: 8-10    test: P81..100  brain        mouse       RNA only
 generaliza-                                                test: lung   test: human test: ATAC
 tion tested)                                                                            
```

What each split tests:

| Split | Generalization tested | Typical use case |
|-------|----------------------|------------------|
| Random cell | Cell-level reconstruction | Sanity check only |
| Cell-type holdout | Transfer across cell types | "Does this drug work in T cells if trained on B cells?" |
| Donor holdout | Patient-level generalization | "Does my model work on a new patient?" |
| Perturbation holdout | Predicting unseen interventions | "Can we skip experiments for these genes?" |
| Combinatorial holdout | Compositional generalization | "Predict A+B from singles A, B" |
| Cross-tissue / -species | Strong distribution shift | Mouse → human translation |

**Key principle**: a paper claiming to predict OOD perturbation effects but only testing on random split has not tested its claim.

## Metrics: From Permissive to Strict

| Metric | Captures | Permissive? |
|--------|---------|--------------|
| **Pearson r** (per gene) | Linear correlation predicted vs observed mean | Very permissive |
| **R²** (per gene/cell) | Variance explained | Permissive |
| **MSE / RMSE** | Squared error | Moderate |
| **Top-K DE gene recall** | Are top differentially expressed genes recovered | Moderate |
| **Effect-size cosine** | Direction of perturbation vector | Direction only, ignores magnitude |
| **MMD (Maximum Mean Discrepancy)** | Distributional similarity in RKHS | Strict |
| **Wasserstein distance** | OT-based distribution distance | Strict |
| **Energy distance** | Distributional, distribution-free | Strict |

### The "looks good on weak metrics" trap

A model that predicts a constant mean expression close to the population average can score:
- High Pearson r (because the across-gene rank ordering is roughly preserved)
- Decent R² on pseudo-bulk
- Poor MMD/Wasserstein (the distribution is wrong)

[[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] highlights this — the "generalization gap" (simple baselines beating SOTA) partly reflects suboptimal evaluation metrics:

> "Recent benchmarks reporting that simple linear or additive baselines often match or outperform state-of-the-art specialist and foundation models when predicting unseen conditions or combinatorial perturbations... Although the strong comparative performance of simple baselines may partially arise from suboptimal evaluation metrics, these results possibly reveal a core limitation."

### Pseudo-bulk vs single-cell metrics

```
Pseudo-bulk metric:                   Single-cell metric:
Average all cells in condition         Compare per-cell distribution
→ compare two means                   → MMD/Wasserstein/etc.

Pros: easy, denoised                  Pros: strict, captures heterogeneity
Cons: loses cell-to-cell variation    Cons: data-hungry, expensive
```

If a paper only reports pseudo-bulk metrics, **the heterogeneity captured by single-cell data is being thrown away in evaluation**. This is one of the field's open methodological issues.

## Standardized Benchmarks

Recent efforts to reduce arbitrary choices:

| Benchmark | What it standardizes | Reference |
|-----------|---------------------|-----------|
| **PerturBench** | Splits + metrics for genetic perturbations | Wong et al. (cited in Dimitrov) |
| **scPerturb** | Curated perturbation datasets with standard preprocessing | Peidli et al. |
| **OpenProblems** | Community challenges for many tasks | sc-best-practices |

## Practical Recommendations

When designing or reading evaluation:

1. **Match split to claim.** "Predicts unseen perturbations" requires perturbation holdout, not random split.
2. **Report multiple metrics.** Pearson r alone is insufficient. Add at least one distributional metric (MMD or Wasserstein).
3. **Compare to simple baselines.** Linear additive baseline (mean of training perturbations + perturbation mean shift) is the minimum.
4. **Check stratification.** Per-cell-type metrics often reveal where models actually break.
5. **Use established benchmarks where possible.** Custom evaluation invites optimistic reporting.

## Connection to Other Concepts

- [[concepts/interpolation-vs-extrapolation]] — what split design actually tests
- [[concepts/distributional-vs-point-prediction]] — why distributional metrics matter
- [[concepts/combinatorial-perturbation-prediction]] — combinatorial holdout is the hardest split

---

*Used in: [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] (review's evaluation challenges section), [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] (GEARS evaluation), [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] (PerturbNet OOD evaluation), [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] (TRADE — proper effect-size evaluation)*
