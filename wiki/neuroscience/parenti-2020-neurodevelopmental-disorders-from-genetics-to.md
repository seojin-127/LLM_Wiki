---
title: "Neurodevelopmental Disorders: From Genetics to Functional Pathways"
authors: Ilaria Parenti, Luis G. Rabaneda, Hanna Schoen, Gaia Novarino
year: 2020
doi: 10.1016/j.tins.2020.05.004
source: parenti-2020-neurodevelopmental-disorders-from-genetics-to.md
category: neuroscience
tags: [NDD, convergence, mTOR, mTORopathy, chromatin-remodelers, synaptic-signaling, two-hit, gene-vulnerability, BAF-complex, FMRP, multipathway-loop, review, Trends-in-Neurosciences, IST-Austria, Novarino-lab]
---

## Summary
A widely-cited *Trends in Neurosciences* review from the Novarino lab (IST Austria) crystallising the **convergence framing** of neurodevelopmental disorders: hundreds of NDD-implicated genes act through three highly interconnected core molecular pathways — PI3K-mTOR (protein synthesis), transcriptional/epigenetic regulation, and synaptic signaling — that bridge into a "multipathway loop". Convergence is set against a genetic-architecture frame of *gene vulnerability + mutational load + the two-hit model* that explains intra-gene phenotypic variability via germline×somatic interactions and oligogenic cumulative burden.

## Key Contributions
- Sets the **convergent-pathway thesis** for NDDs: the empirical pattern that, despite genetic heterogeneity, NDD-causal genes act on three pathway families (mTOR, chromatin/transcription, synaptic). This becomes the dominant framing through which much subsequent NDD work — including organoid convergence ([[paulsen-2022-autism-genes-converge|Paulsen 2022]]) and pooled CRISPR ([[fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence|Fernandez-Garcia 2026]]) — can be read.
- Proposes the **multipathway loop**: mutations in one pathway propagate to the others (e.g., SHANK3 → FMRP/CYFIP1 → mTOR translation → histone acetylation), so therapeutic targets in any node can affect distal loop members.
- Operationalises **gene vulnerability + mutational load + two-hit** as the genetic-architecture frame for individual variability.
- Provides **Table 1**, the most comprehensive comparative table of mouse, rat, and human iPSC/organoid models for the mTOR-pathway risk genes (TSC1, TSC2, DEPDC5) at the time, including conditional Cre-driver matrices.

## Methods & Architecture
The review's structure is built around three interlocking layers:

**Layer A — Genetic-architecture priors** (Figure 1, six panels): mutational load × vulnerability axis; *de novo* AD; AR; multilocus dual diagnoses; two-hit (germline + somatic); polygenic cumulative burden.

**Layer B — Three pathway families** (Figure 2 + body text), each with paradigmatic gene cases and mouse / iPSC / organoid evidence:
1. **PI3K-mTOR** (mTORopathies) — TSC1, TSC2, PTEN, DEPDC5, NPRL2, NPRL3
2. **Transcriptional / epigenetic regulation** — MECP2, SETD5, CHD8, ARID1B (BAF), ASH1L, KMT2A, CHD family
3. **Synaptic signaling** — NRXN, NLGN, SHANK family

**Layer C — Multipathway loop**: SHANK family as the most worked example of cross-pathway propagation (synaptic → mTOR via FMRP/CYFIP1 → chromatin via histone acetylation).

## Results
Key empirical landings the review organises:

| Gene | Pathway | Key finding |
|---|---|---|
| TSC1, TSC2 | mTOR | TSC syndrome (50% ASD, 50–60% ID, 80–90% seizures); haploinsufficient mice → ASD-like + memory deficits but not tumors |
| TSC2 | mTOR | iPSC organoids reveal CLIP cells (human-specific late interneuron progenitor) as TSC tumor founder population |
| DEPDC5 | mTOR / GATOR1 | Germline LoF → focal epilepsy; +somatic biallelic → focal cortical dysplasia (canonical two-hit) |
| MECP2 | chromatin | Rett syndrome; broad pleiotropy; transcriptionally affected modules enriched for NDD risk genes |
| ARID1B | BAF complex (chromatin) | Among most frequent NDD causes; haploinsufficient mice → specific PV-interneuron reduction |
| SETD5 | chromatin | ID + ASD; haploinsufficient mice → synaptic protein dysregulation + cell-fate defects |
| CHD8 | chromatin | Strong human ASD association but mild Chd8+/− mouse phenotype (model-organism caveat) |
| NRXN1 | synaptic CAM | LoF in human neurons → synaptic + NT-release defects |
| SHANK2 | synaptic scaffold | LoF → hyperconnected excitatory neurons; transcriptome enriched for FMRP targets + chromatin/transcriptional regulators (loop entry-point) |
| SHANK3 | synaptic scaffold | Multipathway-loop poster child: connects to FMRP/CYFIP1/mTOR translation + histone acetylation; HDAC-inhibitor rescuable |

## Limitations
- **Environmental factors are explicitly out of scope** — directly stated. This is the gap [[dvir-2026-complex-genotype-phenotype-relationships-in|Dvir 2026]] fills (Layer 3 of that review).
- **Same-gene phenotypic variability** is acknowledged via gene-vulnerability + two-hit but not deeply developed as a question — the inverse problem (why same variant yields different phenotypes) is also more directly addressed in [[dvir-2026-complex-genotype-phenotype-relationships-in|Dvir 2026]].
- **Mouse / human discordance** is acknowledged (e.g., Chd8+/− mild in mice, severe in humans) but framing for resolution is mostly "use iPSC organoids" without quantitative cross-system metrics — [[overviews/brain-organoid-fidelity]] addresses this gap.
- **Cell-type specificity** is not centrally framed — papers from 2022 onward ([[paulsen-2022-autism-genes-converge|Paulsen 2022]], [[fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence|Fernandez-Garcia 2026]]) push this dimension forward.

## Related Papers
- [[dvir-2026-complex-genotype-phenotype-relationships-in]] — *the divergence-direction mirror*. Six years later from a different lab (Hebrew U Jerusalem); same NDD gene set, asks the *opposite* question (same gene → different phenotypes). Read together for a complete picture of the NDD genotype-phenotype problem.
- [[fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence]] — empirical NDD convergence test (pooled CRISPR-KO + zebrafish drug rescue) directly extending this review's pathway-convergence thesis to systematic data.
- [[paulsen-2022-autism-genes-converge]] — autism-gene convergence in cortical organoids; the most direct empirical follow-up to the convergence thesis.
- [[amelan-2026-crispr-knockout-screens-reveal]] — CRISPR-KO screens for ASD risk genes.
- [[jourdon-2023-modeling-idiopathic-autism]] — idiopathic autism iPSC modeling.
- [[jin-2020-in-vivo-perturb-seq]] — *in vivo* Perturb-seq for autism risk genes (contemporary single-cell + perturbation approach).
- [[overviews/convergent-regulation-across-systems]] — overview directly elaborating this convergence framework.
- [[overviews/brain-organoid-fidelity]] — addresses the iPSC/organoid model-fidelity caveat of the review's iPSC-based evidence.
- Single-gene NDD models populating the pathway evidence: [[de-jong-2021-cortical-overgrowth-preclinical]], [[villa-2022-chd8-haploinsufficiency]], [[morelli-2022-mecp2-related-pathways-cortical]], [[martinscosta-2024-arid1b-controls-transcriptional]], [[mato-blanco-2025-early-developmental-origins]], [[schafer-2019-pathological-priming-causes]].
