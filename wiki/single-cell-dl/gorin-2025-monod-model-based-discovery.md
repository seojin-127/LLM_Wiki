---
title: "Monod: model-based discovery and integration through fitting stochastic transcriptional dynamics to single-cell sequencing data"
authors: Gennady Gorin, Tara Chari, Maria Carilli, John J. Vastola, Lior Pachter
year: 2025
doi: 10.1038/s41592-025-02832-x
source: gorin-2025-monod-model-based-discovery.md
category: single-cell-dl
tags: [biophysical-model, bursty-transcription, nascent-mature-RNA, noise-modulation, mechanistic, Monod, chemical-master-equation]
---

## Summary

Monod is a model-based counter to the standard "normalize and dimensionality-reduce" workflow. It fits chemical master equation models of transcription (bursty by default, with extrinsic, CIR, and deterministic-waiting variants) jointly to **nascent and mature RNA counts** at the per-gene, per-cell-type level. The output is biophysically interpretable parameters — burst size, burst frequency, splicing rate, degradation rate — plus technical parameters for capture efficiency. The payoff is that Monod can detect gene-regulatory changes that leave average expression invariant, which traditional DE misses entirely.

## Key Contributions

- **Mean vs. noise modulation distinction**: burst size and burst frequency changes decompose into variance-only (noise) vs. mean changes. No DE method can make this distinction.
- **Cross-platform integration via the technical model**: capture rate and length bias are absorbed into explicit technical parameters, so the same biological parameters can be compared across 10x, Smart-seq, etc.
- **Interpretable by construction**: every parameter has a biophysical meaning. Contrast with VAE latents.
- **Goodness-of-fit and model comparison**: Monod supports statistical tests for which transcription model fits a given gene, turning gene regulation into a falsifiable hypothesis.

## Methods & Architecture

**Bursty model (default)**:
```
∅ --k--> X_N --β--> X_M --γ--> ∅      (biology)
X_N --C_N·L--> X_N + X'_N              (nascent capture, gene-length-dependent)
X_M --λ_M--> X_M + X'_M                (mature capture, length-independent)
```
with geometric burst size b.

**Other supported models**: constitutive (Poisson baseline), extrinsic (gamma-distributed k), Cox-Ingersoll-Ross quasi-bursty, deterministic splicing/degradation waiting times.

**Fitting**:
- Technical parameters shared across genes within a cell type; grid search.
- Biological parameters fit per gene via gradient descent on KL divergence between empirical and predicted joint nascent/mature count distributions.
- Uncertainty via Fisher information matrix.
- Steady-state assumed (rates expressed in units of k).

## Results

- **IdU-induced DNA damage**: detects genome-wide noise enhancement with little average expression change — invisible to DE.
- **Mouse glutamatergic vs. GABAergic neurons**: finds genes with substantial noise differences but minimal average changes.
- **Germ cell development E11-E16**: reveals splicing and degradation rate changes along developmental trajectory, plus burst frequency shifts.
- **Cross-platform**: same biological parameters recovered across 10x and Smart-seq by fitting different technical parameters.

## Limitations

- Steady-state assumption breaks during rapid transitions.
- Technical parameters are weakly identifiable — must be shared across genes.
- Bursty model does not fit every gene; goodness-of-fit selection is required.
- Computational cost scales with number of genes × cell types × model evaluations.
- Monod is descriptive + mechanistic — it does not predict what happens under perturbation.

## Related Papers

- [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna]] — cell2fate, dynamics inference from nascent/mature RNA
- [[single-cell-dl/vinyard-2025-learning-cell-dynamics-with]] — scDiffEq, neural SDE dynamics (contrast: no biophysical prior)
- [[single-cell-dl/lange-2022-cellrank-for-directed-single]] — CellRank, uses RNA velocity but not biophysical models
- [[statistics/sumanaweera-2025-gene-level-alignment-single-cell]] — gene-level alignment, complementary rigorous framework
- [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] — TRADE, statistical framework for DE; Monod is its mechanistic counterpart
