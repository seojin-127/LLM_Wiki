---
title: "Prototype-based Continual Learning for Single-cell Annotation with scEvolver"
authors: Ge, Shuangshuang, Guo, Jinyun, Wang, Chong, Ding, Jun, Zhang, Yan
year: 2026
doi: 10.64898/2026.03.05.709973
source: ge-2026-prototype-based-continual-learning-for.md
category: single-cell-dl
tags: [continual-learning, cell-type-annotation, scGPT, LoRA, prototypes, few-shot, PEFT, multi-modal]
---

## Summary

scEvolver tackles catastrophic forgetting in single-cell annotation by building a continual learning framework on a frozen scGPT backbone with LoRA+MoE adapters. Memory-augmented prototypes (Mp) per cell type and a hard-sample replay buffer are trained with the MAPPL loss, which balances plasticity (learning new types) against stability (retaining old types). In 5-shot settings, scEvolver achieves +24.5% macro-F1 on the PANCREAS benchmark over the next-best baseline, and uncovers previously unidentified SF-like metaplastic epithelial cells in IBD gut data.

## Key Contributions

- scEvolver: continual learning for single-cell annotation across platforms, tissues, and modalities without catastrophic forgetting
- Memory-augmented prototypes (Mp) that retain a weighted history of class distribution shifts across tasks
- Hard-sample replay buffer: prioritizes near-decision-boundary cells for efficient memory replay
- MAPPL loss: unified objective balancing plasticity (new cell types) and stability (previous cell types) via prototype distillation
- Validated on cross-platform, cross-tissue, cross-modality (ATAC+RNA, ADT+RNA) settings

## Methods & Architecture

scGPT is used as a frozen encoder backbone. LoRA adapters plus MoE modules are inserted and updated during continual learning — keeping the pretrained knowledge intact while adapting to new tasks. For each cell type, a prototype vector represents its position in embedding space; the memory augmentation stores a running history of these positions to resist drift. The hard-sample replay buffer selects high-uncertainty examples from previous tasks for reuse during new task training. MAPPL loss combines standard classification cross-entropy with a KL-based prototype distillation term that penalizes large shifts in old-class prototype distributions.

## Results

- PANCREAS 5-shot: +24.5% macro-F1 vs. next-best baseline
- Outperforms scGPT fine-tuning, EWC, LwF across all evaluated benchmarks
- Robust cross-platform (10x ↔ Smart-seq2) and cross-modality (ATAC+RNA, ADT+RNA) performance
- Novel discovery: SF-like metaplastic epithelial cells in IBD gut scRNA-seq data

## Limitations

- Performance inherits scGPT backbone quality and pretraining distribution bias
- Fixed replay buffer size may be insufficient for very long task sequences
- 5-shot prototype initialization quality affects convergence

## Related Papers

- [[single-cell-foundation/cui-2024-scgpt-toward-building-a]] — scGPT; backbone for scEvolver
- [[single-cell-foundation/hao-2024-large-scale-cell-representation]] — scFoundation; alternative foundation model baseline
- [[single-cell-dl/ergen-2024]] — single-cell DL annotation methods; benchmark context
- [[single-cell-dl/wang-2024]] — single-cell DL; related annotation and transfer learning approaches
- [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]] — PerturBERT; another BERT-style foundation model for single-cell tasks
