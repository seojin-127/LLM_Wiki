---
title: "Probabilistic harmonization and annotation of single-cell transcriptomics data with deep generative models"
authors: Xu, Chenling, Lopez, Romain, Mehlman, Edouard, Regier, Jeffrey, Jordan, Michael I., Yosef, Nir
year: 2021
doi: 10.15252/msb.20209620
source: xu-2021-probabilistic-harmonization-and.md
category: single-cell-dl
tags: [scANVI, semi-supervised, VAE, annotation, harmonization, label-transfer, differential-expression]
---

## Summary

scANVI extends scVI with semi-supervised variational inference: cell type labels are treated as latent variables, so labeled reference cells anchor the label structure while unlabeled query cells jointly infer annotation and harmonized embedding. A single generative model simultaneously handles integration, annotation transfer, and downstream differential expression, outperforming annotation-agnostic methods (scVI, Harmony) when reference labels are available.

## Key Contributions

- Semi-supervised ELBO: adds classification term to scVI training; labeled cells fix cell type; unlabeled cells integrate over categorical posterior
- Posterior probability per cell type: probabilistic uncertainty, not just argmax label
- Single model for harmonization + annotation + differential expression; avoids inconsistency between separate tools
- Outperforms Harmony and Seurat v3 label transfer on annotation accuracy across pancreas, PBMC, mouse atlas

## Methods & Architecture

Extends scVI VAE: the encoder maps expression → z (with batch conditioning). Cell type labels y added as categorical latent variable with learned prior; labeled cells use observed y; unlabeled cells marginalize over y. The ELBO augmented with a categorical cross-entropy term for labeled cells. Annotation by argmax of p(y|x); uncertainty by entropy. Harmonized embedding z used for all downstream tasks.

## Results

- Outperforms scVI + Harmony + Seurat v3 on cell type annotation across multiple benchmarks
- Competitive with fully supervised classifiers (SVM, SingleR) while simultaneously integrating
- Correct cross-species, cross-tissue label transfer
- scIB benchmark (Luecken 2022): scANVI ranked top when labels available

## Limitations

- Degrades with very few labeled cells per type
- Novel cell types (absent from reference) yield uncertain predictions; no explicit rejection
- Slower than Harmony at very large scale

## Related Papers

- [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] — scVI: base model that scANVI extends
- [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]] — scArches: enables scANVI reference mapping without data sharing
- [[single-cell-dl/dedonno-2023-population-level-integration-of]] — scPoli: prototype-based extension; outperforms scANVI on population-level tasks
- [[single-cell-dl/luecken-2022-benchmarking-atlas-level-data]] — scIB: benchmark where scANVI is top labeled-integration method
- [[single-cell-dl/aran-2019-reference-based-analysis-of]] — SingleR: supervised baseline comparison
