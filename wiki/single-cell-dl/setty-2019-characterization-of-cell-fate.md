---
title: "Characterization of cell fate probabilities in single-cell data with Palantir"
authors: Manu Setty, Vaidotas Kiseliovas, Jacob Levine, Adam Gayoso, Linas Mazutis, Dana Pe'er
year: 2019
doi: 10.1038/s41587-019-0068-4
source: setty-2019-characterization-of-cell-fate.md
category: single-cell-dl
tags: [trajectory, pseudotime, fate-probability, diffusion-map, Markov-chain, hematopoiesis, differentiation-potential]
---

## Summary

Palantir models differentiation as a probabilistic Markov walk on a diffusion-map manifold. Instead of assigning each cell to one lineage, it gives each cell a **distribution** over terminal fates and a **pseudotime** from a user-defined early cell. The entropy over fate probabilities — **differentiation potential (DP)** — quantifies how plastic a cell is. Applied to human CD34+ bone marrow, it shows hematopoiesis is a continuous fate-choice process with plasticity declining gradually, not a series of discrete branch points.

## Key Contributions

- Broke the "discrete bifurcation" framing of differentiation: cells have *probabilities*, not hard lineage labels.
- **Differentiation potential** as a single-number plasticity metric enabled quantitative comparison of commitment across states.
- Multi-component diffusion-map pseudotime handles multi-fate systems that single-axis methods collapse.
- Waypoint-refined shortest-path pseudotime became a widely reused primitive (including as CellRank's default pseudotime backend).

## Methods & Architecture

1. **Diffusion-map manifold** from scRNA-seq kNN graph — multiple components preserve multiple fates.
2. **Pseudotime** from user-defined early cell via iteratively waypoint-refined shortest paths.
3. **Terminal state identification**: boundary cells that are outliers in the stationary distribution of a random walk on the pseudotime-directed graph.
4. **Absorbing Markov chain**: terminal cells become absorbing. For every cell, integrate absorbing probabilities → vector of branch probabilities.
5. **DP = entropy of branch probabilities**. High DP → uncommitted. Low DP → committed.
6. **Gene trends**: generalized additive models weighted by branch probabilities, so each lineage's gene curves are computed with soft cell assignment.

## Results

- Human CD34+ hematopoiesis (25K cells, 3 donors): recovers monocyte, erythroid, megakaryocyte, lymphoid, cDC, pDC terminal states.
- Canonical markers reproduced: CD34 decline across all lineages, CD79A/GATA1/IRF8 upregulated in lymphoid/erythroid/dendritic.
- DP drops sharply at fate-commitment transitions — these drops are the "landmarks" of hematopoiesis.
- Robust to parameter choices (neighbors k, diffusion components, waypoints) and reproducible across donors.

## Limitations

- Requires user-specified early cell — does not work for systems without a canonical root.
- Assumes unidirectional progression; fails in cancer, regeneration, reprogramming (CellRank solves this).
- Memoryless Markov assumption ignores epigenetic cell history.
- No molecular directional signal — later extended by CellRank using RNA velocity.

## Related Papers

- [[single-cell-dl/lange-2022-cellrank-for-directed-single]] — CellRank, direct extension adding RNA velocity
- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle, perturbation on top of trajectory
- [[single-cell-dl/klein-2025-mapping-cells-through-time]] — moscot, optimal transport as an alternative to Markov chains
- [[brain-development/fleck-2023-inferring-perturbing-cell-fate]] — trajectory + perturbation in brain organoids
