---
title: "CellRank for directed single-cell fate mapping"
authors: Marius Lange, Volker Bergen, Michal Klein, Manu Setty, Bernhard Reuter, Mostafa Bakhti, Heiko Lickert, Meshal Ansari, Janine Schniering, Herbert B. Schiller, Dana Pe'er, Fabian J. Theis
year: 2022
doi: 10.1038/s41592-021-01346-6
category: single-cell-dl
pdf_path: papers/lange-2022-cellrank-for-directed-single.pdf
pdf_filename: lange-2022-cellrank-for-directed-single.pdf
source_collection: downloads-perturb-batch
---

## One-line Summary

CellRank models single-cell fate decisions as a directed Markov chain on the phenotypic manifold, combining similarity-based pseudotime with RNA velocity (or any directional signal) to infer initial/terminal/intermediate states and assign every cell a probabilistic fate vector — without requiring a known lineage hierarchy.

## 1. Document Info
- Journal: Nature Methods, Vol 19, Feb 2022, 159-170
- Code: https://cellrank.org

## 2. Key Contributions

- **Directed Markov chain on the manifold**: fuses kNN-graph similarity with RNA velocity to produce a directed transition matrix, avoiding the need to manually specify an initial cell.
- **Automatic state identification**: uses GPCCA (Generalized Perron Cluster Cluster Analysis) to decompose dynamics into macrostates and classify them as initial, terminal, or intermediate via stability index and coarse-grained stationary distribution.
- **Fate probabilities for every cell**: probability of reaching each terminal state, computed as the solution of a linear system on the absorbing Markov chain.
- **Uncertainty-aware velocity**: propagates scVelo's velocity uncertainty into transition probabilities, so noisy velocity vectors do not catastrophically break downstream inference.
- **Beyond normal development**: works on reprogramming and regeneration where directionality is not given by canonical hierarchies; validated on lineage-traced mouse reprogramming and on post-injury lung regeneration (predicts + validates new dedifferentiation trajectory).

## 3. Methods & Architecture

1. **Graph**: undirected kNN on scRNA-seq PCA.
2. **Directionality**: weight each outgoing edge by alignment with RNA velocity vector (Monte Carlo or analytical approximation to propagate velocity uncertainty).
3. **Transition matrix**: weighted mean of similarity-based and velocity-based transition probabilities.
4. **Macrostates**: GPCCA decomposes dynamics into metastable regions; soft assignment of cells.
5. **State classification**: SI ≥ 0.96 → terminal; low coarse-grained stationary mass → initial.
6. **Fate probabilities**: absorbing Markov chain → linear system → per-cell branch probability vector.
7. **Lineage driver genes**: correlate gene expression with fate probability; visualize gene cascades along lineages using pseudotime as the ordering axis.

## 4. Key Results & Benchmarks

- Pancreatic endocrine development (E15.5 mouse): automatically identifies alpha/beta/delta/epsilon terminal states + Ngn3-low/high progenitor initial state; recovers known lineage drivers and predicts somatostatin lineage drivers.
- Lineage-traced cellular reprogramming: predicted fate bias matches ground-truth clonal outcomes.
- Post-injury lung regeneration: predicts a new dedifferentiation trajectory with novel intermediate states, validated experimentally.
- Outperforms methods without velocity (Palantir, STEMNET) on initial/terminal state identification when dynamics are not monotonic.

## 5. Limitations & Future Work

- Quality of output inherits from velocity quality — poorly estimated velocities propagate noise.
- GPCCA macrostate number is a tunable parameter; automatic selection is heuristic.
- RNA-velocity framework assumes standard splicing kinetics that fail in some cell types (neurons, low-transcription states).
- Fate probabilities are long-range but assume the manifold is stationary during the measured process.

## 6. Related Work

- scVelo (Bergen 2020), velocyto (La Manno 2018) — velocity upstream of CellRank.
- Palantir (Setty 2019) — earlier approach without velocity.
- PAGA, Slingshot, Monocle — alternative trajectory methods benchmarked against.

## 7. Glossary

- **Macrostate**: a metastable cluster of cell states that cells are unlikely to leave on short timescales.
- **GPCCA**: Generalized Perron Cluster Cluster Analysis, a method for decomposing near-decomposable Markov chains.
- **Stability index**: self-transition probability of a macrostate; high → terminal.
- **Fate probability**: probability that a random walk starting from a given cell is absorbed in each terminal macrostate.
- **Absorbing Markov chain**: Markov chain with states that, once entered, cannot be left.
