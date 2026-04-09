---
title: "NeMO Analytics: a compendium of transcriptomic data for the exploration of neocortical development"
authors: Shreyash Sonthalia, Brian Herb, et al., Seth A. Ament, Carlo Colantuoni
year: 2026
doi: 10.1038/s41593-026-02204-4
source: sonthalia-2026-nemo-analytics-compendium.md
category: brain-development
tags: [neocortex, multi-study, matrix-decomposition, oRG, primate-specific, organoid-benchmark, NeMO]
---

## Summary
Compiles ~200 neocortical development studies; joint matrix decomposition across mouse/macaque/human identifies conserved neurogenesis programs and a primate-specific oRG program. Organoid benchmark shows broad recapitulation but missing layer-specific maturation programs. Web tool at nemoanalytics.org.

## Key Contributions
- ~200-study compendium enables joint cross-species transcriptome decomposition
- Primate-specific oRG program identified (absent in rodent gliogenic precursors)
- Layer-specific excitatory neuron maturation is protracted and dissociated from early TF specification
- Organoids lack layer-specific neuronal maturation programs despite broad development recapitulation

## Methods & Architecture
Multi-study data aggregation; joint NMF-based matrix decomposition; cross-species/in vivo vs organoid comparison.

## Results
- Conserved neurogenesis transcriptome dynamics across three species
- Layer-specific signatures emerge late; TFs expressed early (timing dissociation)
- Organoid deficit: missing layer-specific maturation programs

## Limitations
Batch effects from heterogeneous datasets; decomposition assumptions.

## Related Papers
- [[brain-development/herring-2022-human-prefrontal-cortex-gene]] — PFC developmental atlas
- [[brain-development/gordon-2021-long-term-maturation-of]] — long-term organoid maturation
