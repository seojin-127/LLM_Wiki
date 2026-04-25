---
title: "Analyst's 6-Point Checklist for Evaluating Perturbation Models"
type: overview
created: 2026-04-25
category: overviews
tags: [checklist, evaluation, perturbation-modeling, methodology, analyst-tool, multimodal, covariates, interpretability, extrapolation, uncertainty, combinatorial]
papers:
  - single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of
  - drug-resistance/xu-2026-mapping-convergent-regulators-of
  - single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of
  - single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses
  - single-cell-foundation/cui-2024-scgpt-toward-building-foundation
  - single-cell-foundation/szalata-2026-perturbert-learning-gene-co
---

## Purpose

When you encounter a new perturbation modelling paper, this 6-point checklist provides a structured way to evaluate it. It emerged organically from one analyst's first-time reading of the Dimitrov 2026 review — the points are what *should* be present in a complete perturbation method, by working back from the user's biological question to the methodological requirements.

Use it as:
- A reading worksheet (fill in answers as you read)
- A pre-purchase sanity check before adopting a tool
- A comparison framework when choosing between methods
- A self-check when designing your own analysis

---

## The Checklist

```
□ 1. Multimodal integration
□ 2. Covariate handling
□ 3. Interpretability
□ 4. Extrapolation benchmark
□ 5. Uncertainty quantification
□ 6. Non-additive combinatorial
```

No method currently checks all six. The Dimitrov review's outlook section is essentially a wish-list for filling these gaps. Use the checklist not to find the "perfect" method (none exists) but to know what limitations you're inheriting.

---

## Point 1: Multimodal Integration

> **Question**: Does the method use multiple data modalities (RNA + ATAC + protein + spatial), or is it limited to one?

### Why it matters

A single modality (typically scRNA-seq) shows only one layer of regulation. The same cell state can be reached by different chromatin / TF / signalling routes. Without multimodal data, the model has to *infer* upstream causes from downstream effects — and that inference is fundamentally underdetermined.

### What good looks like

- **Method**: ingests ≥2 modalities natively (joint embedding, cross-modal prediction, or causal cascade)
- **Data**: ATAC + RNA + protein from same cells, ideally with spatial context

### What poor looks like

- RNA-only model claiming to infer GRNs from co-expression
- Multimodal data treated as separate analyses then combined post-hoc

### Concept page

[[concepts/multimodal-temporal-readout]] — explains the ATAC → nascent RNA → steady-state RNA cascade and why each layer captures different time windows

### Examples in our wiki

- [[drug-resistance/xu-2026-mapping-convergent-regulators-of]] (PerturbFate) — ATAC + nascent + steady-state + sgRNA in same cell ✓
- [[single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell]] (EpiAgent) — ATAC foundation model, can integrate with RNA ✓
- Most early Perturb-seq methods — RNA only ✗

---

## Point 2: Covariate Handling

> **Question**: How does the method separate the effect of perturbation from cell cycle, cell type, donor genetic background, spatiotemporal context, environmental factors?

### Why it matters

Gene effect = f(perturbation, context). If covariates are not properly disentangled, the model attributes confounding variation to the perturbation. Worse: when transferring to a new context, the contamination travels with the perturbation effect, producing wrong predictions.

### What good looks like

- **Multiple covariate axes** explicitly modeled (CPA, Biolord style)
- **Continuous covariate** support (not just discrete labels)
- **Unknown residual** captured (Biolord's "basal" component)
- **Donor / patient axis** modeled separately from cell type

### What poor looks like

- Cell type as the only covariate
- Donor as a "batch" to be removed (loses biological signal)
- Cell cycle ignored (it's a major confounder in perturbation experiments)

### Concept pages

- [[concepts/factorial-perturbation-design]] — 2×2 design as the experimental backbone
- [[overviews/endogenous-variation-as-natural-perturbation]] — why context-dependence matters

### Examples in our wiki

- [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]] (MrVI) — per-sample distance matrices ✓
- CPA, Biolord (cited in Dimitrov) — multi-component disentanglement ✓
- Most early differential expression analyses — cell type only ✗

---

## Point 3: Interpretability

> **Question**: Does the method only predict effects, or does it provide mechanistic clues about WHY the prediction was made? What in silico perturbation strategy does it use?

### Why it matters

A model that predicts "perturbing X causes Y" without explaining the mechanism cannot be trusted, validated, or extended. Different model classes give different KINDS of explanation — none give true mechanistic causality.

### What good looks like

- **Linear decoder** for gene-level attribution (scVI style)
- **Knowledge-masked latents** with explicit pathway correspondence (Spectra, ExpiMap)
- **Inferred GRN** with directional edges (CellOracle, SCENIC+)
- **Multiple consistent attribution methods** rather than relying on one

### What poor looks like

- Pure black-box transformer with only post-hoc SHAP
- Attention weights treated as if they were causal mechanisms
- "Discovered" mechanisms that match training priors (circular — see [[overviews/prior-knowledge-circular-reasoning]])

### Concept pages

- [[concepts/expressivity-interpretability-tradeoff]] — 5 strategies + comparison
- [[concepts/post-hoc-vs-during-training]] — vocabulary for when interpretability is built in vs added later

### Examples in our wiki

- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] (CellOracle) — mechanistic via inferred GRN, most interpretable ✓
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] (scGPT) — strong predictions, post-hoc interpretation ⚠
- Most foundation models — black-box with attention as proxy ⚠

---

## Point 4: Extrapolation Benchmark

> **Question**: What split was used for evaluation? What metrics? Was a simple baseline included?

### Why it matters

Almost every prediction task in single-cell perturbation is extrapolation, not interpolation. A model evaluated only on random splits has not tested its generalization claim. A model evaluated only on Pearson correlation has not tested distributional fidelity. Without baseline comparison, you can't tell if the method's complexity is justified.

### What good looks like

- **Cell-type / donor / perturbation holdout** (not random split)
- **Multiple metrics**, including at least one distributional (MMD, Wasserstein)
- **Simple linear/additive baseline** included for comparison
- **Standardized benchmark** used (PerturBench, scPerturb, OpenProblems)
- **Per-cell-type stratified results** to show where model breaks

### What poor looks like

- Only random-split Pearson r reported
- "Our method beats prior SOTA" without showing how each compares to additive baseline
- Pseudo-bulk metric only (loses heterogeneity)

### Concept pages

- [[concepts/interpolation-vs-extrapolation]] — 5 scenarios from trivial to full OOD
- [[concepts/perturbation-evaluation-design]] — split hierarchy + metrics catalog

### Examples in our wiki

- [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] (GEARS) — proper holdout for unseen perturbations ✓
- [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] (PerturbNet) — multi-axis evaluation ✓
- Many older papers — random-split only ✗

### Honest field note

[[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] flags the **generalization gap**: simple baselines often beat foundation models on extrapolation. Skepticism is warranted.

---

## Point 5: Uncertainty Quantification

> **Question**: Does the method give predictions with uncertainty bands, or only point estimates? Is uncertainty calibrated under OOD conditions?

### Why it matters

A point prediction "0.7" without uncertainty looks the same whether the model is confidently right or just guessing. For extrapolation specifically, epistemic uncertainty *should* spike when the test point is far from training distribution. Models without proper UQ confidently produce wrong answers in unseen regimes — and downstream wet-lab decisions made on those predictions will fail.

### What good looks like

- **Bayesian framework** giving posterior over predictions (GSFA, Bicycle)
- **Ensemble methods** producing prediction variance
- **Distributional output** (predicting full P(x) not just E[x])
- **Conformal prediction** for distribution-free coverage guarantees
- **Calibration tested** under OOD conditions

### What poor looks like

- Single point prediction with no uncertainty
- "Confidence" reported as model output magnitude (not actual uncertainty)
- Uncertainty calibrated only on in-distribution test data

### Concept pages

- [[concepts/uncertainty-quantification]] — aleatoric vs epistemic; calibration; methods catalog
- [[concepts/distributional-vs-point-prediction]] — distributional methods automatically provide one form of UQ

### Examples in our wiki

- GSFA, Bicycle (cited in Dimitrov) — Bayesian ✓
- Most foundation models (scGPT, scFoundation) — no proper UQ ✗
- [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] (PerturbNet) — distributional output gives some UQ ✓

### Field gap

The Dimitrov review's outlook calls UQ for extrapolation an "underexplored data property". Currently most popular methods don't do it well.

---

## Point 6: Non-Additive Combinatorial

> **Question**: Does the method handle combinations of perturbations? Which of the 5 non-additive effects can it predict (additive, synergy, buffering, suppression, redirection)?

### Why it matters

Most diseases involve multiple gene mutations. Most therapies use drug combinations. Most regulation involves cooperative TF binding. Combinatorial prediction is *the* most important open problem in perturbation modelling — and the area where current methods fail most clearly.

### What good looks like

- **Combinatorial prediction explicitly evaluated** (not just claimed)
- **Non-additive cases stratified** in evaluation (synergy/buffering/suppression/redirection separately)
- **Test combinations** held out from training (not just test perturbations)
- **Triple+ combinations** attempted (very rare)

### What poor looks like

- Single perturbation only
- Combinatorial claim with only additive cases benchmarked
- No comparison to additive baseline (definitionally cannot detect non-additivity)

### Concept page

[[concepts/combinatorial-perturbation-prediction]] — the 5 effect types + sample complexity argument + methods catalog

### Examples in our wiki

- [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] (GEARS) — defined the 5 categories, predicts pairs ✓
- CPA, MultiCPA, SAMS-VAE, AttentionPert (cited Dimitrov) — combinatorial-capable architectures ✓
- [[drug-resistance/xu-2026-mapping-convergent-regulators-of]] (PerturbFate) — combinatorial *validation* (RREB1 + KLF5 + SMAD3 inhibition) ✓
- Most single-perturbation-only methods — silent on this ✗

### Field gap

Combinatorial is where the generalization gap is *worst*. Even GEARS and similar methods give only modest improvement over additive baseline. Triple+ combinations are mostly untouched. This is the highest-impact open frontier.

---

## How To Use This Checklist

### When reading a new paper

1. Open this page alongside the paper
2. For each of the 6 points, fill in: ✓ / ⚠ / ✗ based on what the paper reports
3. Note any ✗ that's relevant to your specific use case
4. Decide whether the method's gaps are acceptable for your question

### When choosing between methods for analysis

1. Score 2–3 candidate methods on the 6 points
2. Methods that score highly on points relevant to your question win
3. Don't expect any method to score 6/6 — none currently exists

### When designing your own analysis

1. Identify which points are critical for your biological question
2. Choose method + data accordingly
3. Be explicit about which points you're sacrificing and why

### When writing your own paper

1. Address each of the 6 points in methods / discussion
2. Honest reporting on weaknesses is more credible than glossing
3. Even if your method is point-of-strength on only 1–2 axes, naming the limitations on the others builds trust

---

## What Each Point Tests Schematically

```
   Biological reality (gene effect = f(perturbation, context, time, cells)):
   
   Point 1: Multimodal       → captures upstream regulatory layers
   Point 2: Covariates       → separates context from perturbation
   Point 3: Interpretability → connects predictions to mechanism
   Point 4: Extrapolation    → generalizes beyond training distribution
   Point 5: UQ              → quantifies trust in predictions
   Point 6: Combinatorial    → handles real-world multi-perturbation cases
   
   No current method aces all six.
   The Dimitrov 2026 outlook is essentially a wish-list for filling these gaps.
```

---

## Cross-References

### Concept pages (each point's deeper treatment)

| Point | Concept page |
|-------|--------------|
| 1. Multimodal | [[concepts/multimodal-temporal-readout]] |
| 2. Covariates | [[concepts/factorial-perturbation-design]], [[overviews/endogenous-variation-as-natural-perturbation]] |
| 3. Interpretability | [[concepts/expressivity-interpretability-tradeoff]], [[concepts/post-hoc-vs-during-training]] |
| 4. Extrapolation | [[concepts/interpolation-vs-extrapolation]], [[concepts/perturbation-evaluation-design]] |
| 5. UQ | [[concepts/uncertainty-quantification]], [[concepts/distributional-vs-point-prediction]] |
| 6. Combinatorial | [[concepts/combinatorial-perturbation-prediction]] |

### Sister overview

- [[overviews/prior-knowledge-circular-reasoning]] — when prior knowledge use becomes circular reasoning, complements this practical checklist with critical-thinking framework

### Source review

- [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] — review that prompted the synthesis; its outlook section reads as the wish-list version of this checklist

---

## Origin Note

This 6-point checklist emerged organically during a study session reading the Dimitrov 2026 review. The reader, working backward from "what would I need to actually trust a perturbation prediction in my biological context?", arrived at these six axes — which turn out to map closely onto the review's outlook section but framed from the analyst's perspective rather than the model developer's. Captured here as a reusable reading tool. Points 5 and 6 were added on a second pass after reading further into the review's evaluation challenges section.
