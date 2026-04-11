---
title: "Cross-tissue immune cell analysis reveals tissue-specific features in humans"
authors: Dominguez Conde, C., Xu, C., Jarvis, L. B., Rainbow, D. B., Wells, S. B., Gomes, T., Howlett, S. K., Suchanek, O., Polanski, K., King, H. W., Mamanova, L., Huang, N., Szabo, P. A., Richardson, L., Bolt, L., Fasouli, E. S., Mahbubani, K. T., Prete, M., Tuck, L., Richoz, N., Tuong, Z. K., Campos, L., Mousa, H. S., Needham, E. J., Pritchard, S., Li, T., Elmentaite, R., Park, J., Rahmani, E., Chen, D., Menon, D. K., Bayraktar, O. A., James, L. K., Meyer, K. B., Yosef, N., Clatworthy, M. R., Sims, P. A., Farber, D. L., Saeb-Parsy, K., Jones, J. L., Teichmann, S. A.
year: 2022
doi: 10.1126/science.abl5197
category: single-cell-dl
pdf_path: papers/dominguez-conde-2022-cross-tissue-immune-cell.pdf
pdf_filename: dominguez-conde-2022-cross-tissue-immune-cell.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

A cross-tissue immune atlas of ~360K cells from 16 tissues (12 donors) combined with CellTypist — a logistic regression machine learning tool for rapid automated cell type annotation — identifies 101 immune populations, revealing tissue-specific adaptations and convergent phenotypes in T and B cell lineages.

## 1. Document Info
- Journal/Conference: Science
- Received/Published: Published May 13, 2022 (DOI: 10.1126/science.abl5197)

## 2. Key Contributions
- CellTypist: logistic regression-based automated cell type annotation tool; trained on curated immune cell reference database (celltypist.org); fast and precise
- Cross-tissue immune atlas: ~360K immune cells from 16 tissues (donor-matched) + VDJ sequencing for T and B cell repertoire
- 101 immune cell types/states identified; tissue-specific and convergent features characterized
- Erythrophagocytic macrophage phenotype convergently found in spleen, liver, bone marrow, lymph nodes
- TRM (tissue-resident memory T) cells most clonally expanded; highest clonal sharing between TRM and effector memory

## 3. Methods & Architecture
- **CellTypist**: logistic regression classifier with stochastic gradient descent (SGD) learning
  - Trained on curated + harmonized public immune cell datasets
  - Input: normalized gene expression per cell
  - Output: cell type probability per cell; argmax for annotation
  - Mini-batch SGD: scalable to millions of cells
  - Reference database: celltypist.org (publicly accessible, regularly updated)
- **Single-cell profiling**: scRNA-seq + scVDJ-seq (paired TCR/BCR) on donor-matched 12 deceased organ donors, up to 16 tissues per donor
- **Annotation pipeline**: CellTypist → manual expert curation → final cell type labels
- **Cross-tissue analysis**: expression modules, tissue-specific signatures, repertoire dynamics

## 4. Key Results & Benchmarks
- CellTypist: rapid annotation of >1M cells; competitive accuracy with manual curation
- 101 immune populations across 16 tissues; many underappreciated tissue-specific states
- Macrophages: strongest tissue restriction; erythrophagocytic phenotype convergently expressed in 4 tissues
- T cell memory: TRM more spatially restricted than effector/central memory; highest clonal expansion
- B cells: plasma cells restricted to gut/bone marrow; memory B cells more widely distributed
- gd T and MAIT cells: tissue-specific distributions resolved by VDJ sequencing

## 5. Limitations & Future Work
- Deceased organ donors: may not fully represent healthy living individuals
- CellTypist performance depends on reference completeness; rare cell types may be mis-annotated
- Snapshot analysis; does not capture temporal dynamics of immune response
- Future: CellTypist models updated with new cell type definitions; integration with spatial data

## 6. Related Work
- SingleR (Aran et al., 2019) — Spearman correlation-based annotation; CellTypist is faster and more scalable
- popV (Ergen et al., 2024) — ensemble annotation including CellTypist and other methods
- Seurat label transfer — alternative annotation via anchors
- Human Cell Atlas immune component — broader cross-tissue profiling effort

## 7. Glossary
- **CellTypist**: the annotation tool — logistic regression with SGD; scales to millions of cells
- **SGD (Stochastic Gradient Descent)**: mini-batch optimization; enables scalable model training
- **TRM (Tissue-Resident Memory T cells)**: memory T cells permanently residing in non-lymphoid tissues; tissue-adapted immune surveillance
- **VDJ sequencing (scVDJ-seq)**: single-cell sequencing of T cell receptor (TCR) and B cell receptor (BCR) variable regions; reveals clonal structure
- **Clonal expansion**: proliferation of immune cells sharing the same antigen receptor; indicates antigen-driven response
- **Erythrophagocytic macrophage**: macrophage specialized in clearing aged/dead red blood cells; found convergently across multiple tissues
- **MAIT (Mucosal-Associated Invariant T) cells**: innate-like T cells with semi-invariant TCR; restricted tissue distribution
