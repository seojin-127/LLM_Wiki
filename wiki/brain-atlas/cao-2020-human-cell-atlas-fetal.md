---
title: "A human cell atlas of fetal gene expression"
authors: Junyue Cao, Diana R. O'Day, Cole Trapnell, Jay Shendure, et al.
year: 2020
doi: 10.1126/science.aba7721
source: cao-2020-human-cell-atlas-fetal.md
category: brain-atlas
tags: [fetal, multi-organ, sci-RNA-seq, cell-atlas, blood, trophoblast, 657-subtypes]
---

## Summary
Cao et al. applied sci-RNA-seq3 to 121 human fetal samples (72–129 days, 15 organs) to generate a 4M-cell atlas with 657 cell subtypes. Provides multi-organ cross-tissue reference for human fetal development; companion to Domcke et al. chromatin accessibility atlas (same Science issue). Key discovery: circulating trophoblast-like cells in unexpected organs.

## Key Contributions
- 4M cells, 121 samples, 15 organs, 657 subtypes — first comprehensive multi-organ fetal atlas
- Circulating trophoblast-like and hepatoblast-like cells in unexpected tissues
- Blood cell trajectory map: HSC → all sublineages across multiple organs
- Cell type specificity quantification framework

## Methods & Architecture
- sci-RNA-seq3 (3-level combinatorial indexing): highly scalable multiwell plate
- 15 organs at 72–129 days post-conception; cross-matched to mouse atlases

## Results
- 657 subtypes; broadly concordant with mouse atlas for shared types
- Unexpected circulating cell populations discovered
- Blood cell atlas across organs: trajectory from HSC to mature lineages

## Limitations
- Preliminary annotation (mouse cross-match); human-specific types may be mislabeled
- Unequal organ depth; some organs underrepresented

## Related Papers
- [[single-cell-methylation/liu-2023-single-cell-dna-methylome]] — companion chromatin modality (Domcke 2020 is the direct companion; Liu 2023 extends this)
- [[brain-atlas/langlieb-2023-molecular-cytoarchitecture-of]] — adult mouse brain atlas (complementary developmental context)
- [[brain-development/herring-2022-human-prefrontal-cortex-gene]] — human PFC development atlas (postnatal complement)
