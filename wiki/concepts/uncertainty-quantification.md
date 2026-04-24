---
title: "Uncertainty Quantification in Deep Learning"
type: concept
created: 2026-04-24
category: concepts
tags: [uncertainty, Bayesian, ensemble, epistemic, aleatoric, calibration, deep-learning]
used_in:
  - single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of
  - single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses
  - single-cell-dl/kamimoto-2023-dissecting-cell-identity-via
  - single-cell-dl/aivazidis-2025-cell2fate-infers-rna
  - single-cell-dl/boyeau-2025-deep-generative-modeling-of
  - single-cell-dl/ergen-2024-consensus-prediction-cell
  - single-cell-dl/gorin-2025-monod-model-based-discovery
  - single-cell-dl/setty-2019-characterization-of-cell-fate
  - single-cell-dl/lange-2022-cellrank-for-directed-single
  - single-cell-dl/lopez-2018-deep-generative-modeling-for
  - single-cell-dl/nadig-2025-transcriptome-wide-analysis-of
---

## The Problem

Most deep learning models output a single answer with no indication of confidence:

```
Input → Model → "Gene A expression = 1.35"

Is the model sure? Or is this a wild guess?
→ No way to tell from the output alone.
```

This is dangerous in biology: a prediction the model is uncertain about could be treated the same as a confident one, leading to wasted experiments or wrong conclusions.

## Two Kinds of Uncertainty

```
┌──────────────────────────────────────────────────────────┐
│                   Total Uncertainty                      │
│                                                          │
│   ┌─────────────────────┐   ┌──────────────────────────┐│
│   │     Aleatoric        │   │      Epistemic           ││
│   │  (data noise)        │   │   (model ignorance)      ││
│   │                      │   │                          ││
│   │  Irreducible:        │   │  Reducible:              ││
│   │  even with perfect   │   │  more data or better     ││
│   │  model, this noise   │   │  model can shrink this   ││
│   │  remains             │   │                          ││
│   └─────────────────────┘   └──────────────────────────┘│
└──────────────────────────────────────────────────────────┘
```

### Aleatoric — "the world is noisy"

Same perturbation, same cell type → cells still respond differently. This is **biological variability**, not model failure.

- Example: knock out gene X → 80% of cells go erythroid, 20% go megakaryocyte
- You cannot reduce this by training a better model — this is how biology works
- Captured by: distributional outputs, VAE posteriors, fate probabilities

### Epistemic — "the model doesn't know"

The model has never seen this gene, this drug, or this cell type. Its prediction is a guess, and the model should say so.

- Example: GEARS predicts effect of knocking out a gene isolated in the GO graph → high epistemic uncertainty → "don't trust this prediction"
- You CAN reduce this by adding more training data for that gene
- Captured by: Bayesian weights, ensembles, MC Dropout

### Why the Distinction Matters

```
High aleatoric, low epistemic:
  "The model is confident that cells respond diversely"
  → Biology is heterogeneous. The prediction is trustworthy —
     it's telling you the truth about variability.

Low aleatoric, high epistemic:
  "The model has no idea but is giving you a single answer"
  → Dangerous! The model looks confident but isn't.
  → This is where bad experimental decisions come from.

High both:
  "The model doesn't know, AND the biology is noisy"
  → Need more data before drawing any conclusion.
```

## Methods for Estimating Uncertainty

### Method 1: Bayesian Neural Network

**Idea**: instead of learning fixed weights, learn a **distribution** over weights.

```
Standard NN:     weight w = 0.73  (fixed number)
Bayesian NN:     weight w ~ N(0.73, 0.12)  (distribution)
```

At prediction time, sample weights multiple times → get multiple predictions → their spread = uncertainty.

```
Same input, different weight samples:
  Sample 1: prediction = 1.35
  Sample 2: prediction = 1.41
  Sample 3: prediction = 1.28
  Sample 4: prediction = 1.39

  Mean = 1.36  (best guess)
  Std  = 0.05  (uncertainty)
```

If the model knows the answer well → weight distributions are narrow → predictions cluster tightly → low uncertainty.
If the model is guessing → weight distributions are wide → predictions scatter → high uncertainty.

**Measures**: primarily epistemic uncertainty.

**Used in wiki**: [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] (GEARS) — uncertainty inversely correlated with GO graph connectivity.

### Method 2: MC Dropout

**Idea**: Dropout (randomly turning off neurons) is normally used only during training to prevent overfitting. MC Dropout keeps it on during prediction too.

```
Training:  dropout ON  (standard)
Normal prediction:  dropout OFF  (standard)
MC Dropout prediction:  dropout ON  (the trick!)

  Prediction 1 (neurons 3,7 off):  1.35
  Prediction 2 (neurons 1,5 off):  1.42
  Prediction 3 (neurons 2,8 off):  1.29

  Spread of predictions = uncertainty estimate
```

- Pro: almost zero extra cost — one line of code change
- Con: theoretically approximate; tends to underestimate true uncertainty

**Measures**: primarily epistemic uncertainty (which neurons matter for this prediction).

**Used in wiki**: not explicitly used by any current wiki paper, but widely used in general deep learning.

### Method 3: Ensemble

**Idea**: train multiple models with different random initializations. If they agree, the prediction is reliable. If they disagree, uncertainty is high.

```
Model 1 (init seed 42):    1.35
Model 2 (init seed 123):   1.41
Model 3 (init seed 7):     1.38
Model 4 (init seed 999):   1.29
Model 5 (init seed 55):    1.40

Mean = 1.37  (consensus prediction)
Std  = 0.04  (uncertainty from disagreement)
```

- Pro: simple, works well in practice, often best-performing
- Con: N models = N× training cost

**Measures**: primarily epistemic uncertainty.

**Used in wiki**: [[single-cell-dl/ergen-2024-consensus-prediction-cell]] (popV) — runs multiple annotation methods, uncertainty = inter-method disagreement.

### Method 4: Distributional Output

**Idea**: instead of predicting one number, predict the **parameters of a distribution** (mean + variance), or directly sample from a learned distribution.

```
Standard model:  input → 1.35  (point estimate)
Distributional:  input → μ=1.35, σ²=0.04  (Gaussian parameters)
            or:  input → 100 samples from learned distribution
```

- Pro: directly models data variability; natural for biology
- Con: captures aleatoric uncertainty well, but NOT epistemic uncertainty (the model can be confidently wrong about the distribution)

**Measures**: primarily aleatoric uncertainty.

**Used in wiki**:
- [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] (PerturbNet) — cINN outputs full cell-state distribution
- [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] (scVI) — VAE posterior gives per-cell latent distribution
- [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]] (MrVI) — hierarchical Bayesian VAE
- [[single-cell-dl/setty-2019-characterization-of-cell-fate]] (Palantir) — per-cell fate probabilities
- [[single-cell-dl/lange-2022-cellrank-for-directed-single]] (CellRank) — directed fate probabilities with velocity uncertainty propagation

### Method 5: Fisher Information

**Idea**: after fitting model parameters, compute how "sharp" the likelihood peak is around each parameter. Sharp peak = well-determined parameter; flat peak = uncertain parameter.

```
Sharp peak (low uncertainty):     Flat peak (high uncertainty):

     ╱╲                              ╱────────╲
    ╱  ╲                            ╱            ╲
   ╱    ╲                          ╱              ╲
──╱──────╲──                   ──╱────────────────╲──
   parameter                         parameter
```

- Pro: principled, no retraining needed
- Con: only works for certain model types (parametric models with tractable likelihoods)

**Measures**: epistemic uncertainty.

**Used in wiki**: [[single-cell-dl/gorin-2025-monod-model-based-discovery]] (Monod) — Fisher information matrix for biophysical transcription parameters.

### Method 6: Statistical Testing

**Idea**: instead of asking "how uncertain is my model?", ask "how uncertain is the ground truth data?"

This is fundamentally different — it questions the **benchmark itself**, not the model.

**Used in wiki**: [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] (TRADE) — shows that Perturb-seq "ground truth" only captures 13-36% of the true transcriptome-wide impact. Before comparing any model prediction to Perturb-seq DEGs, you need to understand that the ground truth itself is uncertain.

## Comparison Table

| Method | What it measures | Extra cost | Theoretical rigor | Implementation difficulty |
|--------|-----------------|------------|-------------------|--------------------------|
| Bayesian NN | Epistemic | Medium | High | Hard |
| MC Dropout | Epistemic | Low | Approximate | Easy (1 line) |
| Ensemble | Epistemic | High (N×) | Medium | Easy |
| Distributional output | Aleatoric | Built-in | High | Medium |
| Fisher Information | Epistemic | Low (post-hoc) | High | Medium |
| Statistical testing | Measurement | Separate analysis | High | Depends |

## Who in This Wiki Has Uncertainty?

### Perturbation prediction methods

| Method | Uncertainty? | Type | How |
|--------|-------------|------|-----|
| GEARS | Yes | Epistemic | Bayesian NN |
| PerturbNet | Yes | Aleatoric | cINN distribution |
| CellOracle | Yes | Epistemic | Bayesian/bagging GRN |
| scGPT | **No** | — | — |
| scFoundation | **No** | — | — |
| PerturBERT | **No** | — | — |
| Squidiff | **No** | — | — |

### Other single-cell methods

| Method | Uncertainty? | Type | How |
|--------|-------------|------|-----|
| scVI / scANVI / MrVI / scPoli | Yes | Aleatoric | VAE posterior |
| Palantir | Yes | Aleatoric | Fate probabilities |
| CellRank | Yes | Aleatoric | Directed Markov chain |
| Cell2fate | Yes | Both | Full Bayesian ODE |
| popV | Yes | Epistemic | Ensemble disagreement |
| Monod | Yes | Epistemic | Fisher information |
| CellTypist | Yes | Aleatoric | Class probability entropy |
| TRADE | Yes | Measurement | Statistical power analysis |
| Harmony | **No** | — | — |
| SingleR | **No** | — | — |
| scTab | **No** | — | — |

### Pattern

- **VAE-based models** (scVI family) naturally provide aleatoric uncertainty through their posterior distributions
- **Probabilistic trajectory models** (Palantir, CellRank) have uncertainty built into their formulation
- **Foundation models** (scGPT, scFoundation, PerturBERT) generally do NOT provide uncertainty — this is a known gap in the field
- **Perturbation prediction**: GEARS (epistemic) and PerturbNet (aleatoric) capture complementary uncertainty types; no current method captures both simultaneously

## The Ideal (Not Yet Achieved)

```
                    Epistemic              Aleatoric
                 (model ignorance)      (biological noise)
                        │                      │
                        ▼                      ▼
              "I haven't seen           "Cells genuinely
               this gene before"        respond diversely"
                        │                      │
                        └──────┬───────────────┘
                               │
                    Combined uncertainty score
                               │
                    "Here's my prediction,
                     and here's how much
                     you should trust it,
                     broken down by source"
```

No perturbation prediction method in this wiki provides both types simultaneously. GEARS gives epistemic only; PerturbNet gives aleatoric only. A complete solution would decompose total uncertainty into both components — telling the user whether the uncertainty comes from model ignorance (fixable with more data) or biological variability (inherent).

---

*Used in: [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]], [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]], [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]], [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna]], [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]], [[single-cell-dl/ergen-2024-consensus-prediction-cell]], [[single-cell-dl/gorin-2025-monod-model-based-discovery]], [[single-cell-dl/setty-2019-characterization-of-cell-fate]], [[single-cell-dl/lange-2022-cellrank-for-directed-single]], [[single-cell-dl/lopez-2018-deep-generative-modeling-for]], [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]]*
