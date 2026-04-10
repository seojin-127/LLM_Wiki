---
title: "An integrated transcriptomic cell atlas of human neural organoids"
authors: Zhisong He, Leander Dony, Jonas Simon Fleck, Artur Szałata, Katelyn X. Li, Irena Slišković, Hsiu-Chuan Lin, Malgorzata Santel, Alexander Atamian, Giorgia Quadrato, Jieran Sun, Sergiu P. Pașca, J. Gray Camp, Fabian J. Theis, Barbara Treutlein
year: 2024
doi: 10.1038/s41586-024-08172-8
category: brain-atlas
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/0915634843/He-2024-An integrated transcriptomic cell atla.pdf
pdf_filename: He-2024-An integrated transcriptomic cell atla.pdf
source_collection: endnote
---

## One-line Summary
Integration of 36 scRNA-seq datasets (1.77M cells, 26 protocols) into a human neural organoid cell atlas (HNOCA) that quantifies transcriptomic fidelity, coverage of brain regions, and utility for disease modeling.

## 1. Document Info
- Journal/Conference: Nature
- Published: 20 November 2024

## 2. Key Contributions
- First large-scale integrated atlas of human neural organoids: 1.77M cells from 36 datasets spanning 26 protocols
- Systematic mapping to developing human brain references to assess which brain regions are and are not covered by existing protocols
- Quantitative measure of transcriptomic fidelity between organoid and primary cell types; cell stress identified as universal distinguishing factor (not core cell identity)
- Atlas as disease control cohort: 11 scRNA-seq datasets for 10 neural diseases mapped onto HNOCA for cell type annotation and DE analysis
- Programmatic interface (snapseed + scPoli) for browsing, querying, and projecting new datasets

## 3. Methods & Architecture
- Data curation: 34 published + 2 unpublished datasets; harmonized metadata and consistent QC
- Integration: 3-step pipeline — (1) RSS projection to primary brain atlas, (2) snapseed marker-based hierarchical annotation, (3) scPoli label-aware integration
- Benchmarked against multiple integration methods; scPoli ranked best
- UMAP clustering; canonical marker gene annotation
- Transcriptomic fidelity estimated per organoid cell type vs. primary counterpart
- Disease model mapping: 11 datasets (ASD, schizophrenia, etc.) as perturbation cohort vs. HNOCA control

## 4. Key Results & Benchmarks
- Dorsal telencephalon (excitatory neurons, NPCs) best covered; non-telencephalic and ventral regions underrepresented
- Cell stress (glycolytic signature) is a universal in vitro artifact but does not erase core neuronal identity
- Atlas successfully annotated cell types in morphogen screens and identified disease-relevant DE genes
- scPoli integration outperformed other methods on organoid batch correction benchmarks

## 5. Limitations & Future Work
- Representation biased toward telencephalic protocols; cerebellar, spinal cord, and other regions sparse
- Single-cell (not spatial) data; no spatial resolution within organoids
- Cell stress correction remains incomplete; metabolic artifacts persist
- Cross-lab batch effects partially unresolved

## 6. Related Work
- Developing human brain reference: Bhaduri et al. 2020, Braun et al. 2023
- scPoli integration: de Donno et al.
- Cell stress in organoids: Lancaster et al., Bhaduri et al.
- Disease organoid models: various (ASD, schizophrenia)

## 7. Glossary
- **HNOCA**: Human Neural Organoid Cell Atlas
- **snapseed**: Tool for hierarchical cell type annotation using marker genes
- **scPoli**: Label-aware integration method for single-cell data
- **RSS**: Reference Similarity Spectrum — projection of query to reference atlas
- **Transcriptomic fidelity**: Quantitative similarity of organoid cell type to primary counterpart
