---
title: "Beyond Canonical Markers: Cell Identity as Program Performance and Trajectory"
type: overview
created: 2026-04-11
category: overviews
tags: [cell-identity, gene-program, module, maturation, trajectory, canonical-marker, PCA, NMF, cNMF, SJD, NeMO, WGCNA, foundation-model, neurodevelopment]
papers:
  - brain-development/sonthalia-2026-nemo-analytics-compendium
  - brain-development/trevino-2020-chromatin-accessibility-forebrain
  - brain-development/mannens-2025-chromatin-accessibility-during
  - brain-development/herring-2022-human-prefrontal-cortex-gene
  - brain-development/uzquiano-2022-proper-acquisition-cell-class
  - brain-development/zhang-2025-pfc-single-cell-spatiotemporal
  - brain-development/zhang-2025-spatial-dynamics-brain-development
  - brain-development/dibella-2021-molecular-logic-of-cellular
  - brain-development/nano-2025-integrated-analysis-molecular
  - brain-development/gordon-2021-long-term-maturation-of
  - brain-development/bhaduri-2020-cell-stress-cortical-organoids
  - brain-development/kanton-2019-organoid-single-cell-genomic
  - brain-development/fleck-2023-inferring-perturbing-cell-fate
  - brain-development/zenk-2024-single-cell-epigenomic-reconstruction
  - brain-development/ding-2026-dissecting-gene-regulatory-networks
  - brain-development/amiri-2018-transcriptome-epigenome-landscape
  - brain-development/jain-2025-morphodynamics-human-early
  - brain-development/keefe-2025-lineage-resolved-atlas-developing
  - brain-development/wang-2025-molecular-cellular-dynamics
  - brain-development/liu-2025-human-specific-enhancer-fine
  - brain-atlas/braun-2023-comprehensive-cell-atlas-first
  - brain-atlas/yao-2023-high-resolution-transcriptomic-spatial
  - brain-atlas/langlieb-2023-molecular-cytoarchitecture-of
  - brain-atlas/zhang-2023-molecularly-defined-spatially
  - brain-atlas/he-2024-integrated-transcriptomic-cell-atlas
  - brain-atlas/corrigan-2025-conservation-and-alteration
  - brain-atlas/gao-2025-continuous-cell-type-diversification
  - brain-atlas/chen-2025-whole-cortex-in-situ
  - single-cell-dl/setty-2019-characterization-of-cell-fate
  - single-cell-dl/lange-2022-cellrank-for-directed-single
  - single-cell-dl/lopez-2018-deep-generative-modeling-for
  - single-cell-dl/korsunsky-2019-fast-sensitive-and-accurate
  - single-cell-dl/liu-2024-discovery-of-optimal-cell
  - single-cell-dl/luecken-2022-benchmarking-atlas-level-data
  - single-cell-dl/schuster-2024-multidgd-versatile-deep
  - single-cell-foundation/cui-2024-scgpt-toward-building-foundation
  - single-cell-foundation/hao-2024-large-scale-foundation-model
  - single-cell-foundation/heimberg-2025-cell-atlas-foundation-model
  - genomic-dl/zemke-2023-conserved-and-divergent-gene
  - neuroscience/paulsen-2022-autism-genes-converge
  - neuroscience/jourdon-2023-modeling-idiopathic-autism
  - neuroscience/mato-blanco-2025-early-developmental-origins
  - neuroscience/schafer-2019-pathological-priming-causes
  - neuroscience/dony-2025-glucocorticoid-amplifies-inhibitory
  - neuroscience/li-2023-single-cell-brain-organoid
  - neuroscience/martinscosta-2024-arid1b-controls-transcriptional
  - neuroscience/jin-2020-in-vivo-perturb-seq
---

## Why This Overview Exists

Canonical markers — *SOX2 for radial glia, SATB2 for upper-layer callosal projection neurons, BCL11B for subcerebral projection neurons* — are the language cell biologists use to talk about identity. They are useful and concise, but they are a **label for early commitment**, not a measure of how deeply a cell is performing that identity right now.

A radial glial cell that has just turned on *SOX2* and a radial glial cell two days into neurogenesis with the full neurogenic program running at peak are both "SOX2+ APs." A marker-centric view says they are the same cell type. Almost every recent developmental atlas in this wiki says they are not: they are two points on a trajectory of **gene program performance**, and the thing that distinguishes them is not markers but the coordinated activity of modules of genes.

This overview argues that developmental cell identity is better represented as **the level and stability of gene program performance along a trajectory** than as the presence or absence of marker genes. It is the extended version of [[overviews/atlas-as-hypothesis-engine#4.-Canonical-markers-vs.-gene-programs-and-trajectories]] — that section made the claim; this overview builds it out using the wiki's developmental atlases, a history of how module-extraction methods evolved (PCA → NMF → cNMF → joint decomposition → foundation-model embeddings), and the tools currently pushing the frontier.

- **Part I** — Why canonical markers stop at the door
- **Part II** — What a gene program is, how we learned to extract them, and why the methods keep upgrading
- **Part III** — Identity has more than one axis: specification, maturation, plasticity
- **Part IV** — What the program view changes for cross-species, disease, and atlas construction

---

# Part I — Why Canonical Markers Stop at the Door

## 1. Markers detect commitment, not performance

A marker gene answers a binary question: *has this cell crossed a commitment threshold?* It does not answer: *how far along the program is it, and how stably is it running?* These are orthogonal questions, and neurodevelopment has a lot of cells sitting between "committed" and "mature" where the markers say yes but the biology is still in motion.

[[brain-development/uzquiano-2022-proper-acquisition-cell-class]] names this explicitly: "**proper acquisition of cell class identity**" is a *process*, not an assignment. Cortical organoids that miss the process produce cells that a classifier will happily label SATB2+ CPN — but whose full program execution is broken. The marker is on; the identity is not being performed. [[brain-development/bhaduri-2020-cell-stress-cortical-organoids]] names the failure mode: stress programs displace identity programs in organoids, without changing the marker labels.

## 2. Expression lags chromatin — by the time a marker is on, the decision was already made

[[brain-development/trevino-2020-chromatin-accessibility-forebrain]] and [[brain-development/mannens-2025-chromatin-accessibility-during]] both show that chromatin accessibility changes precede the transcriptional signatures of the same neuronal class. The regulatory decision is committed when enhancers open. Expression — and therefore the marker gene — follows. A marker-based view of identity is systematically **late**.

[[brain-development/fleck-2023-inferring-perturbing-cell-fate]], [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction]], and [[brain-development/ding-2026-dissecting-gene-regulatory-networks]] use this to invert the framing: gene regulatory networks reconstructed from chromatin *and* expression are the correct primitive for brain-organoid fate decisions, not the downstream marker.

## 3. Markers are not conserved across species; programs often are

[[brain-atlas/corrigan-2025-conservation-and-alteration]] shows that the same cortical cell class expresses different marker genes in human, macaque, and mouse — even when the underlying gene program is conserved. [[brain-development/kanton-2019-organoid-single-cell-genomic]] makes the same point on the organoid side. [[genomic-dl/zemke-2023-conserved-and-divergent-gene]] extends the evidence to the regulatory level: ~80% of human-specific cis-regulatory elements are TE-derived, but the regulatory *syntax* (the program structure) is preserved rodent→primate. If you insist on markers, every comparative study produces a forest of false species differences. If you work at the program level, the conservation becomes visible.

## 4. NS-Forest is the honest way to use markers

[[single-cell-dl/liu-2024-discovery-of-optimal-cell]] systematizes the process of finding *combinations* of markers that approximate a program. Its key metric — **On-Target Fraction** — asks how exclusively a marker is expressed in its assigned type. The need for this method is itself an admission that no single marker is adequate: you always need *combinations*, and even then the combinations are proxies for something that could be measured more directly.

---

# Part II — Gene Programs as the Alternative

## 5. What a gene program actually is

A gene program (or module) is a **coordinated set of genes whose activity varies together across cells, conditions, or time** because they share a regulatory input. The unit of analysis shifts from "is gene X expressed?" to "is module M active, and at what level?"

Programs are:

- **Continuous** — each cell has an activity level, not a yes/no.
- **Multiple per cell** — a cell runs many programs simultaneously (cell cycle, identity, stress, metabolism), which can be disentangled.
- **Transferable** — a program defined in one dataset can (sometimes) be scored in another.
- **Interpretable at the biology level** — a module can be annotated with TFs, pathways, or chromatin features.

## 6. A brief conceptual history: from PCA to joint decomposition to foundation models

The "cells as combinations of programs" framing is not new — it has been the implicit workhorse of single-cell analysis since the beginning. What has changed is the flexibility, scale, and reproducibility of the decomposition. The lineage:

### 6.1 PCA — the implicit first version
Every standard scRNA-seq pipeline begins with PCA on log-normalized counts. PCA is a linear matrix decomposition; its top components *are* the first gene programs the analyst ever sees, and clustering, UMAP, and kNN graphs are all downstream of that basis. [[single-cell-dl/korsunsky-2019-fast-sensitive-and-accurate]] (Harmony) operates on PCA embeddings to correct batch while preserving biology — treating the PCA basis as the unit of analysis. The silent assumption is that real biological programs live in the top ~20-50 principal components. PCA's limits are that (a) components can be negative (no clean "on/off" interpretation), (b) orthogonality forces spurious independence between genuinely correlated programs, and (c) no sharing across datasets.

### 6.2 WGCNA and co-expression modules — the bulk-era parent
Weighted Gene Co-expression Network Analysis (WGCNA) built correlation-based gene modules from bulk RNA-seq years before single-cell. It survives in the wiki in bulk-style module analyses: [[brain-development/amiri-2018-transcriptome-epigenome-landscape]] identifies co-expression modules and regulatory elements jointly across human cortical development; [[neuroscience/paulsen-2022-autism-genes-converge]] and [[neuroscience/jourdon-2023-modeling-idiopathic-autism]] both rely on module-level convergence analyses for ASD genes. WGCNA's single-cell descendants (hdWGCNA etc.) are not yet in the wiki but the *conceptual* primitive — cells × module activity instead of cells × genes — is already the operating framework for these autism studies.

### 6.3 NMF and cNMF — interpretable, non-negative, consensus-based
Non-negative matrix factorization forces factors to be non-negative, which gives them a natural "amount of program" interpretation: gene loadings are ≥0 and cell activities are ≥0, so a factor is literally "a set of genes that are co-expressed at some level." **Consensus NMF (cNMF, Kotliar 2019)** added a stability criterion — run NMF many times with different initializations, keep only the factors that reproduce across runs. This was the first widely-used method that tried to distinguish genuine programs from initialization artifacts. cNMF is not directly represented as a primary paper in this wiki, but its conceptual descendants are — most prominently NMF-based joint decomposition (§6.5 below).

### 6.4 VAE latents and nonlinear module extractors
[[single-cell-dl/lopez-2018-deep-generative-modeling-for]] (scVI) introduced variational autoencoders for scRNA-seq. The latent dimensions of scVI are, in effect, nonlinear generalizations of NMF factors — learned axes of coordinated gene activity, now allowed to be non-orthogonal and nonlinear. [[single-cell-dl/schuster-2024-multidgd-versatile-deep]] (multiDGD) extends this to joint RNA+ATAC latents, which are simultaneously program extractors *and* integration operators. These methods made gene programs scale to millions of cells, but at the cost of interpretability: the latent axes do not always correspond to nameable biology.

### 6.5 Joint decomposition across datasets — NeMO, SJD, meta-modules
Running any of the above on a single dataset gives factors that are partly real, partly dataset-specific. The decisive recent move is **joint decomposition**: force the factorization to find components that are reproducible across many studies. [[brain-development/sonthalia-2026-nemo-analytics-compendium]] is the clearest example — joint NMF-based matrix decomposition across **~200 neocortical development studies** spanning mouse, macaque, and human. Running NMF separately on each dataset gives different factors every time; joint decomposition forces reproducibility, which is the operational definition of a "real" program.

[[brain-development/nano-2025-integrated-analysis-molecular]] runs a parallel meta-analytic approach across 23 human cortical datasets, extracting 500+ reproducible co-expression meta-modules and using them to identify FEZF2+TSHZ3 as drivers of deep-layer specification (validated in chimeroids).

Both papers share the same methodological move: **cross-dataset reproducibility is the criterion that separates programs from noise**. This is the most consequential upgrade over single-study NMF — it converts NMF from an exploratory tool into a cross-study shared vocabulary.

### 6.6 Foundation-model embeddings — implicit programs at scale
The most recent development is that large pretrained transformers produce cell embeddings which can be read as *implicit* gene program representations. [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] (scGPT, 33M+ cells), [[single-cell-foundation/hao-2024-large-scale-foundation-model]] (scFoundation, 50M+ cells), and [[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]] (SCimilarity, 23.4M cells across 412 studies) all produce high-dimensional embeddings that encode program activity without ever explicitly extracting named programs. They are the current top of the lineage in terms of scale; they are also the least interpretable, because the "programs" are distributed across thousands of dimensions with no native link to biology. Whether FM embeddings can be *converted* back into interpretable module structures is an open question — one that the wiki does not yet answer.

## 7. The method landscape today

| Approach | Representative papers | Interpretability | Cross-dataset sharing |
|----------|----------------------|------------------|------------------------|
| PCA / linear embedding | Every standard pipeline; [[single-cell-dl/korsunsky-2019-fast-sensitive-and-accurate]] Harmony | Low (signed, orthogonal) | Via reference projection |
| WGCNA / co-expression modules | [[brain-development/amiri-2018-transcriptome-epigenome-landscape]], [[neuroscience/paulsen-2022-autism-genes-converge]], [[neuroscience/jourdon-2023-modeling-idiopathic-autism]] | High (named modules) | Limited, per-study |
| NMF / cNMF / topic models | Predecessor to [[brain-development/sonthalia-2026-nemo-analytics-compendium]] | High | Single-dataset only unless joint |
| Joint NMF / meta-modules | [[brain-development/sonthalia-2026-nemo-analytics-compendium]] NeMO, [[brain-development/nano-2025-integrated-analysis-molecular]] | High | **Yes — by construction** |
| VAE latent factors | [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] scVI, [[single-cell-dl/schuster-2024-multidgd-versatile-deep]] multiDGD | Medium (unnamed axes) | Via reference mapping |
| GRN-derived programs | [[brain-development/fleck-2023-inferring-perturbing-cell-fate]], [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction]], [[brain-development/ding-2026-dissecting-gene-regulatory-networks]] | High (TF → target) | Per-dataset, GRN-dependent |
| Trajectory-resolved program activity | [[single-cell-dl/setty-2019-characterization-of-cell-fate]] Palantir, [[single-cell-dl/lange-2022-cellrank-for-directed-single]] CellRank | Medium (fate-aligned gene trends) | Limited |
| Foundation-model embeddings | [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] scGPT, [[single-cell-foundation/hao-2024-large-scale-foundation-model]] scFoundation, [[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]] SCimilarity | Low (distributed) | **Yes — pretrained at scale** |

**The two qualitatively different moves in this history**: (a) going non-negative (NMF) gave interpretability, (b) going joint across datasets (NeMO, meta-modules) gave reproducibility. Foundation models are adding scale, but the interpretability step is not yet made — the field is missing a "joint interpretable FM decomposition" that combines all three.

---

# Part III — Identity Has More Than One Axis

## 8. Specification and maturation are separable — and this is the central empirical finding

The cleanest empirical support for separating identity axes is in [[brain-development/sonthalia-2026-nemo-analytics-compendium]]: **layer-specific maturation programs are protracted and dissociated from early TF specification**. Layer-specific TFs are expressed early; the full layer-specific maturation program runs late and for a long time. A cell can be specified as "deep-layer excitatory neuron" at E14 and still be decades away from fully performing that identity.

This is not a small point. It means:

- **Marker-based identity is a test for specification, not maturation**.
- **Two cells with the same marker can be at radically different depths of program performance**.
- **Organoid deficits are usually maturation, not specification** — Sonthalia shows organoids broadly recapitulate specification but **miss layer-specific maturation programs**, consistent with [[brain-development/gordon-2021-long-term-maturation-of]] (year-long maturation required for human cortical neurons) and [[brain-development/bhaduri-2020-cell-stress-cortical-organoids]] (stress signatures correlate with stalled maturation).

[[neuroscience/schafer-2019-pathological-priming-causes]] adds a disease-relevant twist: in idiopathic ASD iPSC-derived NSCs, late developmental gene networks are activated *prematurely* — heterochronicity at the program level. The programs are correctly identified but their temporal execution is broken.

## 9. Trajectory position as a continuous identity coordinate

[[brain-development/dibella-2021-molecular-logic-of-cellular]] argues that apical progenitors form a continuum ordered by **age**, not by future subtype — projection neurons diversify post-mitotically, not via pre-committed progenitors. The correct coordinate for "what is this AP?" is not a subtype label; it is a position on a trajectory + an age.

[[brain-development/herring-2022-human-prefrontal-cortex-gene]] extends this to human PFC: cell-type distinctions are sharpest in adults. In development, the same program unfolds gradually across weeks, and pseudotime position is as informative as cell-type label. [[brain-development/zhang-2025-pfc-single-cell-spatiotemporal]] gives the spatiotemporal view. [[brain-development/wang-2025-molecular-cellular-dynamics]] and [[brain-development/zhang-2025-spatial-dynamics-brain-development]] add spatially resolved program dynamics.

[[brain-atlas/gao-2025-continuous-cell-type-diversification]] names the phenomenon in its title: **continuous cell type diversification**. [[brain-atlas/braun-2023-comprehensive-cell-atlas-first]] (first-trimester human brain atlas), [[brain-atlas/yao-2023-high-resolution-transcriptomic-spatial]] (BICCN whole mouse brain), [[brain-atlas/langlieb-2023-molecular-cytoarchitecture-of]], and [[brain-atlas/zhang-2023-molecularly-defined-spatially]] all provide the large-scale reference atlases that make trajectory-based coordinates tractable at scale. [[brain-development/keefe-2025-lineage-resolved-atlas-developing]] adds lineage resolution on top. [[brain-development/jain-2025-morphodynamics-human-early]] connects trajectory position to morphodynamic state. [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]] (HNOCA) is the organoid-side reference that puts trajectory coordinates into routine use for query mapping.

Discrete labels are a projection of a continuous object; the underlying object is program activity along a trajectory.

## 10. Plasticity / differentiation potential as a third axis

[[single-cell-dl/setty-2019-characterization-of-cell-fate]] Palantir introduced **differentiation potential (DP)** as the entropy of a cell's fate probability vector — a single scalar for "how plastic is this cell?" [[single-cell-dl/lange-2022-cellrank-for-directed-single]] CellRank extended this to systems without canonical hierarchies. DP is orthogonal to identity label: two cells can both be radial glia and have very different DP, which is a meaningful biological distinction that markers cannot express.

So developmental cell identity is at minimum a **three-coordinate quantity**:

1. **Specification** — which trajectory the cell is on (what markers approximate).
2. **Maturation** — how deeply the cell is performing its program (what cNMF / joint NMF / NeMO / GRN-based methods capture).
3. **Plasticity** — how committed the cell is to that trajectory (what Palantir DP measures).

Using markers alone collapses all three onto a single binary.

---

# Part IV — What the Program View Changes

## 11. Cross-species comparison becomes meaningful

When you compare species by markers you find false differences. When you compare by programs you find real ones. [[brain-development/sonthalia-2026-nemo-analytics-compendium]]'s primate-specific oRG program is the clearest case: no species-specific marker gene, but a species-specific coordinated module active in that progenitor population. [[brain-development/kanton-2019-organoid-single-cell-genomic]] and [[brain-atlas/corrigan-2025-conservation-and-alteration]] find the same pattern — conservation of classes, modification of programs, heterochrony of timing. [[genomic-dl/zemke-2023-conserved-and-divergent-gene]] shows the same at the regulatory level: species-specific enhancers modify a conserved regulatory program structure. [[brain-development/liu-2025-human-specific-enhancer-fine]] shows that human-specific enhancers fine-tune existing programs in existing cell classes — not define new classes.

**"Human brain is special" is a program-level claim, not a marker-level claim.**

## 12. Disease convergence happens at the program level

[[neuroscience/paulsen-2022-autism-genes-converge]] shows that three ASD genes (KMT5B, ARID1B, CHD8) converge on **asynchronous GABAergic/excitatory development** — a program-level phenotype. The genes are different, the cell types they act in overlap incompletely, but the program-level outcome is the same. [[neuroscience/jourdon-2023-modeling-idiopathic-autism]] extends this to idiopathic ASD: different individuals show divergent E/I balance at the program level without any single shared risk gene.

The pattern repeats across the wiki's ASD / NDD literature:

- [[neuroscience/jin-2020-in-vivo-perturb-seq]]: 35 ASD/ND risk genes perturbed in mouse cortex collapse to **14 gene modules** across neuronal and glial cells — the 14 modules are the convergent unit, not the 35 genes.
- [[neuroscience/martinscosta-2024-arid1b-controls-transcriptional]]: ARID1B haploinsufficiency disrupts **transcriptional programs** of corpus callosum development, with axon projection as the downstream program-level phenotype.
- [[neuroscience/li-2023-single-cell-brain-organoid]] (CHOOSE): pooled CRISPR screen of 36 ASD risk genes in mosaic organoids — dorsal IPs + ventral progenitors emerge as the cell-type × program windows where risk converges.
- [[neuroscience/dony-2025-glucocorticoid-amplifies-inhibitory]]: chronic glucocorticoid exposure amplifies an inhibitory-neuron program via PBX3, with lasting dysregulation of ASD-risk-gene programs — environmental × genetic convergence at the program level.
- [[neuroscience/mato-blanco-2025-early-developmental-origins]]: neuropsychiatric risk genes converge on brain-organizer hub TFs; TF depletion simulation produces program-level phenotypes seen in ASD patient NSCs.
- [[neuroscience/schafer-2019-pathological-priming-causes]]: heterochronic activation of late programs in idiopathic ASD NSCs — the programs are the invariants, the timing is disrupted.

**Six independent studies, one pattern**: disease mechanisms are not "gene X is broken in cell type Y." They are "program M is mis-timed or mis-balanced across a set of related cell types." A marker-based analysis will see unrelated genes in unrelated types; a program-based analysis will see convergence.

## 13. Atlas construction changes shape

A marker-based atlas is a `cell_id → cell_type_label` table. A program-based atlas stores:

- Trajectory position (pseudotime / fate probability).
- Program activity vector (one scalar per module, at scale).
- Differentiation potential.
- Chromatin priming state (where available).

This is a much richer reference, and it is exactly what the [[overviews/atlas-as-hypothesis-engine]] overview argued an atlas should become. A query cell projected onto such a reference can be asked: *on which trajectory? at what maturation depth? with what plasticity? which programs are off-reference?* None of these questions are answerable against a label-based reference.

## 14. Perturbation interpretation changes too

[[overviews/perturbation-prediction-and-causal-inference]] distinguished descriptive / generative / causal claims. Adding the program view sharpens the descriptive level: instead of asking "does perturbation move cells to new clusters?", you ask "which programs are modulated, and in which direction?" This is a natural language for interpreting Perturb-seq, CellOracle simulations, and foundation-model perturbation predictions, because programs are stable cross-dataset and interpretable in terms of biology. [[neuroscience/jin-2020-in-vivo-perturb-seq]]'s collapse of 35 ASD genes into 14 modules is exactly this move — the Perturb-seq readout becomes useful only once it is reframed as a program-level signal.

---

## Decision Guide: When to Use Markers vs. Programs

```
What am I trying to say about this cell?
│
├─ "It crossed a commitment threshold"
│   └─ Markers are fine (SOX2+, SATB2+, etc.)
│
├─ "It is a specific discrete type in an adult atlas"
│   └─ Markers + NS-Forest combinations are fine
│       (adult tissues have sharper type boundaries)
│
├─ "It is somewhere on a developmental trajectory"
│   └─ Trajectory position + pseudotime (Palantir, CellRank)
│
├─ "It is deeply / shallowly executing its identity"
│   └─ Program activity from NMF / cNMF / joint NMF
│       (NeMO-style joint decomposition)
│       + maturation module scores
│
├─ "It is plastic / committed"
│   └─ Palantir differentiation potential (entropy of fate probabilities)
│
├─ "It differs from a reference in a meaningful, cross-dataset way"
│   └─ Module-level deviation, not single-gene DE
│       (meta-module or joint-NMF framework)
│
├─ "It is aberrant in a disease-relevant way"
│   └─ Program convergence analysis — different genes, same module
│       (every ASD convergence paper in this wiki lands here)
│
└─ "I need cross-study comparison at scale, interpretability is secondary"
    └─ Foundation model embedding (scGPT, scFoundation, SCimilarity)
       — but know that you are working with unnamed, distributed programs
```

---

## Open Problems

1. **Module stability vs. dataset artifacts**: the operational definition of a "real" program is cross-dataset reproducibility ([[brain-development/sonthalia-2026-nemo-analytics-compendium]], [[brain-development/nano-2025-integrated-analysis-molecular]]). But how many datasets are enough, and how do you know a reproducible module isn't a shared technical artifact (batch, kit, lab)? No rigorous test exists in the wiki.

2. **Quantifying maturation depth**: the concept is clear, the metric is not. Sonthalia shows maturation programs run late and long; nobody in the wiki has proposed a single-number "maturation depth" that is comparable across cell types and datasets. Palantir DP measures plasticity (which is related but distinct); a principled maturation metric is missing.

3. **Dynamic modules that reconfigure**: joint NMF assumes a fixed set of programs across the data it decomposes. Developmental programs actually **reconfigure** — the same TFs can participate in different modules at different stages. No method in the wiki handles this natively.

4. **Specification vs. maturation as formally separable axes**: Sonthalia 2026 shows this empirically in cortical development. Whether it generalizes to other tissues (hematopoiesis, gut, immune) is not tested in the wiki.

5. **Programs vs. causal GRNs**: a program is a statistical pattern; a GRN is a causal claim ([[overviews/perturbation-prediction-and-causal-inference]] Part III). The relationship — whether every reproducible program corresponds to a coherent regulatory sub-network, or whether programs can exist without clean GRN explanations — is not systematically analyzed.

6. **Foundation models have not been made interpretable as programs**: scGPT, scFoundation, SCimilarity produce cell embeddings that implicitly encode program activity, but no wiki paper extracts interpretable named modules from these embeddings. Combining NMF-style interpretability with FM-scale pretraining is an open frontier.

7. **Marker-based classifiers still dominate the tooling**: even though the wiki's arguments point at programs, most annotation tools ([[single-cell-dl/aran-2019-reference-based-analysis-of]] SingleR, [[single-cell-dl/dominguez-conde-2022-cross-tissue-immune-cell]] CellTypist) output marker-style labels. The program view has not yet pushed through into the tooling the field actually uses day-to-day.

---

## Summary in One Paragraph

Canonical markers label a cell's early commitment but say nothing about how deeply that cell is performing its identity right now. Recent atlases and decomposition methods — Sonthalia/NeMO's joint NMF across ~200 studies and 3 species, Nano's meta-modules across 23 cortical datasets, Di Bella's age-ordered AP continuum, Herring and Zhang on PFC, Braun and Yao and Langlieb's large reference atlases — all push toward the same conclusion: developmental identity is a **continuous, multi-axis quantity** with at least three components (specification, maturation, plasticity), each of which needs a different measurement. The methodological lineage (PCA → WGCNA → NMF → cNMF → joint NMF/NeMO → VAE latents → foundation-model embeddings) shows that each upgrade added either interpretability or reproducibility, and the current frontier is combining both. The strongest empirical finding is that **specification and maturation are separable**: layer-specific TFs fire early, but the layer-specific maturation program runs late and for a long time, and this is where organoid models fall short. The program-level view is also what makes cross-species comparison and disease convergence meaningful — every ASD convergence paper in this wiki lands at the module level, not the gene level. This overview expands on [[overviews/atlas-as-hypothesis-engine#4.-Canonical-markers-vs.-gene-programs-and-trajectories]] and feeds into [[overviews/perturbation-prediction-and-causal-inference]] by framing perturbations as modulations of programs rather than changes to labels.

---

*Sources: [[brain-development/sonthalia-2026-nemo-analytics-compendium]], [[brain-development/trevino-2020-chromatin-accessibility-forebrain]], [[brain-development/mannens-2025-chromatin-accessibility-during]], [[brain-development/herring-2022-human-prefrontal-cortex-gene]], [[brain-development/uzquiano-2022-proper-acquisition-cell-class]], [[brain-development/zhang-2025-pfc-single-cell-spatiotemporal]], [[brain-development/zhang-2025-spatial-dynamics-brain-development]], [[brain-development/dibella-2021-molecular-logic-of-cellular]], [[brain-development/nano-2025-integrated-analysis-molecular]], [[brain-development/gordon-2021-long-term-maturation-of]], [[brain-development/bhaduri-2020-cell-stress-cortical-organoids]], [[brain-development/kanton-2019-organoid-single-cell-genomic]], [[brain-development/fleck-2023-inferring-perturbing-cell-fate]], [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction]], [[brain-development/ding-2026-dissecting-gene-regulatory-networks]], [[brain-development/amiri-2018-transcriptome-epigenome-landscape]], [[brain-development/jain-2025-morphodynamics-human-early]], [[brain-development/keefe-2025-lineage-resolved-atlas-developing]], [[brain-development/wang-2025-molecular-cellular-dynamics]], [[brain-development/liu-2025-human-specific-enhancer-fine]], [[brain-atlas/braun-2023-comprehensive-cell-atlas-first]], [[brain-atlas/yao-2023-high-resolution-transcriptomic-spatial]], [[brain-atlas/langlieb-2023-molecular-cytoarchitecture-of]], [[brain-atlas/zhang-2023-molecularly-defined-spatially]], [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]], [[brain-atlas/corrigan-2025-conservation-and-alteration]], [[brain-atlas/gao-2025-continuous-cell-type-diversification]], [[brain-atlas/chen-2025-whole-cortex-in-situ]], [[single-cell-dl/setty-2019-characterization-of-cell-fate]], [[single-cell-dl/lange-2022-cellrank-for-directed-single]], [[single-cell-dl/lopez-2018-deep-generative-modeling-for]], [[single-cell-dl/korsunsky-2019-fast-sensitive-and-accurate]], [[single-cell-dl/liu-2024-discovery-of-optimal-cell]], [[single-cell-dl/luecken-2022-benchmarking-atlas-level-data]], [[single-cell-dl/schuster-2024-multidgd-versatile-deep]], [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]], [[single-cell-foundation/hao-2024-large-scale-foundation-model]], [[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]], [[genomic-dl/zemke-2023-conserved-and-divergent-gene]], [[neuroscience/paulsen-2022-autism-genes-converge]], [[neuroscience/jourdon-2023-modeling-idiopathic-autism]], [[neuroscience/mato-blanco-2025-early-developmental-origins]], [[neuroscience/schafer-2019-pathological-priming-causes]], [[neuroscience/dony-2025-glucocorticoid-amplifies-inhibitory]], [[neuroscience/li-2023-single-cell-brain-organoid]], [[neuroscience/martinscosta-2024-arid1b-controls-transcriptional]], [[neuroscience/jin-2020-in-vivo-perturb-seq]]*
