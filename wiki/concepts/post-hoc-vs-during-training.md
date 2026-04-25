---
title: "Post-hoc vs During Training: When Things Get Built Into a Model"
type: concept
created: 2026-04-25
category: concepts
tags: [post-hoc, during-training, attribution, interpretability, calibration, SHAP, LIME, vocabulary, methodology]
used_in:
  - single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of
  - single-cell-foundation/cui-2024-scgpt-toward-building-foundation
  - single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of
---

## Core Distinction

"Post-hoc" is Latin for *"after this"*. In machine learning, it means **"applied after the model is already trained"** — as opposed to **"during training"**, which means built into the model's optimization process itself.

```
   Model lifecycle:
   
   [Data prep] → [Training] ───→ [Trained model] → [Use / evaluate]
                     ↑                                     ↑
                during training                        post-hoc
                                                                    
              Things done HERE                       Things done HERE
              get baked into                         leave the model
              the model itself                       unchanged; only
                                                     analyze or adjust
```

The same goal (e.g., interpretability, knowledge integration, calibration) can be pursued at either stage — but the consequences are very different.

## Five Common Uses of "Post-hoc" in ML / Single-Cell Literature

### (1) Post-hoc interpretation / attribution

The most common usage. After training a black-box model, apply external methods to figure out which inputs mattered for which predictions.

| Tool | What it does |
|------|-------------|
| **SHAP** | Game-theoretic attribution of each input's contribution |
| **LIME** | Local linear approximation around a prediction |
| **Integrated Gradients** | Path integral of input perturbations |
| **DeepLIFT** | Compare to baseline contribution |
| **Attention visualization** | Read off transformer attention weights |
| **Saliency maps** | Gradient w.r.t. input |

> [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] explicitly: *"a common solution to estimate the importance of each feature is to apply **post hoc metrics** that quantify the contribution of each gene to the model's predictions"*

### (2) Post-hoc calibration

Adjusting a trained model's output probabilities to better reflect true confidence.

- **Temperature scaling**: divide output logits by a learned temperature
- **Platt scaling**: fit logistic regression on output → corrected probabilities
- **Isotonic regression**: monotonic mapping for calibration

Connects to [[concepts/uncertainty-quantification]] — calibration is one piece of UQ.

### (3) Post-hoc knowledge integration

Biological priors (GO terms, pathways, TF-target databases) applied AFTER the model is trained, rather than during training.

- **During training**: prior used as a regularization term, masked latent factor, GNN edge structure (e.g., GEARS uses GO graph IN training)
- **Post-hoc**: model trained without prior, then GO/pathway enrichment computed on outputs (e.g., compute pathway enrichment of a model's predicted DE genes)

> [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]]: *"this information being integrated either **during training** or **post hoc**"*

### (4) Post-hoc metric

Evaluating a model on something it wasn't trained to optimize.

Example: a foundation model trained for cell-type classification → evaluate post-hoc whether its embeddings happen to be useful for perturbation prediction. The model never saw perturbation data, but we test it as if it had.

### (5) Post-hoc model combination

Merging or stacking models that were independently trained.

Example: pretrained scGPT embedding + pretrained chemical SMILES embedding combined post-hoc to predict drug response. Neither model was trained to know about the other.

## Trade-offs: During Training vs Post-hoc

| Dimension | During training | Post-hoc |
|-----------|----------------|----------|
| **Effect on the model** | Model internalizes the constraint | Model unchanged; only analysis/adjustment outside |
| **Reliability** | Stronger (model genuinely learned it) | Weaker (external estimate of what model "really" did) |
| **Flexibility** | Once trained, hard to change | Can apply any post-hoc method to any pretrained model |
| **Compute cost** | Expensive (requires retraining) | Cheap |
| **Foundation-model compatibility** | Usually requires retraining | Easy — apply to existing pretrained models |
| **When you'd choose this** | When you know what you want from the start, willing to invest in training | When you're using existing models, want to interpret/extend them flexibly |

## The Honest Limitation of Post-hoc Methods

Post-hoc tools are convenient, but they have **known reliability issues** — analysts should be aware:

1. **Inconsistency across methods**: SHAP, LIME, Integrated Gradients applied to the same model often give *different* attributions for the same prediction.
2. **Faithfulness problem**: post-hoc explanations may not reflect what the model *actually* used internally. The model may have decided based on feature A; SHAP may credit feature B.
3. **Adversarial vulnerability**: post-hoc explanations can be manipulated — keep the model fixed, change only the explanation, in some cases.
4. **No ground truth**: there's no "correct" attribution to validate against.

This is why [[concepts/expressivity-interpretability-tradeoff]] lists post-hoc attribution as the **weakest** of the five interpretability strategies. If you genuinely need interpretability, building it in during training (linear decoder, knowledge mask, attention with explicit semantics) is more trustworthy than applying SHAP to a black-box afterward.

But post-hoc methods are unavoidable when:
- You're using foundation models you didn't train
- You want to compare across architectures
- You need interpretability for a model that wasn't designed with it in mind

## Practical Reading Tip

When a paper says it uses post-hoc attribution / SHAP / Integrated Gradients / etc.:

1. **Ask: did the model itself learn anything interpretable?** If yes (linear decoder, knowledge mask), the post-hoc layer is supplementary. If no (deep transformer), the post-hoc layer is doing all the interpretive work — treat the explanations more cautiously.
2. **Look for consistency checks.** Multiple post-hoc methods agreeing → more trustworthy. Reporting only one method → take with a grain of salt.
3. **Distinguish "model performance" claims from "model interpretation" claims.** Performance is what the model can do; interpretation is what we *think* it does. The two are often less coupled than papers imply.

## Korean Equivalent

**사후 (事後)** — literally "after the event". 사후 분석, 사후 해석 등으로 자주 번역됨.

## Connection to Other Concepts

- [[concepts/expressivity-interpretability-tradeoff]] — post-hoc attribution as one of 5 interpretability strategies (and the weakest)
- [[concepts/uncertainty-quantification]] — post-hoc calibration is a UQ technique
- [[concepts/perturbation-evaluation-design]] — post-hoc metrics evaluate trained models on tasks they weren't trained for
- [[concepts/distributional-vs-point-prediction]] — distributional metrics often applied post-hoc to point-prediction models

---

*Used in: [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] (review uses "post hoc" repeatedly across attribution, knowledge integration, and metric contexts), [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] (scGPT — interpretation relies on post-processing of attention), [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] (GEARS — integrates prior during training, contrast)*
