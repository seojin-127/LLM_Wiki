---
title: "Complex genotype–phenotype relationships in neurodevelopmental disorders"
authors: Elad Dvir, Eran Meshorer, Sagiv Shifman
year: 2026
doi: 10.1016/j.tig.2026.03.005
source: dvir-2026-complex-genotype-phenotype-relationships-in.md
category: neuroscience
tags: [NDD, genotype-phenotype, penetrance, expressivity, modifier-genes, polygenic, oligogenic, GxE, developmental-noise, review, Trends-in-Genetics, Hebrew-University-Jerusalem]
---

## Summary
A *Trends in Genetics* review (Hebrew U Jerusalem) framing the **inverse-of-convergence question** in NDDs: hundreds of high-confidence risk genes are now known, yet individuals carrying *the same pathogenic variant* often show very different diagnoses and severities. Dvir, Meshorer, and Shifman lay out a four-layer framework — the variant itself, modifying genome, environment, developmental noise — with concrete NDD case studies for each, plus a quantitative breakdown showing only ~4.5% of incomplete-penetrance cases remain unexplained after these layers are accounted for.

## Key Contributions
- **Reframes** the NDD genetics literature by stating the *inverse* of the convergence question: not "why do hundreds of genes give the same phenotype?" (the [[parenti-2020-neurodevelopmental-disorders-from-genetics-to|Parenti et al. 2020]] / Sanders-style framing) but **"why does the same variant give hundreds of phenotypes?"**
- Proposes an explicit **four-layer causal frame** for variable expressivity:
  1. *Variant itself* — class (LoF / missense / GoF), affected protein domain, isoform context.
  2. *Other genetic elements* — additive PRS, oligogenic two-hit, paralog buffering, *cis*-regulatory modifiers.
  3. *Environment* — prenatal MIA, prenatal VPA, early-life stress; gene × environment.
  4. *Developmental noise* — measurable stochastic variation between genetically + environmentally identical individuals.
- Uses a **gnomAD-scale penetrance audit** (Chen et al., 807,162 individuals × 77 haploinsufficient genes) to put numbers on the layers — position/isoform effects ≈40%, combined ≈31.5%, *cis*-regulatory ≈7.8%, somatic ≈5.7%, unexplained ≈4.5%.

## Methods & Architecture
This is a review, not an empirical paper, so "method" = the conceptual framework and the curated case studies that populate each layer. The four-layer figure (Figure 1, the review's Key figure) is the structural backbone; subsequent figures (2: mutation type / domain / isoform; 3: polygenic / oligogenic / regulatory; 4: prenatal / early-life environment) decompose each layer into testable sub-mechanisms.

The review's dominant pedagogical move is **paired NDD-gene case studies** — each layer is grounded in 2–4 well-studied risk genes (`SCN2A`, `SYT1`, `AUTS2`, `ANK2`, `POGZ`, `Cntnap2`, etc.) where the layer's mechanism has been empirically demonstrated.

## Results
The "results" of a review are the case-study landings, organized by layer:

| Layer | Gene | Phenotypic axis demonstrated |
|---|---|---|
| Variant class | `SCN2A` | LoF → ASD/ID vs GoF → epilepsy (opposite-direction electrical phenotypes) |
| Affected domain | `SYT1` | C2B → severe + movement disorder; C2A → milder (n=22 individuals) |
| Affected isoform | `AUTS2` | 3′ LoF (both isoforms) → severe ID; 5′ LoF (long-isoform-only) → milder |
| Affected isoform | `ANK2` | Tissue-specific isoforms (220/440/212/160 kDa) → ASD vs cardiac arrhythmia |
| Polygenic | ASD PRS | Higher in affected vs unaffected siblings; lower in de-novo carriers (additive) |
| Oligogenic | 16p12.1 del | Inherited carrier mild; secondary CNV in child = severe; severity tracks across 3 generations |
| Paralog buffer | `Sall1` / `Sall4` | KO of `Sall1` rescued by `Sall4` |
| *Cis*-regulatory | `RET`, `SHROOM3` | Enhancer / eQTL variation modulates penetrance of pathogenic LoF |
| GxE | `Cntnap2 +/−` | Asymptomatic until prenatal stress → repetitive behaviors + 5-hmC variability |
| GxE | `Npas4 +/−` | Sex-specific (male only) social-deficit phenotype after prenatal stress |

## Limitations
- Causal disentanglement of gene-environment effects in **humans** is methodologically hard — confounding via gene-environment correlation and parental "genetic nurture" can mimic direct intrauterine effects.
- **Developmental noise** is the least empirically tractable layer — requires isogenic systems (organoid, mouse isogenic lines) that imperfectly model human brain development.
- **PRS portability** across ancestries limits generality of polygenic-modifier conclusions ([[missing-diversity-in-genomics]]).
- **Functional prediction** for rare missense and noncoding variants is still poor.
- Integration with **single-cell + perturbation genomics** is named as a future direction but not prescribed.

## Related Papers
- [[parenti-2020-neurodevelopmental-disorders-from-genetics-to]] — *the convergence-direction mirror*. Same NDD gene set, opposite question (different genes → common pathways: synaptic plasticity, chromatin remodelers, mTOR). Read together for a complete picture of the NDD genotype-phenotype problem.
- [[fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence]] — empirical convergence test (pooled CRISPR-KO + zebrafish drug rescue) that Dvir's framework provides the *counterweight* to.
- [[paulsen-2022-autism-genes-converge]] — autism-gene convergence in cortical organoids.
- [[jourdon-2023-modeling-idiopathic-autism]] — idiopathic autism iPSC modeling — relevant to developmental-noise framing.
- [[amelan-2026-crispr-knockout-screens-reveal]] — CRISPR screens for ASD risk genes.
- [[overviews/convergent-regulation-across-systems]] — overview that Dvir 2026 reframes as the *inverse* question.
- [[de-jong-2021-cortical-overgrowth-preclinical]], [[villa-2022-chd8-haploinsufficiency]], [[morelli-2022-mecp2-related-pathways-cortical]], [[martinscosta-2024-arid1b-controls-transcriptional]], [[mato-blanco-2025-early-developmental-origins]] — single-gene NDD models that populate the Layer 1 case-study evidence.
