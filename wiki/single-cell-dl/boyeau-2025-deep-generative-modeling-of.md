---
title: "Deep generative modeling of sample-level heterogeneity in single-cell genomics"
authors: Boyeau, Pierre, Hong, Justin, Gayoso, Adam, Kim, Martin, McFaline-Figueroa, Jose L., Jordan, Michael I., Azizi, Elham, Ergen, Can, Yosef, Nir
year: 2025
doi: 10.1038/s41592-025-02808-x
source: boyeau-2025-deep-generative-modeling-of.md
category: single-cell-dl
tags: [MrVI, sample-heterogeneity, hierarchical-VAE, cohort-analysis, COVID-19, IBD, perturbation, sample-distance]
---

## Summary

MrVI is a hierarchical Bayesian generative model for cohort-level single-cell studies. Two latent variables per cell — u (cell state, disentangled from sample) and z (cell state + sample effects) — enable per-cell sample distance matrix computation. This allows annotation-free discovery of clinically relevant sample groups manifested in specific cell subsets. Applied to COVID-19 (T cell severity stratification), IBD (pericyte stenosis subpopulation), and perturbation screens (compound MoA clustering). Part of the scvi-tools ecosystem.

## Key Contributions

- Per-cell sample distance matrix: for each cell, pairwise distances between samples based on counterfactual z projections
- Annotation-free sample stratification: discovers clinically relevant sample groups without predefined cell types or labels
- Mixture of Gaussians prior for u: state-of-the-art integration performance on large diverse cohorts
- Applicable to perturbation screens: groups compounds by mechanism of action from cellular effects
- Open-source at scvi-tools.org

## Methods & Architecture

Hierarchical VAE: u_n (Mixture of Gaussians prior, cell state) and z_n = f(u_n, sample ID s_n) (cell state + sample effect). Observed counts decoded from z_n conditioned on nuisance covariates. Sample distance matrix: for cell n, compute hypothetical z under each sample s'≠s_n; pairwise Euclidean distances → per-cell sample-by-sample matrix. Hierarchical clustering on matrices → annotation-free sample groups per cell population.

## Results

- COVID-19: de novo patient severity stratification via CD8+ T cell and NK cell subsets
- IBD: pericyte subpopulation with stenosis-specific transcriptional changes (novel, invisible to bulk)
- Perturbation screen: MoA grouping of small molecules matches known biochemical pathway groupings
- Integration: MoG prior achieves SOTA on large dataset integration benchmark

## Limitations

- Sample distance matrix computation quadratic in sample number
- Requires sufficient cells per sample for stable distance estimates
- MoG prior adds compute vs. standard scVI

## Related Papers

- [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] — scVI: base model that MrVI hierarchically extends
- [[single-cell-dl/dedonno-2023-population-level-integration-of]] — scPoli: sample embedding approach; scPoli focuses on label transfer, MrVI on sample comparison
- [[single-cell-dl/xu-2021-probabilistic-harmonization-and]] — scANVI: annotation-aware integration; MrVI annotation-free
- [[single-cell-dl/ergen-2024-consensus-prediction-cell]] — popV: annotation tool from same Yosef group
