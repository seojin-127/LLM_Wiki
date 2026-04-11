---
title: "Mapping single-cell data to reference atlases by transfer learning"
authors: Lotfollahi, Mohammad, Naghipourfar, Mohsen, Luecken, Malte D., Khajavi, Matin, Buttner, Maren, Wagenstetter, Marco, Avsec, Ziga, Gayoso, Adam, Yosef, Nir, Interlandi, Marta, Rybakov, Sergei, Misharin, Alexander V., Theis, Fabian J.
year: 2022
doi: 10.1038/s41587-021-01001-7
category: single-cell-dl
pdf_path: papers/lotfollahi-2022-mapping-single-cell-data.pdf
pdf_filename: lotfollahi-2022-mapping-single-cell-data.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

scArches enables decentralized, privacy-preserving reference atlas building and query-to-reference mapping via "architecture surgery" — transfer learning that fine-tunes only a small fraction (~10,000) of parameters in a pre-trained scVI/scANVI model on query data, achieving accurate mapping without sharing raw data.

## 1. Document Info
- Journal/Conference: Nature Biotechnology
- Received/Published: Published January 2022 (DOI: 10.1038/s41587-021-01001-7)

## 2. Key Contributions
- scArches (single-cell architectural surgery): transfer learning framework for reference atlas updating and query mapping using any scVI-family base model
- Architecture surgery: adds dataset-specific parameters to a pretrained conditional neural network; fine-tunes only the new parameters (~10K vs. millions in full model); reference weights frozen
- Privacy-preserving: only the fine-tuned parameters need to be shared, not raw data
- 4 orders of magnitude fewer parameters than full de novo integration
- Retains disease variation when mapping COVID-19 data onto healthy reference
- Generalizes to multimodal and cross-species mapping

## 3. Methods & Architecture
- **Base model**: any scVI-family conditional VAE (scVI, scANVI, trVAE, etc.)
- **Architecture surgery**: for each new dataset/query, add a new set of condition-specific parameters (embedding vectors) to the encoder and decoder condition inputs; freeze all other weights; fine-tune only new parameters on query data
- **Reference building**: train base model on reference data; distribute frozen weights (the "reference model")
- **Query mapping**: user receives reference model; adds new parameters for their batch/dataset; fine-tunes on local data; projects cells into reference latent space
- **Label transfer**: annotation from reference cells to query cells via nearest neighbor in latent space
- **Multimodal mapping**: imputes missing modalities by mapping in shared RNA space

## 4. Key Results & Benchmarks
- Mouse brain atlas mapping: query cells from new protocols mapped accurately; ~10K parameters updated vs. millions in de novo integration
- Pancreas atlas: iterative reference building across multiple labs
- Immune / COVID-19: disease variation preserved when mapping onto healthy reference; disease-specific cell states identified
- Cross-species: human → mouse mapping with appropriate gene orthologs
- Multimodal: RNA→ATAC imputation; cross-modality label transfer

## 5. Limitations & Future Work
- Performance depends on base model quality; if reference model is poor, scArches cannot fully compensate
- Architecture surgery adds a new set of parameters per batch; many batches increase memory
- Fine-tuning requires some query data; zero-shot mapping not supported
- scPoli (2023) and later tools extend and improve the reference mapping paradigm

## 6. Related Work
- scVI (Lopez et al., 2018) — base integration model; scArches extends it
- scANVI (Xu et al., 2021) — semi-supervised base model; scArches enables reference mapping with labels
- scPoli (De Donno et al., 2023) — prototype-based reference mapping; outperforms scArches on population-level tasks
- Seurat anchor transfer — alternative reference mapping approach
- scIB benchmark (Luecken et al., 2022) — scArches variants evaluated in comprehensive benchmark

## 7. Glossary
- **scArches**: single-cell architectural surgery — the transfer learning method
- **Architecture surgery**: the technique of adding dataset-specific parameters to a pretrained model and fine-tuning only those; core innovation of scArches
- **Reference atlas**: a large, well-annotated single-cell dataset serving as a reference for mapping new query data
- **Query dataset**: a new, smaller dataset to be mapped onto the reference atlas
- **Conditional VAE (CVAE)**: VAE conditioned on batch/dataset labels; used as base model in scArches
- **Transfer learning**: leveraging parameters learned from one task/dataset to improve performance on a different but related task/dataset
- **Privacy-preserving**: only model parameters (not raw expression values) need to be shared; protects patient data
