# LLM Wiki — AI for Biology

Claude-maintained personal knowledge base for AI/biology research papers.

Inspired by [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
and [joonan30's biology implementation](https://gist.github.com/joonan30/cbce305684d079dbe9a3fbaefe4e3959).

## Quick Start

```bash
# 1. Add a paper
#    Copy PDF to papers/, then ask Claude:
"Add this paper to the wiki: papers/filename.pdf"

# 2. Query
"Compare DNA foundation model architectures"

# 3. Monitor new papers
python3 scripts/paper_monitor.py --days 7 --min-score 2

# 4. Browse
#    Open this folder as an Obsidian Vault
```

## Structure

```
CLAUDE.md        ← wiki rules (read this first)
index.md         ← full catalog
log.md           ← operation history
papers/          ← original PDFs
sources/         ← LLM-generated summaries
wiki/            ← 25 category folders
scripts/         ← paper_monitor.py + reports
interactives/    ← HTML visualizations
```

See `CLAUDE.md` for full schema and rules.
