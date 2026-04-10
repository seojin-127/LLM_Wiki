---
title: "multiDGD: A versatile deep generative model for multi-omics data"
authors: Viktoria Schuster, Emma Dann, Anders Krogh, Sarah A. Teichmann
year: 2024
doi: 10.1038/s41467-024-53340-z
source: schuster-2024-multidgd-versatile-deep.md
category: single-cell-dl
tags: [deep-generative, VAE, multi-omics, RNA, ATAC, integration, batch-correction]
---

## Summary
multiDGD is a probabilistic deep generative model (VAE-based) for joint representation of paired scRNA-seq + scATAC-seq data. Key advantages: (1) excellent reconstruction without feature selection, (2) post-hoc batch integration via covariate modeling without fine-tuning, (3) statistical identification of gene–regulatory region associations. scverse-compatible.

## Key Contributions
- Best-in-class data reconstruction without feature selection for RNA+ATAC
- Post-hoc integration: sample covariate modeling avoids retraining for new batches
- Gene-regulatory region associations from conditioned representations
- Open-source, scverse ecosystem compatible

## Methods & Architecture
- VAE with shared latent space + separate decoders (RNA: count distribution, ATAC: binary/count)
- Probabilistic sample covariate modeling for batch effects
- Statistical testing for gene–CRE associations conditioned on latent representations

## Results
- Outperforms existing multi-omics methods on reconstruction (human + mouse datasets)
- Well-clustered joint representations; effective batch correction without retraining
- Known TF–CRE links recovered; novel candidates identified

## Limitations
- Limited to RNA+ATAC pairs; other modalities not tested
- Scalability to >1M cells not benchmarked

## Related Papers
- [[single-cell-dl/li-2025-uda-seq-universal-droplet]] — UDA-seq: multimodal data generation (complements multiDGD analysis)
- [[single-cell-dl/wang-2024-scsemiprofiler-advancing-large]] — scSemiProfiler: another deep generative approach for large-cohort single-cell
- [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna]] — Cell2fate: Bayesian ODE for RNA velocity (different multi-modal approach)
