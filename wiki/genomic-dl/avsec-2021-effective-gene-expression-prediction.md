---
title: "Effective gene expression prediction from sequence by integrating long-range interactions"
authors: Žiga Avsec, Vikram Agarwal, Daniel Visentin, et al.
year: 2021
doi: 10.1038/s41592-021-01252-x
source: avsec-2021-effective-gene-expression-prediction.md
category: genomic-dl
tags: [Enformer, transformer, gene-expression-prediction, DNA-sequence, long-range, enhancer, eQTL, DeepMind, chromatin]
---

## Summary
Enformer: self-attention transformer predicting gene expression and chromatin states from 196kb DNA sequences across 5,313 human and 1,643 mouse genomic tracks. Replaces convolution-only architectures (e.g., Basenji2) with transformer self-attention, enabling integration of distal regulatory elements beyond 20kb. Substantially improves eQTL and CRISPRi enhancer prediction benchmarks.

## Key Contributions
- Enformer: transformer-based model with 196kb receptive field for gene expression + chromatin state prediction
- Self-attention replaces CNNs → far greater information flow between distal enhancers and promoters
- Predicts 5,313 human + 1,643 mouse tracks (CAGE, ATAC, ChIP-seq) simultaneously
- Improved eQTL effect prediction vs. prior sequence models
- Better CRISPRi enhancer validation performance

## Methods & Architecture
- Input: 196,608bp DNA sequence (human or mouse)
- Convolutional stem + transformer blocks with self-attention
- Multitask output heads for 5,313 human + 1,643 mouse epigenetic/transcriptional tracks
- Trained on most of human + mouse genome; held-out sequence testing

## Results
- Substantially improved Pearson correlation vs. Basenji2 CNN baseline
- Long-range: integrates elements >20kb from TSS (previously impossible for CNNs)
- Population eQTL: improved common variant effect size prediction
- CRISPRi enhancer: more accurate functional enhancer identification

## Limitations
- 196kb input window; ultra-long-range (>196kb) interactions not captured
- Human/mouse only at publication
- Computationally expensive for genome-wide inference

## Related Papers
- [[genomic-dl/deng-2024-massively-parallel-regulatory]] — lentiMPRA experimental enhancer validation (complementary)
- [[genomic-dl/yu-2026-chrombert-foundation-model]] — ChromBERT: TF-level regulatory network FM (related paradigm)
- [[genomic-dl/zemke-2023-conserved-and-divergent-gene]] — cross-species regulatory genomics (complementary)
