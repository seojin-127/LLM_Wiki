---
title: "PerturbNet predicts single-cell responses to unseen chemical and genetic perturbations"
authors: Hengshi Yu, Weizhou Qian, Yuxuan Song, Joshua D Welch
year: 2025
doi: 10.1038/s44320-025-00131-3
category: single-cell-dl
pdf_path: papers/yu-2025-perturbnet-predicts-single-cell-responses.pdf
pdf_filename: yu-2025-perturbnet-predicts-single-cell-responses.pdf
source_collection: manual
---

## One-line Summary

PerturbNet is a modular deep generative framework using conditional normalizing flows (cINN) to predict the full distribution of single-cell states induced by unseen chemical, genetic (CRISPRa/CRISPRi), and coding-sequence (missense mutation) perturbations.

## 1. Document Info
- Journal: Molecular Systems Biology (EMBO)
- Received: 6 May 2025
- Revised: 3 June 2025
- Accepted: 17 June 2025
- Published: 10 July 2025

## 2. Key Contributions

- Introduces PerturbNet, a modular three-network architecture (perturbation encoder + cell state encoder + conditional invertible neural network) that predicts **distributional** (not just mean) cell-state responses to perturbations
- First method to predict gene expression changes induced by **missense mutations** using protein language model (ESM) embeddings
- Handles three perturbation types in one framework: small molecules (ChemicalVAE), genetic perturbations (GenotypeVAE with GO annotations), and coding-sequence variants (ESM embeddings)
- Outperforms GEARS, chemCPA, and Biolord on multiple benchmarks; particularly strong improvement for **completely unseen genes**
- Demonstrates practical application: predicts effects of all 7,847 possible GATA1 point mutations, identifying variants that block erythroid differentiation in the DNA-contact region

## 3. Methods & Architecture

### Three-Module Design
1. **Perturbation Representation Network** — encodes perturbation into latent space
   - Chemical: ChemicalVAE trained on ~250K ZINC drug-like molecules (SMILES → latent)
   - Genetic (CRISPRa/CRISPRi): GenotypeVAE trained on ~177M single/double-gene GO annotation vectors
   - Coding-sequence: pretrained ESM transformer (250M protein sequences) → deterministic embeddings + Gaussian noise

2. **Cellular Representation Network** — encodes cell states
   - VAE with either Gaussian or ZINB (zero-inflated negative binomial) likelihood
   - Can work on raw counts (ZINB) or normalized data (Gaussian)

3. **Mapping Network (cINN)** — conditional invertible neural network (conditional normalizing flow)
   - Maps perturbation representation → cell state distribution
   - Invertible by construction → stable training
   - Can condition on covariates (dosage, cell type)
   - Outputs a **distribution** of cell states, not just a mean

### Key Design Principles
- **Modularity**: perturbation and cell encoders are independently trained and interchangeable ("mix and match")
- **Pretrained representations**: ChemicalVAE, GenotypeVAE, and ESM can all be pretrained on large unpaired datasets
- **Distributional prediction**: cINN models full conditional distribution p(X|G), capturing cell-state heterogeneity that mean-prediction methods miss

## 4. Key Results & Benchmarks

### Chemical Perturbation (small molecules)
- **LINCS-Drug** (19,990 compounds): PerturbNet outperforms chemCPA; median R²=0.919 (all genes), 0.894 (top 50 DEGs)
- **sci-Plex** (180 compounds, 648K cells): PerturbNet median R²=0.984 (all genes), outperforms Biolord
- Identified stereoisomer data leakage issue in prior benchmarks

### Genetic Perturbation (CRISPRa)
- **Norman et al.** (K562, 230 perturbations): PerturbNet outperforms GEARS and Biolord
  - Median R²=0.942 (all genes), 0.629 (top 50 DEGs)
  - GEARS: 0.858 (all genes), 0.513 (DEGs)
  - Strongest improvement for both-unseen gene combinations
- Better prediction of non-additive genetic interactions (neomorphic, potentiation, strong synergy)
- Worse on redundant interactions

### Coding-Sequence Mutations (first-of-its-kind)
- **Ursu (TP53 + KRAS)**: outperforms baselines on large-effect genes
- **Jorge (GATA1)**: significantly higher R² than all baselines
- All 7,847 GATA1 point mutations predicted → three classes: erythroid-depleted, intermediate, enriched
- Large-effect variants validated in GATA1 DNA-contact region with large amino acid side-chain volume changes

## 5. Limitations & Future Work

- Perturbation representation quality limits prediction (poorly represented perturbations = poor predictions)
- Chemical stereoisomer handling still imperfect (same formula, different 3D orientation)
- CRISPRa/CRISPRi predictions depend on GO annotation completeness (similar limitation to GEARS)
- Coding-sequence variant predictions not yet validated for non-coding regulatory variants
- Distributional predictions harder to evaluate quantitatively than mean predictions
- Does not model causal mechanisms — still Level 2 (generative/interpolation)

## 6. Related Work

- scGen (Lotfollahi et al., 2019) — VAE latent arithmetic for perturbation prediction
- CPA (Lotfollahi et al., 2023) — compositional perturbation autoencoder
- chemCPA (Hetzel et al., 2022) — chemical perturbation with transfer learning
- GEARS (Roohani et al., 2023) — GNN + knowledge graph for genetic perturbation
- Biolord (Piran et al., 2024) — disentangled representations for perturbation
- ESM (Rives et al., 2021) — protein language model used for sequence embeddings
- Norman et al. (2019) — CRISPRa combinatorial screen dataset
- Ursu et al. (2022) — CRISPR genome editing of TP53/KRAS
- Martin-Rufino (Jorge) et al. (2023) — GATA1 variant screen in hematopoiesis

## 7. Glossary

- **cINN**: Conditional Invertible Neural Network — normalizing flow that models conditional distributions; invertible by construction
- **Normalizing flow**: generative model that transforms a simple distribution (Gaussian) through a series of invertible transformations
- **ChemicalVAE**: VAE trained on SMILES strings to encode small-molecule structures
- **GenotypeVAE**: VAE trained on Gene Ontology annotation vectors to encode genetic perturbations
- **ESM**: Evolutionary Scale Modeling — pretrained protein language model (transformer)
- **ZINB**: Zero-Inflated Negative Binomial — likelihood model for sparse scRNA-seq count data
- **CRISPRa/CRISPRi**: CRISPR activation/interference — modulates gene expression without changing DNA sequence
- **Stereoisomer**: molecules with same formula and atom arrangement but different 3D orientation
- **sci-Plex**: single-cell combinatorial indexing for chemical perturbation screens
