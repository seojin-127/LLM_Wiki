---
title: "EpiAgent: foundation model for single-cell epigenomics"
authors: Xiaoyang Chen, Keyi Li, Xuejian Cui, Zian Wang, Qun Jiang, Jiacheng Lin, Zhen Li, Zijing Gao, Hairong Lv, Rui Jiang
year: 2025
doi: 10.1038/s41592-025-02822-z
source: chen-2025-epiagent-foundation-model-single-cell.md
category: single-cell-foundation
tags: [EpiAgent, scATAC-seq, epigenomics, foundation-model, chromatin-accessibility, zero-shot, CRE-knockout, perturbation-prediction]
---

## Summary
EpiAgent: first large-scale foundation model for single-cell epigenomics (scATAC-seq), pretrained on the Human-scATAC-Corpus. Encodes chromatin accessibility as "cell sentences" via bidirectional attention. Achieves state-of-the-art on unsupervised clustering, cell type annotation, data imputation, and enables zero-shot annotation and in silico CRE knockout experiments.

## Key Contributions
- First foundation model specifically for scATAC-seq; pretrained on Human-scATAC-Corpus
- "Cell sentence" encoding: accessible peaks as token sequence for bidirectional transformer
- Zero-shot cell type annotation without task-specific fine-tuning
- In silico CRE knockout: predicts cell state changes from regulatory element removal
- Cellular response prediction for out-of-sample stimuli and unseen genetic perturbations

## Methods & Architecture
- Bidirectional transformer (BERT-style) pretrained on Human-scATAC-Corpus
- Input: chromatin accessibility peaks encoded as ordered "cell sentence" tokens
- External embedding incorporation for multi-modal and perturbation tasks
- Fine-tuning for supervised tasks; zero-shot for annotation

## Results
- Unsupervised clustering: superior to ArchR, Signac baselines
- Cell type annotation: best-in-class on scATAC-seq benchmarks
- Data imputation: best reconstruction of sparse accessibility signal
- Zero-shot annotation: effective without labeled training data
- CRE knockout: predicts expected cell state transitions

## Limitations
- Human-only corpus; other species require adaptation
- scATAC-seq sparsity remains challenging for some tasks
- Multi-omic (RNA+ATAC) integration not primary focus

## Related Papers
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT: RNA-seq foundation model counterpart
- [[single-cell-foundation/hao-2024-large-scale-foundation-model]] — scFoundation: large-scale scRNA-seq FM
- [[brain-atlas/domcke-2020-human-cell-atlas-fetal]] — fetal chromatin accessibility atlas (complementary data resource)
