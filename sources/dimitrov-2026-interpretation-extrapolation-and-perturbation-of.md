---
title: "Interpretation, extrapolation and perturbation of single cells"
authors: Daniel Dimitrov, Stefan Schrod, Martin Rohbeck, Oliver Stegle
year: 2026
doi: 10.1038/s41576-025-00920-4
category: single-cell-dl
pdf_path: papers/dimitrov-2026-interpretation-extrapolation-and-perturbation-of.pdf
pdf_filename: dimitrov-2026-interpretation-extrapolation-and-perturbation-of.pdf
source_collection: manual
---

## One-line Summary

A unifying ontology of machine learning methods for single-cell perturbation modelling — organizes ~150 methods along five shared modelling concepts (representation learning, disentanglement, causal inference, mechanistic discovery, population tracing), three aims (understand / extrapolate / guide), and the causal signatures they exploit (observational/interventional × temporal × spatial × multi-omic).

## 1. Document Info

- Journal: Nature Reviews Genetics
- Volume 27, Pages 349–370, May 2026
- Published online: 2 January 2026
- Affiliations: EMBL Heidelberg, DKFZ Heidelberg, Heidelberg University, Wellcome Sanger Institute
- Type: Review article (Stegle lab)

## 2. Key Contributions

- **Unifying ontology** for single-cell causal/mechanistic modelling that connects ~150 methods through five shared concepts and the causal signatures they exploit
- **Three aims framework**: (1) *understand* perturbation effects, (2) *extrapolate* to unseen conditions, (3) *guide* future experiments via experiment-prediction loops
- **Box 1**: defines and contrasts representation learning, disentanglement, causal inference, mechanistic discovery, population tracing — including their assumptions and what they can/cannot infer
- **Tables 1–3**: catalogue interventional technologies (Perturb-seq, FiCS, ECCITE-seq, Mix-seq, Mosaic, Perturb-Map, etc.), computational tasks/methods, and representative method trade-offs
- **Critical evaluation section**: simple linear/additive baselines often match or outperform state-of-the-art deep learning models (including foundation models) on unseen perturbations and combinatorial extrapolation — exposes generalization gap
- **Online resource**: queryable, extendable method catalogue with technical descriptions

## 3. Methods & Architecture

### Three Aims of Causal Modelling (Fig. 2)

1. **Understand** — characterize alteration effects from differential expression → gene programmes → directed causal interactions (increasing complexity)
2. **Extrapolate** — predict counterfactuals across cell types, time, perturbations (single/combinatorial)
3. **Guide** — iterative experiment ↔ model loop where in silico predictions select next wet-lab targets

### Five Shared Modelling Concepts (Box 1)

| Concept | Goal | Core assumption | Key limitation |
|---------|------|-----------------|----------------|
| **Representation learning** | Embed high-dim data into compact latent space | Manifold structure; shared low-dim patterns | Provides associations only, no causal orientation |
| **Disentanglement** | Decompose entangled cellular processes into distinct factors | Variation can be split into independent meaningful components | Identifiability issues; nonlinear methods often fail to recover ground truth |
| **Causal inference** | Estimate intervention effects (Pearl do-calculus) | Adjusted-for confounders; interventions are primary drivers | Causal sufficiency rarely satisfied with transcriptome alone |
| **Mechanistic discovery** | Infer directed regulatory edges (e.g., TF→target) | All variables observed; prior knowledge generalizable; specific interventions | Often fails to recover known regulators even with multi-omics |
| **Population tracing** | Pair counterfactuals via OT/flow matching/Schrödinger bridges | Smooth continuous transitions between snapshots | Suboptimal mappings for highly divergent populations |

### Causal Signatures (Fig. 1)

- **Endogenous (observational)**: natural variation across donors/tissues/disease states (rich but unknown ground truth)
- **Exogenous (interventional)**: CRISPR/drug perturbations (controlled but artificial context, in vitro bias)
- **Temporal axis**: time-series, pseudotime, RNA velocity → directional inference
- **Spatial axis**: spatial transcriptomics → cell-cell signalling, niche effects
- **Multi-omic axis**: ATAC + RNA + protein → upstream-to-downstream regulatory layers

### Computational Tasks Taxonomy (Table 2)

```
Quantify response
├── Differential analysis (CellDrift, MiloDE, LEMUR, Mixscale, ...)
└── Perturbation responsiveness (CINEMA-OT, MELD, Mixscape, MUSIC, ...)

Latent structures
├── Linear gene programmes (MOFA+, MEFISTO, Spectra, GSFA, scITD, ...)
└── Nonlinear (scVI, scArches, ContrastiveVI, scGPT, Geneformer, ...)

Discover mechanisms
├── Feature relationships (Hotspot, MISTy, Celcomen, Memento, ...)
├── Gene regulatory networks (SCENIC+, CellOracle, Dictys, LINGER, scDoRI, ...)
└── Causal structure (NOTEARS, DCDI, Bicycle, SAMS-VAE, RENGE, ...)

Disentanglement
├── Unsupervised (sparseVAE, DRVI, MichiGAN, MOFA+, ...)
├── Contrastive (cPCA, ContrastiveVI, scDisInFact, ...)
└── Multi-component (CPA, Biolord, SAMS-VAE, SOFA, GSFA, ...)

Predict effects
├── Context transfer (scGEN, CPA, ChemCPA, PrePR-CT, CellOT, MoscOT, ...)
├── Seen perturbations (trVAE, Dr.VAE, scPreGan, LEMUR, ...)
├── Unseen perturbations (GEARS, ChemCPA, CODEX, scGPT, scFoundation, ...)
└── Combinatorial (CPA, GEARS, AttentionPert, SAMS-VAE, SALT&PEPER, State, ...)

Trace populations
└── OT/flow/Schrödinger (CINEMA-OT, CellOT, moscot, Waddington-OT, scPRAM, Prescient, OT-CFM, ...)
```

### Interventional Technologies (Table 1)

| Technology | Cells (n) | Perturbations (n) | Modality |
|------------|-----------|-------------------|----------|
| Perturb-seq | 10K – several million | 100 – 10,000 (genome-scale) | RNA |
| FiCS Perturb-seq | ~8M (2 expts) | All protein-coding genes | RNA (deep) |
| ECCITE-seq | 10Ks | up to 100 | RNA + protein + clonotype |
| Perturb-Multi | 55K (seq) / 79K (img) | ~200 | RNA + protein + spatial |
| Mosaic platform | ~100M | 379 drugs / 1,100 dose-combos | RNA, 50 cell lines |
| Perturb-Map | Millions | 30–40 | RNA + protein + imaging |
| CRISPRmap | 100Ks | 100s | RNA + protein + imaging |

### Trade-offs of Representative Methods (Table 3 abridged)

| Method | Concepts | Application | Trade-off |
|--------|----------|-------------|-----------|
| Mixscale | Causal inference | Perturb-seq across 6 cell lines | More power but downweights weak perturbations |
| CINEMA-OT | Population tracing + disentanglement + repr. learning + causal inference | Airway organoids, PBMCs | Cannot extrapolate to unmeasured cell types |
| Dictys | Mechanistic discovery (multi-omic, OU process) | Human blood | Unstable across runs |
| GSFA | Repr. learning + causal inference (Bayesian factor) | CRISPR repression in neural progenitors → ASD risk genes | Limited scalability (Gibbs sampling) |
| ContrastiveVI | Disentanglement + repr. learning | Mix-seq, ECCITE-seq | Limited to case-control |
| SAMS-VAE | Disentanglement + causal + repr. learning | CRISPRa screen, unseen combos | Nonlinear → less interpretable |
| scGPT | Repr. learning + causal + mechanistic (fine-tuned) | Perturb-seq | Strong embeddings; interpretation needs post-hoc |
| FLeCS | Mechanistic discovery + population tracing | Myeloid progenitors | Linear GRNs interpretable but miss complex trajectories |
| CellFlow | Population tracing + causal inference | PBMCs, zebrafish KO | Transfers across samples, depends on OT map quality |

## 4. Key Results & Findings

### Generalization Gap (Critical Evaluation)

- Recent benchmarks: simple linear or additive baselines **match or outperform** state-of-the-art specialist and foundation models on:
  - Unseen perturbations (refs 217–221, 246)
  - Combinatorial perturbations (refs 84, 213, 220, 221)
- Foundation models (scGPT, scFoundation, Geneformer) **underperform even after fine-tuning** on unseen conditions (refs 218, 221)
- Likely cause: methods capture systematic confounder differences and selection biases, but miss perturbation specificity and context-dependence
- Partly attributable to suboptimal evaluation metrics (refs 220, 248)

### Prior-Knowledge Caveat

- Performance gains from incorporating biological priors may stem from **implicit network sparsity** rather than the biological information itself (ref 245)
- Curated knowledge biases predictions toward well-studied pathways
- Even multi-omics + perturbational mechanistic methods often fail to recover known regulators (refs 160, 176, 244)

### Practical Recommendations

- Standardized benchmarking: common baselines, biologically relevant metrics, representative datasets, reliable ground truth
- Community challenges (refs 243, 252) and platforms (ref 251) needed for transparency
- Method choice should match: causal signature available × biological question × interpretability requirement

## 5. Limitations & Future Work

### Current Bottlenecks

- **Causal sufficiency rarely satisfied**: post-translational modifications, microenvironment, temporal order typically unmeasured
- **Pseudoreplication and confounding**: technical artefacts (gRNA efficiency, batch) and biological artefacts (cell cycle, lineage)
- **Destructive sequencing**: no paired before/after observations per cell
- **In vitro bias**: most interventional screens in cell lines/iPSCs/organoids — miss tissue-scale dynamics, immune context

### Promising Directions

1. **Integrated multi-signature models**: jointly model spatial + temporal + multi-omic + perturbational data (no method currently does all)
2. **Longitudinal designs**: clonal lineage tracing, live-cell sequencing, microscopy-based profiling for non-destructive temporal resolution
3. **3D spatial mapping at consecutive time points**: spatiotemporal trajectory alignment
4. **In vivo CRISPR + spatial profiling**: Perturb-Map, Perturb-CAST, CRISPRmap for tissue-scale interventional data
5. **Cross-modal prediction**: foundation models bridging gene expression ↔ chromatin ↔ imaging ↔ text
6. **Population genetics + interventional**: integrate natural variants (eQTL, GWAS) with CRISPR atlases for disease variant interpretation
7. **Closed-loop experiment-prediction**: active learning, autonomous agents, agentic workflows

## 6. Related Work (key cross-references in our wiki)

### Foundation models reviewed
- scVI, scANVI, scArches, scPoli, MrVI (scVI ecosystem)
- scGPT, scFoundation, Geneformer (single-cell foundation)
- SCimilarity, EpiAgent, PerturBERT

### Perturbation prediction methods reviewed
- GEARS, PerturbNet, Squidiff, scGen, CPA, ChemCPA, Biolord
- CellOracle (GRN-based perturbation simulation)

### Population tracing / OT
- moscot (cited as key OT framework for single-cell)
- Waddington-OT, Prescient, scPRAM

### Mechanistic / GRN
- CellOracle, SCENIC+, Dictys, scDoRI

### Multi-omic / interventional
- PerturbFate (cited as exemplar of >100K-scale CRISPRi multi-modal screens)
- Monod (biophysical nascent/mature transcript modelling)

### Related reviews
- Pearl 2009 Causality (foundational)
- Schölkopf 2021 "Toward causal representation learning" (ref 10)
- Rood 2025 "Human Cell Atlas: census to foundation model" (ref 2)

## 7. Glossary (paper's own glossary)

- **Agentic workflows**: autonomous multi-agent computational processes for complex tasks
- **Causal graph models**: variables = nodes, causal influences = directed edges
- **Causal mechanisms**: directed molecular interactions through which signals propagate
- **Causal signatures**: observable variables reflecting underlying causal processes
- **Conditional independence**: X ⊥ Y | Z — no info between two vars after conditioning
- **Confounders**: extraneous factors producing spurious associations
- **Counterfactual**: hypothetical outcome under alternative intervention
- **Embeddings**: low-dim vector representations capturing properties
- **Factor models**: observed = linear combinations of latent factors + noise
- **Gene programmes**: coordinated gene sets representing shared functions
- **Identifiable**: parameters uniquely determined from data under model assumptions
- **Latent variable**: hidden, inferred from observable data
- **Optimal transport**: cost-efficient pairing of distributions
- **Pseudotime**: cells ordered along inferred trajectory by similarity
- **RNA velocity**: time derivative of expression, from spliced/unspliced ratio
- **Causal sufficiency**: assumption that all common causes of measured variables are themselves measured
