---
title: "Whole-cortex in situ sequencing reveals input-dependent area identity"
authors: Xiaoyin Chen, Stephan Fischer, Mara C.P. Rue, et al.
year: 2025
doi: 10.1038/s41586-025-09043-6
source: chen-2025-whole-cortex-in-situ.md
category: brain-atlas
tags: [BARseq, in-situ-sequencing, cortical-area, mouse, sensory-input, transcriptomic-type, areal-identity]
---

## Summary
BARseq of 10.3M cells (4.2M neurons, 104 genes) across 9 mouse cortical hemispheres. Transcriptomic type composition predicts cortical area identity; areas with similar composition are highly interconnected (cortical modules). Neonatal binocular enucleation shifts visual area types toward neighboring areas — sensory input sharpens area identity.

## Key Contributions
- BARseq: 10.3M cells, 4.2M cortical neurons, 104 genes, 9 hemispheres
- Transcriptomic type composition predicts cortical area identity
- Cortical modules = shared transcriptomic type composition + high connectivity
- Binocular enucleation: visual area types shift → sensory input required for area identity sharpening

## Methods & Architecture
- High-throughput in situ BARseq (104 cell-type markers, 9 hemispheres)
- De novo single-neuron clustering; neonatal enucleation developmental perturbation

## Results
- Transcriptomic composition → area identity prediction
- Cortical modules overlap with anatomical connectivity modules
- Enucleation → visual cortex transcriptomic types shift toward non-visual neighboring areas

## Limitations
- 104-gene targeted panel; not whole transcriptome
- Mouse only; developmental perturbation is coarse

## Related Papers
- [[brain-atlas/yao-2023-high-resolution-transcriptomic-spatial]] — Allen Brain Cell Atlas (scRNA reference for BARseq types)
- [[brain-atlas/zhang-2023-molecularly-defined-spatially]] — MERFISH whole-brain atlas (complementary spatial)
