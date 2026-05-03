---
title: "Transcriptional Heterogeneity in Neural Progenitors as a Developmental Mechanism"
type: overview
created: 2026-05-03
category: overviews
tags: [developmental-noise, NPC, radial-glia, oRG, lineage-potential, fate-commitment, critical-window, NDD, heterogeneity, stochastic-fate, cell-cell-communication, decoder-noise]
papers:
  - neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in
  - neuroscience/parenti-2020-neurodevelopmental-disorders-from-genetics-to
  - brain-development/taverna-2014-cell-biology-of-neurogenesis
  - brain-development/kanton-2019-organoid-single-cell-genomic
  - brain-development/jain-2025-morphodynamics-human-early
  - brain-development/mansour-2018-in-vivo-model-of
  - brain-development/liu-2025-human-specific-enhancer-fine
  - brain-development/dibella-2021-molecular-logic-of-cellular
  - brain-development/uzquiano-2022-proper-acquisition-cell-class
  - brain-development/nano-2025-integrated-analysis-molecular
  - brain-development/zeng-2023-single-cell-spatial-transcriptional
  - brain-development/zhang-2025-pfc-single-cell-spatiotemporal
  - brain-development/zhang-2025-spatial-dynamics-brain-development
  - brain-development/wang-2025-molecular-cellular-dynamics
  - brain-development/gordon-2021-long-term-maturation-of
  - brain-development/glass-2026-human-cortical-organoids-recapitulate
  - brain-development/herring-2022-human-prefrontal-cortex-gene
  - brain-development/mannens-2025-chromatin-accessibility-during
  - brain-development/trevino-2020-chromatin-accessibility-forebrain
  - brain-development/bhaduri-2020-cell-stress-cortical-organoids
  - brain-development/keefe-2025-lineage-resolved-atlas-developing
  - brain-development/fleck-2023-inferring-perturbing-cell-fate
  - brain-development/zenk-2024-single-cell-epigenomic-reconstruction
  - brain-development/ding-2026-dissecting-gene-regulatory-networks
  - brain-atlas/braun-2023-comprehensive-cell-atlas-first
  - neuroscience/schafer-2019-pathological-priming-causes
  - neuroscience/jourdon-2023-modeling-idiopathic-autism
  - neuroscience/paulsen-2022-autism-genes-converge
  - neuroscience/mato-blanco-2025-early-developmental-origins
  - neuroscience/li-2023-single-cell-brain-organoid
  - neuroscience/de-jong-2021-cortical-overgrowth-preclinical
  - neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence
  - neuroscience/dony-2025-glucocorticoid-amplifies-inhibitory
  - neuroscience/tanabe-2025-role-of-immature-choroid
  - single-cell-dl/setty-2019-characterization-of-cell-fate
  - single-cell-dl/lange-2022-cellrank-for-directed-single
  - single-cell-dl/klein-2025-mapping-cells-through-time
  - single-cell-dl/vinyard-2025-learning-cell-dynamics-with
  - single-cell-dl/aivazidis-2025-cell2fate-infers-rna
---

## Why This Overview Exists

The companion overview [[overviews/cell-identity-programs-and-trajectories]] argues that cell identity is best represented as **continuous gene-program performance along a trajectory**, and traces the methodological lineage (PCA → NMF → joint decomposition → foundation models) for *extracting* clean program structure from data. That overview treats heterogeneity as a *resolution problem* — something we want to clean up so the program signal pops out.

This overview takes the **opposite stance**: heterogeneity in neural progenitor cells (NPCs) during critical windows is **not noise to be cleaned up, but a developmental mechanism that drives lineage potential, fate specification, and ultimately the substrate of NDD vulnerability**. The thesis was articulated cleanly in [[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir, Meshorer, Shifman 2026]] (Box 1) as one of four explanation layers for variable expressivity:

> NPC dynamic, heterogeneous gene expression during critical windows of fate commitment is strongly linked to lineage potential and fate specification.

**Why this matters**: in a world where NDD pathogenic variants act on a deterministic developmental substrate, the same variant should give the same phenotype. The fact that monozygotic twins (identical genotype + identical environment) carrying the same NDD variant still show discordant phenotypes points to a **biological floor of stochastic variation** — not measurement noise, but intrinsic heterogeneity in how progenitor cells commit to fates. Quantifying that floor is one of the open problems Dvir 2026 names; it is also the methodological gap that will decide how predictable single-cell-perturbation models can ever be.

This overview compiles the wiki's evidence into a single argument, in seven parts:

- **Part I** — Heterogeneity as mechanism, not noise (the thesis)
- **Part II** — The human-amplified case: oRG / basal radial glia and the expansion of lineage potential
- **Part III** — RG subtypes drive spatial patterning and functional specification
- **Part IV** — Cross-cell-type variability: glia–neuron communication
- **Part V** — Critical windows: when the heterogeneity gets locked in
- **Part VI** — NDD vulnerability *through* heterogeneity
- **Part VII** — How heterogeneity is measured

Closing section connects to the cascade frame in [[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir 2026]]: developmental heterogeneity is the *stochastic component of the bottleneck-to-cell decoder*, not a property of the bottleneck (3 pathways) itself.

---

# Part I — Heterogeneity as Mechanism, Not Noise

## 1. The thesis in one sentence

NPCs do not occupy stable, discrete identity states during fate commitment. They occupy **dynamic, transient, heterogeneous transcriptional states**, and *which state a cell is in at the moment of commitment* is a non-trivial determinant of what cell type it becomes, what regional identity it acquires, and what circuit it ends up wired into. Same starting material + same external signals + same time → still different cells, by design.

This is the inverse of the standard "noise = measurement error" framing: here, **the variability is the signal** that the developmental program reads.

## 2. Why noise is biologically necessary, not accidental

Two arguments, both operationally testable:

- **Lineage diversification requires probabilistic divergence.** A perfectly synchronised, perfectly homogeneous progenitor population would produce a single fate. Cortex needs ~30 cell classes from a small set of progenitor types in a few weeks; heterogeneity at the progenitor level is one mechanism that lets a small number of starting states generate a much larger output set.
- **Lineage *potential* expansion (especially in primates) depends on tolerated heterogeneity.** In rodents the apical RG → IP → neuron axis is relatively constrained. In humans the same axis is augmented by **outer radial glia (oRG / basal radial glia)** that proliferate in the OSVZ; their progenitor pool tolerates much wider state-to-state fluctuations and produces a more diverse output (Part II below).

[[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir 2026]] frames this as the **fourth layer** of NDD phenotype variability, alongside the variant itself, modifying-genome, and environment — and explicitly names it as the layer **least empirically tractable** because controlled isogenic systems are required to distinguish stochastic from deterministic variance.

## 3. Why this overview is distinct from "cell identity as program performance"

[[overviews/cell-identity-programs-and-trajectories]] is about *how to read* cell identity through the lens of program activity. Most of its papers use heterogeneity as a *signal to denoise* — joint NMF, foundation-model embeddings, GRN-derived programs all aim to extract the **stable, reproducible** axes of variation.

This overview is about the *un-denoiseable residual* — the part of variability that is **intrinsically dynamic, cell-autonomous, and time-windowed**, that no amount of better extraction will collapse, because there is no fixed point to collapse to. Methodologically the two overviews use overlapping tools (CellRank, GRN inference, lineage tracing) but ask different questions of the same data.

---

# Part II — The Human-Amplified Case: oRG / bRG and Lineage Potential

## 4. Why oRG matters for this thesis

Outer radial glia (oRG, equivalently **basal radial glia / bRG**) are progenitors located in the outer subventricular zone (OSVZ) that are **massively expanded in primates and humans relative to rodents**. They are the main reason human cortex has so many more upper-layer neurons and so much more lateral neurogenic territory than mouse cortex.

For the heterogeneity thesis, oRG matter for three reasons:
- They divide many more times before commitment than apical RG → the *transient transcriptional state space* explored per progenitor is larger.
- They lack the cell-cell contacts that anchor apical RG to a strict ventricular niche → their gene expression is freer to fluctuate.
- They are the substrate that human-specific cis-regulatory programs (e.g., the human-specific enhancers in [[brain-development/liu-2025-human-specific-enhancer-fine|Liu 2025]]) act on; those enhancers tune NPC dynamics rather than imposing fixed identity.

## 5. What the wiki shows about oRG / NPC heterogeneity

[[brain-development/taverna-2014-cell-biology-of-neurogenesis|Taverna et al. 2014]] is the foundational cell-biology review: it lays out the ventricular vs subventricular zone organisation, oRG identification, and the cell-cycle differences (oRG retain a basal process; apical RG don't) that *enable* the expanded heterogeneity. The review explicitly notes that human progenitor populations are *markedly more heterogeneous* than mouse, and frames this as the cell-biological origin of human cortical expansion.

[[brain-development/kanton-2019-organoid-single-cell-genomic|Kanton et al. 2019]] (Camp / Treutlein labs) is the cross-species comparison that grounds the framing: human, chimp, and macaque organoids analysed at single-cell resolution show **human-specific neuronal neoteny** — human progenitors stay in a proliferative, transcriptionally fluctuating state significantly longer than chimp or macaque equivalents. The "neoteny" framing implies that *time spent in the heterogeneous state* is a species-typical parameter of brain development.

[[brain-development/jain-2025-morphodynamics-human-early|Jain et al. 2025]] adds the morphological / dynamic dimension: NPCs in early human development show characteristic morphodynamics that are not captured by static transcriptomic snapshots — cells move, change shape, and shift transcriptional state on rapid timescales. The implication: the "heterogeneity" we see in single-cell data is partly a *time-averaged* view of cells that are individually moving fast.

[[brain-development/mansour-2018-in-vivo-model-of|Mansour et al. 2018]] (Gage lab) demonstrated that human cortical organoids transplanted into rodent host brains continue to develop with vascularisation and synaptic integration — providing an in-vivo testbed where the human-specific NPC heterogeneity proceeds on its native timescale despite the murine host. This is the methodological complement to organoid-only studies.

[[brain-development/liu-2025-human-specific-enhancer-fine|Liu et al. 2025]] identifies **human-specific enhancers** that fine-tune NPC dynamics — many of them act on RG / NPC populations specifically, suggesting that the regulatory genome has a dedicated layer for *modulating heterogeneity* rather than imposing fixed identity. (See also [[genomic-dl/zemke-2023-conserved-and-divergent-gene]] for the broader observation that ~80% of human-specific cis-regulatory elements are TE-derived but their syntax is preserved — i.e., human-specific *modulation*, not *invention*.)

## 6. The cell-biology corollary

oRG abundance is the cell-biological version of a **larger latent space** for fate commitment. If apical RG live on a 2-D fate manifold and oRG live on a 4-D one, then the stochastic exploration of states that any individual progenitor performs samples a richer territory in primates than in rodents. This is why the *same* progenitor pool can produce a much wider neuronal repertoire — and also why human neurodevelopment is intrinsically harder to *predict* from genotype, because the latent space being sampled is larger.

---

# Part III — RG Subtypes Drive Spatial Patterning and Functional Specification

## 7. Spatial heterogeneity beyond cell-type identity

[[brain-development/nano-2025-integrated-analysis-molecular|Nano et al. 2025]] and [[brain-development/dibella-2021-molecular-logic-of-cellular|Di Bella et al. 2021]] both make the same fundamental move: the molecular logic of cortical neurogenesis cannot be captured at the level of *cell types alone*. The same nominal "RG" cell type, sampled at different cortical positions or different developmental times, runs different gene programs that bias which neuronal subtype the descendants will become.

Nano 2025 specifically extracts ~500 reproducible co-expression meta-modules from 23 human cortical datasets and identifies **FEZF2+TSHZ3 as drivers of deep-layer specification**, validated in chimeroids. The implication: the same RG, depending on its module-activity profile at the moment of neurogenic division, gives rise to a different layer-specific neuron. Module activity is the heterogeneity that matters.

Di Bella 2021 showed that the *temporal sequence* of progenitor states determines the laminar identity of their progeny — each "wave" of neurogenesis comes from progenitors in distinguishable transcriptomic states, even when the canonical RG markers are constant.

## 8. Spatial transcriptomics brings the geometric dimension

Three recent spatially-resolved studies in the wiki compound this picture:

[[brain-development/zeng-2023-single-cell-spatial-transcriptional|Zeng et al. 2023]] resolves single-cell transcriptional state in spatial context across mouse cortex development; the same broad cell type at different cortical coordinates carries different programmatic activity, and that geometric variability is *informative* for fate.

[[brain-development/zhang-2025-pfc-single-cell-spatiotemporal|Zhang et al. 2025 (PFC)]] and [[brain-development/zhang-2025-spatial-dynamics-brain-development|Zhang et al. 2025 (spatial dynamics)]] extend this to human prefrontal cortex and broader brain development respectively. The emerging pattern is that **spatial position is a covariate that explains a substantial fraction of single-cell transcriptional variance** that would otherwise look like noise.

## 9. Areal identity as another source of fate heterogeneity

[[neuroscience/mato-blanco-2025-early-developmental-origins|Mato-Blanco et al. 2025]] traces how risk gene dynamics during early human corticogenesis differ between **brain-organizer hubs** at different anteroposterior / dorsoventral coordinates. Their TF-depletion simulation reveals that the *same TF perturbation* has substantially different downstream consequences depending on which areal hub it occurs in — areal identity is itself a layer of decoder context that modulates how heterogeneity at the progenitor level is read.

## 10. Why this matters for fate specification

Together, parts 7-9 land a single point: **a "neural progenitor" in 2026 cannot be treated as a single state**. It is a *position-, time-, and module-activity-defined coordinate*, and progenitors at different coordinates have measurably different fate distributions even when their overall cell-type label is identical. Fate specification is the *integration* of (cell-type identity × position × time × current module activity) — and the heterogeneity at each axis compounds.

---

# Part IV — Cross-Cell-Type Variability: Glia–Neuron and Other Cell-Cell Communication

## 11. The glial layer of heterogeneity

Neurons are the dominant focus of NPC and fate-commitment work, but glia — astrocytes, oligodendrocyte precursor cells (OPCs), microglia — are produced from overlapping progenitor pools and exhibit their own developmental heterogeneity. More importantly: **neurons and glia communicate with each other during development**, and this cross-cell-type communication is itself heterogeneous from cell to cell.

[[brain-development/wang-2025-molecular-cellular-dynamics|Wang et al. 2025]] is the most direct treatment in the wiki of **OPC × GABAergic neuron communication** during development. The work documents cell-cell interactions between OPCs and immature GABAergic interneurons that vary substantially from cell to cell — i.e., not all OPCs receive the same signals, not all GABAergic neurons send the same signals, and the variability is patterned but stochastic. Functional consequences: variation in myelination timing, GABAergic maturation, and ultimately E/I balance setpoint.

## 12. Glial maturation is a second-order timescale

[[brain-development/gordon-2021-long-term-maturation-of|Gordon et al. 2021]] demonstrated that long-term cortical-spheroid culture proceeds through identifiable maturation milestones for both neurons *and* glia — and that glial maturation lags neurons substantially. This means the glial "decoder context" is dynamically changing under the neurons that are simultaneously specifying their fate. NPCs that commit to neuronal fate at month 2 see a different glial environment than NPCs that commit at month 5.

## 13. Glia as integrators of environmental signals

Three NDD-relevant studies (in the neuroscience category but worth pulling here for completeness):

[[neuroscience/dony-2025-glucocorticoid-amplifies-inhibitory|Dony et al. 2025]] shows that chronic glucocorticoid exposure (a "stress" signal) is integrated by developing cortical organoids in a way that **amplifies inhibitory neuron fate via PBX3** — the environmental signal gets routed through transcriptional programs that are themselves heterogeneous across cells, and the amplification depends on which cells happen to be in receptive states.

[[neuroscience/tanabe-2025-role-of-immature-choroid|Tanabe et al. 2025]] frames the immature choroid plexus as a developmental signalling hub whose own state-heterogeneity shapes downstream cortical maturation and social-behaviour critical period.

[[neuroscience/morelli-2022-mecp2-related-pathways-cortical|Morelli et al. 2022]] (DM1 organoid model) shows how glutamatergic-neuron-specific dysregulation propagates to MECP2 pathway disturbance — implying that even within the *same nominal cell type*, the level of pathway perturbation depends on each cell's particular state at the moment of insult.

## 14. The pattern

Glia-related heterogeneity is **at least a third dimension of developmental noise**, alongside spatial position and temporal stage:
- Different OPCs receive different neuronal signals (Wang 2025)
- Different glial cohorts present different maturation contexts (Gordon 2021)
- Different cells integrate environmental signals (glucocorticoid, signalling-hub niche) at different rates and amplitudes (Dony 2025; Tanabe 2025)

For NDD work this matters because most computational models work at the *neuronal* level — but neuronal phenotype is partly determined by the glial context the neuron developed in, and that context was itself stochastic.

---

# Part V — Critical Windows: When the Heterogeneity Gets Locked In

## 15. The "critical window" framing

Heterogeneity that exists *forever* is just noise. Heterogeneity that exists *and gets read out at a specific developmental moment* is mechanism. The Dvir 2026 framing centres this distinction: progenitor states are dynamic and stochastic, but **fate commitment events are temporally narrow** — once a cell crosses the commitment boundary, the state it was in at the boundary is locked.

[[neuroscience/schafer-2019-pathological-priming-causes|Schafer et al. 2019]] is the wiki's clearest treatment of how this can go wrong: in idiopathic-ASD iPSC-derived NSCs, **late developmental gene networks are activated prematurely** ("pathological priming"), so the commitment-boundary read-out happens against a precociously-mature transcriptomic background. Different individual NSCs prime by different amounts → heterochronicity across patients.

[[brain-development/glass-2026-human-cortical-organoids-recapitulate|Glass et al. 2026]] addresses the question of whether organoids preserve the same critical-window timing as in-vivo cortex — important because all the iPSC-based heterogeneity work in the wiki is implicitly trusting that organoid clocks are calibrated. The answer is partial: some windows are recapitulated, some are not, with major implications for what you can infer from organoid models.

[[brain-development/herring-2022-human-prefrontal-cortex-gene|Herring et al. 2022]] resolves human prefrontal cortex gene-expression dynamics across development with sufficient temporal resolution to identify which genes' expression *peaks during which window*. The peak-window distribution is itself informative about which fate decisions are time-windowed.

## 16. Chromatin sets the windows, transcription crosses them

[[brain-development/mannens-2025-chromatin-accessibility-during|Mannens et al. 2025]] and [[brain-development/trevino-2020-chromatin-accessibility-forebrain|Trevino et al. 2020]] both make the same observation: **chromatin accessibility precedes the transcriptional changes that mark fate commitment**. The regulatory commitment is locked in at the chromatin level, before the marker mRNA appears. This means fate-commitment heterogeneity is partly an *epigenetic* heterogeneity — which enhancers a particular cell happens to have open at the critical window determines what its transcriptional response can be when the developmental signal arrives.

## 17. Why this is a strong argument for *intervention timing*

If the critical windows are real and the heterogeneity gets locked in at the boundaries, then:
- Pre-window interventions can shift the entire heterogeneity distribution
- In-window interventions can selectively redirect the cells that have not yet committed
- Post-window interventions act on already-committed cells and operate on a much narrower mechanism set (synaptic plasticity, modulator tuning)

This is consistent with the [[neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence|Fernandez-Garcia 2026]] finding that convergent NDD drug effects can rescue zebrafish phenotypes **post-mitotically**, but it also explains why such rescues likely need to be *life-long* interventions on sustained pathway state, rather than one-time corrections of identity.

---

# Part VI — NDD Vulnerability *Through* Heterogeneity

This is the integration with the convergence frame from [[neuroscience/parenti-2020-neurodevelopmental-disorders-from-genetics-to|Parenti et al. 2020]] and the divergence frame from [[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir et al. 2026]].

## 18. Pathogenic variants act on heterogeneous substrate, not uniform substrate

A key insight: NDD risk-gene KOs do not perturb a deterministic clockwork. They perturb a *stochastic system that was already heterogeneous before the perturbation*. This explains several otherwise-puzzling observations:

- **Same variant, different cells, different responses** — [[neuroscience/li-2023-single-cell-brain-organoid|Li et al. 2023]] (CHOOSE) used pooled CRISPR of 36 ASD risk genes in mosaic cerebral organoids and found that **dorsal intermediate progenitors and ventral progenitors are differentially vulnerable**. Same gene KO → different outcome by cell-type starting state.
- **Same variant, different individuals, different penetrance** — [[neuroscience/jourdon-2023-modeling-idiopathic-autism|Jourdon et al. 2023]] (idiopathic ASD father-son pairs, n=13) showed that *macrocephalic and normocephalic sons of ASD fathers had opposite E/I imbalances*, with TF divergence between subgroups. Same broad genetic predisposition, opposite phenotypic axis — driven by which TFs ended up high vs low in the affected NSCs at commitment time.
- **Genomic context modulates expressivity** — [[neuroscience/paulsen-2022-autism-genes-converge|Paulsen et al. 2022]] found that the same KO of KMT5B / ARID1B / CHD8 in different organoid lines produced different magnitudes of asynchronous GABAergic / excitatory development — i.e., the genetic background acts as a modifier of the heterogeneity floor.

## 19. "Pathological priming" as heterogeneity-amplification

[[neuroscience/schafer-2019-pathological-priming-causes|Schafer 2019]]'s heterochronicity finding fits directly into the heterogeneity framing: variants that disrupt the *timing* of program activation push some cells across critical-window boundaries early. The heterogeneity that was previously bounded becomes amplified — cells that should have been late-priming arrive at fate commitment in a state usually reserved for later cells. The phenotype is heterogeneous *because* the underlying timing distribution is now wider.

## 20. Convergence at the pathway level *requires* heterogeneity at the cell level

This is the central reconciliation point with [[overviews/convergent-regulation-across-systems]] and [[neuroscience/parenti-2020-neurodevelopmental-disorders-from-genetics-to|Parenti 2020]]: **pathway convergence (the 3-pathway thesis: mTOR + chromatin + synaptic) and cell-level heterogeneity are not in tension — they are the two halves of the same observation.**

- Pathway state is a low-dimensional manifold (the bottleneck).
- *Which* cells respond to a given pathway perturbation depends on which states they are in at the moment of perturbation.
- A KO of a chromatin regulator hits *all cells transcribing that regulator's target genes during that window*; the cell-by-cell response amplitude is heterogeneous because the cells were at heterogeneous states.
- Convergence is a property of the average. Heterogeneity is a property of the distribution around the average.

[[neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence|Fernandez-Garcia 2026]] is the empirical demonstration of this claim: pooled CRISPR-KO of 23 NDD risk genes finds that **convergence is strongest in mature glutamatergic neurons** — not because the genes only act there, but because the heterogeneity-amplification effects are the most legible there. Convergence emerges from heterogeneity, not despite it.

## 21. Why developmental-noise-aware models will outperform deterministic ones

A practical implication, particularly relevant for [[overviews/six-open-issues-perturbation-modelling]] and [[overviews/perturbation-prediction-and-causal-inference]]:

- Deterministic models (input genotype → output phenotype) implicitly assume the substrate is uniform.
- Heterogeneity-aware models (input genotype × stochastic state → distribution over phenotypes) explicitly model the floor.
- The right loss function is *distributional* (e.g., Wasserstein distance to ground-truth phenotype distribution) rather than point-wise (e.g., mean phenotype RMSE) — see [[concepts/distributional-vs-point-prediction]].

For Phase 1 NDD-convergence work, this argues for retaining cell-by-cell heterogeneity rather than averaging it away in early analysis steps.

---

# Part VII — How Heterogeneity Is Measured

## 22. Lineage tracing and resolved fate atlases

[[brain-development/keefe-2025-lineage-resolved-atlas-developing|Keefe et al. 2025]] built a lineage-resolved atlas of developing brain at single-cell resolution, allowing direct readout of *which states a clone passed through to reach a given final identity*. This is the methodological gold standard for the heterogeneity thesis: the same starting clone gives heterogeneous progeny, and the trajectory variance is now measurable.

[[brain-atlas/braun-2023-comprehensive-cell-atlas-first|Braun et al. 2023]] (first-trimester human atlas) provides the temporal scaffold against which heterogeneity is benchmarked — without a high-resolution reference of *expected* state distributions, deviation cannot be quantified.

## 23. Fate inference and dynamic state estimation

The wiki's single-cell-dl methods most relevant for this thesis:

- [[single-cell-dl/setty-2019-characterization-of-cell-fate|Palantir (Setty 2019)]] uses pseudotime and probabilistic fate assignment — every cell gets a *distribution* over terminal fates, not a deterministic assignment. The width of that distribution is itself a measure of heterogeneity.
- [[single-cell-dl/lange-2022-cellrank-for-directed-single|CellRank (Lange 2022)]] extends this to RNA-velocity-informed fate maps, allowing detection of state-to-state transitions in the data.
- [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna|Cell2fate (Aivazidis 2025)]] uses Bayesian ODE linearisation to infer RNA-velocity modules with reduced noise; particularly suited to brain-development data.
- [[single-cell-dl/klein-2025-mapping-cells-through-time|Klein 2025]] introduces methods for mapping cells through time with explicit uncertainty quantification.
- [[single-cell-dl/vinyard-2025-learning-cell-dynamics-with|Vinyard 2025]] adds optimal-transport-based dynamic models of single-cell trajectories.

## 24. GRN-derived programs as the regulatory readout

[[brain-development/fleck-2023-inferring-perturbing-cell-fate|Fleck 2023]], [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction|Zenk 2024]], and [[brain-development/ding-2026-dissecting-gene-regulatory-networks|Ding 2026]] all infer **gene regulatory networks** from joint chromatin-and-expression data. The variance of GRN activity across cells of the same nominal type is one of the most informative measures of heterogeneity, because it captures regulatory commitment that is upstream of the marker-gene-level signal that more standard single-cell analyses use. These methods are also the natural bridge to perturbation-prediction work — see [[overviews/perturbation-prediction-and-causal-inference]].

## 25. The not-yet-solved measurement problem

Despite the methods above, the wiki has *no* paper that explicitly partitions single-cell variance into:
- Deterministic (cell-type / position / time)
- Reducible noise (technical / measurement)
- Irreducible biological stochastic (the floor Dvir 2026 names)

This is a clear methodological gap. Decomposition methods exist for bulk variance (heritability, hLDSC) but not for single-cell variance with developmental-noise interpretability. Bridging this gap is one of the most consequential next steps; see also [[overviews/six-open-issues-perturbation-modelling]] for the perturbation-side framing of the same gap.

---

# Closing — Heterogeneity in the Cascade Frame

In the cascade frame articulated for [[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir 2026]]:

```
INPUT (variants × modifiers)
   ↓ funnel
BOTTLENECK (3-pathway state, low-dimensional manifold)
   ↓ DECODER
   ↓   ↪ deterministic part (cell-type × position × time)
   ↓   ↪ stochastic part (← THIS OVERVIEW IS ABOUT)
OUTPUT (cell phenotype → circuit → behavior)
```

This overview's content sits in the **stochastic part of the decoder**, not in the bottleneck. That placement matters:

- Convergence ([[overviews/convergent-regulation-across-systems]] / [[neuroscience/parenti-2020-neurodevelopmental-disorders-from-genetics-to|Parenti 2020]]) is a property of the bottleneck — different variants funnel onto the same low-dimensional manifold.
- Divergence / heterogeneity ([[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir 2026]] + this overview) is a property of the decoder — even at the same bottleneck position, different cells take different fate decisions.
- Both are *simultaneously true* because they refer to different cascade locations.

The empirical research direction this overview points at:

1. **Separate the deterministic decoder from the stochastic decoder.** Variance decomposition methods that respect single-cell structure are the missing tool. The bulk-genetics analogue (heritability) is well-established; the single-cell analogue is not.
2. **Identify the cell types and developmental windows where the stochastic component is largest.** These are the cells where NDD vulnerability is most concentrated — and also where intervention timing matters most.
3. **Build pathway-perturbation models that explicitly carry heterogeneity through prediction.** Distributional prediction (rather than point prediction) is the natural fit ([[concepts/distributional-vs-point-prediction]]); generative methods that learn $P(\text{phenotype} \mid \text{variant}, \text{cell-state})$ are the methodological direction.

The thesis: **transcriptional heterogeneity in NPCs is not a measurement problem to be cleaned up, but the substrate that makes brain development possible, the source of human-amplified lineage potential, and the floor of NDD phenotype unpredictability**. Quantifying it is one of the next decisive moves in single-cell + perturbation neuroscience.
