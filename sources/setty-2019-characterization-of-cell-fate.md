---
title: "Characterization of cell fate probabilities in single-cell data with Palantir"
authors: Manu Setty, Vaidotas Kiseliovas, Jacob Levine, Adam Gayoso, Linas Mazutis, Dana Pe'er
year: 2019
doi: 10.1038/s41587-019-0068-4
category: single-cell-dl
pdf_path: papers/setty-2019-characterization-of-cell-fate.pdf
pdf_filename: setty-2019-characterization-of-cell-fate.pdf
source_collection: downloads-perturb-batch
---

## One-line Summary

Palantir reframes differentiation as a probabilistic Markov process on a diffusion-map manifold: every cell gets a pseudo-time and a vector of branch probabilities (probability of reaching each terminal state), and the entropy over those probabilities quantifies plasticity — showing that human hematopoiesis is a continuous fate-choice process, not a series of discrete bifurcations.

## 1. Document Info
- Journal: Nature Biotechnology, Vol 37, April 2019, 451-460

## 2. Key Contributions

- **Probabilistic fate instead of discrete branches**: each cell has a distribution over terminal states, not a hard lineage label.
- **Differentiation potential (DP)**: entropy over a cell's branch probabilities → quantitative plasticity metric.
- **Diffusion-map manifold + waypoint-refined pseudotime**: multi-component diffusion maps capture multiple fates; pseudotime is refined iteratively using waypoint cells that span the landscape.
- **Absorbing Markov chain**: terminal states identified as stationary-distribution outliers; fate probabilities computed over absorbing random walks.
- **Human CD34+ hematopoiesis application**: ~25K cells from 3 donors; recovers monocyte/erythroid/megakaryocyte/lymphoid/cDC/pDC terminals; identifies fate-commitment transitions and key TFs.

## 3. Methods & Architecture

1. **Phenotypic manifold**: kNN on scRNA-seq PCA, then diffusion maps (multiple components) to denoise and focus on developmental directions.
2. **Pseudotime**: shortest paths from a user-provided early cell, iteratively refined using waypoints that span the landscape.
3. **Directed graph**: edges oriented by pseudotime.
4. **Terminal states**: boundary cells that are outliers of the stationary distribution of a random walk.
5. **Fate probabilities**: convert terminal states to absorbing states → for each cell, integrate all random walks → vector of branch probabilities.
6. **DP (differentiation potential)**: entropy over the branch-probability vector. High DP = plastic, low DP = committed.
7. **Gene trends**: generalized additive models weighted by branch probabilities → smooth lineage-specific gene expression curves.

## 4. Key Results & Benchmarks

- Recapitulates canonical hematopoiesis markers (CD34 decline, CD79A/GATA1/IRF8 lineage upregulation).
- Identifies transitions where DP drops sharply = fate-commitment landmarks.
- Robust to parameter choices (k, number of diffusion components, waypoint sampling) across three donor replicates.
- Generalizes to mouse ESC differentiation and T cell development in the original paper.
- Became the default pseudotime backbone for CellRank 2022 and many follow-up methods.

## 5. Limitations & Future Work

- Requires user-specified early cell — fails for systems without a canonical root.
- Unidirectional progression assumed; not valid in cancer or reprogramming.
- Markov assumption (memoryless) is a first-order approximation; true cell history (epigenetic memory) is not modeled.
- No directionality from molecular signals (velocity, metabolic labeling) — later addressed by CellRank.

## 6. Related Work

- Monocle, Wanderlust, diffusion pseudotime — earlier pseudotime methods.
- PAGA, Slingshot — alternative trajectory methods.
- Extended by CellRank (Lange 2022) with RNA velocity.

## 7. Glossary

- **Diffusion map**: a manifold-learning technique using the spectrum of a diffusion operator on a neighbor graph.
- **Pseudo-time**: a scalar ordering of cells along a developmental progression, not physical time.
- **Differentiation potential (DP)**: entropy of a cell's fate probability distribution.
- **Waypoint**: a reference cell used to refine pseudotime by providing alternative shortest-path anchors.
- **Absorbing state**: in a Markov chain, a state that cannot be left once entered.
