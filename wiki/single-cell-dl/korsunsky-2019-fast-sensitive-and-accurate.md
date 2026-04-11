---
title: "Fast, sensitive and accurate integration of single-cell data with Harmony"
authors: Korsunsky, Ilya, Millard, Nghia, Fan, Jean, Slowikowski, Kamil, Zhang, Fan, Wei, Kevin, Baglaenko, Yuriy, Brenner, Michael, Loh, Po-ru, Raychaudhuri, Soumya
year: 2019
doi: 10.1038/s41592-019-0619-0
source: korsunsky-2019-fast-sensitive-and-accurate.md
category: single-cell-dl
tags: [Harmony, integration, batch-correction, PCA, soft-clustering, scalability, LISI]
---

## Summary

Harmony integrates scRNA-seq datasets by operating on PCA embeddings: it iteratively assigns cells to soft clusters (with a diversity penalty to force multi-dataset membership), computes cluster-specific linear correction factors, and applies per-cell weighted corrections. The result is a corrected embedding where cells group by cell type rather than dataset. Scales to ~1M cells on a personal computer and handles multiple simultaneous batch factors.

## Key Contributions

- Iterative soft k-means with diversity penalty: forces dataset mixing within clusters while preserving cell-type separation
- Cell-type-specific linear correction: distinct correction factor per cluster/cell type, avoiding global over-normalization
- Handles multiple simultaneous batch factors (lab, technology, tissue source)
- LISI metric (iLISI + cLISI): objective integration quality measure introduced alongside Harmony
- Scales to ~1M cells; R and Python implementations

## Methods & Architecture

Input is a PCA embedding. Harmony iterates: (1) soft k-means clustering with information-theoretic diversity penalty; (2) per-dataset, per-cluster centroid differences → linear correction factors; (3) cell correction = cluster-membership-weighted average of correction factors; repeat until stable. Output: corrected PCA embedding. Downstream UMAP + Louvain applied to Harmony embeddings.

## Results

- Outperforms Seurat, BBKNN, Scanorama, MNN on cell-line, PBMC, pancreas, and embryogenesis datasets
- ~1M cell integration on personal computer; faster than VAE methods
- iLISI/cLISI metrics widely adopted as standard integration benchmarks
- scIB benchmark (Luecken 2022): Harmony best for scATAC-seq; competitive for simple RNA-seq tasks

## Limitations

- Linear correction; may underperform scVI/scANVI for complex nonlinear batch effects
- Can over-correct when disease/biological variation is confounded with batch
- No annotation transfer capability; integration only

## Related Papers

- [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] — scVI: nonlinear integration baseline; often compared
- [[single-cell-dl/luecken-2022-benchmarking-atlas-level-data]] — scIB: comprehensive benchmark where Harmony tops scATAC-seq
- [[single-cell-dl/dedonno-2023-population-level-integration-of]] — scPoli: prototype-based integration; outperforms Harmony on complex RNA tasks
- [[single-cell-dl/hao-2021-integrated-analysis-of-multimodal]] — Seurat v4: Harmony integrated as optional integration backend
