---
title: "A human cell atlas of fetal chromatin accessibility"
authors: Silvia Domcke, Andrew J. Hill, Riza M. Daza, et al.
year: 2020
doi: 10.1126/science.aba7612
source: domcke-2020-human-cell-atlas-fetal.md
category: brain-atlas
tags: [fetal, chromatin-accessibility, ATAC-seq, human, sci-ATAC-seq3, TF-motif, multi-organ, endothelial]
---

## Summary
sci-ATAC-seq3 chromatin accessibility atlas from ~800K human fetal cells (15 organs, 59 samples, 89–125 PCW). TF motifs predict cell type affiliation; activators vs. repressors classified by expression-accessibility correlation. Endothelial chromatin is organ-specific; blood cell chromatin is conserved. Companion to Cao et al. 2020 gene expression atlas.

## Key Contributions
- sci-ATAC-seq3: scalable, low-cost single-cell ATAC-seq (3 rounds of combinatorial indexing)
- ~800K cells from 15 human fetal organs (89–125 PCW)
- TF motifs in accessible sites explain cell type affiliation; activator/repressor classification
- Endothelial: organ-specific chromatin; blood: conserved across organs

## Methods & Architecture
- sci-ATAC-seq3 on 59 fetal samples; cell annotation via Cao et al. paired gene expression
- TF motif enrichment per cell type; expression-accessibility correlation for activator/repressor classification

## Results
- ~800K cells; comprehensive fetal multi-organ chromatin atlas
- Novel and known TF regulators of cell fate specification identified
- Organ-specific endothelial chromatin; blood cell types chromatin conserved across organs

## Limitations
- 89–125 PCW only; earlier/later stages not covered
- Chromatin accessibility alone insufficient for transcriptional activity

## Related Papers
- [[brain-atlas/cao-2020-human-cell-atlas-fetal]] — companion human fetal gene expression atlas (same Science issue)
- [[brain-development/mannens-2025-chromatin-accessibility-during]] — first-trimester chromatin atlas of brain (earlier window)
