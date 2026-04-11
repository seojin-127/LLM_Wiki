---
title: "Single-Cell Annotation Methods: A Comparative Overview"
type: overview
created: 2026-04-11
category: overviews
tags: [annotation, label-transfer, SingleR, CellTypist, scANVI, scTab, popV, scGPT, scEvolver, NS-Forest, foundation-model]
papers:
  - single-cell-dl/aran-2019-reference-based-analysis-of
  - single-cell-dl/dominguez-conde-2022-cross-tissue-immune-cell
  - single-cell-dl/xu-2021-probabilistic-harmonization-and
  - single-cell-dl/dedonno-2023-population-level-integration-of
  - single-cell-dl/lotfollahi-2022-mapping-single-cell-data
  - single-cell-dl/hao-2021-integrated-analysis-of-multimodal
  - single-cell-dl/ergen-2024-consensus-prediction-cell
  - single-cell-dl/fischer-2024-sctab-scaling-cross-tissue
  - single-cell-dl/liu-2024-discovery-of-optimal-cell
  - single-cell-dl/ge-2026-prototype-based-continual-learning-for
  - single-cell-dl/luecken-2022-benchmarking-atlas-level-data
  - single-cell-foundation/cui-2024-scgpt-toward-building-foundation
  - single-cell-foundation/hao-2024-large-scale-foundation-model
  - single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell
  - brain-atlas/he-2024-integrated-transcriptomic-cell-atlas
---

## What Annotation Actually Means: Two Different Problems

"Cell type annotation" conflates two distinct problems.

**1. Reference-to-query label transfer**
- An annotated reference dataset already exists
- Labels are transferred to new query cells
- Core challenges: batch effects, platform differences, handling of unknown cell types

**2. De novo annotation**
- No reference, or an incomplete one
- Labels are assigned from scratch using marker genes or clustering
- Core challenges: marker gene subjectivity, scalability, reproducibility

Most modern methods target (1); (2) still requires domain-expert involvement. NS-Forest ([[single-cell-dl/liu-2024-discovery-of-optimal-cell]]) is an attempt to systematize the marker-selection step of (2).

---

## Six Paradigms

### Paradigm 1 — Correlation-based

#### SingleR
[[single-cell-dl/aran-2019-reference-based-analysis-of]]

Compares each cell's expression profile against pure cell types in a bulk RNA-seq reference using **Spearman correlation**. Iterative refinement: keep only the top candidates, recompute on their distinguishing genes. No training required.

| Property | Detail |
|----------|--------|
| Reference format | Bulk RNA-seq (ImmGen / ENCODE / Blueprint) |
| Training required | ❌ |
| Speed | Medium (scales with reference size) |
| Uncertainty | Correlation score (indirect) |
| Key strength | Zero-setup, works out of the box |
| Key limitation | Cannot annotate types absent from reference; bulk↔single-cell resolution gap |

---

### Paradigm 2 — Supervised classifiers

#### CellTypist
[[single-cell-dl/dominguez-conde-2022-cross-tissue-immune-cell]]

**Logistic regression with SGD**. Pretrained on curated public immune-cell datasets. Models are distributed openly via celltypist.org.

| Property | Detail |
|----------|--------|
| Model | Logistic regression + SGD |
| Training data | Curated public immune-cell reference |
| Speed | Very fast (millions of cells via SGD) |
| Uncertainty | Class probabilities |
| Key strength | Speed, scale, open model ecosystem |
| Key limitation | Cannot recognize cell types outside training set; immune-biased |

#### scTab
[[single-cell-dl/fischer-2024-sctab-scaling-cross-tissue]]

**Tabular deep learning** (MLP) trained on 22.2M scRNA-seq cells. Designed for cross-tissue annotation.

| Property | Detail |
|----------|--------|
| Model | MLP (tabular DL) |
| Training data | 22.2M cells across tissues |
| Scaling law | Both data and model size correlate with performance |
| Key strength | Nonlinear models beat linear ones on cross-tissue tasks |
| Key limitation | Inherits label quality; weak on rare cell types |

---

### Paradigm 3 — Probabilistic generative models

#### scANVI
[[single-cell-dl/xu-2021-probabilistic-harmonization-and]]

Semi-supervised extension of scVI. Cell type labels become latent variables: labeled reference cells fix their label; unlabeled query cells infer labels jointly with integration. **Integration and annotation in one model**.

| Property | Detail |
|----------|--------|
| Model | Semi-supervised VAE |
| Reference | Partial (reference labeled, query unlabeled) |
| Joint integration | ✅ |
| Uncertainty | Per-cell posterior probability |
| scIB benchmark | **Best** on labeled integration |
| Key limitation | Degrades with too few labeled cells per type |

#### scPoli
[[single-cell-dl/dedonno-2023-population-level-integration-of]]

+5.06% over scANVI on its benchmark. Adds a **prototype loss** that pulls cells toward class centroids; unlabeled cells are assigned to the nearest prototype.

- Open-world: new labeled types in the query become new prototypes without retraining
- Learns population-level sample embeddings jointly

#### scArches + label transfer
[[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]]

Adds ~10K query-specific parameters to a frozen pretrained scVI/scANVI reference. Query cells are projected into the reference latent, then **kNN label transfer** is applied. Raw data need never be shared.

---

### Paradigm 4 — Ensembles with uncertainty quantification

#### popV
[[single-cell-dl/ergen-2024-consensus-prediction-cell]]

Runs multiple classifiers (scVI, kNN, SVM, SingleR, …) and derives a consensus via **cell-ontology-aware voting**. Each cell receives an uncertainty score from inter-method agreement.

| Property | Detail |
|----------|--------|
| Members | scVI + kNN + SVM + SingleR + … |
| Uncertainty | Disagreement → high uncertainty |
| Practical value | Auto-annotate 80%+ of cells, flag <20% for review |
| Key limitation | Higher compute than any single method |

**Why popV matters**: at atlas scale, no one can hand-review every cell. popV tells you *which* cells deserve manual inspection. [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]] (HNOCA) adopts this philosophy in its snapseed + scPoli quality-check stage.

---

### Paradigm 5 — Foundation models (fine-tuning / zero-shot)

#### scGPT
[[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]]

GPT-style transformer pretrained on 33M+ cells. A lightweight head is fine-tuned for annotation; **outperforms Seurat and SingleR** on cross-dataset benchmarks.

#### scFoundation
[[single-cell-foundation/hao-2024-large-scale-foundation-model]]

100M parameters, 50M+ cells. SOTA on six tasks including annotation. Read-depth-aware pretraining also helps annotation quality.

#### EpiAgent — scATAC-seq annotation
[[single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell]]

Foundation model dedicated to scATAC-seq. **Zero-shot annotation** from pretrained embeddings without fine-tuning. Fills a major gap — scATAC-seq annotation tooling was scarce compared to scRNA-seq.

| Model | Zero-shot | Fine-tuning | scATAC |
|-------|-----------|-------------|--------|
| scGPT | ❌ | ✅ | partial |
| scFoundation | ❌ | ✅ | ❌ |
| EpiAgent | ✅ | ✅ | ✅ |

---

### Paradigm 6 — Continual learning

#### scEvolver
[[single-cell-dl/ge-2026-prototype-based-continual-learning-for]]

Directly tackles catastrophic forgetting: adding new cell types must not destroy knowledge of existing ones. scGPT backbone + LoRA+MoE adapter + memory-augmented prototypes + hard-sample replay buffer + MAPPL loss.

| Property | Detail |
|----------|--------|
| Backbone | scGPT (frozen) |
| 5-shot performance | +24.5% macro-F1 over next-best on PANCREAS |
| Cross-modality | Handles RNA+ATAC, RNA+ADT |
| Key value | Preserves annotation quality as data accumulates |
| Notable finding | SF-like transitional epithelium in IBD gut, missed by prior annotations |

---

## Upstream of Annotation: Marker Gene Discovery

Before any annotation can run, someone has to decide *which genes define which cell types*. That is the **marker gene selection** problem.

#### NS-Forest v4
[[single-cell-dl/liu-2024-discovery-of-optimal-cell]]

Random forest feature importance → decision tree refinement → **minimal sufficient marker combinations**. Introduces **On-Target Fraction (OTF)** — how exclusively a marker is expressed in its assigned type.

- Beats Wilcoxon-DE marker selection on F-beta score
- Validated on HuBMAP brain / kidney / lung
- Directly usable for spatial transcriptomics panel design

DE-selected genes are "statistically significant," not "sufficient to classify." NS-Forest separates the two.

---

## Method Comparison at a Glance

| Method | Training | Joint integration | Uncertainty | Cross-tissue | Compute | Rare types |
|--------|----------|-------------------|-------------|--------------|---------|------------|
| SingleR | ❌ | ❌ | indirect | ⚠️ | low | ⚠️ |
| CellTypist | pretrained | ❌ | ✅ | ⚠️ | very low | ⚠️ |
| scANVI | ✅ | ✅ | ✅ | ✅ | medium | ⚠️ |
| scPoli | ✅ | ✅ | ✅ | ✅ | medium | ✅ (open-world) |
| scTab | ✅ | ❌ | ❌ | ✅ | medium | ❌ |
| popV | composite | optional | ✅✅ | ✅ | high | ✅ |
| scGPT | pretrained | ✅ | ❌ | ✅ | high | ⚠️ |
| EpiAgent | pretrained | ❌ | zero-shot | ✅ | high | ✅ |
| scEvolver | pretrained | ❌ | ❌ | ✅ | high | ✅ |

---

## Timeline: What Changed

```
2018-2019  Manual marker-based annotation is the norm
  └─ SingleR: first reference-based automation (Spearman)

2019-2021  Integration and annotation done separately
  └─ scANVI: unified them into one model

2022  Ensembles and uncertainty quantification
  └─ popV: tells you which cells to trust and which to doubt
  └─ CellTypist: processes 1M+ cells in minutes

2022-2023  Reference atlas era: annotation = reference mapping
  └─ scArches → scPoli: map new data to an atlas, labels follow

2024-2025  Foundation models raise the baseline
  └─ scGPT, scFoundation: pretrained embeddings reach SOTA on cross-dataset annotation

2026-     Continual learning: atlases become living systems
  └─ scEvolver: add new cell types without forgetting the old
```

---

## Decision Tree

```
I need to annotate new data
│
├─ I have a good reference atlas (same tissue/modality)
│   ├─ Fast, exploratory → CellTypist or SingleR
│   ├─ Strong batch effects → scANVI or scPoli
│   │   └─ Expect novel cell types → scPoli (open-world)
│   ├─ I need to know which cells are uncertain → popV
│   └─ Raw data can't be shared → scArches
│
├─ Cross-tissue annotation (reference and query differ)
│   ├─ RNA-seq → scTab or scGPT fine-tuning
│   └─ ATAC-seq → EpiAgent
│
├─ No reference (de novo)
│   ├─ Discover markers → NS-Forest v4
│   └─ Foundation-model zero-shot → EpiAgent (ATAC), scGPT (RNA)
│
├─ New cell types keep arriving over time
│   └─ scEvolver (continual learning)
│
└─ Highest-trust result for an atlas-level paper
    └─ popV ensemble → expert curation
```

---

## Open Problems This Wiki Cannot Answer

1. **Novel cell type detection**: every method is weak at "types not in the reference." scPoli's open-world mode and scEvolver's uncertainty buffer are partial solutions; systematic benchmarks are missing.

2. **Circular dependency between integration and annotation**: integration quality affects annotation, and labels in turn improve integration (scANVI, scPoli). No standard protocol specifies how many iterations to run.

3. **Foundation-model head-to-head is missing**: whether scGPT / scFoundation actually beat scANVI / scPoli on annotation is not yet shown in this wiki — scGPT (cui-2024) only compares against Seurat and SingleR.

4. **Label-noise propagation**: annotation errors in large atlases propagate to new data through reference-based methods. popV's uncertainty helps detect it, but there is no systematic fix.

---

## Practical Recommendations

**Atlas-scale projects (integrating many datasets)**

1. scPoli for joint integration + label transfer
2. popV for per-cell uncertainty scoring
3. Hand-curate only the <20% high-uncertainty cells
4. Follow the HNOCA pipeline ([[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]]): RSS projection → snapseed → scPoli

**Single small dataset (fast exploration)**

1. CellTypist (immune) or SingleR (general) for a first pass
2. Complement with Seurat label transfer, including WNN for multimodal ([[single-cell-dl/hao-2021-integrated-analysis-of-multimodal]])
3. Validate the resulting markers with NS-Forest

**Environments where data keeps arriving**

- Consider scEvolver: preserves annotation quality as new cell types appear over time

---

*Sources: [[single-cell-dl/aran-2019-reference-based-analysis-of]], [[single-cell-dl/dominguez-conde-2022-cross-tissue-immune-cell]], [[single-cell-dl/xu-2021-probabilistic-harmonization-and]], [[single-cell-dl/dedonno-2023-population-level-integration-of]], [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]], [[single-cell-dl/hao-2021-integrated-analysis-of-multimodal]], [[single-cell-dl/ergen-2024-consensus-prediction-cell]], [[single-cell-dl/fischer-2024-sctab-scaling-cross-tissue]], [[single-cell-dl/liu-2024-discovery-of-optimal-cell]], [[single-cell-dl/ge-2026-prototype-based-continual-learning-for]], [[single-cell-dl/luecken-2022-benchmarking-atlas-level-data]], [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]], [[single-cell-foundation/hao-2024-large-scale-foundation-model]], [[single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell]], [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]]*
