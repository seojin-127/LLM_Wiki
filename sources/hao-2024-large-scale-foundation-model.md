---
title: "Large-scale foundation model on single-cell transcriptomics"
authors: Minsheng Hao, Jing Gong, Xin Zeng, Chiming Liu, Yucheng Guo, Xingyi Cheng, Taifeng Wang, Jianzhu Ma, Xuegong Zhang, Le Song
year: 2024
doi: 10.1038/s41592-024-02305-7
category: single-cell-foundation
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/0613292968/
source_collection: endnote
---

## One-line Summary
scFoundation (xTrimoscFoundationα): 100M parameter asymmetric transformer pretrained on 50M+ human single-cell transcriptomic profiles covering ~20,000 genes; achieves state-of-the-art across gene expression enhancement, drug response prediction, perturbation prediction, and cell type annotation.

## 1. Document Info
- Journal/Conference: Nature Methods
- Published: August 2024

## 2. Key Contributions
- scFoundation: 100M parameter foundation model for scRNA-seq; largest at publication (parameters, gene dimensionality, training data)
- Asymmetric transformer architecture + pretraining task capturing complex gene-gene context relations
- Pretrained on 50M+ human single-cell transcriptomic profiles across all cell types and states
- State-of-the-art on 6+ tasks: gene expression enhancement, tissue drug response, single-cell drug response classification, perturbation prediction, cell type annotation, gene module inference

## 3. Methods & Architecture
- Asymmetric transformer: different encoder/decoder capacities for read-depth-aware pretraining
- Pretraining task: gene expression value reconstruction across varying sequencing depths
- ~20,000 protein-coding genes as vocabulary; gene expression values as "tokens"
- Fine-tuning/adaptation for downstream tasks via transfer learning

## 4. Key Results & Benchmarks
- State-of-the-art gene expression enhancement (imputation of lowly expressed genes)
- Drug response prediction: superior tissue-level and single-cell-level performance
- Perturbation prediction: outperforms task-specific models
- Cell type annotation: competitive with supervised methods
- Gene module inference: biologically coherent gene programs identified

## 5. Limitations & Future Work
- Human-only pretraining; cross-species transfer not addressed
- Very large compute requirement for pretraining
- Gene expression enhancement may propagate systematic biases

## 6. Related Work
- scGPT (Cui et al. 2024): concurrent single-cell foundation model (generative)
- Geneformer: earlier single-cell FM (smaller scale)
- SCimilarity (Heimberg 2025): metric-learning approach (different paradigm)

## 7. Glossary
- **scFoundation**: Also called xTrimoscFoundationα; 100M param single-cell FM
- **Read depth**: Number of sequencing reads per cell; affects gene detection sensitivity
- **Gene expression enhancement**: Imputing expression values for lowly/un-detected genes
- **Perturbation prediction**: Predicting transcriptomic response to genetic/chemical perturbation
