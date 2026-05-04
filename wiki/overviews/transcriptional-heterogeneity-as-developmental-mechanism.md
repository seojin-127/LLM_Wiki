---
title: "Transcriptional Heterogeneity in Neural Progenitors as a Developmental Mechanism"
type: overview
created: 2026-05-03
modified: 2026-05-04
category: overviews
tags: [stochastic-decoder, NPC, radial-glia, oRG, lineage-potential, fate-commitment, critical-window, NDD, heterogeneity, cell-cell-communication, sampling-step]
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

본 overview는 neural progenitor cell (NPC)의 transcriptional heterogeneity를 *fate-driving mechanism*으로 다룬다. 여기서 heterogeneity는 두 source를 *모두* 포함한다 — cell type, developmental time, spatial position, 유전적 배경에 의해 결정되는 *deterministic* 측면, 그리고 transcriptional bursting과 fate-commitment sampling에서 비롯되는 *stochastic* 측면. 두 source 모두 lineage potential을 만들고 fate를 specify하며 neurodevelopmental disorder (NDD) vulnerability의 substrate가 된다.

자매 overview [[overviews/cell-identity-programs-and-trajectories]]는 *동일한 cell-level heterogeneity를 다른 각도*에서 본다. 그쪽은 heterogeneity의 *structure*와 그것을 추출하는 *방법론적 lineage* (PCA → NMF → joint decomposition → foundation-model embedding)를 다루며, heterogeneity를 추출 대상 신호로 취급한다. 본 overview는 그 heterogeneity가 *발달의 mechanism으로 어떻게 작동하는가*에 초점을 둔다. 두 wiki는 같은 phenomenon의 *방법론 측면*과 *생물학 측면*에 해당하며, scope가 strict하게 분할되지 않고 자연스럽게 겹친다.

### 분석 도구로서의 drift-diffusion lens

세포 상태의 시간적 진화를 *분해해서* 이해하고 싶을 때, stochastic differential equation 형태가 유용한 lens를 제공한다. Waddington epigenetic landscape의 수학적 실현이자, 본 wiki의 단일세포 trajectory 방법론들 — [[single-cell-dl/setty-2019-characterization-of-cell-fate|Palantir]], [[single-cell-dl/lange-2022-cellrank-for-directed-single|CellRank]], [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna|Cell2fate]], [[single-cell-dl/maddu-2026-learning-biophysical-models-of|PFM]], [[single-cell-dl/he-2026-squidiff-predicting-cellular-development|Squidiff]] — 이 명시적으로 사용하는 framework이다.

$$dX_t = \underbrace{\mu(X, t)\,dt}_{\text{drift = deterministic 끌림}} + \underbrace{\sigma(X, t)\,dW_t}_{\text{diffusion = stochastic fluctuation}}$$

이 분해는 *literature를 audit*할 때 강력하다 — 어떤 heterogeneity 증거가 drift (cell type × time × position의 결정론적 차이)에 속하고, 어떤 증거가 diffusion (isogenic system 내 같은 cell type · time · position에서도 남는 잔여 분산)에 속하는지 명시적으로 분리할 수 있게 해준다. 그러나 이는 *내부 분석 도구*이며 wiki scope의 strict 분할이 아니다 — 본 overview는 양쪽 모두를 다룬다.

이 framing은 mathematical idealization이며, NPC의 dynamics가 실제로 Langevin equation을 만족한다는 주장은 아니다.

### "Developmental noise"라는 용어에 대하여

해당 분야 literature는 heterogeneity의 *stochastic 성분*을 일반적으로 *developmental noise*라고 부른다. 이 용어는 historical accident이며, 일상적 의미의 "noise"(측정 오차, 무의미한 잡음)와는 다른 것을 가리킨다. 더 정확한 description은 다음과 같다.

> 세포의 transcriptional state가 결정론적이지 않고 *확률적으로* 동작한다는 사실 자체. 잡음이 아니라 mechanism이다.

[[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir et al. 2026]]은 이 stochastic variation을 NDD phenotype 변동을 설명하는 네 layer 중 *하나*(variant 자체, 다른 genetic element, environment에 이어 네 번째)로 명시적으로 framing했다. 일란성 쌍둥이가 동일한 NDD pathogenic variant를 가져도 phenotype이 갈리는 분자적 floor가 이 layer에서 발생한다. 다만 NDD heterogeneity의 *전부*가 stochastic decoder에서 오는 것은 아니며, *deterministic* layer (앞의 세 가지 — cell type-specific 반응, modifier gene, areal context 등) 또한 본 overview의 다루는 범위에 포함된다.

### 본 overview의 구조

- **Part I** — Heterogeneity as mechanism, not measurement noise
- **Part II** — Human-amplified case: oRG / basal radial glia and lineage potential
- **Part III** — RG subtypes drive spatial patterning and functional specification
- **Part IV** — Cross-cell-type variability: glia–neuron communication
- **Part V** — Critical windows: when heterogeneity gets locked in
- **Part VI** — NDD vulnerability *through* heterogeneity
- **Part VII** — How heterogeneity is measured

Closing에서는 본 overview의 내용이 [[overviews/convergence-heterogeneity-cascade-frame|cascade frame overview]]의 어디에 위치하는지 정리한다.

---

# Part I — Heterogeneity as Mechanism, Not Measurement Noise

## 1. The thesis

NPC는 fate commitment 시점에 안정적인 discrete identity state를 점유하지 않는다. 대신 dynamic하고 transient한 heterogeneous transcriptional state를 점유하며, *commitment 시점에 세포가 어떤 state에 있는가*는 그 세포가 어떤 cell type이 되는지, 어떤 areal identity를 획득하는지, 어떤 회로에 wiring되는지를 결정하는 비-trivial한 요인이다. 동일한 starting material과 동일한 외부 신호 아래에서도, 결과 세포의 정체성은 분포로 표현되어야 하며 단일 점값으로 표현될 수 없다.

이는 "noise = 측정 오차"라는 기본 framing의 정반대 입장이다. 본 overview의 thesis는 *variability 자체가 신호*라는 것이며, 발달 program이 그 variability를 *읽어내는* 방식이라는 것이다.

## 2. Why noise is biologically necessary, not accidental

진화가 이 stochasticity를 *유지*한다는 사실 자체가 mechanism의 증거이다. 만약 단순한 오차였다면 selection이 이를 최소화했을 것이다. 두 가지 실증적 논거를 들 수 있다.

- **Lineage diversification에는 stochastic divergence가 요구된다.** 완벽히 동기화되고 균질화된 progenitor 인구는 단일 fate만을 산출한다. Cortex는 작은 progenitor type 집합으로부터 수 주 안에 ~30개의 cell class를 생성해야 하며, progenitor 수준의 heterogeneity는 작은 starting state 집합이 훨씬 큰 output 집합을 만들 수 있게 하는 mechanism 중 하나이다.
- **Lineage *potential*의 확장(특히 primate에서)은 tolerated heterogeneity에 의존한다.** Rodent의 apical RG → IP → neuron 축은 비교적 제약적이지만, human에서는 outer subventricular zone (OSVZ)에 위치한 **outer radial glia (oRG / basal radial glia)**가 같은 축을 augment한다. 이들 progenitor pool은 더 넓은 state-to-state fluctuation을 tolerate하며 더 다양한 output을 산출한다 (Part II).

[[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir 2026]]은 이를 NDD phenotype 변동의 *fourth layer*로 framing하면서, 동시에 *경험적으로 가장 다루기 어려운* layer라고 명시한다. Stochastic variance를 deterministic variance로부터 분리하기 위해서는 isogenic system이 필요하기 때문이다.

## 3. 자매 overview와의 관계

[[overviews/cell-identity-programs-and-trajectories]]와 본 overview는 *동일한 cell-level heterogeneity*를 다루지만 다른 각도에서 본다.

- **자매 overview** = *방법론 lineage*. Heterogeneity의 안정적이고 재현 가능한 *구조*를 추출하는 도구가 어떻게 진화해왔는가 (PCA → WGCNA → NMF / cNMF → joint decomposition → VAE latent → foundation-model embedding). Heterogeneity는 *추출 대상 신호*.
- **본 overview** = *biological mechanism*. 그 heterogeneity가 발달 과정에서 *무엇을 하는가*. Lineage potential을 어떻게 만들고, fate specification에 어떻게 기여하며, NDD vulnerability를 어떻게 driving하는가.

두 wiki는 도구를 부분적으로 공유한다 (CellRank, GRN inference, lineage tracing 모두 양쪽에서 등장). 다만 같은 도구로 *다른 질문*에 답한다 — 자매 wiki는 "이 데이터에서 어떤 program structure가 추출되는가", 본 wiki는 "그 program structure의 변동이 fate / 질병에 어떻게 매핑되는가". Drift-diffusion 분해는 *양쪽 모두에서* 사용 가능한 분석 도구이며, 어느 한 wiki에 귀속되지 않는다.

---

# Part II — The Human-Amplified Case: oRG / bRG and Lineage Potential

## 4. Why oRG matters for this thesis

Outer radial glia (oRG, 동의어 basal radial glia / bRG)는 OSVZ에 위치한 progenitor로, primate와 human에서 rodent 대비 대규모로 확장되어 있다. Human cortex가 mouse cortex보다 upper-layer neuron이 훨씬 많고 측면 neurogenic territory가 훨씬 넓은 주된 cell-biological 이유이다.

Heterogeneity thesis 관점에서 oRG가 중요한 이유는 세 가지이다.

- Apical RG보다 commitment 이전에 훨씬 많이 분열한다. 따라서 한 progenitor가 sampling하는 *transient transcriptional state space*가 더 크다.
- Apical RG를 ventricular niche에 anchor하는 cell-cell contact이 oRG에는 없다. 따라서 gene expression이 더 자유롭게 fluctuate한다.
- Human-specific *cis*-regulatory program ([[brain-development/liu-2025-human-specific-enhancer-fine|Liu 2025]])이 작용하는 substrate이며, 이 enhancer들은 NPC dynamics를 *tune*하지 fixed identity를 *impose*하지 않는다.

## 5. Wiki의 oRG / NPC heterogeneity 증거

[[brain-development/taverna-2014-cell-biology-of-neurogenesis|Taverna et al. 2014]]는 foundational한 cell-biology review로, ventricular zone과 subventricular zone의 구조, oRG의 식별, 그리고 oRG가 basal process를 유지한다는 cell-cycle 차이(apical RG는 분열 시 retract)를 정리한다. 본 review는 human progenitor 인구가 mouse 대비 *눈에 띄게 더 heterogeneous*하다고 명시하며, 이를 human cortical expansion의 cell-biological origin으로 framing한다.

[[brain-development/kanton-2019-organoid-single-cell-genomic|Kanton et al. 2019]] (Camp / Treutlein 연구실)는 cross-species 비교의 정초이다. Human, chimp, macaque organoid의 single-cell 분석은 **human-specific neuronal neoteny**를 보여준다 — human progenitor가 chimp 또는 macaque 등가물 대비 proliferative하고 transcriptionally fluctuating한 state에 유의하게 더 오래 머문다. "Neoteny" framing은 *heterogeneous state에 머무는 시간 자체*가 종-특이적 parameter라는 점을 함의한다.

[[brain-development/jain-2025-morphodynamics-human-early|Jain et al. 2025]]는 형태와 dynamic 차원을 추가한다. 초기 human development의 NPC는 static한 transcriptomic snapshot으로는 포착되지 않는 characteristic한 morphodynamics를 보이며, 세포가 빠른 timescale에서 이동하고 형태를 바꾸며 transcriptional state를 shift한다. 즉 single-cell data에서 관찰되는 "heterogeneity"의 일부는 *빠르게 움직이는 세포의 time-averaged view*이다.

[[brain-development/mansour-2018-in-vivo-model-of|Mansour et al. 2018]] (Gage 연구실)은 human cortical organoid를 rodent host brain에 transplant하여 vascularization과 synaptic integration을 동반한 발달을 보였다. Murine host에도 불구하고 human-specific NPC heterogeneity가 native timescale로 진행되는 in-vivo testbed를 제공한다.

[[brain-development/liu-2025-human-specific-enhancer-fine|Liu et al. 2025]]은 human-specific enhancer를 fine-mapping했다. 이들 중 다수가 RG / NPC 인구에 특이적으로 작용하며, 이는 regulatory genome에 *fixed identity를 impose하기보다 heterogeneity를 modulate하는* dedicated layer가 존재함을 시사한다. 관련하여 [[genomic-dl/zemke-2023-conserved-and-divergent-gene|Zemke et al. 2023]]은 human-specific *cis*-regulatory element의 ~80%가 transposable element 유래이지만 regulatory *syntax*는 rodent와 primate 사이에 보존되어 있음을 보였다. 즉, human-specific *modulation*이지 *invention*이 아니다.

## 6. Cell-biology corollary

oRG의 풍부함은 fate commitment에서 *latent space가 더 큰* 것의 cell-biological 등가물이다. 한 progenitor가 stochastic하게 explore하는 state territory가 primate에서 rodent보다 풍부하며, 이는 같은 progenitor pool이 더 넓은 neuronal repertoire를 산출할 수 있는 이유이자 동시에 human neurodevelopment가 genotype으로부터의 prediction이 본질적으로 더 어려운 이유이기도 하다 — sampling되는 latent space 자체가 더 크기 때문이다.

---

# Part III — RG Subtypes Drive Spatial Patterning and Functional Specification

## 7. Cell-type identity 너머의 spatial heterogeneity

[[brain-development/nano-2025-integrated-analysis-molecular|Nano et al. 2025]]와 [[brain-development/dibella-2021-molecular-logic-of-cellular|Di Bella et al. 2021]]은 동일한 핵심 주장을 한다. Cortical neurogenesis의 molecular logic은 *cell type만으로*는 설명되지 않는다는 것이다. 같은 nominal "RG"라도 다른 cortical position이나 다른 developmental time에 있을 때 다른 gene program이 작동하며, 그 program이 후손 neuron의 subtype을 bias한다.

Nano et al. 2025는 23개 human cortical dataset에서 ~500개의 reproducible co-expression meta-module을 추출하고, **FEZF2 + TSHZ3가 deep-layer specification의 driver**임을 chimeroid에서 검증했다. 같은 RG라도 neurogenic division 시점의 module activity profile에 따라 다른 layer-specific neuron을 산출한다는 것이며, *문제의 heterogeneity는 module activity 차원의 heterogeneity*임을 보여준다.

Di Bella et al. 2021은 progenitor state의 *temporal sequence*가 후손의 laminar identity를 결정함을 보였다. 각 neurogenesis "wave"는 구분 가능한 transcriptomic state의 progenitor에서 유래하며, 이는 canonical RG marker가 동일한 경우에도 그러하다.

## 8. Spatial transcriptomics의 geometric 차원

세 개의 spatially-resolved 연구가 이 그림을 강화한다.

[[brain-development/zeng-2023-single-cell-spatial-transcriptional|Zeng et al. 2023]]은 mouse cortex development에서 spatial context 안의 single-cell transcriptional state를 resolve했다. 같은 broad cell type이 다른 cortical coordinate에서 다른 program activity를 carry하며, 그 geometric variability는 fate에 informative하다.

[[brain-development/zhang-2025-pfc-single-cell-spatiotemporal|Zhang et al. 2025 (PFC)]]와 [[brain-development/zhang-2025-spatial-dynamics-brain-development|Zhang et al. 2025 (spatial dynamics)]]는 이를 human prefrontal cortex와 더 넓은 brain development로 확장한다. 일관된 패턴은 spatial position이 single-cell transcriptional variance의 substantial한 부분을 explain한다는 것이며, 그렇지 않을 경우 noise처럼 보일 변동의 일부가 실제로는 spatially-structured information임을 시사한다.

## 9. Areal identity가 더하는 fate heterogeneity

[[neuroscience/mato-blanco-2025-early-developmental-origins|Mato-Blanco et al. 2025]]은 anteroposterior / dorsoventral 좌표가 다른 *brain-organizer hub* 사이에서 risk gene dynamics가 어떻게 다른지 추적했다. 본 연구의 TF-depletion simulation은 동일한 TF perturbation이 어느 areal hub에서 발생했는가에 따라 상당히 다른 downstream consequence를 가짐을 보였다. 즉 areal identity 자체가 progenitor-level heterogeneity가 read되는 방식을 modulate하는 contextual layer이다.

## 10. Why this matters for fate specification

§7-9의 종합. 2026년의 "neural progenitor"는 단일 state로 다룰 수 없다. *position-, time-, module-activity-defined coordinate*이며, 다른 좌표의 progenitor는 cell-type label이 동일하더라도 측정 가능하게 다른 fate distribution을 가진다. Fate specification은 (cell-type identity × position × time × current module activity)의 integration이며, 각 axis의 heterogeneity가 곱해진다.

---

# Part IV — Cross-Cell-Type Variability: Glia–Neuron Communication

## 11. The glial layer of heterogeneity

NPC와 fate-commitment 연구는 일반적으로 neuron 중심이지만, glia (astrocyte, oligodendrocyte precursor cell (OPC), microglia)도 overlapping progenitor pool에서 산출되며 그들 자신의 발달 heterogeneity를 보인다. 더 중요한 점은 neuron과 glia가 발달 중 *상호 communicate*하며, 이 cross-cell-type communication 자체가 세포마다 heterogeneous하다는 것이다.

[[brain-development/wang-2025-molecular-cellular-dynamics|Wang et al. 2025]]는 wiki에서 OPC × GABAergic neuron communication을 가장 직접적으로 다룬 연구이다. 발달 중 OPC와 immature GABAergic interneuron 사이의 cell-cell interaction이 세포마다 상당히 다르다는 점을 기록한다. 모든 OPC가 동일한 신호를 받는 것이 아니며, 모든 GABAergic neuron이 동일한 신호를 보내는 것도 아니다. 그 variability는 patterned이지만 stochastic하다. 결과적으로 myelination timing, GABAergic maturation, 그리고 궁극적으로 E/I balance setpoint의 변동이 발생한다.

## 12. Glial maturation은 second-order timescale

[[brain-development/gordon-2021-long-term-maturation-of|Gordon et al. 2021]]은 long-term cortical-spheroid culture에서 neuron과 glia 양자가 식별 가능한 maturation milestone을 거치며, glial maturation이 neuronal maturation을 상당히 lag한다는 것을 보였다. 이는 neuron이 fate를 specifying하고 있는 *그 아래*에서 glial decoder context가 동적으로 변화하고 있음을 의미한다. Month 2에 commit한 NPC와 month 5에 commit한 NPC는 다른 glial environment를 보게 된다.

## 13. Glia as integrators of environmental signals

[[neuroscience/dony-2025-glucocorticoid-amplifies-inhibitory|Dony et al. 2025]]은 chronic glucocorticoid exposure(스트레스 신호)가 cortical organoid에서 PBX3를 통해 inhibitory neuron fate를 amplify함을 보였다. Environmental 신호가 transcriptional program을 통해 routing되며, amplification은 어느 세포가 receptive state에 있었는지에 의존한다.

[[neuroscience/tanabe-2025-role-of-immature-choroid|Tanabe et al. 2025]]는 immature choroid plexus (ChP)를 developmental signaling hub로 framing한다. ChP 자체의 state-heterogeneity가 downstream cortical maturation과 social-behavior critical period를 shape한다.

[[neuroscience/morelli-2022-mecp2-related-pathways-cortical|Morelli et al. 2022]] (DM1 organoid model)는 glutamatergic-neuron-specific dysregulation이 MECP2 pathway disturbance로 propagate함을 보였다. 동일한 nominal cell type 내에서도 insult 시점의 세포별 state에 따라 pathway perturbation의 정도가 달라진다.

## 14. The pattern

Glia-related heterogeneity는 spatial position과 temporal stage에 더해지는 *최소 세 번째* developmental noise 차원이다.

- 다른 OPC는 다른 neuronal 신호를 받는다 ([[brain-development/wang-2025-molecular-cellular-dynamics|Wang 2025]]).
- 다른 glial cohort는 다른 maturation context를 제공한다 ([[brain-development/gordon-2021-long-term-maturation-of|Gordon 2021]]).
- 다른 세포는 environmental 신호를 다른 rate / amplitude로 integrate한다 ([[neuroscience/dony-2025-glucocorticoid-amplifies-inhibitory|Dony 2025]], [[neuroscience/tanabe-2025-role-of-immature-choroid|Tanabe 2025]]).

NDD 연구에서 이는 중요하다. 대부분의 computational model은 *neuronal level*에서 작동하지만, neuronal phenotype은 *그 neuron이 발달한 glial context*에 의해 부분적으로 결정되며, 그 context는 stochastic이었기 때문이다.

---

# Part V — Critical Windows: When the Heterogeneity Gets Locked In

## 15. The "critical window" framing

영구적으로 존재하는 heterogeneity는 noise이다. *특정 발달 시점에 read out되는* heterogeneity가 mechanism이다. Dvir 2026의 framing은 이 distinction을 중심에 둔다. Progenitor state는 dynamic하고 stochastic이지만, **fate commitment 사건은 시간적으로 좁다** — 세포가 commitment boundary를 한 번 넘으면 그 boundary 직전의 state가 고정된다.

[[neuroscience/schafer-2019-pathological-priming-causes|Schafer et al. 2019]]는 wiki에서 이 메커니즘이 disrupt되는 가장 명확한 사례를 제공한다. Idiopathic-ASD iPSC-derived NSC에서 **late developmental gene network가 prematurely activate**된다 ("pathological priming"). Commitment boundary read-out이 precociously mature한 transcriptomic background에서 발생하게 되며, individual NSC가 prime되는 정도가 다르기 때문에 patient 간 heterochronicity가 발생한다.

[[brain-development/glass-2026-human-cortical-organoids-recapitulate|Glass et al. 2026]]은 organoid가 in-vivo cortex의 critical-window timing을 보존하는가에 대한 질문을 다룬다. Wiki의 모든 iPSC 기반 heterogeneity 연구가 암묵적으로 organoid clock의 calibration을 trust한다는 점에서 중요하다. 답은 부분적이다 — 일부 window는 recapitulate되지만 일부는 그렇지 않으며, 이는 organoid model로부터 추론할 수 있는 것에 주요한 함의를 가진다.

[[brain-development/herring-2022-human-prefrontal-cortex-gene|Herring et al. 2022]]는 human prefrontal cortex의 gene-expression dynamics를 충분한 temporal resolution으로 resolve하여 어느 gene의 발현이 어느 window에서 peak하는지 식별했다. Peak-window distribution 자체가 어느 fate decision이 어느 window에 time-windowed 되어 있는지에 informative하다.

## 16. Chromatin이 window를 set하고 transcription이 cross한다

[[brain-development/mannens-2025-chromatin-accessibility-during|Mannens et al. 2025]]와 [[brain-development/trevino-2020-chromatin-accessibility-forebrain|Trevino et al. 2020]]은 동일한 관찰을 한다. Chromatin accessibility의 변화가 fate commitment를 mark하는 transcriptional change에 *선행*한다는 것이다. Regulatory commitment는 chromatin level에서 고정되며, marker mRNA는 그 이후에 등장한다. 따라서 fate-commitment heterogeneity는 부분적으로 *epigenetic heterogeneity*이며, critical window에 어느 enhancer가 open되어 있는가가 세포의 transcriptional response 가능성을 정한다.

## 17. Intervention timing에 대한 함의

Critical window가 실재하고 heterogeneity가 boundary에서 고정된다면 다음과 같은 timing-dependent 결과가 따른다.

- **Pre-window intervention**은 entire heterogeneity distribution을 shift할 수 있다.
- **In-window intervention**은 아직 commit하지 않은 세포만 redirect할 수 있다.
- **Post-window intervention**은 이미 commit된 세포에 작용하며, 그 mechanism set은 훨씬 좁다 (synaptic plasticity, modulator tuning 등).

이는 [[neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence|Fernandez-Garcia 2026]]에서 convergent NDD drug effect가 zebrafish phenotype을 *post-mitotically* rescue할 수 있다는 발견과 일치하며, 동시에 그러한 rescue가 *life-long sustained intervention*이어야 함을 시사한다 (one-time identity correction이 아니다).

---

# Part VI — NDD Vulnerability *Through* Heterogeneity

본 part는 [[overviews/convergent-regulation-across-systems]]와 [[neuroscience/parenti-2020-neurodevelopmental-disorders-from-genetics-to|Parenti 2020]]의 convergence framing, 그리고 [[neuroscience/dvir-2026-complex-genotype-phenotype-relationships-in|Dvir 2026]]의 divergence framing 사이의 통합 지점이다.

### 시작하기 전에 — heterogeneity의 두 source 분리

NDD pathogenic variant가 *heterogeneous substrate*에 작용한다는 점은 본 part 전체의 framing이지만, 그 heterogeneity의 source는 두 종류로 분해된다 — drift-diffusion 분해를 적용하면 다음과 같이 audit된다.

- **Deterministic 측면 (drift context modifier)** — cell type, developmental window, spatial position, genetic background 등이 변이 효과를 *결정론적으로* modulate. Wiki에는 이쪽 증거가 풍부하다.
- **Stochastic 측면 (diffusion floor)** — isogenic system에서 동일한 cell type · time · position에 *조건부*했을 때에도 남는 잔여 분산. 일란성 쌍둥이 phenotype 불일치, isogenic clone 간 within-clone 분산 등이 직접적 측정 대상. Wiki에는 이쪽 증거가 *상대적으로 매우 적다* — 본 part 끝에서 literature gap으로 별도로 다룬다.

이하 §18-20의 example들은 *주로 deterministic 측면*을 보여주며, §21-23은 양쪽 모두에 적용 가능한 framing이다.

## 18. Pathogenic variant는 heterogeneous substrate에 작용한다 (deterministic 측면 위주)

핵심은 다음이다. NDD risk-gene KO는 균질한 substrate를 perturb하지 않는다. *이미 cell type / time / background 차원에서 heterogeneous한 system*을 perturb한다. 이 관점은 다음과 같은 puzzling observation들을 설명한다.

- **동일 변이, 다른 cell type, 다른 response (deterministic).** [[neuroscience/li-2023-single-cell-brain-organoid|Li et al. 2023]] (CHOOSE)는 mosaic cerebral organoid에서 36개 ASD risk gene의 pooled CRISPR을 수행했다. **Dorsal intermediate progenitor와 ventral progenitor가 차등적으로 vulnerable**하다. 동일한 gene KO라도 어떤 cell type에서 일어났는가에 따라 다른 outcome이 발생한다. 이는 cell-type identity라는 *결정론적 decoder context*의 효과이다.
- **동일 변이, 다른 individual, 다른 penetrance (mostly deterministic).** [[neuroscience/jourdon-2023-modeling-idiopathic-autism|Jourdon et al. 2023]] (idiopathic ASD father-son pair, n = 13)는 macrocephalic son과 normocephalic son이 *opposite한 E/I imbalance*를 보임을 보고했다. TF divergence가 두 subgroup을 가른다. 두 subgroup 사이의 *집단 평균 차이*는 결정론적 background effect이며, *그 안에서의 환자 간 분산* 일부만이 stochastic 후보로 남는다.
- **Genomic context가 expressivity를 modulate (deterministic).** [[neuroscience/paulsen-2022-autism-genes-converge|Paulsen et al. 2022]]은 KMT5B, ARID1B, CHD8의 동일 KO가 다른 organoid line에서 다른 magnitude의 asynchronous한 GABAergic / excitatory development를 산출함을 보였다. Genetic background가 *변이 효과의 결정론적 modifier*로 작용한다.

## 19. "Pathological priming"은 heterogeneity-amplification (혼합)

[[neuroscience/schafer-2019-pathological-priming-causes|Schafer 2019]]의 heterochronicity 발견은 heterogeneity framing에 직접 들어맞는다. Program activation의 *timing*을 disrupt하는 변이는 일부 세포를 critical-window boundary 너머로 일찍 push한다. 이전에 bounded되어 있던 heterogeneity가 amplify되며, 늦게 prime되어야 했던 세포가 일찍 prime된 세포의 state로 fate commitment에 도달한다. Phenotype이 heterogeneous한 이유는 underlying timing distribution이 더 넓어졌기 때문이다.

이 발견은 *deterministic + stochastic 혼합*에 해당한다. 변이가 timing distribution의 *shape*을 결정론적으로 변경하지만, 그 distribution 안에서 어느 세포가 어느 시점에 prime되는가에는 stochastic 성분이 남는다.

## 20. Pathway 차원의 convergence는 cell 차원의 heterogeneity를 *요구*한다

이 절은 [[overviews/convergent-regulation-across-systems]] 및 [[neuroscience/parenti-2020-neurodevelopmental-disorders-from-genetics-to|Parenti 2020]]와의 reconciliation 지점이다. **Pathway convergence (3-pathway thesis: mTOR + chromatin + synaptic)와 cell-level heterogeneity는 tension 관계가 아니다 — 같은 관찰의 두 측면이다.**

- Pathway state는 low-dimensional manifold이다.
- *어느* 세포가 주어진 pathway perturbation에 반응하는가는 perturbation 시점의 state에 의존한다.
- Chromatin regulator KO는 *해당 window에 그 regulator의 target gene을 transcribe하던 모든 세포*에 hit하며, 세포별 response amplitude는 세포가 heterogeneous state에 있었기 때문에 heterogeneous하다.
- Convergence는 *평균*의 property이다. Heterogeneity는 *분포 모양*의 property이다.

[[neuroscience/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence|Fernandez-Garcia 2026]]은 이 주장의 경험적 demonstration이다. 23개 NDD risk gene의 pooled CRISPR-KO에서 **convergence가 mature glutamatergic neuron에서 가장 강하다**. 그 gene들이 해당 cell type에서만 작용하기 때문이 아니라, *heterogeneity-amplification effect가 거기서 가장 legible하기 때문*이다. 다만 이 발견 또한 주로 *deterministic decoder의 cell-type-specificity*에 해당한다 — within-cell-type 분산의 stochastic-side 분리는 별도 측정이 필요하다 (§25 참조).

## 21. Heterogeneity-aware model이 deterministic model을 outperform할 이유

실용적 함의이다 — [[overviews/six-open-issues-perturbation-modelling]]와 [[overviews/perturbation-prediction-and-causal-inference]]에 관련된다.

- Deterministic model (input genotype → output phenotype)은 substrate가 균일함을 암묵적으로 가정한다.
- Heterogeneity-aware model (input genotype × stochastic state → distribution over phenotype)은 floor를 명시적으로 modeling한다.
- Loss function 또한 *distributional*(예: ground-truth phenotype distribution과의 Wasserstein distance)이 *point-wise*(예: mean phenotype RMSE) 보다 적합하다 ([[concepts/distributional-vs-point-prediction]]).

Phase 1 NDD-convergence 연구에서, 이는 cell-by-cell heterogeneity를 early analysis 단계에서 *averaging away하지 말고 retain*해야 한다는 주장으로 이어진다.

---

# Part VII — How Heterogeneity Is Measured

## 22. Lineage tracing과 resolved fate atlas

[[brain-development/keefe-2025-lineage-resolved-atlas-developing|Keefe et al. 2025]]는 single-cell resolution의 lineage-resolved atlas of developing brain을 구축하여, *어느 clone이 어느 state를 거쳐 final identity에 도달했는가*를 직접 readout 가능하게 했다. Heterogeneity thesis의 methodological gold standard에 해당한다 — 동일 starting clone이 heterogeneous한 progeny를 산출하며, trajectory variance가 이제 측정 가능하다.

[[brain-atlas/braun-2023-comprehensive-cell-atlas-first|Braun et al. 2023]] (first-trimester human atlas)은 heterogeneity가 benchmark되는 temporal scaffold를 제공한다. *기대되는* state distribution의 high-resolution reference 없이는 deviation이 정량화될 수 없다.

## 23. Fate inference와 dynamic state estimation

이 thesis와 가장 유관한 single-cell-dl 방법들은 다음과 같다.

- [[single-cell-dl/setty-2019-characterization-of-cell-fate|Palantir (Setty 2019)]] — pseudotime + probabilistic fate assignment. 모든 세포가 terminal fate에 대한 *분포*를 부여받으며, 분포의 너비 자체가 heterogeneity의 척도가 된다.
- [[single-cell-dl/lange-2022-cellrank-for-directed-single|CellRank (Lange 2022)]] — 위를 RNA-velocity-informed fate map으로 확장하며, 데이터에서 state-to-state transition의 검출을 가능하게 한다.
- [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna|Cell2fate (Aivazidis 2025)]] — Bayesian ODE linearization을 통해 noise-reduced된 RNA-velocity module을 추론하며, brain-development data에 특히 적합하다.
- [[single-cell-dl/klein-2025-mapping-cells-through-time|Klein 2025]] — 명시적인 uncertainty quantification을 동반한 cell-through-time mapping 방법.
- [[single-cell-dl/vinyard-2025-learning-cell-dynamics-with|Vinyard 2025]] — optimal-transport 기반 single-cell trajectory의 dynamic model.

## 24. GRN-derived program이 regulatory readout이 된다

[[brain-development/fleck-2023-inferring-perturbing-cell-fate|Fleck 2023]], [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction|Zenk 2024]], [[brain-development/ding-2026-dissecting-gene-regulatory-networks|Ding 2026]]은 모두 joint chromatin-and-expression data로부터 **gene regulatory network**를 추론한다. 동일한 nominal cell type의 세포들 사이 GRN activity의 분산이 가장 informative한 heterogeneity 척도 중 하나이다 — 표준 single-cell 분석이 사용하는 marker-gene-level signal의 *upstream*에 있는 regulatory commitment를 capture하기 때문이다. 이들 방법은 perturbation-prediction 작업으로의 자연스러운 bridge이기도 하다 ([[overviews/perturbation-prediction-and-causal-inference]] 참조).

## 25. The not-yet-solved measurement problem (stochastic-side literature gap)

위 방법들에도 불구하고, wiki에는 single-cell variance를 다음으로 명시적으로 partition한 paper가 *없다*.

- 결정론적 성분 (cell-type / position / time / genetic background)
- 환원 가능한 noise (technical / measurement)
- 환원 불가능한 biological stochastic (Dvir 2026이 명명한 floor)

이는 명백한 methodological gap이며, 동시에 본 overview의 *§18-20에서 인용한 NDD example들이 거의 전부 deterministic 측면만 isolate하고 있는 이유*이기도 하다. Bulk variance에 대한 decomposition (heritability, hLDSC)은 well-established이지만, *developmental-noise interpretability를 갖는 single-cell variance decomposition*은 아직 존재하지 않는다. NDD context에서 이를 isolate하려면 다음과 같은 측정이 필요하다.

- **Isogenic system의 within-clone variance** — 동일한 게놈, 동일한 niche, 동일한 timing에서도 남는 cell-by-cell 변동.
- **Monozygotic twin discordance** — 환경 통제까지 conditioning한 후 phenotype 분산.
- **Same-cell-type × same-developmental-window 내 perturbation response variance** — Fernandez-Garcia 2026 같은 pooled CRISPR 데이터에서 mean 대신 *within-cluster 분포*를 분석.

이 gap을 메우는 작업은 NDD heterogeneity 연구의 가장 결정적인 다음 단계 중 하나이며, perturbation 측 framing은 [[overviews/six-open-issues-perturbation-modelling]]에서 확인할 수 있다. 동일한 gap이 [[overviews/perturbation-prediction-and-causal-inference]]의 distributional prediction 논의와도 직결된다 — point prediction은 deterministic decoder만 modeling하지만, distributional prediction은 stochastic floor까지 명시적으로 학습한다.

---

# Closing — Heterogeneity in the Cascade and SDE Frames

본 overview의 내용은 자매 wiki와의 strict scope 분할이 아니라 *상보적 perspective*에 해당한다. 여러 frame에서 본 overview의 자리는 다음과 같다.

- **자매 wiki와의 분담** — [[overviews/cell-identity-programs-and-trajectories]]는 *방법론 lineage*를 다루고, 본 overview는 *biological mechanism*을 다룬다. 두 wiki 모두 deterministic decoder context와 stochastic decoder fluctuation을 *함께* 다룬다 — strict 분할은 없다.
- **SDE 분해의 lens** — drift $\mu(X, t)$는 cell-type/time/position의 결정론적 끌림이고, diffusion $\sigma(X, t)\,dW_t$는 그 주변의 stochastic fluctuation이다. 본 overview의 내용은 *drift 측면 (cell-type vulnerability, areal context, genomic background)*과 *diffusion 측면 (NPC critical-window sampling, isogenic 분산)* 양쪽을 모두 포함하지만, 각 example이 어느 쪽에 속하는지는 §18-20과 §22-25에서 명시했다.
- **[[overviews/convergence-heterogeneity-cascade-frame|Cascade frame]]과의 매핑** — *Bottleneck (3-pathway manifold)* = drift attractor의 위치 / 형태. *Decoder의 deterministic component* = cell-type × time × position의 결정론적 readout (drift modifier). *Decoder의 stochastic component* = diffusion. Convergence는 attractor 구조의 property이고, heterogeneity는 attractor 주변의 *분포 모양* (drift gradient + diffusion magnitude 양쪽)의 property이다.
- **NDD pathogenic variant의 modification target** — 대부분은 $\mu$를 shift시키며 (attractor 위치 변경, cell-type-specific 효과 modulation), 일부 chromatin-related 변이는 $\sigma$를 직접 변경한다 (heterogeneity floor 자체의 amplification 또는 dampening). Wiki literature 대부분은 $\mu$ 변경의 증거이며, $\sigma$ 변경의 isolated 측정은 §25의 literature gap이다.

본 overview가 가리키는 경험적 연구 방향은 다음 세 가지이다.

1. **Deterministic decoder와 stochastic decoder의 분리.** Single-cell 구조를 존중하는 variance decomposition method가 missing tool이다. Bulk-genetics analogue (heritability)는 well-established이지만 single-cell analogue는 그렇지 않다.
2. **Stochastic component가 가장 큰 cell type과 developmental window의 식별.** NDD vulnerability가 가장 집중되는 자리이며, intervention timing이 가장 중요한 자리이다.
3. **Heterogeneity를 prediction 끝까지 carry하는 pathway-perturbation model의 구축.** Distributional prediction ([[concepts/distributional-vs-point-prediction]])이 자연스러운 fit이며, $P(\text{phenotype} \mid \text{variant}, \text{cell-state})$를 학습하는 generative method가 그 방법론적 방향이다.

The thesis: NPC의 transcriptional heterogeneity는 cleanup해야 할 measurement 문제가 *아니라*, brain development를 가능하게 하는 substrate, human-amplified lineage potential의 source, 그리고 NDD phenotype unpredictability의 floor이다. 이를 정량화하는 작업이 single-cell + perturbation neuroscience의 다음 결정적 move 중 하나이다.
