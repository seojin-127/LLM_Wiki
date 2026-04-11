---
title: "Squidiff: predicting cellular development and responses to perturbations using a diffusion model"
authors: Siyu He, Yuefei Zhu, Daniel Naveed Tavakol, Haotian Ye, Yeh-Hsing Lao, Zixian Zhu, Cong Xu, Shradha Chauhan, Guy Garty, Raju Tomer, Gordana Vunjak-Novakovic, James Zou, Elham Azizi, Kam W. Leong
year: 2026
doi: 10.1038/s41592-025-02877-y
category: single-cell-dl
pdf_path: papers/he-2026-squidiff-predicting-cellular-development.pdf
pdf_filename: he-2026-squidiff-predicting-cellular-development.pdf
source_collection: downloads-perturb-batch
---

## One-line Summary

Squidiff is a conditional denoising diffusion model (DDIM) for single-cell transcriptomes that predicts future cell states, drug responses, and gene perturbations by manipulating a semantic latent space — capturing transient intermediate states that VAE/GNN/LLM-based perturbation models (scGen, GEARS, GenePert) miss.

## 1. Document Info
- Journal: Nature Methods, Vol 23, Jan 2026, 65-77
- Published online: 3 November 2025

## 2. Key Contributions

- First diffusion-model framework for single-cell perturbation and differentiation prediction. Prior diffusion models for scRNA-seq (scDiffusion, scVAEDer, scDiff) focused on generation, not perturbation.
- Semantic latent space `z_sem` lets users steer cell states by addition (`z_sem + Δz_sem`) or interpolation between states.
- Explicitly predicts transient intermediate states — a weakness of VAE-based methods that produce blurry interpolations.
- Applied to blood vessel organoid development under neutron irradiation + G-CSF protection — a real wet-lab validation loop including experimental scRNA-seq of irradiated BVOs.
- Handles three task classes in one framework: differentiation, gene perturbation, drug response.

## 3. Methods & Architecture

- **Diffusion autoencoder**: semantic encoder → `z_sem`, conditional DDIM decoder → reconstructs / generates scRNA-seq profiles.
- **Training**: forward process adds Gaussian noise over T=1000 steps; reverse process denoises, conditioned on `z_sem`.
- **Generation**: start from Gaussian noise + target `z_sem` → sample new transcriptomes.
- **Perturbation**: apply a direction vector `Δz_sem` in semantic space → denoised output reflects the perturbed state.
- **Interpolation**: linear path between two `z_sem` vectors → continuous time-course generation.

## 4. Key Results & Benchmarks

- Synthetic Splatter scRNA-seq: reconstructs known ground truth after forward+reverse diffusion.
- iPSC → three germ layer differentiation: captures transient states that scGen and scVIDR miss.
- Gene perturbation: outperforms GEARS and GenePert on nonadditive effects (combinations).
- Drug response: glioblastoma and melanoma cells with new drug combinations; predicts cell-type-specific responses.
- Blood vessel organoids + neutron irradiation: predicts mural-to-endothelial trajectory (consistent with recent time-series); predicts G-CSF radioprotective effect via vascular specification; validated with experimental scRNA-seq.

## 5. Limitations & Future Work

- Computationally expensive (diffusion denoising over many steps).
- Semantic latent direction `Δz_sem` requires examples of the perturbed state to learn direction — not fully zero-shot for novel perturbations.
- No explicit causal structure; predictions are pattern-learning in latent space, not mechanistic.
- Diffusion sampling stochasticity complicates reproducibility of per-cell predictions.

## 6. Related Work

- scGen, scVIDR (VAE), CellOT (OT), GEARS (GNN), GenePert (LLM) — prior perturbation prediction methods Squidiff compares to.
- scDiffusion, scVAEDer, scDiff — earlier single-cell diffusion models for generation.
- CellOracle, scGPT perturbation — alternative in silico perturbation paradigms.

## 7. Glossary

- **DDIM**: Denoising Diffusion Implicit Model — deterministic variant of DDPM sampling.
- **Semantic latent**: `z_sem`, a learned embedding that controls the content of diffusion-generated samples.
- **Latent manipulation**: adding a direction vector or interpolating in latent space to produce controlled outputs.
- **Forward diffusion**: progressive Gaussian noise addition over T steps.
