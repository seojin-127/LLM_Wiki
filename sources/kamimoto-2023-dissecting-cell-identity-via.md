---
title: "Dissecting cell identity via network inference and in silico gene perturbation"
authors: Kenji Kamimoto, Blerta Stringa, Christy M. Hoffmann, Kunal Jindal, Lilianna Solnica-Krezel, Samantha A. Morris
year: 2023
doi: 10.1038/s41586-022-05688-9
category: single-cell-dl
pdf_path: papers/kamimoto-2023-dissecting-cell-identity-via.pdf
pdf_filename: kamimoto-2023-dissecting-cell-identity-via.pdf
source_collection: downloads-perturb-batch
---

## One-line Summary

CellOracle infers cell-state-specific gene regulatory networks from scRNA-seq + scATAC-seq and uses them as causal models to simulate in silico TF knockouts, predicting and experimentally validating cell-fate shifts without requiring perturbation training data.

## 1. Document Info
- Journal: Nature
- Published: 23 February 2023 (Vol 614, pp. 742-751)
- Code: https://github.com/morris-lab/CellOracle
- Data explorer: https://celloracle.org

## 2. Key Contributions

- **CellOracle framework**: a computational method that combines custom cluster-specific GRN inference with signal propagation to simulate transcription factor perturbations in silico, using only unperturbed wild-type data.
- **Directed GRN inference**: uses scATAC-seq base GRN (promoter/enhancer + TF motif scan) to fix edge directionality, then fits cluster-wise regularized linear regression on scRNA-seq to prune active connections. Benchmarked AUROC 0.66-0.91 against ChIP-seq ground truth.
- **Validation in haematopoiesis**: recovers known TF regulation of mouse/human myeloid fate (Spi1, Gata1, Klf1, Cebpa) and identifies late-GMP to granulocyte transition as Gata1-sensitive.
- **Novel prediction in zebrafish**: systematic KO simulation across development identifies noto loss producing a prechordal plate phenotype and lhx1a as an axial mesoderm regulator, both experimentally validated.

## 3. Methods & Architecture

**Four-step simulation**:
1. Construct cell-state-specific GRN from multi-omics (scATAC defines base, scRNA fits weights).
2. Propagate TF perturbation through GRN via iterative signal flow → global shift in gene expression (not absolute levels).
3. Compare shifted expression to local neighbors → cell-state transition probability.
4. Convert to 2D weighted local average vector → simulated direction of fate change.

**Key design choices**:
- GRN edges are directional by construction (from motif scan), allowing signal propagation without learning causality from expression.
- Per-cluster linear models keep fitting tractable and avoid nonlinear confounds.
- Bagging / Bayesian regularization gives per-edge certainty; weak edges pruned.
- Output deliberately reduced to 2D transition vector (not absolute expression) to resist noise.

**Base GRNs**: prebuilt for 10 species from promoter scans; optional upgrade to scATAC-derived base when sample-specific ATAC is available.

## 4. Key Results & Benchmarks

- GRN inference AUROC: 0.66-0.85 (promoter base), 0.73-0.91 (scATAC base) against ChIP-seq ground truth across 80 factors × 5 tissues.
- Haematopoiesis: Spi1 KO → inhibited GM lineage differentiation + promoted MEP; Gata1 KO → reverse. Recapitulates Spi1-Gata1 lineage switch.
- Systematic KO of 90 TFs in GM/ME lineages identifies both canonical regulators and flags novel candidates at FPR = 0.01.
- Zebrafish axial mesoderm: noto KO predicted to shift notochord cells to prechordal plate identity; validated by morpholino + scRNA-seq showing the predicted transition in vivo.
- lhx1a identified as an axial mesoderm regulator through in silico screen, then validated experimentally.

## 5. Limitations & Future Work

- Per-cluster linear model cannot capture strongly nonlinear TF-target relationships.
- Signal propagation assumes stationarity around the current state; large perturbations that move cells across phenotypic basins may be extrapolated beyond model validity.
- TF-only perturbations; does not model cofactor or chromatin-level interventions.
- Requires scATAC for best performance; species without scATAC atlases use weaker promoter base.
- GRN directionality is motif-based, so co-binding TFs with shared motifs are not disentangled.

## 6. Related Work

- scVI family for integration but not causal intervention.
- SCENIC, Pando, GRNBoost2 — GRN inference methods that CellOracle benchmarks against.
- Perturb-seq (Dixit 2016, Replogle 2022) — experimental counterpart that CellOracle aims to simulate without new data.
- Fleck et al. 2023 (organoid regulome perturbation) — applies a related approach in brain organoids.

## 7. Glossary

- **GRN (gene regulatory network)**: directed graph of TF → target gene regulatory relationships.
- **Base GRN**: skeleton of potential connections from motif scanning / open chromatin; filtered per cell state by expression data.
- **Signal propagation**: iterative application of GRN as a linear operator to propagate a local TF perturbation to downstream genes.
- **Perturbation score (PS)**: summarizes how strongly a perturbation moves cells away from their current state along a given direction.
- **In silico perturbation**: simulating gene knockout using a model, without wet-lab perturbation.
