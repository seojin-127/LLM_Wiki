---
title: "Transcriptomic and phenotypic convergence of neurodevelopmental disorder risk genes in vitro and in vivo"
authors: Meilin Fernandez Garcia, Kayla Retallick-Townsley, April Pruitt, Elizabeth A. Davidson, Novin Balafkan, et al.; Laura M. Huckins, Ellen J. Hoffman, Kristen Brennand
year: 2026
doi: 10.1038/s41593-026-02247-7
source: fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence.md
category: neuroscience
tags: [ndd, asd, crispr-ko, perturb-seq, ipsc-derived-neurons, convergence, chromatin-modifiers, glutamatergic-neurons, gabaergic-neurons, mitochondria, oxphos, zebrafish, drug-repurposing, brennand-lab, hoffman-lab, yale]
---

## Summary

Yale Brennand & Hoffman labs ask: do the many NDD risk genes — most of them chromatin/transcriptional regulators with apparently distinct functions — actually converge on shared downstream effects in human neurons? They run a **pooled CRISPR-KO of 23 NDD risk genes in 4 iPSC-derived contexts** (NPCs, immature/mature glutamatergic, GABAergic neurons; 118k cells) and quantify "convergence" as DEGs that are significantly perturbed in the **same direction across all KOs**. Three findings define the paper: (1) convergence is **highly cell-type-specific** and **strongest in mature glutamatergic neurons** despite all the targeted genes being chromatin regulators; (2) the convergent pathways include the expected synaptic and epigenetic, plus an **unexpected mitochondrial / OXPHOS signature** validated experimentally (Seahorse, mitochondrial morphology); (3) drugs predicted by Connectivity-Map to reverse the convergent signature **rescued zebrafish behavioral phenotypes in 10/11 cases** — and rescued **post-mitotically**, suggesting an actionable therapeutic window beyond the developmental period.

## Why this paper matters here

This paper sits at the intersection of three lines in the wiki:

1. **NDD/ASD convergence question** — joins [[neuroscience/paulsen-2022-autism-genes-converge]] (organoid, developmental timing), [[neuroscience/jin-2020-in-vivo-perturb-seq]] (in vivo mouse cortex), [[neuroscience/martinscosta-2024-arid1b-controls-transcriptional]], [[neuroscience/villa-2022-chd8-haploinsufficiency]]. Different model systems, same question — and they don't all agree on where convergence happens.
2. **Pooled CRISPR-KO + scRNA-seq method** — same architecture as [[neuroscience/jin-2020-in-vivo-perturb-seq]] and [[neuroscience/amelan-2026-crispr-knockout-screens-reveal]], applied to a curated NDD gene set in human iPSC-derived neurons.
3. **From convergent signature to therapy** — the drug-repurposing arc connects to the broader "in-silico perturbation → drug prediction" theme that sits behind [[overviews/perturbation-prediction-and-causal-inference]].

## Methods & Architecture

### Experimental design

```
hiPSC (single control donor)
   ├── iNPC (Nestin+, day before harvest)
   ├── immature iGLUT (NGN2 day 7)
   ├── mature iGLUT (day 21, MAP2+/vGLUT+)
   └── mature iGABA (day 36, MAP2+/GABA+)

Each context:
   1. Lenti-Cas9v2
   2. Pooled lenti gRNA library (3-4 gRNAs × 24 NDD genes)
   3. 10X scRNA-seq + gRNA assignment
   4. → 118,436 cells, ~25-38k per context
```

### 24 target NDD genes (chromatin/regulatory bias)

ANK3, ARID1B, ASH1L, ASXL3, BCL11A, CHD2, CHD8, DPYSL2, FOXP2, KMT5B (SUV420H1), KDM5B, KDM6B, KMT2C, MBD5, MED13L, NRXN1, PHF12, PHF21A, SCN2A, SETD5, SIN3A, SKI, SMARCC2, WAC.

(3 of these — DPYSL2, FOXP2, SCN2A — were underrepresented in the gRNA library.)

### Convergence definition (the operational core)

For each cell type:
- Pseudobulk per (KO × cell type), DEGs vs non-targeting (LIMMA)
- Meta-analyze across all KOs (METAL) → for each gene, P_meta and Cochran Q
- **Convergent gene** = FDR-adjusted P_meta < 0.05 AND Q P_Het > 0.05 (significant + consistent direction)
- Repeat for all C(n, r) subsets of KOs to quantify convergence strength as a function of how many KOs are required to share the effect

### Drug prediction

Connectivity-Map-style query: take the convergent transcriptomic signature → search LINCS L1000 for compounds whose signature is anti-correlated → cross-reference with arousal/sensory behavioral signatures from prior zebrafish behavior data → shortlist for in vivo testing.

### Zebrafish in vivo validation

- 17 mutant lines or F0 crispants of NDD orthologs (chd8, ash1l, arid1b, kdm5b a/b, kmt5b, kmt2c a/b, nrxn1a, etc.)
- High-throughput behavior battery → 4 behaviorally-correlated mutant clusters
- Drug exposure on each mutant → behavioral rescue scoring (rescued / partial / unchanged / over-corrected / exacerbated)

## Results

### Per-cell-type convergence patterns

- **DEG overlap between cell types is poor** at strict FDR — often the only common DEG between two cell types is the targeted gene itself.
- Convergent gene count (across the 9 NDD genes resolved in all 4 contexts): **mature iGLUT >> immature iGLUT ~ mature iGABA > iNPC**.
- Cross-cell-type correlation of convergence magnitude is highly significant (P_holm < 2.2 × 10⁻¹⁶), with strongest correlation between immature and mature iGLUT.
- >50% of convergent genes in NPC, immature iGLUT, and mature iGABA overlap with mature iGLUT convergent set — but **direction of effect is not necessarily preserved across cell types**.

### Pathway convergence in mature iGLUT

Three pathway clusters dominate the convergent DEGs:
- **Synaptic** (pre-synaptic, post-synaptic, neurotransmitter regulation) — expected
- **Epigenetic** (chromatin organization, histone methylation, SWI/SNF complexes) — expected (since most KOs are chromatin regulators)
- **Mitochondrial / OXPHOS** (inner membrane, ETC, TCA, complex I assembly, mito translation) — **unexpected**

### Mitochondrial validation (the surprise that they bothered to chase)

Three KOs (NRXN1, ASH1L, ARID1B) selected for orthogonal validation:
- **OXPHOS protein expression** (IF intensity) — altered
- **Seahorse OCR** — reduced coupled and maximal respiration
- **Mitochondrial morphology** — altered sphericity / branch length, especially in dendrites
- **Mitochondrial membrane potential** (TMRM) — altered

This is a real experimental claim, not just an enrichment artifact.

### What predicts convergence between two NDD genes?

Convergence strength between gene-pairs correlates with:
- Shared GO biological annotation
- Shared clinical association (ASD vs DD vs SCZ)
- **Postmortem brain co-expression patterns**

Authors' interpretation: convergence reflects developmental brain co-expression structure, not just shared annotation.

### GWAS / rare-variant burden

Convergent gene sets enriched for SCZ-LoF, ASD-LoF, ID-LoF rare variant burden, and SCZ/BIP common-variant signal (MAGMA). Connects in-vitro perturbation results back to population-level genetic risk.

### In vivo drug rescue

10 of 11 tested drugs ameliorate ≥1 behavioral phenotype in the matched zebrafish mutant. Notable pairs:
- chd2 × Pravastatin
- kdm6b × Paclitaxel
- ash1l × Sunitinib / Rosiglitazone / Repaglinide / Ezetimibe
- phf21a × Fluvoxamine / Amiodarone
- kmt5b × Sirolimus / Paclitaxel

Drugs are administered post-developmentally → "reverse, not prevent" — implies a clinically actionable window after symptom onset.

## Limitations

- **Single hiPSC donor** — no genetic background diversity, despite the paper's discussion arguing background matters.
- NGN2-induced glutamatergic neurons reach a relatively early maturation state (day 21) — not adult cortical neurons.
- 23/24 genes are chromatin/transcription regulators — convergence patterns may not generalize to "neuronal communication" class NDD genes (NRXN1 is the main exception in the set).
- Drug rescue in zebrafish ≠ rescue in human; partial rescues for many drugs.
- Convergence is defined statistically (meta-analysis FDR + heterogeneity) — operational, but conservative and direction-monotonic.
- gRNA dropout for DPYSL2, FOXP2, SCN2A → underpowered for those.

## Related Papers

### Direct convergence-of-NDD-genes lineage
- [[neuroscience/paulsen-2022-autism-genes-converge]] — Arlotta lab cortical organoid CRISPR screen; convergence on **asynchronous developmental timing**, not (only) mature-neuron pathway. Complementary frame.
- [[neuroscience/jin-2020-in-vivo-perturb-seq]] — Macosko/Arlotta in vivo Perturb-Seq in mouse cortex. Same method, different model system, NDD risk genes.
- [[neuroscience/villa-2022-chd8-haploinsufficiency]] — single-gene deep dive on CHD8 (one of the genes in this screen).
- [[neuroscience/martinscosta-2024-arid1b-controls-transcriptional]] — single-gene deep dive on ARID1B (another).
- [[neuroscience/jourdon-2023-modeling-idiopathic-autism]] — iPSC modeling of idiopathic ASD, complementary genetic-architecture lens.
- [[neuroscience/morelli-2022-mecp2-related-pathways-cortical]] — MeCP2 / Rett pathway convergence.

### Method kin
- [[neuroscience/amelan-2026-crispr-knockout-screens-reveal]] — CRISPR KO screen design, related architecture.
- [[neuroscience/dubuc-2026-linking-rare-variants-cell-type]] — rare variants → cell-type-specific effects, complementary statistical approach.

### Broader perturbation modeling context
- [[overviews/perturbation-prediction-and-causal-inference]] — landscape page; this paper is the "real wet-lab perturbation" anchor for the in-silico methods.
- [[overviews/six-open-issues-perturbation-modelling]] — Dimitrov 2026 — "convergence" in this paper directly addresses the "interpretation" axis.
- [[overviews/convergent-regulation-across-systems]] — synthetic page on convergent regulation across ASD/melanoma/etc.; this paper extends the convergence theme into glutamatergic neuron context with a mitochondrial twist.
- [[overviews/cell-identity-programs-and-trajectories]] — cell-type-specific convergence speaks to cell-identity-program framing.
