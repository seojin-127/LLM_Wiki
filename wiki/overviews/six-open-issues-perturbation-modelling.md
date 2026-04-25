---
title: "Six Open Issues in Perturbation Modelling"
type: overview
created: 2026-04-25
category: overviews
tags: [open-issues, perturbation-modeling, multimodal, covariates, interpretability, extrapolation, uncertainty, combinatorial, methodology-map]
papers:
  - single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of
  - drug-resistance/xu-2026-mapping-convergent-regulators-of
  - single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of
  - single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses
  - single-cell-foundation/cui-2024-scgpt-toward-building-foundation
  - single-cell-foundation/szalata-2026-perturbert-learning-gene-co
---

## Where This Came From

While reading the Dimitrov 2026 review, a simple question kept surfacing: *"Wouldn't it be cleaner to just measure the data we want directly, rather than infer it through complex models?"*

That instinct hits a wall pretty quickly — measurement has limits (destructive sequencing, cost, throughput, in vivo access). So the question shifted: **given that we can't always measure exactly what we'd want, what does a model actually need to do — and what are the key challenges it faces?**

Working backward from this, six issues kept reappearing across the review's sections. They aren't a grading rubric. They're more like a map of where the field is stuck, viewed from the perspective of someone who'd prefer cleaner data but recognizes models still have to fill the gap.

---

## The Six Issues

```
1. Multimodal integration
2. Covariate handling
3. Interpretability
4. Extrapolation benchmark
5. Uncertainty quantification
6. Non-additive combinatorial
```

No current method addresses all six well. The Dimitrov review's outlook section is essentially a wish-list for filling these gaps. This page lays out each issue, why it persists, and how methods currently approach it.

---

## Issue 1: Multimodal Integration

### The challenge

A single modality (typically scRNA-seq) shows only one layer of regulation. The same cell state can arise via different chromatin / TF / signalling routes. With one modality, the model has to *infer* upstream causes from downstream effects — and that inference is fundamentally underdetermined.

### Where this hurts

GRN inference from co-expression alone is structurally weak: correlation patterns can't reliably orient causal direction. Multimodal data (ATAC + RNA + protein, ideally with spatial context) gives the model intermediate causal layers to anchor on.

### How methods currently approach this

- **Single-modality, GRN-from-coexpression**: most early Perturb-seq methods. Underdetermined.
- **Joint multimodal**: PerturbFate (ATAC + nascent + steady-state + sgRNA in same cell), EpiAgent (ATAC foundation), multi-omics integration like MOFA+. Stronger inference, but data is harder to generate.
- **Cross-modal prediction**: emerging methods that predict one modality from another (foundation-model approach).

### Concept page

[[concepts/multimodal-temporal-readout]] — explains the ATAC → nascent → steady-state cascade and why each layer captures different time windows

### Examples in our wiki

- [[drug-resistance/xu-2026-mapping-convergent-regulators-of]] — PerturbFate, full multimodal
- [[single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell]] — EpiAgent for ATAC

---

## Issue 2: Covariate Handling

### The challenge

Gene effect = f(perturbation, context). Context includes cell cycle stage, cell type, donor genetic background, spatiotemporal position, environmental factors. If covariates aren't separated from the perturbation effect, the model attributes confounding variation to the perturbation. Worse: in extrapolation to a new context, the contamination travels along.

### Where this hurts

This is the core source of irreproducibility across labs / tissues / patients. A perturbation that looks effective in one cell line may have a totally different effect in another, partly because the "effect" measured in line 1 was tangled with line 1's cell cycle / batch / state.

### How methods currently approach this

- **Cell type only as covariate**: oldest approaches; misses everything else.
- **Multi-component disentanglement**: CPA, Biolord, scDisInFact — separate axes for perturbation, cell type, donor.
- **Per-sample distance modelling**: MrVI captures donor-level heterogeneity directly.
- **Continuous covariates**: harder, less standard, but more biologically realistic.

### Concept pages

- [[concepts/factorial-perturbation-design]] — 2×2 design as the experimental backbone
- [[overviews/endogenous-variation-as-natural-perturbation]] — why context-dependence is the heart of the matter

### Examples in our wiki

- [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]] — MrVI, per-sample distance
- CPA, Biolord (cited in Dimitrov) — multi-component disentanglement

---

## Issue 3: Interpretability

### The challenge

A model that predicts "perturbing X causes Y" without explaining the mechanism is hard to trust, validate, or extend. But interpretable models (linear, knowledge-masked) tend to be less expressive. Different model classes give different KINDS of explanation — and none give true mechanistic causality at present.

### Where this hurts

For analysts, interpretability is what bridges a model's output to a biological claim. Without it, the model produces numbers that the analyst has to take on faith. With it, the analyst can ask "is this prediction biologically plausible? Can I propose a mechanism?"

### How methods currently approach this

- **Linear decoder on nonlinear encoder**: scVI-style, gives gene-level attribution while preserving expressive compression
- **Knowledge-masked latents**: Spectra, ExpiMap — force factors to align with known pathways (with the caveats from [[overviews/prior-knowledge-circular-reasoning]])
- **Mechanistic GRN**: CellOracle, SCENIC+ — explicit directional networks with in silico perturbation
- **Attention as interpretation**: scGPT, scPRINT — attention weights as TF→target proxy
- **Post-hoc attribution**: SHAP, LIME, Integrated Gradients — most flexible, least reliable

### Concept pages

- [[concepts/expressivity-interpretability-tradeoff]] — five strategies + comparison
- [[concepts/post-hoc-vs-during-training]] — vocabulary for when interpretability is built in vs added later

### Examples in our wiki

- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle, most mechanistic
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT, post-hoc attention

---

## Issue 4: Extrapolation Benchmark

### The challenge

Almost every prediction task in single-cell perturbation is extrapolation, not interpolation (in high-dim space, the convex hull is sparse). A model evaluated only on random splits has not tested its generalization claim. A model evaluated only on Pearson r has not tested distributional fidelity. Without a simple-baseline comparison, you can't tell if the model's complexity is actually doing work.

### Where this hurts

The Dimitrov review's most uncomfortable finding: simple linear/additive baselines often match or beat state-of-the-art deep learning and foundation models on unseen perturbations. This means the field has been over-trusting model performance numbers that came from too-permissive evaluation.

### How methods currently approach this

- **Random splits + Pearson r**: still common, weak.
- **Holdout by cell type / donor / perturbation**: stronger, becoming more standard.
- **Distributional metrics (MMD, Wasserstein)**: better but data-hungry.
- **Standardized benchmarks (PerturBench, scPerturb, OpenProblems)**: emerging community efforts.
- **Linear baseline comparison**: still missing in many papers; should be standard.

### Concept pages

- [[concepts/interpolation-vs-extrapolation]] — five test scenarios from trivial to full OOD
- [[concepts/perturbation-evaluation-design]] — split hierarchy + metrics catalog

### Examples in our wiki

- [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] — GEARS, proper holdout
- [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] — PerturbNet, multi-axis evaluation

---

## Issue 5: Uncertainty Quantification

### The challenge

A point prediction "0.7" looks the same whether the model is confidently right or just guessing. For extrapolation specifically, epistemic uncertainty *should* spike when the test point is far from training distribution. Models without proper UQ confidently produce wrong answers in unseen regimes — and downstream wet-lab decisions made on those predictions will fail.

### Where this hurts

This is especially dangerous because researchers naturally treat numerical predictions as having implicit precision. Without explicit uncertainty, there's no way to know which predictions to trust before spending months on follow-up experiments.

### How methods currently approach this

- **Bayesian methods**: GSFA, Bicycle — give posterior distributions over predictions
- **Ensemble methods**: train multiple models, use prediction variance
- **Distributional output**: predict P(x) rather than E[x] — naturally captures uncertainty
- **Conformal prediction**: distribution-free coverage guarantees, gaining attention
- **Most foundation models**: no proper UQ, this is a known weakness

### Concept pages

- [[concepts/uncertainty-quantification]] — aleatoric vs epistemic, calibration, methods catalog
- [[concepts/distributional-vs-point-prediction]] — distributional methods automatically provide one form of UQ

### Examples in our wiki

- GSFA, Bicycle (cited in Dimitrov) — Bayesian
- [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] — PerturbNet, distributional output gives some UQ
- Most foundation models: no proper UQ

---

## Issue 6: Non-Additive Combinatorial

### The challenge

Most diseases involve multiple gene mutations. Most therapies use drug combinations. Most regulation involves cooperative TF binding. Combinatorial prediction is *the* most important open problem in perturbation modelling — and the area where current methods fail most clearly. Sample complexity grows as N² for pairs, N³ for triples; the largest published combinatorial screen is tiny relative to the space.

### Where this hurts

Single-gene predictions are partly solved. But biology lives in combinations. Without combinatorial prediction, methods can't address the questions that matter most clinically (drug combinations, polygenic disease, gene interactions).

### How methods currently approach this

- **GEARS**: GNN with gene similarity to predict unseen combinations
- **CPA / MultiCPA**: composes perturbation latent vectors; captures non-additive via nonlinear decoder
- **SAMS-VAE**: explicit sparse additive shifts model
- **AttentionPert, State**: attention-based and foundation-model approaches
- **Linear additive baseline**: definitionally cannot detect non-additivity, but often close to deep methods on benchmarks

### Concept page

[[concepts/combinatorial-perturbation-prediction]] — five non-additive effect types (additive / synergy / buffering / suppression / redirection) + sample complexity argument + methods catalog

### Examples in our wiki

- [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] — GEARS, defined the five categories
- [[drug-resistance/xu-2026-mapping-convergent-regulators-of]] — PerturbFate combinatorial validation (RREB1 + KLF5 + SMAD3)

---

## How To Use This Page

The primary use is **as a map of the field's open challenges**. Reading it gives a sense of where models are doing well, where they're stuck, and what the Dimitrov review's outlook section is really pointing at.

Optional secondary uses:
- **As a reading lens** when working through a new perturbation modelling paper — note which issues the paper tackles and which it skips
- **As a method-selection aid** when choosing between tools for an analysis — match issues that matter for your question to method strengths
- **As a research-direction guide** when thinking about where unmet needs are biggest

It's not meant as a quality scorecard. Methods make different trade-offs based on what they prioritize, and "addressing" an issue isn't binary — it's a spectrum.

---

## What Each Issue Tests Schematically

```
   Biological reality: gene effect = f(perturbation, context, time, cells)
   
   Issue 1: Multimodal       → captures upstream regulatory layers
   Issue 2: Covariates       → separates context from perturbation
   Issue 3: Interpretability → connects predictions to mechanism
   Issue 4: Extrapolation    → generalizes beyond training distribution
   Issue 5: UQ               → quantifies trust in predictions
   Issue 6: Combinatorial    → handles real-world multi-perturbation cases
   
   No current method addresses all six well.
   The Dimitrov 2026 outlook is essentially a wish-list for closing these gaps.
```

---

## Cross-References

### Concept pages (each issue's deeper treatment)

| Issue | Concept page |
|-------|--------------|
| 1. Multimodal | [[concepts/multimodal-temporal-readout]] |
| 2. Covariates | [[concepts/factorial-perturbation-design]], [[overviews/endogenous-variation-as-natural-perturbation]] |
| 3. Interpretability | [[concepts/expressivity-interpretability-tradeoff]], [[concepts/post-hoc-vs-during-training]] |
| 4. Extrapolation | [[concepts/interpolation-vs-extrapolation]], [[concepts/perturbation-evaluation-design]] |
| 5. UQ | [[concepts/uncertainty-quantification]], [[concepts/distributional-vs-point-prediction]] |
| 6. Combinatorial | [[concepts/combinatorial-perturbation-prediction]] |

### Sister overview

- [[overviews/prior-knowledge-circular-reasoning]] — when prior knowledge use becomes circular reasoning, a critical-thinking complement to this map of open issues

### Source review

- [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] — review whose outlook section reads as the wish-list version of this open-issues map

---

## Origin Note

These six issues emerged organically during a study session reading the Dimitrov 2026 review. The starting question was simple — "wouldn't it be easier to just measure things directly?" — which led to "given that we can't always do that, what does a model need to do?" The six points are what kept reappearing as the answer. Issues 5 (UQ) and 6 (combinatorial) were added on a second pass after reading further into the review's evaluation challenges section. Captured here as a reusable mental map, not as a grading rubric.
