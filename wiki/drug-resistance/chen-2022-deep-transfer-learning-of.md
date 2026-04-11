---
title: "Deep transfer learning of cancer drug responses by integrating bulk and single-cell RNA-seq data"
authors: Junyi Chen, Xiaoying Wang, Anjun Ma, Qi-En Wang, Bingqiang Liu, Lang Li, Dong Xu, Qin Ma
year: 2022
doi: 10.1038/s41467-022-34277-7
source: chen-2022-deep-transfer-learning-of.md
category: drug-resistance
tags: [drug-response, transfer-learning, domain-adaptation, bulk-to-single-cell, cancer, integrated-gradients, scDEAL]
---

## Summary

scDEAL bridges the data-scarcity gap in single-cell drug-response prediction by transferring from bulk cancer cell-line screens (GDSC, CCLE) where labels are abundant. Two denoising autoencoders — one for bulk, one for single-cell — feed into a shared feature space aligned by Maximum Mean Discrepancy loss; a bulk-trained response predictor is then applied to the aligned single-cell features. Cell-cluster regularization keeps single-cell heterogeneity from being averaged out by the domain adaptation.

## Key Contributions

- Domain-adaptation strategy for single-cell drug response: exploit large bulk drug-response databases without requiring single-cell labels.
- Cell cluster regularization specifically protects scRNA-seq heterogeneity during transfer — a known failure mode of naive domain alignment.
- Integrated gradient attribution identifies per-cell signature genes driving predictions.
- Benchmarked across six scRNA-seq datasets × five drugs with average F1 = 0.89.

## Methods & Architecture

1. **Bulk path**: DAE encoder E_b learns low-dim features; predictor P maps features to sensitive/resistant labels from GDSC/CCLE.
2. **Single-cell path**: separate DAE encoder E_s on scRNA-seq.
3. **Domain adaptation**: MMD loss between E_b and E_s outputs forces a shared distribution in latent space.
4. **Cluster regularization**: cell clustering penalizes loss so that clusters do not collapse.
5. **Joint training**: all four networks (E_b, D_b, E_s, D_s) + P updated together via multi-task loss (reconstruction + bulk prediction + MMD + cluster).
6. **Transfer**: final predictor applied to single-cell features → per-cell drug response probability.
7. **Attribution**: integrated gradients along a baseline path identify signature genes.

## Results

- Average across 6 scRNA-seq benchmarks: F1 0.892, AUROC 0.898, AP 0.944, precision 0.926, recall 0.899.
- Prediction UMAPs separate sensitive from resistant cells in the expected ways.
- Integrated-gradient gene signatures recover known drug-resistance markers.
- Predicted response probability tracks expression trajectory of treatment.

## Limitations

- Requires the drug to be present in GDSC/CCLE bulk screens — no support for novel compounds.
- Binary labels lose dose-response information.
- MMD alignment is aggressive; cluster regularization is the only safeguard for heterogeneity.
- No explicit cell-type-specific mechanism — cell types are only preserved through clustering.
- Inherits cell-line biology from GDSC/CCLE, which may not transfer to patient-derived cells.

## Related Papers

- [[drug-resistance/alsulami-2026-predicting-and-interpreting-cell]] — PrePR-CT, cell-type-specific graph-prior alternative
- [[drug-resistance/antonopoulos-2026-zero-shot-prediction-of-drug]] — LEMBAS zero-shot drug response, different paradigm
- [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] — Squidiff, diffusion-based alternative for perturbation prediction
- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle, mechanistic GRN-based alternative
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT foundation-model alternative
