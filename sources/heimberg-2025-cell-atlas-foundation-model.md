---
title: "A cell atlas foundation model for scalable search of similar human cells"
authors: Graham Heimberg, Tony Kuo, Daryle J. DePianto, Omar Salem, et al.
year: 2025
doi: 10.1038/s41586-024-08411-0
category: single-cell-foundation
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/3800712968/
source_collection: endnote
---

## One-line Summary
SCimilarity: metric-learning foundation model for single-cell profiles enabling rapid search of 23.4M cells across 412 studies; identifies similar cell states across tissues/diseases; ILD macrophage query finds similar states in other fibrotic diseases.

## 1. Document Info
- Journal/Conference: Nature
- Published: February 2025

## 2. Key Contributions
- SCimilarity: metric-learning framework for universal single-cell profile representation
- Enables rapid query of 23.4M cells from 412 scRNA-seq studies
- Finds transcriptionally similar cell profiles across organs, diseases, and in vitro models
- ILD macrophage query: finds similar states in other fibrotic diseases/tissues
- Hydrogel 3D system (top in vitro hit for macrophage query) experimentally validated
- Foundation model approach: unified representation without dataset-specific retraining

## 3. Methods & Architecture
- Metric learning: trained to embed single-cell profiles such that similar cells are close in representation space
- 23.4M-cell atlas from 412 studies as the searchable corpus
- Query: input a cell profile → retrieve most similar profiles from atlas
- Interpretable representation: can identify which genes drive similarity

## 4. Key Results & Benchmarks
- Rapid search across 23.4M cells (scalable)
- ILD (interstitial lung disease) macrophage query → finds similar states in other fibrotic diseases
- ILD fibroblast query → similar profiles in other fibrotic tissues
- Top in vitro hit (3D hydrogel macrophage) experimentally validated to reproduce cell state
- Cross-study, cross-tissue cell similarity discovery enabled

## 5. Limitations & Future Work
- Training corpus biased toward well-studied tissues/diseases
- Metric learning may not capture all aspects of cell identity (e.g., spatial context)
- Annotation quality of 412 studies varies

## 6. Related Work
- Fischer et al. 2024 (scTab): cell type annotation (complementary)
- Ergen et al. 2024 (popV): label transfer with uncertainty (complementary)

## 7. Glossary
- **Metric learning**: Supervised approach to learn a distance function where similar examples are close
- **ILD**: Interstitial lung disease — fibrotic lung condition; used as model query system
- **Foundation model**: Large pre-trained model applicable to many downstream tasks without retraining
