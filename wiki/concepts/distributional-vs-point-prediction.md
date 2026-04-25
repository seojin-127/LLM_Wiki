---
title: "Distributional vs Point Prediction in Single-Cell Models"
type: concept
created: 2026-04-25
category: concepts
tags: [distributional-prediction, conditional-generative-model, counterfactual, heterogeneity, flow-matching, diffusion, normalizing-flow]
used_in:
  - single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses
  - single-cell-dl/he-2026-squidiff-predicting-cellular-development
  - single-cell-dl/klein-2025-mapping-cells-through-time
  - single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of
---

## Two Different Prediction Targets

When a model predicts cellular response to perturbation, it can target:

```
POINT prediction:                  DISTRIBUTIONAL prediction:
Mean expression vector E[x]        Full distribution P(x)
                                                                
"After this perturb, average        "After this perturb, 30% of cells
 expression of gene Y is 5.2"        will have Y > 8, 50% near 5,
                                     20% will have Y < 2"
                                                                
1 vector per condition              probability density per condition
```

These are fundamentally different statistical objects. Point prediction is what most early methods do (mean of perturbed cells); distributional prediction is the recent frontier.

## Why Mean Prediction Loses Critical Information

Cell-to-cell heterogeneity within a single perturb-context combination is **biologically real**, not noise:

- **Responder vs non-responder**: same perturbation → some cells reorganize chromatin and dedifferentiate, others escape entirely
- **Stochastic state transitions**: developmental decisions often involve probabilistic commitment
- **Intrinsic GRN noise**: bursty transcription means single cells visit different attractor states
- **Latent cell-state heterogeneity within annotated populations**: "T cells" actually contains exhausted, naive, memory subsets that respond differently

Averaging across these subpopulations loses the signal that *is* the phenomenon.

```
True distribution:        Mean prediction sees:
●●●●●  ●●●●●              ●●●●●●●●●●  
"bimodal: half escape,    "moderate average response"
 half respond fully"      
                          → If you treat 100 patients,
                            mean ≠ what any patient experiences
```

## Why Distributional Prediction Matters Clinically

If 30% of cells fully respond and 70% don't, that's clinically very different from "100% of cells partially respond" — even though the means are identical. Distributional prediction directly answers:

- "What fraction of cells will go into resistant state X?"
- "How many patients out of 100 will respond strongly?"
- "Is this drug a partial response in everyone, or a full response in some?"

## Methods That Predict Distributions

| Method | Mechanism | Wiki page |
|--------|-----------|-----------|
| **PerturbNet** | conditional Invertible Neural Network (cINN), models full distribution | [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] |
| **Squidiff** | conditional denoising diffusion, captures transient distributions | [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] |
| **moscot** | optimal transport, maps source distribution → target distribution | [[single-cell-dl/klein-2025-mapping-cells-through-time]] |
| **CFGen** | conditional flow generation | (cited in Dimitrov 2026) |
| **MFM / MMFM** | (multi-marginal) flow matching | (cited in Dimitrov 2026) |
| **CellFlow** | OT + neural ODE for distribution-level transfer | (cited in Dimitrov 2026) |
| **scDiffusion** | diffusion-based generation | (cited in Dimitrov 2026) |

Common architectural choices: VAE, normalizing flow, diffusion, optimal transport. All can in principle generate from $P(x \mid \text{condition})$ rather than just $E[x \mid \text{condition}]$.

## Counterfactual Distributions

Pearl-style counterfactual reasoning at the distributional level:

$$P(x \mid do(\text{perturb}), \text{context})$$

This is the formal target of perturbation prediction. Methods differ in what they actually optimize:

- **Mean estimators** target $E[x \mid do(\text{perturb}), \text{context}]$
- **Distributional estimators** target the full $P(x \mid do(\text{perturb}), \text{context})$
- **OT-based** methods construct a coupling between control distribution and perturbed distribution, allowing counterfactuals at the level of (cell → its hypothetical perturbed self)

[[concepts/multimodal-temporal-readout]] connects: nascent + steady-state RNA together can resolve directional dynamics (RNA velocity), giving distributional methods richer training signal for state transitions.

## Evaluation Challenges

Distributional prediction is harder to evaluate than point prediction:

| Challenge | Implication |
|-----------|-------------|
| Need many cells per condition for ground truth distribution | Limits applicability to data-rich settings |
| Distributional metrics (MMD, Wasserstein) are computationally expensive | Slower benchmarking |
| Sparse, noisy single-cell counts make distribution estimation noisy | Lower SNR than pseudo-bulk |
| No single agreed-upon metric | Method comparison is inconsistent |

See [[concepts/perturbation-evaluation-design]] for metric details.

## Limitations of Current Methods

Despite the conceptual appeal:

- Most distributional methods still suffer from the same **generalization gap** as point methods on unseen perturbations
- Computational cost makes scaling to genome-wide perturbations hard
- Identifying *which* cells will respond vs not (rather than just the proportion) is still mostly out of reach
- The training data itself often lacks the depth needed to estimate within-condition distributions properly (small N per condition)

## Practical Reading Tip

When a paper claims "predicts perturbation effect":

1. **Check what is predicted.** Mean expression vector? Full per-cell distribution? Effect direction?
2. **Check evaluation metric.** Pearson on means → point prediction. MMD/Wasserstein → distributional.
3. **Check number of cells per condition.** Distributional claims with <100 cells per condition are statistically weak.

## Part of broader synthesis

- [[overviews/six-open-issues-perturbation-modelling]] — distributional output is one form of **Issue 5: Uncertainty Quantification** (predicting P(x) rather than E[x] naturally captures within-condition heterogeneity); also relates to **Issue 4: Extrapolation Benchmark** (distributional metrics like MMD/Wasserstein are stricter)
- [[concepts/cell-level-counterfactual]] — cell-level counterfactual goes one step further than distributional comparison: uses distributional input to produce individual-level mapping

---

*Used in: [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] (PerturbNet — explicit distributional via cINN), [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] (Squidiff — diffusion-based distributional), [[single-cell-dl/klein-2025-mapping-cells-through-time]] (moscot — OT-based distribution mapping), [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] (review's population-tracing concept covers this category)*
