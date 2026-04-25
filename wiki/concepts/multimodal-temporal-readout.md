---
title: "Multimodal Temporal Readout: ATAC → Nascent RNA → Steady-state RNA"
type: concept
created: 2026-04-25
category: concepts
tags: [multimodal, ATAC, nascent-RNA, metabolic-labeling, RNA-velocity, temporal-dynamics, causal-inference]
used_in:
  - drug-resistance/xu-2026-mapping-convergent-regulators-of
  - single-cell-dl/gorin-2025-monod-model-based-discovery
---

## Core Idea

Three single-cell readouts are not redundant views of "gene activity" — they are **three different time windows** of the same regulatory cascade. Reading them together (rather than any one alone) lets you reconstruct cause → mechanism → outcome **within one cell**.

```
Time →

Chromatin opens   →   TF binds   →   Nascent RNA made   →   Steady-state mRNA accumulates
      ↑                                    ↑                          ↑
    ATAC                              5-EU labeled               Unlabeled
  (potential)                        (instantaneous              (accumulated
                                       output)                    identity)
```

## What Each Layer Encodes

| Layer | Time window | What it measures | Physical meaning |
|-------|-------------|------------------|------------------|
| **ATAC** | ~hours of priming | Open chromatin regions where TFs *can* bind | **Potential / preparation** |
| **Nascent RNA** | ~1 hour pulse (5-EU) | mRNA synthesized *during* the pulse | **Present GRN output (instantaneous)** |
| **Steady-state RNA** | ~hours of accumulation | Total mRNA pool, balance of synthesis vs decay | **Cellular identity (functional state)** |

At equilibrium:
$$[\text{steady-state mRNA}] = \frac{\text{transcription rate}}{\text{decay rate}}$$

- **Nascent** measures the numerator directly
- **Steady-state** measures the ratio
- Comparing the two reveals whether a gene is **rising, falling, or at steady state** — this is the principle behind **RNA velocity**

## Why You Need All Three

### Steady-state alone is insufficient

- Cell-type definitions (e.g., `SOX10+ = melanocytic`, `AXL+ = neural crest-like`) are based on steady-state mRNA, so it tells you "what the cell currently is"
- But it cannot distinguish "stably this state" vs "transitioning into this state" vs "leaving this state"
- It integrates over hours of past transcription, so transient changes are invisible

### Nascent alone is insufficient

- Sparse and noisy (1-hour pulse captures few molecules per gene)
- Decoupled from function for genes with long mRNA half-lives (high transcription rate ≠ high protein)
- No reference to identity — current transcription doesn't tell you whether the cell has actually become something new

### ATAC alone is insufficient

- Open chromatin = *potential*, not actualized output
- Many open regions are never transcribed in a given cell
- Cannot tell which TFs are active vs merely able to bind

### The pair (nascent + steady-state) gives direction

| Nascent | Steady-state | Interpretation |
|---------|--------------|----------------|
| ↑ high | ↓ still low | **Just turning ON** (early induction) |
| ↓ low | ↑ still high | **Turning OFF** (decay-limited, lagging) |
| ≈ balanced | ≈ balanced | **At steady state** |
| ↑ high | ↑ high | **Confirmed new identity** |

### The triplet closes the causal chain

```
ATAC ─────→ Nascent RNA ─────→ Steady-state RNA
 (cause)        (mechanism)         (outcome)

Did the TF        Is the TF         Has the cell's
binding site     actively driving   identity actually
become open?     transcription?     changed?
```

When all three layers point the same direction → strong evidence of a real, completed regulatory event.
When they disagree → reveals subtler states (primed but not actualized, or fading rather than emerging).

## In Practice: PerturbFate Convergence Story

The convergence finding in [[drug-resistance/xu-2026-mapping-convergent-regulators-of]] (24 perturbations → shared dedifferentiated state) is rigorous *because* all three layers were consistent:

| Single readout | What you would conclude | Failure mode |
|----------------|------------------------|--------------|
| ATAC only | "AP-1/TEAD motifs opened" | Could be priming without transcription |
| Nascent only | "Dedifferentiation TFs are actively transcribing" | Could be transient noise |
| Steady-state only | "Neural crest markers present" | Could be residual, not actively maintained |
| **All three together** | **"Real, ongoing dedifferentiation across diverse perturbations"** | High confidence |

## Relation to Classical RNA Velocity

The unspliced-vs-spliced approach (La Manno 2018, scVelo) infers transcription dynamics from intronic reads as a *proxy* for nascent RNA. Metabolic labeling (5-EU, 4sU) directly labels newly synthesized RNA — cleaner separation, fewer assumptions about splicing kinetics. PerturbFate uses 5-EU; [[single-cell-dl/gorin-2025-monod-model-based-discovery]] formalizes the underlying biophysics.

## Practical Takeaway

When reading any multimodal paper that profiles chromatin + nascent + steady-state:

1. **Don't treat the three as redundant** — each answers a different question
2. **Look for agreement across layers** = strong evidence of completed regulatory event
3. **Look for disagreement** = subtle dynamics (priming, decay, transition)
4. **Steady-state defines "what cell"; nascent defines "where going"; ATAC defines "what enabled"**

---

*Used in: [[drug-resistance/xu-2026-mapping-convergent-regulators-of]] (PerturbFate — multimodal CRISPRi screen), [[single-cell-dl/gorin-2025-monod-model-based-discovery]] (Monod — biophysical modeling of nascent/mature counts)*
