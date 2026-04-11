---
title: "Fast, sensitive and accurate integration of single-cell data with Harmony"
authors: Korsunsky, Ilya, Millard, Nghia, Fan, Jean, Slowikowski, Kamil, Zhang, Fan, Wei, Kevin, Baglaenko, Yuriy, Brenner, Michael, Loh, Po-ru, Raychaudhuri, Soumya
year: 2019
doi: 10.1038/s41592-019-0619-0
category: single-cell-dl
pdf_path: papers/korsunsky-2019-fast-sensitive-and-accurate.pdf
pdf_filename: korsunsky-2019-fast-sensitive-and-accurate.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

Harmony integrates single-cell RNA-seq datasets by iteratively learning cell-specific linear correction factors via soft k-means clustering, achieving scalable batch correction to ~1M cells on a personal computer while preserving biological cell-type resolution.

## 1. Document Info
- Journal/Conference: Nature Methods
- Received/Published: Published December 2019 (DOI: 10.1038/s41592-019-0619-0)

## 2. Key Contributions
- Harmony: fast, scalable integration algorithm operating on PCA embeddings; corrects multiple simultaneous batch factors
- Iterative soft k-means clustering with a diversity penalty ensures clusters span multiple datasets — avoids mixing cell types from the same dataset
- Cell-type-specific correction: cluster centroids serve as surrogates for cell states; per-cluster correction factors applied to each cell
- Integrates ~1M cells on a personal computer; handles complex experimental designs (multiple batches, tissue sources, modalities)

## 3. Methods & Architecture
- **Input**: PCA embedding of cells (from any preprocessing pipeline)
- **Soft k-means clustering**: assigns each cell to multiple clusters; diversity penalty (information-theoretic) penalizes clusters dominated by one dataset
- **Linear correction**: per-cluster, per-dataset correction factors computed from centroid differences; each cell's correction = cluster-weighted average
- **Iteration**: clustering → correction → re-clustering, repeated until stable
- **Output**: Harmony embedding (corrected PCs); downstream analysis (UMAP, Louvain) applied to Harmony embeddings
- **Benchmarking metric**: iLISI (integration LISI) and cLISI (cell-type LISI) based on local inverse Simpson's Index
- **Implementation**: R package (github.com/immunogenomics/harmony); Python interface via harmonypy

## 4. Key Results & Benchmarks
- Outperforms Seurat, BBKNN, Scanorama, MNN on cell-line, PBMC, pancreas, and embryogenesis datasets
- ~1M cell integration feasible on personal computer; faster than deep learning methods
- Handles complex designs: multiple batches + tissue sources simultaneously
- Cross-modality integration: scRNA-seq + spatial transcriptomics
- LISI metrics introduced as objective integration quality measures

## 5. Limitations & Future Work
- Linear correction assumption; may underperform for highly nonlinear batch effects
- Requires input PCA embedding; quality depends on upstream preprocessing
- May over-correct when biological variation is confounded with batch (e.g., disease vs. control studies)
- Cannot transfer annotations to new data (see scArches, scPoli for reference mapping)

## 6. Related Work
- scVI (Lopez et al., 2018) — nonlinear VAE-based integration; deeper correction but less scalable
- scANVI (Xu et al., 2021) — label-aware extension of scVI; handles annotation transfer
- scIB benchmark (Luecken et al., 2022) — comprehensive benchmark where Harmony performs well on scATAC-seq
- Seurat v3/v4 (Stuart et al. / Hao et al.) — anchor-based integration; Harmony often integrated as alternative

## 7. Glossary
- **Harmony**: the integration method — iterative soft-clustering linear correction of PCA embeddings
- **iLISI / cLISI**: integration/cell-type Local Inverse Simpson's Index — metrics for integration quality; iLISI measures dataset mixing, cLISI measures cell type separation
- **Soft k-means**: probabilistic k-means where each cell has fractional membership in multiple clusters; enables smooth correction across cell states
- **Diversity penalty**: information-theoretic term penalizing single-dataset-dominated clusters; forces cluster membership to span datasets
- **PCA**: Principal Component Analysis — linear dimensionality reduction; Harmony operates on pre-computed PCs
