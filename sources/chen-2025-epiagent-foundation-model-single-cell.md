---
title: "EpiAgent: foundation model for single-cell epigenomics"
authors: Xiaoyang Chen, Keyi Li, Xuejian Cui, Zian Wang, Qun Jiang, Jiacheng Lin, Zhen Li, Zijing Gao, Hairong Lv, Rui Jiang
year: 2025
doi: 10.1038/s41592-025-02822-z
category: single-cell-foundation
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/3039610999/
source_collection: endnote
---

## One-line Summary
EpiAgent: foundation model pretrained on large-scale Human-scATAC-Corpus; encodes chromatin accessibility as "cell sentences" via bidirectional attention; achieves state-of-the-art on scATAC-seq tasks including unsupervised clustering, cell type annotation, data imputation, perturbation prediction, and zero-shot annotation.

## 1. Document Info
- Journal/Conference: Nature Methods
- Published: November 2025

## 2. Key Contributions
- EpiAgent: first large-scale foundation model for scATAC-seq (single-cell epigenomics)
- Pretrained on Human-scATAC-Corpus (manually curated, large-scale)
- "Cell sentence" encoding: chromatin accessibility peaks → token sequence for bidirectional transformer
- Zero-shot cell type annotation from pretrained representations
- In silico CRE knockout: models cell state changes from cis-regulatory element perturbations
- Cellular response prediction for out-of-sample stimulations and unseen genetic perturbations

## 3. Methods & Architecture
- Bidirectional transformer (BERT-style) pretrained on scATAC-seq chromatin accessibility
- Input: accessible chromatin peaks encoded as "cell sentences" (avoids high-dimensional cell-by-cCRE matrix)
- Incorporates external embeddings for multi-modal tasks
- Fine-tuning for: cell type annotation, data imputation, perturbation response prediction

## 4. Key Results & Benchmarks
- Unsupervised feature extraction: superior clustering vs. ArchR, Signac
- Supervised cell type annotation: outperforms task-specific scATAC methods
- Data imputation: best-in-class reconstruction of sparse accessibility signal
- Zero-shot annotation: effective without task-specific fine-tuning
- In silico CRE knockout: predicts expected cell state shifts

## 5. Limitations & Future Work
- Human-only corpus; mouse/other species require adaptation
- Binary/sparse nature of scATAC-seq remains challenging for some tasks
- Integration with scRNA-seq (multi-omic) not primary focus

## 6. Related Work
- scGPT (Cui 2024): RNA-seq foundation model counterpart
- scFoundation (Hao 2024): large-scale scRNA-seq FM
- Domcke et al. 2020: fetal chromatin accessibility atlas (complementary data resource)

## 7. Glossary
- **scATAC-seq**: Single-cell ATAC sequencing; measures chromatin accessibility per cell
- **cCRE**: Candidate cis-regulatory element — accessible chromatin region potentially acting as enhancer/promoter
- **Cell sentence**: EpiAgent's representation of a cell as an ordered sequence of accessible peaks
- **CRE knockout**: In silico removal of a regulatory element to predict downstream transcriptomic effect
