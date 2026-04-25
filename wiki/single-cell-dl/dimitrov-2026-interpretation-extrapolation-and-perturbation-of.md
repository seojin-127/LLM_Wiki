---
title: "Interpretation, extrapolation and perturbation of single cells"
authors: Daniel Dimitrov, Stefan Schrod, Martin Rohbeck, Oliver Stegle
year: 2026
doi: 10.1038/s41576-025-00920-4
source: dimitrov-2026-interpretation-extrapolation-and-perturbation-of.md
category: single-cell-dl
tags: [review, ontology, causal-inference, perturbation-modeling, representation-learning, disentanglement, mechanistic-discovery, population-tracing, optimal-transport, foundation-models, benchmarking, Stegle]
---

## Summary

A unifying ontology of ~150 ML methods for single-cell perturbation modelling. Organizes methods along three orthogonal axes: (1) **causal signatures** they exploit (observational vs interventional × temporal × spatial × multi-omic), (2) **shared modelling concepts** (representation learning, disentanglement, causal inference, mechanistic discovery, population tracing), and (3) **computational tasks** they address. Critically, recent benchmarks reveal that simple linear/additive baselines often match or beat state-of-the-art deep learning and foundation models on unseen perturbation extrapolation — exposing a generalization gap.

## Key Contributions

- **Three aims framework**: understand → extrapolate → guide
- **Five concept ontology** (Box 1): each with explicit assumptions and limitations
- **Method ontology figure** (Fig. 3): visual map placing scVI, scGPT, GEARS, CPA, MOFA+, SCENIC+, CINEMA-OT, NOTEARS, etc. in shared conceptual space
- **Three reference tables**: Table 1 (interventional technologies), Table 2 (computational tasks/methods), Table 3 (representative method trade-offs)
- **Critical evaluation**: simple baselines often beat foundation models on extrapolation; prior knowledge benefits may come from implicit sparsity not biological content
- **Online queryable resource** with technical method descriptions

## The Three Aims Framework

```
                  ┌──────────────────┐
                  │   UNDERSTAND     │  What changed?
                  │ DE → programmes  │  How do cells respond?
                  │ → causal nets    │  Why do they differ?
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │   EXTRAPOLATE    │  What if we tried X?
                  │ unseen cells/    │  What would unseen
                  │ perturbations/   │  combinations do?
                  │ combinations     │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │      GUIDE       │  What should we
                  │ experiment ↔     │  measure next?
                  │ prediction loop  │  Active learning
                  └──────────────────┘
```

## The Five Modelling Concepts (Box 1)

```
                Observational signatures           Interventional signatures
                       │                                    │
                       ▼                                    ▼
              ┌────────────────────────────────────────────────────┐
              │                                                    │
              │  REPRESENTATION LEARNING                           │
              │   (compress to latent space; manifold assumption)  │
              │                  │                                 │
              │                  ▼                                 │
              │  ┌──────────────────┬────────────────────────┐   │
              │  │ DISENTANGLEMENT  │  CAUSAL INFERENCE      │   │
              │  │ (separate factors│  (Pearl do-calculus,   │   │
              │  │  via priors,     │   adjust confounders,  │   │
              │  │  contrast, etc.) │   counterfactual)      │   │
              │  └────────┬─────────┴───────────┬────────────┘   │
              │           │                     │                │
              │           ▼                     ▼                │
              │  ┌──────────────────┬────────────────────────┐   │
              │  │ MECHANISTIC      │  POPULATION TRACING    │   │
              │  │ DISCOVERY        │  (OT, flow matching,   │   │
              │  │ (TF→target,      │   Schrödinger bridges) │   │
              │  │  GRN, directed)  │                        │   │
              │  └──────────────────┴────────────────────────┘   │
              └────────────────────────────────────────────────────┘
```

Each concept has **its own assumptions and failure modes** — Box 1 makes these explicit.

| Concept | Core assumption | What it cannot do alone |
|---------|-----------------|-------------------------|
| Representation learning | Manifold structure exists | Provide causal direction |
| Disentanglement | Factors are independent | Recover ground truth without supervision (nonlinear case) |
| Causal inference | Confounders observable | Work on transcriptome alone (causal sufficiency fails) |
| Mechanistic discovery | All variables observed; priors generalizable | Recover known regulators reliably (often fails) |
| Population tracing | Smooth continuous transitions | Handle highly divergent populations |

## Causal Signatures (Fig. 1)

Observational and interventional data each provide *partial views* of the causal process. Combining them is the goal:

| Axis | Observational | Interventional |
|------|---------------|----------------|
| **Source** | Natural variation (tissue, donor, disease) | CRISPR / drugs |
| **Tractability** | Atlas-scale, in vivo realistic | Lower scale, in vitro bias |
| **Causal interpretation** | Requires strong assumptions | Direct (Pearl do-operation) |
| **Examples** | HCA atlases, eQTL studies | Perturb-seq, FiCS, ECCITE-seq |

Plus three orthogonal modality axes — **temporal**, **spatial**, **multi-omic** — which add structural constraints for causal inference.

## Method Catalog Highlights

### Methods we have wiki pages for, classified by Dimitrov ontology

| Method | Aim | Concept | Wiki page |
|--------|-----|---------|-----------|
| scVI | Understand | Repr. learning (nonlinear) | [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] |
| scANVI | Understand | Repr. learning + disentangle | [[single-cell-dl/xu-2021-probabilistic-harmonization-and]] |
| scArches | Extrapolate (context) | Repr. learning | [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]] |
| scPoli | Understand | Repr. learning + disentangle | [[single-cell-dl/dedonno-2023-population-level-integration-of]] |
| MrVI | Understand | Repr. learning + disentangle | [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]] |
| moscot | Trace populations | Population tracing (OT) | [[single-cell-dl/klein-2025-mapping-cells-through-time]] |
| Monod | Understand | Repr. learning + mechanistic | [[single-cell-dl/gorin-2025-monod-model-based-discovery]] |
| GEARS | Extrapolate (unseen) | Disentanglement + repr. learning + priors | [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] |
| PerturbNet | Extrapolate (unseen) | Disentanglement + repr. learning | [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] |
| Squidiff | Extrapolate (unseen) | Population tracing (diffusion) | [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] |
| TRADE | Understand | Disentanglement (effect-size dist.) | [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] |
| CellOracle | Discover mechanisms | Mechanistic + in silico interventions | [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] |
| scGPT | Repr. + mechanistic | Foundation model | [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] |
| scFoundation | Repr. learning | Foundation model | [[single-cell-foundation/hao-2024-large-scale-foundation-model]] |
| SCimilarity | Repr. learning | Foundation (metric learning) | [[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]] |
| EpiAgent | Repr. + mechanistic | Foundation (scATAC) | [[single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell]] |
| PerturBERT | Repr. learning | Foundation (perturbation) | [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]] |
| PerturbFate | Quantify response | Multimodal causal anchor | [[drug-resistance/xu-2026-mapping-convergent-regulators-of]] |

### Methods reviewed but not yet in our wiki

Notable methods to potentially ingest later: CPA, ChemCPA, MOFA+, MEFISTO, CINEMA-OT, ContrastiveVI, SAMS-VAE, Biolord, NOTEARS, DCDI, Bicycle, SCENIC+, Dictys, scDoRI, LINGER, Spectra, NicheCompass, Waddington-OT, CellOT, SOFA, GSFA, FLeCS, CellFlow, Prescient, scGen, DRVI, Mixscape, MELD, MUSIC, scPRINT.

## The Generalization Gap (Critical Section)

Recent benchmarks reveal an uncomfortable truth:

```
   Task: Predict unseen perturbation effects
   ─────────────────────────────────────────

   Simple linear/additive baseline:    [████████████████]  Strong
   Specialist deep learning models:    [████████████████]  Comparable
   Foundation models (even fine-tuned):[████████████░░░░]  Often worse

   (paraphrased from refs 217–221, 246, 84, 213, 220)
```

Implications:
- Many "improvements" capture systematic confounder differences, not true perturbation specificity
- Prior-knowledge benefits may stem from implicit network sparsity, not biological information (ref 245)
- Foundation models' representations may not be as generalist as claimed
- Suboptimal evaluation metrics partially explain — but don't fully excuse — these results

This challenges the field to:
1. Adopt standardized baselines and biologically meaningful metrics
2. Build community benchmarks (refs 243, 251, 252)
3. Design models that capture context-dependence, not just population-level shifts

## Outlook — What's Next

1. **Multi-signature integration**: no current method jointly models spatial + temporal + multi-omic + perturbational; the field needs unified frameworks
2. **Non-destructive longitudinal**: clonal lineage tracing, live-cell sequencing, microscopy-based profiling
3. **In vivo perturbation + spatial**: Perturb-Map, Perturb-CAST, CRISPRmap (Table 1 spatial technologies)
4. **Cross-modal foundation models**: text + omics + imaging
5. **Population genetics × interventional**: natural variants + CRISPR atlases for disease variant effects
6. **Closed-loop experiment-prediction**: active learning, agentic workflows

## How to Use This Review

This is a **navigation hub** for our single-cell-dl section:
- Looking for a method? Find it in Table 2 (tasks), Fig. 3 (ontology), or Table 3 (trade-offs)
- Reading a method paper? Locate it in the ontology to understand its concept and assumptions
- Designing a study? Use Fig. 1 to identify which causal signatures your data captures, then pick methods that exploit those signatures
- Evaluating claims? Read the "Modelling and evaluation challenges" section for skepticism guardrails

## Limitations of the Review Itself

- Coverage of preprints means some ranked methods may not survive peer review
- Ontology assigns each method to one concept, but most methods integrate multiple — the assignment is a simplification
- Online resource is the more up-to-date catalogue; the figures and tables are necessarily snapshot
- Heavy emphasis on transcriptomics; spatial and multi-omic coverage growing but not exhaustive

## Related Papers

### Concept pages
- [[concepts/multimodal-temporal-readout]] — ATAC → nascent → steady-state cascade (used in this review's multi-omic discussion)
- [[concepts/factorial-perturbation-design]] — 2×2 perturb × context (the ontology's "predict effects" tasks build on this)
- [[concepts/variational-autoencoder]] — backbone of most repr. learning + disentanglement methods cataloged here
- [[concepts/graph-neural-network]] — used in mechanistic discovery (GEARS, graphVCI, PDGrapher)
- [[concepts/uncertainty-quantification]] — relevant for benchmarking and confidence-aware extrapolation

### Methods cataloged in the review (already in wiki)
- [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] — scVI
- [[single-cell-dl/xu-2021-probabilistic-harmonization-and]] — scANVI
- [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]] — scArches
- [[single-cell-dl/dedonno-2023-population-level-integration-of]] — scPoli
- [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]] — MrVI
- [[single-cell-dl/klein-2025-mapping-cells-through-time]] — moscot (population tracing exemplar)
- [[single-cell-dl/gorin-2025-monod-model-based-discovery]] — Monod
- [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] — GEARS
- [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] — PerturbNet
- [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] — Squidiff
- [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] — TRADE
- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT
- [[single-cell-foundation/hao-2024-large-scale-foundation-model]] — scFoundation
- [[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]] — SCimilarity
- [[single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell]] — EpiAgent
- [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]] — PerturBERT
- [[drug-resistance/xu-2026-mapping-convergent-regulators-of]] — PerturbFate (multimodal interventional anchor)
- [[overviews/convergent-regulation-across-systems]] — uses this review's ontology to position convergent regulation findings
