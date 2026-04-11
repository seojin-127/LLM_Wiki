---
title: "Predicting and interpreting cell-type-specific drug responses in the small-data regime using inductive priors"
authors: Reem Alsulami, Robert Lehmann, Sumeer A. Khan, Vincenzo Lagani, Alberto Maillo, David Gomez-Cabrero, Narsis A. Kiani, Jesper Tegner
year: 2026
doi: 10.1038/s42256-026-01202-2
source: alsulami-2026-predicting-and-interpreting-cell.md
category: drug-resistance
tags: [drug-response, perturbation-prediction, GNN, graph-attention, inductive-prior, cell-type-specificity, interpretability, small-data]
---

## Summary

PrePR-CT predicts how a previously unseen cell type will respond transcriptionally to a chemical perturbation, using cell-type-specific co-expression graphs as an inductive prior. A graph attention network learns per-cell-type features from those graphs, which are concatenated with SMILES-derived drug embeddings and control expression and passed through an MLP regression head. The inductive bias is the key design move: it lets PrePR-CT generalize to unseen cell types where generative baselines (scGen, CPA, chemCPA) fail in the small-data regime.

## Key Contributions

- Cell-type-specific co-expression graphs → cell-type feature vectors → conditioned perturbation prediction. Different cell types use *different* graphs, which is what enables generalization.
- Beats scGen, CPA, chemCPA on unseen-cell-type and unseen-perturbation benchmarks.
- Attention-value attribution for each gene → interpretable beyond DEG lists, pointing to pathway mechanisms.
- Scales to 144-perturbation NeurIPS small-molecule dataset while remaining cell-type-specific.

## Methods & Architecture

1. Build cell-type-specific co-expression networks from training data (per cell type: gene-gene graph).
2. GAT layers process each graph → node-level features.
3. Max-pool across nodes → single feature vector per cell type.
4. Concatenate with SMILES-derived perturbation embedding and basal control expression.
5. MLP regression head → post-perturbation mean + variance for each gene.
6. Training: matched control/perturbed samples via SEACells metacells (paired measurements are not feasible in scRNA-seq).
7. Evaluation: leave-one-out cross-validation across cell types (OOD test).

## Results

- **Kang PBMC IFNβ**: R² > 0.90 mean, > 0.70 variance; R² = 0.99 for upregulated DEGs in B cells. Outperforms scGen and CPA with more stable cross-cell-type R².
- **NeurIPS PBMC 144 small molecules × 4 immune types**: highest R² among baselines on top-100 DEGs; especially strong on strong-perturbation compounds.
- **McFarland, Chang cancer cell lines**: OOD cell-type generalization beats chemCPA.
- **Mouse liver (Nault) 11 cell types**: generalizes across diverse tissue cell types.
- **Attribution**: high-attention genes add mechanism-level information not captured by DEG analysis.

## Limitations

- Co-expression networks are correlational, not causal — "inductive prior" here is a soft bias, not a mechanism.
- Requires some labeled perturbation data for training; not zero-shot.
- Cell-type graph quality depends on training sample size per cell type.
- No explicit perturbation time dynamics.

## Related Papers

- [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] — Squidiff, diffusion alternative
- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle, causal mechanism alternative (GRN-based)
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT, foundation-model alternative
- [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]] — PerturBERT perturbation embeddings
- [[drug-resistance/antonopoulos-2026-zero-shot-prediction-of-drug]] — LEMBAS zero-shot drug response, different paradigm
- [[drug-resistance/chen-2022-deep-transfer-learning-of]] — scDEAL, bulk-to-single-cell transfer learning alternative
