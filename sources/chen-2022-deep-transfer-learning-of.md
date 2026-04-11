---
title: "Deep transfer learning of cancer drug responses by integrating bulk and single-cell RNA-seq data"
authors: Junyi Chen, Xiaoying Wang, Anjun Ma, Qi-En Wang, Bingqiang Liu, Lang Li, Dong Xu, Qin Ma
year: 2022
doi: 10.1038/s41467-022-34277-7
category: drug-resistance
pdf_path: papers/chen-2022-deep-transfer-learning-of.pdf
pdf_filename: chen-2022-deep-transfer-learning-of.pdf
source_collection: downloads-perturb-batch
---

## One-line Summary

scDEAL transfers knowledge from bulk cancer cell-line drug-response data (GDSC, CCLE) to single-cell drug response prediction via a Domain-adaptive Neural Network (DaNN), harmonizing bulk and scRNA-seq feature spaces with denoising autoencoders and cluster-regularized loss — achieving ~0.90 F1 across six benchmark drug-treated scRNA-seq datasets.

## 1. Document Info
- Journal: Nature Communications, 2022, 13:6494
- Received: 6 August 2021
- Accepted: 19 October 2022

## 2. Key Contributions

- **Bulk → single-cell transfer learning**: uses GDSC/CCLE bulk drug-response data (where labels are abundant) to train a predictor, then adapts to scRNA-seq via DaNN where labels are scarce.
- **Two denoising autoencoders** (bulk + scRNA-seq) share a low-dim feature space; Maximum Mean Discrepancy loss aligns distributions.
- **Cell cluster regularization**: retains single-cell heterogeneity during transfer (otherwise scRNA-seq would be pulled to bulk centroid).
- **Integrated gradient attribution**: identifies signature genes contributing to drug response predictions.
- Benchmarked on 6 scRNA-seq datasets × 5 drugs (Cisplatin, Gefitinib, I-BET-762, Docetaxel, Erlotinib) with ground-truth sensitivity labels.

## 3. Methods & Architecture

1. **Bulk feature extractor** (DAE E_b, D_b): denoising autoencoder on bulk cell-line expression.
2. **Bulk drug-response predictor** (P): fully connected classifier from bulk features to sensitive/resistant.
3. **Single-cell feature extractor** (DAE E_s, D_s): separate denoising autoencoder on scRNA-seq.
4. **Domain adaptation**: Maximum Mean Discrepancy loss between bulk and single-cell features → shared latent space.
5. **Cluster regularization**: single-cell clustering results regularize loss to prevent heterogeneity collapse.
6. **Transfer**: trained predictor applied to single-cell features → per-cell drug response.

## 4. Key Results & Benchmarks

- Average across 6 datasets: F1 = 0.892, AUROC = 0.898, AP = 0.944, precision = 0.926, recall = 0.899.
- Predicted response UMAPs track cell clusters and treatment conditions.
- Integrated gradient gene signatures overlap with known drug-resistance markers.
- Pseudotime analysis: drug-response probability aligns with treatment trajectory.

## 5. Limitations & Future Work

- Supervised transfer still requires abundant labeled bulk data (GDSC/CCLE) — extends to drugs in those screens only.
- Binary sensitive/resistant labels discard continuous dose-response information.
- MMD alignment can force bulk-like patterns onto scRNA-seq, muting genuine single-cell heterogeneity if cluster regularization is weak.
- Does not explicitly model cell-type-specific response mechanisms.
- Integrated gradient attribution is sensitive to baseline choice.

## 6. Related Work

- scGen, CPA, chemCPA — generative perturbation models that do not use bulk transfer.
- PrePR-CT (Alsulami 2026) — graph-prior alternative for cell-type-specific drug responses.
- scDrug, DeepCDR — bulk drug response prediction ancestors.

## 7. Glossary

- **DaNN**: Domain-adaptive Neural Network — aligns source (bulk) and target (single-cell) domain feature distributions.
- **MMD**: Maximum Mean Discrepancy — distance between distributions used as domain-adaptation loss.
- **DAE**: Denoising Autoencoder — encoder/decoder trained with corrupted inputs for robust feature extraction.
- **GDSC / CCLE**: Genomics of Drug Sensitivity in Cancer / Cancer Cell Line Encyclopedia — bulk drug response databases.
- **Integrated gradients**: attribution method for neural networks that integrates gradient along a path from baseline to input.
