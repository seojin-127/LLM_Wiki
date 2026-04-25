---
title: "Combinatorial Perturbation Prediction: Non-Additive Effects and Methods"
type: concept
created: 2026-04-25
category: concepts
tags: [combinatorial-perturbation, non-additive-effects, synergy, buffering, suppression, redirection, GEARS, CPA, drug-combination]
used_in:
  - single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of
  - single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of
  - single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses
  - drug-resistance/xu-2026-mapping-convergent-regulators-of
---

## The Problem

Given measured single-perturbation effects (knock down gene A alone, knock down gene B alone), can we predict the joint effect of A+B together?

If biology were additive, this would be trivial: $\text{effect}(A+B) = \text{effect}(A) + \text{effect}(B)$. Empirically, biology is often **not additive** — and the non-additivity is precisely the signal of interest (for drug combinations, genetic interactions, epistasis).

## Five Types of Non-Additive Effects (GEARS taxonomy)

[[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] formalized the categories:

```
Single A:    ▲▲▲░░░░░░░
Single B:    ░░▲▲▲░░░░░
                          Predicted from singles    Observed (actual combination)
                          (linear additive)
                          
Additive       ▲▲▲▲▲░░░░  →   ▲▲▲▲▲░░░░░          [no surprise; baseline]
Synergy        ▲▲▲▲▲░░░░  →   ▲▲▲▲▲▲▲▲░░          [combination > sum]
Buffering      ▲▲▲▲▲░░░░  →   ▲▲░░░░░░░░          [combination < sum]
Suppression    ▲▲▲▲▲░░░░  →   ░░░░░░░░░░          [near-zero despite singles]
Redirection    ▲▲▲▲▲░░░░  →   ░░░░░░▲▲▲▲          [different gene set affected]
```

**Why each matters biologically**:

| Type | Biological interpretation |
|------|--------------------------|
| **Additive** | Independent pathways, no interaction |
| **Synergy** | Cooperative regulation (drug combination opportunity) |
| **Buffering** | Functional redundancy or compensation |
| **Suppression** | One gene gates the other's effect |
| **Redirection** | Combinatorial recruits a third pathway absent in singles |

Synergy is what drug combination therapy hopes to find. Buffering/suppression explains why some single-gene therapies fail. Redirection is the rarest and most interesting.

## Why Combinatorial Is Fundamentally Hard

### Sample complexity

| Order | Number of combinations | Realistic to measure |
|-------|----------------------|---------------------|
| Singles | $N$ (∼20,000 genes) | Yes, with Perturb-seq |
| Pairs | $N^2/2$ (∼200M for genome-wide) | Only ∼100–1000 measured |
| Triples | $N^3/6$ (∼1.3T) | Almost never measured |
| Higher | Combinatorial explosion | Untestable |

The **largest published genetic combinatorial screen** (Norman 2019) covered ∼300 pairs from ∼100 genes. This is rounding error compared to all possible combinations.

### Non-additivity is the signal

If you only have singles data, you fundamentally cannot predict non-additive combinations without an additional inductive bias. Linear/additive baseline is **definitionally** unable to predict synergy/buffering/suppression/redirection.

So combinatorial prediction is harder than single perturbation prediction *in kind*, not just degree.

## Methods That Attempt Combinatorial Prediction

| Method | Strategy | Wiki |
|--------|----------|------|
| **GEARS** | GNN message passing + GO/coexpression similarity to learn interaction patterns from training combos | [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] |
| **CPA / MultiCPA** | Compose perturbation vectors in latent space (additive in latent → nonlinear after decoder) | (cited Dimitrov) |
| **SAMS-VAE** | Sparse Additive Shifts model — explicit combinatorial structure | (cited Dimitrov) |
| **AttentionPert** | Attention over perturbations to learn pairwise interactions | (cited Dimitrov) |
| **PerturbNet** | Modular cINN composes chemical/genetic embeddings | [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] |
| **PRNet, SALT&PEPER** | Graph-based and sequence-based combinatorial models | (cited Dimitrov) |
| **State** | Foundation model with combinatorial context | (cited Dimitrov, recent) |

Common architectural pattern: **learn the perturbation embedding such that algebraic operations in embedding space correspond to combinatorial effects**. The hope is that synergy/buffering/etc. emerge as predictable patterns from training data.

## The Generalization Gap Bites Hardest Here

[[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]]:

> "Recent benchmarks reporting that simple linear or additive baselines often match or outperform state-of-the-art specialist and foundation models when predicting unseen conditions or **combinatorial perturbations**."

Specifically on Norman 2019:
- Additive baseline gives reasonable performance
- GEARS, CPA, and foundation models give *small* improvements
- Synergy/buffering/redirection remain hard
- Triple+ combinations are mostly untouched

**Interpretation**: current methods learn "average" combinatorial behavior but struggle with the rare, biologically interesting non-additive patterns — which are precisely the cases that justify combinatorial prediction in the first place.

## Connection to Drug Combination Therapy

Combinatorial prediction in single-cell biology is the same conceptual problem as **drug combination prediction** in oncology:

- Synergy → "combination index < 1" in pharmacology (Bliss/Loewe synergy)
- Buffering → resistance mechanism
- Suppression → drug antagonism
- Redirection → off-target combinatorial effect

Methods cross-pollinate: drug combination predictors (DeepSynergy, etc.) and single-cell perturbation predictors (GEARS, CPA) share architectural ideas.

[[drug-resistance/xu-2026-mapping-convergent-regulators-of]] (PerturbFate) uses combinatorial *validation* — combining RREB1 KD + KLF5 inhibitor + SMAD3 inhibitor to test the cooperative TF hub hypothesis. The 3-way combination produced 3.1× more reduction than any single intervention — which is precisely the kind of synergy combinatorial methods aim to predict.

## Why This Is the Most Important Open Problem

Single perturbation effects are partially solved. Combinatorial effects are where biology lives:

- Most diseases involve multiple gene mutations
- Most drug therapies use combinations
- Most cellular regulation involves cooperative TF binding
- Most epistasis is combinatorial by definition

Yet combinatorial prediction is **the area where current models fail most clearly**. A breakthrough here would be the highest-impact advance in the field.

## Practical Reading Tip

When a paper claims "predicts combinatorial perturbations":

1. **Check the order.** Pairs are routine claims; triples and higher are extraordinary.
2. **Check the holdout strategy.** "Train on singles, test on pairs" is much harder than "train on some pairs, test on other pairs".
3. **Check non-additivity capture.** Predicting additive cases well is trivial; the real test is synergy, buffering, suppression, redirection.
4. **Compare to additive baseline.** If the paper doesn't show this comparison, treat the claim with caution.

## Connection to Other Concepts

- [[concepts/interpolation-vs-extrapolation]] — combinatorial is the most demanding extrapolation
- [[concepts/perturbation-evaluation-design]] — combinatorial holdout is the strictest split
- [[concepts/distributional-vs-point-prediction]] — combinatorial effects often manifest at distribution level (e.g., subpopulation emerges)
- [[concepts/expressivity-interpretability-tradeoff]] — non-additive interactions require nonlinear models, sacrificing interpretability
- [[concepts/factorial-perturbation-design]] — 2×2 design is the experimental backbone for measuring combinatorial effects

## Part of broader synthesis

- [[overviews/six-open-issues-perturbation-modelling]] — this concept directly addresses **Issue 6: Non-Additive Combinatorial** (the area where current methods fail most clearly per Dimitrov; sample complexity argument is core)
- [[overviews/convergent-regulation-across-systems]] — combinatorial perturbation is what reveals convergent TF hubs (e.g., RREB1+KLF5+SMAD3 in PerturbFate); validation of convergent regulation requires combinatorial intervention

---

*Used in: [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] (GEARS — defined the 5 non-additive categories), [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] (review's combinatorial section), [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] (PerturbNet — combinatorial via composition), [[drug-resistance/xu-2026-mapping-convergent-regulators-of]] (PerturbFate — combinatorial validation experiment)*
