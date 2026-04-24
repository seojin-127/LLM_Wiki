---
title: "Variational Autoencoder (VAE)"
type: concept
created: 2026-04-24
category: concepts
tags: [VAE, generative-model, latent-space, representation-learning, deep-learning]
used_in:
  - single-cell-dl/lopez-2018-deep-generative-modeling-for
  - single-cell-dl/xu-2021-probabilistic-harmonization-and
  - single-cell-dl/boyeau-2025-deep-generative-modeling-of
  - single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses
  - single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of
  - single-cell-dl/lotfollahi-2022-mapping-single-cell-data
  - single-cell-dl/dedonno-2023-population-level-integration-of
---

## What Is a VAE?

Variational Autoencoder (VAE) is a deep generative model that learns to **compress high-dimensional data into a smooth, low-dimensional latent space** and **generate new data** by sampling from that space. It consists of two neural networks: an encoder (compresses) and a decoder (reconstructs).

## Architecture

```
Input x (high-dimensional)
  ↓
┌─────────┐
│ Encoder │ → outputs μ (mean) and σ (variance)
└─────────┘
  ↓
z ~ N(μ, σ²)        ← sample from learned distribution (reparameterization trick)
  ↓
┌─────────┐
│ Decoder │ → reconstructs x̂
└─────────┘
  ↓
Output x̂ (high-dimensional)
```

## Why Not Just Use a Regular Autoencoder?

A regular autoencoder compresses data into a latent code, but that code is just a deterministic point — the latent space has no structure.

```
Regular AE latent space:           VAE latent space:

   *    *                           . . . . . .
       *   *                        . . . . . . .
   *        *                       . . . . . . .
      *                             . . . . . . .
          *  *                      . . . . . . .

(sparse, irregular)                (smooth, continuous)
```

The VAE forces z to follow a Gaussian distribution. This makes the latent space **continuous** — nearby points decode to similar outputs, and you can sample new points to generate new data.

## The Two Loss Terms

VAE training minimizes two losses simultaneously:

```
Total Loss = Reconstruction Loss + KL Divergence

             "How well can the          "How close is the learned
              decoder rebuild            distribution to a
              the original input?"       standard Gaussian?"
```

1. **Reconstruction loss**: ensures the compressed representation retains enough information to rebuild the input (makes z informative)
2. **KL divergence**: prevents the encoder from "cheating" by memorizing each data point as a unique code; forces z to stay close to N(0, I) (makes z smooth and generalizable)

The tension between these two terms is fundamental: too much reconstruction focus → latent space becomes irregular; too much KL → latent space is smooth but loses information.

## Why the Decoder Matters

A common question: if we only want the compressed representation (z), why do we need a decoder?

**During training**: the decoder is the "exam" — it tests whether the encoder's compression preserved enough information. Without the decoder, there is no training signal for the encoder.

**After training**: depends on the use case.

| Use case | Encoder needed? | Decoder needed? |
|----------|----------------|-----------------|
| Encode new data → latent vector | Yes | No |
| Generate new samples | No | Yes |
| Encode → manipulate → decode | Yes | Yes |

In biology:
- **scVI** ([[single-cell-dl/lopez-2018-deep-generative-modeling-for]]): uses both — encoder embeds cells, decoder reconstructs expression for imputation/DE
- **PerturbNet ChemicalVAE** ([[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]]): only encoder used after training (drug → z vector); decoder was only needed during training
- **PerturbNet Cell VAE**: both used — encoder embeds cells, decoder translates predicted z back to gene expression

## VAE Variants in This Wiki

### scVI (2018) — The Foundational Biology VAE
[[single-cell-dl/lopez-2018-deep-generative-modeling-for]]

```
Cell (gene counts) → Encoder → z (latent) → Decoder → reconstructed counts
                                  ↑
                           batch variable
                           injected here
                           (batch correction)
```

- Likelihood: Zero-Inflated Negative Binomial (ZINB) — models scRNA-seq count structure (overdispersion + dropouts)
- The z captures biological variation; batch effects are modeled separately
- Spawned an entire ecosystem: scANVI, scArches, scPoli, MrVI

### ChemicalVAE (PerturbNet)

```
Drug SMILES string → Conv Encoder → z → Sequence Decoder → reconstructed SMILES
     "CSCC(=O)NNC..."                           "CSCC(=O)NNC..."
```

- Trained on ~250K ZINC drug-like molecules
- Chemically similar drugs → nearby z vectors
- No biology involved — pure chemical structure learning

### GenotypeVAE (PerturbNet)

```
GO annotation vector → MLP Encoder → z → MLP Decoder → reconstructed annotations
  [0,1,1,0,...,1]                              [0,1,1,0,...,1]
  (15,988 dim)                                  (15,988 dim)
```

- Trained on ~177M single/double gene GO vectors
- Functionally similar genes → nearby z vectors

## VAE vs Other Generative Models

| Model | Latent space | Generation | Training stability |
|-------|-------------|------------|-------------------|
| **VAE** | Smooth, continuous | Sample z ~ N(0,I) → decode | Stable |
| **GAN** | No explicit latent | Generator vs discriminator | Unstable (mode collapse) |
| **Diffusion** | Noise schedule | Iterative denoising | Stable but slow |
| **Normalizing Flow** | Invertible transform | Exact likelihood | Stable, invertible |

## Key Intuition for Biology

VAE's smoothness property is why it dominates single-cell biology:

```
Cell A (neuron) ●                    ● Cell B (astrocyte)
                 \                  /
                  ● ● ● ● ● ● ● ●
                  (intermediate states)
```

In a well-trained VAE, the path between two cell types in latent space passes through biologically meaningful intermediate states. This is why:
- **scVI** can impute missing expression values (nearby z → similar expression)
- **scArches** can map new data onto existing references (smooth manifold transfer)
- **PerturbNet** can predict unseen perturbations (nearby z_drug → similar cell response)

---

*Used in: [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] (scVI), [[single-cell-dl/xu-2021-probabilistic-harmonization-and]] (scANVI), [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]] (MrVI), [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]] (scArches), [[single-cell-dl/dedonno-2023-population-level-integration-of]] (scPoli), [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] (PerturbNet), [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] (GEARS — minor use)*
