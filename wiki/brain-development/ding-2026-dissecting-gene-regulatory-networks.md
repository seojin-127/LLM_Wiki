---
title: "Dissecting gene regulatory networks governing human cortical cell fate"
authors: Yuxiang Ding, et al.
year: 2026
doi: 10.1038/s41586-025-08756-2
source: ding-2026-dissecting-gene-regulatory-networks.md
category: brain-development
tags: [CRISPRi, GRN, radial-glia, TF, cortical-neurogenesis, ASD, perturbation]
---

## Summary
Pooled CRISPRi screen of 44 transcription factors in human primary radial glia maps the GRN governing cortical cell fate. ZNF219 represses premature differentiation, while NR2E1 and ARX play opposing roles in RG lineage plasticity. Convergent downstream effector genes are enriched for neurodevelopmental disorder risk variants.

## Key Contributions
- CRISPRi screen of 44 TFs in human primary RG culture with Perturb-seq readout
- ZNF219: critical repressor of premature RG differentiation
- NR2E1 vs. ARX: opposing roles in RG self-renewal/differentiation balance
- Convergent effector genes enriched for ASD/ID risk variants

## Methods & Architecture
- Human primary radial glia culture (not organoid-based)
- Pooled CRISPRi (dCas9-KRAB) lentiviral screen targeting 44 TFs
- Single-cell RNA-seq (Perturb-seq) readout per perturbation
- Effector gene identification + disease variant enrichment

## Results
- ZNF219 KD → premature neuronal differentiation, loss of RG identity
- NR2E1 KD → increased self-renewal; ARX KD → increased differentiation
- Multiple TF perturbations converge on shared effector gene sets
- Effector gene sets enriched for ASD and intellectual disability risk variants

## Limitations
- Primary RG culture; in vivo validation pending
- 44 TFs screened; full GRN coverage incomplete
- CRISPRi knockdown (not full KO); residual activity possible

## Related Papers
- [[neuroscience/li-2023-single-cell-brain-organoid]] — CHOOSE pooled CRISPR screen of ASD risk genes in organoids (complementary approach)
- [[neuroscience/jourdon-2023-modeling-idiopathic-autism]] — TF divergence in idiopathic ASD neural progenitors
- [[brain-development/nano-2025-integrated-analysis-molecular]] — FEZF2/TSHZ3 TF programs in cortical layer specification
