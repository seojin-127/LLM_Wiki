---
title: "PerturBERT: Learning Gene Co-Response Representations from Genetic Perturbation Data"
authors: Szalata, Artur, Bica, Ioana, Schaar, Anne C., Lotfollahi, Mohammad
year: 2026
doi: ""
source: szalata-2026-perturbert-learning-gene-co.md
category: single-cell-foundation
tags: [BERT, perturbation, foundation-model, gene-embeddings, L1000, Perturb-seq, masked-gene-modeling]
---

## Summary

PerturBERT is a BERT-style foundation model (57.6M parameters, 8 layers) pretrained exclusively on ~1 million genetic and chemical perturbation signatures from L1000 and Perturb-seq across 248 cell lines. Using a masked-gene modeling objective on (gene, perturbation-response) token pairs, it learns gene co-response representations that achieve SOTA on gene dependency prediction (R²=0.8805) and match or beat scGPT on 10/15 gene-property tasks using ~30× less training data.

## Key Contributions

- Perturbation-centric pretraining: the first foundation model trained exclusively on interventional (perturbation) rather than observational (expression atlas) data
- Masked-gene modeling on (gene, response-value) token pairs as pretraining objective
- ~30× data efficiency vs. scGPT while achieving competitive or superior performance on gene-property benchmarks
- SOTA gene dependency prediction (R²=0.8805) using DepMap as downstream task

## Methods & Architecture

BERT encoder with 8 transformer layers, 12 attention heads, hidden dimension 256, and intermediate dimension 1024 (57.6M total parameters). Each input token encodes a (gene identity, perturbation response value) pair from a single perturbation experiment. The masked-gene modeling objective randomly masks gene tokens and trains the model to predict masked gene identities given the remaining (gene, response) context. Pretraining used ~975K L1000 (CMap) signatures plus Perturb-seq single-cell CRISPR screens spanning 248 cancer cell lines. Downstream evaluation uses frozen encoder + linear probe.

## Results

- Gene dependency prediction (DepMap): R²=0.8805 (SOTA)
- Beats scGPT on 10/15 gene-property tasks
- Achieves this with ~30× less training data than scGPT
- Particularly strong on perturbation-relevant tasks such as gene co-essentiality and dependency

## Limitations

- L1000 covers only ~978 landmark genes; full-transcriptome coverage depends on Perturb-seq data
- Generates gene-level, not cell-level embeddings — not directly applicable to cell-type annotation
- Training data skewed toward cancer cell lines (CMap/DepMap ecosystem)

## Related Papers

- [[single-cell-foundation/hao-2024-large-scale-cell-representation]] — scFoundation; large-scale single-cell foundation model; benchmark target
- [[single-cell-foundation/cui-2024-scgpt-toward-building-a]] — scGPT; primary benchmark comparison model
- [[neuroscience/jin-2025]] — Perturb-seq in neuroscience context; PerturBERT could apply to brain perturbation data
- [[single-cell-foundation/chen-2025-epiagent]] — EpiAgent; another perturbation-aware single-cell model
