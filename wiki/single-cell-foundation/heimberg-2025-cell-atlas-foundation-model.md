---
title: "A cell atlas foundation model for scalable search of similar human cells"
authors: Graham Heimberg, Tony Kuo, Daryle J. DePianto, et al.
year: 2025
doi: 10.1038/s41586-024-08411-0
source: heimberg-2025-cell-atlas-foundation-model.md
category: single-cell-foundation
tags: [foundation-model, metric-learning, cell-similarity, atlas, scRNA-seq, ILD, fibrosis, cross-tissue]
---

## Summary
SCimilarity: metric-learning foundation model enabling rapid search of 23.4M human single-cell profiles from 412 studies. Finds transcriptionally similar cell states across organs, diseases, and in vitro models without retraining. ILD macrophage queries find similar states in other fibrotic diseases; top in vitro hit experimentally validated.

## Key Contributions
- SCimilarity: metric-learning framework for universal, interpretable single-cell representation
- 23.4M-cell searchable atlas from 412 scRNA-seq studies
- Cross-tissue, cross-disease cell similarity search at scale
- ILD macrophage/fibroblast queries → similar states in other fibrotic tissues
- 3D hydrogel macrophage system (top in vitro hit) experimentally validated

## Methods & Architecture
- Metric learning: single-cell profiles embedded so similar cells are proximal
- 23.4M-cell corpus from 412 studies; query = input cell profile → nearest neighbors

## Results
- Rapid scalable search across 23.4M cells
- Cross-study similar cell state discovery (ILD → fibrosis; in vitro → in vivo)
- Interpretable: gene-level drivers of cell similarity identified

## Limitations
- Training corpus biased toward well-studied tissues
- Spatial context not captured in representation

## Related Papers
- [[single-cell-dl/fischer-2024-sctab-scaling-cross-tissue]] — scTab cross-tissue cell annotation (complementary)
- [[single-cell-dl/ergen-2024-consensus-prediction-cell]] — popV label transfer with uncertainty
