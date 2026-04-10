---
title: "Transcriptome and epigenome landscape of human cortical development modeled in organoids"
authors: Anahita Amiri, Gianfilippo Coppola, Soraya Scuderi, Feinan Wu, et al.
year: 2018
doi: 10.1126/science.aat6720
source: amiri-2018-transcriptome-epigenome-landscape.md
category: brain-development
tags: [organoid, enhancer, epigenome, ChIP-seq, ASD, PsychENCODE, WGCNA, embryonic-cortex, regulatory-elements]
---

## Summary
PsychENCODE cortical organoid study profiling transcriptome and epigenome (H3K27ac, H3K27me3, H3K4me3) across 5–16 post-conception weeks. Identifies 96,375 gene-linked enhancers, stratified into activating (A-reg) and repressive (R-reg) categories. ASD de novo variants enriched in enhancers targeting specific TF binding sites. Validates organoids as a model for early human embryonic cortex.

## Key Contributions
- 96,375 gene-linked enhancers from Hi-C + ChIP-seq; 49,640 organoid-specific (not active in mid-fetal brain)
- WGCNA: 54 co-expressed gene modules + 29 co-active enhancer modules; 6 and 4 global supermodules
- A-reg vs. R-reg enhancer stratification based on gene expression correlation
- Human-lineage-gained enhancers active earliest — target radial glia growth genes
- ASD de novo variants disrupt homeodomain, Hes1, NR4A2, Sox3, NFIX binding sites in enhancers

## Methods & Architecture
- hiPSC-derived cortical organoids + isogenic fetal cortex
- RNA-seq + ChIP-seq (H3K27ac, H3K27me3, H3K4me3) time course
- Hi-C for promoter-enhancer linking; WGCNA for network analysis
- ASD de novo variant enrichment testing in enhancer modules

## Results
- Organoids model 5–16 PCW embryonic cortex; greatest transcriptional change at stem cell → progenitor transition
- 96,375 gene-linked enhancers; 49,640 unique to organoid stage
- A-regs and R-regs co-activate/repress linked gene modules
- ASD-implicated variants enriched in specific enhancer modules with known TF binding sites

## Limitations
- Bulk ChIP-seq: limited cell-type resolution
- Organoid window limited to 5–16 PCW equivalent; later fetal stages not covered
- Functional validation of individual enhancer–gene links needed

## Related Papers
- [[genomic-dl/deng-2024-massively-parallel-regulatory]] — lentiMPRA enhancers in developing cortex (complementary)
- [[brain-development/fleck-2023-inferring-perturbing-cell-fate]] — organoid GRN inference with Pando
- [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction]] — single-cell epigenomic atlas in organoids
