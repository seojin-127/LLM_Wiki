---
title: "Consensus prediction of cell type labels in single-cell data with popV"
authors: Can Ergen, Galen Xing, Nir Yosef, et al.
year: 2024
doi: 10.1038/s41588-024-01993-3
source: ergen-2024-consensus-prediction-cell.md
category: single-cell-dl
tags: [annotation, label-transfer, ensemble, uncertainty, cell-ontology, popV]
---

## Summary
popV aggregates multiple cell type prediction methods via ontology-based voting, providing well-calibrated uncertainty scores for reference-to-query label transfer. Accurately annotates the majority of cells while flagging ambiguous populations for targeted manual review — reducing human annotation burden.

## Key Contributions
- Ensemble + ontology voting: outperforms individual methods
- Calibrated uncertainty scores: reliably identify hard-to-annotate populations
- Reduces manual review to <20% of cells (the ambiguous ones)

## Methods & Architecture
- Multiple classifiers (SCVI, KNN, SVM, etc.) + cell ontology-based voting scheme
- Benchmarked on multiple reference atlases (Tabula Sapiens, PBMC, etc.)

## Results
- High accuracy annotation; well-calibrated uncertainty
- Flags cell populations with low consensus for manual review

## Limitations
- Performance depends on reference atlas quality
- Computationally more expensive than single-method approaches

## Related Papers
- [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]] — HNOCA uses similar annotation pipeline (snapseed); popV is complementary
- [[single-cell-dl/wang-2024-scsemiprofiler-advancing-large]] — scSemiProfiler: complementary large-cohort profiling approach
