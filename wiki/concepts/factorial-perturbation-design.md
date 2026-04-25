---
title: "Factorial Perturbation Design: Revealing Condition-Dependent Effects"
type: concept
created: 2026-04-25
category: concepts
tags: [experimental-design, perturbation-screen, factorial, condition-dependence, interaction-effect, CRISPRi]
used_in:
  - drug-resistance/xu-2026-mapping-convergent-regulators-of
---

## Core Idea

A **single-condition perturbation screen** (perturb vs. control, in one context) tells you *whether* a perturbation matters. A **factorial design** (perturb × context, e.g., 2×2) tells you *under what conditions* it matters — and that often reveals different mechanistic categories that single-condition screens would lump together.

## The 1D vs 2D Picture

### 1D screen (standard)

```
NTC control ─────→ KD/perturb
              effect = Δ_observed
```

You measure: "Does this perturbation change phenotype?"
You miss: "Does this perturbation only matter under stress / drug / specific cell state?"

### 2×2 factorial screen (e.g., PerturbFate)

```
                   Context A         Context B
                  (e.g., DMSO)       (e.g., drug)
                  ─────────────     ─────────────
NTC control      │   baseline_A    │   baseline_B
                 │                 │
─────────────────┼─────────────────┼─────────────────
KD / perturb     │   KD_A          │   KD_B
                 │                 │
                  ─────────────     ─────────────

Effect in A:        Δ_A = KD_A − baseline_A
Effect in B:        Δ_B = KD_B − baseline_B
Interaction:        Δ_B − Δ_A   (does context modify the perturbation effect?)
```

The interaction term is the key new information.

## Three Mechanistic Categories the Design Reveals

| Pattern | Δ_A (no stress) | Δ_B (stress/drug) | Mechanistic class | Interpretation |
|---------|-----------------|-------------------|-------------------|----------------|
| **Constitutive driver** | Large | Small or absent | Acts independent of context | Always-on mechanism; context can mask but not enable |
| **Contingent driver** | Small or absent | Large | Only matters under stress/drug | Latent mechanism, revealed when normal pathway is blocked |
| **Context-independent** | Large | Large | Drives phenotype regardless | Robust; both conditions reveal it |
| **Antagonistic** | Opposite signs | — | Effect direction flips with context | Rare but mechanistically informative |

## Worked Example: Mediator Complex in Melanoma Resistance

[[drug-resistance/xu-2026-mapping-convergent-regulators-of]] used DMSO vs. vemurafenib as the two contexts. Both perturbations target the same complex (Mediator), produce the same outcome (dedifferentiation + resistance), but fall into different categories:

```
                          DMSO              Vemurafenib
                       ─────────────       ─────────────
NTC                  │ baseline          │ baseline + drug
                     │ (melanocytic)     │ response (arrest,
                     │                   │  re-differentiation)
─────────────────────┼───────────────────┼─────────────────
MED12 KD             │   ★★★            │    ★
(Kinase module)      │   strong dedif    │    attenuated
─────────────────────┼───────────────────┼─────────────────
MED15 KD             │   minimal         │   ★★★
(Tail module)        │                   │   strong dedif + resistance
```

- **MED12 KD** = constitutive driver → unleashes dedifferentiation regardless of drug; Vem context only modulates magnitude
- **MED15 KD** = contingent driver → effect only revealed under drug pressure; in DMSO the cell's normal MAPK-driven program masks the loss

**Same complex. Same convergent outcome. Different conditional logic.** A 1D screen (Vem only) would have called both "dedifferentiation drivers" and missed the distinction.

## Why This Matters for Therapeutic Design

The mechanistic class predicts how a target should be drugged:

- **Constitutive drivers** can be targeted as monotherapy — they act independent of disease context
- **Contingent drivers** must be combined with the inducing context (e.g., the drug they sensitize against) — alone they may have no effect
- This shapes which combinations are worth testing and which would be redundant

In PerturbFate, the convergent TF hub (FOSL1, KLF5, RREB1, SMAD3) was identified as the shared downstream target across both classes — combinatorial inhibition reduced resistance 3.1-fold across diverse upstream perturbations.

## Generalizing the Design

The "context" dimension can be anything that modulates pathway state:

| Context A | Context B | Reveals |
|-----------|-----------|---------|
| Vehicle | Drug | Drug-dependent vs constitutive drivers |
| Unstimulated | Cytokine/ligand | Signal-dependent regulation |
| Cell state X | Cell state Y | State-specific dependencies |
| Time t₀ | Time t₁ | Temporal dependence of effect |
| Wildtype | Mutant background | Genetic interaction (epistasis) |

The general principle: **adding a second axis lets you ask not just "does this matter?" but "when does it matter?"** — and "when" is often more informative for mechanism and therapy than "whether."

## Limitations

- Doubles or quadruples experimental cost
- Requires that both contexts can be applied uniformly to the same perturbation library
- Higher-order interactions (3+ factors) explode combinatorially — usually 2×2 is the practical ceiling
- Interpretation requires care: an absent effect in one context could mean "doesn't matter there" OR "compensated by context-specific redundancy"

## Practical Takeaway

When reading a perturbation screen paper:

1. **Check whether the design is 1D or factorial** — this changes what conclusions are possible
2. **Look for interaction terms** (Δ_B − Δ_A), not just main effects
3. **A perturbation showing no effect in one context is informative**, not a negative result — it tells you the mechanism is contingent on the *other* context
4. **"Same outcome" across perturbations does not mean "same mechanism"** — only a factorial design can distinguish convergent vs identical paths

## Part of broader synthesis

- [[overviews/six-open-issues-perturbation-modelling]] — this concept is the experimental backbone for **Issue 2: Covariate Handling** (factorial design is what lets you separate context from perturbation effect)
- [[overviews/endogenous-variation-as-natural-perturbation]] — donors as a covariate axis = natural perturbation; factorial designs across donor backgrounds reveal context-dependence
- [[overviews/convergent-regulation-across-systems]] — factorial design with shared context is what reveals convergence (different perturbs → same outcome under same condition)

---

*Used in: [[drug-resistance/xu-2026-mapping-convergent-regulators-of]] (PerturbFate — DMSO × Vemurafenib factorial CRISPRi screen)*
