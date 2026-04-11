---
title: "Population-level integration of single-cell datasets enables multi-scale analysis across samples"
authors: De Donno, Carlo, Hediyeh-Zadeh, Soroor, Moinfar, Amir Ali, Wagenstetter, Marco, Zappia, Luke, Lotfollahi, Mohammad, Theis, Fabian J.
year: 2023
doi: 10.1038/s41592-023-02035-2
category: single-cell-dl
pdf_path: papers/dedonno-2023-population-level-integration-of.pdf
pdf_filename: dedonno-2023-population-level-integration-of.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

scPoli is an open-world learner for population-level single-cell atlas integration that jointly learns cell and sample embeddings via prototype loss, enabling scalable data integration, label transfer, and reference mapping for datasets up to 7.8M cells across 2,375 samples.

## 1. Document Info
- Journal/Conference: Nature Methods
- Received/Published: Published October 2023 (DOI: 10.1038/s41592-023-02035-2)

## 2. Key Contributions
- scPoli: generative model learning both cell-level and sample-level embeddings simultaneously; bridges single-cell and sample metadata
- Prototype loss: class prototypes in latent space improve biological signal conservation during integration (5.06% improvement over scANVI in benchmark)
- Open-world learner: can extend reference atlas with novel cell types from labeled query data without retraining
- Scales to 7.8M cells across 2,375 samples (PBMC atlas)
- Explains sample-level variation: sample embeddings reveal batch- and biology-associated gene programs

## 3. Methods & Architecture
- **Base**: conditional VAE (scVI-family architecture)
- **Condition embedding**: learned continuous sample representations replace one-hot batch encodings; captures sample-level variation
- **Prototype loss**: for each cell type, maintain a prototype (mean embedding); add KL term to loss encouraging cells to cluster near their prototype; unlabeled cells classified by nearest prototype
- **Open-world extension**: new cell types from labeled query added as new prototypes without modifying reference encoder weights
- **Sample embeddings**: sample-level PCA of condition embeddings; reveals batch vs. biological variation per gene
- **Integration metrics**: biological conservation + batch correction (same as scIB benchmark)

## 4. Key Results & Benchmarks
- Outperforms scANVI by 5.06% overall on integration benchmark (6 datasets)
- Better biological conservation than all compared methods (scVI, scANVI, Seurat v3, Symphony, SVM, MARS)
- Novel cell type extension: correctly identifies novel cell types added from query without full retraining
- PBMC atlas (7.8M cells, 2,375 samples): successfully integrated; sample embeddings explain COVID-19 severity variation
- Lung atlas: sample-level gene programs distinguish technical vs. biological batch sources
- scATAC-seq and cross-species: applicable with appropriate feature spaces

## 5. Limitations & Future Work
- Prototype loss benefits depend on annotation quality in labeled training data
- Open-world extension limited to labeled query data; unlabeled novel types require additional discovery step
- Condition embedding interpretability requires downstream analysis (PCA, correlation)
- Very large atlases (>10M cells) may require distributed training

## 6. Related Work
- scVI (Lopez et al., 2018) — base architecture; scPoli adds sample embedding + prototype loss
- scANVI (Xu et al., 2021) — previous best for labeled integration; scPoli outperforms
- scArches (Lotfollahi et al., 2022) — reference mapping via architecture surgery; scPoli adds open-world capability
- scIB benchmark (Luecken et al., 2022) — benchmark framework; metrics reused in scPoli evaluation
- MrVI (Boyeau et al., 2025) — sample-level heterogeneity modeling; complementary approach focusing on differential analysis

## 7. Glossary
- **scPoli**: single-cell Population Level Integration — the method introduced here
- **Prototype**: representative embedding vector per cell type; mean of all same-type cells in latent space
- **Prototype loss**: additional loss term minimizing distance between cells and their type prototype; improves biological signal clustering
- **Open-world learner**: model that can be extended to new categories (cell types) without retraining from scratch
- **Sample embedding**: learned continuous representation of each biological sample; captures sample-level variation in a low-dimensional space
- **Condition embedding**: scPoli's term for sample/batch representation; replaces one-hot encoding with a learned continuous vector
- **Population-level analysis**: analysis that links cell-level data to sample-level metadata (e.g., disease status, demographics)
