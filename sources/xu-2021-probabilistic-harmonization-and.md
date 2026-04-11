---
title: "Probabilistic harmonization and annotation of single-cell transcriptomics data with deep generative models"
authors: Xu, Chenling, Lopez, Romain, Mehlman, Edouard, Regier, Jeffrey, Jordan, Michael I., Yosef, Nir
year: 2021
doi: 10.15252/msb.20209620
category: single-cell-dl
pdf_path: papers/xu-2021-probabilistic-harmonization-and.pdf
pdf_filename: xu-2021-probabilistic-harmonization-and.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

scANVI extends scVI with a semi-supervised variational inference framework for simultaneous dataset harmonization and probabilistic cell type annotation, enabling label-aware integration that outperforms annotation-agnostic methods while preserving a unified generative model for downstream differential expression.

## 1. Document Info
- Journal/Conference: Molecular Systems Biology
- Received/Published: Published 2021 (DOI: 10.15252/msb.20209620); Received April 2020

## 2. Key Contributions
- scANVI (single-cell ANnotation using Variational Inference): semi-supervised extension of scVI that jointly learns harmonized embeddings and cell type annotation
- Fully probabilistic: uncertainty over cell type assignments propagates to downstream differential expression
- Handles partially labeled data: leverages existing annotations from reference datasets to guide query cell annotation
- Outperforms annotation-agnostic integration methods (scVI, Harmony) when labels are available; competitive with supervised methods

## 3. Methods & Architecture
- **Base**: scVI generative model (ZINB distribution, VAE encoder-decoder)
- **Semi-supervised extension**: cell type labels treated as latent variables with categorical prior; labeled cells pin cell type; unlabeled cells infer cell type posterior
- **Variational inference**: ELBO augmented with classification term; trained end-to-end on labeled + unlabeled cells simultaneously
- **Annotation**: posterior probability over cell types per cell; argmax gives predicted label; entropy gives uncertainty
- **Harmonization**: same latent space z used for both integration and annotation; batch effects removed via conditional decoding
- **Differential expression**: posterior predictive tests in harmonized z-space; probabilistically interpretable
- **Implementation**: scvi-tools Python package (formerly scVI)

## 4. Key Results & Benchmarks
- Outperforms scVI, Harmony, Seurat v3 anchor transfer on accuracy of cell type annotation
- Competitive with fully supervised methods (SVM, SingleR) while also performing harmonization
- Correctly transfers annotations across species, tissues, and technologies
- Differential expression in harmonized space: higher specificity than methods without probabilistic integration
- Benchmarked on pancreas, PBMC, mouse atlas datasets

## 5. Limitations & Future Work
- Performance degrades with very few labeled cells per type
- Cell type categories must be predefined; novel cell types appear as uncertain predictions
- Slower than Harmony for very large datasets
- scArches later enables reference mapping (add new data without retraining)

## 6. Related Work
- scVI (Lopez et al., 2018) — base unsupervised model that scANVI extends
- scArches (Lotfollahi et al., 2022) — transfer learning wrapper enabling scANVI reference mapping
- scPoli (De Donno et al., 2023) — prototype-based extension; scPoli outperforms scANVI in population-level integration
- SingleR (Aran et al., 2019) — reference-based annotation; supervised baseline
- Harmony (Korsunsky et al., 2019) — annotation-agnostic integration baseline

## 7. Glossary
- **scANVI**: single-cell ANnotation using Variational Inference — the semi-supervised model introduced here
- **Semi-supervised learning**: learning from a mix of labeled and unlabeled data; leverages annotation structure while handling unannotated cells
- **ELBO**: Evidence Lower Bound — variational inference objective; scANVI adds a classification term to the standard scVI ELBO
- **Categorical prior**: prior distribution over cell type labels; labeled cells fix this to a delta; unlabeled cells integrate over it
- **Harmonization**: removal of technical batch effects while preserving biological variation; joint embedding of multiple datasets
- **scvi-tools**: Python package unifying scVI, scANVI, scArches and related models (scverse ecosystem)
