---
title: "Single-cell spatiotemporal dissection of the human maternal–fetal interface"
authors: Cheng Wang, Yan Zhou, Yuejun Wang, Tuhin Kumar Guha, Zhida Luo, Anxhela Mustafaraj, Tara I. McIntyre, Marisa E. Schwab, Brittany R. Davidson, Gabriella C. Reeder, Ronald J. Wong, Sarah K. England, Juan M. Gonzalez, Robert Blelloch, Alexis J. Combes, Linda C. Giudice, Adrian Erlebacher, Tippi C. MacKenzie, David K. Stevenson, Gary M. Shaw, Michael P. Snyder, Xiaofei Sun, Virginia D. Winn, Susan J. Fisher, Jingjing Li
year: 2026
doi: 10.1038/s41586-026-10316-x
category: reproductive-biology
pdf_path: papers/wang-2026-single-cell-spatiotemporal-dissection.pdf
pdf_filename: wang-2026-single-cell-spatiotemporal-dissection.pdf
source_collection: endnote-library
---

## One-line Summary

Comprehensive single-nucleus multiomics + submicrometre spatial transcriptomics atlas of the human maternal–fetal interface (GW5–39), resolving cell differentiation programs, spatial niches, and cell states vulnerable to pregnancy complications.

## 1. Document Info
- Journal/Conference: Nature
- DOI: 10.1038/s41586-026-10316-x
- Received: 25 September 2024
- Accepted: 23 February 2026
- Published: 2026 (online first)

## 2. Key Contributions
- Large-scale snRNA-seq + snATAC-seq atlas of the human MFI across full gestation (GW5–39): 191,735 paired nuclei, 19 cell types
- Submicrometre spatial whole-transcriptome mapping (STOmics Stereo-seq, 0.5 µm) of 16 second-trimester basal plate sections (~1.1 million cells), integrated with CODEX multiplex protein imaging
- Toggle switch model for cytotrophoblast fate: mutually exclusive EVT vs. SCT lineage commitment enforced by reciprocal transcription factor networks
- Discovery of a novel arterial endothelial state transition (R0 → R1 → R2) during EVT-mediated spiral artery remodelling
- Machine learning model predicting cytotrophoblast invasiveness from transcriptomic signatures
- Identification of a decidual stromal cell subtype that suppresses cytotrophoblast invasion via endocannabinoid signalling
- GWAS integration pinpointing cell types most vulnerable to pre-eclampsia, preterm birth, and miscarriage

## 3. Methods & Architecture

**Data generation:**
- snRNA-seq + snATAC-seq (10x Genomics): 191,735 paired nuclei, average 8,336 nuclei/sample
- Spatial transcriptomics: STOmics Stereo-seq (0.5 µm resolution, 1 cm × 1 cm chips), 16 second-trimester basal plate sections, ~1.1 million cells
- CODEX multiplex protein imaging (pan-CK, CD31, etc.)
- Samples: GW5–GW39, normal pregnancies, decidua basalis + basal plate

**Analysis pipeline:**
- Souporcell: maternal/fetal origin assignment (>95% of cells)
- chromVar: ATAC-seq transcription factor motif enrichment
- CellOracle: GRN reconstruction integrating snATAC-seq + snRNA-seq
- Spatial co-occurrence analysis: decidual niche architecture
- GWAS integration: cell-type-level vulnerability to pregnancy complications

**Cell types (19):**
VCT, EVT, SCT, DSC, eS, FB, PV, mVEC, fVEC, LEC, eEpi, Cili, dNK, M, HB, DC, B, T, Ery

## 4. Key Results & Benchmarks

**Toggle switch model (EVT vs. SCT fate):**
- 71 TFs specifically upregulated in EVTs, 30 in SCTs (FDR ≤ 0.01)
- EVT TFs (ASCL2, FOS, KLF6, STAT1) activate EVT genes while repressing SCT genes; reciprocal pattern in SCTs
- Shared TF GCM1 engages distinct target gene sets in each lineage
- FOS positively regulates HLA-G, KRT8, FN1 in EVTs; negatively associates with SCT markers (CGA, TFPI2, PLAC4)

**Spiral artery remodelling:**
- Novel R0 (normal arterial EC) → R1 (transitional) → R2 (post-EVT invasion) endothelial state transition
- R2 state enriched for GO terms: negative regulation of cell proliferation, positive regulation of apoptosis (FDR 10⁻³–10⁻⁵)

**Spatial architecture:**
- DSC–dNK spatial co-localization confirmed as a recurring decidual niche
- EVT invasion patterns spatially quantified around spiral arteries

**Pregnancy complications:**
- GWAS integration maps specific cell types most vulnerable to pre-eclampsia, preterm birth, and miscarriage

## 5. Limitations & Future Work
- Focus on normal pregnancies; limited pathological samples for direct comparison
- Spatial profiling concentrated in second trimester; first/third trimester spatial data lacking
- Observational atlas; no perturbation/functional validation experiments
- Endocannabinoid-mediated invasion suppression requires in vivo validation

## 6. Related Work
- Vento-Tormo et al. (prior placental atlas; used for label transfer validation)
- CellOracle (GRN reconstruction tool)
- STOmics Stereo-seq (spatial transcriptomics platform)
- chromVar (ATAC-seq TF motif analysis)
- Souporcell (genotype-based cell demultiplexing)

## 7. Glossary
- **MFI (Maternal-Fetal Interface)**: Hemi-allogeneic tissue junction between placenta and decidua
- **EVT (Extravillous Trophoblast)**: Invasive trophoblast cells; remodel spiral arteries
- **SCT (Syncytiotrophoblast)**: Multinucleated fused trophoblast; mediates nutrient exchange and hormone secretion
- **VCT (Villous Cytotrophoblast)**: Progenitor cells giving rise to both EVT and SCT lineages
- **DSC (Decidual Stromal Cell)**: Uterine stromal cells supporting placental attachment
- **GRN (Gene Regulatory Network)**: Transcription factor–target gene regulatory network
- **snATAC-seq**: Single-nucleus open chromatin sequencing
- **Stereo-seq**: STOmics submicrometre spatial transcriptomics platform
- **CODEX**: Multiplexed protein imaging technology
- **Toggle switch model**: Bistable regulatory system that reinforces one cell fate while actively suppressing the alternative
- **Spiral artery remodelling**: EVT-driven conversion of uterine spiral arteries into low-resistance vessels
