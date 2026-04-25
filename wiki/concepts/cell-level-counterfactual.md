---
title: "Cell-Level Counterfactual: Pairing Cells Across Conditions via Optimal Transport"
type: concept
created: 2026-04-25
category: concepts
tags: [counterfactual, optimal-transport, OT, destructive-sequencing, cell-pairing, lineage, Waddington, moscot, CINEMA-OT, flow-matching]
used_in:
  - single-cell-dl/klein-2025-mapping-cells-through-time
  - single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of
  - drug-resistance/xu-2026-mapping-convergent-regulators-of
---

## The Core Problem

Single-cell sequencing is **destructive**. To read a cell's transcriptome, you have to dissociate and lyse it. The cell never lives to be measured a second time. This means:

```
What we WANT to observe:        What we CAN observe:
                                                
Same cell:                      Different cells:
   [t=0]                            Cell A: [time of harvest] ──→ dead
      ↓ perturb                     Cell B: [time of harvest] ──→ dead
   [t=1]                            Cell C: [time of harvest] ──→ dead
   ↑ paired observation             ↑ unpaired snapshots
```

Every cell is observed exactly once. **There is no within-cell before/after.**

This is the fundamental obstacle that gives rise to all of single-cell perturbation modelling. Methods exist precisely *because* the data we'd ideally want — paired observations of the same cell — cannot be obtained.

## Three Levels of "Counterfactual" Inference

Given two populations (e.g., control cells and perturbed cells), we can compare them at three increasingly refined levels:

```
LEVEL 1 — Point estimate (mean shift)
─────────────────────────────────────
   Mean(control) ────→ Mean(perturbed)
   
   Output: 1 vector
   "On average, perturbation shifts expression this way"
   
   Misses: heterogeneity, subpopulations, individual variation


LEVEL 2 — Distributional comparison
─────────────────────────────────────
   P(control)  ←→  P(perturbed)
   
   Output: distance/similarity score (MMD, Wasserstein)
   "These two distributions differ by this much, in this shape"
   
   Captures: bimodality, variance change, escape populations
   Still misses: which specific cell maps to which


LEVEL 3 — Cell-level counterfactual (OT)
─────────────────────────────────────
   Each control cell ●ᵢ ──→ predicted perturbed cell ◉ⱼ
   
   Output: cell-to-cell coupling (transport plan)
   "This specific control cell, if perturbed, would have become
    this specific perturbed cell (or this mixture of perturbed cells)"
   
   Captures: per-cell counterfactual estimates
```

Cell-level counterfactual goes **one step further** than distributional. It uses distributional matching to produce **individual-level predictions**.

## Why This Is BOTH Distributional and Individual

The user's intuitive question — "이것도 분포의 컨셉이라고?" — has a precise answer: **yes, but it produces individual-level output.**

The mechanism:
- Input: full distribution of control cells, full distribution of perturbed cells
- Algorithm: match cells across distributions to minimize total transport cost
- Output: per-cell pairing (a "transport map" or "coupling")

```
Uses distributional information     →     Produces individual mapping
─────────────────────────────              ────────────────────────────
P(control), P(perturbed)                   ●₁ → ◉ₐ
shape, density, geometry                   ●₂ → ◉_b (mixture)
                                          ●₃ → ◉_c
                                          ...
```

So the distinction with [[concepts/distributional-vs-point-prediction]] is:
- **Distributional prediction**: predicts the distribution shape
- **Cell-level counterfactual**: uses distributional information to predict cell-to-cell mappings

Both reject the point estimate, but they answer different questions.

## Optimal Transport Intuition — "Moving Sand"

The mathematical framework is **Optimal Transport (OT)**:

```
Imagine sand piles at two sets of locations:

Before:                            After:
   ●●●     ●●●                       ◉◉◉◉◉      ◉◉
   pile A   pile B                   pile A'    pile B'
   (control distribution)            (perturbed distribution)

Question: How do you move sand from {A, B} to {A', B'}
          such that total transport cost (distance × amount) is minimized?

OT's answer: An optimal transport plan that says, for each grain of
             sand at origin, where it should go.
```

In single-cell terms:
- "Grain of sand" = one cell (a point in latent or expression space)
- "Origin pile" = control cell
- "Destination pile" = perturbed cell
- "Distance" = similarity between cells (e.g., Euclidean in latent space)
- **OT plan** = "control cell ●₁ corresponds to perturbed cell ◉ₐ" mapping

This pairing is the **cell-level counterfactual**: a pseudo before-after that destructive sequencing prevented us from observing directly.

## What You Get From a Cell-Level Counterfactual

| Output | Use case |
|--------|----------|
| Per-cell predicted change | "Cell ●₁ would gain expression of X, lose Y if perturbed" |
| Heterogeneous response detection | Identify cells that escape vs respond strongly |
| Trajectory across time points | Multi-marginal OT links t=0, t=1, t=2 → cellular fate paths |
| Lineage estimation without barcodes | Computational alternative to clonal lineage tracing |
| Counterfactual outcomes for downstream analysis | "What if this cell had not been treated?" feeds into causal inference |

## Methods (Catalog from Dimitrov 2026 ontology)

| Method | What it maps | Wiki page |
|--------|-------------|-----------|
| **moscot** | Temporal, spatial, perturbation — most general framework | [[single-cell-dl/klein-2025-mapping-cells-through-time]] |
| **Waddington-OT** | Time t ↔ time t+1 distributions across development | (cited in Dimitrov) |
| **CINEMA-OT** | Perturbed ↔ control + ICA confounder removal | (cited in Dimitrov) |
| **CellOT** | General perturbation effect mapping | (cited in Dimitrov) |
| **CondOT** | Conditional OT (perturbation given covariate) | (cited in Dimitrov) |
| **scPRAM** | Drug response mapping | (cited in Dimitrov) |
| **CoSpar** | Lineage barcode + state coupling | (cited in Dimitrov) |

### Extensions and Variants

| Variant | Difference from basic OT |
|---------|-------------------------|
| **Flow matching** (CellFlow, MFM, MMFM, CFGen) | Continuous-time OT via neural ODE; scales better, smoother trajectories |
| **Schrödinger bridges** (SBalign, DeepRUOT, ARTEMIS) | Stochastic OT — allows noise and randomness in the mapping |
| **Multi-marginal OT** | Maps three or more distributions simultaneously (e.g., t=0, t=1, t=2 together) |
| **Gromov-Wasserstein OT** (GWOT, moscot's GW mode) | Maps distributions in *different* spaces (e.g., RNA ↔ ATAC) |

## Computational vs Experimental Lineage

Cell-level counterfactual via OT is the **computational answer** to a question that experimental lineage tracing answers more directly:

| Approach | Pros | Cons |
|----------|------|------|
| **OT-based pairing** | Cheap (no extra experiment), works on any scRNA-seq data | Statistical pairing only — not biological identity |
| **CRISPR / barcode lineage tracing** (CARLIN, GESTALT, MARC1) | True clonal identity | Expensive, requires special experimental setup |
| **Live-cell imaging + sequencing** | Direct observation | Throughput limited |
| **Naturally occurring lineage markers** (mtDNA mutations) | No engineering needed | Sparse signal |

Dimitrov 2026's outlook flags this as a key future direction — combining OT-based computational pairing with sparse experimental lineage anchors gives the best of both.

## Critical Caveats for Interpretation

When you read "we used OT to map perturbed cells to controls":

1. **The pairing is statistical, not biological.** "Cell A → cell B" means "in this distribution geometry, A and B are most plausibly paired", **not** "A is literally B in another timeline".

2. **Quality depends on distribution overlap.** If control and perturbed populations are very different (e.g., perturbation causes huge cell death and creates entirely new cell types), OT can produce nonsensical mappings.

3. **Latent space matters.** OT in raw expression space is usually bad (curse of dimensionality, sparsity). Most methods do OT in a learned latent space — which means the latent representation's quality propagates into the OT output.

4. **Soft vs hard mappings.** Most modern methods produce *soft* couplings (one cell maps to a probability distribution over target cells). Treating these as deterministic pairs loses information.

5. **Confounders are a problem.** If batch effects or cell cycle state differ between control and perturbed populations, OT may map cells based on those differences instead of the perturbation effect. CINEMA-OT addresses this with ICA preprocessing.

## When To Use Cell-Level Counterfactual

| Question | Need cell-level? |
|----------|------------------|
| "What's the average effect of perturbing X on cell type Y?" | No — point estimate is fine |
| "Does perturbing X create heterogeneous response?" | Distributional methods sufficient |
| "Which specific cells would have responded if untreated?" | Yes — need cell-level pairing |
| "What cellular trajectory does perturbation X induce?" | Yes — temporal OT or flow matching |
| "Map RNA cells to ATAC cells of the same condition" | Yes — Gromov-Wasserstein OT |
| "Pair pre-treatment biopsy cells to post-treatment biopsy cells" | Yes — clinical longitudinal analogy |

## Connection to Other Concepts

- [[concepts/distributional-vs-point-prediction]] — cell-level counterfactual is built on distributional thinking but produces individual-level output
- [[concepts/multimodal-temporal-readout]] — OT maps not just within-modality but across modalities (Gromov-Wasserstein) and across time
- [[concepts/uncertainty-quantification]] — OT produces *one* coupling, but uncertainty in the coupling itself is rarely reported
- [[concepts/factorial-perturbation-design]] — cell-level counterfactual lets us interpret 2×2 cells (perturb × context) at individual resolution
- [[concepts/expressivity-interpretability-tradeoff]] — OT is interpretable as "this maps to that", but the underlying latent space (where OT happens) is often opaque

## Part of broader synthesis

- [[overviews/six-open-issues-perturbation-modelling]] — cell-level counterfactual cuts across multiple issues: foundational for **Issue 4: Extrapolation** (predicting individual cells, not just population means), connects to **Issue 5: UQ** (the coupling has its own uncertainty), and enables **Issue 1: Multimodal** integration via Gromov-Wasserstein cross-modality mapping. The destructive-sequencing problem this concept solves is *why* OT keeps appearing across the modelling field.

---

## Practical Reading Tip

When a paper claims "we recovered cellular trajectories" or "we identified per-cell perturbation effects":

1. **Look for OT mention** — if so, expect cell-level claims, but verify caveats above
2. **Check the latent space used for OT** — quality of the embedding determines quality of the mapping
3. **Look for confounder treatment** — does the method address batch effects, cell cycle, etc.?
4. **Distinguish soft vs hard pairings** — papers sometimes overstate hard pairings when their method actually outputs probabilities
5. **Compare to true lineage tracing where available** — best validation for OT-based claims

---

*Used in: [[single-cell-dl/klein-2025-mapping-cells-through-time]] (moscot — most general OT framework for single-cell), [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] (review's population-tracing modelling concept), [[drug-resistance/xu-2026-mapping-convergent-regulators-of]] (PerturbFate — uses RNA velocity from nascent + steady-state, conceptual cousin to cell-level counterfactual)*
