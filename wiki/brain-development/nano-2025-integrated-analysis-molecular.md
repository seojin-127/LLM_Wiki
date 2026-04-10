---
title: "Integrated analysis of molecular atlases unveils modules driving developmental cell subtype specification in the human cortex"
authors: Patricia R. Nano, Elisa Fazzari, Aparna Bhaduri, et al.
year: 2025
doi: 10.1038/s41593-025-01933-2
source: nano-2025-integrated-analysis-molecular.md
category: brain-development
tags: [human-cortex, meta-analysis, gene-modules, neurogenesis, FEZF2, TSHZ3, chimeroid, deep-layer]
---

## Summary
Nano et al. performed parallel meta-analysis of 23 human cortical scRNA-seq datasets (7 developmental + 16 adult), generating 500+ gene co-expression meta-modules. Meta-module 20 (FEZF2+/TSHZ3) drives deep layer neuron specification: cortical chimeroid experiments confirm both TFs are required via distinct mechanisms (cell fate vs. transcriptional regulation).

## Key Contributions
- 500+ meta-modules from 23 datasets; dynamic developmental specificity around peak neurogenesis
- Meta-module 20 (FEZF2+/TSHZ3+): deep layer specification module linked to neurodevelopmental disorders
- Cortical chimeroid validation: FEZF2 and TSHZ3 both required but via distinct modalities
- Framework: meta-atlas → mechanism (scalable to other modules)

## Methods & Architecture
- WGCNA-based co-expression across 23 scRNA-seq datasets; 7 dev + 16 adult human cortex
- Cortical chimeroids: KO cells in mouse cortex for in vivo human cell validation

## Results
- FEZF2 KO: disrupts deep layer cell fate
- TSHZ3 KO: disrupts module 20 transcriptional program without fate change
- Both required for deep layer specification module activity

## Limitations
- Cross-dataset batch effects partially managed
- Chimeroid: mouse host environment may differ from human

## Related Papers
- [[brain-development/herring-2022-human-prefrontal-cortex-gene]] — human PFC developmental atlas (one of the 23 source datasets)
- [[brain-development/sonthalia-2026-nemo-analytics-compendium]] — NeMO Analytics: another large-scale multi-dataset meta-analysis
- [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]] — HNOCA: similar meta-atlas approach for organoids
