---
title: "Complex genotype–phenotype relationships in neurodevelopmental disorders"
authors: Elad Dvir, Eran Meshorer, Sagiv Shifman
year: 2026
doi: 10.1016/j.tig.2026.03.005
category: neuroscience
pdf_path: papers/dvir-2026-complex-genotype-phenotype-relationships-in.pdf
pdf_filename: dvir-2026-complex-genotype-phenotype-relationships-in.pdf
source_collection: nature-springer-direct
---

## One-line Summary
A *Trends in Genetics* review (Hebrew U Jerusalem) framing the **inverse-of-convergence question** in NDDs — *why pathogenic variants in the same gene give different phenotypes* — through four interacting layers (the variant itself, modifying genome, environment, developmental noise) with concrete case studies and a unified causal framework.

## 1. Document Info
- **Journal**: Trends in Genetics
- **Volume / Year**: Vol. xx, No. xx, 2026 (in-press; March 2026)
- **DOI**: 10.1016/j.tig.2026.03.005
- **Type**: Review
- **Length**: 13 pages
- **Authors / Affiliations**:
  - Elad Dvir¹ — Department of Genetics, The Alexander Silberman Institute of Life Sciences, Hebrew University of Jerusalem
  - Eran Meshorer¹,² — same + The Edmond and Lily Safra Center for Brain Sciences (ELSC), Hebrew U Jerusalem (epigenetics, brain development)
  - Sagiv Shifman¹ — same as Dvir (NDD genetics, ASD risk genes)
- **Lab landscape**: Meshorer lab works on epigenetic regulation of neural identity (chromatin, pluripotency); Shifman lab focuses on the genetic architecture of ASD and NDDs at population scale. The pairing brings together epigenetic / developmental noise framings with population-genetic perspectives — a relatively distinctive Israeli outpost in NDD genetics review writing, with frequent cross-listing to gnomAD-scale and family-cohort analyses.

## 2. Key Contributions
- **Reframes the question** from the more common "different genes converge on the same phenotype" to its inverse: *the same pathogenic variant produces different phenotypes — why?* This is exactly the methodological complement to convergence-direction reviews like [[parenti-2020-neurodevelopmental-disorders-from-genetics-to|Parenti et al. 2020]].
- **Four-layer causal frame** for variable expressivity (Figure 1, Key figure):
  1. **Allelic variation in the gene itself** — variant class (LoF/missense/GoF), affected protein domain, affected isoform.
  2. **Other genetic elements** — polygenic background (additive small-effect), oligogenic "two-hit" rare-variant combinations, paralog buffering, *cis*-regulatory variation.
  3. **Environmental factors** — prenatal exposures (maternal immune activation, valproic acid), early-life stress (limited bedding/nesting paradigms in mice), gene × environment interaction.
  4. **Developmental noise** — stochastic variability between genetically and environmentally identical individuals.
- Highlights that **only ~4.5% of incomplete-penetrance cases remain unexplained** in a large gnomAD analysis (Chen et al.); ~40% are position/isoform effects, 31.5% combined explanations, 7.8% *cis*-regulatory rescue, 5.7% somatic mosaicism.
- Argues for **integrative approaches** combining population-scale genetics, functional genomics, environmental monitoring, and quantitative measurements of stochastic developmental variation.

## 3. Conceptual Architecture (the framework, in lieu of methods)
Four explanation layers, each illustrated with paradigmatic NDD case studies:

### Layer 1 — The variant itself
- **Mutation type** — `SCN2A`: GoF → epilepsy; LoF → ASD/ID. Same gene, opposite-direction electrical phenotypes.
- **Affected protein domain** — `SYT1` (Baker-Gordon syndrome, n=22): C2B domain variants → severe + early movement disorder; C2A → milder.
- **Affected isoform** — `AUTS2`: 3′ LoF disrupts both isoforms → severe ID; 5′ LoF affects long isoform only → milder. `ANK2` 220 kDa (ubiquitous) vs 440 kDa (brain) vs 212 kDa (muscle) vs 160 kDa (heart) explain ASD vs cardiac arrhythmia phenotypes.
- **Quantitative breakdown** (Chen et al., 807,162 gnomAD individuals, 77 haploinsufficient genes): position/isoform effects ≈40%, combined ≈31.5%, *cis*-regulatory ≈7.8%, somatic ≈5.7%, unexplained ≈4.5%.

### Layer 2 — Other genetic elements
- **Polygenic additive** — ASD PRS higher in affected vs unaffected siblings; lower in de-novo-variant carriers (additive complementarity).
- **Oligogenic / "two-hit"** — 16p12.1 deletion: parental carriers often mild; affected children carry secondary CNV; severity tracks variant accumulation across 3 generations. Different secondary-variant pathways differentiate phenotypic axes (neurogenesis → growth/skeletal; hedgehog → behavioral).
- **Paralog buffering** — Disease genes have fewer paralogs (selection signature). `Sall1` rescued by `Sall4`; `Lhx1`/`Lhx5` Purkinje pair; `Tbx1`/`Tbx2`/`Tbx3` craniofacial-cardiac.
- ***Cis*-regulatory variation** — Enhancer / promoter QTLs modulating expression level/timing of risk genes (`RET` Hirschsprung; `SHROOM3` craniofacial microsomia).

### Layer 3 — Environment × genotype
- **Prenatal MIA (maternal immune activation)** — LPS / poly(I:C) in pregnant mice → cerebellar neuroinflammation, synaptic-pruning defects, ASD-like offspring behavior.
- **Prenatal VPA** (valproic acid, a class I/II HDAC inhibitor) — disrupts neurogenesis, synaptic plasticity, E/I balance.
- **GxE in mice** — `Cntnap2 +/−` females asymptomatic until prenatal stress reveals repetitive behaviors + altered sociability; effect tracks 5-hmC variability. `Npas4 +/−` males (not females) exposed to prenatal stress show social deficits.
- **Early-life stress** — Limited bedding-and-nesting (LBN) in `Cntnap2 +/−` produces microglial morphology changes; similar GxE for `Shank3`, `D2`, `MeCP2`.
- **Human evidence is harder** — confounded by gene-environment correlation, parental genetic nurture, ascertainment bias. MoBa cohort: maternal fever associated with modest ASD-risk increase; specific infections weaker. Triangulation (sibling controls, MR, polygenic analyses) often shrinks reported associations.

### Layer 4 — Developmental noise
- Stochastic variability *between* monozygotic twins / isogenic clones / siblings sharing pathogenic variants, after controlling for genetic + environmental factors.
- Quantitative framing: developmental noise as a measurable axis of phenotypic variance, not residual error.

## 4. Key Examples (the review's evidence base)
| Gene | Variant feature | Phenotypic axis |
|---|---|---|
| `SCN2A` | LoF vs GoF | ASD/ID vs epilepsy |
| `SYT1` | C2A vs C2B domain | mild vs severe + movement disorder |
| `AUTS2` | 5′ vs 3′ LoF | mild vs severe ID |
| `ANK2` | tissue-specific isoforms | ASD vs cardiac arrhythmia |
| `POGZ` | DD penetrance | ~100% DD; ~50% ASD; ~50% microcephaly |
| 16p12.1 del | inheritance + 2nd hit | parental mild ↔ child severe |
| `Cntnap2 +/−` | × prenatal stress | asymptomatic → ASD-like |
| `RET` | enhancer modifier | Hirschsprung penetrance |

## 5. Limitations & Open Questions Acknowledged
- Causal disentanglement of gene-environment interactions in humans remains methodologically hard (confounding, ascertainment).
- Quantifying developmental noise requires controlled isogenic systems (organoids, mouse isogenic lines) that don't perfectly model human brain development.
- PRS portability across ancestries limits the generality of polygenic-modifier conclusions ([[missing-diversity-in-genomics]]).
- Variant-level functional prediction is still poor for many rare missense and noncoding variants, hampering the variant-itself layer.
- Integration with functional genomics (single-cell, perturbation) is named as a future direction but not deeply prescribed.

## 6. Related Work
- **Inverse-of-this review** (convergence direction): [[parenti-2020-neurodevelopmental-disorders-from-genetics-to|Parenti et al. 2020]] — same gene panel, asks "different genes converge on common pathways"; this Dvir review asks "same gene diverges into different phenotypes". The two are *complementary halves* of the NDD genotype-phenotype problem.
- **Empirical convergence work** that this review's framing motivates:
  - [[fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence|Fernandez-Garcia & Brennand-Hoffman 2026]] — pooled CRISPR-KO + zebrafish drug rescue for NDD convergence (this Dvir review provides the *theoretical* counterweight).
  - [[paulsen-2022-autism-genes-converge|Paulsen 2022]] — autism genes converging on shared developmental targets in cortical organoids.
  - [[jourdon-2023-modeling-idiopathic-autism|Jourdon 2023]] — modeling idiopathic autism in iPSC.
  - [[amelan-2026-crispr-knockout-screens-reveal|Amelan 2026]] — CRISPR-KO screens for ASD genes.
- **Synthesis pages**:
  - [[overviews/convergent-regulation-across-systems]] — directly answers "why hundreds of mutations converge on the same phenotype"; this Dvir review is the *open-mirror* question.
- **Related NDD-relevant work**: [[de-jong-2021-cortical-overgrowth-preclinical|de Jong 2021]], [[villa-2022-chd8-haploinsufficiency|Villa 2022]] (CHD8), [[morelli-2022-mecp2-related-pathways-cortical|Morelli 2022]] (MeCP2), [[martinscosta-2024-arid1b-controls-transcriptional|Martins-Costa 2024]] (ARID1B), [[mato-blanco-2025-early-developmental-origins|Mato-Blanco 2025]].

## 7. Glossary (paper's own glossary, condensed)
- **ASD** — autism spectrum disorder
- **DD / ID** — developmental delay / intellectual disability
- **Penetrance** — proportion of variant carriers showing the phenotype
- **Expressivity** — severity/specificity of phenotype among carriers
- **PRS** — polygenic risk score (cumulative small-effect variants)
- **Oligogenic model** — small number of rare variants jointly producing a phenotype (vs. polygenic model = many small-effect)
- **Epistasis** — non-additive interaction; one variant's effect depends on another
- **Paralogous genes** — duplication-derived siblings with overlapping function (paralog buffering = mutual rescue)
- ***Cis*-regulatory** — non-coding sequences (promoters, enhancers, silencers, insulators) acting in *cis* on adjacent genes
- **eQTL** — locus where genotype associates with expression of a gene
- **MIA** — maternal immune activation (prenatal infection / inflammation)
- **VPA** — valproic acid (HDAC class I/II inhibitor; antiepileptic; teratogenic for ASD-like phenotype in offspring)
- **Modifier gene** — gene whose variation alters the phenotype of a variant in another gene
- **Developmental noise** — stochastic variation in development not attributable to genetics or environment
- **LBN** — limited bedding-and-nesting (a mouse early-life stress paradigm)
