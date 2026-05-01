---
title: "Generative ML Models as Distribution Learners"
description: "All modern generative ML models — VAE, diffusion, flow matching, transformer — learn the same object P(data|condition); generation, batch correction, perturbation prediction, imputation, annotation are all different queries to that same distribution"
category: concepts
tags: [generative-modeling, vae, diffusion, flow-matching, transformer, distributional-thinking, mental-model]
---

## Core Insight

All modern generative ML models — VAE, diffusion, flow matching, transformer — learn the **same kind of object**: a probability distribution `P(data | condition)`. What look like four different methods are four different **training procedures** for learning the same kind of object.

Once a model has learned `P(data | condition)`, every downstream task becomes a different **query** to that distribution.

This single framing unifies a field that otherwise looks like an alphabet soup of unrelated methods.

---

## The Confusion This Resolves

A common entry-level misconception when first using tools like scVI:

> "I use scVI for batch correction. Why is everyone calling it a 'generative model'? The decoder is just there to validate that the latent is good — it's reconstruction, not generation."

This is true for plain **Autoencoders (AE)**, where the latent is a discrete blob of points and the decoder cannot produce anything outside training samples.

It is **not** true for VAE, diffusion, flow matching, or transformer models. They all learn a continuous, sampleable distribution, and the "reconstruction" of training samples is just a training procedure — the learned capability is much richer.

---

## Why Reconstruction ≠ The Goal

The training task and the model's actual learned capability are different things.

**Sculptor analogy**: a sculptor practices by carving copies of existing statues. The training task is exact replication. But after enough practice, they internalize the principles of sculpture — proportion, balance, technique. They can now carve a new statue that never existed. The training task was reconstruction; the **learned capability is the structure of statues itself**.

In ML:
- Training: VAE/diffusion/transformer practice on real cells via reconstruction-like tasks.
- Learned: the **shape of the cell distribution** in expression space.
- After training: sample from that distribution → produce new cells the model never saw.

---

## Four Paradigms, One Goal

| Method | Training task | What's actually learned |
|---|---|---|
| **VAE** (scVI) | Encode → bottleneck → decode | Latent distribution + decoder mapping; KL term forces latent to be smooth/sampleable |
| **Diffusion** | Add noise, learn to denoise step-by-step | Score function over data manifold; reverse process samples from data distribution |
| **Flow Matching** | Predict velocity along noise→data path | Vector field transporting prior to data distribution |
| **Transformer** | Mask features, predict from context | Joint conditional distribution over features (e.g., genes) |

All four converge to the same product: a learned `P(data | condition)`.

---

## Two Families: Transport vs Relational

These four paradigms cluster into two families based on **how** they reach the distribution:

### Transport-based (Diffusion + Flow Matching)
- Both learn **paths** from a prior (noise) to the data distribution.
- Diffusion = stochastic path with noise injection at each step.
- Flow Matching = deterministic path along a learned ODE velocity field.
- Recently understood as two solutions to the same underlying transport problem.
- Mental model: GPS navigation from "anywhere" to "real cell".

### Relational (Transformer)
- Learns **joint conditional dependencies** among features (genes, tokens).
- Generation = autoregressive sampling or mask-filling.
- Mental model: a graph of dependencies; given a partial observation, fill in the rest by traversing the graph.

### VAE
- Sits between: latent compression + smooth latent space.
- Often combined with one of the above (e.g., SAVE uses VAE + Flow Matching in latent space; scDiffusion uses VAE + diffusion in latent space).

These families produce the same kind of object (a learned distribution) but reach it differently — useful when picking the right tool for a task.

---

## All Tasks = Queries to the Distribution

Once a model has learned `P(cell | conditions)`, every single-cell ML task becomes a different query:

| Task | Query to the distribution |
|---|---|
| **Generation** | "Sample one cell with condition X" |
| **Batch correction** | "Re-sample this cell with batch=null" — counterfactual generation |
| **Perturbation prediction** | "Re-sample with perturbation=Y" — counterfactual generation |
| **Imputation** | "Most likely value of missing genes given observed" |
| **Cell type annotation** | "Which cell-type marginal `P(cell\|type)` is highest for this observation?" |
| **Differential expression** | "How does `P(cell\|disease)` differ from `P(cell\|control)`?" |
| **Uncertainty quantification** | "How wide is the distribution at this query?" |

This is why scVI is used for batch correction *and* generation *and* annotation *and* DE — same model, different queries.

It is also why a new "foundation model" paper claiming SOTA on annotation + batch correction + perturbation + imputation is not doing four separate things — it is showing one well-learned distribution under four queries. Performance on one task usually correlates with performance on others.

---

## Why Batch Correction Is Generative

Common misconception: scVI/VAE batch correction is just "encoding then decoding" — like data cleaning.

What's actually happening:
1. Encode cell + batch label → latent z (batch information disentangled into the conditioning slot)
2. Decode with `batch=null` (or batch=average) → produce a cell **as if** the batch effect were removed
3. The output cell was **never actually measured** — it's a counterfactual generation

"Batch-corrected" data is **generated data** representing what the cell would look like in a hypothetical batch-free condition.

Contrast: **Harmony**-style methods move points in a latent space without generating new ones. They are non-generative batch correctors. This is why Harmony cannot be used to generate new cells, predict perturbations, or impute missing values, while scVI can — they're different paradigms despite both being labeled "batch correction".

---

## Probabilistic, Not Deterministic

Classical algorithm mental model:

```
f(x) = y          deterministic mapping
```

ML mental model:

```
model = P(y | x)  → sample y ~ P(y | x)
```

Practical consequences:
- Same input → different outputs across runs (sampling variance).
- Diversity is built in: many "plausible" answers, not one correct one.
- Uncertainty is the width of the output distribution.
- Reproducibility requires fixing random seeds (which fixes the sampling, not the underlying randomness).
- "The right answer" is replaced by "the right distribution".

This is why ML results have variance, why generation gives different cells each time you call it, and why classical correctness criteria ("matches expected output") give way to distributional criteria (Wasserstein distance, MMD, FID, etc.).

---

## Practical Implications

### When picking a method
Ask: **(a)** how well does this training procedure recover `P(data | condition)` on my data type, **(b)** which queries do I care about, **(c)** what compute / interpretability / data-scale constraints apply?

Two methods with similar query results may differ wildly in interpretability, speed, or how they degrade on unseen conditions.

### When reading new papers
A new generative single-cell paper is almost always claiming: "**our training procedure recovers `P(cell | condition)` better, especially on [X] queries**." The paper's experiments are usually a battery of queries to demonstrate this. Translating each "task" into "which query is being shown" makes the contribution legible quickly.

### When evaluating model behavior
- Single-task evaluation (e.g., cell type accuracy alone) can be misleading. A good distribution model should pass multiple queries simultaneously.
- A model that generates badly typically corrects batches badly too — they share machinery.
- Variance across runs is informative: it reveals the distribution width the model has learned.

---

## Related Pages

- [[concepts/variational-autoencoder]] — VAE specifics: how the KL term enables generation
- [[concepts/distributional-vs-point-prediction]] — predicting full distribution vs mean (related but distinct: this is about output type, not learning goal)
- [[concepts/cell-level-counterfactual]] — destructive sequencing means we can't observe before/after for the same cell; batch correction & perturbation prediction generate these counterfactuals
- [[overviews/single-cell-integration-methods]] — applies this framing to compare integration paradigms (Harmony vs scVI vs WNN vs FM)
- [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] — scVI: foundational example of VAE for single-cell, demonstrating the unification (one model: batch correction, generation, DE, imputation)
- [[single-cell-dl/li-2026-save-a-generalizable-framework]] — SAVE: explicit demonstration of one model serving generation + batch correction + perturbation prediction in one framework
- [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] — Squidiff: same family as SAVE but uses diffusion (transport, stochastic path) instead of flow matching
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT: relational family (transformer with masked modeling)
- [[single-cell-dl/korsunsky-2019-fast-sensitive-and-accurate]] — Harmony: contrast — non-generative batch corrector that moves points without learning a distribution
