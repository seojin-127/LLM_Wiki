---
title: "Population-level integration of single-cell datasets enables multi-scale analysis across samples"
authors: De Donno, Carlo, Hediyeh-Zadeh, Soroor, Moinfar, Amir Ali, Wagenstetter, Marco, Zappia, Luke, Lotfollahi, Mohammad, Theis, Fabian J.
year: 2023
doi: 10.1038/s41592-023-02035-2
source: dedonno-2023-population-level-integration-of.md
category: single-cell-dl
tags: [scPoli, integration, prototype-loss, reference-mapping, sample-embedding, open-world, population-level]
---

## Summary

scPoli extends scVI-family conditional VAEs with (1) learned continuous condition (sample) embeddings replacing one-hot batch encodings and (2) a prototype loss that clusters cells near their cell-type centroid in latent space. The combination improves biological conservation by 5.06% over scANVI, enables open-world extension to novel cell types from labeled query data, and scales to 7.8M cells across 2,375 samples. Used in HNOCA (He et al. 2024) as the atlas integration tool.

## Key Contributions

- Sample/condition embeddings: learned continuous vectors per sample capturing both biological and technical variation; replace one-hot batch encodings
- Prototype loss: KL term pulling cell embeddings toward their class prototype → better biological signal conservation
- Open-world learner: novel cell types added as new prototypes from labeled query without retraining reference
- Scales to 7.8M cells / 2,375 samples (PBMC atlas); sample embeddings explain COVID-19 severity variation

## Methods & Architecture

Base CVAE (scVI-family). Condition embeddings: a learned d-dimensional vector per sample (trained jointly); captures batch + biology at sample resolution. Prototype loss: for each cell type, maintain prototype = mean embedding; add KL divergence term to ELBO encouraging cells to cluster near prototype. Open-world extension: labeled query adds new prototype vectors; reference encoder frozen. Unlabeled cells classified by nearest prototype distance.

## Results

- 5.06% improvement over scANVI on integration benchmark across 6 diverse datasets
- Better biological conservation than all compared methods (scVI, scANVI, Seurat v3, Symphony, SVM, MARS)
- Lung atlas: sample embeddings decompose technical vs. biological batch sources
- PBMC atlas (7.8M cells, 2,375 samples): COVID-19 severity variation captured in sample embeddings
- Adopted by HNOCA (He et al. 2024) as best integration method for organoid atlas

## Limitations

- Prototype loss benefit depends on annotation quality of training reference
- Open-world extension requires labeled query data for novel type discovery
- Very large atlas (>10M cells) may need distributed training

## Related Papers

- [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] — scVI: base architecture
- [[single-cell-dl/xu-2021-probabilistic-harmonization-and]] — scANVI: previous best labeled method; scPoli outperforms
- [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]] — scArches: reference mapping predecessor; scPoli adds open-world
- [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]] — MrVI: sample-level heterogeneity modeling; complementary
- [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]] — HNOCA: scPoli chosen as best integration for this organoid atlas
