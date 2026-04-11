---
title: "Mapping cells through time and space with moscot"
authors: Dominik Klein, Giovanni Palla, Marius Lange, Michal Klein, Zoe Piran, Manuel Gander, Laetitia Meng-Papaxanthos, Michael Sterr, Lama Saber, Changying Jing, Aimée Bastidas-Ponce, Perla Cota, Marta Tarquis-Medina, Shrey Parikh, Ilan Gold, Heiko Lickert, Mostafa Bakhti, Mor Nitzan, Marco Cuturi, Fabian J. Theis
year: 2025
doi: 10.1038/s41586-024-08453-2
source: klein-2025-mapping-cells-through-time.md
category: single-cell-dl
tags: [optimal-transport, trajectory, spatial, multimodal, scalability, Waddington-OT, embryogenesis]
---

## Summary

moscot replaces a patchwork of optimal-transport methods (WOT, PASTE, NovoSpaRc) with a single scalable, multimodal framework. Its three moves: (1) supports multimodality throughout — the same pipeline works for RNA, ATAC, protein, or combinations; (2) scales to millions of cells via low-rank OT and JAX-based OTT; (3) unifies temporal, spatial, and spatiotemporal mapping under one API. Demonstrated on a 1.7M-cell × 20-timepoint mouse embryogenesis atlas that exhausted WOT at 75K cells.

## Key Contributions

- **Scalability as the enabling move**: low-rank OT + JAX/OTT brings linear memory complexity, making atlas-scale OT routine.
- **Multimodality everywhere**: Gromov-Wasserstein and fused-GW enable cross-modality mapping (e.g., CITE-seq → spatial slide).
- **Spatiotemporal**: explicit joint mapping across both space and time — not just temporal OR spatial.
- Unified scverse-integrated API; interoperates with CellRank for downstream trajectory analysis.
- Experimental validation: NEUROD2 identified from mouse pancreas mapping and validated in human iPSC islet differentiation as an epsilon-cell progenitor regulator.

## Methods & Architecture

- **OT problem types**:
  - W-type (Wasserstein): same feature space — e.g., two RNA timepoints.
  - GW-type (Gromov-Wasserstein): different spaces — e.g., RNA vs. ATAC, or two spatial slides.
  - FGW-type (fused GW): partial feature overlap.
- **Solvers**: Sinkhorn (W), entropic GW, low-rank variants for atlas scale. Backend = OTT (JAX) with JIT compilation and GPU.
- **Priors**: cellular growth/death rates (inherited from WOT), spatial coordinates, proliferation markers can guide the coupling.
- **Coupling matrix**: probabilistic cell-to-cell assignment; feeds downstream into trajectory inference (CellRank), spatial enrichment, interpolation.

## Results

- **Mouse embryogenesis**: 1.7M cells × 20 timepoints (E3.5-E13.5). WOT fails >75K cells per timepoint. moscot.time processes 275K cells per timepoint on a laptop. Matches dataset-specific TOME on germ-layer and cell-type matching metrics.
- **Growth rates**: cell-level TOME (clTOME) predicted unrealistic 19% apoptosis at E8.0-E8.25; moscot produces more realistic cell-type-specific rates, matching scanpy cell-cycle scores on reprogramming data.
- **Spatial mapping**: mouse liver CITE-seq enriches spatial transcriptomic slides with surface protein information; multi-slide mouse brain alignment.
- **Pancreas RNA+ATAC**: delineates delta and epsilon lineages; identifies NEUROD2 as epsilon progenitor regulator; experimentally validated in human iPSC islet differentiation.

## Limitations

- Population-level probabilistic coupling — does not replace lineage tracing for per-clone identity.
- Low-rank approximations require a tuning parameter (rank).
- Growth rate modeling inherits WOT's proxies and assumptions.
- Descriptive framework: moscot aligns what exists, it does not predict perturbation effects.

## Related Papers

- [[single-cell-dl/lange-2022-cellrank-for-directed-single]] — CellRank, downstream trajectory inference on moscot couplings
- [[single-cell-dl/setty-2019-characterization-of-cell-fate]] — Palantir, trajectory inference ancestor
- [[single-cell-dl/vinyard-2025-learning-cell-dynamics-with]] — scDiffEq, alternative neural SDE approach to cell dynamics
- [[brain-development/fleck-2023-inferring-perturbing-cell-fate]] — organoid trajectories + perturbation, complementary framework
- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle, in silico perturbation on top of trajectories
