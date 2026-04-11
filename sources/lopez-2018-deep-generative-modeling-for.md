---
title: "Deep generative modeling for single-cell transcriptomics"
authors: Lopez, Romain, Regier, Jeffrey, Cole, Michael B., Jordan, Michael I., Yosef, Nir
year: 2018
doi: 10.1038/s41592-018-0229-2
category: single-cell-dl
pdf_path: papers/lopez-2018-deep-generative-modeling-for.pdf
pdf_filename: lopez-2018-deep-generative-modeling-for.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

scVI is a scalable deep generative model (hierarchical Bayesian + VAE) for probabilistic normalization, batch correction, dimensionality reduction, clustering, and differential expression of scRNA-seq data, scaling to 1M+ cells.

## 1. Document Info
- Journal/Conference: Nature Methods
- Received/Published: Published December 2018 (DOI: 10.1038/s41592-018-0229-2)

## 2. Key Contributions
- scVI (single-cell Variational Inference): unified probabilistic framework for scRNA-seq analysis based on a zero-inflated negative binomial (ZINB) generative model with VAE
- Single model for batch correction, normalization, visualization, clustering, and differential expression — avoiding inconsistency from using separate methods
- Scalable to 1M+ cells via stochastic optimization (mini-batch training); most competitors failed at >50K cells
- Explicitly models two key nuisance factors: library size (capture efficiency) and batch effects

## 3. Methods & Architecture
- **Generative model**: ZINB distribution for each gene × cell; parameters predicted by neural networks
- **Encoder (recognition network)**: maps observed expression + batch label → approximate posterior over latent variables (z, l)
  - z: low-dimensional (10D) Gaussian capturing biological variation
  - l: 1D Gaussian capturing library size (nuisance)
- **Decoder**: maps z (conditioned on batch s) → ZINB parameters (dropout rate, mean)
- **Training**: variational inference with ELBO maximization via stochastic gradient descent (Adam); mini-batch processing enables scale
- **Downstream tasks**: clustering (Louvain on kNN graph in z-space), differential expression (posterior predictive comparison), imputation (decoded mean), batch correction (z-space embedding)

## 4. Key Results & Benchmarks
- Scales to 1.3M mouse brain cells (BRAIN-LARGE); most alternatives exceeded memory at >50K cells
- Imputation: competitive with or better than MAGIC, BISCUIT, ZINB-WaVE on 5 benchmark datasets
- Differential expression: better calibrated p-values vs. Wilcoxon, MAST, edgeR
- Batch correction: separates biological variation from technical variation on PBMC and mouse brain data
- Available at: github.com/YosefLab/scVI

## 5. Limitations & Future Work
- ZINB assumption may not fit all sequencing technologies equally
- Relies on supplied batch labels; cryptic batch effects not captured automatically
- Downstream clustering requires additional tools (Louvain); not end-to-end
- Future: semi-supervised extension (→ scANVI), multi-modal, reference mapping (→ scArches)

## 6. Related Work
- scANVI (Xu et al., 2021) — semi-supervised extension of scVI for label-aware harmonization
- scArches (Lotfollahi et al., 2022) — transfer learning / reference mapping built on scVI
- scPoli (De Donno et al., 2023) — population-level integration using scVI-family architecture
- MrVI (Boyeau et al., 2025) — sample-level heterogeneity modeling; next-generation scVI extension
- ZINB-WaVE, ZIFA — earlier probabilistic scRNA-seq models

## 7. Glossary
- **scVI**: single-cell Variational Inference — the method introduced in this paper
- **VAE (Variational Autoencoder)**: generative model with encoder-decoder architecture trained via variational inference; learns latent representations
- **ZINB (Zero-Inflated Negative Binomial)**: count distribution modeling overdispersion and excess zeros in scRNA-seq data
- **ELBO (Evidence Lower Bound)**: variational inference objective; maximizing ELBO approximates the marginal likelihood
- **Library size**: total number of UMIs/reads per cell; a technical nuisance factor capturing capture efficiency
- **Batch effect**: unwanted technical variation between samples processed in different batches, labs, or platforms
- **Louvain clustering**: community detection algorithm applied to kNN graphs; standard scRNA-seq clustering method
