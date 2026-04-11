---
title: "Learning cell dynamics with neural differential equations"
authors: Michael E. Vinyard, Anders W. Rasmussen, Ruitong Li, Allon M. Klein, Gad Getz, Luca Pinello
year: 2025
doi: 10.1038/s42256-025-01150-3
source: vinyard-2025-learning-cell-dynamics-with.md
category: single-cell-dl
tags: [neural-SDE, cell-dynamics, drift-diffusion, lineage-tracing, fate-prediction, hematopoiesis, scDiffEq]
---

## Summary

scDiffEq learns a **neural stochastic differential equation** from multi-timepoint scRNA-seq: two networks parameterize the drift `f(z)` and the diffusion `g(z)` of cell state changes, with `g(z)` explicitly cell-state-dependent rather than constant. Trained on lineage-traced LARRY hematopoiesis via Sinkhorn-divergence matching to observed populations, it outperforms PRESCIENT, Dynamo, CellRank and Waddington-OT on fate prediction, and shows that the optimal drift/diffusion ratio is ~2.5 — a biological parameter prior methods implicitly mis-set.

## Key Contributions

- Cell-state-dependent diffusion is the first-order innovation. Every prior drift-diffusion method for single-cell dynamics (PBA, PRESCIENT, Dynamo) treats diffusion as a constant, isotropic hyperparameter. scDiffEq shows that is wrong.
- Demonstrates that drift/diffusion ratio is a meaningful biological quantity, not a fitting artifact. Optimal ratio 2.5 (hematopoiesis); PRESCIENT's implicit 161 is off by nearly two orders of magnitude.
- Beats PRESCIENT by ~6% on LARRY fate prediction (54.8% vs. 50.7%).
- Framework extends to in silico perturbation by modifying the drift field.

## Methods & Architecture

- **Model**: `dz = f(z) dt + g(z) dW`, neural SDE.
- **Input**: PCA-reduced embeddings of multi-timepoint scRNA-seq (LARRY here).
- **Training**: Euler-Maruyama integration → Sinkhorn divergence between predicted and observed distributions at each held-out timepoint + regularization.
- **Inference**: simulate 50K trajectories from day-2 cells; label outcomes by nearest-neighbor assignment to observed day-4/6 cells.
- **Perturbation**: modify drift field `f` corresponding to a CRISPR-simulated state → re-simulate trajectories.
- **Gene-level decoding**: backward-transform drift and diffusion from PCA to gene space → reveal genes driving drift (deterministic) vs. diffusion (stochastic).

## Results

- **LARRY fate prediction** (day 2 → day 4/6): linear regression on static features 61.9% (non-dynamic ceiling). Dynamo/CellRank ~4-46%. PRESCIENT 42.5% (50.7% with KEGG growth weights). **scDiffEq 52.5-54.8%** depending on drift/diffusion ratio.
- **Drift/diffusion sweep**: stable 1.0-5.0, optimum at 2.5, sharp drop at ≥10.
- **CRISPR-perturbed hematopoiesis**: scDiffEq recapitulates observed perturbation dynamics via drift modification.
- **Gene-level decoding**: identifies TFs whose expression correlates with drift vs. diffusion, suggesting how cells exploit stochasticity during GMP → neutrophil/monocyte bifurcation.

## Limitations

- Requires multi-timepoint or lineage-traced data.
- PCA dimensionality reduction may discard biological signal.
- Perturbation prediction via drift modification is pattern-learning, not mechanistic (contrast with CellOracle).
- Computational cost scales with SDE integration step count.
- Benchmarked primarily on hematopoiesis; generalization to organoid/brain trajectories unclear.

## Related Papers

- [[single-cell-dl/lange-2022-cellrank-for-directed-single]] — CellRank, Markov chain approach; outperformed by scDiffEq on LARRY fate prediction
- [[single-cell-dl/setty-2019-characterization-of-cell-fate]] — Palantir, earlier probabilistic fate framework
- [[single-cell-dl/klein-2025-mapping-cells-through-time]] — moscot, optimal-transport dynamics alternative
- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle, mechanistic GRN-based perturbation contrast
- [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] — Squidiff, diffusion-model alternative for perturbation prediction
- [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna]] — cell2fate, RNA velocity refinement
