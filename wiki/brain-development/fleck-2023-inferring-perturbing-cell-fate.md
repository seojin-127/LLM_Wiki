---
title: "Inferring and perturbing cell fate regulomes in human brain organoids"
authors: Jonas Simon Fleck, Sophie Martina Johanna Jansen, Damian Wollny, Fides Zenk, et al.
year: 2023
doi: 10.1038/s41586-023-06683-4
source: fleck-2023-inferring-perturbing-cell-fate.md
category: brain-development
tags: [GRN, multiome, scRNA-seq, scATAC-seq, CRISPR-perturbation, organoid, GLI3, Pando, TF-regulome, dorsoventral-patterning]
---

## Summary
Pando framework infers a global gene regulatory network (GRN) from multiome (scRNA-seq + scATAC-seq) time course in human brain organoids. Pooled CRISPR-knockout with scRNA-seq readout identifies GLI3 as required for cortical fate establishment. Two distinct GLI3 regulomes govern dorsoventral patterning (via HES4/5) and ganglionic eminence diversification.

## Key Contributions
- Pando: flexible GRN inference framework integrating multiome data + TF binding site predictions
- Dense time course multiome (scRNA + scATAC) covering neuroepithelial formation through neurogenesis
- Pooled CRISPR-knockout + single-cell transcriptome readout in organoids
- GLI3 required for cortical (dorsal) fate establishment — recapitulates mammalian in vivo results
- Two GLI3 regulomes: (1) dorsoventral patterning via HES4/5 direct targets; (2) ganglionic eminence diversification

## Methods & Architecture
- Multiome (scRNA-seq + scATAC-seq) at dense time course during organoid development
- Pando GRN inference: multi-omic data + TF motif predictions → global regulatory network
- Pooled CRISPRko library + scRNA-seq readout for TF perturbation in organoids

## Results
- Pando infers global GRN describing organoid brain development
- TFs identified that regulate cell fate abundance vs. neuronal cell state post-differentiation
- GLI3 KO: disrupts cortical fate; aberrant ventral-fate specification
- GLI3 regulome 1: HES4/5 as direct targets for dorsoventral patterning
- GLI3 regulome 2: ganglionic eminence diversification at later developmental stages

## Limitations
- Organoid model: variable regional identity limits GRN specificity
- Chromatin-based GRN inference; experimental validation needed per interaction
- Dense time course requires large cell numbers

## Related Papers
- [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction]] — histone modification atlas in organoids (complementary epigenomics)
- [[genomic-dl/deng-2024-massively-parallel-regulatory]] — lentiMPRA regulatory elements in developing cortex (complementary)
- [[brain-development/ding-2026-dissecting-gene-regulatory-networks]] — GRN dissection in human brain organoids (closely related)
