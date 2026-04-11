---
title: "Predicting and interpreting cell-type-specific drug responses in the small-data regime using inductive priors"
authors: Reem Alsulami, Robert Lehmann, Sumeer A. Khan, Vincenzo Lagani, Alberto Maillo, David Gomez-Cabrero, Narsis A. Kiani, Jesper Tegner
year: 2026
doi: 10.1038/s42256-026-01202-2
category: drug-resistance
pdf_path: papers/alsulami-2026-predicting-and-interpreting-cell.pdf
pdf_filename: alsulami-2026-predicting-and-interpreting-cell.pdf
source_collection: downloads-perturb-batch
---

## One-line Summary

PrePR-CT predicts cell-type-specific transcriptional responses to chemical perturbations by injecting cell-type-specific co-expression graphs as an inductive prior into a graph attention network — outperforming scGen, CPA, chemCPA on unseen-cell-type generalization in the small-data regime.

## 1. Document Info
- Journal: Nature Machine Intelligence, Vol 8, March 2026, 461-473
- Published online: 16 March 2026

## 2. Key Contributions

- **Cell-type-specific co-expression graphs as inductive bias**: a GAT processes each cell type's graph to produce a cell-type embedding before perturbation prediction.
- Generalizes to unseen cell types and unseen perturbations — the central weakness of scGen, CPA, chemCPA.
- Chemical structure embeddings from SMILES fed jointly with cell-type embeddings.
- Attention-value attribution reveals high-attention genes that complement traditional DEG analyses with mechanism-specific interpretations.
- Benchmarked on 5 scRNA-seq datasets + 1 bulk + 1 large-scale chemical screen.

## 3. Methods & Architecture

1. Construct cell-type-specific co-expression graphs from the training samples (cells × genes).
2. Graph attention network (GAT) layers learn per-cell-type features on the graph.
3. Max pooling across nodes → cell-type feature vector.
4. Concatenate with perturbation embedding (SMILES-derived) and control gene expression.
5. MLP regression predicts post-perturbation expression (mean + variance).
6. Leave-one-out cross validation across cell types for OOD evaluation.
7. Metacells (SEACells) used to pair control and perturbed cells without true paired measurement.

## 4. Key Results & Benchmarks

- Kang PBMC IFNβ: R² > 0.90 mean, > 0.70 variance; top-100 DEGs even higher. Beats scGen and CPA.
- NeurIPS PBMC 144 small molecules × 4 immune cell types: consistently highest R² among top-100 DEGs.
- McFarland, Chang cancer cell lines: outperforms baselines especially for OOD cell types.
- Mouse liver 11 cell types (Nault): generalizes across diverse tissue cell types.
- Attribution: high-attention genes overlap but also complement DEG lists, pointing to pathway-specific mechanisms.

## 5. Limitations & Future Work

- Graph construction is from training data — quality depends on the reference co-expression networks.
- Still requires some labeled perturbation data; not fully zero-shot.
- Co-expression graphs are not causal; inductive bias ≠ mechanism.
- Scaling to thousands of perturbations is untested.

## 6. Related Work

- scGen (Lotfollahi 2019), CPA (Lotfollahi 2023), chemCPA (Hetzel 2022), GEARS (Roohani 2024), GenePert — baseline perturbation prediction methods.
- SCimilarity, scGPT — foundation-model alternatives.

## 7. Glossary

- **GAT**: Graph Attention Network, a GNN variant that learns per-edge attention weights.
- **Inductive prior**: a model architecture choice that biases the learner toward a class of hypotheses, reducing data demand.
- **SEACells**: metacell construction method for single-cell data.
- **OOD generalization**: performance on distributions not seen during training (new cell types, new perturbations).
