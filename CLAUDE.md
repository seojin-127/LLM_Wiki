# LLM Wiki — AI for Biology: Collaborator Guide

This is an LLM-maintained wiki of research papers in AI/deep learning for biology.
Claude reads this file automatically to understand the schema and rules.

---

## Project Overview

This wiki follows the LLM Wiki pattern: research PDFs are converted into structured
markdown, creating a searchable, interconnected knowledge base.

**Structure stats (update periodically)**
- Source summaries: 0
- Wiki pages: 0
- Categories: 25
- Interactive visualizations: 0

---

## Three-Layer Architecture

```
Original PDFs (papers/)
→ Source markdown (sources/)     [LLM-generated summaries with YAML frontmatter]
→ Wiki pages (wiki/{category}/)  [polished pages with wikilinks]
```

1. **papers/** — Original PDF files. Always copy, never symlink.
2. **sources/** — Claude-extracted summaries with YAML frontmatter.
3. **wiki/** — Final wiki pages with cross-linked `[[wikilinks]]`.

---

## Folder Structure

```
llm-wiki/
├── CLAUDE.md                  ← this file (schema & rules)
├── index.md                   ← page catalog (Claude maintains)
├── log.md                     ← operation log (Claude maintains)
├── scripts/
│   ├── paper_monitor.py       ← daily monitoring script
│   └── monitor_reports/       ← daily reports (monitor-YYYY-MM-DD.md)
├── papers/                    ← original PDFs
├── sources/                   ← LLM-generated summaries (1 per paper)
├── wiki/
│   ├── genomic-dl/
│   ├── single-cell-dl/
│   ├── single-cell-foundation/
│   ├── protein-ai/
│   ├── gwas/
│   ├── neuroscience/
│   ├── brain-development/
│   ├── brain-atlas/
│   ├── long-read/
│   ├── lrRNA/
│   ├── drug-resistance/
│   ├── methylation-ai/
│   ├── methylation/
│   ├── medical-llm/
│   ├── statistics/
│   ├── sex-differences-biology/
│   ├── reproductive-biology/
│   ├── meiosis/
│   ├── synapse-evolution/
│   ├── aging/
│   ├── organoid/
│   ├── concepts/
│   ├── overviews/             ← synthetic overview pages
│   └── other/
└── interactives/              ← HTML/CSS/JS visualizations
```

---

## Category Definitions

| Category | Contents |
|----------|----------|
| `genomic-dl` | DNA language models, variant effect prediction, regulatory genomics |
| `single-cell-dl` | scRNA-seq deep learning, cell type annotation |
| `single-cell-foundation` | Geneformer, scGPT, large-scale single-cell foundation models |
| `protein-ai` | Protein language models, structure prediction |
| `gwas` | GWAS, EWAS, rare variant testing, population genetics |
| `neuroscience` | ASD, schizophrenia, psychiatric genetics |
| `brain-development` | Normal brain development, cortical biology, neurogenesis |
| `brain-atlas` | Brain cell atlases, BICCN, spatial transcriptomics |
| `long-read` | PacBio, Oxford Nanopore sequencing methods |
| `lrRNA` | Long-read RNA-seq: Iso-seq, MAS-seq, ONT |
| `drug-resistance` | Cancer proteomics, drug resistance mechanisms |
| `methylation-ai` | Methylation **AI/DL models only** |
| `methylation` | General DNA methylation biology |
| `medical-llm` | Medical/clinical LLMs, NLP for EHR |
| `statistics` | Statistical methods (FDR, Bayesian, batch effects) |
| `sex-differences-biology` | Sex-specific genetic architecture, XWAS |
| `reproductive-biology` | Germ cell development, PGC, genomic imprinting |
| `meiosis` | Meiotic recombination, crossover mechanisms |
| `synapse-evolution` | Synaptic molecular evolution |
| `aging` | Longevity genetics, lifespan QTL |
| `organoid` | Non-brain organoids |
| `concepts` | General ML/DL concepts used across biology |
| `overviews` | Synthetic pages spanning multiple papers |
| `other` | Cross-topic, wet biology, reviews, benchmarks |

**Category rules:**
- Assign based on **method**, not just keywords (e.g., EWAS paper → `gwas`, not `methylation-ai`)
- `methylation-ai` = AI/DL models only, not every paper that mentions methylation
- Pure experimental wet biology → `other`
- When unsure → `other` (don't over-categorize)

---

## File Naming Convention

All three files (PDF, source, wiki page) share the **same stem**:

```
{lastname-year-first5words}.pdf
{lastname-year-first5words}.md   (in sources/)
{lastname-year-first5words}.md   (in wiki/{category}/)
```

Examples:
- `vaswani-2017-attention-is-all-you.pdf`
- `sources/vaswani-2017-attention-is-all-you.md`
- `wiki/concepts/vaswani-2017-attention-is-all-you.md`

---

## Source File Format (`sources/*.md`)

```yaml
---
title: "Exact paper title"
authors: Author1, Author2, Author3
year: 2024
doi: 10.xxxx/xxxxx
category: genomic-dl
pdf_path: papers/filename.pdf
pdf_filename: filename.pdf
source_collection: collection-name
---

## One-line Summary

## 1. Document Info
- Journal/Conference:
- Received/Published:

## 2. Key Contributions
(2-4 bullet points)

## 3. Methods & Architecture
(core technical approach)

## 4. Key Results & Benchmarks
(main findings with numbers)

## 5. Limitations & Future Work

## 6. Related Work
(papers cited or closely related)

## 7. Glossary
(domain-specific terms defined)
```

---

## Wiki Page Format (`wiki/{category}/*.md`)

```yaml
---
title: "Exact paper title"
authors: Author1, Author2, Author3
year: 2024
doi: 10.xxxx/xxxxx
source: source_filename.md
category: genomic-dl
tags: []
---

## Summary
(2-3 sentence overview)

## Key Contributions
(bullet points)

## Methods & Architecture
(technical approach, diagrams if helpful)

## Results
(key numbers and findings)

## Limitations

## Related Papers
- [[category/page-slug]] — reason for connection
- [[category/page-slug]] — reason for connection
```

---

## Claude's Operation Rules

### Ingest (Add a new paper)

When asked `"Add this paper: papers/filename.pdf"`:

1. Extract text from PDF using `opendataloader-pdf` (preferred) or `pypdf` (fallback)
2. Create `sources/{stem}.md` with full structured summary
3. Determine correct category from Category Definitions above
4. Create `wiki/{category}/{stem}.md` with wiki page
5. Add `[[wikilinks]]` to related existing pages
6. Update `index.md` — add entry under correct category
7. Append to `log.md` — date, paper title, category, files created
8. **Before creating**: check if DOI already exists to avoid duplicates

### Query (Answer questions)

- Read `index.md` first, then relevant wiki pages
- **Answer only from papers in this wiki** — do NOT use web search to fill gaps
- Every claim must be traceable to a specific paper in the wiki
- End response with: `Sources: [[category/page]], [[category/page]]`
- If the wiki lacks papers on the topic: say so explicitly and ask for PDFs

### Lint (Quality check)

When asked to lint:
- Find contradictions between pages
- Flag broken `[[wikilinks]]`
- Identify outdated information (check year vs. newer papers in wiki)
- Suggest merging duplicate content
- Report: list of issues with file:line references

---

## PDF Text Extraction

### Primary: opendataloader-pdf (best quality, requires Java)

```bash
export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"
python3 -c "
import opendataloader_pdf, tempfile, os, re, sys
pdf = sys.argv[1]
with tempfile.TemporaryDirectory() as d:
    opendataloader_pdf.convert(pdf, output_dir=d, format='markdown',
                               pages='1-15', image_output='off', quiet=True)
    stem = os.path.splitext(os.path.basename(pdf))[0]
    text = open(f'{d}/{stem}.md').read()
lines = [l for l in text.splitlines() if not re.match(r'!\[image \d+\]', l)]
print('\n'.join(lines)[:12000])
" "papers/filename.pdf"
```

### Fallback: pypdf (simple, no Java)

```bash
python3 -c "
import pypdf, sys
reader = pypdf.PdfReader(sys.argv[1])
text = ''
for page in reader.pages[:40]:
    t = page.extract_text()
    if t: text += t + '\n'
    if len(text) > 12000: break
print(text[:12000])
" "papers/filename.pdf"
```

**Install:**
```bash
pip3 install opendataloader-pdf pypdf
brew install openjdk  # for opendataloader-pdf
```

---

## Daily Workflow

### 1. Run paper monitor
```bash
python3 scripts/paper_monitor.py --days 7 --min-score 2
```

### 2. Review report
Open `scripts/monitor_reports/monitor-YYYY-MM-DD.md`:
- **Ready to collect** (score ≥4, OA PDF available) → add immediately
- **Manual review** (score ≥2, no OA or needs judgment) → decide

### 3. Add papers
```
Add this paper to the wiki: papers/filename.pdf
```

### 4. Query the wiki
```
Compare DNA foundation model architectures
What are the best methods for rare variant testing?
Summarize ASD genetics papers in this wiki
```

### 5. Save insights as overviews
After a synthesis answer:
```
Save this as an overview page
```
→ Saved to `wiki/overviews/`

### 6. Build interactive visualizations
```
Create an interactive visualization comparing genomic language model architectures
```
→ Saved to `interactives/{topic-name}/index.html`

---

## Browsing

### Obsidian (recommended)
- Open `llm-wiki/` as Obsidian Vault
- Use graph view, full-text search, `[[wikilink]]` navigation

### Claude Code
- Claude reads `CLAUDE.md` + `index.md` then finds relevant pages

---

## Key Lessons

1. **Papers-only principle** ⭐ Most important
   - All answers must be grounded in papers in this wiki
   - Never fill gaps with web search
   - If a topic has no papers: say so, ask for PDFs

2. **Always copy PDFs** — never symlink, always real files in `papers/`

3. **Overview pages are the most valuable** — synthetic knowledge compounds

4. **Don't over-categorize** — 25 categories is enough, use `other` liberally

5. **Check for duplicates before ingesting** — same DOI in multiple categories wastes space

6. **Human review is essential** — LLMs classify by keywords, not understanding
