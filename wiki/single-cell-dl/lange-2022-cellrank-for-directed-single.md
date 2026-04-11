---
title: "CellRank for directed single-cell fate mapping"
authors: Marius Lange, Volker Bergen, Michal Klein, Manu Setty, Bernhard Reuter, Mostafa Bakhti, Heiko Lickert, Meshal Ansari, Janine Schniering, Herbert B. Schiller, Dana Pe'er, Fabian J. Theis
year: 2022
doi: 10.1038/s41592-021-01346-6
source: lange-2022-cellrank-for-directed-single.md
category: single-cell-dl
tags: [trajectory, RNA-velocity, fate-probability, Markov-chain, GPCCA, regeneration, reprogramming]
---

## Summary

CellRank asks: "given a snapshot of cells, what is the probability that each cell becomes each terminal state?" It builds a directed Markov chain on the phenotypic manifold — nodes are cells, edges are similarity-weighted kNN, and directionality comes from RNA velocity (or any other vector field). GPCCA decomposes this chain into macrostates, which are then automatically labeled initial / terminal / intermediate. Fate probabilities for every cell are then a linear-system solve over an absorbing Markov chain.

## Key Contributions

- First trajectory method that **automatically** identifies initial and terminal states without a user-defined root — opens fate inference to regeneration, reprogramming, and disease, where canonical hierarchies do not exist.
- Velocity is treated as one of several possible direction sources; the framework generalizes to metabolic labeling, lineage tracing, or real-time annotation.
- Propagates velocity uncertainty into transition probabilities, so noisy per-cell velocities do not destroy downstream inference.
- Fate probabilities are global and probabilistic, not local arrows — they describe long-range lineage bias that local velocity vectors cannot.

## Methods & Architecture

1. **Similarity graph**: undirected kNN on scRNA-seq PCA.
2. **Directed transition matrix**: for each edge, weight by alignment with the source cell's RNA velocity vector. Velocity uncertainty (from scVelo) is propagated analytically or via Monte Carlo. A similarity-only transition matrix is also computed and blended with the velocity-directed one.
3. **Macrostates via GPCCA**: metastable regions where cells linger. Soft assignment of cells to macrostates.
4. **Automatic state classification**: stability index (self-transition) ≥ 0.96 → terminal; low mass in coarse-grained stationary distribution → initial.
5. **Absorbing Markov chain**: terminal states become absorbing; solve a linear system to get per-cell fate probabilities.
6. **Lineage drivers**: correlate gene expression with fate probability; visualize gene cascades along pseudotime with Palantir as the default pseudotime backend.

## Results

- **Mouse pancreas E15.5**: identifies alpha/beta/delta/epsilon terminals + Ngn3 progenitor initial state without user input; recovers known drivers (Pdx1, Nkx6-1) and identifies putative delta-cell drivers.
- **Lineage-traced reprogramming (Biddy 2018)**: predicted fate bias matches clonal ground truth.
- **Lung regeneration after bleomycin injury**: predicts a new dedifferentiation trajectory with novel intermediate states; experimentally validated.
- Outperforms Palantir, STEMNET and velocity-only projections on initial/terminal identification when dynamics are non-monotonic or multi-root.

## Limitations

- Output quality inherits from RNA velocity quality; fails when splicing kinetics are atypical (neurons, quiescent states).
- GPCCA macrostate count is semi-automatic (knee-point) and can be sensitive.
- Assumes the measured snapshot covers the manifold — does not extrapolate to unsampled states.
- Does not model perturbations directly — it describes what *is* happening, not what *would* happen under intervention.

## Related Papers

- [[single-cell-dl/setty-2019-characterization-of-cell-fate]] — Palantir, CellRank's predecessor; still used as the pseudotime backend
- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle, in silico perturbation on the same kind of trajectory
- [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna]] — cell2fate, RNA velocity refinement
- [[brain-development/fleck-2023-inferring-perturbing-cell-fate]] — trajectory + perturbation in brain organoids
- [[single-cell-dl/klein-2025-mapping-cells-through-time]] — moscot, optimal-transport approach to trajectories
