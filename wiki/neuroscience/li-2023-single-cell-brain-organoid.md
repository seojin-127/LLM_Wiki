---
title: "Single-cell brain organoid screening identifies developmental defects in autism"
authors: Chong Li, Jonas Simon Fleck, Catarina Martins-Costa, Juergen A. Knoblich, Barbara Treutlein, et al.
year: 2023
doi: 10.1038/s41586-023-06367-y
source: li-2023-single-cell-brain-organoid.md
category: neuroscience
tags: [ASD, CRISPR, organoid, screening, GRN, BAF-complex, ARID1B, pooled]
---

## Summary
Li et al. developed CHOOSE — a pooled CRISPR-Cas9 loss-of-function screen in mosaic cerebral organoids with scRNA-seq readout — to screen 36 high-risk ASD transcriptional regulator genes simultaneously. Dorsal intermediate progenitors, ventral progenitors, and upper-layer excitatory neurons are most vulnerable. ARID1B disrupts OPC/interneuron precursor fate transitions, confirmed in patient-specific iPSC organoids.

## Key Contributions
- CHOOSE: first pooled organoid perturbation screening system with scRNA-seq readout
- 36 ASD risk genes screened simultaneously; cell-type vulnerability map produced
- Most vulnerable: dorsal IPs, ventral progenitors, upper-layer excitatory neurons
- ARID1B (BAF): disrupts OPC + interneuron precursor fate; validated in patient iPSCs
- Developmental GRN from scRNA-seq + chromatin; ASD regulatory modules identified

## Methods & Architecture
- Mosaic cerebral organoids with inducible CRISPR-Cas9; guide RNA recovered from scRNA-seq
- Pooled multi-gene perturbation in single batch; chromatin + transcriptomic GRN

## Results
- BAF complex perturbations → ventral telencephalon enrichment
- ARID1B KO → impaired OPC + interneuron precursor fate transition
- Patient iPSC organoids confirm ARID1B phenotype

## Limitations
- Mosaic KO dilutes phenotypic effects; incomplete penetrance
- Organoid model incompletely recapitulates in vivo development

## Related Papers
- [[neuroscience/martinscosta-2024-arid1b-controls-transcriptional]] — ARID1B in callosal organoids (same gene, callosal phenotype vs. OPC/interneuron here)
- [[neuroscience/jin-2020-in-vivo-perturb-seq]] — in vivo Perturb-Seq of ASD genes (complementary in vivo approach)
- [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]] — HNOCA for mapping organoid perturbation cell states
