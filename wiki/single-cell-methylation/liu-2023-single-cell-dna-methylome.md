---
title: "Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain"
authors: Hanqing Liu, Qiurui Zeng, Jingtian Zhou, Joseph R. Ecker, et al.
year: 2023
doi: 10.1038/s41586-023-06805-y
source: liu-2023-single-cell-dna-methylome.md
category: single-cell-methylation
tags: [DNA-methylation, mouse-brain, snmC-seq, Hi-C, 3D-genome, multi-omic, atlas, regulatory-network]
---

## Summary
Liu et al. built the first whole-brain single-cell DNA methylation and 3D multi-omic atlas of the adult mouse brain: 301,626 methylomes + 176,003 methylome+Hi-C profiles from 117 anatomical regions, defining 4,673 cell groups and 274 subclasses. 2.6M differentially methylated regions identified; spatial methylation patterns linked to transcription; multi-omic regulatory networks constructed.

## Key Contributions
- First brain-wide single-cell methylation atlas: 301K methylomes from 117 regions
- First brain-wide 3D multi-omic atlas: snm3C-seq (methylation + Hi-C), 176K profiles
- 4,673 methylation cell groups → 274 annotated subclasses
- 2.6M DMRs as potential regulatory elements; spatial methylation patterns
- TF → CRE → target gene regulatory networks integrating all three modalities
- Intragenic methylation + Hi-C predicts alternative isoform expression

## Methods & Architecture
- snmC-seq3 for methylation; snm3C-seq for joint methylation + chromatin conformation
- 117 anatomical dissectates; 55 mice; integration with snRNA-seq + snATAC-seq
- Brain-wide spatial transcriptomics for validation

## Results
- Methylation-based taxonomy aligns with transcriptomic (274 subclasses)
- Chromatin conformation diversity highest in neuronal genes; correlated with methylation and transcription
- Alternative isoform expression predicted from intragenic methylation + Hi-C

## Limitations
- Adult brain only; developmental dynamics not captured
- snm3C-seq: lower cell recovery than standard snRNA-seq

## Related Papers
- [[genomic-dl/zemke-2023-conserved-and-divergent-gene]] — cross-species multiomics in motor cortex; complementary methylation + ATAC approach
- [[brain-atlas/langlieb-2023-molecular-cytoarchitecture-of]] — companion transcriptomic atlas (same whole-brain adult mouse context)
- [[brain-development/trevino-2020-chromatin-accessibility-forebrain]] — chromatin in forebrain organoids (related epigenomic approach)
