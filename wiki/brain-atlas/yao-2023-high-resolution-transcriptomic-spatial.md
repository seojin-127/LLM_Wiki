---
title: "A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain"
authors: Zizhen Yao, Cindy T.J. van Velthoven, et al. (Allen Institute)
year: 2023
doi: 10.1038/s41586-023-06812-z
source: yao-2023-high-resolution-transcriptomic-spatial.md
category: brain-atlas
tags: [Allen-Brain-Atlas, mouse, whole-brain, MERFISH, scRNA-seq, taxonomy, spatial, TF-code]
---

## Summary
Allen Brain Cell Atlas: ~4M scRNA-seq + 4.3M MERFISH cells from whole adult mouse brain. Hierarchical taxonomy: 34 classes, 338 subclasses, 1,201 supertypes, 5,322 clusters. Reveals dorsal-ventral dichotomy in neuronal diversity, extraordinary neuropeptide co-expression, and combinatorial TF code defining cell types brain-wide.

## Key Contributions
- ~4M scRNA-seq + 4.3M MERFISH cells; 5,322 clusters = highest-resolution whole-brain mouse atlas
- Four-level hierarchy: class → subclass → supertype → cluster
- Dorsal brain: fewer, more divergent types; ventral: more numerous, more similar types
- Combinatorial TF code: major determinant of cell type identity across all brain regions
- Allen Brain Cell Atlas online visualization platform

## Methods & Architecture
- scRNA-seq (~7M profiled, ~4M QC) + MERFISH spatial (4.3M cells)
- 4-level hierarchical clustering; scRNA-MERFISH integration for spatial assignment

## Results
- High correspondence between transcriptomic identity and spatial specificity
- Dorsal-ventral dichotomy in neuronal type organization
- Neuropeptide/neurotransmitter co-expression: extraordinary brain-wide diversity
- TF combinatorial code defines cell types in all brain regions

## Limitations
- Adult mouse only; developmental/aging covered by separate efforts
- MERFISH: targeted gene panel, not whole transcriptome
- Human equivalent atlas under construction

## Related Papers
- [[brain-atlas/van-velthoven-2025-transcriptomic-spatial-organization]] — telencephalic GABAergic atlas (subset, higher resolution)
- [[brain-atlas/winter-2023-transcriptomic-taxonomy-mouse]] — SPN taxonomy using this atlas as reference
- [[brain-atlas/zhang-2023-molecularly-defined-spatially]] — earlier MERFISH whole-brain atlas (complementary)
