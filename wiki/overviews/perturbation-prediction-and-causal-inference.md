---
title: "From Prediction to Cause: Perturbation Models in Single-Cell Data"
type: overview
created: 2026-04-11
category: overviews
tags: [perturbation, causal-inference, GRN, foundation-model, Perturb-seq, variant-interpretation, predictive-vs-causal, pattern-learning]
papers:
  - single-cell-dl/kamimoto-2023-dissecting-cell-identity-via
  - single-cell-dl/nadig-2025-transcriptome-wide-analysis-of
  - single-cell-dl/lange-2022-cellrank-for-directed-single
  - single-cell-dl/setty-2019-characterization-of-cell-fate
  - single-cell-dl/he-2026-squidiff-predicting-cellular-development
  - single-cell-dl/klein-2025-mapping-cells-through-time
  - single-cell-dl/vinyard-2025-learning-cell-dynamics-with
  - single-cell-dl/gorin-2025-monod-model-based-discovery
  - single-cell-dl/aivazidis-2025-cell2fate-infers-rna
  - single-cell-foundation/cui-2024-scgpt-toward-building-foundation
  - single-cell-foundation/hao-2024-large-scale-foundation-model
  - single-cell-foundation/szalata-2026-perturbert-learning-gene-co
  - drug-resistance/alsulami-2026-predicting-and-interpreting-cell
  - drug-resistance/chen-2022-deep-transfer-learning-of
  - drug-resistance/antonopoulos-2026-zero-shot-prediction-of-drug
  - brain-development/fleck-2023-inferring-perturbing-cell-fate
  - brain-development/zenk-2024-single-cell-epigenomic-reconstruction
  - brain-development/ding-2026-dissecting-gene-regulatory-networks
  - genomic-dl/zinati-2024-groundgan-grn-guided
  - genomic-dl/deng-2024-massively-parallel-regulatory
  - neuroscience/jin-2020-in-vivo-perturb-seq
  - neuroscience/amelan-2026-crispr-knockout-screens-reveal
  - neuroscience/paulsen-2022-autism-genes-converge
  - neuroscience/jourdon-2023-modeling-idiopathic-autism
  - neuroscience/dubuc-2026-linking-rare-variants-cell-type
---

## Why This Overview Exists

The [[overviews/atlas-as-hypothesis-engine]] overview ended with a loop: **reference → project → compare → predict → perturb → update**. That loop only works if the *predict* step is actually trustworthy, and trustworthy means different things depending on whether you want to **describe** what cells are doing now, **generate** plausible cell states under hypothetical conditions, or **intervene** in a causal graph and read off the consequences.

Most methods in this wiki that call themselves "perturbation prediction" quietly occupy different cells of that three-way distinction. Treating them as substitutes produces overconfident conclusions. This overview makes the distinction explicit, then asks a second question that sits under it: **is gene-level perturbation enough to interpret variants?**

- **Part I** — What "predict a perturbation" actually means, and how co-expression, latent representation, GRN inference, and intervention each say something different
- **Part II** — Why gene knockout is not a variant effect
- **Part III** — Mapping methods to what they actually deliver
- **Part IV** — Handing the loop back to the atlas overview

---

# Part I — What "Predict a Perturbation" Actually Means

## 1. Three levels of claim

| Level | What the model does | Epistemic status |
|-------|---------------------|------------------|
| **Descriptive** | Reconstructs observed dynamics on the manifold (trajectories, fates, transitions) | "This is what the data already shows if we look at it right" |
| **Generative (in-distribution)** | Samples cell states that resemble real perturbed cells seen during training | "Given perturbations I've seen, I can interpolate to similar ones" |
| **Interventional (counterfactual)** | Predicts what would happen under a do(gene = 0) operation on the causal graph | "If I intervened, this is what would change" |

Every method in this wiki's perturbation literature lives on one of these levels. The tragedy is that **papers routinely frame level-2 work in level-3 language** — "perturbation prediction" suggests intervention, but the math delivers interpolation.

## 2. What co-expression, latent representation, and GRN inference each tell you

At a glance — the four primitive approaches, what they actually compute, and which claim level they can legitimately support:

```
┌────────────────┬──────────────────┬──────────────────┬─────────┬──────────────────┐
│ Approach       │ Input signal     │ What it learns   │ Claim   │ Wiki examples    │
├────────────────┼──────────────────┼──────────────────┼─────────┼──────────────────┤
│ Co-expression  │ Gene × gene      │ Undirected       │ Level 1 │ PrePR-CT prior,  │
│                │ correlation      │ gene graph       │ (+ bias │ WGCNA modules    │
│                │                  │ (no direction)   │  for 2) │                  │
├────────────────┼──────────────────┼──────────────────┼─────────┼──────────────────┤
│ Latent         │ Cell × gene      │ Low-dim manifold │ Level 2 │ scVI, scGPT,     │
│ representation │ matrix (+ batch) │ where similar    │         │ scFoundation,    │
│ (VAE / FM /    │                  │ cells are close. │         │ Squidiff,        │
│  diffusion)    │                  │ No causal dirs.  │         │ PerturBERT       │
├────────────────┼──────────────────┼──────────────────┼─────────┼──────────────────┤
│ GRN inference  │ RNA + ATAC +     │ Directional      │ Level 3 │ CellOracle,      │
│ (motif-fixed)  │ motif scan       │ TF → target      │ (by     │ Fleck, Zenk,     │
│                │                  │ with propagation │ design) │ Ding             │
│                │                  │ operator         │         │                  │
├────────────────┼──────────────────┼──────────────────┼─────────┼──────────────────┤
│ Intervention   │ CRISPR KO/KD +   │ Measured         │ Level 3 │ Jin Perturb-seq, │
│ (wet lab)      │ scRNA-seq        │ response per     │ (gold   │ Amelan screens,  │
│                │                  │ perturbation     │  std)   │ Replogle (TRADE) │
└────────────────┴──────────────────┴──────────────────┴─────────┴──────────────────┘
                     │                    │                  │
                     ▼                    ▼                  ▼
               correlational        interpolation     causal / counterfactual
```

- **Co-expression** (what gene pairs move together) is purely correlational. Two genes can covary because one regulates the other, because both respond to the same upstream driver, or because they mark the same cell state. From co-expression alone you cannot tell which. Gene-gene graphs used in [[drug-resistance/alsulami-2026-predicting-and-interpreting-cell]] (PrePR-CT) are useful as an **inductive bias** that makes learning easier, not as a causal map.
- **Latent representation** (what VAEs, foundation models, and diffusion models learn) compresses high-dimensional gene space into a lower-dimensional manifold where "similar cells are close." This is useful for interpolation between observed states but carries no guarantee about *causal directions* in the original gene space. [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] (scGPT) and [[single-cell-foundation/hao-2024-large-scale-foundation-model]] (scFoundation) learn rich latent spaces, but their perturbation-prediction benchmarks ask "can you reproduce observed perturbation responses" — a level-2 test, not a level-3 one. [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] (Squidiff) is even more explicit: perturbation is a `Δz_sem` direction learned from paired examples, not a causal edit.
- **GRN inference** (inferring which TF regulates which target) at least has *directional* edges, but those directions usually come from motif priors, not from interventional data. Classical co-expression-based GRN methods (SCENIC, GRNBoost2) orient edges by convention, not by evidence. [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] (CellOracle) makes a specific move to sidestep this: it fixes directionality using motif scans on open chromatin (scATAC), then uses the fitted linear model as a **signal-propagation operator**. That is a level-3 claim: the model is designed to be applied as an intervention.
- **Intervention** (gold standard) is to actually perturb and measure. Perturb-seq ([[neuroscience/jin-2020-in-vivo-perturb-seq]]) and genome-scale CRISPR screens ([[neuroscience/amelan-2026-crispr-knockout-screens-reveal]]) occupy this level. Their limitations are entirely about statistical power and gene-vs-variant granularity, not about epistemic level.

## 3. Where the gap shows up in practice

The diagnostic question to ask any "perturbation prediction" paper: **what claim level does the model advertise, and what claim level does the validation actually support?** The two rarely match. The 3×3 diagnostic:

```
                            VALIDATION LEVEL
                   ┌──────────────┬──────────────┬──────────────┐
                   │  1: observed │ 2: held-out  │ 3: novel     │
                   │  recap       │ perturbation │ intervention │
                   ├──────────────┼──────────────┼──────────────┤
           1       │   HONEST     │   over-      │    over-     │
   C    describe  │ (Palantir,   │   scoped     │   scoped     │
   L    dynamics  │  CellRank,   │              │              │
   A              │  moscot,     │              │              │
   I              │  Monod)      │              │              │
   M              ├──────────────┼──────────────┼──────────────┤
           2       │  under-      │   HONEST     │   aspira-    │
   L   generate  │  sold        │ (scGPT,      │   tional     │
   E   in-dist    │              │  Squidiff,   │              │
   V              │              │  PerturBERT, │              │
   E              │              │  PrePR-CT)   │              │
   L              ├──────────────┼──────────────┼──────────────┤
           3       │ silent       │ LEVEL 2      │   HONEST     │
     intervene    │ over-        │ MASQUERADING │ (CellOracle  │
                   │ claim        │ AS LEVEL 3 ⚠ │  zebrafish   │
                   │              │              │  noto KO)    │
                   └──────────────┴──────────────┴──────────────┘

          Above the diagonal = under-sold; below the diagonal = over-sold.
          The common failure mode is the ⚠ cell (bottom-middle).
```

Four characteristic patterns:

- **⚠ Level 2 masquerading as level 3** (bottom-middle cell): when [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]] (PerturBERT) or [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] (Squidiff) are asked to predict a *novel* perturbation whose target gene was never in the training set, performance degrades in ways that pure-interpolation methods must. They are working on the manifold of observed perturbation signatures, not on a causal model.
- **Level 3 claim, level 1 validation** (bottom-left): [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] (CellOracle) uses a linear-GRN operator as a causal model, but its validation is benchmarked against known haematopoiesis biology and a novel zebrafish phenotype — real interventional validation, but only in a handful of cases. Whether the operator generalizes as a causal model across thousands of TFs in arbitrary cell states is not shown.
- **Level 1 correctly scoped** (top-left): [[single-cell-dl/setty-2019-characterization-of-cell-fate]] (Palantir), [[single-cell-dl/lange-2022-cellrank-for-directed-single]] (CellRank), and [[single-cell-dl/klein-2025-mapping-cells-through-time]] (moscot) are explicitly descriptive — they reconstruct observed trajectories. They do not claim to predict intervention, and so are not at risk of overclaiming.
- **Statistical grading** (the ruler under the whole matrix): [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] (TRADE) exists because even level-3 wet-lab Perturb-seq is undersampled — most of the true effect variance is missed by per-gene FDR thresholds. TRADE says: before you compare any prediction to "ground truth Perturb-seq DEGs," understand that the ground truth itself only captures ~13-36% of the transcriptome-wide impact.

---

# Part II — Gene Knockout Is Not a Variant Effect

The second question is narrower but more practically urgent: **given that GWAS identifies thousands of risk variants, can we interpret them using gene-level perturbation data?**

## 4. What Perturb-seq measures

A Perturb-seq screen knocks out or knocks down a gene with CRISPR, then reads out the transcriptome. It answers: *what cell-state change does a complete loss-of-function cause?*

- [[neuroscience/jin-2020-in-vivo-perturb-seq]]: 35 autism/ND risk genes in mouse cortex → 14 gene modules → conserved in human ASD brain.
- [[neuroscience/amelan-2026-crispr-knockout-screens-reveal]]: genome-wide KO during mESC → neural differentiation → 331 neural-differentiation-essential genes, including PEDS1 (plasmalogen biosynthesis) validated as a new recessive microcephaly gene.
- [[neuroscience/paulsen-2022-autism-genes-converge]]: three ASD genes (KMT5B, ARID1B, CHD8) converge on asynchronous GABAergic/excitatory development in organoids.

These are excellent for identifying **which genes matter** and **which cell types they matter in**. They are poor for asking **what a specific variant does**.

## 5. What a variant actually does that gene KO misses

A risk variant is almost never a full loss-of-function. It is usually:

- A regulatory change (enhancer, promoter) that modulates expression by 10-50% in a specific cell context.
- A splice-altering intronic change.
- A protein-coding change with partial functional effect (missense, hypomorph).
- Allele-specific expression with cis-regulatory logic.

Gene-level KO screens **cannot tell you** what a 30% expression reduction in radial glia at E14 does, which is what GWAS actually asks. The closest the wiki comes to variant-level interventional data is [[genomic-dl/deng-2024-massively-parallel-regulatory]] (lentiMPRA of 46,802 enhancers with allele-specific activity for 164 psychiatric variants) — but MPRA is a reporter assay in cell lines, not a scRNA-seq readout.

## 6. What the wiki offers for variant interpretation

Given this gap, what can the wiki's tools actually do?

| Strategy | Method | What it buys you |
|----------|--------|------------------|
| Map variant → gene → cell type via transcriptomics | [[neuroscience/dubuc-2026-linking-rare-variants-cell-type]] (rare variants + FM) | Cell-type-of-effect, not mechanism |
| Simulate gene KO on top of normal atlas | [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] (CellOracle), [[brain-development/fleck-2023-inferring-perturbing-cell-fate]] (organoid regulome) | Direction of fate shift, assuming KO as a proxy for LoF |
| Compare disease to healthy on the atlas | [[neuroscience/jourdon-2023-modeling-idiopathic-autism]], [[neuroscience/paulsen-2022-autism-genes-converge]] | Which trajectory diverges, not which variant caused it |
| Test variants in allelic reporter assays | [[genomic-dl/deng-2024-massively-parallel-regulatory]] (lentiMPRA) | Allelic effect at the enhancer level, no cell-state readout |
| Zero-shot predict drug response via signaling | [[drug-resistance/antonopoulos-2026-zero-shot-prediction-of-drug]] (LEMBAS) | Drug MoA, tangentially relevant for chemical probes of risk pathways |

**The wiki does not yet contain a method that connects a non-coding risk variant to a cell-state change in a developmentally specific context.** That is the central gap — and it is not a gap the gene-level perturbation literature can fill alone.

---

# Part III — Mapping Methods to Claims

Putting Parts I and II together, the method landscape falls into five honest categories:

## A. Descriptive dynamics — "what the data shows"

| Method | What it delivers |
|--------|------------------|
| [[single-cell-dl/setty-2019-characterization-of-cell-fate]] Palantir | Probabilistic fate + differentiation potential |
| [[single-cell-dl/lange-2022-cellrank-for-directed-single]] CellRank | Directed Markov chain with fate probabilities, works on regeneration/reprogramming |
| [[single-cell-dl/klein-2025-mapping-cells-through-time]] moscot | Optimal-transport alignment across time, space, modalities |
| [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna]] cell2fate | Bayesian ODE-refined RNA velocity |
| [[single-cell-dl/vinyard-2025-learning-cell-dynamics-with]] scDiffEq | Neural SDE with state-dependent drift and diffusion |
| [[single-cell-dl/gorin-2025-monod-model-based-discovery]] Monod | Biophysical stochastic transcription parameters |

**Claim level**: 1 (with some level-2 extensions in scDiffEq's drift perturbation mode). **Variant-level use**: none directly, but these are the substrate on which any causal claim must be made.

## B. Latent-space pattern learning — "what looks similar"

| Method | Backbone |
|--------|----------|
| [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] scGPT | Transformer pretrained on 33M cells |
| [[single-cell-foundation/hao-2024-large-scale-foundation-model]] scFoundation | 100M-parameter asymmetric transformer |
| [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]] PerturBERT | BERT on perturbation signatures |
| [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] Squidiff | Conditional diffusion on scRNA-seq |
| [[drug-resistance/alsulami-2026-predicting-and-interpreting-cell]] PrePR-CT | GAT on cell-type co-expression graphs |
| [[drug-resistance/chen-2022-deep-transfer-learning-of]] scDEAL | Bulk → single-cell transfer learning |

**Claim level**: 2. These interpolate between observed perturbation/drug responses but do not model causation. Their benchmarks are "can you reproduce observed responses" — a level-2 test. They can be excellent for **in-distribution** drug-response prediction and for **feature extraction**; they are a poor substitute for intervention.

## C. Mechanistic / causal operators — "what do(X=0) does"

| Method | Causal move |
|--------|-------------|
| [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] CellOracle | Directional GRN (motif-fixed) as signal-propagation operator |
| [[brain-development/fleck-2023-inferring-perturbing-cell-fate]] Pando/brain-organoid GRN | Brain-organoid application of the same paradigm |
| [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction]] | Epigenomic-anchored GRN for brain development |
| [[brain-development/ding-2026-dissecting-gene-regulatory-networks]] | GRN governing cortical fate |
| [[genomic-dl/zinati-2024-groundgan-grn-guided]] GRouNdGAN | GRN-guided causal GAN for scRNA-seq simulation + in silico TF KO |

**Claim level**: 3 (intended). Caveat: the causal claim is only as strong as the GRN prior. Motif-based directionality is a real move, but it cannot disentangle co-binding factors and it assumes that a linear propagation operator is adequate. Validation is typically sparse — a handful of known perturbations plus one or two novel predictions.

## D. Biophysical mechanism — "what the molecular kinetics are doing"

| Method | What it models |
|--------|----------------|
| [[single-cell-dl/gorin-2025-monod-model-based-discovery]] Monod | Bursty / extrinsic / CIR chemical master equation, per gene per cell type |

**Claim level**: sits outside the 1/2/3 axis. Monod models *how* transcription happens, not *what* happens under perturbation. It is the natural partner of a causal operator: a CellOracle-style GRN tells you which edges matter; Monod tells you what those edges mean biophysically (burst frequency vs. burst size change).

## E. Statistical grading — "how to test any of the above"

| Method | What it grades |
|--------|---------------|
| [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] TRADE | Transcriptome-wide impact of real Perturb-seq |

**Role**: TRADE is the honest ruler. Before you claim a predicted perturbation "matches" Perturb-seq ground truth, you need TRADE to tell you what the ground truth even is, statistically. TRADE's finding that only 13-36% of the true effect variance is captured by FDR-significant DEGs implies that most prediction benchmarks are measuring the wrong thing.

---

# Part IV — Closing the Atlas Loop

The [[overviews/atlas-as-hypothesis-engine]] overview proposed a loop:

```
reference → project → compare → predict → perturb → update
```

Now each step can be matched to the methods that actually support it:

| Step | What it needs | Methods in this wiki |
|------|---------------|----------------------|
| **Reference** | Multimodal, trajectory-aware atlas | [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]] HNOCA, [[brain-atlas/braun-2023-comprehensive-cell-atlas-first]] Braun, [[brain-development/dibella-2021-molecular-logic-of-cellular]] Di Bella |
| **Project** | Query embedding on frozen reference | [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]] scArches, [[single-cell-dl/dedonno-2023-population-level-integration-of]] scPoli |
| **Compare** | Per-cell / per-sample deviation with uncertainty | [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]] MrVI, [[single-cell-dl/ergen-2024-consensus-prediction-cell]] popV |
| **Describe dynamics** | Trajectory + dynamics on the query | Palantir → CellRank → scDiffEq → moscot (chain) |
| **Predict (level 2)** | In-distribution drug / gene response | scGPT, scFoundation, Squidiff, PerturBERT, PrePR-CT |
| **Predict (level 3)** | Causal intervention simulation | **CellOracle** (and organoid extensions: Fleck, Zenk, Ding) |
| **Grade predictions** | Rigorous DE analysis of real Perturb-seq | TRADE |
| **Perturb (wet)** | Gene-level validation | Jin 2020 Perturb-seq, Amelan 2026 CRISPR screens, Paulsen, Jourdon |
| **Update** | Re-integrate new data into the atlas | scArches / scPoli loop |

**Two critical gaps the loop currently has**:

1. **Between level-2 prediction and level-3 intervention**: no method in this wiki has been benchmarked at closing that gap, i.e., showing that a foundation-model prediction agrees with a CellOracle-style causal operator *and* with Perturb-seq. Each pair of the triangle has been tested separately at most.

2. **Between gene-level perturbation and variant-level effect**: not closed by any single method. [[neuroscience/dubuc-2026-linking-rare-variants-cell-type]] attempts to bridge rare variants to cell types via a foundation model, but cannot simulate the cell-state consequence of a 30% expression reduction in a specific developmental window — which is what a non-coding GWAS hit actually corresponds to. Closing this gap requires variant-level interventional readouts (base-editing CRISPRi, allelic reporter × scRNA-seq) that the wiki does not yet contain.

---

## Decision Guide: What Claim Can I Actually Make?

```
I want to say something about a perturbation
│
├─ "I can show how the trajectory progresses"
│   └─ Descriptive dynamics (Palantir, CellRank, moscot, scDiffEq)
│
├─ "I can show what a drug / gene does to similar cells"
│   ├─ Seen perturbations → any level-2 method
│   ├─ Unseen cell type, seen drug class → PrePR-CT (graph prior helps)
│   ├─ Seen pathway, new combination → Squidiff (diffusion interpolation)
│   └─ Large-scale FM baseline → scGPT / scFoundation
│
├─ "I can simulate a gene knockout and get a causally meaningful direction"
│   └─ CellOracle (and brain-organoid extensions)
│   NOTE: causal claim rests on motif-based GRN priors and linear propagation
│
├─ "I can tell you whether my predictions match real Perturb-seq"
│   └─ TRADE for the grading layer (and know that 60-85% of signal is sub-threshold)
│
├─ "I can predict what a non-coding variant does to a cell state"
│   └─ THE WIKI CANNOT YET DO THIS HONESTLY
│       closest: dubuc-2026 (variant → cell type via FM)
│                deng-2024 (variant → enhancer activity via MPRA)
│                combined they suggest a pipeline; no single paper delivers it
│
└─ "I can explain the biophysics of the transcriptional change"
    └─ Monod (burst frequency vs. burst size decomposition)
```

---

## Open Problems

1. **No wiki-level benchmark across claim levels**: level-2 (scGPT, Squidiff, PerturBERT) and level-3 (CellOracle) methods have never been compared on the same Perturb-seq dataset graded with TRADE. The field does not know which matters more: better representation learning (level 2) or better causal operators (level 3).

2. **The variant-to-cell-state gap**: closing this requires base-editing screens × scRNA-seq or allelic-expression × scRNA-seq. Neither is in this wiki. Until they are, all "variant interpretation" via this wiki's tools is at best *cell-type localization* — which risk variants act in which cell types — not *mechanism*.

3. **GRN quality is the limiting factor for level 3**: CellOracle-style causal operators inherit their entire causal claim from the upstream GRN. Motif-based priors are better than co-expression-only priors, but neither is validated at single-perturbation granularity. Brain-specific GRNs ([[brain-development/fleck-2023-inferring-perturbing-cell-fate]], [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction]], [[brain-development/ding-2026-dissecting-gene-regulatory-networks]]) are a partial answer, but have not been compared at the operator level.

4. **Statistical grounding of foundation-model predictions**: scGPT and scFoundation are evaluated by MSE and correlation against observed perturbations. TRADE's analysis of Perturb-seq noise suggests these metrics overestimate performance because they are dominated by a small fraction of large-effect genes. A TRADE-style reanalysis of FM perturbation benchmarks is missing.

5. **The perturbation-to-update step of the atlas loop is unbuilt**: no paper in this wiki demonstrates the full loop (reference → predict → Perturb-seq → update reference) end-to-end. The components exist; the loop does not.

---

## Summary in One Paragraph

"Perturbation prediction" is not one task — it is three overlapping tasks with different epistemic standards. Descriptive dynamics (Palantir, CellRank, moscot, Monod) are level 1; latent-space pattern learners (scGPT, scFoundation, Squidiff, PerturBERT, PrePR-CT) are level 2; causal operators (CellOracle and its GRN cousins) are level 3 by design but depend on GRN quality for their causal standing. Gene-level Perturb-seq and CRISPR KO screens occupy the ground truth position but cannot stand in for variant-level effects, which remain the central unsolved problem — no method in this wiki closes the gap between a non-coding GWAS hit and a cell-state change in a developmentally specific context. Put back into the [[overviews/atlas-as-hypothesis-engine]] loop, the wiki can support every step except the variant-to-cell-state prediction and the end-to-end closed loop itself.

---

*Sources: [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]], [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]], [[single-cell-dl/lange-2022-cellrank-for-directed-single]], [[single-cell-dl/setty-2019-characterization-of-cell-fate]], [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]], [[single-cell-dl/klein-2025-mapping-cells-through-time]], [[single-cell-dl/vinyard-2025-learning-cell-dynamics-with]], [[single-cell-dl/gorin-2025-monod-model-based-discovery]], [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna]], [[single-cell-dl/ergen-2024-consensus-prediction-cell]], [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]], [[single-cell-dl/dedonno-2023-population-level-integration-of]], [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]], [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]], [[single-cell-foundation/hao-2024-large-scale-foundation-model]], [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]], [[drug-resistance/alsulami-2026-predicting-and-interpreting-cell]], [[drug-resistance/chen-2022-deep-transfer-learning-of]], [[drug-resistance/antonopoulos-2026-zero-shot-prediction-of-drug]], [[brain-development/fleck-2023-inferring-perturbing-cell-fate]], [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction]], [[brain-development/ding-2026-dissecting-gene-regulatory-networks]], [[brain-development/dibella-2021-molecular-logic-of-cellular]], [[genomic-dl/zinati-2024-groundgan-grn-guided]], [[genomic-dl/deng-2024-massively-parallel-regulatory]], [[neuroscience/jin-2020-in-vivo-perturb-seq]], [[neuroscience/amelan-2026-crispr-knockout-screens-reveal]], [[neuroscience/paulsen-2022-autism-genes-converge]], [[neuroscience/jourdon-2023-modeling-idiopathic-autism]], [[neuroscience/dubuc-2026-linking-rare-variants-cell-type]], [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]], [[brain-atlas/braun-2023-comprehensive-cell-atlas-first]]*
