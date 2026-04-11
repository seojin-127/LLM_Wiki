---
title: "Single-cell genomics decontamination using CellSweep"
authors: Caskey, Conor W., Stoeckius, Marlon
year: 2026
doi: 10.64898/2026.03.04.709349
source: caskey-2026-single-cell-genomics-decontamination.md
category: single-cell-dl
tags: [ambient-RNA, decontamination, EM, mixture-model, scRNA-seq, spatial-transcriptomics, ATAC-seq]
---

## Summary

CellSweep addresses ambient RNA contamination in single-cell genomics using a multinomial mixture model that decomposes each cell's counts into cell-type-specific, ambient, and bulk-contamination components. Parameters are estimated by the EM algorithm. It achieves 98.84% cross-species contamination removal with a simulation PPV of 0.981, runs in 25 seconds on 16 CPU threads, and works across 10x Chromium, Smart-seq2, scATAC-seq, and Visium HD spatial transcriptomics.

## Key Contributions

- Multinomial mixture model with three components: clean cell-type signal, ambient RNA, and bulk contamination
- EM inference with an alternative mode for datasets without empty droplet barcodes
- 25-second runtime on 16 CPU threads — competitive with SoupX, DecontX, CellBender
- Validated on scRNA-seq, Smart-seq2, scATAC-seq, and spatial transcriptomics (Visium HD)

## Methods & Architecture

Each cell's count vector is modeled as a multinomial mixture of three profiles: (1) a cell-type-specific expression profile (the clean signal), (2) an ambient RNA profile estimated from empty droplets, and (3) a bulk contamination profile. The EM algorithm alternates between estimating per-cell mixing proportions (E-step) and updating the mixture parameters (M-step). When empty droplet barcodes are unavailable, CellSweep estimates the ambient profile directly from the count matrix. Implementation is multithreaded C++.

## Results

- Cross-species contamination removal: 98.84%
- Simulation PPV: 0.981
- Runtime: 25 seconds (16 CPU threads)
- Broad platform validation: 10x Chromium, Smart-seq2, scATAC-seq, Visium HD

## Limitations

- EM initialization sensitivity in highly heterogeneous datasets
- Captures-only ambient estimation less precise than empty-droplet-based estimation
- Performance on subtle, low-level ambient contamination less well-characterized

## Related Papers

- [[single-cell-dl/ergen-2024]] — single-cell DL quality control and preprocessing; complementary tool
- [[brain-atlas/braun-2023]] — large-scale single-cell brain atlas where ambient RNA decontamination is critical
- [[brain-atlas/corrigan-2025]] — brain atlas data; ambient RNA artifacts relevant in atlas-scale studies
