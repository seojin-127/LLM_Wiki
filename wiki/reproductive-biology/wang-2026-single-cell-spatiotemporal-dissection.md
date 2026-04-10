---
title: "Single-cell spatiotemporal dissection of the human maternal–fetal interface"
authors: Cheng Wang, Yan Zhou, Yuejun Wang, Susan J. Fisher, Jingjing Li et al.
year: 2026
doi: 10.1038/s41586-026-10316-x
source: wang-2026-single-cell-spatiotemporal-dissection.md
category: reproductive-biology
tags: [maternal-fetal-interface, single-cell, spatial-transcriptomics, cytotrophoblast, decidua, placenta, GWAS, atlas]
---

## Summary

Comprehensive atlas of the human maternal–fetal interface (MFI) spanning full gestation (GW5–39), integrating single-nucleus multiomics (191,735 paired snRNA+ATAC nuclei) with submicrometre spatial transcriptomics (~1.1 million cells via Stereo-seq). Resolves cytotrophoblast differentiation via a toggle switch model, discovers a novel R0→R1→R2 arterial endothelial state transition during spiral artery remodelling, and integrates GWAS data to pinpoint cells vulnerable to pregnancy complications.

## Key Contributions

- **Comprehensive MFI atlas**: 191,735 paired snRNA-seq + snATAC-seq nuclei, 19 cell types, GW5–39
- **Submicrometre spatial mapping**: STOmics Stereo-seq, 16 second-trimester sections, ~1.1 million cells
- **Toggle switch model**: EVT (71 TFs) vs. SCT (30 TFs) fate enforced by reciprocal transcription factor networks (FDR ≤ 0.01)
- **R0→R1→R2 endothelial state transition**: novel states during EVT-mediated spiral artery remodelling
- **ML invasiveness predictor**: cytotrophoblast invasiveness predicted from transcriptomic signatures
- **Endocannabinoid suppression**: DSC subtype suppresses EVT invasion via endocannabinoid signalling
- **GWAS integration**: cell types vulnerable to pre-eclampsia, preterm birth, and miscarriage identified

## Methods & Architecture

**Data layers:**
1. snRNA-seq + snATAC-seq (10x Genomics) — 191,735 paired nuclei, avg 8,336/sample
2. STOmics Stereo-seq (0.5 µm) — 16 slices, ~1.1M cells, 1 cm × 1 cm chips
3. CODEX multiplex protein imaging (pan-CK, CD31)

**Analysis:**
- Souporcell: maternal/fetal origin assignment (>95% success rate)
- chromVar: ATAC-seq TF motif enrichment
- CellOracle: GRN reconstruction (snATAC + snRNA integrated)
- Spatial co-occurrence analysis for decidual niche architecture
- GWAS fine-mapping integration

**Toggle switch GRN:**
- FOS → HLA-G, KRT8, FN1 (EVT activation)
- EVT TFs negatively associated with CGA, TFPI2, PLAC4 (SCT program suppression)
- Shared TF GCM1 required by both lineages but engages distinct target gene sets

## Results

| Item | Value |
|------|-------|
| Nuclei (multiomics) | 191,735 (paired snRNA + snATAC) |
| Spatial cells | ~1.1 million (Stereo-seq, 16 slides) |
| Cell types | 19 (VCT, EVT, SCT, DSC, mVEC, fVEC, dNK, etc.) |
| EVT-specific TFs | 71 (FDR ≤ 0.01) |
| SCT-specific TFs | 30 (FDR ≤ 0.01) |
| Endothelial states | R0, R1, R2 (spiral artery remodelling stages) |
| Maternal/fetal assignment | >95% (Souporcell) |

R2 state (post-EVT invasion): enriched for negative regulation of cell proliferation and positive regulation of apoptosis (FDR 10⁻³–10⁻⁵).

## Limitations

- Normal pregnancies only; limited pathological comparisons
- Spatial profiling concentrated in second trimester
- No perturbation/functional validation
- Endocannabinoid invasion suppression requires in vivo confirmation

## Related Papers

- [[single-cell-dl/]] — scRNA-seq cell annotation methodology
- [[gwas/]] — GWAS integration for pregnancy complications
