---
title: "scSemiProfiler: Advancing large-scale single-cell studies through semi-profiling with deep generative models and active learning"
authors: Jingtao Wang, Gregory J. Fonseca, Jun Ding
year: 2024
doi: 10.1038/s41467-024-50150-1
source: wang-2024-scsemiprofiler-advancing-large.md
category: single-cell-dl
tags: [scRNA-seq, deep-generative-model, active-learning, bulk-RNA-seq, cost-reduction, cohort]
---

## Summary
scSemiProfiler reduces cost of large-cohort single-cell studies by combining bulk RNA-seq for all samples with targeted scRNA-seq on a few active-learning-selected representatives, using a deep generative model to infer full single-cell profiles across the cohort.

## Key Contributions
- Semi-profiling framework: bulk RNA-seq + selected scRNA-seq + generative model → full cohort single-cell profiles
- Active learning sample selection outperforms random selection
- Validated across heterogeneous datasets; inferred profiles match ground truth

## Methods & Architecture
VAE-based deep generative model conditioned on bulk RNA-seq; active learning for representative sample selection; validated against full scRNA-seq ground truth.

## Results
- Inferred profiles enable standard downstream single-cell analyses
- Active learning selection maximizes information per dollar spent
- Scalable to large disease cohort studies

## Limitations
Relies on bulk-single-cell correspondence; may miss rare cell types.

## Related Papers
