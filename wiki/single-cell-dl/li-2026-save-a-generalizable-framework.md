---
title: "SAVE: A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention"
authors: Jiahao Li, Jiayi Dong, Peng Ye, Xiaochi Zhou, Haohai Lu, Fei Wang
year: 2026
arxiv: 2604.16776
source: li-2026-save-a-generalizable-framework.md
category: single-cell-dl
tags: [generative-model, flow-matching, vae, transformer, gene-block, conditional-generation, batch-correction, perturbation-prediction, classifier-free-guidance, iclr-2026]
---

## Summary

SAVE (Fudan, Wang lab; ICLR 2026) is a **VAE + Conditional Flow Matching** framework for multi-condition scRNA-seq generation. Its central trick: instead of treating each gene as an independent token (the scGPT/scBERT/Geneformer school), it groups genes into **semantic Gene Blocks** using LLM embeddings (text-embedding-ada-002 on NCBI gene summaries) clustered by Optimal Transport, then applies Transformer attention over these coarser, biologically meaningful blocks. Conditions (batch, cell type, disease, perturbation) are injected via **AdaLN**, and a 60% **condition masking** strategy enables Classifier-Free Guidance and out-of-sample condition combinations. Beats scVI, CFGen, scDiffusion across single-/dual-/multi-condition generation, beats Harmony/scVI/trVAE on scIB batch correction, and beats scGEN/trVAE/scDisInFact on IFN-β perturbation prediction — all with a single hyperparameter set on a single RTX 3090.

## Key Contributions

- **Gene Block Attention**: attention over semantically clustered gene groups instead of flat gene tokens. Blocks come from LLM embeddings (text-embedding-ada-002, 1,536-d) of cleaned NCBI Gene "Summary" texts, partitioned into L equal-size blocks by iterative Optimal Transport clustering (default K=3200 genes/block).
- **Latent Flow Matching backbone**: VAE with Gene Block Attention encoder/decoder for compression, plus a Conditional Flow Matching network operating on the latent space using an affine probability path `xₜ = (1−t)x₀ + tx₁`.
- **AdaLN-based condition injection**: arbitrary categorical conditions encoded into learnable embeddings, then projected to per-layer (α, β, γ) modulation parameters that gate Attention/FFN sub-layers — same machinery as DiT, but for cells.
- **Condition masking + Classifier-Free Guidance**: each condition slot independently masked at p=0.6 during training, enabling the FM network to learn both `v_θ(xₜ,t,s)` and `v_θ(xₜ,t)` and supports unseen condition combinations at inference.
- **One model, three benchmarks**: single hyperparameter set wins on (a) conditional generation fidelity, (b) batch correction (scIB), and (c) out-of-sample drug perturbation prediction.

## Methods & Architecture

```
NCBI Gene Summary text
    ↓ text-embedding-ada-002
Gene embeddings g_i ∈ ℝ^1536
    ↓ Optimal Transport clustering (balanced)
L gene blocks of K genes each   →   reshape Y(N×G) → X(N×L×K)

X ─[Gene Block Attn Encoder]─→ μ, σ²  ─reparam→  z   (VAE)
                                                  │
            x₀ (Gaussian prior)                    │ 
                  │                                ▼
       Conditional Flow Matching ──AdaLN──→ generated z
       (affine path, MSE on velocity)        ↑
                                            S (conditions, 60% masked)

z ─[Gene Block Attn Decoder]─→ X̂ ─reshape→ Ŷ(N×G)
```

### Three modules
1. **Gene Block Construction** (offline, once per gene set)
   - Clean NCBI Gene "Summary" texts (avg ~73 words, per Chen & Zou 2024 protocol)
   - Encode → 1,536-d embeddings; iteratively assign to L blocks via balanced OT (`T·1_L = a, T^T·1_G = b`); update block centroids until convergence
   - Result: each gene belongs to exactly one biologically coherent block

2. **VAE encoder/decoder over blocks**
   - Linear lift `W_in: ℝ^K → ℝ^e` per block, then standard pre-LN Transformer (attention + FFN) over the L block tokens
   - Encoder outputs Gaussian `(μ,σ²)` for `N×L×d` latent; KL penalty + reparameterization
   - Decoder mirrors structure; reconstruction is `−log L(X̂|X)`

3. **Conditional Flow Matching network** (DiT-style)
   - Affine path: `xₜ = (1−t)x₀ + t·x₁`, target velocity `uₜ = x₁ − x₀`
   - Loss `L_FM = 𝔼[‖v_θ(xₜ,t,s) − uₜ‖²]`
   - AdaLN injects condition embeddings; CFG `v̂ = (1−w)v_θ(xₜ,t) + w·v_θ(xₜ,t,s)` at inference

### Training detail
- log-CPM (10⁴ counts) → max-abs scale to [0,1]
- AdamW lr=1e-4, weight decay=2.5e-5, mask p=0.6
- Single RTX 3090 24GB; same hyperparameters across all benchmarks

## Results

### Conditional generation
| Dataset | Conditions | Best baseline | SAVE |
|---|---|---|---|
| PBMC3K | cell type | CFGen WD 16.94 | WD 19.14 / **MMD 1.80** (mixed) |
| Dentate Gyrus | clusters | scDiffusion WD 22.56 | **WD 9.16 / MMD 0.17** (>2× better) |
| Tabula Muris | tissue | CFGen MMD 0.19 | **MMD 0.04** |
| Heart | batch + cell type | CFGen WD 12.57 | **WD 8.30 / MMD 0.63** |
| PBMC | batch + cell type | scDiffusion WD 11.38 | **WD 5.37 / MMD 0.29** |
| Lung Atlas | batch + cell type | scDiffusion WD 13.89 | **WD 4.37 / MMD 1.14** |
| Lung Cancer (5-cond, 27 types) | seen | scDiffusion WD 5.27 | **WD 3.10±0.96** |
| Lung Cancer | **unseen** combinations | scDiffusion WD 5.29 | **WD 4.63±0.95** |

UMAP visualizations on Heart show SAVE distinguishes batch differences within Ventricular Cardiomyocytes that CFGen/scDiffusion blur; on Lung Cancer unseen conditions, SAVE retains tighter ground-truth alignment in latent space.

### Batch correction (scIB)
| Method | Lung Atlas | Heart | PBMC |
|---|---|---|---|
| Scanorama | 0.77 | 0.76 | 0.80 |
| Harmony | 0.76 | 0.81 | 0.80 |
| scVI | 0.68 | 0.72 | 0.59 |
| trVAE | 0.78 | 0.78 | 0.82 |
| **SAVE** | **0.81** | 0.80 | **0.83** |

SAVE tops biological conservation on all three; tops batch score on 2/3 (Harmony wins Heart batch).

### IFN-β perturbation prediction (PBMC-IFN, Haber et al.)
- SAVE-generated stimulated profiles most closely match real perturbed distribution across CD4T, Dendritic, B, NK, FCGR3A+Mono, CD14+Mono, CD8T cell types
- ISG15 / TNFSF10 violin plots: SAVE most faithfully reproduces magnitude + spread of stimulation response
- Outperforms scGEN, trVAE, scDisInFact

## Limitations

- **K=3200 genes/block fixed** — block size is a hyperparameter, not learned
- **NCBI English summaries required**: unannotated or poorly annotated genes are awkward; non-human/mouse coverage less clear
- **Per-dataset training** — not a foundation model; doesn't share pretrained weights across studies the way scGPT/scFoundation do
- **scRNA-seq only** — no scATAC, no spatial, no protein
- **Perturbation eval is narrow**: one drug (IFN-β) on PBMC; no genetic perturbations, no GEARS-style 0/1/2-gene held-out splits, no chemCPA-style chemical structure conditioning
- **Block-level interpretability**: attention is over blocks, not genes — gives *module-level* explanation, but not per-gene mechanism

## Related Papers

### Direct baselines / contrasts
- [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] — scVI: VAE+ZINB foundation; SAVE upgrades the encoder/decoder with Gene Block Attention and bolts on flow matching
- [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] — Squidiff: closest philosophical sibling — conditional **diffusion** for scRNA-seq generation/perturbation; SAVE picks **flow matching** over diffusion (same goal, simpler ODE)
- [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] — PerturbNet: distributional perturbation prediction with cINN; SAVE uses CFG instead of normalizing flows but covers similar ground

### Tokenization contrasts (the "flat gene token" school SAVE explicitly criticizes)
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT: rank-binned gene tokens
- [[single-cell-foundation/hao-2024-large-scale-foundation-model]] — scFoundation: special-token zero handling

### Batch correction baselines
- [[single-cell-dl/korsunsky-2019-fast-sensitive-and-accurate]] — Harmony: linear iterative soft-clustering — SAVE's strongest classical competitor
- [[single-cell-dl/luecken-2022-benchmarking-atlas-level-data]] — scIB: the integration benchmark SAVE evaluates on

### Perturbation prediction context
- [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] — GEARS: GNN + GO graph; harder combinatorial held-out splits than SAVE evaluates on
- [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] — Stegle lab review: argues simple baselines often beat foundation models on extrapolation; SAVE's per-dataset training fits this critique's recommendation

### Concept pages
- [[concepts/variational-autoencoder]] — VAE backbone
- [[concepts/distributional-vs-point-prediction]] — SAVE predicts the full distribution, evaluated by WD/MMD (not mean reconstruction)
- [[concepts/combinatorial-perturbation-prediction]] — Lung Cancer 27-type setup with 2 held-out combinations is a (limited) instance of this evaluation
- [[concepts/interpolation-vs-extrapolation]] — held-out conditions = extrapolation; condition masking is SAVE's main mechanism for handling it
- [[concepts/expressivity-interpretability-tradeoff]] — Gene Blocks sit on the "knowledge mask" axis (semantic prior baked into tokenization) vs scGPT's flat tokens
