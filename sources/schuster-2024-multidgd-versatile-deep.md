---
title: "multiDGD: A versatile deep generative model for multi-omics data"
authors: Viktoria Schuster, Emma Dann, Anders Krogh, Sarah A. Teichmann
year: 2024
doi: 10.1038/s41467-024-53340-z
category: single-cell-dl
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/1570100585/Schuster-2024-multiDGD_ A versatile deep gener.pdf
pdf_filename: Schuster-2024-multiDGD_ A versatile deep gener.pdf
source_collection: endnote
---

## One-line Summary
multiDGD is a scalable deep generative model providing a probabilistic framework for joint representation of scRNA-seq + scATAC-seq, with outstanding data reconstruction without feature selection, post-hoc data integration via covariate modeling, and statistical gene-regulatory region associations.

## 1. Document Info
- Journal/Conference: Nature Communications
- Published: 2024

## 2. Key Contributions
- Scalable deep generative model for paired scRNA-seq + scATAC-seq (multi-omics)
- Outstanding data reconstruction without feature selection (vs. existing methods)
- Probabilistic modeling of sample covariates enables post-hoc batch integration without fine-tuning
- Detects statistical associations between genes and regulatory regions conditioned on learned representations
- scverse-compatible; open-source on GitHub

## 3. Methods & Architecture
- Deep generative model (VAE-based) with separate decoders for RNA and chromatin modalities
- Shared latent space for joint representation learning
- Probabilistic covariate modeling (sample-level) for integration of multiple batches
- Gene-regulatory region association: statistical testing conditioned on representations
- Benchmarked on human + mouse datasets

## 4. Key Results & Benchmarks
- Data reconstruction: outperforms existing multi-omics methods without feature selection
- Well-clustered joint representations on human + mouse datasets (multiple cell types)
- Post-hoc integration: effective batch correction without fine-tuning via covariate modeling
- Gene-regulatory associations: identifies known TF–CRE links; novel candidates identified

## 5. Limitations & Future Work
- Currently paired RNA+ATAC; extension to other modality pairs not demonstrated
- Scalability tested on moderate-scale datasets; ultra-large (>1M cells) not benchmarked
- Associations are statistical; require experimental validation

## 6. Related Work
- scVI (Lopez et al.): foundational VAE for scRNA-seq
- MOFA: multi-omics factor analysis
- ArchR, Signac: ATAC-seq analysis frameworks
- Li et al. 2025 (UDA-seq): complementary multimodal data generation

## 7. Glossary
- **DGD**: Deep Generative Decoder
- **VAE**: Variational autoencoder — probabilistic deep generative model
- **Post-hoc integration**: Integration without retraining; uses covariate modeling
- **Feature selection**: Filtering to highly variable features; multiDGD avoids this step
- **scverse**: Open-source single-cell analysis ecosystem (AnnData, scanpy, etc.)
