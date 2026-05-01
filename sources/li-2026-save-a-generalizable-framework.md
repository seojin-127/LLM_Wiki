---
title: "SAVE: A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention"
authors: Jiahao Li, Jiayi Dong, Peng Ye, Xiaochi Zhou, Haohai Lu, Fei Wang
year: 2026
arxiv: 2604.16776
category: single-cell-dl
pdf_path: papers/li-2026-save-a-generalizable-framework.pdf
pdf_filename: li-2026-save-a-generalizable-framework.pdf
source_collection: user-supplied
---

## One-line Summary
SAVE: VAE + Conditional Flow Matching with **Gene Block Attention** — genes grouped into semantic blocks via LLM (text-embedding-ada-002 on NCBI summaries) + Optimal Transport clustering, with condition masking for unseen-condition generalization. Beats scVI, CFGen, scDiffusion across single/dual/multi-condition generation, batch correction, and IFN-β perturbation prediction.

## 1. Document Info
- Conference: ICLR 2026 (published as conference paper)
- arXiv: 2604.16776v1, posted 18 Apr 2026
- Affiliation: College of Computer Science and AI, Fudan University; Shanghai Key Laboratory of Intelligent Information Processing
- Code: https://github.com/fdu-wangfeilab/sc-save
- Corresponding author: Fei Wang (wangfei@fudan.edu.cn)

## 2. Key Contributions
- **Gene Block Attention**: Groups genes into semantic blocks using LLM embeddings (text-embedding-ada-002 on NCBI Gene Database "Summary" texts) clustered by Optimal Transport into L balanced, non-overlapping blocks. Replaces flat gene-token view with biologically meaningful coarse-grained tokens.
- **Latent Flow Matching (LFM) framework**: VAE encoder/decoder (with Gene Block Attention) compresses scRNA-seq into latent space; a Conditional Flow Matching network with affine probability path generates samples from the latent prior.
- **Condition injection via AdaLN**: Adaptive Layer Normalization injects categorical conditions (batch, cell type, disease stage, perturbation, donor age, etc.) into Transformer blocks via learnable scaling/shift parameters.
- **Condition Mask training strategy**: Each condition element independently masked with p=0.6, enabling Classifier-Free Guidance and generalization to unseen condition combinations.
- Unified framework — single hyperparameter set works across conditional generation, batch correction, and out-of-sample perturbation prediction.

## 3. Methods & Architecture

### Three core modules
1. **Gene Block Construction** (preprocessing, done once per dataset)
   - Pull "Summary" text from NCBI Gene Database for each gene → clean
   - Encode with `text-embedding-ada-002` → 1,536-d gene embedding `gᵢ`
   - Iterative Optimal Transport clustering: cost `Cᵢⱼ = ‖gᵢ − cⱼ‖²`, balanced transport (uniform marginals `T·1_L = a, T^T·1_G = b`) → L equally-sized blocks of K genes each
   - Reshape input scRNA-seq `Y ∈ ℝ^(N×G)` into `X ∈ ℝ^(N×L×K)` (default K=3200)

2. **VAE with Gene Block Attention**
   - Linear projection `W_in` lifts each block to e-dim hidden, then standard pre-LN Transformer blocks (attention + FFN over the L block tokens)
   - Encoder outputs `μ, σ²` for `N×L×d` Gaussian latent; KL penalty against `N(0,1)`
   - Reparameterization trick + decoder mirrors encoder; reconstruction loss `−log L(X̂|X)`

3. **Conditional Flow Matching network**
   - Conditions `S ∈ ℝ^(N×d_s)` → learned embeddings `S_E ∈ ℝ^(N×d_s×e)`
   - **AdaLN**: `α₁,β₁,γ₁,α₂,β₂,γ₂ = S_E W_S`; `AdaLN(h,γ,β) = γ·(h−μ)/√(σ²+ε) + β`; gates each Attention/FFN sub-layer
   - **Affine path**: `xₜ = (1−t)x₀ + t·x₁`, target velocity `uₜ = x₁ − x₀` (constant along path)
   - **Loss**: `L_FM = 𝔼[‖v_θ(xₜ,t,s) − uₜ‖²]`
   - **Inference**: solve ODE `dxₜ/dt = v_θ(xₜ,t,s)` from t=0→1
   - **Classifier-Free Guidance**: `v̂ = (1−w)·v_θ(xₜ,t) + w·v_θ(xₜ,t,s)`

### Training
- Preprocessing: 10⁴-count normalize → log-transform → max-abs scale to [0,1]
- AdamW, lr=1e-4, weight decay=2.5e-5; condition mask ratio p=0.6
- Single RTX 3090 24GB GPU; same hyperparameters across all experiments

## 4. Key Results & Benchmarks

### Conditional generation (Wasserstein Distance ↓, MMD ↓)
| Setting | Best baseline | SAVE |
|---|---|---|
| **Single-cond Dentate Gyrus** | scDiffusion WD=22.56 / MMD=1.22 | **WD=9.16 / MMD=0.17** (>2× reduction) |
| **Tabula Muris MMD** | CFGen 0.19 | **0.04** |
| **Dual-cond Heart** | CFGen WD=12.57 | **WD=8.30** |
| **Dual-cond PBMC** | scDiffusion WD=11.38 | **WD=5.37** |
| **Dual-cond Lung Atlas** | scDiffusion WD=13.89 | **WD=4.37** |
| **5-cond Lung Cancer (unseen)** | scDiffusion WD=5.29 | **WD=4.63±0.95** |

### Batch effect correction (scIB score)
- **SAVE wins on all 3 datasets**: Lung Atlas 0.81, Heart 0.80, PBMC 0.83
- Beats Scanorama, Harmony, scVI, trVAE on biological conservation (top in 3/3) and batch correction (top in 2/3)
- Harmony stays competitive (best on Heart batch); scVI weakest on bio conservation

### IFN-β drug perturbation prediction (PBMC-IFN dataset, Haber et al. 2017)
- SAVE predictions of stimulated cells most closely match real perturbed distribution (UMAP overlap)
- Outperforms scGEN, trVAE, scDisInFact on differentially-expressed gene distributions (e.g., ISG15, TNFSF10)
- scGEN is competitive runner-up

### Ablation insights (mentioned, full table in appendix)
- Gene Block Attention vs flat-gene transformer: significant gain
- Condition masking (p=0.6) crucial for unseen-condition extrapolation
- LFM (latent flow matching) > diffusion for stability + speed at this scale

## 5. Limitations & Future Work
- **Gene block size K is fixed** (K=3200) per dataset — not learned, not adaptive to gene set sizes
- **NCBI summaries required**: depends on English-language gene annotations; unannotated genes are awkward
- **Per-dataset training**: not a foundation model — must retrain on new datasets, unlike scGPT/scFoundation
- **Single modality**: scRNA-seq only; no spatial, ATAC, or protein integration
- **Limited perturbation evaluation**: only one drug (IFN-β on PBMC) shown; no genetic perturbation, no chemCPA-style screens
- **Combinatorial held-out tested narrowly**: 27-type Lung Cancer with 2 unseen — no GEARS-style 0/1/2 train→test generalization curves
- **Not interpretable at gene level**: block-level attention ≠ per-gene mechanism

## 6. Related Work (in this wiki)
- **scVI** ([[single-cell-dl/lopez-2018-deep-generative-modeling-for]]) — VAE+ZINB foundation that SAVE benchmarks against
- **scGPT** ([[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]]) — flat-gene tokenization that SAVE explicitly criticizes
- **scFoundation** ([[single-cell-foundation/hao-2024-large-scale-foundation-model]]) — special-token zero-handling alternative
- **Squidiff** ([[single-cell-dl/he-2026-squidiff-predicting-cellular-development]]) — closest philosophical sibling: conditional diffusion for scRNA-seq generation
- **PerturbNet** ([[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]]) — distributional perturbation prediction with cINN
- **GEARS** ([[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]]) — combinatorial perturbation prediction
- **Harmony** ([[single-cell-dl/korsunsky-2019-fast-sensitive-and-accurate]]) — batch correction baseline
- **scArches** ([[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]]) — reference mapping
- **scIB** ([[single-cell-dl/luecken-2022-benchmarking-atlas-level-data]]) — integration benchmark used in §4.3

## 7. Glossary
- **Gene Block**: a non-overlapping cluster of K functionally similar genes, used as a coarse Transformer token in place of individual genes.
- **Optimal Transport (OT) clustering**: balanced k-means variant where the transport plan T enforces equal-sized clusters via uniform marginal constraints (`T·1_L = a, T^T·1_G = b`).
- **Flow Matching (FM)**: alternative to diffusion that regresses an instantaneous velocity field along a deterministic probability path between prior and data; affine path = linear interpolation `xₜ = (1−t)x₀ + tx₁`, target `uₜ = x₁ − x₀`.
- **AdaLN (Adaptive Layer Normalization)**: replaces fixed γ,β in LayerNorm with condition-derived learnable scale/shift; standard mechanism in conditional DiT/diffusion transformers.
- **Classifier-Free Guidance (w)**: inference-time interpolation between conditional and unconditional velocity field; trades sample diversity for fidelity to condition.
- **WD (Wasserstein Distance)**: earth-mover distance between generated and real cell distributions in (typically PCA) space; lower = more accurate.
- **MMD (Maximum Mean Discrepancy)**: kernel-based distributional distance; measures alignment of distribution moments.
- **scIB**: integration benchmark combining biological conservation (Bio.) and batch mixing (Batch) scores; standard for batch correction evaluation.
