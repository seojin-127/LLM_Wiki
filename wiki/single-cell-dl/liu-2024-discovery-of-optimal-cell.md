---
title: "Discovery of optimal cell type classification marker genes from single cell RNA sequencing data"
authors: Liu, Angela, Peng, Beverly, Pankajam, Ajith V., Duong, Thu Elizabeth, Pryhuber, Gloria, Scheuermann, Richard H., Zhang, Yun
year: 2024
doi: 10.1186/s44330-024-00015-2
source: liu-2024-discovery-of-optimal-cell.md
category: single-cell-dl
tags: [NS-Forest, marker-genes, random-forest, cell-type-classification, HuBMAP, spatial-panel-design]
---

## Summary

NS-Forest v4.0 identifies minimal necessary-and-sufficient marker gene combinations for cell type classification using random forest feature importance followed by decision tree refinement. A new On-Target Fraction (OTF) metric quantifies how exclusively a marker is expressed in the target type. Applied to HuBMAP/BICCN brain, kidney, and lung atlases, NS-Forest v4.0 outperforms differential expression-based marker selection and earlier NS-Forest versions, producing compact gene panels useful for spatial transcriptomics.

## Key Contributions

- On-Target Fraction (OTF): selectivity metric 0–1; OTF=1 means marker expressed only in target type
- Modular decision tree step: allows user-defined vs. computed markers to be compared head-to-head
- Atlas-scale efficiency improvements; handles millions of cells across hundreds of cell types
- Outperforms Wilcoxon DE and Azimuth-style marker selection on F-beta score and OTF

## Methods & Architecture

Per cell type (one-vs-rest): (1) Random forest trained → gene importance scores; (2) Top genes screened for binary expression pattern (OTF threshold); (3) Decision tree built on candidate genes → minimal combination identified by pruning. v4.0 modularizes step 3, enabling external marker lists to be scored and compared. Output: minimal marker combination + OTF values + decision tree classifier per cell type.

## Results

- Brain (MTG): smaller, more selective marker sets than DE-based approaches
- Kidney (HuBMAP): highest F-beta vs. Wilcoxon + Azimuth reference markers
- Lung (HuBMAP): distinguishes closely related epithelial cell types where DE fails
- OTF >0.9 for most well-defined atlas clusters
- Spatial panel design: NS-Forest markers cover major cell types with minimal gene count

## Limitations

- Cluster quality limits marker quality; poorly defined clusters yield non-selective markers
- One-vs-rest design; hierarchical cell type relationships require multi-level application
- Runtime scales with cluster number for large atlases

## Related Papers

- [[single-cell-dl/aran-2019-reference-based-analysis-of]] — SingleR: reference annotation; NS-Forest provides the marker genes for such references
- [[single-cell-dl/dominguez-conde-2022-cross-tissue-immune-cell]] — CellTypist: uses curated gene lists; NS-Forest can provide systematic alternatives
- [[single-cell-dl/ergen-2024-consensus-prediction-cell]] — popV: annotation tool; NS-Forest marker genes feed into annotation frameworks
- [[brain-atlas/chen-2025-whole-cortex-in-situ]] — BARseq spatial: NS-Forest panels applicable to in situ spatial gene panels
