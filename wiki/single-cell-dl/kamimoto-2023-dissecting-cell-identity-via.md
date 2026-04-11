---
title: "Dissecting cell identity via network inference and in silico gene perturbation"
authors: Kenji Kamimoto, Blerta Stringa, Christy M. Hoffmann, Kunal Jindal, Lilianna Solnica-Krezel, Samantha A. Morris
year: 2023
doi: 10.1038/s41586-022-05688-9
source: kamimoto-2023-dissecting-cell-identity-via.md
category: single-cell-dl
tags: [GRN, in-silico-perturbation, CellOracle, causal-inference, TF-knockout, multi-omics, scATAC, haematopoiesis, zebrafish]
---

## Summary

CellOracle builds cluster-specific gene regulatory networks from scRNA-seq + scATAC-seq and uses them as causal models to simulate transcription factor knockouts. Starting from unperturbed wild-type data, it propagates a TF perturbation through a regularized linear GRN, converts the downstream expression shift into a cell-state transition vector, and projects that onto the existing trajectory embedding. The prediction is a direction of fate change, not absolute new expression values — a deliberate choice to stay robust to noise.

## Key Contributions

- First widely used method to treat a GRN as an *operator* for in silico perturbation rather than a descriptive network.
- Directional edges come from motif scans on open chromatin (scATAC) rather than from expression alone, bypassing the causal-direction problem that plagues pure co-expression GRN inference.
- Benchmarked against 1,298 ChIP-seq datasets (AUROC 0.66-0.91 depending on base GRN source).
- Validated by recapitulating canonical haematopoiesis TF logic (Spi1-Gata1 lineage switch) and by predicting-then-validating a novel noto KO phenotype in zebrafish axial mesoderm.

## Methods & Architecture

**Why a linear GRN at all?** Because CellOracle needs the GRN to function as a propagation operator. A regularized linear model lets a TF perturbation be applied as a matrix multiply that iteratively updates downstream expression. Per-cluster fitting means each linear fit only needs to approximate local, cell-state-specific regulation.

**Pipeline**:
1. **Base GRN** from scATAC: Cicero identifies co-accessible peaks → TF motif scan → directed skeleton of all plausible TF → target edges in that species.
2. **Cluster-specific refinement** from scRNA: regularized linear regression (with Bayesian / bagging certainty) fits which skeleton edges are active in each cell cluster.
3. **Perturbation simulation**: apply TF KO or overexpression → propagate through GRN iteratively → downstream gene expression shift.
4. **Cell-state transition**: compare shifted expression vector to each cell's k-nearest neighbors → assign transition probabilities → aggregate to a 2D vector field on the trajectory embedding.

**Important conceptual point**: CellOracle deliberately does *not* predict absolute post-perturbation expression. It predicts the direction of cell-state movement. This reframes perturbation prediction as a question about trajectories on the manifold, not about new gene expression values.

## Results

- **Haematopoiesis (mouse + human)**: Spi1 KO vector field shows GM lineage inhibition and MEP promotion; Gata1 KO shows the reverse. Systematic KO of 90 TFs in GM/ME lineages recovers both canonical regulators (Spi1, Gata1, Klf1, Cebpa) and identifies novel candidates at FPR 0.01.
- **Zebrafish embryogenesis**: identified noto KO as producing a prechordal-plate-like shift in notochord cells — a previously unreported phenotype — and validated by morpholino + scRNA-seq.
- **lhx1a**: identified as an axial mesoderm regulator through the in silico screen, then validated.

## Limitations

- Local linear model cannot capture strongly nonlinear regulation.
- Assumes the current phenotypic manifold is relevant to the perturbed state — fails if perturbation moves cells into a region unseen in training.
- Only TF perturbations; no cofactors, enhancers, or small molecules.
- Motif-based directionality cannot disentangle TFs sharing motifs.
- Requires scATAC for best-quality base GRN; species without scATAC atlases fall back to weaker promoter-only base.

## Related Papers

- [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] — scVI, latent representation approach without explicit causal model
- [[brain-development/fleck-2023-inferring-perturbing-cell-fate]] — applies CellOracle-style in silico perturbation to human brain organoid regulomes
- [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction]] — GRN reconstruction from paired scRNA+scATAC in brain development
- [[brain-development/ding-2026-dissecting-gene-regulatory-networks]] — GRNs governing human cortical fate
- [[neuroscience/jin-2020-in-vivo-perturb-seq]] — experimental Perturb-seq counterpart in brain
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — foundation-model alternative for perturbation prediction
- [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]] — BERT-style perturbation signatures
