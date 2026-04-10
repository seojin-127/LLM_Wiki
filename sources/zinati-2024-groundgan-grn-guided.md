---
title: "GRouNdGAN: GRN-guided simulation of single-cell RNA-seq data using causal generative adversarial networks"
authors: Yazdan Zinati, Abdulrahman Takiddeen, Amin Emad
year: 2024
doi: 10.1038/s41467-024-48516-6
category: genomic-dl
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/2639549003/Zinati-2024-GRouNdGAN_ GRN-guided simulation o.pdf
pdf_filename: Zinati-2024-GRouNdGAN_ GRN-guided simulation o.pdf
source_collection: endnote
---

## One-line Summary
GRouNdGAN is a GRN-guided causal GAN that simulates realistic scRNA-seq data with user-specified gene regulatory networks, enabling in silico TF knockout experiments and providing ground-truth GRNs for benchmarking GRN inference algorithms.

## 1. Document Info
- Journal/Conference: Nature Communications
- Published: 2024

## 2. Key Contributions
- GRN-guided GAN: user specifies a GRN; model simulates scRNA-seq where genes are causally expressed under TF control
- Reference-based: trained on real experimental datasets (6 datasets used)
- Captures non-linear TF-gene dependencies; preserves cell trajectories, pseudotime, and biological noise
- In silico perturbation: TF knockout experiments simulated
- GRN inference benchmark: GRouNdGAN bridges gap between simulated and biological benchmarks

## 3. Methods & Architecture
- Causal implicit generative model (GAN architecture)
- GRN imposed in model architecture as causal constraints
- Steady-state + transient-state simulation
- Training on 6 experimental scRNA-seq reference datasets
- Benchmarking: various GRN inference algorithms evaluated on GRouNdGAN output

## 4. Key Results & Benchmarks
- Simulated data matches real data in cell trajectories, pseudotime ordering, and technical noise characteristics
- In silico TF KO: correctly predicts downstream gene expression changes
- GRN inference benchmarking: GRouNdGAN provides more realistic benchmark than curated databases

## 5. Limitations & Future Work
- GRN must be user-specified (prior knowledge required); no de novo GRN learning
- Trained on 6 datasets; generalizability to rare cell types or non-standard tissues unclear
- GAN training instability common to all GAN approaches

## 6. Related Work
- SERGIO: earlier GRN-guided scRNA-seq simulator
- BEELINE/GNNs for GRN inference
- scVI: deep generative model for scRNA-seq (no GRN guidance)

## 7. Glossary
- **GRN**: Gene regulatory network — directed graph of TF→gene regulatory relationships
- **Causal GAN**: GAN where causal structure (GRN) is imposed in the model architecture
- **In silico KO**: Computational knockout experiment; remove TF from simulation to predict downstream effects
- **Implicit generative model**: Model learned from data distribution without explicit density estimation
