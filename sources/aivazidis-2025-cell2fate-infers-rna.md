---
title: "Cell2fate infers RNA velocity modules to improve cell fate prediction"
authors: Alexander Aivazidis, Fani Memi, Vitalii Kleshchevnikov, Sezgin Er, Brian Clarke, Oliver Stegle, Omer Ali Bayraktar
year: 2025
doi: 10.1038/s41592-025-02608-3
category: single-cell-dl
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/0432273717/Aivazidis-2025-Cell2fate infers RNA velocity m.pdf
pdf_filename: Aivazidis-2025-Cell2fate infers RNA velocity m.pdf
source_collection: endnote
---

## One-line Summary
Cell2fate reformulates RNA velocity using a Bayesian linearization of the velocity ODE, decomposing solutions into interpretable modules and enabling biophysically accurate cell fate prediction; applied to developing human brain to spatially map RNA velocity modules.

## 1. Document Info
- Journal/Conference: Nature Methods
- Published: April 2025 (Vol. 22, 698–707)

## 2. Key Contributions
- Developed cell2fate: Bayesian RNA velocity model using ODE linearization for biophysically accurate estimation
- Decomposes RNA velocity into modules, linking velocity to statistical dimensionality reduction
- Avoids coarse biophysical approximations (existing models) and extensive numerical approximations
- Enhanced interpretability and power for complex/weak dynamical signals and rare/mature cell types
- Applied to developing human brain: spatially maps RNA velocity modules onto tissue architecture

## 3. Methods & Architecture
- Linearization of RNA velocity ODE → fully Bayesian model
- Module decomposition of velocity solutions (connects RNA velocity to dimensionality reduction)
- Benchmarked against scVelo, velociraptor, and other RNA velocity methods on real datasets
- Application: developing human brain scRNA-seq + spatial transcriptomics mapping

## 4. Key Results & Benchmarks
- cell2fate outperforms existing methods on complex dynamics and weak dynamical signals
- Enhanced detection of dynamics in rare and mature cell types (missed by previous methods)
- RNA velocity modules spatially map onto distinct tissue regions in developing human brain
- Biophysical accuracy improved over scVelo and other approximation-based methods

## 5. Limitations & Future Work
- Linearization may break down for highly nonlinear dynamics
- Computationally more demanding than simpler velocity methods
- Requires both spliced and unspliced counts (not always available)

## 6. Related Work
- scVelo (Bergen et al. 2020): dynamical RNA velocity model
- UniTVelo, velociraptor: other RNA velocity refinements
- Bayesian single-cell models: scVI (Lopez et al. 2018)

## 7. Glossary
- **RNA velocity**: Rate of change of mRNA abundance estimated from spliced/unspliced ratio
- **ODE**: Ordinary differential equation — governing RNA transcription/splicing/degradation dynamics
- **Bayesian model**: Statistical framework treating parameters as distributions; enables uncertainty quantification
- **Velocity module**: Decomposed component of the RNA velocity solution associated with a biological process
