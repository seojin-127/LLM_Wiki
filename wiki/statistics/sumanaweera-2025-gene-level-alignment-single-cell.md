---
title: "Gene-level alignment of single-cell trajectories"
authors: Dinithi Sumanaweera, Chenqu Suo, Ana-Maria Cujba, Daniele Muraro, Emma Dann, et al.
year: 2025
doi: 10.1038/s41592-024-02378-4
source: sumanaweera-2025-gene-level-alignment-single-cell.md
category: statistics
tags: [trajectory-alignment, pseudotime, dynamic-programming, Bayesian, single-cell, T-cell, in-vitro-vs-in-vivo]
---

## Summary
Genes2Genes: a Bayesian information-theoretic dynamic programming framework for aligning single-cell pseudotime trajectories at the gene level. Unlike DTW, captures sequential mismatches (insertions/deletions) per gene. Reveals that in vitro T cells match an immature in vivo state while lacking TNF signaling gene expression — demonstrating utility for optimizing cell culture systems.

## Key Contributions
- Genes2Genes: gene-level trajectory alignment using Bayesian information-theoretic dynamic programming
- Five-state alignment: 1-to-1, 1-to-many, many-to-1, insertion, deletion
- Removes DTW assumption that every time point must match
- Identifies clusters of genes with distinct alignment patterns
- Application: in vitro vs. in vivo T cell comparison reveals missing TNF signaling

## Methods & Architecture
- Bayesian information-theoretic DP for sequence alignment
- Gene-level scoring: per-gene alignment between reference and query trajectories
- Validated on real and simulated single-cell datasets
- Inputs: pseudotime trajectories from any pseudotime inference method

## Results
- Accurately infers trajectory alignments vs. ground truth (simulated data)
- In vitro T cells: match immature in vivo state; TNF signaling gene cluster absent
- Identifies gene clusters with distinct alignment patterns across trajectories
- Disease cell-state trajectory analysis demonstrated

## Limitations
- Requires pseudotime trajectory inference upstream
- Computationally intensive for large gene sets
- Binary reference/query only; multi-trajectory comparison not yet supported

## Related Papers
- CellAlign (DTW-based trajectory comparison) — predecessor method improved upon
- [[single-cell-dl/fischer-2024-sctab-scaling-cross-tissue]] — cross-tissue single-cell integration (complementary)
