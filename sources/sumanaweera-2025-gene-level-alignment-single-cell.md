---
title: "Gene-level alignment of single-cell trajectories"
authors: Dinithi Sumanaweera, Chenqu Suo, Ana-Maria Cujba, Daniele Muraro, Emma Dann, Krzysztof Polanski, Alexander S. Steemers, et al.
year: 2025
doi: 10.1038/s41592-024-02378-4
category: statistics
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/4030732580/
source_collection: endnote
---

## One-line Summary
Genes2Genes: Bayesian information-theoretic dynamic programming framework for gene-level alignment of single-cell pseudotime trajectories; captures sequential matches and mismatches (insertions/deletions) per gene; applied to reveal gaps between in vitro and in vivo T cell differentiation.

## 1. Document Info
- Journal/Conference: Nature Methods
- Published: January 2025

## 2. Key Contributions
- Genes2Genes: novel trajectory alignment method using Bayesian information-theoretic dynamic programming
- Gene-level alignment: identifies per-gene sequential matches AND mismatches (insertions/deletions) between reference and query trajectories
- Captures distinct clusters of alignment patterns across genes
- Proof-of-concept: in vitro T cell differentiation matches immature in vivo state; lacks TNF signaling genes
- Improves on DTW by removing assumption that every time point must match

## 3. Methods & Architecture
- Bayesian information-theoretic dynamic programming for sequence alignment
- Five-state alignment string: 1-to-1, 1-to-many, many-to-1, insertion, deletion
- Reference vs. query trajectory comparison at individual gene level
- Validated on real-world and simulated single-cell datasets

## 4. Key Results & Benchmarks
- Accurately infers trajectory alignments (real + simulated data)
- In vitro T cells: match immature in vivo state; TNF signaling gene cluster absent in vitro → guides culture optimization
- Identifies mismatched gene clusters not detectable by DTW
- Disease cell-state trajectory analysis demonstrated

## 5. Limitations & Future Work
- Computationally intensive for very large gene sets
- Requires pseudotime trajectory inference as input (upstream dependency)
- Binary reference/query comparison; multi-trajectory alignment not yet addressed

## 6. Related Work
- CellAlign (DTW-based): established trajectory comparison tool (improved upon)
- Teichmann lab trajectory inference methods (Sanger Institute)

## 7. Glossary
- **Pseudotime trajectory**: Computational ordering of cells along a developmental or dynamic process
- **Dynamic time warping (DTW)**: Classic sequence alignment algorithm; assumes full matching
- **Insertion/deletion (indel)**: Unmatched states in trajectory alignment — gene present in one trajectory but not the other
- **Bayesian information criterion (BIC)**: Model selection criterion balancing fit and complexity
