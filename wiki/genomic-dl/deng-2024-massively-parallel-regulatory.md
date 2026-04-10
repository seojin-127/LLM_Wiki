---
title: "Massively parallel characterization of regulatory elements in the developing human cortex"
authors: Chengyu Deng, Sean Whalen, Marilyn Steyert, et al.
year: 2024
doi: 10.1126/science.adh0559
source: deng-2024-massively-parallel-regulatory.md
category: genomic-dl
tags: [lentiMPRA, regulatory-elements, enhancer, deep-learning, psychiatric-disorder, developing-cortex, organoid, variant-effect]
---

## Summary
lentiMPRA + deep learning evaluates >100K regulatory sequences in developing human cortex and organoids. Identifies 46,802 active enhancers; 164 psychiatric disorder variants with allele-specific activity. Sequence-to-activity neural network predicts regulatory grammar and enables in silico variant scanning.

## Key Contributions
- lentiMPRA of >100K sequences; 46,802 active enhancers in developing cortex
- 164 psychiatric disorder variants with allele-specific enhancer activity
- Sequence-to-activity DL model: regulatory grammar + in silico saturation mutagenesis
- Organoids reproduce primary cell MPRA results

## Methods & Architecture
- lentiMPRA in mid-gestation human cortical cells + cerebral organoids
- DL model (sequence → enhancer activity) trained on lentiMPRA data; in silico variant scanning

## Results
- 46,802 active enhancers; cell-type-specific
- 164 psychiatric disorder variants show differential allele-specific enhancer activity
- DL model captures regulatory grammar; predicts variant effects genome-wide

## Limitations
- Mid-gestation only; isolated sequence context (not full genomic context)
- DL model trained on limited cell type diversity

## Related Papers
- [[genomic-dl/zemke-2023-conserved-and-divergent-gene]] — CRE prediction across species (complementary regulatory genomics)
- [[brain-development/amiri-2018-transcriptome-epigenome-landscape]] — organoid enhancer atlas (earlier work)
- [[brain-development/fleck-2023-inferring-perturbing-cell-fate]] — organoid GRN inference (complementary)
