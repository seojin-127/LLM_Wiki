---
title: "scGPT: end-to-end protocol for fine-tuned retinal cell type annotation"
authors: Shanli Ding, Jin Li, Rui Luo, Haotian Cui, Bo Wang, Rui Chen
year: 2026
doi: 10.1038/s41596-025-01220-1
category: other
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/3965572886/
source_collection: endnote
---

## One-line Summary
Nature Protocols paper providing a comprehensive guide for fine-tuning scGPT for cell type annotation in scRNA-seq data; demonstrated on retinal dataset achieving 99.5% F1-score; provides command-line scripts and Jupyter notebooks for accessible deployment.

## 1. Document Info
- Journal/Conference: Nature Protocols
- Published: March 2026

## 2. Key Contributions
- End-to-end protocol for fine-tuning scGPT on custom scRNA-seq datasets
- Demonstrated on retinal cell type annotation: 99.5% F1-score
- Automates data preprocessing, model fine-tuning, and evaluation steps
- Command-line script + Jupyter Notebook for accessibility (minimal Python/Linux knowledge needed)
- Addresses rare cell type annotation challenge via foundation model transfer learning

## 3. Methods & Architecture
- scGPT fine-tuning workflow: data preprocessing → tokenization → fine-tuning → evaluation
- Target task: cell type classification in scRNA-seq
- Custom retina dataset used as demonstration
- Computing cluster + Jupyter Notebook versions provided

## 4. Key Results & Benchmarks
- 99.5% F1-score on retinal cell type annotation
- Outperforms Seurat, scPred, scArches, Geneformer on retinal dataset
- Handles rare cell types better than marker-gene-based methods

## 5. Limitations & Future Work
- Protocol specific to scGPT; not generalizable to other foundation models without modification
- Retinal demonstration; performance on other tissues needs validation
- Requires computing cluster for fine-tuning step

## 6. Related Work
- cui-2024-scgpt (scGPT original paper): foundation model being fine-tuned
- ergen-2024 (popV): cell type annotation ensemble method (complementary)
- fischer-2024 (scTab): tabular DL for cell type annotation (alternative approach)

## 7. Glossary
- **scGPT**: Single-cell GPT; generative pretrained transformer for scRNA-seq (Cui et al. 2024)
- **F1-score**: Harmonic mean of precision and recall; benchmark metric for cell type annotation
- **Fine-tuning**: Adapting a pretrained foundation model to a specific task/dataset
