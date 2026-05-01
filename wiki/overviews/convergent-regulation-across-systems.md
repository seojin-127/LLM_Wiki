---
title: "Why Do Hundreds of Different Mutations Converge on the Same Phenotype?"
type: overview
created: 2026-04-24
updated: 2026-05-01
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
  - neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence
  - brain-development/fleck-2023-inferring-perturbing-cell-fate
  - brain-development/ding-2026-dissecting-gene-regulatory-networks
  - brain-development/dibella-2021-molecular-logic-of-cellular
  - single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of
  - single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses
  - single-cell-dl/kamimoto-2023-dissecting-cell-identity-via
  - single-cell-dl/nadig-2025-transcriptome-wide-analysis-of
  - single-cell-dl/setty-2019-characterization-of-cell-fate
  - single-cell-dl/lange-2022-cellrank-for-directed-single
  - single-cell-dl/maddu-2026-learning-biophysical-models-of
  - genomic-dl/zinati-2024-groundgan-grn-guided
  - brain-atlas/gao-2025-continuous-cell-type-diversification
  - single-cell-foundation/szalata-2026-perturbert-learning-gene-co
---

## 핵심 질문 세 가지

이 overview는 다음 세 가지 질문을 축으로 정리한다.

**Q1. 발달 trajectory × cell type × convergence dynamics**
Continuous developmental trajectory 위에서 cell type 수준의 NDD risk gene convergence가 어떻게 변하는가. Snapshot 비교가 아니라 continuous flow 안에서, 같은 KO가 시간에 따라 어떤 program으로 funnel되는지.

**Q2. Variant 종류별 convergence 차이**
Variant 종류 (LoF, missense, CNV, partial loss-of-function) 에 따라 convergence 양상이 다른가. 완전 KO와 partial perturbation이 같은 attractor로 수렴하는지, 다른 sub-attractor로 갈라지는지.

**Q3. Module → drug → phenotype chain**
발달 단계 및 cell type specific하게 수렴하는 module을 약물로 타겟하면 — (a) 전사체 수준의 병리적 signature를 reverse할 수 있는가, (b) 그 reverse가 실제 phenotype 개선으로 이어지는가.

확장 축: spatial 차원 및 glia/vasculature 상호작용을 더했을 때, microenvironment context 안에서 convergence가 어떻게 reshape되는지.

---

## The Question (background)

> "자폐스펙트럼 장애에서는 수백 개의 서로 다른 유전자에서 유전변이가 발생하는데, 왜 그 결과는 자폐스펙트럼 장애라는 하나의 표현형으로 귀결되는가? 유전적 원인은 수백 가지인데 임상적 결과는 유사하다면, 그 사이에 어떤 수렴의 논리가 있는 것인가?"

This question — why do many different genetic causes produce the same phenotypic outcome — is not unique to autism. It recurs across biology:

| System | Diverse inputs | Convergent output |
|--------|---------------|-------------------|
| **ASD/NDD** | >100 risk genes (CHD8, PTEN, ARID1B, KMT5B, ...) | Shared neurodevelopmental phenotype |
| **Melanoma drug resistance** | >140 resistance genes (NF2, MED12, NF1, SMARCE1, ...) | Shared dedifferentiated cell state |
| **Cancer in general** | Thousands of driver mutations | ~10 hallmarks of cancer |

This overview pulls together the wiki's evidence on convergence — what we observe, why it happens (TF hub funneling on a Waddington-like attractor landscape), how we measure it, and what remains open.

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

Key finding: 35 KOs collapse to a much smaller module count — the transcriptome's available repertoire of perturbation responses is far smaller than the perturbation diversity. Modules here are gene-level convergence summarized post-hoc into modules; the explicit Layer-A/B separation came later.

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

Three genes with completely different molecular functions — one reads chromatin, one remodels it, one modifies histones — produce the **same timing defect** in the same cell types. Phenotype expressivity varied by individual genomic background (gene × background interaction): convergence operates at the program level while severity is modulated by context.

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

Convergence at a higher level: different patients, different (unknown) genetic causes, but the **same type of disruption** (E/I balance) manifests. The convergent unit is not a gene or a pathway — it is a **developmental program**.

## 4. ASD chromatin regulators × 4 cell types: cell-type-specific convergence + mitochondrial surprise (Fernandez-Garcia 2026)

[[neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence]] performed pooled CRISPR-KO of **23 NDD risk genes (chromatin/regulatory class)** across **four cell-type contexts** (iNPC, immature/mature iGLUT, mature iGABA), 118k cells.

The paper measures convergence at two complementary levels:
- **Gene-level** (METAL meta-analysis with FDR-adjusted P_meta < 0.05 + Cochran Q P_Het > 0.05) — captures cases where multiple KOs perturb the *same effector gene in the same direction*. Borrowed from GWAS meta-analysis tooling, the dual significance + directional-consistency criterion is what distinguishes real convergence from shared variability.
- **Network-level** (BicMix sparse biclustering — a sparse latent factor model in the NMF family) — captures cases where multiple KOs perturb *different individual genes within the same latent module*. Useful when KOs hit different parts of a shared regulatory program.

Four findings tightly aligned with the convergence question:

**(a) Convergence is highly cell-type-specific**, strongest in **mature glutamatergic neurons**:
```
iNPC          ← weakest convergence; KO effects diffuse
immature iGLUT ← intermediate
mature iGLUT  ← STRONGEST convergence (Layer A and Layer B)
mature iGABA  ← intermediate
```
Even when convergent gene pools overlapped >50% between cell types, *direction of effect was not preserved* — the same gene could be convergently up in one cell type and convergently down in another. Cell type sets the *resolution* at which convergence is visible.

**(b) Pathway-level convergence in mature iGLUT** (post-hoc GSEA on Layer-A convergent genes): synaptic + epigenetic + **mitochondrial/OXPHOS** — the mitochondrial signature was unexpected given that all KOs were chromatin regulators. Validated experimentally (Seahorse OCR ↓, OXPHOS protein ↓, mitochondrial morphology altered in dendrite) — establishing that transcriptomic convergence translates to functional defect.

**(c) Convergence integrates with population genetics**: behavioral clustering of zebrafish mutants → behavioral sets → set-specific in vitro convergence → set-specific rare variant burden enrichment (Set 3 = SCZ-NS, Set 4 = ASD-LoF). Three independent layers (organism behavior, in vitro molecular, human population genetics) align on the same NDD subset partition.

**(d) Network-level (BicMix) reveals hierarchical sub-modules**: a parent factor capturing broad shared response across many KOs, with narrower sub-factors capturing convergence specific to functional sub-families (e.g., methyl gene family vs SWI/SNF family). This is direct experimental evidence that convergence has *layered structure* — a broad attractor with finer sub-attractors.

## 5. Melanoma: 140+ genes → one dedifferentiated state

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

The multimodal readout (ATAC + nascent RNA + steady-state RNA) revealed convergence at **three levels simultaneously**:
- Chromatin: shared accessible regions open across perturbations
- Nascent transcription: same TF programs activated
- Steady-state: same gene expression signature accumulates

## 6. Neural differentiation: 331 essential genes, shared phenotypes

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

## 7. The attractor state model

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
- **Cell-type specificity of convergence**: the landscape topology *is itself* cell-type-specific (Fernandez-Garcia 2026 — mature iGLUT has deeper, sharper attractors than iNPC)

## 8. The TF hub as convergence mechanism

Both melanoma and brain studies point to **TF hubs** as the molecular identity of the attractor — these are the molecular layer where converging upstream signals funnel:

| System | Convergent TF hub | Evidence |
|--------|-------------------|----------|
| Melanoma resistance | FOSL1, KLF5, RREB1, SMAD3 | PerturbFate: activated across 24/24 resistant perturbations |
| Melanoma differentiation | SOX10 | PerturbFate: loss of SOX10 activity drives dedifferentiation |
| Brain development | GLI3, NR2E1, ZNF219, ARX | [[brain-development/ding-2026-dissecting-gene-regulatory-networks]]: CRISPRi screen of 44 TFs |
| Brain organoid | Pando-inferred regulomes | [[brain-development/fleck-2023-inferring-perturbing-cell-fate]]: GLI3 required for cortical fate |
| ASD chromatin regulators | E/I + OXPHOS + synaptic programs (BicMix sub-modules) | Fernandez-Garcia 2026: hierarchical factor structure with parent broad + narrower sub-factors |

The pattern: **upstream perturbations are diverse, but they all funnel through a small number of TF regulatory nodes**. Network-level convergence measurements (e.g., shared latent factors across KOs) are the statistical signature of this funneling.

[[brain-development/ding-2026-dissecting-gene-regulatory-networks]] made this explicit: CRISPRi knockdown of 44 different TFs in cortical development produced convergent effector genes enriched for ASD and intellectual disability risk variants. The convergence reflects the **hierarchical structure of GRNs** — many upstream signals integrated by a few master regulators.

## 9. Programs, not genes, are the unit of convergence

The [[overviews/cell-identity-programs-and-trajectories]] overview established that cell identity is defined by **gene programs** (coordinated modules of co-regulated genes), not individual marker genes. Convergence follows naturally:

```
Gene level:       hundreds of different perturbations
                         │
Program level:    a few shared gene programs disrupted
                         │
Phenotype level:  one clinical/cellular outcome
```

This hierarchy explains why genes in completely different molecular pathways (e.g., PTEN signaling vs CHD8 chromatin remodeling) can converge: both feed into the same developmental programs (cell proliferation timing, E/I balance). **Programs are the bottleneck** — the narrow waist of the hourglass.

## 10. Hierarchical sub-modules within convergence

When sparse factor models like BicMix are applied to convergence data, they tend to produce a **parent factor + nested sub-factors** structure:

```
Parent factor:  broad gene set shared across many KOs
                (e.g., "common chromatin regulator response")
   │
   ├── Sub-factor 1:  narrower gene subset shared by KO subgroup
   │                  (e.g., methyl gene family — KDM6B, KMT5B, KMT2C)
   │                  ↳ enriched for SCZ-NS rare variants (Fernandez-Garcia 2026)
   │
   └── Sub-factor 2:  another narrower gene subset, different KO subgroup
                      (e.g., SWI/SNF family — ARID1B, CHD8, ASH1L, ...)
                      ↳ enriched for ASD-LoF rare variants
```

This structure is partly a property of the model (sparsity drives hierarchical decomposition) and partly biological (functional sub-families share more downstream effects than the broader gene class). The biological reading: a broad attractor can have functional-family-specific sub-attractors. This may explain why rare variant burden (SCZ-NS vs ASD-LoF) maps onto specific NDD subgroups despite all being chromatin regulators.

Relevant to Q2 — whether variant-type-specific convergence operates at parent level, sub-level, or both, remains open.

---

# Part III — How Do We Study Convergence Experimentally?

## 11. Generations of tools

| Generation | Technology | What it reveals about convergence | Limitations |
|-----------|-----------|----------------------------------|-------------|
| **1st** (2016–2022) | Perturb-seq (RNA only) | Gene-level convergence; module summaries | No chromatin; mRNA reflects past + present; no temporal ordering |
| **2nd** (2022–2024) | Multiome (ATAC + RNA) | Chromatin vs expression decoupling | No nascent/pre-existing separation |
| **2nd+** (2026) | **Pooled scCRISPR + 4 cell types + cross-validation across modalities** (Fernandez-Garcia 2026) | Layered (gene + network) convergence; cell-type stratification; in vivo + population-genetics integration | Single donor hiPSC; pseudobulk loses single-cell heterogeneity; no chromatin layer |
| **3rd** (2026) | **PerturbFate** (ATAC + nascent + steady-state) | Full regulatory cascade per cell; temporal ordering within snapshot | Single cell line; in vitro only |

PerturbFate's multimodal readout exposed the *intermediate* convergence states (chromatin open, transcription not yet following) invisible to RNA-only methods. Fernandez-Garcia 2026's contribution is *orthogonal*: not deeper modalities, but stronger *measurement framework* + multi-context replication.

## 12. Computational prediction of convergence

| Model | What it predicts | Can it predict convergence? |
|-------|-----------------|---------------------------|
| [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] GEARS | Mean expression after gene KO | Partially — GO graph captures functional similarity but no attractor dynamics |
| [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] PerturbNet | Distribution of cell states | Better — distributional output captures bimodal convergent vs non-convergent outcomes; supports missense via ESM |
| [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] CellOracle | TF KO effect on cell fate | Yes in principle — GRN structure explicitly models TF hubs through which convergence occurs |
| [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] TRADE | True effect size of perturbation | Enables fair comparison — without TRADE, distinguishing real convergence from shared noise is hard |
| [[single-cell-dl/maddu-2026-learning-biophysical-models-of]] PFM | Stochastic dynamics on continuous trajectory | Promising for Q1 — SDE drift `h(x)` defined in gene space allows OOD initial conditions (e.g., perturbed states); biophysical noise term captures fate decisions |

**The gap**: no model in the wiki predicts convergence *from gene identity alone* in a way that would replace experimental screens. GEARS/PerturbNet predict individual outcomes but not whether two perturbations will collapse onto the same attractor. PFM is the closest mechanistic candidate (it models the SDE on which attractors live), but it has not been applied to NDD perturbation data yet.

---

# Part IV — Unsolved Questions (and how today's questions map onto them)

## 13. Variant-level convergence (maps to Q2)

Gene-level KO shows convergence. But most disease-associated variants are not full knockouts:

```
What Perturb-seq/PerturbFate does:    gene X → completely off
What GWAS variants actually do:        gene X → 10–30% less expression
                                                in a specific cell type
                                                at a specific developmental window
```

**Open question**: Does convergence still hold for partial, context-specific perturbations? Variant-level resolution (LoF vs missense vs CNV vs eQTL) of convergence has not been measured experimentally at scale. Fernandez-Garcia 2026 hints at variant-class differences (Set 3 SCZ-NS vs Set 4 ASD-LoF) but only via post-hoc enrichment, not direct variant perturbation.

[[neuroscience/dubuc-2026-linking-rare-variants-cell-type]] proposes a framework, but the experimental data remain missing. **This is the experimental version of Q2.**

## 14. Trajectory dynamics of convergence (maps to Q1)

Snapshot studies (including Fernandez-Garcia 2026's 4 cell-type snapshots) cannot answer how convergence *unfolds* over continuous developmental time. Does the convergent attractor exist at every developmental stage? Does it deepen with maturation? Do early KOs and late KOs reach the same attractor or different ones?

The methods that can begin to answer this:
- Continuous-trajectory dynamics models like PFM ([[single-cell-dl/maddu-2026-learning-biophysical-models-of]]) or moscot ([[single-cell-dl/klein-2025-mapping-cells-through-time]])
- Long-time-course developmental atlas + perturbation (e.g., extending [[neuroscience/mato-blanco-2025-early-developmental-origins]] with perturbations)

**This is the dynamical version of Q1.**

## 15. Therapeutic exploitation of convergence (maps to Q3)

PerturbFate demonstrated this in melanoma: instead of targeting individual resistance genes (which differ per patient), target the **convergent TF hub** (FOSL1 + KLF5 + RREB1 + SMAD3) → 3.1× resistance reduction across 24 diverse perturbations.

The brain equivalent has begun in Fernandez-Garcia 2026's CMap-based drug screen: 10/11 drugs (selected to reverse the *transcriptomic* convergent signature) ameliorated at least one zebrafish behavioral phenotype, **post-mitotically** — reversing rather than preventing.

But the chain is incomplete:
```
(a) drug → transcriptomic signature reverse?  ← partially shown
(b) (a) → phenotype improvement?              ← shown for behaviors in zebrafish
(c) (b) → human clinical relevance?           ← unknown
(d) Which sub-module within the hierarchy?    ← unaddressed
```

The hierarchical convergence structure (§10) implies that drug selection should be *sub-module-specific* — different functional-family attractors (methyl vs remodeler) may respond to different drug classes. **This is the systematic version of Q3.**

## 16. Cross-system universality of convergence

Melanoma and ASD both show convergence, but through different TF hubs:

```
Melanoma:  → FOSL1, KLF5, RREB1, SMAD3
ASD/Brain: → E/I maturation + OXPHOS + synaptic programs
```

Is there a **universal principle** of convergence — e.g., "any cell-state landscape with few deep attractors and shallow barriers will exhibit convergence"? Or is each system's landscape topology fundamentally unique? The wiki has no cross-system comparison study.

## 17. Phase 2 — Spatial and microenvironmental convergence

All current convergence studies (including Fernandez-Garcia 2026) are in *isolated* cell systems — neurons in monolayer, organoids without vasculature, in vivo without spatial resolution. Open questions:
- Does convergence look different when neurons are embedded in their native spatial context (cortical layers, projections)?
- Do glial co-cultures (astrocytes, microglia) shift the convergent attractor?
- Does vasculature influence which sub-module within the hierarchy is dominant?

Spatial transcriptomics + perturbation, and organoid-microenvironment systems, are the experimental routes. None of the perturbation papers in this wiki currently address this.

---

## Synthesis

Convergence is not a mystery, but it has more structure than the original "many genes → one phenotype" framing suggested. Pulling together what the wiki now contains:

1. **Convergence is real**: 35 ASD genes → 14 modules (Jin 2020); 3 ASD genes → same E/I defect (Paulsen 2022); 23 NDD genes → cell-type-specific layered convergence (Fernandez-Garcia 2026); 140+ melanoma genes → same dedifferentiated state (Xu 2026).
2. **Convergence is measurable at complementary levels**: gene-level (same effector across KOs, via meta-analysis) and network-level (shared latent modules across KO subsets, via sparse factor models) — and the network-level structure can itself be hierarchical (broad parent + functional-family sub-modules).
3. **The mechanism is TF hubs + attractor topology**: diverse upstream perturbations funnel through a small number of master TFs that define cell-state attractors; the topology is itself cell-type-specific.
4. **Cell type sets the resolution at which convergence is visible**: mature glutamatergic neurons consistently show the strongest convergence in NDD datasets — likely because their attractor landscape is more sharply defined.
5. **Multimodal + multi-context measurement is needed**: no single technology suffices. Fernandez-Garcia 2026's strength is multi-context (4 cell types, in vitro + zebrafish + population genetics), PerturbFate's is multimodal (chromatin + nascent + steady-state). The two strengths haven't been combined yet.
6. **Therapeutic exploitation is feasible** but requires sub-module-specific targeting given the hierarchical structure.

The convergence question has matured from "does it happen?" to:

> **"At what hierarchy level (broad parent vs narrow sub-attractor), in what cell type, along what developmental trajectory, for what variant class — and can we modulate the responsible regulatory hub?"**

This precisely matches the three questions framed in the opening section. The frontier experiment — implicit across the wiki — is **PerturbFate × brain organoid × continuous trajectory × variant-resolved × spatial**. None of the papers currently combine all four axes; each addresses one or two. The gap defines the research direction.

---

*Sources: [[drug-resistance/xu-2026-mapping-convergent-regulators-of]], [[neuroscience/jin-2020-in-vivo-perturb-seq]], [[neuroscience/paulsen-2022-autism-genes-converge]], [[neuroscience/jourdon-2023-modeling-idiopathic-autism]], [[neuroscience/amelan-2026-crispr-knockout-screens-reveal]], [[neuroscience/dubuc-2026-linking-rare-variants-cell-type]], [[neuroscience/morelli-2022-mecp2-related-pathways-cortical]], [[neuroscience/martinscosta-2024-arid1b-controls-transcriptional]], [[neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence]], [[brain-development/fleck-2023-inferring-perturbing-cell-fate]], [[brain-development/ding-2026-dissecting-gene-regulatory-networks]], [[brain-development/dibella-2021-molecular-logic-of-cellular]], [[brain-atlas/gao-2025-continuous-cell-type-diversification]], [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]], [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]], [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]], [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]], [[single-cell-dl/setty-2019-characterization-of-cell-fate]], [[single-cell-dl/lange-2022-cellrank-for-directed-single]], [[single-cell-dl/maddu-2026-learning-biophysical-models-of]], [[genomic-dl/zinati-2024-groundgan-grn-guided]], [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]], [[overviews/cell-identity-programs-and-trajectories]], [[overviews/perturbation-prediction-and-causal-inference]]*
