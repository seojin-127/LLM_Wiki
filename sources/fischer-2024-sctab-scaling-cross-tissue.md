---
title: "scTab: Scaling cross-tissue single-cell annotation models"
authors: Felix Fischer, David S. Fischer, Roman Mukhin, Andrey Isaev, Evan Biederstedt, Alexandra-Chloé Villani, Fabian J. Theis
year: 2024
doi: 10.1038/s41467-024-51059-5
category: single-cell-dl
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/3496659844/
source_collection: endnote
---

## One-line Summary
scTab is a tabular deep learning model for cross-tissue cell type annotation trained on 22.2M scRNA-seq cells; performance scales with data and model size, and a novel data augmentation scheme improves generalization across tissues.

## 1. Document Info
- Journal/Conference: Nature Communications
- Published: 2024

## 2. Key Contributions
- scTab: automated cell type prediction model for tabular scRNA-seq data
- Trained on 22.2M cells from large curated corpus across diverse tissues
- Shows cross-tissue annotation requires nonlinear models (vs. linear baselines)
- Performance scales with both training dataset size and model size
- Novel data augmentation schema improves cross-tissue generalization

## 3. Methods & Architecture
- Tabular deep learning architecture (MLP-style for scRNA-seq input)
- Training corpus: 22.2M cells across multiple tissues and datasets
- Data augmentation: gene dropout and expression noise during training
- Evaluated on held-out tissues and datasets

## 4. Key Results & Benchmarks
- Nonlinear models (scTab) outperform linear models for cross-tissue annotation
- Scaling laws: both data and model size improve annotation accuracy
- Data augmentation consistently improves generalization to unseen tissues
- De novo cell type prediction without reference-dataset-specific retraining

## 5. Limitations & Future Work
- Requires curated large-scale training corpus
- Annotation quality depends on training label quality
- Does not handle rare or novel cell types not in training distribution

## 6. Related Work
- Ergen et al. 2024 (popV): ensemble+ontology cell type label transfer (complementary)
- Heimberg et al. 2025 (SCimilarity): metric learning for cell similarity search
- ScVI/scANVI: deep generative models for cell type annotation

## 7. Glossary
- **Tabular DL**: Deep learning applied to tabular (gene × cell matrix) data
- **Cross-tissue annotation**: Cell type prediction generalizing across different organ datasets
- **Data augmentation**: Artificially expanding training data diversity to improve generalization
