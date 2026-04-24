---
title: "PerturbNet predicts single-cell responses to unseen chemical and genetic perturbations"
authors: Hengshi Yu, Weizhou Qian, Yuxuan Song, Joshua D Welch
year: 2025
doi: 10.1038/s44320-025-00131-3
source: yu-2025-perturbnet-predicts-single-cell-responses.md
category: single-cell-dl
tags: [perturbation-prediction, normalizing-flow, cINN, chemical-perturbation, genetic-perturbation, missense-mutation, ESM, distributional-prediction, GATA1]
---

## Summary

PerturbNet is a modular deep generative framework that predicts the **full distribution** of single-cell gene expression states induced by unseen perturbations. Unlike prior methods that predict only mean expression changes, PerturbNet uses a conditional invertible neural network (cINN) to model the entire cell-state distribution p(X|G). Its modular design supports three perturbation types — small molecules (via ChemicalVAE), genetic perturbations (via GenotypeVAE with GO annotations), and coding-sequence mutations (via ESM protein embeddings) — making it the first method to predict transcriptional effects of missense mutations.

## Key Contributions

- **Distributional prediction**: models full p(X|G) via normalizing flow, not just mean shift — captures cell-state heterogeneity (e.g., subpopulation-specific responses)
- **Three perturbation modalities** in one framework: chemical (ChemicalVAE), genetic (GenotypeVAE), coding-sequence (ESM)
- **First missense mutation prediction**: uses pretrained ESM protein embeddings to predict how amino acid changes affect cell states
- **Outperforms GEARS** on Norman et al. CRISPRa dataset, especially for completely unseen genes
- **GATA1 variant scanning**: predicted all 7,847 point mutations → identified DNA-contact-region variants as highest-impact

## Methods & Architecture

### Modular Three-Network Design

```
Perturbation          Mapping           Cell State
Representation  →    Network    →     Representation
Network              (cINN)            Network

Chemical: ChemicalVAE (250K ZINC molecules)
Genetic:  GenotypeVAE (177M GO annotation vectors)
Variant:  ESM (250M protein sequences, pretrained)
                        ↓
              Conditional Normalizing Flow
              p(z_cell | z_perturbation, covariates)
                        ↓
              Cell VAE Decoder → gene expression
```

### Why cINN (Conditional Invertible Neural Network)?
- Normalizing flows transform Gaussian noise → complex cell-state distributions through invertible layers
- Conditioning on perturbation embedding → different perturbations produce different distributions
- Invertible by construction → stable training, no mode collapse
- Can incorporate covariates (dose, cell type) directly

### GEARS vs PerturbNet: Architectural Comparison

| Feature | GEARS | PerturbNet |
|---------|-------|------------|
| Output | Mean expression change | Full distribution p(X\|G) |
| Perturbation encoding | GNN on GO + coexpression graphs | Modular: ChemicalVAE / GenotypeVAE / ESM |
| Perturbation types | Genetic only (CRISPRa/KO) | Chemical + genetic + coding variants |
| Knowledge graph | Gene coexpression + GO (dual GNN) | GO annotations (GenotypeVAE) |
| Combinatorial | Yes (composition operator) | Yes (union of GO annotations) |
| Unseen genes | Via GO graph connectivity | Via GO annotation similarity |
| Missense mutations | Not supported | ESM protein embeddings |
| Cell-state heterogeneity | Not modeled | Modeled via cINN |
| Raw count support | No (normalized only) | Yes (ZINB likelihood option) |

## Results

### Head-to-head vs GEARS (Norman et al. CRISPRa, K562)

| Metric | GEARS | PerturbNet |
|--------|-------|------------|
| Median R² (all genes) | 0.858 | **0.942** |
| Mean R² (all genes) | 0.853 | **0.928** |
| Median R² (top 50 DEGs) | 0.513 | **0.629** |
| Mean R² (top 50 DEGs) | 0.451 | **0.535** |

- PerturbNet advantage largest for **both-unseen gene** combinations
- Better at non-additive interactions (neomorphic, potentiation, strong synergy)
- GEARS slightly better for redundant interactions

### Chemical Perturbation
- LINCS-Drug: outperforms chemCPA (median R² 0.919 vs 0.899)
- sci-Plex: outperforms Biolord (median R² 0.984 vs 0.587)
- Identified stereoisomer data leakage in prior benchmarks

### Coding-Sequence Variants (unique to PerturbNet)
- GATA1: all 7,847 point mutations → 3 predicted classes (erythroid-depleted/intermediate/enriched)
- Large-effect variants cluster in DNA-contact region with large side-chain volume changes
- TP53/KRAS: outperforms baselines on large-effect genes

## Limitations

- Still Level 2 (generative interpolation), not Level 3 (causal intervention) — same epistemic limitation as GEARS
- Distributional predictions harder to benchmark — standard metrics (R², Pearson) don't fully capture distribution quality
- GO annotation completeness limits GenotypeVAE (shared limitation with GEARS)
- Coding-variant predictions limited to missense; non-coding regulatory variants not addressed
- Does not model GRN structure or causal direction

## Related Papers

- [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] — GEARS: direct competitor; GNN + knowledge graph approach (PerturbNet outperforms on same benchmarks)
- [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] — Squidiff: diffusion model approach to perturbation prediction
- [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]] — PerturBERT: BERT-based perturbation foundation model
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT: foundation model with perturbation task
- [[single-cell-foundation/hao-2024-large-scale-foundation-model]] — scFoundation: perturbation prediction downstream task
- [[drug-resistance/alsulami-2026-predicting-and-interpreting-cell]] — PrePR-CT: drug response prediction with graph attention
- [[drug-resistance/chen-2022-deep-transfer-learning-of]] — scDEAL: bulk→single-cell drug response transfer learning
- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle: GRN-based causal perturbation (Level 3 approach, contrasts with PerturbNet's Level 2)
