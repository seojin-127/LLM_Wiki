---
title: "Benchmarking atlas-level data integration in single-cell genomics"
authors: Luecken, Malte D., Buttner, M., Chaichoompu, K., Danese, A., Interlandi, M., Mueller, M. F., Strobl, D. C., Zappia, L., Dugas, M., Colome-Tatche, M., Theis, Fabian J.
year: 2022
doi: 10.1038/s41592-021-01336-8
source: luecken-2022-benchmarking-atlas-level-data.md
category: single-cell-dl
tags: [benchmarking, integration, scIB, batch-correction, scVI, scANVI, Harmony, scATAC-seq, atlas]
---

## Summary

The scIB benchmark evaluates 68 method-preprocessing combinations across 13 atlas-level integration tasks (85 batches, >1.2M cells) using 14 metrics. Key findings: scANVI tops labeled-integration; Scanorama and scVI lead unsupervised RNA-seq; Harmony and LIGER best for scATAC-seq; HVG selection universally helps; z-score scaling prioritizes batch removal over biological conservation.

## Key Contributions

- scIB Python module: reusable benchmarking pipeline with 14 integration quality metrics
- 13 atlas-level tasks spanning nested batch effects, multiple protocols, and 1M+ cells
- Definitive ranking of 16 methods; guides tool selection for new projects
- Key preprocessing insight: HVG selection helps all methods; scaling hurts biological conservation

## Methods & Architecture

16 methods benchmarked: MNN, FastMNN, Seurat v3 (CCA+RPCA), scVI, scANVI, Scanorama, BBKNN, LIGER, Conos, SAUCIE, Harmony, ComBat, DESC, trVAE, scGen. Composite score = 0.4 × batch removal + 0.6 × biological conservation, using kBET, graph iLISI/cLISI, ASW, kNN connectivity, NMI, ARI, trajectory conservation, and cell cycle conservation.

## Results

- **RNA-seq, labels available**: scANVI > scGen > scVI
- **RNA-seq, unsupervised**: Scanorama ≈ scVI > Harmony
- **scATAC-seq**: Harmony > LIGER (peak space); LIGER better on window space
- **ComBat**: poor on atlas-level despite good simple benchmark performance
- **HVG**: universally improves all methods
- **Scaling**: improves batch correction but reduces biological signal conservation

## Limitations

- Static snapshot (2021); newer methods (scPoli, scArches, foundation models) not included
- scATAC-seq coverage less comprehensive than RNA-seq
- Ground truth annotation quality varies across tasks

## Related Papers

- [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] — scVI: top unsupervised RNA integration
- [[single-cell-dl/xu-2021-probabilistic-harmonization-and]] — scANVI: top labeled integration
- [[single-cell-dl/korsunsky-2019-fast-sensitive-and-accurate]] — Harmony: best scATAC-seq integration
- [[single-cell-dl/dedonno-2023-population-level-integration-of]] — scPoli: next-generation method outperforming scANVI
- [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]] — scArches: reference mapping extension evaluated here
