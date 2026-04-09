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
