---
title: "Expressivity vs Interpretability Tradeoff in Single-Cell DL"
type: concept
created: 2026-04-25
category: concepts
tags: [interpretability, expressivity, linear-decoder, attention, knowledge-mask, causal-graph, attribution, in-silico-perturbation]
used_in:
  - single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of
  - single-cell-dl/lopez-2018-deep-generative-modeling-for
  - single-cell-dl/kamimoto-2023-dissecting-cell-identity-via
  - single-cell-foundation/cui-2024-scgpt-toward-building-foundation
---

## The Core Dilemma

Single-cell biology requires capturing nonlinear, multi-scale dynamics (feedback, saturation, threshold effects). But the same nonlinearity that gives expressive power destroys interpretability — predictions become opaque, and "why this prediction?" becomes hard to answer.

```
LINEAR models                        NONLINEAR (deep learning) models
─────────────────────────────        ─────────────────────────────────
+ Each weight has direct meaning     + Capture feedback/saturation/threshold
+ Surprisingly competitive baselines + Can match complex nonlinear systems
+ Attribution is trivial             - Predictions are opaque
- Cannot capture nonlinearity        - Cannot directly attribute to genes
- Threshold/saturation invisible     - Need post-hoc methods to interpret
                                                                       
Examples: Mixscale, MOFA+, GSFA,     Examples: scVI, scGPT, GEARS, CPA,
          scGEN (latent arithmetic)            CellOracle (partial)
```

This tradeoff is structural — you cannot simply "have both" without explicit architectural choices.

## Five Strategies to Balance the Tradeoff

| Strategy | Mechanism | Examples |
|----------|-----------|----------|
| **Nonlinear encoder + linear decoder** | Compression is nonlinear (expressive); reconstruction is linear (interpretable) | scVI ([[single-cell-dl/lopez-2018-deep-generative-modeling-for]]), OntoVAE, NicheCompass, ExpiMap |
| **Knowledge-masked latents** | Force latent factors to correspond to known pathways via binary masks | Spectra, ExpiMap, VEGA, scDoRI |
| **Attention as interpretation** | Read attention weights as TF→target proxy | scGPT ([[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]]), scPRINT |
| **Causal graph + neural net** | Explicit DAG (interpretable) + nonlinear conditional functions | Bicycle, NOTEARS-MLP, DCDI |
| **Post-hoc attribution** | Apply interpretability methods on top of any black-box model | DeepLIFT, Integrated Gradients, SHAP |

The first strategy (linear decoder) is the most popular in single-cell because it's architecturally simple and gives gene-level attribution.

## How Current Models "Explain" A Perturb → B Cell State

Different model families give **different kinds** of answers to "why does perturbing A cause cell state B?":

| Model class | What it can say | Mechanism level |
|-------------|----------------|-----------------|
| **CellOracle** ([[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]]) | "A regulates TFs C, D in the inferred GRN; perturbing A propagates through GRN to shift state vector toward B" | **Mechanistic** (GRN-based) |
| **scGEN / latent arithmetic** | "The mean control→perturbed direction in latent space points toward B" | **Direction only**, no mechanism |
| **CPA / Biolord** | "A's perturbation embedding composes with context embedding to produce a latent close to B" | **Compositional**, opaque mechanism |
| **scGPT** (in silico edit) | "Silencing A's token in the transformer input produces output closer to B" | **Black box**, post-hoc attention |
| **GEARS** ([[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]]) | "A's GO/coexpression neighbors shift expression toward B via GNN message passing" | **Partial mechanism** via prior |

## The Key Honest Observation

**No current model gives a true mechanistic causal explanation** in the sense of "perturbing A causes B because A → C → D → B with these specific kinetics".

- Models predict **effects**, but rarely the **causal chain** that produces them
- CellOracle is closest because it has an explicit GRN, but the GRN itself is inferred from data and may be wrong
- Foundation models (scGPT) trade mechanistic transparency for predictive flexibility
- This is exactly the gap [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] flags as "mechanistic discovery often fails to recover known regulators"

> The tension: prediction accuracy and mechanistic explanation are not the same thing, and improving one does not automatically improve the other.

## In Silico Perturbation (How Models Simulate Interventions)

Different strategies for simulating "what if we perturbed gene A":

```
GRN-based (CellOracle, SCENIC+):
  Set A's expression = 0 in the GRN model
  → propagate through inferred network
  → read out shifted state vector
  
  Pro: mechanistic, interpretable
  Con: only as good as the GRN

Latent arithmetic (scGEN):
  z_perturbed = z_control + perturb_direction_vector
  → decode z_perturbed
  
  Pro: simple, model-agnostic
  Con: assumes linear additivity in latent space

In silico token edit (scGPT, scFoundation):
  Replace A's token with mask/zero
  → forward pass transformer
  → read decoded expression
  
  Pro: leverages large pretrained model
  Con: black box; what is being "perturbed" is unclear

Causal graph intervention (NOTEARS-style, Bicycle):
  do(A = 0) on the inferred causal DAG
  → recompute downstream conditionals
  
  Pro: principled (Pearl do-operator)
  Con: requires correct DAG; assumption-heavy
```

Choice between these is not just technical — it determines *what kind of biological claim* the model can make.

## Practical Reading Tip

When a paper claims "perturbing X causes Y":

1. **Ask what mechanism the model assumes.** GRN? Latent arithmetic? Black-box transformer? Each makes different assumptions.
2. **Check if the claim is a prediction or a mechanistic hypothesis.** "We predicted the effect" vs "we identified the causal chain" are very different claims.
3. **Look for validation.** Computational predictions need experimental confirmation, especially for novel mechanisms.

## Connection to Other Concepts

- [[concepts/interpolation-vs-extrapolation]] — interpretability often degrades faster than predictive accuracy in extrapolation
- [[concepts/perturbation-evaluation-design]] — interpretability is rarely benchmarked formally, unlike prediction accuracy
- [[concepts/combinatorial-perturbation-prediction]] — combinatorial prediction is where the tradeoff bites hardest
- [[concepts/multimodal-temporal-readout]] — multimodal data can help mechanistic interpretation by providing intermediate causal layers

---

*Used in: [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] (review's central tension between prediction and mechanism), [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] (scVI uses linear decoder for interpretability), [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] (CellOracle: GRN-based mechanistic), [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] (scGPT: attention as interpretation)*
