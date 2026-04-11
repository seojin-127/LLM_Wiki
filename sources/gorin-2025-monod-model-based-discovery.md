---
title: "Monod: model-based discovery and integration through fitting stochastic transcriptional dynamics to single-cell sequencing data"
authors: Gennady Gorin, Tara Chari, Maria Carilli, John J. Vastola, Lior Pachter
year: 2025
doi: 10.1038/s41592-025-02832-x
category: single-cell-dl
pdf_path: papers/gorin-2025-monod-model-based-discovery.pdf
pdf_filename: gorin-2025-monod-model-based-discovery.pdf
source_collection: downloads-perturb-batch
---

## One-line Summary

Monod fits biophysically interpretable stochastic models of transcription (bursty, constitutive, extrinsic, Cox-Ingersoll-Ross) jointly to nascent and mature mRNA counts per cell, extracting burst size, burst frequency, splicing rate, and degradation rate — revealing regulatory modulation invisible to average-expression analyses and enabling cross-platform integration without distortive normalization.

## 1. Document Info
- Journal: Nature Methods, Vol 22, Nov 2025, 2286-2300
- Published online: 7 November 2025

## 2. Key Contributions

- **Biophysical model fitting at single-cell scale**: Monod fits chemical master equation models (bursty, extrinsic, CIR, deterministic-degradation, deterministic-splicing) to joint nascent + mature RNA counts per gene per cell type.
- **Burst-frequency vs. burst-size decomposition**: distinguishes *noise modulation* (variance change at constant mean) from *mean modulation* — a distinction traditional DE cannot make.
- **Cross-platform integration**: same model applied to 10x, Smart-seq, etc.; technical parameters (capture efficiency, length bias) absorbed into the technical component of the model.
- Demonstrated across 9 datasets spanning cell culture, cancer, radiation, development, blood, brain.

## 3. Methods & Architecture

**Model structure** (bursty default):
- Biological: bursty transcription → nascent RNA X_N → splicing β → mature X_M → degradation γ.
- Technical: nascent capture rate C_N × L (gene length dependent), mature capture rate λ_M (length independent).
- Steady-state assumption; rates in units of k (so k=1).

**Model choices supported**:
- Constitutive (Poisson, no overdispersion — baseline only).
- Bursty (geometric burst size) — **default**.
- Extrinsic (gamma-distributed transcription rate).
- Cox-Ingersoll-Ross quasi-bursty limit.
- Deterministic splicing / degradation waiting times.

**Inference**:
- Technical parameters shared across genes within a cell type; grid search.
- Biological parameters per gene; gradient descent on KLD.
- Uncertainty via Fisher information matrix.
- Post-hoc goodness-of-fit tests.

## 4. Key Results & Benchmarks

- **IdU-induced DNA damage**: genome-wide noise enhancement detected via burst-size modulation without average expression change — invisible to standard DE.
- **Mouse glutamatergic vs. GABAergic neurons**: identifies genes with large noise differences but little average expression change.
- **Germ-cell development E11-E16**: nascent/mature dynamics reveal splicing and degradation FC changes along trajectory.
- **Cross-platform**: fits same biological parameters with different technical parameters for 10x vs. Smart-seq.

## 5. Limitations & Future Work

- Steady-state assumption — not valid during rapid transitions.
- Technical parameters are weakly identifiable; requires shared-gene assumption.
- Bursty model may not fit all genes; goodness-of-fit tests required.
- Computational cost for large atlases.
- Not a perturbation prediction tool — it is a descriptive + mechanistic modeling framework.

## 6. Related Work

- scVelo (Bergen 2020) — also uses nascent/mature but for velocity, not bursting.
- Previous biophysical models (Munsky, Singh) — fluorescence-transcriptomics tradition Monod adapts to sequencing.
- cellRank, scDiffEq — dynamics modeling alternatives that do not use biophysical priors.

## 7. Glossary

- **Bursty transcription**: RNA produced in discrete bursts with geometric burst size, reflecting promoter on/off kinetics.
- **Burst frequency (k)**: how often transcription bursts occur.
- **Burst size (b)**: mean number of transcripts per burst.
- **Nascent / mature RNA**: unspliced vs. spliced transcripts; distinguishable via intron read alignment.
- **Fisher information matrix**: used for uncertainty quantification in maximum-likelihood estimation.
- **CME (chemical master equation)**: describes the time evolution of a Markov-jump process for molecular counts.
