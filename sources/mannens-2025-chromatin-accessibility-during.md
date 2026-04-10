---
title: "Chromatin accessibility during human first-trimester neurodevelopment"
authors: Camiel C. A. Mannens, Lijuan Hu, Peter Lönnerberg, Marijn Schipper, Caleb C. Reagor, Xiaofei Li, Xiaoling He, Roger A. Barker, Erik Sundström, Danielle Posthuma, Sten Linnarsson
year: 2025
doi: 10.1038/s41593-025-01933-2
category: brain-development
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/1698198906/Mannens-2025-Chromatin accessibility during hu.pdf
pdf_filename: Mannens-2025-Chromatin accessibility during hu.pdf
source_collection: endnote
---

## One-line Summary
Whole-brain first-trimester human neurodevelopment chromatin accessibility + paired gene expression atlas (135 clusters, 6–13 weeks), using a CNN to identify TF binding sites in enhancers and linking GWAS variants to CREs — identifies midbrain GABAergic neurons as most vulnerable to major depressive disorder mutations.

## 1. Document Info
- Journal/Conference: Nature (Nat. Neurosci. indicated in header)
- Published: November 2025 (Vol 647)

## 2. Key Contributions
- First whole-brain chromatin accessibility (ATAC-seq) + paired gene expression atlas of human first trimester (6–13 weeks post-conception)
- 135 clusters across whole developing brain (not forebrain-only)
- CNN identifies putative functional TF binding sites in cell-type-specific enhancers
- Applied CNN to ESRRB CREs to elucidate Purkinje cell lineage activation mechanism
- GWAS variant → CRE linking: identifies midbrain-derived GABAergic neurons as most vulnerable to major depressive disorder (MDD)-related mutations
- Accessible regions increase with both age and neuronal differentiation

## 3. Methods & Architecture
- Single-nucleus ATAC-seq (snATAC-seq) + paired RNA-seq from whole developing human brain
- 6–13 weeks post-conception (first trimester)
- 135 clusters; multiomic linkage of CREs to gene expression
- Convolutional neural network (CNN): trained on cell-type-specific ATAC peaks to identify TF binding sites
- Disease-associated SNP → CRE → gene linking for GWAS interpretation

## 4. Key Results & Benchmarks
- Accessible regions increase with developmental age and along neuronal differentiation trajectory
- CNN accurately identifies TF binding sites; applied to ESRRB for Purkinje cell lineage
- GWAS variant analysis: midbrain GABAergic neurons most enriched for MDD-associated CREs
- Multiple disease-associated variants validated via CRE linkage (schizophrenia, ASD, depression)

## 5. Limitations & Future Work
- First trimester only; second/third trimester and postnatal dynamics not covered
- Human fetal tissue: limited access and sample size
- CNN interpretability: TF binding predictions require experimental validation

## 6. Related Work
- Zemke et al. 2023: cross-species multiomics in motor cortex (related ATAC/methylation approach)
- Trevino et al. 2020: chromatin in forebrain organoids (forebrain-focused, complementary)
- Herring et al. 2022: human PFC postnatal development atlas

## 7. Glossary
- **snATAC-seq**: Single-nucleus ATAC-seq — chromatin accessibility at single-cell resolution
- **CNN**: Convolutional neural network — used here for TF binding site prediction from DNA sequence
- **CRE**: Cis-regulatory element — ATAC peak linked to gene regulation
- **ESRRB**: Estrogen-related receptor beta — TF; activation mechanism in Purkinje cells elucidated
- **MDD**: Major depressive disorder; midbrain GABAergic neurons most vulnerable based on GWAS
