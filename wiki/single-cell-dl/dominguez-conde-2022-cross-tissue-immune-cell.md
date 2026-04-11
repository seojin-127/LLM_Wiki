---
title: "Cross-tissue immune cell analysis reveals tissue-specific features in humans"
authors: Dominguez Conde, C., Xu, C., Jarvis, L. B., Rainbow, D. B., Wells, S. B., Gomes, T., Howlett, S. K., Suchanek, O., Polanski, K., King, H. W., Mamanova, L., Huang, N., Szabo, P. A., Richardson, L., Bolt, L., Fasouli, E. S., Mahbubani, K. T., Prete, M., Tuck, L., Richoz, N., Tuong, Z. K., Campos, L., Mousa, H. S., Needham, E. J., Pritchard, S., Li, T., Elmentaite, R., Park, J., Rahmani, E., Chen, D., Menon, D. K., Bayraktar, O. A., James, L. K., Meyer, K. B., Yosef, N., Clatworthy, M. R., Sims, P. A., Farber, D. L., Saeb-Parsy, K., Jones, J. L., Teichmann, S. A.
year: 2022
doi: 10.1126/science.abl5197
source: dominguez-conde-2022-cross-tissue-immune-cell.md
category: single-cell-dl
tags: [CellTypist, annotation, logistic-regression, immune-atlas, cross-tissue, TRM, CITE-seq, VDJ]
---

## Summary

A cross-tissue immune atlas of ~360K cells (16 tissues, 12 donors) built using CellTypist — a logistic regression annotation tool trained on curated immune reference data. CellTypist scales to millions of cells via SGD, identifies 101 immune cell types/states, and reveals tissue-specific macrophage adaptations, TRM cell diversity, and convergent erythrophagocytic phenotypes across tissues.

## Key Contributions

- CellTypist: logistic regression + SGD annotation; trained on curated public immune data (celltypist.org); fast and scalable to millions of cells
- 101 immune populations across 16 human tissues; donor-matched, paired scVDJ-seq
- Erythrophagocytic macrophages: convergent phenotype across spleen, liver, bone marrow, lymph nodes
- TRM cells: most clonally expanded; gd T and MAIT tissue distributions resolved by VDJ sequencing
- Public resource: celltypist.org with regularly updated models

## Methods & Architecture

CellTypist: multi-class logistic regression trained with SGD on curated harmonized public immune datasets. Per-cell prediction: probability vector over cell types; argmax = label; entropy = uncertainty. Atlas: scRNA-seq + scVDJ-seq from donor-matched 16 tissues → CellTypist automated annotation → expert curation → 101 final cell type labels.

## Results

- CellTypist rapid annotation: competitive accuracy with manual curation at 1M+ cell scale
- 101 immune populations; tissue-specific and convergent features characterized
- Macrophages: strongest tissue restriction; erythrophagocytic type in 4 tissues
- T cells: TRM most restricted + most clonally expanded; diverse gd/MAIT tissue distributions

## Limitations

- Deceased organ donor cohort; may not represent all living individual variation
- CellTypist reference completeness limits rare cell type annotation accuracy
- Snapshot; no longitudinal dynamics

## Related Papers

- [[single-cell-dl/aran-2019-reference-based-analysis-of]] — SingleR: Spearman reference annotation; CellTypist is faster alternative
- [[single-cell-dl/ergen-2024-consensus-prediction-cell]] — popV: ensemble annotation including CellTypist
- [[single-cell-dl/hao-2021-integrated-analysis-of-multimodal]] — Seurat WNN: multimodal atlas framework (Seurat preprocessing used upstream)
- [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]] — HNOCA: similar cross-dataset atlas construction
