---
title: "Spatial landmark detection and tissue registration with deep learning"
authors: Markus Ekvall, Ludvig Bergenstråhle, Alma Andersson, Paulo Czarnewski, Johannes Olegård, Lukas Käll, Joakim Lundeberg
year: 2024
doi: 10.1038/s41592-024-02199-5
source: ekvall-2024-spatial-landmark-detection-tissue.md
category: other
tags: [spatial-omics, tissue-registration, landmark-detection, deep-learning, thin-plate-splines, histology, multimodal]
---

## Summary
ELD (effortless landmark detection): unsupervised deep learning method for spatial landmark detection and tissue registration. Uses a landmark detector network guided by thin-plate splines (TPS) for precise image warping. Works with small datasets (<10 samples), handles nonlinear deformations, and supports multimodal spatial omics data (histology, Visium, mass spectrometry imaging).

## Key Contributions
- ELD: unsupervised landmark detection + registration using CNN + thin-plate splines (no generative model)
- Works with small datasets typical of spatial omics experiments
- Handles nonlinear/elastic tissue deformations (beyond affine-only methods)
- Multimodal: aligns histology + spatial transcriptomics + MSI concurrently
- 3D z-stack alignment capability

## Methods & Architecture
- Landmark detector CNN identifies landmarks in tissue images
- TPS warping for precise image registration
- No generative model required (simpler than competing approaches)
- Evaluated on histology, spatially resolved transcriptomics (Visium), mass spectrometry imaging

## Results
- Superior accuracy and stability vs. existing landmark detection methods
- Effective with <10 training samples (relevant for spatial omics)
- Successfully aligns multimodal spatial data
- 3D tissue reconstruction from z-stacks demonstrated

## Limitations
- Highly irregular tissue morphologies not fully characterized
- Requires preprocessing of spatial omics data before registration

## Related Papers
- Spatial omics atlas papers using tissue registration (e.g., Allen Brain Atlas CCF)
- [[brain-atlas/shi-2023-spatial-atlas-mouse-cns]] — spatial atlas requiring tissue alignment (complementary use case)
