# Operation Log

> Claude appends an entry here every time a paper is ingested or a major operation runs.

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
