---
title: "Deep generative modeling for single-cell transcriptomics"
authors: Lopez, Romain, Regier, Jeffrey, Cole, Michael B., Jordan, Michael I., Yosef, Nir
year: 2018
doi: 10.1038/s41592-018-0229-2
source: lopez-2018-deep-generative-modeling-for.md
category: single-cell-dl
tags: [scVI, VAE, ZINB, batch-correction, normalization, differential-expression, scalability]
---

## Summary

scVI is the foundational deep generative model for scRNA-seq: a hierarchical Bayesian VAE using a zero-inflated negative binomial (ZINB) distribution to model each gene's expression while explicitly accounting for library size and batch effects. A single model handles normalization, batch correction, dimensionality reduction, clustering, and differential expression, scaling to 1M+ cells via stochastic optimization.

## Key Contributions

- Unified probabilistic model for five scRNA-seq analysis tasks with a single consistent generative framework
- ZINB distribution captures overdispersion and dropout; explicit modeling of library size (l) and batch (s)
- Scalable to 1.3M cells — outpaces alternatives that fail at >50K cells
- Foundational model for scANVI, scArches, scPoli, MrVI, multiDGD, and the scvi-tools ecosystem

## Methods & Architecture

Two latent variables per cell: l (1D, library size nuisance) and z (10D, biological variation). An encoder neural network maps expression + batch label → approximate posterior over (z, l). A decoder maps z conditioned on batch → ZINB parameters (mean, dispersion, dropout rate). Training via ELBO maximization with mini-batch SGD enables scale. Downstream: kNN graph on z → Louvain clustering; UMAP visualization; differential expression via posterior predictive comparison of decoded gene means.

## Results

- Scales to 1.3M mouse brain cells; most competitors exceed memory at >50K cells
- Imputation accuracy competitive with or better than MAGIC, BISCUIT, ZINB-WaVE
- Differential expression: better-calibrated p-values than Wilcoxon, MAST, edgeR
- Effective batch correction validated on PBMC and brain datasets

## Limitations

- Relies on explicit batch labels; cryptic batch effects not captured automatically
- ZINB may not fit all sequencing technologies equally (e.g., full-length protocols)
- Clustering requires external tools; not end-to-end

## Related Papers

- [[single-cell-dl/xu-2021-probabilistic-harmonization-and]] — scANVI: semi-supervised annotation extension of scVI
- [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]] — scArches: transfer learning reference mapping built on scVI
- [[single-cell-dl/dedonno-2023-population-level-integration-of]] — scPoli: prototype-based extension of scVI for population-level integration
- [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]] — MrVI: sample-level hierarchical extension of scVI
- [[single-cell-dl/luecken-2022-benchmarking-atlas-level-data]] — scIB benchmark: scVI among top performers
- [[single-cell-dl/schuster-2024-multidgd-versatile-deep]] — multiDGD: scVI-family model for RNA+ATAC
