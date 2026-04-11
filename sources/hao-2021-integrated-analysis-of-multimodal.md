---
title: "Integrated analysis of multimodal single-cell data"
authors: Hao, Yuhan, Hao, Stephanie, Andersen-Nissen, Erica, Mauck, William M., Zheng, Shiwei, Butler, Andrew, Lee, Maddie J., Wilk, Aaron J., Darby, Charlotte, Zager, Michael, Hoffman, Paul, Stoeckius, Marlon, Papalexi, Efthymia, Mimitou, Eleni P., Jain, Jaison, Srivastava, Avi, Stuart, Tim, Fleming, Lamar M., Yeung, Bertrand, Rogers, Angela J., McElrath, Juliana M., Blish, Catherine A., Gottardo, Raphael, Smibert, Peter, Satija, Rahul
year: 2021
doi: 10.1016/j.cell.2021.04.048
category: single-cell-dl
pdf_path: papers/hao-2021-integrated-analysis-of-multimodal.pdf
pdf_filename: hao-2021-integrated-analysis-of-multimodal.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

Seurat v4 introduces Weighted Nearest Neighbor (WNN) analysis, an unsupervised framework for multimodal single-cell data integration that learns cell-specific modality weights from CITE-seq (RNA + protein), resolving immune cell states inaccessible to transcriptomics alone and enabling reference-based mapping of new datasets.

## 1. Document Info
- Journal/Conference: Cell
- Received/Published: Published June 24, 2021 (DOI: 10.1016/j.cell.2021.04.048)

## 2. Key Contributions
- WNN (Weighted Nearest Neighbor): unsupervised framework learning per-cell modality weights, reflecting information content of each data type in each cell
- Applied to CITE-seq (RNA + 228 antibody-derived tags, ADTs) of 211,000 PBMCs — largest multimodal reference at publication
- Resolves immune cell states (e.g., gd T cells, MAIT cells, NK subtypes) that are inseparable by RNA alone
- Multimodal reference mapping: query datasets mapped onto reference using cross-modality anchors
- Part of Seurat v4 package; foundational for subsequent Seurat v5

## 3. Methods & Architecture
- **WNN graph construction**:
  1. Compute within-modality neighborhood graphs for each modality independently
  2. For each cell, estimate the modality-specific information content by comparing within-modality neighbors to cross-modality predicted neighbors
  3. Assign per-cell weights to each modality (higher weight = more informative for that cell)
  4. Combine modality-specific graphs using these weights into a unified WNN graph
- **CITE-seq processing**: RNA → Seurat normalization + PCA; ADT → CLR normalization + PCA
- **Clustering**: Louvain/Leiden on WNN graph; UMAP on WNN embedding
- **Reference mapping**: Seurat anchor-based transfer using cross-modality neighbors
- **Applications**: CITE-seq, ATAC+RNA (10x Multiome), spatial transcriptomics + protein

## 4. Key Results & Benchmarks
- WNN substantially improves cluster resolution vs. RNA-only or protein-only for T cell subtypes
- 211K PBMC CITE-seq reference: 21 immune cell types at first level, finer resolution at sub-levels
- Novel lymphoid subpopulations identified and validated by surface marker co-expression
- Vaccine/COVID-19 immune response interpretation via reference mapping
- Multimodal reference mapping generalizes to unseen datasets from different donors/technologies

## 5. Limitations & Future Work
- WNN requires paired measurements in the same cell; not applicable when modalities are unpaired
- Protein panel must be designed a priori; missing markers limit resolution
- Computational cost scales with number of modalities and cells
- Extended in Seurat v5: bridge integration for modality alignment without paired data

## 6. Related Work
- Seurat v3 (Stuart et al., 2019) — anchor-based integration (RNA-only); predecessor
- multiDGD (Schuster et al., 2024) — VAE for RNA+ATAC joint representation; complementary
- scVI / scArches — alternative probabilistic integration frameworks
- CellTypist (Dominguez Conde et al., 2022) — logistic regression annotation; uses Seurat preprocessing as input
- CITE-seq (Stoeckius et al., 2017) — the multimodal technology enabling WNN analysis

## 7. Glossary
- **WNN (Weighted Nearest Neighbor)**: the key method — per-cell modality-weighted graph combining multiple data types
- **CITE-seq**: Cellular Indexing of Transcriptomes and Epitopes by Sequencing — simultaneous RNA + surface protein quantification via oligonucleotide-conjugated antibodies
- **ADT (Antibody-Derived Tag)**: sequencing-based readout of surface protein levels in CITE-seq
- **CLR normalization**: Centered Log Ratio normalization — applied to ADT counts before PCA
- **Modality weight**: per-cell scalar reflecting how informative a given modality is for defining that cell's identity
- **Anchor**: matched cell pairs across datasets or modalities used by Seurat for integration and label transfer
- **Seurat v4**: the R package version containing WNN and reference mapping; standard scRNA-seq analysis suite
