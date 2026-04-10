---
title: "scGPT: toward building a foundation model for single-cell multi-omics using generative AI"
authors: Haotian Cui, Chloe Wang, Hassaan Maan, Kuan Pang, Fengning Luo, Nan Duan, Bo Wang
year: 2024
doi: 10.1038/s41592-024-02201-0
category: single-cell-foundation
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/3112472836/
source_collection: endnote
---

## One-line Summary
scGPT: generative pretrained transformer for single-cell multi-omics trained on 33M+ cells; achieves state-of-the-art on cell type annotation, multi-batch integration, multi-omic integration, perturbation response prediction, and gene network inference via fine-tuning.

## 1. Document Info
- Journal/Conference: Nature Methods
- Published: February 2024

## 2. Key Contributions
- scGPT: generative pretrained transformer pretrained on 33M+ cells (Human Cell Atlas and other datasets)
- Unified model for diverse downstream single-cell tasks via fine-tuning
- Tasks: cell type annotation, multi-batch integration, multi-omic integration, perturbation prediction, gene network inference
- Demonstrates scaling law: larger pretraining data → better downstream performance

## 3. Methods & Architecture
- Generative pretrained transformer (GPT-style) with gene expression tokens
- Pretraining: masked gene expression prediction on 33M+ scRNA-seq cells
- Gene and condition tokens; attention-based gene-gene interaction learning
- Fine-tuning with task-specific heads for each downstream application

## 4. Key Results & Benchmarks
- Cell type annotation: superior to Seurat, SingleR on cross-dataset benchmarks
- Multi-batch integration: competitive with scVI and Harmony
- Multi-omic integration (RNA+ATAC): effective cross-modality embedding
- Perturbation prediction: outperforms GEARS on held-out gene perturbations
- Gene network inference: recovers known GRN interactions

## 5. Limitations & Future Work
- GPT-style architecture; context window limits number of genes modeled simultaneously
- Pretraining on human cells only; cross-species transfer requires fine-tuning
- Perturbation prediction still limited to in-distribution cell types

## 6. Related Work
- scFoundation (Hao 2024): concurrent larger-scale single-cell FM
- Geneformer: earlier encoder-only single-cell FM
- SCimilarity (Heimberg 2025): metric-learning search approach
- EpiAgent (Chen 2025): extends foundation model paradigm to scATAC-seq

## 7. Glossary
- **scGPT**: single-cell GPT; generative pretrained transformer for scRNA-seq
- **Multi-omic integration**: Combining RNA + ATAC (or other modalities) in joint embedding
- **Perturbation prediction**: Predicting post-perturbation transcriptome from pre-perturbation state
- **Gene network inference**: Deriving gene regulatory relationships from attention weights
