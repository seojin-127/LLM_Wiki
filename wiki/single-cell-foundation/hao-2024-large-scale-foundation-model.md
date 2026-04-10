---
title: "Large-scale foundation model on single-cell transcriptomics"
authors: Minsheng Hao, Jing Gong, Xin Zeng, Chiming Liu, Yucheng Guo, Xingyi Cheng, Taifeng Wang, Jianzhu Ma, Xuegong Zhang, Le Song
year: 2024
doi: 10.1038/s41592-024-02305-7
source: hao-2024-large-scale-foundation-model.md
category: single-cell-foundation
tags: [foundation-model, scRNA-seq, transformer, pretraining, drug-response, perturbation-prediction, gene-expression-enhancement, 100M-parameters]
---

## Summary
scFoundation (xTrimoscFoundationα): 100M parameter asymmetric transformer pretrained on 50M+ human single-cell transcriptomic profiles covering ~20,000 genes. At publication, the largest single-cell foundation model by parameters, gene dimensionality, and training data. Achieves state-of-the-art on gene expression enhancement, drug response prediction, perturbation prediction, cell type annotation, and gene module inference.

## Key Contributions
- 100M parameter asymmetric transformer pretrained on 50M+ human scRNA-seq profiles
- Largest single-cell FM at publication (parameters + gene dimensionality + data volume)
- Asymmetric architecture + read-depth-aware pretraining captures complex gene-gene context
- State-of-the-art on 6+ tasks without task-specific pretraining

## Methods & Architecture
- Asymmetric transformer: different encoder/decoder capacities for read-depth-aware pretraining
- ~20,000 protein-coding genes as token vocabulary; gene expression values as inputs
- Pretraining: gene expression reconstruction across varying sequencing depths
- Transfer learning / fine-tuning for downstream tasks

## Results
- Gene expression enhancement: best-in-class imputation of lowly detected genes
- Tissue drug response and single-cell drug response classification: superior performance
- Perturbation prediction: outperforms task-specific models
- Cell type annotation: competitive with supervised baselines
- Gene module inference: biologically coherent programs identified

## Limitations
- Human-only pretraining; cross-species transfer not addressed
- Large compute requirement for pretraining
- Expression enhancement may propagate systematic biases from training data

## Related Papers
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT: concurrent generative single-cell FM (complementary architecture)
- [[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]] — SCimilarity: metric-learning FM (different paradigm)
- [[single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell]] — EpiAgent: extends FM to scATAC-seq epigenomics
