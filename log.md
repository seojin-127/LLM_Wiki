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
