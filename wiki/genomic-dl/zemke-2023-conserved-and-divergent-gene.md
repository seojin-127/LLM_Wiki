---
title: "Conserved and divergent gene regulatory programs of the mammalian neocortex"
authors: Nathan R. Zemke, Ethan J. Armand, Bing Ren, Joseph R. Ecker, et al.
year: 2023
doi: 10.1038/s41586-023-06819-6
source: zemke-2023-conserved-and-divergent-gene.md
category: genomic-dl
tags: [CRE, transposable-elements, cross-species, multiomics, machine-learning, GWAS, neocortex]
---

## Summary
Zemke et al. performed cross-species single-cell multiomics (RNA, ATAC, DNA methylation, Hi-C) from 200K+ cells in primary motor cortex (human/macaque/marmoset/mouse). Key finding: ~80% of human-specific CREs are TE-derived. ML sequence-based predictors show that regulatory syntax is conserved from rodents to primates, enabling cross-species CRE prediction and improved GWAS variant interpretation.

## Key Contributions
- ~80% of human-specific CREs are transposable element–derived
- TF expression divergence → species-specific chromatin landscapes
- ML CRE predictors: regulatory syntax preserved rodent→primate
- Epigenetic conservation + sequence similarity outperforms sequence alone for CRE identification
- GWAS neurological trait variants interpretable via predicted CREs

## Methods & Architecture
- 4-species cross-species single-cell multiomics: RNA + ATAC + snmC-seq + Hi-C
- 200K+ cells from primary motor cortex M1 per species
- Sequence-based ML models trained on ATAC peaks; cross-species prediction benchmarked

## Results
- TEs: dominant source of human-specific CREs (80%)
- 3D genome shows conserved and divergent features mirroring CRE conservation
- ML models: high cross-species CRE prediction accuracy; syntax conserved across 70–90M years evolution
- Functional CRE identification improved by combining epigenetic conservation + sequence similarity

## Limitations
- Single brain region (M1); may not generalize
- ML predictions correlative; individual CREs need experimental validation

## Related Papers
- [[brain-development/trevino-2020-chromatin-accessibility-forebrain]] — chromatin accessibility in forebrain organoids; complementary ATAC approach
- [[brain-development/herring-2022-human-prefrontal-cortex-gene]] — human PFC snRNA-seq + snATAC-seq across development
- [[brain-development/liu-2025-human-specific-enhancer-fine]] — HAR enhancer (HARE5) driving human-specific cortical expansion
