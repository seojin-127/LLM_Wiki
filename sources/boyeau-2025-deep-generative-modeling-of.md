---
title: "Deep generative modeling of sample-level heterogeneity in single-cell genomics"
authors: Boyeau, Pierre, Hong, Justin, Gayoso, Adam, Kim, Martin, McFaline-Figueroa, Jose L., Jordan, Michael I., Azizi, Elham, Ergen, Can, Yosef, Nir
year: 2025
doi: 10.1038/s41592-025-02808-x
category: single-cell-dl
pdf_path: papers/boyeau-2025-deep-generative-modeling-of.pdf
pdf_filename: boyeau-2025-deep-generative-modeling-of.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

MrVI (Multi-resolution Variational Inference) is a hierarchical Bayesian deep generative model for cohort-level single-cell analysis that computes per-cell sample distance matrices to perform de novo sample stratification and comparative analysis without predefined cell states, discovering clinically relevant subtypes in COVID-19 and IBD datasets.

## 1. Document Info
- Journal/Conference: Nature Methods
- Received/Published: Published October 2025 (DOI: 10.1038/s41592-025-02808-x)

## 2. Key Contributions
- MrVI: hierarchical deep generative model with two latent variables — u (cell state, independent of sample) and z (cell state + sample effect) — disentangling cellular identity from sample-level variation
- Per-cell sample distance matrix: for each cell, computes pairwise distances between samples based on how each sample shifts that cell in z-space; enables cell-type-specific sample stratification
- De novo sample grouping: annotation-free discovery of clinically relevant sample clusters manifested in specific cell subsets
- Applied to COVID-19 (severity stratification via T cell subset), IBD (pericyte subpopulation with stenosis-specific transcriptional changes), and perturbation screens (compound MoA grouping)
- Open-source at scvi-tools.org

## 3. Methods & Architecture
- **Two latent variables per cell**:
  - u_n: cell state disentangled from sample; Mixture of Gaussians prior (enables better integration than unimodal Gaussian)
  - z_n: cell state + sample effects; function of u_n and sample ID s_n
- **Generative model**: observed counts x_n ~ NegBinomial(decode(z_n | nuisance covariates))
- **Nuisance covariates**: technical batch, protocol, study; condition on decoder but not in u/z
- **Target covariates**: biological sample identity (donor ID, perturbation ID); captured in z
- **Sample distance matrix**: for cell n, compute hypothetical z under each sample s' ≠ s_n; Euclidean distance between hypothetical states → per-cell sample-by-sample distance matrix
- **Exploratory analysis**: hierarchical clustering of sample distance matrices → sample groups per cell population
- **Comparative analysis**: test for differential gene expression between predefined sample groups at single-cell resolution
- **MoG prior**: mixture of Gaussians for u; outperforms single Gaussian for large diverse datasets

## 4. Key Results & Benchmarks
- COVID-19: de novo stratifies patients by severity via CD8+ T cell and NK cell subsets; clinically concordant grouping
- IBD: identifies pericyte subpopulation with stenosis-specific transcriptional changes not seen in bulk analysis
- Perturbation screen: groups small molecules by biochemical mechanism of action (MoA) based on cellular effects
- Integration: MoG prior achieves state-of-the-art integration on large datasets; competitive with scPoli and scVI
- Comparative DE: single-cell resolution reveals cell-type-specific differences invisible to pseudobulk approaches

## 5. Limitations & Future Work
- Scalability: sample distance matrix computation grows quadratically with number of samples
- Requires sufficient cells per sample for stable distance estimation
- Mixture of Gaussians prior adds computational complexity vs. standard scVI
- Future: integration with spatial data; longitudinal analysis; faster approximation of sample distances

## 6. Related Work
- scVI (Lopez et al., 2018) — foundational model; MrVI extends with sample-level hierarchy
- scANVI (Xu et al., 2021) — annotation-aware extension; MrVI is annotation-free
- scPoli (De Donno et al., 2023) — sample embedding approach; scPoli focuses on label transfer, MrVI on sample comparisons
- Milo (Dann et al.) — neighborhood-level differential abundance analysis; complementary to MrVI's cell-resolved approach
- popV (Ergen et al., 2024) — same Yosef group; annotation framework; MrVI provides underlying sample comparisons

## 7. Glossary
- **MrVI**: Multi-resolution Variational Inference — the hierarchical Bayesian model introduced here
- **Sample distance matrix**: per-cell matrix of pairwise distances between samples in z-space; core output of MrVI for exploratory analysis
- **u_n**: MrVI cell-state latent variable disentangled from sample identity; used for cell type annotation
- **z_n**: MrVI cell+sample latent variable capturing both cell state and sample-level variation; used for comparison
- **Nuisance covariate**: technical factor (batch, protocol) conditioned away in the decoder
- **Target covariate**: biological factor of interest (donor, perturbation) captured in z
- **MoG prior**: Mixture of Gaussians prior for u; more flexible than single Gaussian; improves integration
- **MoA (Mechanism of Action)**: biochemical pathway by which a compound exerts its effect; MrVI groups compounds by similar cellular MoA
