---
title: "In vivo Perturb-Seq reveals neuronal and glial abnormalities associated with autism risk genes"
authors: Xin Jin, Sean K. Simmons, Amy Guo, Ashwin S. Shetty, Michelle Ko, Lan Nguyen, Vahbiz Jokhi, Elise Robinson, Paul Oyler, Nathan Curry, Giulio Deangeli, Simona Lodato, Joshua Z. Levin, Aviv Regev, Feng Zhang, Paola Arlotta
year: 2020
doi: 10.1126/science.aaz6063
category: neuroscience
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/0023489362/Jin_2020_Science_InVivoPerturbSeq_AutismGenes.pdf
pdf_filename: Jin_2020_Science_InVivoPerturbSeq_AutismGenes.pdf
source_collection: endnote
---

## One-line Summary
In vivo Perturb-Seq in the developing mouse neocortex screens 35 ASD/ND risk genes at single-cell resolution, revealing cell-type-specific and evolutionarily conserved gene modules in both neurons and glia.

## 1. Document Info
- Journal/Conference: Science
- Published: 27 November 2020 (Vol. 370, eaaz6063)

## 2. Key Contributions
- Developed in vivo Perturb-Seq: CRISPR-Cas9 frameshift mutations in 35 ASD/ND risk genes in pooled in utero injection → postnatal single-cell RNA-seq
- Identified 14 covarying gene modules across 5 cell classes (cortical projection neurons, inhibitory neurons, astrocytes, oligodendrocytes, microglia)
- 9 ASD/ND genes had significant effects across 5 modules in 4 cell classes
- Gene modules and affected cell types conserved in human brain and ASD patient brain data

## 3. Methods & Architecture
- In utero lentiviral delivery of CRISPR-Cas9 + pooled gRNA library targeting 35 ASD/ND risk genes at E12.5
- Single-cell RNA-seq of P7 mouse cortex; cells filtered for single perturbations using barcodes
- Weighted gene correlation network analysis (WGCNA) to identify 14 covarying gene modules
- Joint linear regression model to estimate perturbation effect sizes per module
- Co-analysis with human ASD patient scRNA-seq data (Velmeshev et al. 2019)

## 4. Key Results & Benchmarks
- 14 gene modules identified: some pan-cell-class (common biology), others cell-type-specific
- 9/35 genes had significant perturbation effects; both neuronal and glial cell classes affected
- Conservation of gene modules and affected cell types confirmed in human brain tissue
- Overlap between perturbed mouse modules and ASD patient transcriptomic phenotypes

## 5. Limitations & Future Work
- Mouse neocortex model; may not capture all human-specific ASD phenotypes
- Frameshift mutations model LoF; gain-of-function variants not assessed
- Limited to E12.5 injection window (cortical lineages); other brain regions not covered

## 6. Related Work
- ASD/ND risk gene lists: Satterstrom et al. 2020
- Human ASD single-cell data: Velmeshev et al. 2019
- In vitro Perturb-Seq (Dixit et al. 2016, Adamson et al. 2016)

## 7. Glossary
- **Perturb-Seq**: CRISPR perturbation combined with single-cell RNA-seq readout
- **ASD/ND**: Autism spectrum disorder / neurodevelopmental delay
- **WGCNA**: Weighted gene correlation network analysis — identifies co-regulated gene modules
- **In utero electroporation/injection**: Delivery of genetic constructs into embryonic brain in vivo
- **De novo LoF**: De novo loss-of-function variant — new mutation not inherited from parents
