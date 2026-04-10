---
title: "Spatial landmark detection and tissue registration with deep learning"
authors: Markus Ekvall, Ludvig Bergenstråhle, Alma Andersson, Paulo Czarnewski, Johannes Olegård, Lukas Käll, Joakim Lundeberg
year: 2024
doi: 10.1038/s41592-024-02199-5
category: other
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/3910611928/
source_collection: endnote
---

## One-line Summary
ELD (effortless landmark detection): unsupervised deep learning method using neural-network-guided thin-plate splines for spatial landmark detection and tissue registration across histology and spatial transcriptomics data; handles small datasets, nonlinear deformations, and multimodal inputs.

## 1. Document Info
- Journal/Conference: Nature Methods
- Published: April 2024

## 2. Key Contributions
- ELD: unsupervised landmark detection + image registration using neural network + thin-plate splines (TPS)
- No large training dataset required (works with <10 samples)
- Handles nonlinear/elastic deformations (not just affine)
- Supports multimodal spatial omics (histology, Visium, MSI)
- 3D z-stack alignment capability

## 3. Methods & Architecture
- Landmark detector network (CNN-based) identifies landmarks in images
- Thin-plate splines (TPS) for precise image warping/registration (no generative model needed)
- Built on Sanchez et al. unsupervised landmark detection framework
- Evaluated on histology, spatially resolved transcriptomics, mass spectrometry imaging

## 4. Key Results & Benchmarks
- Superior landmark detection accuracy and stability vs. existing methods
- Works with small datasets (relevant for spatial omics experiments with <10 tissue sections)
- Successfully aligns multimodal spatial data (histology + transcriptomics)
- 3D tissue reconstruction from z-stacks demonstrated

## 5. Limitations & Future Work
- Performance on highly irregular tissue morphologies not fully characterized
- Requires spatial omics data preprocessing before registration

## 6. Related Work
- Spatial transcriptomics tissue registration methods (affine-only approaches)
- Sanchez et al.: foundational unsupervised landmark detection framework

## 7. Glossary
- **Thin-plate splines (TPS)**: Mathematical function for smooth interpolation/warping of 2D/3D coordinates
- **CCF**: Common coordinate framework — reference atlas space for tissue registration
- **Spatial omics**: Technologies measuring molecular data with spatial coordinates (e.g., Visium, MERFISH)
- **MSI**: Mass spectrometry imaging — spatial metabolomics/proteomics modality
