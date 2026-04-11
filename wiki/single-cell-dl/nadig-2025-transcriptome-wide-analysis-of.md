---
title: "Transcriptome-wide analysis of differential expression in perturbation atlases"
authors: Ajay Nadig, Joseph M. Replogle, Angela N. Pogson, Mukundh Murthy, Steven A. McCarroll, Jonathan S. Weissman, Elise B. Robinson, Luke J. O'Connor
year: 2025
doi: 10.1038/s41588-025-02169-3
source: nadig-2025-transcriptome-wide-analysis-of.md
category: single-cell-dl
tags: [Perturb-seq, differential-expression, transcriptome-wide-impact, CRISPRi, statistics, effect-size-distribution, neuropsychiatric]
---

## Summary

TRADE attacks a statistical problem baked into Perturb-seq: per-perturbation sample sizes are small, so per-gene significance tests miss most of the signal. Instead of testing one gene at a time, TRADE fits a distribution to the full set of DE effect sizes (with their SEs) using adaptive shrinkage, and summarizes that distribution with two estimands — **transcriptome-wide impact (TI)**, the variance of the true effect distribution, and **effective number of DEGs (πDEG)**, derived from kurtosis. The punchline: in K562 genome-scale Perturb-seq, FDR-significant genes explain only 36% of TI, and a typical gene perturbation affects ~45 genes transcriptome-wide.

## Key Contributions

- A clean estimand for "how much does this perturbation move the transcriptome" — one that is interpretable, unbiased at finite sample size, and directly comparable across experiments.
- Empirical demonstration that standard Perturb-seq analyses miss 60-85% of the signal captured by TI.
- Shows that TI is far more reproducible across experiments than DEG counts (R² 59.7% vs. 28.4% in downsampling).
- Bridges Perturb-seq effect sizes to GWAS-style heritability metrics across neuropsychiatric disorders.

## Methods & Architecture

**The statistical problem**: for perturbation g with few cells, β̂_g is noisy. Thresholding at FDR 5% per gene discards many real small effects. But aggregated across ~20,000 genes, those small effects carry most of the variance.

**TRADE's move**:
1. Compute DESeq2 pseudobulk β̂_g, SE_g for every gene under every perturbation.
2. Fit the distribution of true β_g via `ash` (adaptive shrinkage) — a nonparametric mixture that honestly treats noise.
3. Report Var(β_g) as **TI**, kurtosis-derived **πDEG**, cross-experiment correlations, and gene-set enrichments.

**Why this beats per-gene significance**: the per-gene FDR is a property of the *test*, not of the biology. Two perturbations with identical real effects but different n will look very different in DEG counts and nearly identical in TI.

## Results

| Dataset | % of TI in FDR-sig genes | median πDEG |
|---------|-------------------------|-------------|
| K562-GenomeWide (9,866 perturbations) | 36% | 45 |
| K562-Essential | 18% | >500 (essential) |
| RPE1-Essential | 35% | >500 |
| Jurkat-Essential | 13% | >500 |
| HepG2-Essential | 14% | >500 |

- Downsampling K562 to 50% of GEM groups: DEG counts drop sharply, TI barely moves. TI is the stable quantity.
- Essential-gene perturbations hit >500 genes; typical gene perturbations hit ~45. The gap is nearly an order of magnitude.
- Cross cell-type analysis: perturbation effects are moderately, not completely, consistent across cell types. Some perturbations show qualitatively different responses at different dosages.
- Connects TI to heritability-based analyses for schizophrenia, bipolar, autism — quantitative bridge between GWAS and Perturb-seq.

## Limitations

- Pseudobulk throws away single-cell heterogeneity within a perturbation. TI is a population-level quantity.
- Slight downward bias in TI at small n (very small effects are undetectable even in aggregate).
- CRISPRi gene knockdown only — does not model variant-level effects, which is the central gap for interpreting GWAS loci.
- Inherits DESeq2's assumptions on overdispersion and read-count noise.

## Related Papers

- [[neuroscience/jin-2020-in-vivo-perturb-seq]] — in vivo Perturb-seq for autism genes; TRADE is the analysis layer such data needs
- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle simulates what Perturb-seq measures; TRADE is how you grade those simulations
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT perturbation prediction; TI is the natural benchmark target
- [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]] — PerturBERT learns perturbation signatures; TRADE characterizes what those signatures should match
- [[neuroscience/paulsen-2022-autism-genes-converge]] — autism gene convergence in organoids; TI-style analysis would sharpen the convergence claim
