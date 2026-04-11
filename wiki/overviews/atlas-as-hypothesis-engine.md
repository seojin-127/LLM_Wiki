---
title: "From Catalog to Hypothesis Engine: Atlases, Developmental Identity, and Disease Vulnerability"
type: overview
created: 2026-04-11
category: overviews
tags: [atlas, foundation-model, queryable-reference, neurodevelopment, cell-identity, trajectory, gene-program, cross-species, temporal-architecture, disease-vulnerability]
papers:
  - single-cell-foundation/heimberg-2025-cell-atlas-foundation-model
  - single-cell-foundation/cui-2024-scgpt-toward-building-foundation
  - single-cell-foundation/hao-2024-large-scale-foundation-model
  - single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell
  - single-cell-foundation/szalata-2026-perturbert-learning-gene-co
  - single-cell-dl/lotfollahi-2022-mapping-single-cell-data
  - single-cell-dl/dedonno-2023-population-level-integration-of
  - single-cell-dl/boyeau-2025-deep-generative-modeling-of
  - single-cell-dl/hao-2021-integrated-analysis-of-multimodal
  - brain-atlas/he-2024-integrated-transcriptomic-cell-atlas
  - brain-atlas/braun-2023-comprehensive-cell-atlas-first
  - brain-atlas/yao-2023-high-resolution-transcriptomic-spatial
  - brain-development/trevino-2020-chromatin-accessibility-forebrain
  - brain-development/herring-2022-human-prefrontal-cortex-gene
  - brain-development/mannens-2025-chromatin-accessibility-during
  - brain-development/zhang-2025-pfc-single-cell-spatiotemporal
  - brain-development/fleck-2023-inferring-perturbing-cell-fate
  - brain-development/uzquiano-2022-proper-acquisition-cell-class
  - brain-development/kanton-2019-organoid-single-cell-genomic
  - brain-development/liu-2025-human-specific-enhancer-fine
  - brain-atlas/corrigan-2025-conservation-and-alteration
  - neuroscience/jourdon-2023-modeling-idiopathic-autism
  - neuroscience/paulsen-2022-autism-genes-converge
  - neuroscience/mato-blanco-2025-early-developmental-origins
  - neuroscience/dubuc-2026-linking-rare-variants-cell-type
  - neuroscience/jin-2020-in-vivo-perturb-seq
---

## Why This Overview Exists

The first generation of cell atlases answered "what cell types exist?" The next generation has to answer something harder: *given a new profile, a disease, a perturbation, a species — what does the reference tell me that I couldn't have asked before?*

This overview reframes a set of conceptual questions about atlases, developmental identity, and disease vulnerability in three parts. Each part is answered only from papers already in this wiki.

- **Part I — What an atlas should become**: catalog → queryable foundation, and the role of multimodality
- **Part II — How developmental identity should be defined**: discrete types vs. continuous trajectories, markers vs. programs, and cross-species comparison
- **Part III — Temporal architecture and disease vulnerability**: when and where risk variants act, and why the atlas is a hypothesis engine

---

# Part I — What an Atlas Should Become

## 1. From catalog to queryable foundation

A catalog answers *"does this cell type exist?"* A queryable reference answers *"how does this new sample differ from everything I already know?"* Four concrete questions should be askable:

1. **Deviation** — is this cell state unusual relative to the reference?
2. **Gene program** — which coordinated gene modules are active, not just which marker genes are expressed?
3. **Proportion change** — are some populations depleted or expanded compared to controls?
4. **Perturbation prediction** — if I knock out gene X in this cell type, what happens?

Different tools target different sub-questions:

| Capability | Method | Paper |
|------------|--------|-------|
| Atlas-scale nearest-neighbor query | SCimilarity (23.4M cells, 412 studies) | [[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]] |
| Reference projection + disease-preserving query | scArches (~10K query-specific params, frozen reference) | [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]] |
| Population-level reference with open-world cell types | scPoli (2,375 samples, 7.8M PBMCs) | [[single-cell-dl/dedonno-2023-population-level-integration-of]] |
| Per-cell sample-level distance — which samples differ? | MrVI (counterfactual projection) | [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]] |
| Zero/few-shot gene-program and perturbation inference | scGPT (33M cells), scFoundation (50M+ cells) | [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]], [[single-cell-foundation/hao-2024-large-scale-foundation-model]] |
| Perturbation-signature representation learning | PerturBERT | [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]] |

The concrete change is that a reference is no longer a table of centroids — it is a **model** you can push new data into, ask counterfactuals from, and interrogate for gene-program activity. [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]] (HNOCA) operationalizes this: disease organoid data is projected onto a 1.8M-cell healthy reference via scPoli, and deviation, gene program, and fate-divergence questions are asked on the mapped embedding — not on the raw query.

## 2. Multimodality: different layers for different questions

No single modality is the "best" layer. Each modality reflects biology on a different timescale and is informative for a different type of question. The wiki's multimodal papers converge on the same point: **the right leading indicator depends on the question**.

| Question | Leading indicator | Why | Paper |
|----------|-------------------|-----|-------|
| "Which state will this cell become?" | Chromatin accessibility (scATAC) | Open regions precede expression — primes lineage choice before transcription catches up | [[brain-development/trevino-2020-chromatin-accessibility-forebrain]], [[brain-development/mannens-2025-chromatin-accessibility-during]] |
| "What is this cell doing right now?" | scRNA-seq | Transcription reflects the current steady state | [[brain-atlas/braun-2023-comprehensive-cell-atlas-first]] |
| "What stable identity has been committed?" | DNA methylation | Slow timescale, locks in lineage decisions | [[single-cell-dl/liu-2023-methylome]] (wiki entry), [[single-cell-methylation/...]] generally |
| "Which cell subtype is this really?" (resolving ambiguous RNA states) | RNA + protein (CITE / WNN) | Surface proteins disambiguate states RNA alone cannot separate | [[single-cell-dl/hao-2021-integrated-analysis-of-multimodal]] |
| "What is the regulatory logic driving this state?" | RNA + ATAC jointly | Enables GRN inference, peak-to-gene linkage | [[brain-development/fleck-2023-inferring-perturbing-cell-fate]], [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction]] |

The practical corollary: **if your question is about fate commitment or priming, chromatin leads. If it is about current function or perturbation, RNA leads. If it is about durable identity, methylation leads.** An atlas that only stores one modality implicitly answers only one class of question.

The same lesson shows up in the brain directly. [[brain-development/trevino-2020-chromatin-accessibility-forebrain]] shows that forebrain chromatin accessibility shifts precede the transcriptional signatures of each neuronal class; [[brain-development/mannens-2025-chromatin-accessibility-during]] extends this across cortical development. Using only RNA would have missed the *priming* window where the decision has already been made but has not yet been expressed.

---

# Part II — How Developmental Identity Should Be Defined

## 3. Cell type as category vs. state trajectory

For adult tissues, discrete cell type categories work well enough. For the developing brain, they break down. Several wiki papers argue — with different wording — that developmental identity is better described as a **continuous trajectory of states** than as a membership label.

- [[brain-development/trevino-2020-chromatin-accessibility-forebrain]]: in the developing forebrain, the same radial-glial pool gives rise to a continuum of excitatory neuron states with no clean categorical boundary; chromatin changes are monotone along pseudotime.
- [[brain-development/herring-2022-human-prefrontal-cortex-gene]]: in human PFC from prenatal to adult, cell-type distinctions are sharpest in adults — in development, the same transcriptional program unfolds across weeks.
- [[brain-development/uzquiano-2022-proper-acquisition-cell-class]]: "proper acquisition of cell class identity" is a process, not an assignment — organoids that miss the process produce cells that look like nothing in vivo, even though a classifier will still put a label on them.
- [[brain-development/zhang-2025-pfc-single-cell-spatiotemporal]]: the prefrontal cortex builds itself through overlapping waves, not through spawning discrete type populations in sequence.
- [[brain-atlas/gao-2025-continuous-cell-type-diversification]]: the title says it — **continuous diversification**. Discrete labels are a projection of a continuous object.

The consequence for atlases: a developmental atlas stored as `cell_id → cell_type` throws away exactly the information that matters most. A developmental atlas should store positions in a trajectory, pseudotime, lineage, and the program activities that define them.

## 4. Canonical markers vs. gene programs and trajectories

Canonical markers are a convenient human-interpretable shorthand. They are not the underlying biological unit. The wiki evidence for this is consistent:

- **Markers are late**. By the time a canonical marker is expressed at classifier-friendly levels, the cell has already committed — chromatin opened first ([[brain-development/trevino-2020-chromatin-accessibility-forebrain]], [[brain-development/mannens-2025-chromatin-accessibility-during]]).
- **Markers are noisy across species**. The same cell class expresses different marker genes in human vs. mouse vs. non-human primate, even when the underlying program is conserved ([[brain-atlas/corrigan-2025-conservation-and-alteration]]).
- **Programs transfer, markers do not**. [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] and [[single-cell-foundation/hao-2024-large-scale-foundation-model]] succeed at cross-dataset annotation precisely because they learn gene programs, not marker-based rules.
- **NS-Forest is needed only because markers are a bad primitive**. [[single-cell-dl/liu-2024-discovery-of-optimal-cell]] systematizes the process of finding *combinations* of markers that approximate a program — an admission that no single marker carries the identity.

For developmental cell state, **program activity along a trajectory** is a more faithful representation than "marker X+ marker Y−". An overview page on integration ([[overviews/single-cell-integration-methods]]) and one on annotation ([[overviews/single-cell-annotation-methods]]) both land on the same conclusion from different directions: the useful representation is the embedding and the programs, not the labels.

## 5. Cross-species comparison: new types or modified conserved classes?

The wiki's cross-species papers almost uniformly reject "new human-specific cell types" as the main story. The story is **conserved initial classes with modified programs, timing, or migration**.

- [[brain-development/kanton-2019-organoid-single-cell-genomic]] compares human, chimp, and macaque cortical organoids: the cell-type taxonomy is almost identical; the differences are in **tempo** — human cells spend much longer in progenitor states — and in **program activity**, not in the existence of new classes.
- [[brain-atlas/corrigan-2025-conservation-and-alteration]] explicitly frames its results as "conservation and alteration": the classes are conserved; what changes is their gene programs and spatial distribution.
- [[brain-atlas/hahn-2023-evolution-of-neuronal-cell]]: retinal neuronal classes are largely conserved across vertebrates; species differences are in subtype proportions and program modification, not class invention.
- [[brain-development/liu-2025-human-specific-enhancer-fine]]: human-specific enhancers fine-tune existing programs in existing cell classes — they do not define new classes.

So: **cross-species comparison is about reading how a conserved initial class is modified, not about finding entirely new types**. The exception proves the rule — the rare "new" types reported in the literature are usually subdivisions of conserved classes under finer resolution.

## 6. Human-specific brain development: expression, migration, or timing?

Given that classes are mostly conserved, what is the *dominant* axis of human-specific difference? The wiki converges, surprisingly consistently, on **timing first, then gene expression, then migration**:

- **Timing (heterochrony)**. [[brain-development/kanton-2019-organoid-single-cell-genomic]] shows that the single biggest human-chimp difference in cortical development is *how long* human progenitors stay in their progenitor state before differentiating. [[brain-development/gordon-2021-long-term-maturation-of]] shows that human cortical organoids continue maturing over years, not weeks. [[brain-development/sonthalia-2026-nemo-analytics-compendium]] catalogs heterochrony as a pervasive theme.
- **Gene expression**. [[brain-development/liu-2025-human-specific-enhancer-fine]] and [[brain-development/amiri-2018-transcriptome-epigenome-landscape]] identify human-specific regulatory changes that re-tune expression levels within conserved cell types. This is second-order relative to timing.
- **Migration**. Migratory-route differences exist ([[brain-development/mato-blanco-2025-early-developmental-origins]], [[brain-development/nano-2025-integrated-analysis-molecular]]) but are a smaller axis of variance than timing or program modification.

The practical message: **heterochrony is the leading human-specific signal**. An atlas that ignores time is ignoring the main axis along which human brains differ from their closest relatives.

---

# Part III — Temporal Architecture and Disease Vulnerability

## 7. Which developmental stages and cell states carry risk?

Disease-risk variants do not act uniformly across development. Several wiki papers localize risk to specific stage × cell state windows.

- [[neuroscience/paulsen-2022-autism-genes-converge]]: autism risk genes converge on a narrow set of developmental trajectories — not a random spread. Convergence is at the trajectory level, not the cell type level.
- [[neuroscience/mato-blanco-2025-early-developmental-origins]]: neuropsychiatric risk shows early developmental origins. Adult disease states are traced to early cell states that would otherwise look normal.
- [[neuroscience/dubuc-2026-linking-rare-variants-cell-type]]: rare variants associated with autism act in specific cell types during specific developmental windows — a foundation model is used as the lens that makes the window visible.
- [[neuroscience/jourdon-2023-modeling-idiopathic-autism]]: idiopathic autism organoids show divergence in fate choice, not failure of individual cell types. The thing that goes wrong is *which* fate, *when*.

The pattern: **risk is a property of the trajectory window, not of a static cell type**. A catalog-style atlas cannot see this; a trajectory-aware atlas can.

## 8. When does aberrant fate diverge from the normal atlas?

Overlaying disease data on a normal developmental atlas answers a question impossible to ask from disease data alone: *at which point on the trajectory does the disease branch diverge?*

- [[neuroscience/jourdon-2023-modeling-idiopathic-autism]] projects idiopathic-autism organoids onto a healthy reference and identifies divergence in deep-layer vs. upper-layer fate balance — divergence occurs upstream of any detectable marker failure.
- [[neuroscience/paulsen-2022-autism-genes-converge]] traces risk-gene perturbations to a specific intermediate-progenitor window; the divergence is detectable in the progenitor state before any post-mitotic phenotype.
- [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]] (HNOCA) was explicitly built for this: disease query datasets are projected onto the healthy organoid reference and compared with per-cell uncertainty, so divergence can be pinpointed rather than inferred.
- [[neuroscience/martinscosta-2024-arid1b-controls-transcriptional]] shows that ARID1B haploinsufficiency perturbs transcriptional programs in a specific developmental window, not uniformly.

**Aberrant fate diverges earlier than the phenotype is visible**. The normal atlas is what makes the early divergence measurable.

## 9. Temporal architecture: brief embryonic windows vs. prolonged diversification

Brain structures differ dramatically in *how long they take to finalize identity*. Some commit most of their neuronal identities inside a short embryonic window; others continue to diversify postnatally for years.

- **Short embryonic window — early-commit structures**. [[brain-atlas/yao-2023-high-resolution-transcriptomic-spatial]] and [[brain-atlas/braun-2023-comprehensive-cell-atlas-first]] show that many subcortical structures establish near-adult taxonomies during the embryonic period.
- **Prolonged postnatal diversification — late-commit structures**. [[brain-development/herring-2022-human-prefrontal-cortex-gene]] shows that the human prefrontal cortex continues transcriptional diversification into adolescence. [[brain-development/zhang-2025-pfc-single-cell-spatiotemporal]] gives a spatiotemporal view: PFC cell states are still being refined long after birth. [[brain-development/gordon-2021-long-term-maturation-of]] shows that human cortical neurons in organoids require more than a year in vivo to approach maturity.

Why the difference? The pattern in the wiki is that **structures with stereotyped, tightly-coupled circuits (basal ganglia, many brainstem nuclei) finalize early; structures whose function depends on experience-shaped integration (association cortex, especially PFC) stay plastic for years**. The temporal architecture reflects the computational role.

## 10. Does this temporal architecture explain complexity and vulnerability?

If late-diversifying structures are the ones whose function depends on prolonged experience-shaped refinement, then:

- **Functional complexity** should concentrate in late-diversifying structures. The wiki supports this indirectly: PFC, which is the canonical "complex" structure, is also the latest to finalize ([[brain-development/herring-2022-human-prefrontal-cortex-gene]], [[brain-development/zhang-2025-pfc-single-cell-spatiotemporal]]).
- **Disease vulnerability** should also concentrate there, because a longer vulnerability window means more opportunities for perturbation to misroute fate. This is what the autism and schizophrenia papers in the wiki find — [[neuroscience/mato-blanco-2025-early-developmental-origins]] and [[neuroscience/paulsen-2022-autism-genes-converge]] both localize risk to cortical trajectories with extended diversification.
- [[brain-development/gordon-2021-long-term-maturation-of]] makes the prediction explicit: the prolonged maturation of human cortical neurons *is* the feature that makes them both computationally rich and disease-prone.

So the temporal architecture is not a quirk — it is plausibly the *mechanism* linking human cognitive complexity to human-specific disease susceptibility. This is a hypothesis the wiki supports but does not prove.

## 11. The atlas as hypothesis engine

Putting Parts I, II, and III together, the atlas stops being the end-point of classification and becomes the starting point for a specific kind of hypothesis:

> *If cell state X at developmental time T is where risk genes converge on aberrant fate, what happens when I perturb gene Y in that exact state?*

The wiki already contains the components to ask this:

1. **The reference**: a healthy developmental atlas with trajectories, not just labels ([[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]], [[brain-atlas/braun-2023-comprehensive-cell-atlas-first]], [[brain-development/zhang-2025-pfc-single-cell-spatiotemporal]])
2. **The projection**: query disease/perturbation data onto the reference with uncertainty ([[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]], [[single-cell-dl/dedonno-2023-population-level-integration-of]])
3. **The comparison**: per-sample, per-cell divergence from the reference ([[single-cell-dl/boyeau-2025-deep-generative-modeling-of]])
4. **The perturbation prediction**: ask what a genetic perturbation would do *in silico* before running the experiment ([[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]], [[single-cell-foundation/hao-2024-large-scale-foundation-model]], [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]])
5. **The validation**: in vivo Perturb-seq in the predicted vulnerable window ([[neuroscience/jin-2020-in-vivo-perturb-seq]], [[neuroscience/dubuc-2026-linking-rare-variants-cell-type]])

This is the loop the catalog cannot close. Once the atlas is a model rather than a table, the loop runs: **reference → project → compare → predict → perturb → update reference**. That is the shift.

**What this loop leaves open — and where the next overview picks up**: the *predict → perturb* step is the hardest one to evaluate, because "predict a perturbation" means three different things (describe dynamics, generate plausible states, intervene on a causal graph) and most methods silently conflate them. For the method-by-method breakdown of what each tool actually delivers, how gene-level perturbation relates to variant interpretation, and which steps of this loop are currently unbuildable, see [[overviews/perturbation-prediction-and-causal-inference]].

---

## Summary in One Paragraph

A developmental brain atlas should be a **queryable, multimodal, trajectory-aware foundation model**, not a catalog of discrete types. Chromatin leads for fate priming, RNA leads for current state, methylation leads for durable identity; the right layer depends on the question. Developmental cell identity is better represented as a trajectory of gene-program activities than as a marker-based label. Cross-species comparison is mostly about modifications of conserved classes, with heterochrony — especially the prolonged diversification of human association cortex — as the leading axis. This prolonged temporal window is the plausible common cause of both human cognitive complexity and human-specific disease vulnerability, and it makes the atlas the natural substrate for localizing aberrant fate, predicting perturbations, and generating the next experiment.

---

## Open Problems the Wiki Does Not Yet Answer

1. **No head-to-head on perturbation prediction**: scGPT, scFoundation, and PerturBERT all claim perturbation-prediction capability, but there is no wiki-level benchmark showing which is reliable for a *developmental* question. See [[overviews/perturbation-prediction-and-causal-inference]] for why this gap is especially dangerous — most of these methods are level-2 (pattern learning) while the claim is level-3 (causal intervention).
2. **Trajectory alignment across species is unresolved**: the wiki has cross-species atlases and trajectory methods, but aligning heterochronic trajectories so that "equivalent developmental time" is comparable is not solved.
3. **Disease divergence timing is under-quantified**: Jourdon et al., Paulsen et al., and Mato-Blanco et al. all localize divergence windows, but there is no shared framework converting "divergence" into a stage coordinate on the normal atlas.
4. **Multimodal atlases are still mostly RNA-first**: truly joint RNA + ATAC + methylation developmental atlases remain rare; the leading-indicator framework above is assembled across papers rather than within one.
5. **Closing the perturbation loop**: the full reference → predict → Perturb-seq → update-reference loop has not been demonstrated end-to-end in any single paper in this wiki. [[overviews/perturbation-prediction-and-causal-inference]] maps each step of the loop to the specific methods that can (and cannot) support it, and identifies the variant-to-cell-state gap as the most consequential missing piece.

---

*Sources: [[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]], [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]], [[single-cell-foundation/hao-2024-large-scale-foundation-model]], [[single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell]], [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]], [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]], [[single-cell-dl/dedonno-2023-population-level-integration-of]], [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]], [[single-cell-dl/hao-2021-integrated-analysis-of-multimodal]], [[single-cell-dl/liu-2024-discovery-of-optimal-cell]], [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]], [[brain-atlas/braun-2023-comprehensive-cell-atlas-first]], [[brain-atlas/yao-2023-high-resolution-transcriptomic-spatial]], [[brain-atlas/corrigan-2025-conservation-and-alteration]], [[brain-atlas/gao-2025-continuous-cell-type-diversification]], [[brain-atlas/hahn-2023-evolution-of-neuronal-cell]], [[brain-development/trevino-2020-chromatin-accessibility-forebrain]], [[brain-development/herring-2022-human-prefrontal-cortex-gene]], [[brain-development/mannens-2025-chromatin-accessibility-during]], [[brain-development/zhang-2025-pfc-single-cell-spatiotemporal]], [[brain-development/fleck-2023-inferring-perturbing-cell-fate]], [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction]], [[brain-development/uzquiano-2022-proper-acquisition-cell-class]], [[brain-development/kanton-2019-organoid-single-cell-genomic]], [[brain-development/gordon-2021-long-term-maturation-of]], [[brain-development/liu-2025-human-specific-enhancer-fine]], [[brain-development/amiri-2018-transcriptome-epigenome-landscape]], [[brain-development/sonthalia-2026-nemo-analytics-compendium]], [[brain-development/nano-2025-integrated-analysis-molecular]], [[neuroscience/paulsen-2022-autism-genes-converge]], [[neuroscience/mato-blanco-2025-early-developmental-origins]], [[neuroscience/dubuc-2026-linking-rare-variants-cell-type]], [[neuroscience/jourdon-2023-modeling-idiopathic-autism]], [[neuroscience/martinscosta-2024-arid1b-controls-transcriptional]], [[neuroscience/jin-2020-in-vivo-perturb-seq]]*
