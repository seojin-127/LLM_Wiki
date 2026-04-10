---
title: "Conserved and divergent gene regulatory programs of the mammalian neocortex"
authors: Nathan R. Zemke, Ethan J. Armand, Wenliang Wang, Seoyeon Lee, Jingtian Zhou, Yang Eric Li, Hanqing Liu, Wei Tian, Joseph R. Nery, Rosa G. Castanon, Anna Bartlett, Julia K. Osteen, Daofeng Li, Xiaoyu Zhuo, Vincent Xu, Lei Chang, Keyi Dong, Hannah S. Indralingam, Jonathan A. Rink, Yang Xie, Michael Miller, Fenna M. Krienen, Qiangge Zhang, Naz Taskin, Jonathan Ting, Guoping Feng, Steven A. McCarroll, Edward M. Callaway, Ting Wang, Ed S. Lein, M. Margarita Behrens, Joseph R. Ecker, Bing Ren
year: 2023
doi: 10.1038/s41586-023-06819-6
category: genomic-dl
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/1466273892/Zemke-2023-Conserved and divergent gene regula.pdf
pdf_filename: Zemke-2023-Conserved and divergent gene regula.pdf
source_collection: endnote
---

## One-line Summary
Single-cell multiomics (RNA, ATAC, DNA methylation, 3D genome) from 200K+ cells across human/macaque/marmoset/mouse primary motor cortex reveals that transposable elements drive ~80% of human-specific CREs and that machine learning can predict CREs with preserved regulatory syntax across rodents to primates.

## 1. Document Info
- Journal/Conference: Nature
- Published: 14 December 2023

## 2. Key Contributions
- Cross-species single-cell multiomics atlas: 200K+ cells from primary motor cortex of human, macaque, marmoset, and mouse
- Transposable elements (TEs) contribute ~80% of human-specific candidate cis-regulatory elements (CREs) in cortical cells
- Divergence of TF expression correlates with species-specific epigenome landscapes
- Machine learning sequence-based predictors of CREs developed; demonstrates genomic regulatory syntax preserved from rodents to primates
- Epigenetic conservation + sequence similarity identifies functional CREs and improves GWAS interpretation

## 3. Methods & Architecture
- Single-cell RNA-seq, ATAC-seq, DNA methylation (snmC-seq), Hi-C from same tissue (primary motor cortex M1)
- 4 species: human, macaque, marmoset, mouse; 200K+ cells total
- CRE prediction: machine learning (sequence-based models) trained on ATAC peaks per species
- Comparative epigenomics: identifying conserved vs. species-specific CREs
- GWAS variant interpretation using predicted CREs

## 4. Key Results & Benchmarks
- ~80% of human-specific candidate CREs are TE-derived
- TF expression divergence → species-specific chromatin accessibility landscapes
- 3D genome organization reflects conserved and divergent regulatory features
- ML sequence models accurately predict CREs across species; syntax conserved rodent→primate
- Epigenetic conservation (+ sequence similarity) better predicts functional CREs than sequence alone

## 5. Limitations & Future Work
- Single brain region (primary motor cortex) — may not generalize to all cortical areas
- ML predictions are correlative; need experimental validation for individual CREs
- TE contribution to CREs may differ across cell types and brain regions

## 6. Related Work
- Trevino et al. 2020: chromatin accessibility in forebrain organoids
- Herring et al. 2022: human PFC multiomics
- Liu et al. 2023: single-cell DNA methylome and 3D chromatin

## 7. Glossary
- **CRE**: Cis-regulatory element — DNA sequence that regulates gene expression in cis
- **TE**: Transposable element — mobile DNA; major source of novel regulatory sequences
- **snmC-seq**: Single-nucleus methylcytosine sequencing — single-cell DNA methylation
- **Hi-C**: Proximity ligation sequencing for 3D genome conformation
- **Regulatory syntax**: Combinatorial TF binding motif arrangement preserved across species
