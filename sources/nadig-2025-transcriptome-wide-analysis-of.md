---
title: "Transcriptome-wide analysis of differential expression in perturbation atlases"
authors: Ajay Nadig, Joseph M. Replogle, Angela N. Pogson, Mukundh Murthy, Steven A. McCarroll, Jonathan S. Weissman, Elise B. Robinson, Luke J. O'Connor
year: 2025
doi: 10.1038/s41588-025-02169-3
category: single-cell-dl
pdf_path: papers/nadig-2025-transcriptome-wide-analysis-of.pdf
pdf_filename: nadig-2025-transcriptome-wide-analysis-of.pdf
source_collection: downloads-perturb-batch
---

## One-line Summary

TRADE is a statistical method that estimates the full distribution of true differential expression effects in Perturb-seq, introducing a "transcriptome-wide impact" (TI) metric that captures signal missed by per-gene significance thresholds — showing that a typical gene perturbation moves ~45 genes and a typical essential gene moves >500.

## 1. Document Info
- Journal: Nature Genetics, Vol 57, May 2025, 1228-1237
- Received: 24 June 2024
- Accepted: 17 March 2025

## 2. Key Contributions

- **TRADE** fits an `ash`-based mixture model to pseudobulk DE point estimates and standard errors, recovering the true effect-size distribution while accounting for noise from small per-perturbation sample sizes.
- **Transcriptome-wide impact (TI)**: the variance of the inferred effect distribution — a single-number summary of "how much does this perturbation move the transcriptome overall".
- **Effective number of DEGs (πDEG)**: derived from kurtosis; quantifies how many genes are needed to explain most of TI, without an arbitrary zero/nonzero boundary.
- **Empirical findings**: applied to K562, RPE1, Jurkat, HepG2 Perturb-seq atlases — only ~13-36% of TI is captured by FDR-significant genes; median πDEG ≈ 45 for typical perturbations and >500 for essential genes.
- **Genetic-transcriptomic bridge**: uses TI to connect GWAS-derived heritability-style metrics to Perturb-seq signals across neuropsychiatric disorders.

## 3. Methods & Architecture

- **Input**: pseudobulk DE from DESeq2 — point estimates β̂_g and standard errors per gene per perturbation.
- **Model**: β̂_g = β_g + ε_g with ε_g ∼ N(0, σ_g²); fit distribution of β using `ash` (adaptive shrinkage, Stephens 2016).
- **Estimand**: Var(β) = transcriptome-wide impact (TI).
- **Derived quantities**: gene-set enrichments, cross-experiment correlations, effective number of DEGs — all unbiased at finite sample size.
- **Comparison methods that fail this bar**: iDEA π (biased at finite n), energy distance (ambiguous units), running-sum GSEA (no clean estimand).

## 4. Key Results & Benchmarks

- K562-GenomeWide (9,866 perturbations): median πDEG = 45; 36% of TI captured by FDR-significant genes.
- K562/Jurkat/HepG2/RPE1 essential atlases: 13-35% of TI in significant genes, >500 median πDEG for essential genes.
- Downsampling K562 by 50%: significant-gene signal drops sharply, but TI estimate changes only slightly — TI is far more robust than DEG counts for cross-experiment comparison (TI R² = 59.7% vs. DEG count R² = 28.4%).
- Cross cell-type comparison shows moderate but not complete consistency of perturbation effects; identifies perturbations with qualitatively different responses across dosage.
- Connects Perturb-seq TI to GWAS heritability-style analysis for schizophrenia, bipolar, autism — bridging genetic and transcriptomic correlations.

## 5. Limitations & Future Work

- Slight downward bias in TI at low sample size (inherited from failure to detect very small effects).
- Built for CRISPRi gene-level KD; does not directly model variant-level effects or dose-response shapes outside the tested perturbations.
- DESeq2 pseudobulk: inherits DESeq2's assumptions about overdispersion and count-level noise.
- TI is population-level — does not capture which *cells* within a perturbation respond strongly.

## 6. Related Work

- Dixit 2016 Perturb-seq, Replogle 2022 genome-scale Perturb-seq — the data TRADE is designed to analyze.
- SNP heritability methods (LD score regression, GCTA) — philosophical template.
- iDEA, energy distance, GSEA — alternative DE summary methods TRADE outperforms.

## 7. Glossary

- **TI (transcriptome-wide impact)**: Var(β_g) across all genes g, where β is the true log2FC under perturbation.
- **πDEG**: effective number of genes needed to explain most of TI, computed from kurtosis.
- **ash**: adaptive shrinkage, a Bayesian method for estimating an effect-size distribution from point estimates + SEs.
- **Perturb-seq**: pooled CRISPR screen read out by single-cell RNA-seq.
