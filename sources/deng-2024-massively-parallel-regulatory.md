---
title: "Massively parallel characterization of regulatory elements in the developing human cortex"
authors: Chengyu Deng, Sean Whalen, Marilyn Steyert, Ryan Ziffra, Pawel F. Przytycki, Fumitaka Inoue, et al.
year: 2024
doi: 10.1126/science.adh0559
category: genomic-dl
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/4179407654/
source_collection: endnote
---

## One-line Summary
lentiMPRA + deep learning evaluates >100K regulatory elements in developing human cortex and organoids; identifies 46,802 active enhancers; 164 psychiatric disorder variants show allele-specific enhancer activity; sequence-to-activity neural network predicts regulatory grammar.

## 1. Document Info
- Journal/Conference: Science
- Published: 2024 (PsychENCODE2)

## 2. Key Contributions
- lentiMPRA of >100K candidate regulatory elements in mid-gestation human cortical cells and cerebral organoids
- 46,802 enhancer-active sequences identified
- 164 psychiatric disorder-associated variants with differential allele-specific enhancer activity
- Sequence-to-activity neural network trained on lentiMPRA data → predicts regulatory grammar
- Organoid vs. primary cell MPRA comparison: organoids effective in vitro model for MPRA studies
- Massive in silico scanning of nucleotide variants predicting enhancer disruption

## 3. Methods & Architecture
- lentiMPRA (lentivirus-based massively parallel reporter assay): >100K sequences, cell-type-specific activity
- Mid-gestation human cortical cells + cerebral organoids
- Deep learning model: sequence → enhancer activity; trained on lentiMPRA data
- In silico saturation mutagenesis for variant effect prediction

## 4. Key Results & Benchmarks
- 46,802 active enhancers in developing human cortex
- Cell-type-specific enhancer activity resolved
- 164 psychiatric disorder variants show allele-specific activity differences
- DL model captures regulatory grammar; enables in silico variant scanning
- Organoids largely recapitulate primary cell MPRA results

## 5. Limitations & Future Work
- Mid-gestation window only; later stages not covered
- lentiMPRA measures isolated sequence activity (not genomic context)
- DL model trained on limited cell type diversity

## 6. Related Work
- Zemke et al. 2023: CRE prediction across species (complementary)
- Amiri et al. 2018: organoid enhancer atlas (earlier work in same area)
- Fleck et al. 2023: organoid GRN inference (complementary)

## 7. Glossary
- **lentiMPRA**: Lentivirus-based MPRA — tests enhancer activity of thousands of sequences simultaneously in hard-to-transfect cells
- **MPRA**: Massively parallel reporter assay
- **Allele-specific activity**: Different enhancer strength for reference vs. variant allele
- **Regulatory grammar**: Combinatorial rules of TF binding site arrangement determining enhancer activity
