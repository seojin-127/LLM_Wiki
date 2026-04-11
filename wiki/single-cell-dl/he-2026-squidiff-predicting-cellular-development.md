---
title: "Squidiff: predicting cellular development and responses to perturbations using a diffusion model"
authors: Siyu He, Yuefei Zhu, Daniel Naveed Tavakol, Haotian Ye, Yeh-Hsing Lao, Zixian Zhu, Cong Xu, Shradha Chauhan, Guy Garty, Raju Tomer, Gordana Vunjak-Novakovic, James Zou, Elham Azizi, Kam W. Leong
year: 2026
doi: 10.1038/s41592-025-02877-y
source: he-2026-squidiff-predicting-cellular-development.md
category: single-cell-dl
tags: [diffusion-model, perturbation-prediction, drug-response, cell-differentiation, generative-model, latent-manipulation, organoid]
---

## Summary

Squidiff is a conditional denoising diffusion model that predicts single-cell transcriptomic changes under cell-state transitions: differentiation, gene perturbation, or drug treatment. It learns a semantic latent `z_sem` via a diffusion autoencoder and generates new cell profiles by denoising Gaussian noise conditioned on a manipulated `z_sem`. Latent addition (`+Δz_sem`) encodes a perturbation direction; linear interpolation produces time-course trajectories. Compared to VAE- and GNN-based perturbation models (scGen, GEARS, GenePert), it better captures transient intermediate states that smoother decoders blur.

## Key Contributions

- First diffusion model applied to single-cell *perturbation* rather than just generation.
- A single framework handles differentiation, gene perturbation, and drug response prediction.
- Captures transient intermediate states that VAE/GNN models miss — a direct consequence of diffusion's iterative denoising vs. a single-shot decoder.
- Wet-lab validation loop: predicted + experimentally confirmed neutron-irradiation effects and G-CSF radioprotection in blood vessel organoids.

## Methods & Architecture

- **Diffusion autoencoder** (Preechakul et al. 2022 adapted): semantic encoder maps scRNA-seq → `z_sem`; conditional DDIM decoder reconstructs gene expression by reverse denoising Gaussian noise `x_T` conditioned on `z_sem`.
- **Training loss**: standard DDIM denoising objective + reconstruction.
- **Generation modes**:
  - **Addition**: `z_sem' = z_sem + Δz_sem`, where `Δz_sem` is estimated from paired perturbed/unperturbed examples.
  - **Interpolation**: linear path `(1-t)·z_A + t·z_B` → continuous trajectory of transcriptomes between states A and B.
- **Input**: preprocessed scRNA-seq counts; optional conditioning on drug chemical structure and dose.

## Results

- **Synthetic (Splatter)**: perfect reconstruction after forward+reverse diffusion; latent space separates simulated cell types.
- **iPSC → three germ layers**: generates differentiation trajectories guided by stimulus vectors; captures transient states scGen and scVIDR miss.
- **Gene perturbation**: outperforms GEARS and GenePert on nonadditive perturbation effects.
- **Drug combinations**: glioblastoma and melanoma cell-type-specific responses predicted for new combinations.
- **Blood vessel organoids under neutron irradiation**: predicts mural→endothelial pathway; predicts G-CSF's vascular-specification radioprotective effect; experimentally validated with scRNA-seq of irradiated BVOs ± G-CSF.

## Limitations

- Expensive: iterative denoising across many steps.
- Not fully zero-shot: `Δz_sem` must be learned from seen perturbation examples.
- Pattern-learning in latent space, not causal mechanism — does not tell you *why* a perturbation moves cells.
- Diffusion sampling stochasticity means per-cell predictions are noisy and require averaging.

## Related Papers

- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle, alternative causal-mechanistic perturbation simulation
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT perturbation task; foundation model alternative
- [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]] — PerturBERT, BERT-style perturbation signatures
- [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] — scVI VAE ancestor of generative scRNA-seq modeling
- [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] — TRADE, statistical framework for grading perturbation predictions
- [[drug-resistance/antonopoulos-2026-zero-shot-prediction-of-drug]] — LEMBAS zero-shot drug response; alternative paradigm
