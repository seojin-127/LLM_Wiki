---
title: "Mapping cells through time and space with moscot"
authors: Dominik Klein, Giovanni Palla, Marius Lange, Michal Klein, Zoe Piran, Manuel Gander, Laetitia Meng-Papaxanthos, Michael Sterr, Lama Saber, Changying Jing, Aimée Bastidas-Ponce, Perla Cota, Marta Tarquis-Medina, Shrey Parikh, Ilan Gold, Heiko Lickert, Mostafa Bakhti, Mor Nitzan, Marco Cuturi, Fabian J. Theis
year: 2025
doi: 10.1038/s41586-024-08453-2
category: single-cell-dl
pdf_path: papers/klein-2025-mapping-cells-through-time.pdf
pdf_filename: klein-2025-mapping-cells-through-time.pdf
source_collection: downloads-perturb-batch
---

## One-line Summary

moscot is a scalable, multimodal optimal-transport framework for aligning single-cell data across time, space, and modalities — handling 1.7M-cell mouse embryogenesis atlases on a laptop where Waddington-OT runs out of memory, and unifying temporal, spatial, and spatiotemporal mapping under one API.

## 1. Document Info
- Journal: Nature, Vol 638, 27 Feb 2025, 1065-1071
- Published online: 22 January 2025
- Code: https://moscot-tools.org

## 2. Key Contributions

- **Unified OT framework**: Wasserstein (same feature space), Gromov-Wasserstein (different spaces), Fused GW (partially shared features) all accessible through one API.
- **Scalability**: low-rank OT approximations give linear memory complexity; JAX/OTT backend enables GPU acceleration and laptop-scale processing of 1.7M cells × 20 timepoints.
- **Multimodality throughout**: same OT pipeline accepts RNA, ATAC, protein, and their combinations.
- **Temporal**: moscot.time replaces WOT for time-course trajectory reconstruction; cell-growth-rate modeling retained.
- **Spatial**: moscot.spatial aligns spatial transcriptomic slides, maps CITE-seq modalities to spatial slides.
- **Spatiotemporal**: moscot.spatiotemporal — new concept jointly using space and time axes.
- Experimental validation: NEUROD2 as epsilon-cell progenitor regulator in human iPSC islet differentiation, predicted from paired mouse pancreas RNA+ATAC.

## 3. Methods & Architecture

- **OT problem setup**: input two (or more) unpaired distributions of cells; optional prior (growth rates, spatial coordinates).
- **Solvers** via OTT (JAX): Sinkhorn-based W-type, entropic GW, low-rank variants for atlases.
- **Coupling matrix**: probabilistic cell-to-cell mapping, downstream feeds into trajectory, alignment, interpolation.
- **Multimodality**: shared latent representation → OT applied in latent space.
- **Integration with scverse**: interoperates with CellRank 2, scanpy, anndata.

## 4. Key Results & Benchmarks

- Mouse embryogenesis (Qiu et al. 2022, 1.7M cells × 20 timepoints E3.5-E13.5): WOT fails >75K cells per timepoint; moscot processes 275K on a laptop. Comparable accuracy to dataset-specific TOME on germ-layer and cell-type matching metrics.
- More realistic cell growth rates than cell-level TOME (clTOME), which predicted unrealistic 19% apoptosis at E8.0-E8.25.
- Mouse liver CITE-seq → spatial mapping: multimodal enrichment of spatial slides.
- Mouse brain coronal section alignment: multi-slide spatial atlas.
- Mouse pancreas E12.5-E15.5 RNA+ATAC: delineates delta and epsilon lineages; identifies NEUROD2 as epsilon progenitor regulator; validated in human iPSC islet differentiation in vitro.

## 5. Limitations & Future Work

- OT couplings are population-level probabilistic mappings; per-cell clonal identity still requires lineage tracing.
- Low-rank approximations trade accuracy for scalability; choice of rank is a tuning parameter.
- Growth rate modeling inherits WOT's assumptions about proliferation/death proxies.
- Does not explicitly model perturbations; it is a descriptive alignment tool.

## 6. Related Work

- Waddington-OT (Schiebinger 2019) — temporal predecessor, unimodal and not scalable.
- PASTE, NovoSpaRc — spatial OT alignment predecessors.
- CellRank (Lange 2022) — trajectory inference that moscot couplings can feed into.

## 7. Glossary

- **Optimal transport (OT)**: framework for computing a cost-minimizing mapping between two probability distributions.
- **Wasserstein distance**: OT distance when source and target live in the same feature space.
- **Gromov-Wasserstein**: OT for distributions in different spaces, comparing intra-distribution pairwise distances.
- **Fused GW**: hybrid of W and GW for partially shared features.
- **Low-rank OT**: approximation that constrains the coupling matrix rank → linear memory.
- **Coupling matrix**: probabilistic assignment of source cells to target cells.
