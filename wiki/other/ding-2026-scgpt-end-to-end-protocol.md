---
title: "scGPT: end-to-end protocol for fine-tuned retinal cell type annotation"
authors: Shanli Ding, Jin Li, Rui Luo, Haotian Cui, Bo Wang, Rui Chen
year: 2026
doi: 10.1038/s41596-025-01220-1
source: ding-2026-scgpt-end-to-end-protocol.md
category: other
tags: [scGPT, protocol, cell-type-annotation, retina, fine-tuning, Nature-Protocols, scRNA-seq]
---

## Summary
Nature Protocols guide for fine-tuning scGPT for cell type annotation in scRNA-seq data, demonstrated on a retinal dataset achieving 99.5% F1-score. Provides automated pipeline with command-line scripts and Jupyter Notebooks accessible to researchers with minimal Python/Linux knowledge. Addresses rare cell type annotation challenge via foundation model transfer learning.

## Key Contributions
- End-to-end protocol: data preprocessing → scGPT fine-tuning → evaluation
- Demonstrated on retinal dataset: 99.5% F1-score on cell type annotation
- Outperforms Seurat, scPred, scArches, Geneformer on retinal data
- Command-line script + Jupyter Notebook versions for accessibility
- Handles rare cell types better than marker-gene-based methods

## Methods & Architecture
- scGPT fine-tuning workflow on custom scRNA-seq dataset
- Automates tokenization, model adaptation, and evaluation steps
- Computing cluster + Jupyter Notebook implementations

## Results
- 99.5% F1-score on retinal cell type annotation
- Superior to multiple baselines including other foundation models
- Accessible to researchers without deep ML expertise

## Limitations
- Protocol specific to scGPT; not generalizable to other FMs without modification
- Retinal demonstration; broader tissue validation needed
- Requires computing cluster for fine-tuning step

## Related Papers
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT original paper (foundation model being fine-tuned)
- [[single-cell-dl/ergen-2024-consensus-prediction-cell]] — popV: ensemble cell type annotation (complementary)
- [[single-cell-dl/fischer-2024-sctab-scaling-cross-tissue]] — scTab: tabular DL annotation (alternative approach)
