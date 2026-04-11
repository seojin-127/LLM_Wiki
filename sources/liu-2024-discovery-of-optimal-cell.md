---
title: "Discovery of optimal cell type classification marker genes from single cell RNA sequencing data"
authors: Liu, Angela, Peng, Beverly, Pankajam, Ajith V., Duong, Thu Elizabeth, Pryhuber, Gloria, Scheuermann, Richard H., Zhang, Yun
year: 2024
doi: 10.1186/s44330-024-00015-2
category: single-cell-dl
pdf_path: papers/liu-2024-discovery-of-optimal-cell.pdf
pdf_filename: liu-2024-discovery-of-optimal-cell.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

NS-Forest v4.0 uses random forest feature importance + decision trees to identify minimal combinations of necessary and sufficient marker genes for cell type classification, with a new On-Target Fraction metric for selectivity; outperforms prior methods on brain, kidney, and lung HuBMAP/HCA atlas datasets.

## 1. Document Info
- Journal/Conference: BMC Methods
- Received/Published: Published 2024 (DOI: 10.1186/s44330-024-00015-2)

## 2. Key Contributions
- NS-Forest v4.0 (Necessary and Sufficient Forest): random forest + decision tree pipeline for identifying minimal, binary-expression marker gene combinations for cell type classification
- On-Target Fraction (OTF) metric: quantifies how exclusively a marker is expressed in the target cell type vs. all others; ranges 0–1
- Modular decision tree step: allows comparison of user-defined vs. NS-Forest-derived marker combinations
- Outperforms marker selection by differential expression (Wilcoxon, Azimuth) and previous NS-Forest versions
- Applicable to atlas-scale datasets (millions of cells); useful for spatial transcriptomics panel design

## 3. Methods & Architecture
- **Step 1**: Random forest trained per cell type (one-vs-rest); gene importance scores extracted
- **Step 2**: Top-ranked genes by importance screened for binary expression pattern (high in target, low in others)
- **Step 3**: Decision tree classifier built using top gene candidates; minimal combination identified by pruning
- **New in v4.0**: modular decision tree step separable from RF; OTF metric computed for each candidate marker; efficiency improvements for atlas-scale data
- **On-Target Fraction (OTF)**: fraction of cells expressing a marker that belong to the target cell type; measures exclusivity of expression
- **Output**: minimal marker gene combination per cell type + OTF scores + decision tree classifier

## 4. Key Results & Benchmarks
- Brain (MTG, AIBS): NS-Forest v4.0 identifies smaller, more selective marker sets than DE-based approaches
- Kidney (HuBMAP): higher F-beta score than Wilcoxon DE + Azimuth reference markers
- Lung (HuBMAP): best marker gene combinations for distinguishing closely related epithelial cell types
- OTF > 0.9 achieved for most cell types in well-defined atlas clusters
- Utility for spatial transcriptomics: compact gene panels derived from NS-Forest markers cover major cell types

## 5. Limitations & Future Work
- Performance depends on cluster quality in input data; poorly defined clusters yield poor markers
- One-vs-rest design may not identify the best markers for hierarchical cell type relationships
- Runtime increases with cluster number for very large atlases
- Future: integration with cell type ontology (CL); automated ASCT+B table generation

## 6. Related Work
- Differential expression methods (Wilcoxon, edgeR) — standard marker identification; NS-Forest outperforms for classification
- Azimuth (Hao et al.) — Seurat reference-based annotation using DE markers; comparison baseline
- SingleR (Aran et al., 2019) — reference-based annotation; complementary (annotation) vs. NS-Forest (marker discovery)
- Cell Ontology (CL) — ontology for standardizing cell type definitions; downstream use of NS-Forest markers

## 7. Glossary
- **NS-Forest**: Necessary and Sufficient Forest — the marker gene selection algorithm
- **On-Target Fraction (OTF)**: proportion of expressing cells that belong to the target cell type; measures marker exclusivity
- **Random forest**: ensemble of decision trees; NS-Forest uses feature importance from random forest to rank candidate marker genes
- **Binary expression pattern**: gene that is highly expressed in target cell type and minimally expressed in all others; ideal marker criterion
- **F-beta score**: weighted harmonic mean of precision and recall; used to evaluate cell type classification quality
- **ASCT+B table**: Anatomical Structures, Cell Types, and Biomarkers table; HuBMAP resource; NS-Forest markers can populate these tables
- **HuBMAP**: Human BioMolecular Atlas Program — NIH initiative to map the human body at molecular resolution
