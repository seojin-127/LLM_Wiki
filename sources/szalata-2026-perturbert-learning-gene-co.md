---
title: "PerturBERT: Learning Gene Co-Response Representations from Genetic Perturbation Data"
authors: Szalata, Artur, Bica, Ioana, Schaar, Anne C., Lotfollahi, Mohammad
year: 2026
doi: ""
category: single-cell-foundation
pdf_path: papers/szalata-2026-perturbert-learning-gene-co.pdf
pdf_filename: szalata-2026-perturbert-learning-gene-co.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

PerturBERT pretrains a BERT encoder on ~1 million genetic perturbation signatures (L1000 + Perturb-seq) to learn gene co-response embeddings, matching or beating scGPT on 15 gene-property tasks with ~30× less training data.

## 1. Document Info
- Journal/Conference: ICLR 2026 Workshop on Machine Learning for Genomics Explorations (MLGenX)
- Received/Published: 2026

## 2. Key Contributions
- Purpose-built perturbation foundation model: pretrains exclusively on genetic perturbation response data (not bulk expression), learning how genes co-respond to interventions
- Masked-gene modeling objective on (gene, response) token pairs; 57.6M parameter BERT encoder (8 layers, 12 heads, hidden dim 256, intermediate dim 1024)
- Trained on ~1M perturbation signatures from L1000 (bulk, chemical/genetic) and Perturb-seq (single-cell, genetic) spanning 248 cell lines
- Achieves SOTA on gene dependency prediction (R²=0.8805) and competitive performance on 10/15 gene-property benchmarks vs. scGPT using ~30× less training data

## 3. Methods & Architecture
- **Architecture**: BERT encoder (transformer, bidirectional attention); 57.6M parameters; 8 layers, 12 heads, hidden dim 256, intermediate dim 1024
- **Tokenization**: each input token represents a (gene, perturbation-response-value) pair from a single perturbation experiment
- **Pre-training objective**: masked-gene modeling — randomly mask gene tokens and predict their identities from context (analogous to MLM but operating on gene-response pairs)
- **Training data**:
  - L1000 (CMap): ~975K signatures; bulk expression of ~978 landmark genes measured after chemical and genetic perturbations across 248 cell lines
  - Perturb-seq: single-cell CRISPR perturbation screens; transcriptomic responses per gene knockdown
- **Fine-tuning**: frozen encoder + linear probe for downstream gene-property tasks
- **Downstream tasks**: gene dependency (DepMap), gene essentiality, protein-protein interaction prediction, transcription factor binding, etc.

## 4. Key Results & Benchmarks
- Gene dependency prediction: R²=0.8805 (SOTA)
- Beats or matches scGPT on 10 of 15 gene-property benchmarks
- ~30× less training data than scGPT (single-cell expression atlas) yet competitive performance
- Particularly strong on perturbation-relevant tasks (gene dependency, co-essentiality)

## 5. Limitations & Future Work
- L1000 covers only ~978 landmark genes; full transcriptome coverage limited unless Perturb-seq data used
- BERT encoder produces gene embeddings, not cell embeddings — not directly applicable to cell-type annotation tasks
- Pretraining data biased toward cancer cell lines (DepMap/CMap)
- Future: scale to full-genome perturbation data; combine with cell-level models for cell-state prediction

## 6. Related Work
- scGPT (Cui et al., 2024) — generative single-cell foundation model pretrained on >33M cells; benchmark comparison target
- scFoundation (Hao et al., 2024) — large-scale single-cell foundation model; another benchmark
- GEARS (Roohani et al.) — perturbation prediction using gene interaction graphs
- ESM-2, DNABERT — analogous BERT-style encoders for protein/DNA sequences

## 7. Glossary
- **L1000 / CMap (Connectivity Map)**: LINCS database of ~1M chemical/genetic perturbation gene expression profiles measured via Luminex-based L1000 assay (~978 landmark genes)
- **Perturb-seq**: pooled single-cell CRISPR screen with transcriptome readout (10x Genomics); measures gene knockdown effects at single-cell resolution
- **Masked-gene modeling**: PerturBERT's pretraining objective — masking gene tokens and predicting them from context; analogous to masked language modeling in BERT
- **Gene dependency (DepMap)**: measure of how essential a gene is for cancer cell line survival; from CRISPR screens in the Cancer Dependency Map
- **scGPT**: single-cell generative pretrained transformer; foundation model pretrained on 33M+ single cells
- **Co-response**: the correlated transcriptional response patterns of gene pairs across many perturbation experiments
