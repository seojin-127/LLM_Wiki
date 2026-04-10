---
title: "UDA-seq: universal droplet microfluidics-based combinatorial indexing for massive-scale multimodal single-cell sequencing"
authors: Yun Li, Zheng Huang, Lubin Xu, et al.
year: 2025
doi: 10.1038/s41592-024-02586-y
source: li-2025-uda-seq-universal-droplet.md
category: single-cell-dl
tags: [multimodal, droplet-microfluidics, combinatorial-indexing, throughput, clinical, ATAC, CRISPR]
---

## Summary
UDA-seq adds a universal post-indexing step to any droplet microfluidics-based single-cell protocol, enabling massive-scale multimodal profiling (RNA+ATAC, RNA+VDJ, RNA+CRISPR). Demonstrated at clinical scale: 100K+ high-quality cells from 36 frozen biopsies in a single experiment, with identification of rare clinical subpopulations.

## Key Contributions
- Universal adaptor workflow — extends any droplet-based multimodal method without major protocol changes
- 100K+ cells from 36 clinical biopsies in one experiment
- Validated for RNA+VDJ, RNA+ATAC, RNA+CRISPR modality pairs
- Rare cell subpopulation detection from clinical specimens

## Methods & Architecture
- Post-indexing step added after droplet encapsulation; combinatorial barcoding for throughput
- Benchmarked across tissue types and species
- Compatible with standard analysis pipelines

## Results
- Massive scalability: 100K+ cells per experiment from clinical frozen specimens
- Rare subpopulation detection not achievable with lower-throughput methods
- Cost and throughput advantages over existing combinatorial indexing platforms

## Limitations
- Per-modality optimization still required; not fully plug-and-play
- Clinical biopsy quality variation; batch effects from frozen specimens

## Related Papers
- [[single-cell-dl/schuster-2024-multidgd-versatile-deep]] — multiDGD: deep generative model for RNA+ATAC joint analysis (downstream analysis complement)
- [[single-cell-dl/wang-2024-scsemiprofiler-advancing-large]] — scSemiProfiler: another approach to large-cohort single-cell profiling
