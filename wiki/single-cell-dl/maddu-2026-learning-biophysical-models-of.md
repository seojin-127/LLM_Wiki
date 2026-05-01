---
title: "Learning biophysical models of gene regulation with probability flow matching"
authors: Suryanarayana Maddu, Victor Chardès, Michael J. Shelley
year: 2026
arxiv: 2604.25062
source: maddu-2026-learning-biophysical-models-of.md
category: single-cell-dl
tags: [flow-matching, probability-flow-ode, biophysical-model, sde, gene-regulatory-network, hematopoiesis, perturbation-prediction, fokker-planck, chebyshev, unbalanced-ot, mechanistic-interpretability, flatiron, shelley-lab]
---

## Summary

PFM (Maddu, Chardès, Shelley — Flatiron Institute) extends Flow Matching to **multi-marginal time-resolved scRNA-seq** by parameterizing both **drift** `f(x)` and **diffusion** `D(x)` of a stochastic process directly in **gene space**, with the diffusion term tied to the **chemical Langevin** form `D = diag(h + ℓx)` so that the noise is biophysical (Poisson birth-death) rather than a free scalar. The key empirical claim is that **interpolation accuracy is not a sufficient diagnostic** — multiple parameterizations match the snapshot data equally well but encode fundamentally different dynamics, and only the biophysically-consistent one recovers lineage decisions and gene-perturbation responses on hematopoiesis. Two engineering pieces make the framework practical: (1) **Chebyshev polynomial mean paths** between marginals (avoiding piecewise-constant velocity artifacts of linear interpolants), and (2) **unbalanced** CFM via an auxiliary mass density that absorbs proliferation/death.

## Why this paper matters here

PFM sits at the **mechanistic** end of the [[overviews/perturbation-prediction-and-causal-inference|perturbation-prediction landscape]]. Compared to [[single-cell-dl/li-2026-save-a-generalizable-framework|SAVE]], which also uses Conditional Flow Matching for scRNA-seq:

| Axis | SAVE (Li 2026) | PFM (Maddu 2026) |
|------|----------------|------------------|
| Where FM operates | VAE **latent space** | **Gene space** directly |
| Conditioning | AdaLN + classifier-free guidance over batch/cell-type/drug | None — perturbation = changing the SDE drift |
| Drift `f(x)` | Generic neural net (no biology) | Biophysical: production `h(x)` − degradation `ℓx` |
| Diffusion `D(x)` | Implicit (FM noise schedule) | **Explicitly parameterized**, chemical Langevin |
| Out-of-distribution initial conditions | Limited (manifold-constrained) | Designed for it (no latent projection) |
| Intended use | Scale up multi-condition generation | Mechanistic understanding + in-silico perturbation |

These are not competitors — they answer different questions. SAVE: "given lots of conditions, generate held-out combinations." PFM: "given time-resolved snapshots, recover the underlying regulatory SDE."

## Methods & Architecture

### Theoretical core

Single-cell snapshots `{p_{t_k}(x)}_k` are samples from the time-evolving density of a Fokker–Planck equation:

```
∂p_t/∂t = −∇·(u_t(x) p_t(x)) + g_t(x) p_t(x)
u_t(x) = f(x) − ∇·D(x) − D(x) ∇log p_t(x)
```

The velocity field `u_t(x)` is the **Probability Flow ODE** (Song et al. 2021): a deterministic ODE whose marginals exactly match the underlying SDE's marginals. Many existing methods are special cases:

- `D(x) = 0`, time-dependent drift → TrajectoryNet, TIGON
- Conservative `f(x) = −∇φ(x)`, isotropic `D` → PRESCIENT
- Biophysical `f`, state-dependent `D` → **PFM**

### The biophysical SDE

```
dx = ( h(x) − ℓ x ) dt  +  diag( h(x) + ℓ x )^(1/2) dw
```

- `h(x)`: gene-regulatory **production** rate (function of TFs, chromatin)
- `ℓ`: per-gene mRNA **degradation** rate
- Diffusion = `√(production + degradation)` → intrinsic transcriptional noise from the chemical Langevin approximation, not a tunable hyperparameter

### Algorithm — three steps

1. **Estimate the score** `∇log p_t(x)` independently per snapshot via denoising score matching. Estimating it jointly with drift+diffusion creates an **identifiability collapse** (errors absorbed into wrong term).
2. **Construct conditional paths** `p_t(x|z) = N(x | Q_t(z), σ²)` where `Q_t` is a **Chebyshev polynomial** through the multi-marginal samples; `z ~ q(z)` set to the multi-marginal **OT coupling π***.
3. **Regress velocity** by minimizing the unbalanced Conditional FM loss

```
L_CFM = E_{t, q(z), p_t(x|z)} [ (m_t(z)/M_t) · ‖ u_t(x|z) − u_θ(x) ‖² ]
```

where `m_t(x)` is an auxiliary mass density that captures cell-state-specific birth/death.

### Why Chebyshev paths

Linear interpolation of mean paths between observed marginals produces **piecewise-constant velocities** with discontinuities at the data points. Stochastic gene-regulatory dynamics should be smooth; those discontinuities corrupt the regressed `u_θ`. Chebyshev polynomials give globally smooth time derivatives with near-minimax error, and beat cubic splines empirically (RMSE 0.15 vs 0.59 on a 2D Ornstein-Uhlenbeck benchmark).

## Results

- **Order-of-magnitude speed/memory** improvement over the previous PFI [29] (their own prior method), via simulation-free training + Chebyshev quadrature.
- **Three hematopoiesis datasets** (10X v1, CITE-seq, LARRY): biophysical PFM recovers lineage transitions and TF interactions consistent with known hematopoietic biology; deterministic baselines with similar interpolation RMSE do not.
- **Cross-experiment transfer**: model trained on 10X Chromium v3 generalizes to CITE-seq with cell-type-paired Pearson correlations preserved (validated by OT-matched cells).
- **Out-of-distribution initial conditions**: gene-space parameterization enables predicting trajectories from unseen starting transcriptomes — bottleneck for in-silico perturbation that latent-space methods can't address.
- **Unbalanced inference**: on the LARRY in-vitro dataset, simultaneously fits cell-state-specific proliferation and death rates alongside the regulatory drift.

## Limitations

- TF identifiability requires manually filtering "ubiquitous" high-count TFs (BTF3, ENO1, NPM1, PTMA, YBX1, HMG-family) — heuristic.
- Biophysical model is **coarse-grained**: production rate `h(x)` lumps chromatin accessibility, TF binding, polymerase recruitment into one function. No splicing, no nuclear/cytoplasmic split.
- Score is estimated **per-snapshot independently**, not jointly with the dynamics — convenient for identifiability but loses temporal coupling.
- Demonstrated on hematopoiesis (well-characterized, ~moderate dimensionality). Behavior on weaker-signal, higher-G systems (whole-organ atlases, perturbation screens) is open.
- No comparison yet against neural-SDE methods that also parameterize diffusion.

## Related Papers

### Same family — Flow Matching / dynamics on scRNA-seq
- [[single-cell-dl/li-2026-save-a-generalizable-framework]] — Conditional Flow Matching in **VAE latent space** with classifier-free guidance; complementary scaling-vs-mechanism trade-off (see comparison table above).
- [[single-cell-dl/klein-2025-mapping-cells-through-time]] — entropic OT for trajectory inference; PFM generalizes by adding state-dependent diffusion and biophysical constraints.
- [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] — diffusion-model approach to cellular dynamics; both use score-based machinery but PFM ties it to a chemical Langevin SDE.

### Biophysical / mechanistic single-cell models
- [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna]] — biophysical RNA velocity; same spirit (mechanistic mRNA dynamics) at the per-gene level.
- [[single-cell-dl/gorin-2025-monod-model-based-discovery]] — chemical-master-equation framework for mRNA distributions.

### Perturbation prediction
- [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] — GEARS, GNN over GO graph for perturbation prediction.
- [[overviews/perturbation-prediction-and-causal-inference]] — landscape; PFM is a **mechanistic SDE** entry vs the latent-space generative entries.
- [[overviews/six-open-issues-perturbation-modelling]] — Dimitrov 2026 review; PFM directly addresses the "interpretation vs interpolation" issue.

### Concept pages
- [[concepts/models-as-distribution-learners]] — generative models as samplers from `p(data | conditions)`; PFM is the "physics-constrained" instantiation.
- [[concepts/distributional-vs-point-prediction]] — PFM produces full SDE → trajectory distribution, not point predictions.
- [[concepts/cell-level-counterfactual]] — PFM enables counterfactual trajectories by changing `h(x)` (perturbing TFs in the drift).
- [[concepts/interpolation-vs-extrapolation]] — central to this paper's headline claim: interpolation accuracy ≠ correct dynamics.
- [[concepts/expressivity-interpretability-tradeoff]] — PFM trades neural-net expressivity in the drift for mechanistic readability.
