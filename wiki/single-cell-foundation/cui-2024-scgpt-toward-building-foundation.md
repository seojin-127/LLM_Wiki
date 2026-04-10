---
title: "scGPT: toward building a foundation model for single-cell multi-omics using generative AI"
authors: Haotian Cui, Chloe Wang, Hassaan Maan, Kuan Pang, Fengning Luo, Nan Duan, Bo Wang
year: 2024
doi: 10.1038/s41592-024-02201-0
source: cui-2024-scgpt-toward-building-foundation.md
category: single-cell-foundation
tags: [scGPT, GPT, generative, transformer, pretraining, cell-type-annotation, perturbation, multi-omic, 33M-cells]
---

## Summary
scGPT: generative pretrained transformer for single-cell multi-omics pretrained on 33M+ cells from the Human Cell Atlas and other datasets. Achieves state-of-the-art on cell type annotation, multi-batch integration, multi-omic integration (RNA+ATAC), perturbation response prediction, and gene network inference through fine-tuning.

## Key Contributions
- scGPT: GPT-style generative transformer pretrained on 33M+ scRNA-seq cells
- Unified model for 5+ diverse single-cell tasks via fine-tuning
- Demonstrates scaling: more pretraining data → better downstream performance
- Perturbation prediction: outperforms GEARS on held-out gene perturbations

## Methods & Architecture
- Generative pretrained transformer with gene expression tokens + condition tokens
- Pretraining: masked gene expression prediction across 33M+ cells
- Attention mechanism captures gene-gene interaction patterns
- Task-specific fine-tuning with lightweight heads per application

## Results
- Cell type annotation: outperforms Seurat, SingleR on cross-dataset benchmarks
- Multi-batch integration: competitive with scVI and Harmony
- Multi-omic (RNA+ATAC): effective cross-modality joint embedding
- Perturbation prediction: outperforms GEARS on held-out perturbations
- Gene network inference: recovers known GRN interactions from attention weights

## Limitations
- Context window limits simultaneous gene count
- Human-only pretraining; cross-species requires fine-tuning
- Perturbation prediction limited to in-distribution cell types

## Related Papers
- [[single-cell-foundation/hao-2024-large-scale-foundation-model]] — scFoundation: larger-scale concurrent scRNA-seq FM
- [[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]] — SCimilarity: metric-learning approach (different paradigm)
- [[single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell]] — EpiAgent: extends FM to scATAC-seq
