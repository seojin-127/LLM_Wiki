---
title: "ChromBERT: A foundation model for learning interpretable representations for context-specific transcriptional regulatory networks"
authors: Zhaowei Yu, Dongxu Yang, Qianqian Chen, Yuxuan Zhang, Zhanhao Li, Yucheng Wang, Chenfei Wang, Yong Zhang
year: 2026
doi: 10.1016/j.xgen.2025.101130
source: yu-2026-chrombert-foundation-model.md
category: genomic-dl
tags: [ChromBERT, BERT, ChIP-seq, TRN, cistrome, transcription-factor, foundation-model, regulatory-network, context-specific]
---

## Summary
ChromBERT: BERT-based foundation model pretrained on ~1,000 transcription regulators from large-scale human ChIP-seq data. Learns genome-wide TF interaction syntax and generates interpretable transcriptional regulatory network (TRN) representations. Prompt-enhanced fine-tuning enables cistrome imputation in unseen cell types and single cells without additional ChIP-seq experiments.

## Key Contributions
- Pretrained on ~1,000 TFs/co-regulators from large-scale ENCODE/ChIP-seq data
- Learns general genome-wide TF regulatory cooperation syntax
- Prompt-enhanced fine-tuning for cistrome imputation in unseen cell types and single cells
- Context-specific TRN representations via lightweight fine-tuning
- Identifies key TF drivers of cell state transitions — no additional ChIP-seq needed

## Methods & Architecture
- BERT-style transformer pretrained on human ChIP-seq data (~1,000 TFs)
- Input: genomic regions + TF occupancy signals
- Prompt-enhanced fine-tuning for cell-type-specific downstream tasks
- Interpretable TRN representations from attention patterns

## Results
- Cistrome imputation: outperforms existing methods for unseen TF binding
- Context-specific TRN: captures regulatory dynamics across cell types
- Identifies known TF drivers of cell state transitions (validated)
- Single-cell TRN inference from sparse chromatin data

## Limitations
- Human-only pretraining
- ChIP-seq-based; doesn't directly model chromatin accessibility or 3D genome
- Regulatory syntax interpretability limited to known TF interactions

## Related Papers
- [[genomic-dl/avsec-2021-effective-gene-expression-prediction]] — Enformer: sequence-to-expression genomic DL (complementary)
- [[genomic-dl/deng-2024-massively-parallel-regulatory]] — lentiMPRA: experimental regulatory validation (complementary)
- [[single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell]] — EpiAgent: scATAC-seq FM (related paradigm)
