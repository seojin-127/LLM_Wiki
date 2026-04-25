---
title: "Endogenous Variation as Natural Perturbation: Why Gene Effects Are Context-Dependent"
type: overview
created: 2026-04-25
category: overviews
tags: [context-dependence, endogenous-variation, natural-perturbation, expressivity, donor-heterogeneity, ASD, causal-inference, disentanglement, Pearl]
papers:
  - single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of
  - neuroscience/paulsen-2022-autism-genes-converge
  - neuroscience/jourdon-2023-modeling-idiopathic-autism
  - neuroscience/li-2023-single-cell-brain-organoid
  - neuroscience/schafer-2019-pathological-priming-causes
  - drug-resistance/xu-2026-mapping-convergent-regulators-of
---

## The Reframe

Single-cell biology typically draws a sharp line:

- **Observational data**: natural variation across donors, tissues, disease states
- **Interventional data**: deliberate CRISPR / drug perturbations

But this boundary is partly artificial. **Endogenous variation IS perturbation** — just unplanned. Every donor's genetic background is a natural experiment in which thousands of variants act as interventions. Pearl's causal framework treats this as the basis for *natural experiments* and *instrumental variables* — long-standing tools in economics and epidemiology, only recently being formalized for single-cell genomics.

The consequence — and the question this overview is built around:

> **Gene effects are not fixed properties of the gene.** They are functions of the context — including the genomic background on which a perturbation lands.

If we accept this, "what does gene X do?" is the wrong question. The right question is "what does X do *given* context Y?"

---

## Why this matters

If gene X had a fixed effect, then:
- Two patients with the same X mutation should have the same phenotype.
- KO of X in any donor's iPSC line should give the same magnitude effect.
- Spectrum disorders (ASD, schizophrenia) would not exist as spectra.

Empirically, none of these hold. Clinical genetics has long named the phenomenon:

- **Variable expressivity**: same variant, different magnitude of phenotype
- **Incomplete penetrance**: same variant, sometimes no phenotype at all
- **Genetic modifiers**: other variants in the same genome that buffer or amplify

What single-cell biology adds: the molecular dissection of *how* context modifies effect, cell-type by cell-type.

---

## Empirical evidence in this wiki

### Interventional × natural variation (the cleanest demonstrations)

[[neuroscience/paulsen-2022-autism-genes-converge]] knocked KMT5B, ARID1B, and CHD8 to haploinsufficiency in human cortical organoids — across **multiple donor lines per gene**. The result has two faces:
- Convergence: all 3 genes produce asynchronous GABAergic / deep-layer excitatory development
- **Divergence**: same KO across donors produces *different magnitudes* of the same phenotype
- Direct quote from the wiki page: *"Genomic context modulates expressivity (gene × background interaction)"*

[[neuroscience/li-2023-single-cell-brain-organoid]] (CHOOSE) screens 36 ASD genes in mosaic organoids — different perturbations, different cell types within the same organoid → cell-type-context interacts with perturbation effect.

### Pure endogenous variation (no CRISPR — observation alone reveals heterogeneity)

[[neuroscience/jourdon-2023-modeling-idiopathic-autism]] used iPSC organoids from 13 idiopathic ASD father-son pairs. **Macrocephalic vs. normocephalic ASD show *opposite* E/I imbalances.** Same diagnostic label, opposite molecular signatures. Pure natural perturbation — no CRISPR, no drug — exposing a hidden axis of heterogeneity.

[[neuroscience/schafer-2019-pathological-priming-causes]] documents *heterochronicity* across ASD individuals — each donor's developmental clock runs at a different rate. Time itself becomes a context variable.

### The flip side: shared context absorbs perturbation diversity

[[drug-resistance/xu-2026-mapping-convergent-regulators-of]] (PerturbFate) shows the converse phenomenon. >140 functionally diverse perturbations all converge on the same dedifferentiated state — but only *under vemurafenib pressure* (the context). Without the drug, MED15 KD has no effect; with it, MED15 KD becomes a strong driver. The context is what enables the convergence.

---

## The two faces of context-dependence

```
                              Same outcome?
                          ┌──────────┬──────────┐
                          │   YES    │    NO    │
        ┌─────────────────┼──────────┼──────────┤
        │                 │          │          │
  Same  │   YES (same     │   ★      │    ☆     │
perturb?│   KO, multiple  │ trivial  │ DIVERGE  │
        │   donors)       │          │          │
        ├─────────────────┼──────────┼──────────┤
        │                 │          │          │
        │   NO (different │   ◎      │    ●     │
        │   KOs, shared   │ CONVERGE │ unrelated│
        │   context)      │          │          │
        └─────────────────┴──────────┴──────────┘

  ☆  DIVERGENCE: same perturbation, different contexts → different effects
       Examples: Paulsen donor variation, Jourdon father-son pairs,
                 Schafer heterochronicity

  ◎  CONVERGENCE: different perturbations, shared context → same effect
       Examples: PerturbFate (Vem) → all routes to dedifferentiation,
                 Paulsen 3 ASD genes → asynchronous timing
       (covered in detail in the sister overview)
```

Both ☆ and ◎ are different shadows of the same underlying truth:

$$\text{effect} = f(\text{perturbation},\ \text{context})$$

not

$$\text{effect} = f(\text{perturbation})$$

The convergent-regulation overview ([[overviews/convergent-regulation-across-systems]]) explores ◎. This page explores ☆ and the unifying framing.

---

## Methodological framing — Dimitrov 2026 ontology

If we accept that effect = f(perturbation, context), then computational modelling has two jobs, and they are **serial, not parallel**:

```
   Raw data: perturbed cells + control cells
             across multiple cell types, donors, time points
                              ↓
   ┌──────────────────────────────────────────────────────┐
   │  STEP 1: DISENTANGLEMENT (separate)                  │
   │  observed variation = e_perturb + e_celltype +       │
   │                       e_donor + e_time + e_basal     │
   │  → learn an independent latent axis per covariate    │
   └──────────────────────┬───────────────────────────────┘
                          ↓
   Learned: a "perturbation X effect" vector decoupled from context
                          ↓
   ┌──────────────────────────────────────────────────────┐
   │  STEP 2: EXTRAPOLATION (recompose)                   │
   │  new context (e_celltype_new, e_donor_new, ...)      │
   │  + e_perturb_X                                       │
   │  → decode → counterfactual prediction                │
   └──────────────────────────────────────────────────────┘
                          ↓
   "What would this perturbation do in this new context?"
```

**Step 1 is the precondition for Step 2.** If perturbation effect and context aren't cleanly separated, the contamination travels with you when you transfer to a new context — and the prediction is wrong in ways that won't be obvious. This is why Dimitrov 2026 [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] writes:

> *"Disentanglement provides one approach to capture heterogeneity, thereby potentially improving not only interpretability but also accuracy for prediction tasks such as predicting cellular responses. **As such, it bridges the gap between understanding (What is?) and extrapolating (What could have been?)**."*

### Methods classified by which step they cover

| Method (in our wiki where ✓) | Step 1 (disentangle) | Step 2 (extrapolate) | Notes |
|---|:---:|:---:|---|
| ContrastiveVI | ✓ | — | Pure separation, case vs. control only |
| scGen | — | ✓ | Latent arithmetic on top of pre-learned representation |
| CPA (Compositional Perturbation Autoencoder) | ✓ | ✓ | Adversarial disentangle + compose new combinations |
| Biolord | ✓ | ✓ | Known covariates + unknown residual, both disentangled |
| GEARS ✓ ([[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]]) | (label-based) | ✓ | Predicts unseen perturbations via gene similarity priors |
| PerturbNet ✓ ([[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]]) | (modular) | ✓ | Chemical/genetic embeddings → unseen perturbations |
| ChemCPA | ✓ | ✓ | CPA + drug structure embedding for unseen molecules |
| PrePR-CT ✓ ([[drug-resistance/alsulami-2026-predicting-and-interpreting-cell]]) | ✓ | ✓ | Cell-type-specific co-expression graph as inductive bias |
| MrVI ✓ ([[single-cell-dl/boyeau-2025-deep-generative-modeling-of]]) | ✓ | (limited) | Per-cell sample distance matrices for stratification |
| moscot ✓ ([[single-cell-dl/klein-2025-mapping-cells-through-time]]) | — | ✓ | Population-tracing alternative to disentanglement-based extrapolation |
| Squidiff ✓ ([[single-cell-dl/he-2026-squidiff-predicting-cellular-development]]) | (semantic) | ✓ | Diffusion model with latent semantic manipulation for transfer |

### Why the generalization gap matters here

The Dimitrov review's most uncomfortable finding — that simple linear/additive baselines often beat state-of-the-art models on unseen perturbations — has a specific interpretation in this two-step framing:

> **Step 1 is not clean enough in current models.** What models call "perturbation effect" still has confounder contamination. When transferred to new context (Step 2), that contamination travels along, breaking predictions in unobvious ways.

The review's outlook addresses this by proposing **richer causal signatures** — adding temporal, spatial, and multi-omic axes — to constrain Step 1 better. Single-axis transcriptome data is underdetermined; the model has too many degrees of freedom to truly separate cause from coincidence.

Concretely, the outlook highlights **integrating natural genetic variants from population studies with interventional CRISPR atlases** as a key future direction — exactly the observational × interventional synthesis this overview foregrounds.

---

## How this changes the way we read papers

When you encounter a paper claiming "gene X causes phenotype Y":

1. **In which context?** Cell type, donor background, disease state, tissue, stage of development?
2. **Was natural variation across patients/donors quantified, or averaged out as noise?** A single mean effect across donors hides the variation that *is* the phenomenon.
3. **Would the conclusion hold in a different context?** A drug pressure, a different cell type, a different developmental stage?

When you see "we screened 100 genes and these 5 are hits":

1. **The 95 'non-hits' may be hits in a different context.** Reproducibility issues across ASD organoid screens often look like failure to replicate but may be context dependence in disguise.

When you see two papers reporting different effects of the same gene:

1. **Don't immediately call one of them wrong.** First ask whether they used different cell types, donor backgrounds, or developmental windows. Conflicting results may both be correct in their context.

---

## Open questions

1. **How do we quantify "context"?** Genetic background can be summarized as a high-dimensional vector (eQTL profile, polygenic score) — but most current methods reduce it to a discrete batch covariate.
2. **Can we predict context-dependence?** I.e., given an unseen donor genome, predict the magnitude of effect of a known perturbation. PrePR-CT, Biolord, ChemCPA are early attempts; benchmarks remain weak (see Dimitrov generalization gap).
3. **Are there "context-invariant" perturbation effects?** If most effects are context-dependent, what subset is robust enough to act on therapeutically? PerturbFate's RREB1+KLF5+SMAD3 hub may be one example.
4. **What's the right experimental design?** Currently most interventional screens use a single cell line. Donor diversity (e.g., Paulsen multi-donor design) is the gold standard but expensive. Multiplexed donor pooling (Mix-seq, Mosaic) is the scalable route.

---

## Related Reading

- [[overviews/convergent-regulation-across-systems]] — the sister overview focused on CONVERGENCE (different perturbations → same phenotype). This page extends to DIVERGENCE and the unifying frame
- [[concepts/factorial-perturbation-design]] — the methodological tool for measuring context-dependence (perturb × context grid)
- [[concepts/multimodal-temporal-readout]] — multimodal cascade (context-dependent effect can manifest at different layers)
- [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] — review formalizing these phenomena as modelling problems

---

## Origin Note

This overview was prompted by a study-session insight: realizing that observational endogenous variation is itself a form of natural perturbation, and that "gene effect" is not a fixed property but a function of context. The reframe inverts the usual research question from "what does X do?" to "what does X do *given* Y?" — and in doing so, makes the methodological problems formalized in Dimitrov 2026 (disentanglement, context transfer, causal inference) feel less like ML technicalities and more like answers to a clinical question that has existed since the first geneticists noticed that the same variant doesn't always produce the same disease.
