---
title: "Chromatin accessibility during human first-trimester neurodevelopment"
authors: Camiel C. A. Mannens, Lijuan Hu, Sten Linnarsson, et al.
year: 2025
doi: 10.1038/s41593-025-01933-2
source: mannens-2025-chromatin-accessibility-during.md
category: brain-development
tags: [chromatin, ATAC-seq, first-trimester, human-brain, CNN, TF-binding, GWAS, MDD]
---

## Summary
Mannens et al. generated the first whole-brain chromatin accessibility + paired gene expression atlas of the human first trimester (6–13 weeks, 135 clusters). A CNN identifies TF binding sites in cell-type-specific enhancers; applied to ESRRB in Purkinje cells. GWAS variant → CRE linking identifies midbrain GABAergic neurons as most vulnerable to major depressive disorder mutations.

## Key Contributions
- First whole-brain (not forebrain-only) first-trimester chromatin atlas (135 clusters)
- CNN for TF binding site identification in cell-type-specific enhancers
- GWAS → CRE → cell type vulnerability: midbrain GABAergic neurons for MDD
- Accessible regions increase with age and neuronal differentiation
- CRE → gene linkage by multiomic paired measurement

## Methods & Architecture
- snATAC-seq + paired RNA from whole developing human brain (6–13 weeks)
- CNN trained on cell-type-specific peaks for TF binding prediction
- Disease SNP → CRE → gene linkage for GWAS interpretation

## Results
- Chromatin opens progressively during first trimester and along neuronal differentiation
- ESRRB: CNN reveals Purkinje lineage activation mechanism
- MDD: midbrain GABAergic neurons most enriched for disease-associated CREs
- ASD, schizophrenia: additional validated cell type–disease associations

## Limitations
- First trimester only; postnatal dynamics not covered
- Limited fetal tissue access; CNN predictions need experimental validation

## Related Papers
- [[brain-development/trevino-2020-chromatin-accessibility-forebrain]] — forebrain organoid ATAC-seq (complementary; organoid rather than primary tissue)
- [[brain-development/herring-2022-human-prefrontal-cortex-gene]] — human PFC snATAC+RNA across development (postnatal complement)
- [[genomic-dl/zemke-2023-conserved-and-divergent-gene]] — cross-species ATAC+methylation in motor cortex; similar ML-CRE approach
