---
title: "The molecular cytoarchitecture of the adult mouse brain"
authors: Jonah Langlieb, Nina S. Sachdev, et al.
year: 2023
doi: 10.1038/s41586-023-06808-9
source: langlieb-2023-molecular-cytoarchitecture-of.md
category: brain-atlas
tags: [mouse, brain-atlas, snRNA-seq, spatial, Slide-seq, neuropeptide, heritability]
---

## Summary
Langlieb et al. built a whole-brain adult mouse atlas by combining high-throughput snRNA-seq from 92 anatomical dissectates with Slide-seq spatial transcriptomics, mapping cell type identity to specific neuroanatomical structures. Cell type diversity is highest in midbrain, hindbrain, and hypothalamus. The atlas also maps neuropeptide/neurotransmitter co-expression and shows GWAS heritability enrichment in specific cell types for psychiatric traits. Available at BrainCellData.org.

## Key Contributions
- Comprehensive cell type–to–neuroanatomical structure mapping for whole adult mouse brain
- Highest cell type diversity in midbrain/hindbrain/hypothalamus (≥3 markers needed)
- Complete neuropeptide/neurotransmitter signaling atlas
- Heritability enrichment: psychiatric/neurological GWAS traits linked to specific cell types
- Resource: BrainCellData.org + genetic access framework

## Methods & Architecture
- 92 anatomical dissectates, 55 mice → snRNA-seq (high throughput)
- Slide-seq (near-cellular spatial transcriptomics) paired for spatial mapping
- S-LDSC heritability partitioning for disease trait enrichment

## Results
- Midbrain/hindbrain/hypothalamus: most diverse; cortex: relatively simpler
- Region-specific activity-regulated gene expression programs
- Schizophrenia, depression heritability enriched in identified cell types

## Limitations
- Adult only; no developmental data
- Slide-seq ~10 µm resolution (near-cellular, not single-cell)

## Related Papers
- [[brain-atlas/zhang-2023-molecularly-defined-spatially]] — complementary MERFISH whole-brain atlas (same year, Nature)
- [[brain-atlas/gao-2025-continuous-cell-type-diversification]] — developmental trajectory atlas (mouse cortex)
- [[brain-atlas/steyn-2024-temporal-cortex-cell-atlas]] — human temporal cortex cell atlas
