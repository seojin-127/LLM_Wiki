---
title: "Inferring and perturbing cell fate regulomes in human brain organoids"
authors: Jonas Simon Fleck, Sophie Martina Johanna Jansen, Damian Wollny, Fides Zenk, et al.
year: 2023
doi: 10.1038/s41586-023-06683-4
category: brain-development
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/4233689617/
source_collection: endnote
---

## One-line Summary
Pando framework infers a global GRN from multiome (scRNA + scATAC) time course in brain organoids; pooled CRISPR perturbation with scRNA-seq readout identifies GLI3 as required for cortical fate establishment; GLI3 regulomes control dorsoventral patterning and ganglionic eminence diversification.

## 1. Document Info
- Journal/Conference: Nature
- Published: September 2023

## 2. Key Contributions
- Pando: flexible GRN inference framework integrating multiome data + TF binding site predictions
- Dense time course: scRNA + scATAC of brain organoids covering neuroepithelial formation through neurogenesis
- Pooled CRISPR genetic perturbation + single-cell transcriptome readout in organoids
- GLI3 required for cortical fate establishment (recapitulates mammalian model results)
- Two GLI3 regulomes: (1) dorsoventral patterning via HES4/5; (2) ganglionic eminence diversification

## 3. Methods & Architecture
- Multiome (scRNA-seq + scATAC-seq) at dense time course during organoid development
- Pando: GRN inference using multi-omic data + TF motif predictions
- Pooled CRISPRko with scRNA-seq readout for TF perturbation

## 4. Key Results & Benchmarks
- Pando infers global GRN describing organoid brain development
- TF factors identified that regulate cell fate abundance vs. neuronal cell state post-differentiation
- GLI3 loss: disrupts cortical fate, aberrant ventral-fate specification
- GLI3 regulome 1: HES4/5 as direct targets for dorsoventral patterning
- GLI3 regulome 2: ganglionic eminence diversification at later stages

## 5. Limitations & Future Work
- Organoid model: variable regional identity limits GRN specificity
- Pando GRN: chromatin-based inference; experimental validation needed per interaction
- Dense time course requires large cell numbers

## 6. Related Work
- Zenk et al. 2024: histone modification atlas in organoids (complementary epigenomics)
- Deng et al. 2024: lentiMPRA regulatory elements in developing cortex (complementary)
- Zinati et al. 2024 (GRouNdGAN): GRN-guided simulation

## 7. Glossary
- **Pando**: Python-based GRN inference framework for multiome data
- **GLI3**: Transcription factor; Hedgehog signaling effector; required for cortical dorsal identity
- **Regulome**: Set of regulatory elements and target genes controlled by a specific factor
- **Ganglionic eminence**: Ventral telencephalic structure; source of GABAergic interneurons
