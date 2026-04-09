---
title: "scSemiProfiler: Advancing large-scale single-cell studies through semi-profiling with deep generative models and active learning"
authors: Jingtao Wang, Gregory J. Fonseca, Jun Ding
year: 2024
doi: 10.1038/s41467-024-50150-1
category: single-cell-dl
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/0353661551/Wang-2024-scSemiProfiler_ Advancing large-scal.pdf
pdf_filename: Wang-2024-scSemiProfiler_ Advancing large-scal.pdf
source_collection: endnote
---

## One-line Summary
scSemiProfiler combines deep generative models with active learning to infer single-cell profiles across large cohorts by fusing bulk RNA-seq with targeted single-cell profiling from a few representative samples, dramatically reducing cost while maintaining single-cell resolution.

## 1. Document Info
- Journal/Conference: Nature Communications
- Published: 2024

## 2. Key Contributions
- Introduced scSemiProfiler: semi-profiling framework combining bulk RNA-seq (cheap) + targeted scRNA-seq of representative samples + deep generative model to infer full cohort single-cell profiles
- Uses active learning to select the most informative representative samples for actual single-cell profiling
- Reduces cost while enabling single-cell-level analyses across large disease cohorts
- Validated across heterogeneous datasets; aligns closely with true single-cell data

## 3. Methods & Architecture
- Deep generative model (VAE-based): learns single-cell profile distribution conditioned on bulk RNA-seq
- Active learning: selects optimal representative samples to maximize information gain per sequencing dollar
- Input: bulk RNA-seq for all samples + scRNA-seq for selected representatives
- Output: inferred single-cell profiles for all samples
- Validation: comparison to ground-truth scRNA-seq across diverse datasets

## 4. Key Results & Benchmarks
- scSemiProfiler inferred profiles closely match true single-cell data across heterogeneous datasets
- Active learning selection outperforms random sample selection
- Enables downstream single-cell analyses (clustering, DE) on inferred profiles
- Cost: far fewer samples require actual scRNA-seq (~$6000/20k cells in 2023)
- Scalable to large disease cohorts originally infeasible for scRNA-seq

## 5. Limitations & Future Work
- Generative model quality depends on bulk-single-cell correspondence
- May miss rare cell types not represented in bulk signal
- Representative sample selection assumes bulk profiles are informative proxies

## 6. Related Work
- CIBERSORTx, MuSiC: deconvolution methods (infer proportions, not full profiles)
- Scaden, TAPE: deep learning deconvolution
- VAE-based single-cell generative models (scVI, scGen)

## 7. Glossary
- **Semi-profiling**: Profiling some samples fully (single-cell) + inferring the rest from bulk + model
- **Active learning**: Iterative strategy to select most informative data points for labeling
- **VAE**: Variational Autoencoder — deep generative model for learning latent data distributions
- **Bulk RNA-seq**: Ensemble average of all cells in a sample; cheaper than single-cell
