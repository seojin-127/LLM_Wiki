---
title: "Spatial atlas of the mouse central nervous system at molecular resolution"
authors: Hailing Shi, Yichun He, Yiming Zhou, et al.
year: 2023
doi: 10.1038/s41586-023-06569-5
source: shi-2023-spatial-atlas-mouse-cns.md
category: brain-atlas
tags: [STARmap, spatial, mouse, CNS, in-situ-sequencing, 3D, AAV, molecular-resolution, brain-spinal-cord]
---

## Summary
STARmap PLUS in situ sequencing at 194 nm voxel resolution maps 1.09M cells (1,022 genes) across adult mouse brain and spinal cord. Defines 230 molecular cell types and 106 molecular tissue regions; transcriptome-wide atlas via scRNA-seq integration (11,844 genes); AAV-PHP.eB tropism mapped at cell-type resolution.

## Key Contributions
- STARmap PLUS: 3D in situ sequencing at 194 × 194 × 345 nm³ voxels
- 1.09M cells, 1,022 genes, 230 cell types, 106 molecular tissue regions
- Novel tissue architectures identified beyond established brain anatomy
- scRNA-seq integration: transcriptome-wide (11,844 genes) spatial imputation
- AAV-PHP.eB viral tropism mapped at cell-type resolution

## Methods & Architecture
- STARmap PLUS click chemistry in situ sequencing in 3D; ClusterMap segmentation
- Integration with Allen Brain Atlas scRNA-seq for transcriptome-wide imputation

## Results
- 3D subcellular-resolution spatial atlas of entire CNS
- 230 molecular cell types; 106 tissue regions (some novel)
- AAV-PHP.eB: cell-type-specific tropism characterized

## Limitations
- 1,022-gene panel; transcriptome-wide via imputation (not direct)
- Mouse only; 3D section alignment errors possible

## Related Papers
- [[brain-atlas/zhang-2023-molecularly-defined-spatially]] — MERFISH whole mouse brain atlas (complementary)
- [[brain-atlas/yao-2023-high-resolution-transcriptomic-spatial]] — Allen Brain Cell Atlas (scRNA reference for integration)
