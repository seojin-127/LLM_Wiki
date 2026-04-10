---
title: "Consensus prediction of cell type labels in single-cell data with popV"
authors: Can Ergen, Galen Xing, Chenling Xu, Martin Kim, Michael Jayasuriya, Erin McGeever, Angela Oliveira Pisco, Aaron Streets, Nir Yosef
year: 2024
doi: 10.1038/s41588-024-01993-3
category: single-cell-dl
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/2587791190/Ergen-2024-Consensus prediction of cell type l.pdf
pdf_filename: Ergen-2024-Consensus prediction of cell type l.pdf
source_collection: endnote
---

## One-line Summary
popV is an ensemble method for single-cell cell-type label transfer using ontology-based voting across multiple prediction models, providing accurate annotations with well-calibrated uncertainty scores that flag hard-to-annotate populations for targeted manual review.

## 1. Document Info
- Journal/Conference: Nature Genetics
- Published: December 2024

## 2. Key Contributions
- popV: ensemble of prediction models + ontology-based voting for cell type label transfer
- Well-calibrated uncertainty scores: cells with low confidence flagged for manual review
- Reduces manual annotation burden by focusing human review on problematic populations
- Benchmarked across multiple reference atlases and query datasets

## 3. Methods & Architecture
- Ensemble approach: multiple prediction methods (SCVI, KNN, SVM, etc.) combined
- Ontology-based voting: uses cell ontology structure to aggregate predictions
- Uncertainty score: based on consensus across ensemble models
- Applied to multiple case studies (tabula sapiens, PBMC references, etc.)

## 4. Key Results & Benchmarks
- popV accurately labels the majority of cells with high confidence
- Uncertainty scores reliably identify hard-to-annotate populations
- Reduces manual review burden: focus human effort on <20% of cells
- Outperforms individual methods on annotation accuracy benchmarks

## 5. Limitations & Future Work
- Requires a well-annotated reference atlas; performance degrades with poor references
- Cell ontology structure needed; not all organisms/tissues have comprehensive ontologies
- Ensemble is computationally more expensive than single-method approaches

## 6. Related Work
- scVI/scArches: reference-based integration (used within popV)
- Seurat: label transfer method
- Cell Ontology: structured vocabulary for cell types

## 7. Glossary
- **popV**: Popular Vote — ensemble consensus cell type annotation tool
- **Cell ontology**: Hierarchical structured vocabulary of cell types
- **Label transfer**: Automated annotation of unannotated data by mapping to reference atlas
- **Uncertainty score**: Measure of disagreement across ensemble models; low score = ambiguous cell
