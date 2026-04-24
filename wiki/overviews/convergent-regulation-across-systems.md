---
title: "Why Do Hundreds of Different Mutations Converge on the Same Phenotype?"
type: overview
created: 2026-04-24
category: overviews
tags: [convergence, attractor-state, ASD, drug-resistance, GRN, cell-state, Perturb-seq, CRISPR-screen, chromatin-remodeler, TF-hub, Waddington-landscape, perturbation]
papers:
  - drug-resistance/xu-2026-mapping-convergent-regulators-of
  - neuroscience/jin-2020-in-vivo-perturb-seq
  - neuroscience/paulsen-2022-autism-genes-converge
  - neuroscience/jourdon-2023-modeling-idiopathic-autism
  - neuroscience/amelan-2026-crispr-knockout-screens-reveal
  - neuroscience/dubuc-2026-linking-rare-variants-cell-type
  - neuroscience/morelli-2022-mecp2-related-pathways-cortical
  - neuroscience/martinscosta-2024-arid1b-controls-transcriptional
  - brain-development/fleck-2023-inferring-perturbing-cell-fate
  - brain-development/ding-2026-dissecting-gene-regulatory-networks
  - brain-development/dibella-2021-molecular-logic-of-cellular
  - single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of
  - single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses
  - single-cell-dl/kamimoto-2023-dissecting-cell-identity-via
  - single-cell-dl/nadig-2025-transcriptome-wide-analysis-of
  - single-cell-dl/setty-2019-characterization-of-cell-fate
  - single-cell-dl/lange-2022-cellrank-for-directed-single
  - genomic-dl/zinati-2024-groundgan-grn-guided
  - brain-atlas/gao-2025-continuous-cell-type-diversification
  - single-cell-foundation/szalata-2026-perturbert-learning-gene-co
---

## The Question

> "자폐스펙트럼 장애에서는 수백 개의 서로 다른 유전자에서 유전변이가 발생하는데, 왜 그 결과는 자폐스펙트럼 장애라는 하나의 표현형으로 귀결되는가? 유전적 원인은 수백 가지인데 임상적 결과는 유사하다면, 그 사이에 어떤 수렴의 논리가 있는 것인가?"

This question — why do many different genetic causes produce the same phenotypic outcome — is not unique to autism. It recurs across biology:

| System | Diverse inputs | Convergent output |
|--------|---------------|-------------------|
| **ASD** | >100 risk genes (CHD8, PTEN, ARID1B, KMT5B, ...) | Shared neurodevelopmental phenotype |
| **Melanoma drug resistance** | >140 resistance genes (NF2, MED12, NF1, SMARCE1, ...) | Shared dedifferentiated cell state |
| **Cancer in general** | Thousands of driver mutations | ~10 hallmarks of cancer |

This overview asks: **what does this wiki's evidence say about the mechanism of convergence?** And can we now study it experimentally?

---

# Part I — The Evidence: Convergence Is Real and Measurable

## 1. ASD: 35 genes → 14 modules

[[neuroscience/jin-2020-in-vivo-perturb-seq]] performed in vivo Perturb-seq, knocking out 35 ASD/neurodevelopmental risk genes one at a time in the mouse cortex and reading out single-cell transcriptomes.

```
35 ASD risk genes
  │
  ├─ span: chromatin remodelers, kinases, transcription factors,
  │        RNA-binding proteins, synaptic proteins
  │
  └─ transcriptional responses collapse into 14 gene modules
     shared across perturbations AND conserved in human ASD brain
```

Key finding: the 35 genes are not producing 35 independent effects. They are perturbing a **shared set of gene programs** — a much smaller number of modules that the transcriptome can occupy.

## 2. ASD: 3 chromatin remodelers → same E/I timing defect

[[neuroscience/paulsen-2022-autism-genes-converge]] knocked out three ASD genes in brain organoids:

```
CHD8  (chromatin remodeler, also mutated in colon cancer)
ARID1B (SWI/SNF complex, Coffin-Siris syndrome)
KMT5B  (histone methyltransferase)
  │
  └─→ All three converge on: asynchronous development of
      GABAergic interneurons and deep-layer excitatory neurons
```

Three genes with completely different molecular functions — one reads chromatin, one remodels it, one modifies histones — produce the **same timing defect** in the same cell types. But: phenotype expressivity varied by individual genomic background (gene × background interaction), meaning convergence operates at the program level while severity is modulated by context.

[[neuroscience/martinscosta-2024-arid1b-controls-transcriptional]] deepened the ARID1B story: haploinsufficiency reduces chromatin accessibility specifically at SATB2+ callosal neuron programs, impairing axon formation. This converges on the same corpus callosum defect seen in CHD8 haploinsufficiency ([[neuroscience/villa-2022-chd8-haploinsufficiency]]).

## 3. Idiopathic ASD: no single gene, same trajectory divergence

[[neuroscience/jourdon-2023-modeling-idiopathic-autism]] studied organoids from idiopathic ASD patients — no known single-gene cause. Even without a shared genetic variant:

```
Macrocephalic ASD:    excess excitatory neurons
Normocephalic ASD:    excess inhibitory neurons
  │
  └─ Both show E/I imbalance — but in opposite directions!
     Rare-variant ASD genes enriched in altered transcripts
     despite no individual carrying the same mutation
```

This is convergence at a higher level: different patients, different (unknown) genetic causes, but the **same type of disruption** (E/I balance) manifests. The convergent unit is not a gene or a pathway — it is a **developmental program**.

## 4. Melanoma: 140+ genes → one dedifferentiated state

[[drug-resistance/xu-2026-mapping-convergent-regulators-of]] applied PerturbFate to knock down >140 vemurafenib resistance-associated genes in melanoma cells:

```
NF2 KD   (Hippo pathway)        ─┐
MED12 KD (Mediator complex)      ─┤
SMARCE1 KD (SWI/SNF)            ─┤
NF1 KD   (MAPK pathway)         ─┼──→ Same dedifferentiated state
DUSP6 KD (MAPK phosphatase)     ─┤    (FOSL1+, KLF5+, RREB1+, SMAD3+)
KEAP1 KD (Nrf2 pathway)         ─┤
...24 resistant perturbations    ─┘
```

The multimodal readout (ATAC + nascent RNA + steady-state RNA) revealed that convergence happens at **three levels simultaneously**:
- Chromatin: shared accessible regions open across perturbations
- Nascent transcription: same TF programs activated
- Steady-state: same gene expression signature accumulates

## 5. Neural differentiation: 331 essential genes, shared phenotypes

[[neuroscience/amelan-2026-crispr-knockout-screens-reveal]] performed genome-wide CRISPR KO during mESC → neural differentiation:

```
~18,000 genes screened
  └─ 331 neural-differentiation-essential genes (NEGs)
     └─ enriched for known NDD genes
     └─ 8 of 32 tested produce neuroanatomical defects
        └─ half show microcephaly
```

PEDS1 (plasmalogen biosynthesis — no prior brain association) was validated as a recessive microcephaly gene. A metabolic enzyme, not a transcription factor or chromatin remodeler, yet it converges on the same macroscopic phenotype.

---

# Part II — Why Does Convergence Happen?

## 6. The attractor state model

The most parsimonious explanation across all these systems is that cell states are organized as **attractors** in a landscape:

```
Waddington landscape:

     Normal state              Disease/resistant state
      (attractor 1)              (attractor 2)
         /\                          /\
        /  \                        /  \
       /    \     energy barrier   /    \
  ────/──────\───────────────────/──────\────

  Hundreds of genes maintain the barrier.
  Perturbing ANY of them can lower it.
  Once the barrier is crossed, the cell rolls
  into the disease attractor regardless of
  which gene was perturbed.
```

This explains why:
- **Many genes → one phenotype**: each gene contributes to the barrier; removing any one can be enough
- **Same gene → different severity**: genetic background modulates the barrier height (Paulsen 2022)
- **Different mechanisms, same destination**: the attractor is defined by TF network topology, not by which upstream signal changed

## 7. The TF hub as convergence mechanism

Both melanoma and brain studies point to **TF hubs** as the molecular identity of the attractor:

| System | Convergent TF hub | Evidence |
|--------|-------------------|----------|
| Melanoma resistance | FOSL1, KLF5, RREB1, SMAD3 | PerturbFate: activated across 24/24 resistant perturbations |
| Melanoma differentiation | SOX10 | PerturbFate: loss of SOX10 activity drives dedifferentiation |
| Brain development | GLI3, NR2E1, ZNF219, ARX | [[brain-development/ding-2026-dissecting-gene-regulatory-networks]]: CRISPRi screen of 44 TFs |
| Brain organoid | Pando-inferred regulomes | [[brain-development/fleck-2023-inferring-perturbing-cell-fate]]: GLI3 required for cortical fate |
| ASD | E/I maturation program | Jin 2020: 14 gene modules across 35 genes |

The pattern: **upstream perturbations are diverse, but they all funnel through a small number of TF regulatory nodes**. These nodes define the attractor.

[[brain-development/ding-2026-dissecting-gene-regulatory-networks]] made this particularly explicit: CRISPRi knockdown of 44 different TFs in cortical development produced convergent effector genes that were enriched for ASD and intellectual disability risk variants. The convergence is not coincidental — it reflects the **hierarchical structure of gene regulatory networks**, where many upstream signals are integrated by a few master regulators.

## 8. Programs, not genes, are the unit of convergence

The [[overviews/cell-identity-programs-and-trajectories]] overview established that cell identity is defined by **gene programs** (coordinated modules of co-regulated genes), not individual marker genes. Convergence follows naturally from this:

```
Gene level:       hundreds of different perturbations
                         │
Program level:    a few shared gene programs disrupted
                         │
Phenotype level:  one clinical/cellular outcome
```

This hierarchy explains the professor's observation about PTEN and CHD8: they are in completely different molecular pathways, but both pathways feed into the same developmental programs (cell proliferation timing, E/I balance). The programs are the bottleneck — the narrow waist of the hourglass.

---

# Part III — Can We Now Study Convergence Experimentally?

## 9. Three generations of tools

| Generation | Technology | What it reveals about convergence | Limitations |
|-----------|-----------|----------------------------------|-------------|
| **1st** (2016-2022) | Perturb-seq (RNA only) | Which genes produce similar transcriptomic responses | Cannot see chromatin; mRNA reflects past + present; no temporal ordering |
| **2nd** (2022-2024) | Multiome (ATAC + RNA) | Chromatin vs expression decoupling | No nascent/pre-existing separation; droplet throughput limits |
| **3rd** (2026) | **PerturbFate** (ATAC + nascent + steady-state) | Full regulatory cascade per cell; temporal ordering within snapshot | Single cell line; in vitro only |

PerturbFate's multimodal readout is why it could identify the transiently reactivating state (chromatin open, transcription not yet following) — a convergence intermediate that was invisible to earlier tools.

## 10. Computational prediction of convergence

Computational models can extend experimental screens to untested perturbations:

| Model | What it predicts | Can it predict convergence? |
|-------|-----------------|---------------------------|
| [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] GEARS | Mean expression after gene KO | Partially — predicts similar outputs for GO-related genes, but cannot model attractor dynamics |
| [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] PerturbNet | Distribution of cell states | Better — distributional output can capture bimodal convergent/non-convergent outcomes |
| [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] CellOracle | TF KO effect on cell fate | Yes in principle — GRN structure explicitly models TF hubs through which convergence occurs |
| [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] TRADE | True effect size of perturbation | Enables fair comparison — without TRADE, you cannot tell if two perturbations truly converge or if you are comparing noise |

**The gap**: no computational model in this wiki can predict convergence **from gene identity alone**. GEARS and PerturbNet can predict individual perturbation outcomes, but cannot tell you whether two perturbations will converge on the same attractor state. This requires explicit modeling of the landscape topology — which none of them do.

---

# Part IV — The Unsolved Questions

## 11. The variant-level convergence gap

Gene-level KO shows convergence. But most disease-associated variants are **not full knockouts**:

```
What Perturb-seq/PerturbFate does:    gene X → completely off
What GWAS variants actually do:        gene X → 10-30% less expression
                                                in a specific cell type
                                                at a specific developmental window
```

Does convergence still hold for partial, context-specific perturbations? We don't know. [[neuroscience/dubuc-2026-linking-rare-variants-cell-type]] proposes a framework for linking rare variants to cell-type-specific effects, but the experimental data to test whether **partial loss-of-function variants still converge** do not exist in this wiki.

## 12. Cross-system conservation of convergence

Melanoma and ASD both show convergence, but through different TF hubs:

```
Melanoma:  → FOSL1, KLF5, RREB1, SMAD3
ASD/Brain: → E/I maturation programs, SOX10-like identity programs
```

Is there a **universal principle** of convergence? Or is each system's attractor landscape unique? The wiki has no cross-system comparison. A starting hypothesis: convergence happens whenever a cell-state landscape has **few deep attractors separated by shallow barriers** — a property that may be common in developmental and cancer systems.

## 13. Can convergence be therapeutically exploited?

PerturbFate demonstrated this in melanoma: instead of targeting individual resistance genes (which differ per patient), target the **convergent TF hub** (FOSL1 + KLF5 + RREB1 + SMAD3) → 3.1-fold resistance reduction across 24 diverse perturbations.

The brain equivalent would be:

```
Instead of:  targeting CHD8, or ARID1B, or KMT5B individually
Target:      the convergent E/I maturation program itself

But: we don't yet know the TF-level identity of this program
     in the brain with the same precision as in melanoma.
     PerturbFate-level multimodal data in brain organoids would be needed.
```

## 14. PerturbFate in the brain — the obvious next experiment

```
Current state:
  Jin 2020:     35 ASD genes × in vivo × RNA only → 14 modules
  Paulsen 2022: 3 ASD genes × organoid × RNA only → E/I timing
  Fleck 2023:   brain organoid × ATAC + RNA (no nascent separation) → regulome

What's missing:
  PerturbFate × brain organoid × 100+ ASD genes
  = ATAC + nascent RNA + steady-state RNA per cell
  = chromatin → TF → transcription cascade for each ASD gene
  = identify the convergent TF hub (brain equivalent of FOSL1/KLF5/RREB1/SMAD3)
  = test whether combinatorial TF modulation rescues the phenotype
```

This experiment would directly answer the professor's question: "what is the logic of convergence?" The logic would be spelled out as a TF regulatory network, anchored in chromatin accessibility, validated by nascent transcription dynamics, and testable by combinatorial perturbation.

---

## Summary

Convergence — many mutations, one phenotype — is not a mystery. It is a structural property of gene regulatory networks. The evidence from this wiki:

1. **Convergence is real**: 35 ASD genes → 14 modules (Jin); 3 ASD genes → same E/I defect (Paulsen); 140+ melanoma genes → same dedifferentiated state (PerturbFate)
2. **The mechanism is TF hubs**: diverse upstream perturbations funnel through a small number of master TFs that define cell-state attractors
3. **Programs, not genes, are the unit**: cell identity is a coordinated gene program; convergence happens because many genes feed into the same programs
4. **Multimodal readout reveals the cascade**: PerturbFate shows chromatin → nascent RNA → steady-state, exposing intermediate convergence states invisible to RNA-only methods
5. **Therapeutic implication**: target the convergent hub, not individual upstream genes — validated in melanoma (3.1× resistance reduction)
6. **The gap**: this has been done in melanoma but not yet in brain. PerturbFate × brain organoid × 100+ ASD genes is the experiment that would close this gap

The convergence question is no longer "does it happen?" — it is "what are the exact TF nodes, and can we modulate them?"

---

*Sources: [[drug-resistance/xu-2026-mapping-convergent-regulators-of]], [[neuroscience/jin-2020-in-vivo-perturb-seq]], [[neuroscience/paulsen-2022-autism-genes-converge]], [[neuroscience/jourdon-2023-modeling-idiopathic-autism]], [[neuroscience/amelan-2026-crispr-knockout-screens-reveal]], [[neuroscience/dubuc-2026-linking-rare-variants-cell-type]], [[neuroscience/morelli-2022-mecp2-related-pathways-cortical]], [[neuroscience/martinscosta-2024-arid1b-controls-transcriptional]], [[brain-development/fleck-2023-inferring-perturbing-cell-fate]], [[brain-development/ding-2026-dissecting-gene-regulatory-networks]], [[brain-development/dibella-2021-molecular-logic-of-cellular]], [[brain-atlas/gao-2025-continuous-cell-type-diversification]], [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]], [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]], [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]], [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]], [[single-cell-dl/setty-2019-characterization-of-cell-fate]], [[single-cell-dl/lange-2022-cellrank-for-directed-single]], [[genomic-dl/zinati-2024-groundgan-grn-guided]], [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]], [[overviews/cell-identity-programs-and-trajectories]], [[overviews/perturbation-prediction-and-causal-inference]]*
