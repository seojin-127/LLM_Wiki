---
title: "Reconciling Convergence and Heterogeneity in NDDs: A Cascade Framework"
type: overview
created: 2026-05-03
category: overviews
tags: [NDD, convergence, heterogeneity, cascade, autoencoder, latent-manifold, decoder, developmental-noise, gene-environment, cell-type-specificity, distributional-prediction, framework, synthesis]
papers:
  - neuroscience/parenti-2020-neurodevelopmental-disorders-from-genetics-to
  - neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in
  - neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence
  - neuroscience/paulsen-2022-autism-genes-converge
  - neuroscience/jourdon-2023-modeling-idiopathic-autism
  - neuroscience/li-2023-single-cell-brain-organoid
  - neuroscience/dubuc-2026-linking-rare-variants-cell-type
  - neuroscience/jin-2020-in-vivo-perturb-seq
  - neuroscience/dony-2025-glucocorticoid-amplifies-inhibitory
  - neuroscience/mato-blanco-2025-early-developmental-origins
  - neuroscience/schafer-2019-pathological-priming-causes
  - single-cell-dl/maddu-2026-learning-biophysical-models-of
  - single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of
  - single-cell-dl/li-2026-save-a-generalizable-framework
  - single-cell-dl/lopez-2018-deep-generative-modeling-for
  - single-cell-foundation/szalata-2026-perturbert-learning-gene-co
  - drug-resistance/xu-2026-mapping-convergent-regulators-of
  - concepts/distributional-vs-point-prediction
  - concepts/interpolation-vs-extrapolation
  - concepts/factorial-perturbation-design
  - concepts/expressivity-interpretability-tradeoff
  - concepts/uncertainty-quantification
---

## Why This Overview Exists

Two recent reviews of neurodevelopmental disorders (NDDs) point in apparently opposite directions:

- [[neuroscience/parenti-2020-neurodevelopmental-disorders-from-genetics-to|Parenti et al. 2020]] crystallises the **convergence** picture: hundreds of NDD risk genes act through three core pathway families (PI3K-mTOR, transcriptional/epigenetic regulation, synaptic signaling) connected as a multipathway loop. Different variants → same set of pathways → similar disease class.
- [[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir et al. 2026]] crystallises the **heterogeneity / divergence** picture: even the *same pathogenic variant* in the *same gene* yields different phenotypes across individuals — explained by four layers (variant itself / other genetic elements / environment / developmental noise) interacting at every step from genome to phenotype.

The wiki carries an overview for each side:
- Convergence side → [[overviews/convergent-regulation-across-systems]]
- Heterogeneity side → [[overviews/transcriptional-heterogeneity-as-developmental-mechanism]]

A reader who holds both overviews in mind ends up with a real puzzle: **how can NDDs show *strong functional convergence* and *pervasive heterogeneity at every observable layer* at the same time?** This overview is the bridge that argues the apparent paradox dissolves once we stop modelling NDDs as a single genotype → phenotype mapping and start modelling them as a **multi-stage information cascade**, where convergence is a property of one stage (a low-dimensional bottleneck) and heterogeneity enters at every other stage. Both claims are simultaneously true; they just refer to different cascade locations.

The framework articulated here generalises beyond NDDs to any disease where a small number of pathway nodes funnel a vast input variant space into a vast output phenotype space — many cancer driver studies, the broader [[overviews/convergent-regulation-across-systems]] framing, and the [[overviews/endogenous-variation-as-natural-perturbation]] sister overview all sit in the same conceptual region.

This overview is structured as eight parts:
- **Part I** — The apparent paradox stated explicitly
- **Part II** — Reframing: biology is a cascade, not a single mapping
- **Part III** — The autoencoder analogy: low-dimensional manifold + cell-type-specific decoder
- **Part IV** — Where each layer of heterogeneity enters the cascade
- **Part V** — The information-theoretic view: data processing inequality, decoder context as side-information
- **Part VI** — Resolving the paradox: convergence and heterogeneity at different cascade locations
- **Part VII** — Mapping the user's NDD-convergence research questions onto the cascade
- **Part VIII** — Methodological agenda: variance decomposition, distributional prediction, decoder identification
- **Closing** — How this overview sits between the convergence and heterogeneity overviews

---

# Part I — The Apparent Paradox

## 1. Two reviews, two thesis statements

Take the two NDD reviews on the wiki and reduce each to one sentence:

- **Parenti 2020**: NDD-causing variants across hundreds of genes converge onto a small set of core pathways (mTOR, chromatin, synaptic) connected through a multipathway loop, and the convergence is the basis for whatever therapeutic possibilities exist.
- **Dvir 2026**: NDD phenotypes are heterogeneous at every observable layer (variant type, protein domain, isoform, cRE interactions, oligogenic interactions, cell-type response, developmental timing, penetrance, expressivity), and the heterogeneity is what makes individual prediction so hard.

Read in isolation each thesis is internally coherent. Read together they look like a contradiction: if hundreds of variants funnel onto three pathways, why are phenotypes so heterogeneous? If phenotypes are so heterogeneous, what does "convergence" really mean?

## 2. Why this puzzle has substance, not just framing

The puzzle is not resolved by saying "convergence is partial". The empirical picture is that convergence is *strong* at the pathway level — multiple independent CRISPR-KO studies converge on the same pathway nodes ([[neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence|Fernandez-Garcia 2026]] for NDDs; [[drug-resistance/xu-2026-mapping-convergent-regulators-of|Xu 2026 PerturbFate]] for cancer drug resistance) — and heterogeneity is *strong* at the phenotype level — gnomAD-scale audits show that the same predicted-LoF variant produces different phenotypes in different carriers, with multiple reasons including position, isoform, modifying genetics, and stochastic developmental factors ([[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir 2026]]'s Box 1 catalogue).

Both observations are *quantitatively well-supported*. So the puzzle is real: the same biology is showing convergence in one set of measurements and heterogeneity in another.

## 3. The mistake the puzzle is built on

The puzzle dissolves once we recognise the implicit assumption that creates it: **modelling NDDs as a single genotype → phenotype mapping**. Under that assumption, "the system" is one function, and either it converges (many inputs → one output) or it doesn't. Convergence and heterogeneity become rivals.

The actual biology is not a single function. It is a cascade of functions:

```
genome → pathway state → cell-type response → circuit assembly → behavior
```

Each arrow is its own function with its own input-output ratio. The system *as a whole* can perfectly well show convergence at one arrow and heterogeneity at another. The "paradox" is an artefact of the single-function framing.

---

# Part II — Reframing: Biology as a Cascade, Not a Single Mapping

## 4. The cascade in full

Spelling out the same arrow chain with the actual biological content makes the framing concrete:

```
[INPUT — extremely high-dimensional]
   gene variants (3B bp space, ~10^6 known coding variants)
   × variant type (LoF / missense / GoF / synonymous / regulatory)
   × position (domain / isoform / cRE)
   × other variants in the genome (oligogenic / polygenic / paralog)
   × parental haplotypes (genetic background, PRS)
   ↓
   ↓  [funnel — variant maps onto pathway influence]
   ↓
[BOTTLENECK — low-dimensional, but graded]
   mTOR axis activity (continuous, not on/off)
   × Chromatin axis activity (a high-dim summary of dysregulated modules)
   × Synaptic axis activity (where in the synapse, how)
   × interactions among the three axes (multipathway loop)
   ↓
   ↓  [decode — pathway state read by each cell type]
   ↓
[CELL-TYPE LAYER]
   pathway state × cell-type-specific reading function
   = transcriptomic / proteomic / functional response per cell
   ↓
   ↓  [decode — cell response unfolded over time]
   ↓
[DEVELOPMENTAL TIMING LAYER]
   cell-type response × developmental window
   = trajectory deviation
   ↓
   ↓  [circuit assembly + plasticity + compensation]
   ↓
[CIRCUIT / BEHAVIORAL LAYER — high-dim again]
   penetrance, expressivity, comorbidity profile, diagnostic label
```

In this picture:
- *Convergence* is what happens at the funnel from INPUT to BOTTLENECK — the dimensionality drops sharply.
- *Heterogeneity* enters at three places: at INPUT (variant features), inside the BOTTLENECK (where on the manifold), and at the DECODE arrows (cell-type, timing, circuit).

The two phenomena are at *different cascade locations*. They cannot be in tension.

## 5. Why this framing is not just rhetorical

Three concrete consequences distinguish the cascade view from the single-function view:

- It predicts that convergence depth depends on *measurement scale*. If you measure at the pathway level, you see convergence; if you measure at single-cell transcriptomics, convergence loosens because you have moved post-bottleneck.
- It predicts that heterogeneity is *not random* but *structured by cascade location*. Pre-bottleneck heterogeneity (variant type, domain) is genetically observable. Post-bottleneck heterogeneity (cell type × time) is observable in single-cell + spatial data. Stochastic decoder heterogeneity (developmental noise) needs isogenic comparisons.
- It predicts that *intervention design depends on cascade target*. Pre-bottleneck interventions (gene therapy, ASOs) act on the input. Bottleneck interventions (drugs targeting mTOR, HDAC inhibitors) act on the manifold. Post-bottleneck interventions (cognitive therapies, neuromodulators) act on the decoder.

Each consequence is empirically tractable. The framework earns its keep by predicting where to look for each phenomenon.

---

# Part III — The Autoencoder Analogy

## 6. Why the cascade looks like an autoencoder

A reader fluent in [[overviews/cell-identity-programs-and-trajectories]] or [[concepts/variational-autoencoder]] will already see the shape: the cascade has the architecture of a **(variational) autoencoder**.

```
INPUT          ENCODER        LATENT          DECODER          OUTPUT
(high-dim)     (= variant     (= pathway      (= cell-type    (= phenotype
               function)        manifold)       reading +       distribution)
                                                stochasticity)
```

In ML terms:
- The **encoder** is the function that maps a variant (genome state) to its effect on the three pathway axes. This is the "convergence" arrow.
- The **latent code** is *low-dimensional* (3 pathway axes, plus their interactions) but **continuous** — every variant lands at some specific real-valued position on the manifold, not at one of three discrete points.
- The **decoder** is cell-, time-, and circuit-specific: it reads the latent code and produces a phenotype distribution. This is where post-bottleneck heterogeneity lives.

The crucial property of autoencoders for this reframe: **a latent code being low-dimensional does not mean the model represents only a few things**. A 3-dimensional continuous code can represent infinitely many distinct configurations. The latent space is *compressed* but not *collapsed*.

## 7. Why this dissolves the puzzle

If "convergence onto 3 pathways" meant "every NDD variant lands on one of exactly 3 discrete pathway states", heterogeneity would indeed be inexplicable. But the convergence is onto a **3-axis manifold**, where every variant occupies a different real-valued position. Two variants that both perturb mTOR can land at very different mTOR-axis positions, and that position difference (plus the cell-type decoder) is what generates phenotypic diversity.

This matches the empirical picture exactly. [[neuroscience/parenti-2020-neurodevelopmental-disorders-from-genetics-to|Parenti 2020]] notes that *within* the mTOR pathway, growth-factor-arm mutations (TSC1/2/PTEN) produce different phenotypes from amino-acid-sensing-arm mutations (DEPDC5/NPRL2/3). Same pathway, different position on the pathway-axis sub-structure, different output.

## 8. The decoder is not just a noise filter — it is the engine of decompression

The most consequential difference between the cascade frame and a "single mapping with noise" frame is what happens after the bottleneck. In the autoencoder analogy, the decoder is *not* a passive reader. It is a function with its own structure, parameters, and context. The same latent code passed through different decoder contexts produces qualitatively different outputs. In NDDs:

- Same mTOR hyperactivity in a glutamatergic neuron → synapse hypertrophy → ASD-like profile
- Same mTOR hyperactivity in a GABAergic interneuron → maturation delay → seizure susceptibility
- Same mTOR hyperactivity in an astrocyte → reactive astrogliosis → altered signaling environment

The decoder *adds information* about cell type. The output is high-dimensional precisely because the decoder context is itself high-dimensional. (This is the formal point made in Part V.)

---

# Part IV — Where Each Layer of Heterogeneity Enters the Cascade

The Dvir 2026 four-layer framework was originally framed as a parallel list. In the cascade frame, the four layers map to specific cascade locations — each a different *kind* of heterogeneity entry point.

## 9. Layer 1 — The variant itself (pre-bottleneck heterogeneity)

This is the *input* heterogeneity: which variant, where, of what type. The encoder function maps each input feature to a pathway-axis displacement.

| Heterogeneity source | Effect at the bottleneck |
|---|---|
| Variant type (LoF / GoF / missense / silent) | Sign and magnitude of pathway displacement |
| Affected protein domain | Which sub-axis is hit (e.g., TSC1 vs DEPDC5: both mTOR, different arms) |
| Affected isoform | Which (cell type, time) the displacement is active in |
| *Cis*-regulatory variation | Baseline offset on the pathway axis |
| Other variants (oligogenic / polygenic) | Vector sum on the manifold |

Examples populating each entry:
- **Variant type, same gene, opposite phenotypes**: `SCN2A` LoF → ASD/ID, `SCN2A` GoF → epilepsy ([[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir 2026]] Layer 1).
- **Domain matters**: `SYT1` C2A vs C2B variants give mild vs severe Baker-Gordon syndrome (n = 22 individuals).
- **Isoform matters**: `AUTS2` 5′ vs 3′ LoF → mild vs severe ID; `ANK2` brain isoform vs cardiac isoform → ASD vs cardiac arrhythmia from the same gene.
- **Polygenic background modulates**: ASD PRS is higher in affected siblings vs unaffected siblings; ASD PRS is *lower* in carriers of *de novo* large-effect variants — the additive signal partially substitutes for the rare hit.
- **Oligogenic / two-hit examples**: 16p12.1 deletion is mild in parents who carry it alone, severe in children who carry it plus an additional CNV. Severity tracks variant accumulation across three generations.

All of this is *encoder heterogeneity*. The same gene can land at many different pathway-axis positions depending on which feature was hit.

## 10. Layer 2 — The bottleneck itself is high-dimensional, not 3-dimensional

A subtle but important point: when Parenti says "three pathways", the *biological* dimensionality is much higher. Each pathway is itself decomposable:

- **mTOR axis** — 3 sub-arms (growth factor / energy / amino acid) plus mTORC1 vs mTORC2 differential dependency.
- **Chromatin axis** — hundreds of downstream gene modules; ARID1B and SETD5 mutations both perturb "the chromatin pathway" but their dysregulated module sets only partially overlap.
- **Synaptic axis** — pre/post compartments × CAM/scaffold/receptor positions; NRXN1 LoF is at the cell-adhesion sub-axis, SHANK3 LoF is at the postsynaptic-scaffold sub-axis.

The "3-axis" description is a *useful coarse-graining*. The real bottleneck dimensionality is more likely on the order of 30-50 sub-axes, organised hierarchically with strong correlations within sub-axes and weaker correlations across pathways. This is what [[neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence|Fernandez-Garcia 2026]]'s BicMix biclustering picks up — convergence at multiple levels of granularity, with fine sub-modules nested inside broader convergent attractors.

→ At the bottleneck, heterogeneity is *the position on a high-dimensional but still low-rank manifold*.

## 11. Layer 3 — Cell type × developmental timing (deterministic post-bottleneck heterogeneity)

This is the *deterministic* portion of the decoder: given (pathway state, cell type, developmental window), the cellular response is largely determined. But cell types and windows differ widely, so even a fixed bottleneck position produces radically different cell phenotypes depending on which cell × time coordinate it is read at.

Three concrete demonstrations on the wiki:

- [[neuroscience/li-2023-single-cell-brain-organoid|Li 2023 (CHOOSE)]] — pooled CRISPR of 36 ASD risk genes in mosaic cerebral organoids. Dorsal IPs and ventral progenitors are *differentially vulnerable* to the same gene knockouts. Same encoder input, same bottleneck, different decoder coordinate, different phenotype.
- [[neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence|Fernandez-Garcia 2026]] — convergence is *cell-type-specific* and strongest in *mature glutamatergic neurons*. The decoder is more sensitive in some coordinates than others.
- [[neuroscience/jourdon-2023-modeling-idiopathic-autism|Jourdon 2023]] (idiopathic ASD father-son pairs) — macrocephalic and normocephalic carriers show *opposite* E/I imbalances. Same genetic predisposition class, different decoder context (driven by which TFs ended up high vs low), opposite phenotypic axis.

Decoder context is what produces the most clinically observable layer of NDD heterogeneity. It is also the layer most amenable to single-cell and spatial measurements ([[overviews/cell-identity-programs-and-trajectories]] for the methodology).

## 12. Layer 4 — Developmental noise (stochastic post-bottleneck heterogeneity)

The remaining heterogeneity, after controlling for input, bottleneck position, cell type, and developmental window, is what Dvir 2026 calls **developmental noise**. The companion overview [[overviews/transcriptional-heterogeneity-as-developmental-mechanism]] is dedicated to this layer in detail. Here the relevant claim is:

- Even with isogenic background and identical environmental control, monozygotic twins carrying the same NDD pathogenic variant show discordant phenotypes.
- The mechanism is **stochastic transcriptional state** in NPCs at the moment of fate commitment.
- This is a property of the decoder being a *probabilistic* function, not a deterministic one.

Stochastic decoder heterogeneity is the *floor* of NDD prediction — the irreducible variance even after every observable covariate is conditioned on. Its existence is the technical reason that distributional prediction ([[concepts/distributional-vs-point-prediction]]) is the right loss for NDD modeling: a deterministic prediction is misspecified at the decoder level.

## 13. Layer 5 — Environment (decoder modulator)

Although the user has flagged environmental factors as not their primary interest, the cascade frame makes one observation worth keeping:

**Environmental factors do not constitute a separate cascade layer; they re-enter through the same pathways as genetic variants, modulating the decoder context.**

- *Valproic acid (VPA)* — a class I/II HDAC inhibitor. Mechanistically chromatin-pathway perturbation. Prenatal VPA effects on offspring are an "environmental" exposure that lands on Layer 2 of the bottleneck.
- *Maternal immune activation (MIA)* — cytokine signaling → STAT-mediated transcription → chromatin remodeling + microglial activation → synaptic pruning. Lands on Layer 2 (chromatin) plus Layer 3 (decoder modulation via glia).
- *Early-life stress* — glucocorticoid signaling → CREB / IEG activation → chromatin remodeling. Lands on Layer 2.
- *5-hmC variability in `Cntnap2` GxE* — gene × environment manifests as epigenetic variance ([[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir 2026]] case study). Layer 2 again.

Two methodological consequences are independently important even for researchers who do not study environment per se:

- **Most "environmental" effects in NDD epidemiology shrink dramatically under sibling controls / Mendelian randomisation / polygenic adjustment.** What looks like an environmental effect is often *gene-environment correlation* (parental genetic nurture). This is a methodological caveat that re-reads much of the existing NDD environment literature.
- **MIA studies show that timing and magnitude of inflammation matter more than pathogen identity.** This points to the *immune integrator* (microglia, cytokine load) as the proximate decoder modulator, not specific infections.

Net: the environment is one of several routes by which the chromatin and synaptic axes are perturbed. In the cascade frame, it is *not* a separate layer; it is an *alternative input* to the same encoder + decoder structure.

---

# Part V — The Information-Theoretic View

## 14. Data processing inequality

A formal point that helps: the **data processing inequality** says that the information content of a signal cannot increase as it passes through a deterministic processing pipeline. So if the cascade is purely:

```
INPUT → BOTTLENECK → OUTPUT
```

with each arrow a deterministic function, then `H(OUTPUT) ≤ H(BOTTLENECK) ≤ H(INPUT)`. Information at the bottleneck cannot exceed information at the input; output information cannot exceed bottleneck information.

But empirically the OUTPUT layer (phenotype space — penetrance, expressivity, comorbidity, age of onset, severity, ...) is *very* high-dimensional. If `H(BOTTLENECK)` is small (3 pathway axes × continuous), how does `H(OUTPUT)` remain large?

## 15. Decoder context as side information

The answer is that the cascade is not a single chain. It is a chain *plus side inputs* at each decoder step:

```
INPUT  →  BOTTLENECK  →  OUTPUT
                ↑
                | (side info)
                |
           cell type
           developmental timing
           circuit configuration
           stochastic state
```

Each side input adds its own entropy to the decoder. The output information is bounded above by `H(BOTTLENECK) + H(side-info-1) + H(side-info-2) + ...`, which can be very large even when `H(BOTTLENECK)` is small.

This is the *formal* reason why a low-dimensional bottleneck does not mean a low-dimensional phenotype space. The bottleneck only constrains the *bottleneck-attributable* portion of phenotype variance. The remainder is the side-information-attributable portion, decoder-deterministic, decoder-stochastic, or both.

## 16. Implication: variance decomposition is the right tool

The information-theoretic view directly recommends a methodology — **partition phenotype variance by cascade source**:

| Variance source | What it measures | Methodologically reachable via |
|---|---|---|
| Encoder (input → bottleneck) | "Pathway effect" of the variant | Pathway-level perturbation experiments; coarse aggregate analyses |
| Bottleneck position | "Which sub-axis was hit, how strongly" | Fine-resolution sub-pathway analyses; manifold-based methods |
| Cell-type decoder (deterministic) | "Same pathway state, different cell types respond differently" | Single-cell perturbation; cell-type-stratified analyses |
| Stochastic decoder | "Identical inputs still produce variable outputs" | Isogenic systems; clone-paired analyses |
| Side-information modulators | "Environment / timing / circuit modify the response" | Controlled perturbation × context combinations |

Single-cell perturbation methods ([[overviews/perturbation-prediction-and-causal-inference]], [[overviews/six-open-issues-perturbation-modelling]]) are the natural empirical instrument because they touch most of these variance sources simultaneously — but only if the analysis explicitly retains heterogeneity instead of collapsing to means.

---

# Part VI — Resolving the Paradox at Each Cascade Location

The two original observations now have specific cascade homes:

| Observation | Cascade location | Why it is true |
|---|---|---|
| **Convergence onto 3 pathways** | The funnel from INPUT to BOTTLENECK | Many high-dim inputs map to a low-dim manifold |
| **Variant-type / domain / isoform variability** | INPUT layer of the encoder | Different input features are different inputs |
| **Manifold-position variability within "the same pathway"** | Inside the BOTTLENECK | The bottleneck is graded and high-dim, not 3 discrete points |
| **Cell-type / developmental-timing variability** | DETERMINISTIC decoder | Different decoder contexts read the same code differently |
| **Penetrance / expressivity / monozygotic twin discordance** | STOCHASTIC decoder | The decoder is probabilistic, not deterministic |
| **Environmental modifier effects** | Decoder context modulator (Layer 5) | Same encoder/bottleneck routes, alternative input |
| **Drug rescue post-mitotically** | Bottleneck-level intervention | Pathway state is the controllable level even after fate commitment |

Reading down this table, both Parenti's convergence claim and Dvir's heterogeneity claim are simultaneously true — they refer to different rows. There is no actual disagreement.

The reframing converts a "puzzle" into a "research program": **for any NDD finding, ask which row of this table it belongs to.** Disputes that look like they are about whether NDDs are more convergent or more heterogeneous often turn out to be disputes about which cascade row two researchers are measuring.

## 17. Dual perspectives on the same case study — `SHANK3`

A worked example that exercises all five layers:

`SHANK3` mutations are one of the cleanest demonstrations of the multipathway loop ([[neuroscience/parenti-2020-neurodevelopmental-disorders-from-genetics-to|Parenti 2020]]):
- Encoder layer — `SHANK3` LoF positions on the synaptic axis (postsynaptic scaffold sub-axis specifically).
- Bottleneck — through the multipathway loop, the synaptic perturbation propagates to the chromatin axis (Shank3+/− mice show histone acetylation changes) and to the mTOR axis (SHANK3 transcriptome enriched for FMRP targets; FMRP modulates mTOR translation).
- Cell-type decoder — synaptic-pathway perturbation lands hardest on neurons that depend most on PSD scaffold integrity (mature glutamatergic neurons).
- Stochastic decoder — different individuals with overlapping `SHANK3` genotypes show different ASD severities; the unexplained variance is the stochastic decoder.
- Environmental — early-life stress further modulates the decoder context.

The same gene — same encoder input — produces a heterogeneous phenotype distribution that is *also* concentrated on a small region of the bottleneck manifold. Convergence and heterogeneity at the same time, exactly as the framework predicts.

---

# Part VII — Mapping the Phase 1 Research Questions onto the Cascade

For a researcher doing single-cell + perturbation work on NDD convergence, the cascade frame is not just a conceptual organiser — it is a way to see *which cascade location each research question targets*.

The Phase 1 questions articulated in [[overviews/convergent-regulation-across-systems]] map cleanly:

| Phase 1 question | Cascade location | What is being measured |
|---|---|---|
| Trajectory × cell-type × convergence | DECODER specificity | "Where in cell-type × time space is convergence sharpest?" |
| Variant-type-specific convergence | ENCODER mapping function | "Do LoF / missense / GoF variants land at different bottleneck coordinates?" |
| Drug → signature → phenotype chain | DECODER invertibility | "Can a downstream drug push the cell back along the cascade to a healthier signature?" |

This mapping exposes a useful structural fact: the three Phase 1 questions are not independent. They are about *three different mathematical operators* on the same cascade — the encoder map, the latent geometry, and the decoder inverse. A paper that unifies all three in a single perturbation experiment is doing the most ambitious thing one could do at this level of the field.

[[neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence|Fernandez-Garcia 2026]] is the closest existing instance — pooled CRISPR-KO (encoder), BicMix manifold structure (bottleneck), Connectivity Map drug rescue (decoder inverse) — but its variant-type axis is restricted (knockouts only) and its decoder coverage is restricted (NPC + GLUT + GABA). A follow-up that retained both the *variant-type* axis (via base/prime editing or CRISPRi titration) and the *full decoder* axis (across timing windows + glia + spatial context) would address Phase 1 in its full scope.

[[overviews/six-open-issues-perturbation-modelling|Six open issues]] enumerates the methodological gaps; this overview's contribution is to argue that the gaps are not arbitrary — they are exactly the cascade locations where current methods are weakest.

---

# Part VIII — Methodological Agenda

The cascade frame implies a concrete methodological program. Each item is a measurable target.

## 18. Variance decomposition at single-cell resolution

The bulk-genetics analogue (heritability, hLDSC) decomposes variance into genetic vs environmental components. The single-cell analogue does not exist with developmental-noise interpretability. This is the single biggest measurement gap in the cascade frame.

What it would look like: for each variant × cell-type × time triple, partition single-cell phenotype variance into:
- Encoder variance (different inputs at the same bottleneck)
- Bottleneck variance (same encoder input, manifold position differs by sub-axis hit)
- Deterministic decoder variance (same code, different cell type / window)
- Stochastic decoder variance (irreducible)

[[neuroscience/dubuc-2026-linking-rare-variants-cell-type|Dubuc 2026]] (linking rare variants to cell-type function via FM inference) is one piece of this puzzle. It does not yet give a clean variance-component decomposition, but it begins to make the rare-variant → cell-type-effect arrow measurable.

## 19. Distributional prediction over point prediction

[[concepts/distributional-vs-point-prediction]] argues for distributional loss in single-cell models. The cascade frame strengthens that argument: because the decoder is probabilistic, *any* point prediction misses the floor of stochastic decoder variance. The right target is `P(phenotype | variant, cell-state)`, learned over enough data to estimate the conditional distribution shape.

[[single-cell-dl/li-2026-save-a-generalizable-framework|SAVE]] (multi-condition single-cell generation) and [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co|PerturBERT]] (gene co-perturbation transformer) are recent examples of distributional models for perturbation prediction. [[single-cell-dl/maddu-2026-learning-biophysical-models-of|PFM]] (biophysical foundation model in gene space) goes one step further by encoding a mechanistic prior into the distributional model — closer to a constrained autoencoder where the latent code has biophysical meaning.

## 20. Decoder identification — the biggest open methods question

To do variance decomposition we need to *identify* the decoder. This is hard because the decoder is high-dimensional, cell-type-specific, time-varying, and partially stochastic. Current approaches each capture a piece:

- **Cell-type stratified analyses** ([[neuroscience/li-2023-single-cell-brain-organoid|Li 2023]], [[neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence|Fernandez-Garcia 2026]]) — control for the deterministic decoder by comparing within cell types.
- **Trajectory-based methods** ([[overviews/cell-identity-programs-and-trajectories]]) — control for developmental timing.
- **Lineage-resolved atlases** ([[overviews/transcriptional-heterogeneity-as-developmental-mechanism]] Part VII) — observe stochastic decoder directly through clone-paired comparisons.
- **Foundation-model embeddings** ([[overviews/cell-identity-programs-and-trajectories]] §6.6) — implicit decoder representations at scale.

What is *not* yet on the wiki is a method that explicitly ties all three decoder dimensions (cell type × time × stochastic) into one variance-decomposition framework. This is the methodological gap most directly recommended by the cascade frame.

## 21. Intervention design — choosing the cascade row

The framework also makes intervention design legible. For any proposed therapy, ask: which cascade row does it act on?

- **Pre-bottleneck (encoder-level) interventions** — gene therapy, ASOs, CRISPR base/prime editing. Most direct, but carries the burden of variant-specificity.
- **Bottleneck-level interventions** — drugs targeting pathway nodes (rapamycin, HDAC inhibitors). Generic across many variants, narrow across pathways. The convergence frame is what makes these viable.
- **Deterministic decoder interventions** — cell-type-targeted approaches (DREADDs, optogenetics, cell-type-specific gene therapy). Capture the specificity of the deterministic decoder.
- **Stochastic decoder interventions** — interventions that *reduce variance* rather than shift means (anything that improves developmental robustness, e.g., reducing cellular stress). Currently the least-explored category.
- **Side-information modulators** — environmental / developmental intervention (early-life enrichment, prenatal nutrition, etc.).

A treatment plan can combine multiple rows. The cascade view makes the combination structure explicit instead of leaving it intuitive.

---

# Closing — How This Overview Sits Between the Two Sides

This overview does not introduce new biology beyond what the convergence and heterogeneity overviews already cover. Its contribution is *structural*: it provides a single framework — the cascade with encoder, low-dimensional manifold bottleneck, and cell-type-specific stochastic decoder — within which both sides of the NDD literature become non-conflicting predictions of the same model.

The intended reading order:
1. Start with the empirical evidence: [[neuroscience/parenti-2020-neurodevelopmental-disorders-from-genetics-to|Parenti 2020]] and [[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir 2026]] — the two NDD reviews.
2. Read each side's overview separately:
   - Convergence side → [[overviews/convergent-regulation-across-systems]] (uses ASD + cancer drug-resistance evidence to make the convergence case)
   - Heterogeneity side → [[overviews/transcriptional-heterogeneity-as-developmental-mechanism]] (uses NPC developmental work to make the mechanism-of-noise case)
3. Read this overview to see how the two reconcile into one cascade architecture.
4. Then read [[overviews/perturbation-prediction-and-causal-inference]] and [[overviews/six-open-issues-perturbation-modelling]] for the methodological program implied by the cascade.

The two key takeaways:

- **Convergence and heterogeneity refer to *different cascade locations*, not to disagreements about the same data.** Whenever they appear to conflict, ask which cascade row each side is measuring.
- **The cascade frame implies a concrete methodological agenda**: variance decomposition at single-cell scale, distributional prediction, decoder identification, intervention design by cascade row. Each of these is empirically tractable and on the near horizon for the field.

Beyond NDDs, the cascade frame likely applies to any disease class with strong pathway convergence and pervasive phenotypic heterogeneity. The framework is most clearly elaborated for NDDs because of the genetic-architecture density, but the same architecture maps onto cancer drug-resistance ([[drug-resistance/xu-2026-mapping-convergent-regulators-of|Xu 2026 PerturbFate]]'s 140+ regulators converging on a single drug-tolerant state), and the [[overviews/endogenous-variation-as-natural-perturbation]] sister overview already explored the divergence-and-convergence dual frame for general cellular perturbation. The cascade view unifies these by making explicit *which cascade location each phenomenon refers to*.
