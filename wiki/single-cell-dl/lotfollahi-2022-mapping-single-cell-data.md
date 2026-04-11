---
title: "Mapping single-cell data to reference atlases by transfer learning"
authors: Lotfollahi, Mohammad, Naghipourfar, Mohsen, Luecken, Malte D., Khajavi, Matin, Buttner, Maren, Wagenstetter, Marco, Avsec, Ziga, Gayoso, Adam, Yosef, Nir, Interlandi, Marta, Rybakov, Sergei, Misharin, Alexander V., Theis, Fabian J.
year: 2022
doi: 10.1038/s41587-021-01001-7
source: lotfollahi-2022-mapping-single-cell-data.md
category: single-cell-dl
tags: [scArches, transfer-learning, reference-mapping, atlas, privacy-preserving, architecture-surgery, scVI]
---

## Summary

scArches enables privacy-preserving, decentralized reference atlas building and query-to-reference mapping via "architecture surgery": a pre-trained scVI/scANVI model is extended with a small set of query-specific parameters (~10K) that are fine-tuned while freezing reference weights. Users share only the fine-tuned parameters (not raw data), then project their cells into the reference latent space for label transfer and comparative analysis. Retains disease variation when mapping COVID-19 data onto a healthy reference.

## Key Contributions

- Architecture surgery: adds query-specific condition embeddings to pretrained CVAE; fine-tunes only ~10K of millions of parameters
- Privacy-preserving: model parameters only (not raw data) need to be shared
- 4 orders of magnitude fewer updated parameters than de novo integration
- Preserves disease-specific cell states when mapping COVID-19 onto healthy immune reference
- Generalizes to multimodal mapping (RNA→ATAC imputation) and cross-species

## Methods & Architecture

Architecture surgery: given a pretrained scVI/scANVI model (reference), add a new learned embedding vector per query batch to the encoder and decoder conditioning inputs; freeze all other weights; fine-tune new parameters on query data via the same ELBO objective. Label transfer: kNN from query z to reference z → reference annotations assigned. Modality imputation: map in RNA space → impute missing modality via reference decoder.

## Results

- Mouse brain atlas mapping: query cells from new protocols integrated accurately with ~10K parameter updates
- Pancreas atlas: iterative reference building across multiple labs; each lab extends without sharing raw data
- COVID-19 immune mapping: disease-specific monocyte and T cell states retained in shared healthy reference embedding
- Cross-species: human → mouse orthologs mapped with appropriate gene list
- Multimodal: RNA-only query imputes ATAC accessibility from reference

## Limitations

- Quality depends on reference model; poor reference propagates errors
- New parameters per query batch; memory grows with many queries
- Fine-tuning requires local query data; zero-shot not supported
- scPoli (2023) extends with prototype-based open-world capability

## Related Papers

- [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] — scVI: base model; scArches wraps it
- [[single-cell-dl/xu-2021-probabilistic-harmonization-and]] — scANVI: label-aware base model for scArches
- [[single-cell-dl/dedonno-2023-population-level-integration-of]] — scPoli: next-generation reference mapping with open-world capability
- [[single-cell-dl/luecken-2022-benchmarking-atlas-level-data]] — scIB benchmark: scArches variants evaluated
- [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]] — HNOCA uses scPoli (scArches successor) for integration
