---
title: "Cell2fate infers RNA velocity modules to improve cell fate prediction"
authors: Alexander Aivazidis, Fani Memi, Vitalii Kleshchevnikov, Sezgin Er, Brian Clarke, Oliver Stegle, Omer Ali Bayraktar
year: 2025
doi: 10.1038/s41592-025-02608-3
source: aivazidis-2025-cell2fate-infers-rna.md
category: single-cell-dl
tags: [RNA-velocity, Bayesian, ODE, cell-fate, scRNA-seq, modules, developing-brain]
---

## Summary
Cell2fate improves RNA velocity by linearizing the velocity ODE within a fully Bayesian framework, decomposing solutions into interpretable modules. Outperforms scVelo on complex dynamics and rare/mature cell types; spatially maps velocity modules in developing human brain.

## Key Contributions
- Bayesian ODE linearization → biophysically accurate RNA velocity without numerical approximations
- Module decomposition links RNA velocity to dimensionality reduction
- Better performance on rare/mature cell types and weak dynamical signals
- Spatial mapping of RNA velocity modules in developing human brain

## Methods & Architecture
Bayesian linearized ODE model; velocity module decomposition; benchmarked against scVelo/velociraptor; applied to human brain scRNA-seq + spatial transcriptomics.

## Results
- Improved reconstruction of complex dynamics vs. existing methods
- RNA velocity modules spatially localized in developing human brain tissue

## Limitations
Linearization may fail for highly nonlinear dynamics; requires spliced/unspliced counts.

## Related Papers
- [[single-cell-dl/wang-2024-scsemiprofiler-advancing-large]] — deep generative model for single-cell
