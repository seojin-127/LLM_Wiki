---
title: "Are We Just Confirming What We Know? Prior Knowledge in Perturbation Modelling"
type: overview
created: 2026-04-25
category: overviews
tags: [prior-knowledge, GO-terms, pathway-databases, circular-reasoning, confirmation-bias, methodology-critique, validation, interpretability]
papers:
  - single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of
  - single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of
  - single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses
  - single-cell-dl/kamimoto-2023-dissecting-cell-identity-via
---

## The Question

> "We perturb genes precisely because we don't know what they do in this context. Then we use existing GO terms / pathway databases as priors when modelling the perturbation. Isn't that like asking a question while peeking at the answer key?"

This question — articulated by an attentive first-time reader of the Dimitrov 2026 review — is not naive. It identifies a real methodological tension that the field is actively grappling with. This overview explores when the concern is valid and when prior knowledge is legitimately useful.

---

## Two Roles Priors Play in Perturbation Modelling

### Role 1: Improving interpretation

After training a latent variable model, the dimensions are arbitrary numbers. To make them biologically meaningful, methods *constrain* the model so each latent factor corresponds to a known pathway:

```
Plain VAE:                       Knowledge-masked VAE:
gene_1 ──┐                       gene_1 ──┐ (TCR pathway)
gene_2 ──┼─→ latent_7             gene_2 ──┼─→ latent_7 = TCR activity
gene_3 ──┤   (uninterpretable)   gene_3 ──┘ only TCR-pathway genes
gene_4 ──┘                                   can load on this factor
```

Examples: NicheCompass, Spectra, ExpiMap, VEGA, scDoRI

### Role 2: Enhancing extrapolation

When predicting unseen perturbations, the model uses *similarity in prior databases* (gene ontology co-membership, pathway shared genes, chemical structure) to guess what an untested intervention would do:

```
Training: 100 measured perturbations + GO/pathway graph
                          ↓
Test: novel gene 101 → "GO says it shares pathway with measured genes 50, 73, 88"
                          ↓
                     Predicted effect = weighted average of (50, 73, 88) effects
```

Examples: GEARS, ChemCPA, CODEX, PrePR-CT

→ Both roles use the same fuel (prior databases), but at different stages: one in the model's structure, one in the input features.

---

## The Circular Reasoning Concern

Stripped to essentials, the user's concern:

```
Question:  What does perturbing gene X do?
              ↓
              (we don't know — that's why we perturb)
              ↓
Model uses: GO term saying "X is in pathway P"
              ↓
Model's answer: "Perturbation of X affects pathway P"
              ↓
We confirm:  ★ Is this discovery, or is this the model
                regurgitating GO?
```

If the model learns that X is in pathway P from a GO database, and then "discovers" that perturbing X affects pathway P, that's not biological discovery — it's prior reflection.

---

## What the Dimitrov Review Itself Admits

This concern is not a layperson's confusion. The review explicitly flags it (paraphrasing):

> *"the choice of priors and their inherent biases can notably influence predictions — an issue that, with some exceptions, **remains largely underexplored** in perturbation modelling"*

> *"recent findings suggest that the observed performance benefits may be attributable to **implicit network sparsity encoded by such priors rather than the biological information they contain**"*

> *"even with the incorporation of prior knowledge, gene modules often capture **indirect effects rather than genuine signalling interactions**"*

The middle quote is the most striking: priors might help **not because they encode biology**, but because they impose **sparsity** that constrains the model's hypothesis space. In other words, GO might be useful as a *regularizer* even if its biological content is partly wrong.

---

## Three Failure Modes

### (1) Confirmation bias

A model with GO priors finds patterns compatible with GO. Patterns that *don't* fit GO categories are harder to discover, because the model's hypothesis space is shaped by GO from the start.

**Symptom**: discoveries from priors-based models tend to confirm existing pathway annotations, with novel-pathway findings being rarer.

### (2) Streetlight effect

Well-studied genes have rich annotations. Under-studied genes have sparse or wrong annotations. Priors push attention toward already-studied biology, away from genes that might hold the most novel insights.

**Symptom**: the same well-known genes (TP53, MYC, NF-κB, etc.) keep showing up as "key regulators" across studies; under-annotated genes are systematically missed.

### (3) Error propagation

GO and pathway databases are imperfect — many annotations are inferred from low-evidence sources, are outdated, or transferred from other species. If the model treats them as ground truth, it inherits the errors.

**Symptom**: model predictions may be confidently wrong in ways that match documented database errors.

---

## Three Reasons to Still Use Priors

Despite the concerns, priors aren't abandoned. Three legitimate reasons:

### (1) Sample efficiency

Single-cell perturbation datasets are typically small relative to the biological question (∼100K cells, ∼100 perturbations). Pure data-driven models with millions of parameters overfit such data. Priors give the model a structured starting point.

### (2) Hypothesis space restriction

Even *imperfect* priors are useful as constraints. A model with no priors can fit anything (and overfit to anything). Priors restrict the search to biologically plausible structures.

This is why the Dimitrov review's "performance comes from sparsity, not biology" finding is not a damning verdict — sparsity is *itself* useful, just maybe not *biologically* useful in the claimed way.

### (3) Not all prior use is circular

Critically: using priors to **train** a model is different from using priors to **confirm** the model's output.

```
Circular ★:    Use GO to train → discover gene X is in GO-pathway P → "GO confirmed"

Not circular ✓: Use GO to train → predict gene X's effect in a NEW cell type
                / NEW disease / NEW drug combination → that prediction was
                NOT in GO. If experimentally validated, this is real discovery.
```

The model is allowed to use priors as **scaffolding**. The discovery is what the model produces in **new contexts** that weren't in the priors.

---

## When Priors Are Safe vs Risky

```
                            Priors SAFE                  Priors RISKY
                            ───────────                  ────────────
Well-studied system +       OK                           Risky (any "discovery"
known pathway               (saves time)                 will likely just re-confirm
                                                         GO; novelty hard to claim)

Under-studied gene +        Very risky                   Safer
novel context               (priors are sparse,          (priors are weak so data
                            may mislead direction)        drives more)

Wet-lab follow-up           Much safer                   (without validation, no
available                   (model is only                prior method's output
                            prioritization tool)          should be fully trusted)
```

---

## A Useful Analogy

Think of using prior knowledge like using a textbook when exploring a forest:

| Strategy | What it gets you | Risk |
|----------|------------------|------|
| **No textbook** (pure data-driven) | Discover anything, no bias | Wander aimlessly; fail in small forests |
| **Stay on textbook paths** (rigid prior) | Efficient navigation | Never find unmapped species |
| **Textbook + willing to leave paths** (most modern methods) | Efficient + open to discovery | Need discipline to actually leave paths |

The danger isn't using the textbook — it's **believing it where it's wrong**, or **never leaving the path**.

---

## How To Make Priors-Based Discoveries Trustworthy

The honest validation hierarchy, weakest to strongest:

| Validation level | What it shows | Strength |
|------------------|---------------|----------|
| Model agrees with GO it was trained on | Nothing — confirmation | ✗ |
| Model predictions reproducible across runs | Numerical stability | ✗ |
| Model agrees with held-out priors | Generalization within prior space | ⚠ |
| Model predicts effect in unseen context | Genuine extrapolation | ✓ |
| Wet-lab experimental validation | Independent confirmation | ✓✓ |
| Independent priors-free model agrees | Convergent evidence | ✓✓ |

For perturbation modelling specifically: **the gold standard is wet-lab validation in a context the priors did not cover**.

---

## Practical Reading Tips for Analysts

When you see a paper claiming discovery via priors-based modelling:

### (1) Was the discovered finding already in the priors?

If yes, the "discovery" is suspect — it might be GO regurgitation. Ask whether the paper compared findings against the prior database it used.

### (2) Was a no-prior baseline tested?

If the paper only tested the priors-based model, you can't tell whether priors *did the work* or *limited the discovery*. Look for: "we also trained without priors, and the result was..."

### (3) Was wet-lab validation done?

Especially for "novel" findings. Computational predictions enabled by priors *must* be validated experimentally to be credible.

### (4) Were under-studied genes excluded from claims?

Priors are sparse / wrong for under-studied biology. If the paper's conclusions focus on well-studied pathways, it's probably reflecting the priors' bias rather than discovering new biology. Ask: "Did this method find anything for the long tail of under-studied genes?"

---

## Connection to Other Wiki Content

- [[concepts/expressivity-interpretability-tradeoff]] — knowledge-masked latents are listed as one of 5 interpretability strategies; the priors discussion adds *trust* dimension to that strategy
- [[concepts/post-hoc-vs-during-training]] — priors can be applied either way; the trade-off discussion connects
- [[concepts/perturbation-evaluation-design]] — proper benchmarking should include priors-free baselines
- [[overviews/six-open-issues-perturbation-modelling]] — map of the six open challenges in perturbation modelling, complements this overview's critical-thinking approach
- [[overviews/endogenous-variation-as-natural-perturbation]] — the context-dependence framing makes priors *more* problematic (context-blind priors meet context-dependent biology)

---

## Origin Note

This overview was prompted by a study-session question while reading the Dimitrov 2026 review's section on *"Improving interpretations with prior knowledge"*. The reader observed that using existing GO/pathway databases to model perturbations whose effects we don't know feels like "asking a question while peeking at the answer key." The intuition is correct, the field acknowledges the concern, and this page formalizes the framework for thinking about when prior use is legitimate versus circular. A useful filter for future paper reading.
