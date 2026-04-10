---
title: "Effective gene expression prediction from sequence by integrating long-range interactions"
authors: Žiga Avsec, Vikram Agarwal, Daniel Visentin, et al.
year: 2021
doi: 10.1038/s41592-021-01252-x
category: genomic-dl
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/2956304341/
source_collection: endnote
---

## One-line Summary
Enformer: self-attention transformer for predicting gene expression and chromatin states from 196kb DNA sequences in human and mouse; substantially improves long-range regulatory element integration; outperforms CNNs on eQTL and CRISPRi enhancer benchmarks.

## 1. Document Info
- Journal/Conference: Nature Methods
- Published: 2021

## 2. Key Contributions
- Enformer: transformer-based model predicting 5,313 human + 1,643 mouse genomic tracks from 196kb DNA input
- Self-attention replaces convolution-only architecture → far greater receptive field for distal regulatory elements
- Improved long-range enhancer-gene interaction modeling (>20kb, previously impossible for CNNs)
- Better eQTL effect prediction vs. prior models
- Improved CRISPRi enhancer validation benchmarks

## 3. Methods & Architecture
- Input: 196,608bp DNA sequence (human or mouse)
- Encoder: convolutional stem + transformer blocks with self-attention
- Output: 5,313 human + 1,643 mouse epigenetic/transcriptional tracks (CAGE, ATAC, ChIP-seq, RNA-seq)
- Multitask prediction across tissues and cell types simultaneously
- Trained on most of human + mouse genome; tested on held-out sequences

## 4. Key Results & Benchmarks
- Substantially improved Pearson correlation between predicted and measured expression vs. Basenji2 (CNN baseline)
- Better CRISPRi enhancer prediction: more accurate identification of functional enhancers
- Population eQTL prediction: improved accuracy for common variants
- Long-range dependency: self-attention allows integration of elements >20kb from TSS

## 5. Limitations & Future Work
- 196kb input window; ultra-long-range interactions (>100kb) still challenging
- Human/mouse only; no multi-species generalization at publication
- Computationally expensive; inference not real-time

## 6. Related Work
- Basenji2: CNN predecessor (limited to ~20kb context)
- Sei, DNABERT: other genomic DL models
- deng-2024 (lentiMPRA): experimental validation of regulatory elements (complementary)

## 7. Glossary
- **Enformer**: Enhancer + transformer portmanteau; DeepMind/Calico/Google model
- **eQTL**: Expression quantitative trait locus — DNA variant affecting gene expression
- **CRISPRi**: CRISPR interference — transcriptional repression for enhancer validation
- **CAGE**: Cap analysis of gene expression — measures transcription start site activity
