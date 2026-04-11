---
title: "Benchmarking atlas-level data integration in single-cell genomics"
authors: Luecken, Malte D., Buttner, M., Chaichoompu, K., Danese, A., Interlandi, M., Mueller, M. F., Strobl, D. C., Zappia, L., Dugas, M., Colome-Tatche, M., Theis, Fabian J.
year: 2022
doi: 10.1038/s41592-021-01336-8
category: single-cell-dl
pdf_path: papers/luecken-2022-benchmarking-atlas-level-data.pdf
pdf_filename: luecken-2022-benchmarking-atlas-level-data.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

The most comprehensive benchmarking study of single-cell data integration methods: 68 method-preprocessing combinations evaluated on 85 batches from 13 atlas-level tasks (>1.2M cells), using 14 metrics; scANVI, Scanorama, scVI, and scGen lead overall; Harmony and LIGER best for scATAC-seq.

## 1. Document Info
- Journal/Conference: Nature Methods
- Received/Published: Published January 2022 (DOI: 10.1038/s41592-021-01336-8)

## 2. Key Contributions
- scIB (single-cell integration benchmarking): Python module + benchmarking pipeline for evaluating integration methods
- 68 method-preprocessing combinations on 13 integration tasks (up to 23 batches, 1M cells); most comprehensive benchmark at publication
- 14 evaluation metrics split into batch removal and biological conservation
- Key findings: (1) scANVI > scVI > Harmony in RNA-seq; (2) Harmony + LIGER best for scATAC-seq; (3) HVG selection helps; (4) scaling harms biological conservation

## 3. Methods & Architecture
- **Methods benchmarked (16)**: MNN, FastMNN, Seurat v3 (CCA + RPCA), scVI, scANVI, Scanorama, BBKNN, LIGER, Conos, SAUCIE, Harmony, ComBat, DESC, trVAE, scGen
- **Integration tasks (13)**: simulation (2) + scRNA-seq (5) + scATAC-seq (6); tissues include pancreas, PBMC, lung, mouse atlas, human atlas
- **Evaluation metrics (14)**:
  - Batch removal: kBET, kNN graph connectivity, ASW (batch), graph iLISI, PCA regression
  - Biological conservation: graph cLISI, ASW (cell type), NMI, ARI, isolated label scores, trajectory conservation, cell cycle conservation
- **Scoring**: composite score = 0.4 × batch removal + 0.6 × biological conservation
- **Key preprocessing finding**: HVG (highly variable gene) selection consistently improves performance; z-score scaling improves batch removal but hurts biological conservation

## 4. Key Results & Benchmarks
- **Top methods (RNA-seq)**: scANVI (best when labels available), Scanorama and scVI (best unsupervised)
- **Top methods (scATAC-seq)**: Harmony and LIGER; window and peak feature spaces differ in ranking
- **Harmony**: fast and effective but less accurate for complex nested batch effects vs. scVI/scANVI
- **ComBat**: poor performance on atlas-level tasks despite strong performance in simpler benchmarks
- **Biological conservation**: scGen (perturbation-aware) best when condition labels available
- **Usability**: many methods lack scalability, documentation, or memory efficiency

## 5. Limitations & Future Work
- Benchmark static at publication; newer methods (scPoli, scArches) not included
- scATAC-seq benchmark less comprehensive; feature space choice (peaks vs. windows) strongly affects results
- Ground truth relies on manual annotation of reference batches; annotation errors propagate to metrics
- Computational cost limits exhaustive comparison of all hyperparameter combinations

## 6. Related Work
- scVI (Lopez et al., 2018) — top performer in unsupervised RNA integration
- scANVI (Xu et al., 2021) — top performer when cell type labels available
- Harmony (Korsunsky et al., 2019) — fast linear method; best for scATAC-seq
- Scanorama (Hie et al., 2019) — SVD-based integration; top unsupervised performer
- scPoli (De Donno et al., 2023) — next-generation method outperforming scANVI on population-level tasks

## 7. Glossary
- **scIB**: single-cell Integration Benchmarking — the Python package and framework introduced here
- **kBET**: k-nearest-neighbor Batch Effect Test — statistical test measuring how well datasets mix in local neighborhoods
- **LISI**: Local Inverse Simpson's Index — measures effective number of datasets (iLISI) or cell types (cLISI) in local neighborhood
- **ASW**: Average Silhouette Width — measures cluster separation; used for both batch mixing and cell type conservation
- **HVG**: Highly Variable Genes — gene selection strategy retaining genes with high variance across cells; standard preprocessing step
- **NMI / ARI**: Normalized Mutual Information / Adjusted Rand Index — cluster-level label conservation metrics
- **Trajectory conservation**: metric assessing whether biological trajectories (pseudotime) are preserved after integration
