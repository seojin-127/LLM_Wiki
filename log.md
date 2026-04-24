# Operation Log

> Claude appends an entry here every time a paper is ingested or a major operation runs.

---

### 2026-04-24 — Ingest single paper (#124)

- Roohani et al. (2023) — GEARS: GNN + knowledge graph for combinatorial perturbation prediction → `single-cell-dl`
  - Source: `sources/roohani-2023-predicting-transcriptional-outcomes-of.md`
  - Wiki: `wiki/single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of.md`
  - PDF: `papers/roohani-2023-predicting-transcriptional-outcomes-of.pdf`
- Yu et al. (2025) — PerturbNet: modular cINN for distributional perturbation prediction (chemical/genetic/missense) → `single-cell-dl`
  - Source: `sources/yu-2025-perturbnet-predicts-single-cell-responses.md`
  - Wiki: `wiki/single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses.md`
  - PDF: `papers/yu-2025-perturbnet-predicts-single-cell-responses.pdf`
- Concept pages created (2):
  1. VAE (Variational Autoencoder) → `wiki/concepts/variational-autoencoder.md`
  2. GNN (Graph Neural Network) → `wiki/concepts/graph-neural-network.md`
  3. Uncertainty Quantification → `wiki/concepts/uncertainty-quantification.md`
- Xu et al. (2026) — PerturbFate: multimodal CRISPRi screening for melanoma drug resistance → `drug-resistance`
  - Source: `sources/xu-2026-mapping-convergent-regulators-of.md`
  - Wiki: `wiki/drug-resistance/xu-2026-mapping-convergent-regulators-of.md`
  - PDF: `papers/xu-2026-mapping-convergent-regulators-of.pdf`

---

### 2026-04-11 — Ingest batch (perturbation/causal methods, papers 112-123)

- **Papers ingested** (12 편, Q1/Q2 overview 준비용):
  1. Kamimoto et al. (2023) — CellOracle: GRN + in silico TF perturbation → `single-cell-dl`
  2. Nadig, Replogle et al. (2025) — TRADE: transcriptome-wide impact for Perturb-seq → `single-cell-dl`
  3. Lange, Theis et al. (2022) — CellRank: directed Markov chain fate mapping → `single-cell-dl`
  4. Setty, Pe'er et al. (2019) — Palantir: probabilistic fate on diffusion map → `single-cell-dl`
  5. He, Azizi et al. (2026) — Squidiff: diffusion model for perturbation prediction → `single-cell-dl`
  6. Amelan, Shifman et al. (2026) — Genome-wide CRISPR KO for neural differentiation, PEDS1 → `neuroscience`
  7. Klein, Theis et al. (2025) — moscot: scalable multimodal optimal transport → `single-cell-dl`
  8. Vinyard, Pinello et al. (2025) — scDiffEq: neural SDE with state-dependent diffusion → `single-cell-dl`
  9. Alsulami, Tegner et al. (2026) — PrePR-CT: graph-prior GAT for cell-type drug response → `drug-resistance`
  10. Gorin, Pachter et al. (2025) — Monod: biophysical stochastic transcription models → `single-cell-dl`
  11. Di Bella, Arlotta et al. (2021) — Mouse cortex molecular logic atlas → `brain-development`
  12. Chen, Ma et al. (2022) — scDEAL: bulk→single-cell transfer learning for drug response → `drug-resistance`
- **Files created**: 12 PDFs in papers/ + 12 sources/ + 12 wiki/
- **Notes**: All from Downloads/. Total: 123 papers. Balance option (HIGH 7 + MEDIUM 5) from triage of 24 PDFs. Purpose: prepare for question-driven overview on "gene-level perturbation vs. variant interpretation" and "pattern-learning vs. causal structure" (co-expression, latent, GRN, perturbation). Skipped duplicates: s41586-022-05279-8 (=fleck-2023), s41586-025-09997-7 (=ding-2026), s44330-024-00015-2 (=liu-2024 NS-Forest).

---

## Format

```
### YYYY-MM-DD — Operation type
- **Paper**: Title (Year)
- **Authors**: ...
- **Category**: category-name
- **Files created**:
  - sources/filename.md
  - wiki/category/filename.md
- **Notes**: any relevant notes
```

---

### 2026-04-11 — Overview page created (brain organoid fidelity)

- **Title**: Brain Organoid Fidelity: What Organoids Get Right and What They Don't
- **File**: wiki/overviews/brain-organoid-fidelity.md
- **Papers synthesized**: 12편 (bhaduri-2020, he-2024 HNOCA, uzquiano-2022, sonthalia-2026, gordon-2021, herring-2022, kanton-2019, mansour-2018, revah-2022, cakir-2019, glass-2026, birtele-2025)
- **Content**: 6개 fidelity 층위 표, 스트레스 아티팩트 통합 분석, 공학적 해결책 비교, 연구 질문별 결정 트리

---

### 2026-04-11 — Overview page created

- **Title**: Single-Cell Integration Methods: A Comparative Overview
- **File**: wiki/overviews/single-cell-integration-methods.md
- **Papers synthesized**: 11편 (scVI, Harmony, scANVI, Seurat WNN, scArches, scIB, CellTypist, scPoli, multiDGD, MrVI, SCimilarity)
- **Content**: 4 paradigms, scIB benchmark table, decision framework, scVI lineage diagram, practical pipeline recommendation

---

### 2026-04-11 — Ingest batch (papers 101-111, single-cell tools)

- **Papers ingested** (all → `single-cell-dl`):
  1. Lopez, Regier, Cole, Jordan, Yosef (2018) — scVI → `single-cell-dl`
  2. Korsunsky, Millard, Fan, Raychaudhuri (2019) — Harmony → `single-cell-dl`
  3. Aran, Looney, Liu, Bhattacharya (2019) — SingleR → `single-cell-dl`
  4. Xu, Lopez, Mehlman, Yosef (2021) — scANVI → `single-cell-dl`
  5. Hao, Hao, Andersen-Nissen, Satija (2021) — Seurat v4 / WNN → `single-cell-dl`
  6. Lotfollahi, Luecken, Theis (2022) — scArches → `single-cell-dl`
  7. Luecken, Buttner, Theis (2022) — scIB benchmark → `single-cell-dl`
  8. Dominguez Conde, Xu, Teichmann (2022) — CellTypist → `single-cell-dl`
  9. De Donno, Lotfollahi, Theis (2023) — scPoli → `single-cell-dl`
  10. Liu, Scheuermann, Zhang (2024) — NS-Forest v4.0 → `single-cell-dl`
  11. Boyeau, Hong, Ergen, Yosef (2025) — MrVI → `single-cell-dl`
- **Files created**: 11 PDFs in papers/ + 11 sources/ + 11 wiki/single-cell-dl/
- **Notes**: All from Downloads/. Total: 111 papers. Core scVI-tools ecosystem (scVI→scANVI→scArches→scPoli→MrVI) now fully covered. Also added Harmony, SingleR, CellTypist, Seurat WNN, NS-Forest, and the definitive scIB benchmark paper.

---

### 2026-04-11 — Ingest batch (papers 96-100)

- **Papers ingested**:
  1. Antonopoulos & Collins (2026) — Zero-shot prediction of drug response via LEMBAS RNN + TF activity → `drug-resistance`
  2. Szalata, Bica, Schaar, Lotfollahi (2026) — PerturBERT: BERT on perturbation signatures → `single-cell-foundation`
  3. Caskey & Stoeckius (2026) — CellSweep: multinomial EM ambient RNA decontamination → `single-cell-dl`
  4. Melsted, Booeshaghi, Pachter (2026) — GPU-accelerated kallisto RNA-seq → `other`
  5. Ge, Guo, Wang, Ding, Zhang (2026) — scEvolver: continual learning cell annotation → `single-cell-dl`
- **Files created**:
  - papers/antonopoulos-2026-zero-shot-prediction-of-drug.pdf + sources/ + wiki/drug-resistance/
  - papers/szalata-2026-perturbert-learning-gene-co.pdf + sources/ + wiki/single-cell-foundation/
  - papers/caskey-2026-single-cell-genomics-decontamination.pdf + sources/ + wiki/single-cell-dl/
  - papers/melsted-2026-rna-seq-analysis-in-seconds.pdf + sources/ + wiki/other/
  - papers/ge-2026-prototype-based-continual-learning-for.pdf + sources/ + wiki/single-cell-dl/
- **Notes**: All 5 PDFs from Desktop/Paper/. Total: 100 papers. New category populated: drug-resistance (first paper). DOIs: 10.1371/journal.pcbi.1014100, ICLR 2026 workshop (no DOI), 10.64898/2026.03.04.709349, 10.64898/2026.03.04.709526, 10.64898/2026.03.05.709973.

---

### 2026-04-11 — Ingest (paper 95)

- **Paper**: Single-cell spatiotemporal dissection of the human maternal–fetal interface (2026)
- **Authors**: Cheng Wang, Yan Zhou, Yuejun Wang, ... Susan J. Fisher, Jingjing Li
- **Category**: reproductive-biology
- **Files created**:
  - papers/wang-2026-single-cell-spatiotemporal-dissection.pdf
  - sources/wang-2026-single-cell-spatiotemporal-dissection.md
  - wiki/reproductive-biology/wang-2026-single-cell-spatiotemporal-dissection.md
- **Notes**: Nature 2026, DOI 10.1038/s41586-026-10316-x. snRNA+ATAC 멀티오믹스(191K 핵) + Stereo-seq 공간 전사체(1.1M 세포). Toggle switch 모델, R0→R1→R2 endothelial state, GWAS 통합. Reproductive-biology 카테고리 첫 논문.

---

### 2026-04-10 — Ingest batch (papers 86-94, new uploads)

- hao-2024 (scFoundation) → single-cell-foundation | cui-2024 (scGPT) → single-cell-foundation
- chen-2025 (EpiAgent) → single-cell-foundation | avsec-2021 (Enformer) → genomic-dl
- yu-2026 (ChromBERT) → genomic-dl | dubuc-2026 (rare variants + autism + FM) → neuroscience
- nowakowski-2025 (brain dev Perspective) → other | klingler-2022 (cortical malformations review) → other
- ding-2026 (scGPT retinal protocol) → other
- Skipped (duplicates/errata/corrections): fleck dup, he-2024 dup ×2, kanton dup, mannens dup, erratum ×3, NRN news

---

### 2026-04-10 — Ingest batch (papers 82-95 of 100)

- uzquiano-2022 → brain-development | bhaduri-2020 → brain-development | wang-2025-molecular-cellular-dynamics → brain-development
- revah-2022 → brain-development | shi-2023 → brain-atlas | kronman-2024 → brain-atlas
- keefe-2025 → brain-development | deng-2024 → genomic-dl | fleck-2023 → brain-development
- glass-2026 → brain-development | amiri-2018 → brain-development | ekvall-2024 → other
- sumanaweera-2025 → statistics | brancati-2020 → other | maoz-2018 → other | ullah-2025 → other
- Skipped (pure wet biology / duplicates): kiecker-2001, mansour-2018 (dup), braun-2023 (dup), rallu-2002, jayaraman-2018

---

### 2026-04-10 — Ingest batch (papers 72-81 of 100)

- chen-2024-brain-cell-atlas → brain-atlas | foord-2025 → lrRNA | mato-blanco-2025 → neuroscience
- zhang-2025-pfc → brain-development | chen-2025-whole-cortex → brain-atlas | heimberg-2025 → single-cell-foundation
- domcke-2020 → brain-atlas

---

### 2026-04-10 — Ingest batch (papers 62-71 of 100)

- de-jong-2021 → neuroscience | zhang-2025-spatial → brain-development | birey-2017 → brain-development
- braun-2023 → brain-atlas | winter-2023 → brain-atlas | lancaster-2013 → other
- jin-2025 → aging | zhou-2023 → brain-atlas | fischer-2024-sctab → single-cell-dl
- yao-2023 → brain-atlas
- Fixed: pagliaro-2025 (wiki page + index entry added; source existed but was missing wiki/index)
- Skipped: 0912826566 (Kiecker-2001, Xenopus Wnt, pure wet), 2827885190 (Mansour dup), 3570684337 (Braun dup), 4008095624 (Rallu-2002, pure wet)

---

### 2026-04-10 — Ingest batch (papers 57-60 of 100)

- zeng-2023 → brain-development | ding-2026 → brain-development | zenk-2024 → brain-development
- van-velthoven-2025 → brain-atlas

---

### 2026-04-10 — Ingest batch (papers 37-56 of 100)

- pasca-2015 → brain-development | jain-2025 → brain-development | ergen-2024 → single-cell-dl
- gabriel-2021 → brain-development | zinati-2024 → genomic-dl | joglekar-2024 → lrRNA
- cao-2020 → brain-atlas | mannens-2025 → brain-development | giandomenico-2019 → brain-development
- lawrence-2024 → other | birtele-2025 → other | paulsen-2022 → neuroscience
- jourdon-2023 → neuroscience | villa-2022 → neuroscience
- Skipped/duplicates: 1004829149 (He-2025 publisher correction), 1799977537 (research highlight), 1881964893 (Mansour dup), 2311317948/3764047813 (He-2024 dups), 3974428323 (Kanton dup), 4102187095 (Mannens dup), 2621489392 (Fitzgerald correction), 1379048265 (Whalley research highlight)

---

### 2026-04-10 — Ingest batch (papers 22-36 of 100)

- he-2024 → brain-atlas | mansour-2018 → brain-development | gao-2025 → brain-atlas
- taverna-2014 → brain-development | tanabe-2025 → neuroscience | langlieb-2023 → brain-atlas
- zemke-2023 → genomic-dl | dony-2025 → neuroscience | li-2025-uda-seq → single-cell-dl
- li-2023-choose → neuroscience | schuster-2024-multidgd → single-cell-dl | nano-2025 → brain-development
- liu-2023-methylome → single-cell-methylation
- Skipped/duplicates: Kiecker-2001 (pure wet biology, Xenopus), Whalley-2021 (NRN research highlight), Mansour-2018-erratum (0957714383), He-2025 (publisher correction), Kanton-2019-dup (3974428323)

### 2026-04-10 — Ingest batch (papers 3-20 of 100)

- gordon-2021 → brain-development | herring-2022 → brain-development | corrigan-2025 → brain-atlas
- kaplan-2025 → brain-development | wang-2024 → single-cell-dl | steyn-2024 → brain-atlas
- aivazidis-2025 → single-cell-dl | sonthalia-2026 → brain-development | morelli-2022 → neuroscience
- schafer-2019 → neuroscience | trevino-2020 → brain-development | eichmuller-2022 → other
- liu-2025 → brain-development | martinscosta-2024 → neuroscience | adlakha-2023 → other
- cakir-2019 → brain-development | zhang-2023 → brain-atlas | kanton-2019 → brain-development

---

### 2026-04-09 — Ingest batch (papers 1-2 of 100)

- **Paper**: Evolution of neuronal cell classes and types in the vertebrate retina (2023)
  - **Authors**: Hahn, Monavarfeshani et al.
  - **Category**: brain-atlas
  - **Files**: sources/hahn-2023-evolution-of-neuronal-cell.md, wiki/brain-atlas/hahn-2023-evolution-of-neuronal-cell.md

- **Paper**: In vivo Perturb-Seq reveals neuronal and glial abnormalities associated with autism risk genes (2020)
  - **Authors**: Jin, Simmons et al.
  - **Category**: neuroscience
  - **Files**: sources/jin-2020-in-vivo-perturb-seq.md, wiki/neuroscience/jin-2020-in-vivo-perturb-seq.md

---

### 2026-04-09 — Setup & Configuration

- **Type**: Infrastructure setup
- **Actions**:
  - Synced schema with joonan30 gist (https://gist.github.com/joonan30/cbce305684d079dbe9a3fbaefe4e3959)
  - Added missing `single-cell-methylation` category (folder + CLAUDE.md + index.md)
  - Total categories: 26
- **PDF source confirmed**: `C:\Users\SAMSUNG\Documents\My EndNote Library.Data\PDF\` (EndNote library)
- **PDF extraction test** (Hahn-2023, Nature):
  - opendataloader-pdf: 구조 좋음 (markdown heading 지원), figure 노이즈 소량 있음
  - pypdf: 빠르고 텍스트 깔끔, markdown 구조 없음
  - **선택**: opendataloader-pdf primary + pypdf fallback
- **Environment**: Java 21 (OpenJDK Temurin), Python 3.14, opendataloader-pdf & pypdf 설치 확인
