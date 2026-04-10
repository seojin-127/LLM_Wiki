---
title: "An integrated transcriptomic cell atlas of human neural organoids"
authors: Zhisong He, Leander Dony, Jonas Simon Fleck, et al.
year: 2024
doi: 10.1038/s41586-024-08172-8
source: he-2024-integrated-transcriptomic-cell-atlas.md
category: brain-atlas
tags: [organoid, atlas, scRNA-seq, integration, fidelity, disease-modeling]
---

## Summary
He et al. built the Human Neural Organoid Cell Atlas (HNOCA) by integrating 36 scRNA-seq datasets (1.77M cells, 26 protocols) from neural organoid studies. Mapping to primary developing brain references shows dorsal telencephalic cell types are well-covered while non-telencephalic regions are sparse. Cell stress is identified as a universal in vitro artifact that is separable from core neuronal identity.

## Key Contributions
- Largest integrated organoid atlas to date: 1.77M cells, 36 datasets, 26 protocols
- Systematic quantification of which brain regions can and cannot be generated with current protocols
- Cell stress (glycolytic signature) is universal in vitro artifact; core cell identity is preserved
- Disease modeling application: 11 neural disease datasets mapped onto HNOCA as control cohort

## Methods & Architecture
- 3-step integration: RSS projection → snapseed annotation → scPoli label-aware integration
- snapseed: hierarchical marker-based cell type annotation tool
- scPoli ranked best in integration benchmarks for these datasets
- Programmatic interface for browsing atlas and projecting new data

## Results
- Dorsal telencephalon (NPCs, excitatory neurons) best covered; cerebellar/spinal cord largely absent
- Transcriptomic fidelity quantified per cell type across protocols
- Disease models (ASD, schizophrenia) annotated via HNOCA; protocol-relevant DE genes identified
- Metabolic stress signature distinguishes in vitro from in vivo neurons regardless of protocol

## Limitations
- Biased toward telencephalic protocols; non-telencephalic brain regions underrepresented
- No spatial resolution; purely transcriptomic
- Cross-lab batch effects partially unresolved even after integration

## Related Papers
- [[brain-atlas/corrigan-2025-conservation-and-alteration]] — complementary cross-species cell atlas approach
- [[brain-development/gordon-2021-long-term-maturation-of]] — organoid maturation trajectory relevant to atlas fidelity
- [[brain-development/sonthalia-2026-nemo-analytics-compendium]] — another large-scale organoid compendium with similar atlas-vs-primary comparisons
- [[brain-development/kanton-2019-organoid-single-cell-genomic]] — original cross-species organoid scRNA-seq (3 species)
