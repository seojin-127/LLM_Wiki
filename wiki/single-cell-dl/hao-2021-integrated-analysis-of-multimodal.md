---
title: "Integrated analysis of multimodal single-cell data"
authors: Hao, Yuhan, Hao, Stephanie, Andersen-Nissen, Erica, Mauck, William M., Zheng, Shiwei, Butler, Andrew, Lee, Maddie J., Wilk, Aaron J., Darby, Charlotte, Zager, Michael, Hoffman, Paul, Stoeckius, Marlon, Papalexi, Efthymia, Mimitou, Eleni P., Jain, Jaison, Srivastava, Avi, Stuart, Tim, Fleming, Lamar M., Yeung, Bertrand, Rogers, Angela J., McElrath, Juliana M., Blish, Catherine A., Gottardo, Raphael, Smibert, Peter, Satija, Rahul
year: 2021
doi: 10.1016/j.cell.2021.04.048
source: hao-2021-integrated-analysis-of-multimodal.md
category: single-cell-dl
tags: [Seurat, WNN, multimodal, CITE-seq, ADT, integration, reference-mapping, immune-atlas]
---

## Summary

Seurat v4 introduces Weighted Nearest Neighbor (WNN) analysis: an unsupervised framework that learns per-cell modality weights from any combination of data types (RNA, protein, ATAC, etc.) and constructs a joint neighborhood graph. Applied to 211K PBMC CITE-seq profiles (RNA + 228 ADTs), WNN resolves T cell subtypes (gd, MAIT, NK subsets) invisible to RNA alone and enables reference-based multimodal mapping of new datasets.

## Key Contributions

- WNN: per-cell modality weights learned by comparing within-modality vs. cross-modality predicted neighborhoods; higher weight = more informative modality for that cell
- 211K PBMC CITE-seq multimodal reference atlas (228 antibodies); largest at publication
- Identifies and validates novel lymphoid subpopulations inaccessible to transcriptomics alone
- Reference-based multimodal mapping: maps query datasets onto WNN reference using cross-modality anchors
- Core algorithm in Seurat v4; widely adopted as standard multimodal analysis workflow

## Methods & Architecture

For each cell and modality: build within-modality kNN graph; compute predicted neighbors using other modalities; compare overlap to determine information content → per-cell modality weight. WNN graph = modality-weight-averaged combination of modality-specific graphs. Clustering (Louvain/Leiden) and UMAP applied to WNN graph. Seurat anchor framework extended to cross-modality reference mapping.

## Results

- WNN substantially improves T cell subset resolution vs. RNA-only or protein-only
- 211K PBMC reference: 21 major immune types; finer subpopulation resolution at sub-level
- Novel lymphoid subsets (DN T cells, MAIT subtypes) validated by surface co-expression
- Reference mapping generalizes to vaccine response and COVID-19 immune profiling datasets

## Limitations

- Requires paired same-cell multimodal measurements; unpaired data not directly handled (extended in Seurat v5)
- Protein panel must be designed a priori; missing key markers limit resolution
- Computationally demanding at >500K cells

## Related Papers

- [[single-cell-dl/schuster-2024-multidgd-versatile-deep]] — multiDGD: VAE for RNA+ATAC; complementary deep learning alternative to WNN
- [[single-cell-dl/dominguez-conde-2022-cross-tissue-immune-cell]] — CellTypist atlas: immune cell types defined using Seurat preprocessing
- [[single-cell-dl/luecken-2022-benchmarking-atlas-level-data]] — scIB: Seurat v3/v4 as benchmark baseline methods
- [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]] — scArches: alternative reference mapping framework
