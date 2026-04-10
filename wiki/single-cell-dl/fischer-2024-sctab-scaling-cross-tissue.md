---
title: "scTab: Scaling cross-tissue single-cell annotation models"
authors: Felix Fischer, David S. Fischer, Roman Mukhin, et al.
year: 2024
doi: 10.1038/s41467-024-51059-5
source: fischer-2024-sctab-scaling-cross-tissue.md
category: single-cell-dl
tags: [cell-annotation, tabular-DL, cross-tissue, scaling, data-augmentation, scRNA-seq]
---

## Summary
scTab is a tabular deep learning model for automated cross-tissue cell type annotation, trained on 22.2M scRNA-seq cells. Cross-tissue annotation requires nonlinear models, and performance scales with both data and model size; data augmentation improves generalization.

## Key Contributions
- scTab: tabular DL model for de novo cross-tissue cell type annotation
- 22.2M training cells across diverse tissues
- Scaling laws confirmed: more data + larger model → better annotation
- Novel data augmentation improves cross-tissue generalization

## Methods & Architecture
- MLP-style tabular deep learning on gene expression input
- Training on 22.2M curated scRNA-seq cells; held-out tissue evaluation
- Data augmentation: gene dropout and expression noise

## Results
- Nonlinear models outperform linear baselines for cross-tissue annotation
- Data and model size both show positive scaling effects
- Data augmentation consistently improves generalization to unseen tissues

## Limitations
- Annotation quality depends on training label quality
- Struggles with rare/novel cell types outside training distribution

## Related Papers
- [[single-cell-dl/ergen-2024-consensus-prediction-cell]] — popV ensemble cell type label transfer (complementary)
- [[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]] — SCimilarity foundation model for cell similarity (related)
