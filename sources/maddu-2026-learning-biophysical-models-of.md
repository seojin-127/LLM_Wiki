---
title: "Learning biophysical models of gene regulation with probability flow matching"
authors: Suryanarayana Maddu, Victor Chardès, Michael J. Shelley
year: 2026
arxiv: 2604.25062
category: single-cell-dl
pdf_path: papers/maddu-2026-learning-biophysical-models-of.pdf
pdf_filename: maddu-2026-learning-biophysical-models-of.pdf
source_collection: arxiv-q-bio.MN
---

## One-line Summary

PFM (Flatiron / Shelley group) is a simulation-free Flow Matching framework that learns **biophysically-constrained stochastic gene-regulatory dynamics directly in gene space** from cross-sectional scRNA-seq snapshots, recovering mechanism (production/degradation rates, lineage decisions) where latent-space FM/OT methods stay descriptive.

## 1. Document Info

- Venue: arXiv:2604.25062 [q-bio.MN], 2026-04-27
- Affiliations: Flatiron Institute Center for Computational Biology; Harvard MCB; Courant Institute (NYU)
- Code: https://vchz.github.io/pfi/
- Data: https://zenodo.org/records/19237708
- Group: Michael Shelley lab (Flatiron CCB) — applied math / biophysics; continuation of their PFI line (Maddu et al., previous work, ref [29])

## 2. Key Contributions

1. **Probability Flow Matching (PFM)** — extends Flow Matching to multi-marginal time-resolved single-cell data via the Fokker–Planck → Probability Flow ODE recasting, parameterizing both **drift** `f(x)` and **diffusion** `D(x)` rather than just a transport vector field.
2. **Gene-space, biophysically-constrained parameterization** — uses the coarse-grained transcription model `dx = (h(x) − ℓx)dt + √(h(x) + ℓx) dw` (production `h(x)` minus first-order degradation `ℓx`, with intrinsic Poisson-like noise via the `+ℓx` diffusion term). This is a **chemical Langevin** form, not a generic neural ODE.
3. **Chebyshev conditional paths** — replaces the standard Brownian-bridge / linear interpolant of FM with **globally-smooth Chebyshev polynomial** mean paths between marginals; avoids piecewise-constant velocity discontinuities at observed time points and converges faster than cubic splines.
4. **Unbalanced (growth-aware) extension** — auxiliary mass density `m_t(x)` is folded into the CFM loss, enabling joint inference of cell-state-specific proliferation and death rates.
5. **Empirical claim**: models with similar **interpolation accuracy** can encode **fundamentally different dynamics** — only the biophysically-consistent formulation correctly recovers lineage transitions, fate specification, and **gene-perturbation** responses on three hematopoiesis datasets.

## 3. Methods & Architecture

### Setup

Given K cross-sectional scRNA-seq snapshots `{p_{t_k}(x)}` at times `t_0 < … < t_{K-1}` where `x ∈ ℝ^G` is the transcriptional state. Goal: infer the latent SDE that interpolates these marginals.

### Theoretical core

Fokker–Planck equation for the time-evolving density (with growth term `g_t`):

```
∂p_t/∂t = −∇·(u_t(x) p_t(x)) + g_t(x) p_t(x)
u_t(x) = f(x) − ∇·D(x) − D(x) ∇log p_t(x)
```

`u_t(x)` is the right-hand side of the **Probability Flow ODE** (Song et al. 2021), obtained by recasting the FP equation in Lagrangian coordinates. The score `∇log p_t(x)` is what couples deterministic transport to the stochastic SDE.

### Algorithm — three steps

1. **Estimate score** `∇log p_t(x)` from snapshots independently (denoising score matching, [54, 63]); avoids the identifiability issues of jointly training score + drift + diffusion.
2. **Construct smooth conditional paths** `p_t(x|z) = N(x | Q_t(z), σ²)` where `Q_t` is a **Chebyshev polynomial interpolant** through the multi-marginal samples; conditioning variable `z ~ q(z)` set to the multi-marginal optimal-transport coupling `π*`.
3. **Regress velocity** by minimizing the unbalanced Conditional FM loss:

```
L_CFM = E_{t, q(z), p_t(x|z)} [ (m_t(z)/M_t) · ‖ u_t(x|z) − u_θ(x) ‖² ]
```

where `M_t = ∫ p_t(x) dx` is total cell abundance.

### Biophysical drift / diffusion

Coarse-grained transcription model:

```
dx = ( h(x) − ℓ x ) dt + diag( h(x) + ℓ x )^(1/2) dw
```

- `h(x)`: regulatory dynamics (production rate, function of TF activity / chromatin state)
- `ℓ`: per-gene mRNA degradation rate
- Diffusion `D(x) = diag(h(x) + ℓx)` reflects **intrinsic transcriptional noise** (sum of birth + death events under chemical Langevin approximation), not a tunable scalar.

Special cases the FP framework recovers:
- `D(x) = 0` + time-dependent drift → **TrajectoryNet** [34], **TIGON** [62] (deterministic OT-based)
- Conservative `f(x) = −∇φ(x)` + isotropic `D` → **PRESCIENT** [42]
- The biophysical SDE above → PFM

### Engineering wins vs prior PFI

- Simulation-free training (no ODE solves inside the loop)
- Chebyshev quadrature for the regression integral → order-of-magnitude speed/memory reduction over PFI [29]
- Score estimated separately, avoiding the drift–score identifiability collapse

### Hematopoiesis applications

Three datasets used:
- 10X Chromium v1 induced human CD34+ HSPC differentiation [57]
- CITE-seq induced human CD34+ HSPC differentiation [67]
- LARRY-barcoded mouse HSPC differentiation [13]

For TF inference: filter to ~24 TFs that have statistically lower counts than non-TF gene sets (one-sided permutation p-value), with the caveat that ubiquitously-expressed TFs like BTF3, ENO1, NPM1, PTMA, YBX1, HMG-family must be discarded.

## 4. Key Results & Benchmarks

- **Interpolation ≠ mechanism**: deterministic and biophysical PFM models can hit similar interpolation RMSE on snapshot reconstruction but encode different dynamics — only the biophysical model recovers lineage transitions and fate decisions on hematopoiesis.
- **Cross-experiment generalization**: model trained on the 10X Chromium v3 dataset transfers to CITE-seq with cell-type-paired Pearson correlations preserved (validated by OT-matched pairs of cells across experiments).
- **Out-of-distribution initial conditions**: gene-space (vs latent-space) parameterization lets PFM predict trajectories from unseen starting transcriptomes — claimed to be the bottleneck for in-silico perturbation.
- **Unbalanced inference**: on the in-vitro LARRY hematopoiesis dataset, PFM predicts cell-state-specific growth dynamics jointly with the regulatory drift — useful for population-level changes that pure-OT methods miss.
- **Chebyshev > spline > linear**: on a 2D Ornstein–Uhlenbeck benchmark, Chebyshev path interpolation gives RMSE 0.1534 vs cubic spline 0.5897 in vector-field reconstruction.

## 5. Limitations & Future Work

- TF identifiability requires manually filtering out high-count "ubiquitous" TFs — heuristic and dataset-specific.
- Scale demonstrated on hematopoiesis (well-studied, low-dimensional fate landscape); behavior on truly high-G systems with weak signals is open.
- The biophysical form `dx = (h − ℓx)dt + √(h + ℓx)dw` is a **coarse-grained** model — collapses chromatin/protein layers into the production rate `h(x)`. Doesn't model mRNA splicing, nuclear/cytoplasmic compartments, etc.
- Score is estimated **per snapshot independently** — not enforced to be temporally consistent with the inferred dynamics.
- No comparison yet to neural-SDE methods that also learn diffusion (only to deterministic OT/FM and PRESCIENT-class models).

## 6. Related Work

- **Standard Flow Matching**: Lipman et al. 2023 [43], Tong et al. 2024 [44] — base distribution → target via simulation-free vector-field regression.
- **Optimal-Transport for single-cell trajectories**: Schiebinger 2019, TrajectoryNet [34], TIGON [62], Klein 2025 (entropic OT, brain) [from wiki]
- **PRESCIENT** [42] (Yeo et al. 2021) — conservative-force biophysical model with isotropic diffusion; PFM generalizes by lifting both constraints.
- **PFI** (previous Maddu et al.) [29] — first version of probability-flow inference; PFM removes simulation cost via FM + Chebyshev.
- **Cell2fate** (Aivazidis 2025), **monod** (Gorin 2025) — biophysical RNA velocity / chemical-master-equation models for mRNA dynamics from snapshot data.
- **SAVE** (Li 2026) — also uses Conditional Flow Matching for scRNA-seq, but in **VAE latent space** with classifier-free-guidance for conditions; complementary trade-off (scalable conditioning vs mechanistic interpretability).
- **Squidiff** (He 2026), **PerturbNet** (Yu 2025), **GEARS** (Roohani 2023) — perturbation-response prediction; PFM tackles the same goal but via mechanistic SDE rather than learned representation.

## 7. Glossary

- **Probability Flow ODE**: deterministic ODE `dx/dt = u_t(x) = f(x) − ∇·D(x) − D(x)∇log p_t(x)` whose marginal density at each `t` matches the marginal of the underlying SDE `dx = f(x)dt + G(x)dw`. Same trick used in score-based diffusion models (Song et al. 2021) for sampling.
- **Score function**: `∇_x log p_t(x)` — gradient of log-density, used to convert SDE → equivalent ODE that has the same marginals.
- **Conditional Flow Matching (CFM)**: training objective regressing `u_θ(x)` against analytical conditional velocities `u_t(x|z)` along prescribed paths `p_t(x|z)` — bypasses the marginal velocity which is intractable.
- **Brownian bridge**: standard FM's choice of conditional path between two endpoints; PFM replaces it with a Chebyshev-polynomial mean path for K>2 marginals.
- **Chebyshev polynomial interpolation**: globally smooth, near-minimax polynomial fit; superior convergence to local cubic splines, no Runge phenomenon.
- **Multi-marginal optimal transport coupling π***: joint distribution over `(x_{t_0}, …, x_{t_{K-1}})` whose marginals match observed snapshots and minimizes a transport cost — used as `q(z)` in CFM.
- **Unbalanced FM**: extension where total mass `M_t = ∫ p_t dx` need not be 1, allowing modeling of birth/death (proliferation, apoptosis).
- **Chemical Langevin equation**: SDE approximation of birth-death stochastic processes where diffusion equals √(rates), used here for `D = diag(h + ℓx)`.
- **Identifiability collapse**: when score, drift, and diffusion are jointly trained, errors in score get absorbed into the wrong term — PFM avoids by estimating score independently first.
