---
title: "Single-cell genomics decontamination using CellSweep"
authors: Caskey, Conor W., Stoeckius, Marlon
year: 2026
doi: 10.64898/2026.03.04.709349
category: single-cell-dl
pdf_path: papers/caskey-2026-single-cell-genomics-decontamination.pdf
pdf_filename: caskey-2026-single-cell-genomics-decontamination.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

CellSweep is a fast multinomial mixture model (EM-based) for ambient RNA decontamination in scRNA-seq, achieving 98.84% cross-species contamination removal in 25 seconds on 16 CPU threads across 10x, Smart-seq2, ATAC-seq, and spatial transcriptomics.

## 1. Document Info
- Journal/Conference: bioRxiv preprint
- Received/Published: March 6, 2026 (DOI: 10.64898/2026.03.04.709349)

## 2. Key Contributions
- CellSweep: multinomial mixture model decomposing each cell's counts into cell-type-specific, ambient RNA, and bulk contamination components; parameters inferred by Expectation-Maximization (EM)
- Extremely fast: 25 seconds on 16 CPU threads for a typical scRNA-seq dataset
- Broad applicability: validated on 10x Chromium, Smart-seq2, ATAC-seq (open chromatin), and Visium HD spatial transcriptomics
- Alternative model for datasets without empty droplets / non-cellular barcodes (captures-only mode)

## 3. Methods & Architecture
- **Model**: multinomial mixture model with three components per cell:
  1. Cell-type-specific expression profile (clean signal)
  2. Ambient RNA profile (estimated from empty droplets)
  3. Bulk contamination profile (e.g., cross-species contamination)
- **Parameter inference**: Expectation-Maximization (EM) algorithm iterates until convergence
- **Input**: standard count matrix (cells × genes) + optional cell type annotations + empty droplet barcodes
- **Alternative mode**: when empty droplets are unavailable, CellSweep estimates the ambient profile directly from the count matrix
- **Output**: decontaminated count matrix with per-cell contamination fractions
- **Implementation**: multithreaded C++ (16 threads for speed benchmark)

## 4. Key Results & Benchmarks
- Cross-species contamination (human/mouse cell mixing): 98.84% contamination removal
- Runtime: 25 seconds on 16 CPU threads (competitive with SoupX, DecontX, CellBender)
- Simulation benchmark: PPV (Positive Predictive Value) = 0.981
- Validated on: 10x Chromium scRNA-seq, Smart-seq2, scATAC-seq, Visium HD spatial transcriptomics
- Robust when non-cellular barcodes are absent (alternative estimation mode)

## 5. Limitations & Future Work
- EM convergence sensitive to initialization; may require careful initialization in highly heterogeneous datasets
- Ambient profile estimation in captures-only mode less precise than when empty droplets are available
- Benchmarked primarily on well-defined contamination scenarios; performance on subtle ambient contamination may vary
- Future: integration with standard pipelines (Seurat, Scanpy); extension to multi-sample decontamination

## 6. Related Work
- SoupX (Young & Behjati, 2020) — ambient RNA removal using cell clustering + empty droplet profiles
- DecontX (Yang et al., 2020) — Bayesian mixture model for ambient RNA decontamination
- CellBender (Fleming et al., 2023) — deep learning-based ambient RNA removal
- DoubletFinder, Scrublet — related quality control tools for single-cell data

## 7. Glossary
- **Ambient RNA**: free-floating RNA released from lysed cells that contaminates droplets in 10x Genomics and similar platforms
- **Empty droplets**: droplets that capture ambient RNA but no live cells; used to estimate the ambient expression profile
- **EM (Expectation-Maximization)**: iterative optimization algorithm for latent variable models; alternates between inferring latent states (E-step) and updating parameters (M-step)
- **Multinomial mixture model**: probabilistic model where each count observation is drawn from a mixture of multinomial distributions (one per component)
- **PPV (Positive Predictive Value)**: proportion of predicted-contaminated counts that are truly contaminated; measure of decontamination precision
- **Visium HD**: 10x Genomics spatial transcriptomics platform with high-resolution spot grid (~2 µm bins)
- **Cross-species contamination**: experimental artifact from mixing human and mouse cells, used as a gold-standard benchmark for decontamination
