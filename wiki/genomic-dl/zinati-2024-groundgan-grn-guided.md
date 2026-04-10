---
title: "GRouNdGAN: GRN-guided simulation of single-cell RNA-seq data using causal generative adversarial networks"
authors: Yazdan Zinati, Abdulrahman Takiddeen, Amin Emad
year: 2024
doi: 10.1038/s41467-024-48516-6
source: zinati-2024-groundgan-grn-guided.md
category: genomic-dl
tags: [GRN, GAN, simulation, scRNA-seq, TF, benchmark, causal, in-silico-perturbation]
---

## Summary
GRouNdGAN is a causal GAN where user-specified GRNs are imposed in the model architecture, simulating scRNA-seq data where genes are causally regulated by TFs. Trained on 6 real datasets, it preserves cell trajectories, pseudotime, and noise while enabling in silico TF knockouts. Provides ground-truth GRNs for benchmarking GRN inference algorithms.

## Key Contributions
- GRN-guided causal simulation: user GRN → realistic scRNA-seq data
- Non-linear TF-gene dependencies preserved; cell trajectories and pseudotime maintained
- In silico TF KO experiments
- GRN inference benchmarking with realistic ground truth (bridges simulated-to-biological gap)

## Methods & Architecture
- Causal GAN with GRN imposed in architecture; steady-state + transient simulation
- Trained on 6 experimental scRNA-seq datasets; benchmarked multiple GRN inference methods

## Results
- Simulated data: realistic cell trajectories, pseudotime, noise vs. 6 real datasets
- GRN benchmark: more realistic than curated database benchmarks
- In silico KO: correctly predicts downstream effects

## Limitations
- User must specify GRN (no de novo GRN learning from data)
- GAN instability; 6 training datasets

## Related Papers
- [[genomic-dl/zemke-2023-conserved-and-divergent-gene]] — CRE prediction (related regulatory genomics ML)
- [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna]] — RNA velocity/GRN inference (complementary)
