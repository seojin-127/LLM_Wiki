---
title: "Learning cell dynamics with neural differential equations"
authors: Michael E. Vinyard, Anders W. Rasmussen, Ruitong Li, Allon M. Klein, Gad Getz, Luca Pinello
year: 2025
doi: 10.1038/s42256-025-01150-3
category: single-cell-dl
pdf_path: papers/vinyard-2025-learning-cell-dynamics-with.pdf
pdf_filename: vinyard-2025-learning-cell-dynamics-with.pdf
source_collection: downloads-perturb-batch
---

## One-line Summary

scDiffEq learns neural stochastic differential equations (neural SDEs) that model both the deterministic drift and *cell-state-dependent* diffusion of single-cell dynamics — beating PRESCIENT, CellRank, Dynamo on lineage-traced fate prediction (54.8% accuracy) and showing that the drift/diffusion ratio is a biologically meaningful quantity that prior methods hard-coded incorrectly.

## 1. Document Info
- Journal: Nature Machine Intelligence, Vol 7, Dec 2025, 1969-1984
- Published online: 18 December 2025

## 2. Key Contributions

- First single-cell framework that models **cell-state-dependent diffusion** (stochastic component) with a neural network, rather than treating diffusion as a constant hyperparameter.
- Neural SDE parameterization: two networks `f(z)` (drift) and `g(z)` (diffusion) trained via Sinkhorn divergence between predicted and observed cell populations across time points.
- Outperforms PRESCIENT, Dynamo, CellRank, Waddington-OT on LARRY lineage-tracing fate-prediction benchmark.
- Shows that the optimal drift/diffusion ratio is ~2.5 for hematopoiesis — PRESCIENT's implicit ratio of 161 is far off, highlighting how "stochasticity as a constant" misses real biology.
- Extends in silico perturbation: drift field can be perturbed to simulate CRISPR-like interventions, and scDiffEq recapitulates CRISPR-perturbed hematopoiesis dynamics.

## 3. Methods & Architecture

- **Input**: PCA-reduced scRNA-seq embeddings from multi-timepoint lineage-traced data (e.g., LARRY).
- **Neural SDE**: dz = f(z) dt + g(z) dW, with f and g as neural networks.
- **Training**: Euler-Maruyama integration to advance cells through time; loss = sum of Sinkhorn divergences between predicted and observed distributions at each timepoint + regularization.
- **Perturbation**: modify drift field f to reflect simulated CRISPR perturbation → simulate new trajectories.
- **Gene-level dynamics**: backward-decode from PCA to reveal which genes drive drift and which drive diffusion along a trajectory.

## 4. Key Results & Benchmarks

- LARRY hematopoiesis (Weinreb 2020): day 2 → day 4 / 6 fate prediction.
- Static-signature linear regression: 61.9% (non-dynamic baseline).
- Previous generative methods: 4.1-46.1% accuracy (Dynamo, CellRank poor; PRESCIENT 42.5%, 50.7% with KEGG).
- scDiffEq: 52.5% without KEGG, 54.8% at optimal drift/diffusion ratio 2.5 — ~6% over SotA.
- Drift/diffusion sweep: ratios 1.0-5.0 stable, sharp drop at ≥10. PRESCIENT's implicit 161 is far suboptimal.
- CRISPR perturbation reproduction: scDiffEq recapitulates perturbed trajectories.

## 5. Limitations & Future Work

- Requires multi-timepoint data (lineage-traced or at least dense time course); limited on single-snapshot datasets unless extended.
- PCA reduction may discard biologically relevant variance.
- Computational cost scales with SDE integration steps.
- No direct causal mechanism — still pattern-learning in a continuous-space embedding.
- Perturbation modeling via drift modification is not derived from a GRN or mechanistic model.

## 6. Related Work

- PRESCIENT (Yeo 2021), Dynamo (Qiu 2022), CellRank (Lange 2022), Waddington-OT (Schiebinger 2019), scTour, TIGON, TrajectoryNet, MIOFlow — trajectory / dynamics modeling.
- PI-SDE — parallel neural-SDE framework focused on interpolation.
- scDiffEq extends neural-ODE/SDE dynamics to explicit cell-state-dependent diffusion.

## 7. Glossary

- **Neural SDE**: stochastic differential equation where drift and diffusion are parameterized by neural networks.
- **Drift / diffusion ratio**: relative contribution of deterministic vs. stochastic dynamics; biologically meaningful.
- **Sinkhorn divergence**: regularized Wasserstein distance used as training loss.
- **LARRY**: lineage and RNA recovery, a heritable-barcode lineage-tracing technology.
- **PBA**: population balance analysis, an earlier steady-state approach to cell dynamics.
