---
title: "ChromBERT: A foundation model for learning interpretable representations for context-specific transcriptional regulatory networks"
authors: Zhaowei Yu, Dongxu Yang, Qianqian Chen, Yuxuan Zhang, Zhanhao Li, Yucheng Wang, Chenfei Wang, Yong Zhang
year: 2026
doi: 10.1016/j.xgen.2025.101130
category: genomic-dl
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/2345888234/
source_collection: endnote
---

## One-line Summary
ChromBERT: BERT-based foundation model pretrained on ~1,000 transcription regulators from large-scale human ChIP-seq data; learns genome-wide TF interaction syntax; enables imputation of unseen cistromes and context-specific TRN inference without additional ChIP-seq experiments.

## 1. Document Info
- Journal/Conference: Cell Genomics
- Published: April 2026

## 2. Key Contributions
- ChromBERT: foundation model learning interaction syntax of ~1,000 transcription regulators from ChIP-seq
- Genome-wide regulatory cooperation syntax learned from large-scale ENCODE/ChIP-seq data
- Prompt-enhanced fine-tuning for cistrome imputation in unseen cell types and single cells
- Context-specific TRN representations from lightweight fine-tuning
- Interprets key TF regulators driving cell state transitions — no additional ChIP-seq needed

## 3. Methods & Architecture
- BERT-style transformer pretrained on large-scale human ChIP-seq (covering ~1,000 TFs/co-regulators)
- Input: genomic regions + TF occupancy signals
- Prompt-enhanced fine-tuning for downstream cell-type-specific tasks
- Generates interpretable TRN representations usable for regulatory inference

## 4. Key Results & Benchmarks
- Cistrome imputation: outperforms existing methods for unseen TF binding profiles
- Context-specific TRN: captures regulatory dynamics across cell types without ChIP-seq
- Identifies key TF drivers of cell state transitions (validated against known regulators)
- Single-cell TRN inference: effective from sparse single-cell chromatin data

## 5. Limitations & Future Work
- Human-only pretraining
- ChIP-seq-based; doesn't directly model chromatin accessibility or 3D genome structure
- Interpretability of regulatory syntax still limited to known TF interactions

## 6. Related Work
- Enformer (Avsec 2021): sequence-to-expression genomic DL (complementary)
- deng-2024 (lentiMPRA): experimental regulatory element validation (complementary)
- EpiAgent (Chen 2025): scATAC-seq foundation model (related paradigm)

## 7. Glossary
- **Cistrome**: Genome-wide set of binding sites for a specific transcription factor (ChIP-seq derived)
- **TRN**: Transcriptional regulatory network — network of TF-target gene interactions
- **Prompt-enhanced fine-tuning**: Using learned prompts to adapt pretrained model to new tasks
- **ChromBERT**: Chromatin + BERT; trained on chromatin occupancy data
