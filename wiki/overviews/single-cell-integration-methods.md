---
title: "Single-Cell Integration Methods: A Comparative Overview"
type: overview
created: 2026-04-11
category: overviews
tags: [integration, batch-correction, annotation, scVI, Harmony, scPoli, scArches, WNN, benchmark]
papers:
  - single-cell-dl/lopez-2018-deep-generative-modeling-for
  - single-cell-dl/korsunsky-2019-fast-sensitive-and-accurate
  - single-cell-dl/xu-2021-probabilistic-harmonization-and
  - single-cell-dl/hao-2021-integrated-analysis-of-multimodal
  - single-cell-dl/lotfollahi-2022-mapping-single-cell-data
  - single-cell-dl/luecken-2022-benchmarking-atlas-level-data
  - single-cell-dl/dominguez-conde-2022-cross-tissue-immune-cell
  - single-cell-dl/dedonno-2023-population-level-integration-of
  - single-cell-dl/schuster-2024-multidgd-versatile-deep
  - single-cell-dl/boyeau-2025-deep-generative-modeling-of
  - single-cell-foundation/heimberg-2025-cell-atlas-foundation-model
  - single-cell-foundation/cui-2024-scgpt-toward-building-foundation
---

## What Is Integration?

Single-cell "integration" covers two conceptually distinct but often conflated tasks:

1. **Batch correction / harmonization** — removing technical variation (lab, protocol, platform) while preserving biological variation; output is a shared embedding or corrected count matrix
2. **Label transfer / annotation** — assigning cell type labels from a reference to a query dataset; requires a harmonized embedding as prerequisite

A third task has emerged more recently:

3. **Sample-level comparison** — after cell-level integration, asking *which samples/donors differ and in which cell populations* ([[single-cell-dl/boyeau-2025-deep-generative-modeling-of]])

Most tools target task 1 or 1+2 together. The choice of method should be driven by which task you actually need.

---

## The Landscape: Four Paradigms

### Paradigm 1 — Linear correction (Harmony)

**Representative**: [[single-cell-dl/korsunsky-2019-fast-sensitive-and-accurate]]

Operates on a pre-computed PCA embedding. Iteratively clusters cells into soft groups (with a diversity penalty that forces multi-dataset membership), then computes per-cluster linear correction factors. Each cell's correction is a membership-weighted average of cluster corrections.

| Property | Detail |
|----------|--------|
| Input | PCA embedding (not raw counts) |
| Correction | Linear, cell-type-specific |
| Scale | ~1M cells on a laptop |
| Speed | Very fast |
| Annotation transfer | No |
| scIB rank (RNA) | Competitive for simple tasks; top for scATAC-seq |
| Key limitation | Linear assumption; over-corrects when biology is confounded with batch |

**When to use**: Quick exploratory integration; scATAC-seq; when you need to run Seurat/Scanpy and want a drop-in batch correction.

---

### Paradigm 2 — Deep generative models: the scVI family

The scVI family models count data directly with a probabilistic generative model (VAE + ZINB distribution), jointly learning a batch-corrected low-dimensional latent space. All members share the same scvi-tools framework.

#### scVI — the foundation
[[single-cell-dl/lopez-2018-deep-generative-modeling-for]]

Encoder: expression + batch label → latent z (biological) + l (library size). Decoder: z + batch → ZINB parameters. Batch effects removed implicitly by conditioning the decoder on batch while keeping z batch-agnostic. A single model covers normalization, batch correction, clustering, DE, and imputation.

| Property | Detail |
|----------|--------|
| Correction | Nonlinear (neural network) |
| Scale | 1M+ cells (stochastic optimization) |
| Annotation transfer | No |
| scIB rank (RNA, unsupervised) | Top-tier alongside Scanorama |
| Key strength | Probabilistic DE in harmonized space |

#### scANVI — add labels
[[single-cell-dl/xu-2021-probabilistic-harmonization-and]]

Semi-supervised extension: cell type labels become latent variables. Labeled reference cells anchor annotation; unlabeled query cells infer labels jointly with integration. Single model handles harmonization + annotation + DE.

| Property | Detail |
|----------|--------|
| Labels required | Partial (reference only) |
| scIB rank (RNA, labeled) | **Best overall** |
| Key strength | Probabilistic uncertainty per cell |
| Key limitation | Degrades with very few labeled cells per type |

#### scArches — reference mapping
[[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]]

"Architecture surgery": adds ~10K query-specific parameters to a frozen pretrained scVI/scANVI model; fine-tunes only those. Users share fine-tuned weights, not raw data → privacy-preserving. Retains disease variation when mapping onto a healthy reference.

| Property | Detail |
|----------|--------|
| New parameters | ~10K vs. millions in de novo integration |
| Privacy | Raw data never shared |
| Disease variation | Preserved |
| Key limitation | Zero-shot not supported; quality inherits from reference |

#### scPoli — population level
[[single-cell-dl/dedonno-2023-population-level-integration-of]]

Two innovations on top of scVI: (1) continuous sample embeddings (replace one-hot batch vectors) and (2) prototype loss that pulls same-type cells toward class centroids. Open-world: novel cell types from labeled query added as new prototypes without retraining.

| Property | Detail |
|----------|--------|
| vs. scANVI | +5.06% overall on scIB-style benchmark |
| Scale | 7.8M cells / 2,375 samples (PBMC atlas) |
| Novel cell types | Open-world extension |
| Sample-level | Sample embeddings explain batch/biology sources |
| Used by | HNOCA (He et al. 2024) — chosen as best integrator |

#### MrVI — cohort comparisons
[[single-cell-dl/boyeau-2025-deep-generative-modeling-of]]

Hierarchical extension: two latent variables per cell — u (cell state, disentangled from sample) and z (cell state + sample effects). Computes a per-cell sample distance matrix by projecting each cell counterfactually into every sample's z. Enables annotation-free discovery of which samples differ, and in which cell populations.

| Property | Detail |
|----------|--------|
| Primary task | Sample-level comparison, not just integration |
| Sample grouping | Annotation-free |
| Applied to | COVID-19 severity, IBD pericytes, perturbation MoA |
| Key limitation | Sample distance matrix is O(S²) per cell |

---

### Paradigm 3 — Multimodal integration (WNN / multiDGD)

When you have multiple data types per cell (RNA + protein, RNA + ATAC), different methods are needed.

#### Seurat v4 WNN
[[single-cell-dl/hao-2021-integrated-analysis-of-multimodal]]

Learns per-cell modality weights reflecting how informative each data type is for that specific cell. Builds a weighted nearest-neighbor graph combining modality-specific graphs. Resolves cell states (gd T cells, MAIT) that RNA alone cannot separate.

| Property | Detail |
|----------|--------|
| Modalities | Any paired (RNA+ADT, RNA+ATAC, etc.) |
| Per-cell weights | Yes — each cell can weight modalities differently |
| Reference mapping | Cross-modality anchor-based |
| Limitation | Requires same-cell paired data |

#### multiDGD
[[single-cell-dl/schuster-2024-multidgd-versatile-deep]]

VAE with separate decoders per modality (RNA: NB, ATAC: binary/count). Post-hoc batch integration via covariate modeling without retraining. Best reconstruction without feature selection.

| Property | Detail |
|----------|--------|
| Modalities | RNA + ATAC (tested) |
| Batch integration | Post-hoc; no retraining needed |
| Key strength | No feature selection required |

---

### Paradigm 4 — Foundation model embeddings

Large pretrained single-cell transformers produce embeddings that implicitly integrate across batches.

#### scGPT
[[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]]

Pretrained on 33M+ cells; multi-batch integration via fine-tuning. Competitive with scVI and Harmony on cross-dataset benchmarks. Additional capability: perturbation prediction, GRN inference.

#### scFoundation
[[single-cell-foundation/hao-2024-large-scale-foundation-model]]

100M parameters, 50M+ cells. Asymmetric transformer with read-depth-aware pretraining. State-of-the-art on 6+ tasks including integration; can enhance gene expression before integration.

#### SCimilarity
[[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]]

Metric learning on 23.4M cells from 412 studies. Query = any cell profile → nearest neighbors in embedding space. Not batch correction per se, but cross-study cell similarity search at scale.

**Caveat**: Foundation model integration is still emerging; scIB benchmark (2022) predates these tools. Direct head-to-head against scVI/scPoli is not yet in this wiki.

---

## Decision Framework

```
What do you need?
│
├─ Just batch correction, no labels
│   ├─ Fast / RAM-limited → Harmony
│   ├─ Best quality (RNA) → scVI or Scanorama
│   └─ scATAC-seq → Harmony or LIGER
│
├─ Batch correction + annotation transfer
│   ├─ Labels from reference → scANVI (best in scIB)
│   ├─ Many samples, population-level → scPoli (better than scANVI + sample embeddings)
│   └─ Privacy-sensitive / federated → scArches on top of scANVI
│
├─ Multimodal (RNA + protein/ATAC in same cell)
│   ├─ Exploratory, RNA + ADT → Seurat WNN
│   └─ RNA + ATAC, need reconstruction → multiDGD
│
├─ Large cohort: which samples differ?
│   └─ → MrVI (per-cell sample distance matrix)
│
└─ Cross-study cell search (no explicit integration)
    └─ → SCimilarity
```

---

## What the scIB Benchmark Tells Us

[[single-cell-dl/luecken-2022-benchmarking-atlas-level-data]] — 68 methods × 13 tasks × 14 metrics:

| Scenario | Winner | Runner-up |
|----------|--------|-----------|
| RNA, labels available | **scANVI** | scGen |
| RNA, unsupervised | **Scanorama** ≈ **scVI** | Harmony |
| scATAC-seq | **Harmony** | LIGER |
| Simple tasks | ComBat, Harmony | — |
| Complex nested batches | scANVI, scVI | Scanorama |

**Key preprocessing findings**:
- HVG (highly variable gene) selection universally improves all methods
- Z-score scaling improves batch removal but *hurts* biological conservation — avoid unless batch removal is the only goal

**Important caveat**: scIB was published in 2022. scPoli, MrVI, and foundation models postdate this benchmark. scPoli outperforms scANVI by 5% on its own benchmark.

---

## The scVI-tools Lineage

The scVI ecosystem has progressively addressed new problems:

```
scVI (2018)
  └─ Unsupervised harmonization + DE
      └─ scANVI (2021)
           └─ + semi-supervised annotation
               └─ scArches (2022)
                    └─ + reference mapping, privacy
                        └─ scPoli (2023)
                             └─ + population-level, open-world, sample embeddings
                                 └─ MrVI (2025)
                                      └─ + per-cell sample-level comparison
```

All available through scvi-tools (scverse ecosystem). If you're already using scVI, upgrading to scANVI → scPoli is low-friction.

---

## Practical Notes

**Pipeline that currently has the most empirical support** (as of this wiki):

1. **Preprocessing**: HVG selection (2,000–5,000 genes); no z-score scaling
2. **Integration**: scPoli (if you have reference labels) or scVI (if unsupervised)
3. **Annotation**: scANVI / scPoli label transfer, or popV ensemble ([[single-cell-dl/ergen-2024-consensus-prediction-cell]])
4. **Quality check**: iLISI / cLISI on the output embedding ([[single-cell-dl/luecken-2022-benchmarking-atlas-level-data]])
5. **Cohort comparisons**: MrVI on top of integrated embedding

**Harmony is not "worse"** — it's faster, simpler, and well-suited for:
- Quick exploration
- scATAC-seq
- Downstream tools that expect PCA-style input (e.g., standard Seurat/Scanpy pipelines)

---

## Open Questions (Not Covered by This Wiki)

- **Foundation models vs. classical integration**: scGPT/scFoundation head-to-head against scPoli not yet benchmarked here
- **Scalability beyond 10M cells**: scPoli tested to 7.8M; limits unclear
- **When does integration fail?**: biological variation confounded with batch (e.g., disease-specific cohorts) remains unsolved
- **Spatial data**: none of these methods natively handle spatial coordinates; specialized tools needed

---

*Sources: [[single-cell-dl/lopez-2018-deep-generative-modeling-for]], [[single-cell-dl/korsunsky-2019-fast-sensitive-and-accurate]], [[single-cell-dl/xu-2021-probabilistic-harmonization-and]], [[single-cell-dl/hao-2021-integrated-analysis-of-multimodal]], [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]], [[single-cell-dl/luecken-2022-benchmarking-atlas-level-data]], [[single-cell-dl/dedonno-2023-population-level-integration-of]], [[single-cell-dl/schuster-2024-multidgd-versatile-deep]], [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]], [[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]], [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]]*
