---
title: "CRISPR knockout screens reveal genes and pathways essential for neuronal differentiation and implicate PEDS1 in neurodevelopment"
authors: Alana Amelan, Stephan C. Collins, Nadirah S. Damseh, Nanako Hamada, Ahd Salim, Elad Dvir, Galya Monderer-Rothkoff, Tamar Harel, Koh-ichi Nagata, Binnaz Yalcin, Sagiv Shifman
year: 2026
doi: 10.1038/s41593-025-02165-0
source: amelan-2026-crispr-knockout-screens-reveal.md
category: neuroscience
tags: [CRISPR-screen, neural-differentiation, NDD, PEDS1, microcephaly, plasmalogen, radial-glia, gene-level-perturbation]
---

## Summary

Genome-wide CRISPR knockout screens in mouse ESCs differentiating to neural lineage (day 0 / 4 / 10) identify 331 **neural-differentiation-essential genes (NEGs)** — a gene set that is enriched for known NDD genes but is mostly novel. NEGs converge on transcription/chromatin regulation (dominant NDD-like) and metabolic processes (recessive NDD-like). Mouse KOs of 8 candidate NEGs produce neuroanatomical defects; PEDS1, a plasmalogen biosynthesis enzyme, is validated as a recessive microcephaly gene in a consanguineous human family.

## Key Contributions

- Systematic gene-level screen for neural differentiation essentiality, distinct from general mESC essentiality.
- Identifies transcription/chromatin as the dominant-NDD axis and metabolism as the recessive-NDD axis — a clean genetic architecture split.
- **PEDS1 / plasmalogen biosynthesis** as a new NDD mechanism: lipid metabolism enters the NDD gene catalog.
- Demonstrates that gene-level CRISPR KO is a viable source of NDD candidate genes, complementary to exome sequencing.

## Methods & Architecture

1. **Library**: 19,674 genes × 4 sgRNAs in mouse ESCs.
2. **Differentiation time course**: day 0 (mESC, Nanog+), day 4 (neural commitment, Sox1+), day 10 (early neurons, Tubb3+).
3. **Hit definition**:
   - mESC-essential genes (EEGs) = depleted in day 0 library → removed as background.
   - NEGs (331) = depleted on day 4 or 10, but NOT in mESC.
   - NGGs (110) = enriched on day 10 — growth-restricting during differentiation.
4. **Validation**:
   - Sox1-GFP reporter + flow cytometry (G6pdx, Hmgcs1, Ola1, Rbpj).
   - Mouse knockouts of 32 NEGs → neuroanatomy with histomorphometry → 8 hits (FDR <0.1).
   - PEDS1 family study: whole-exome sequencing identified homozygous variant segregating with microcephaly + cataracts + delay.
   - Peds1-/- mouse: accelerated cell cycle exit, impaired neuronal differentiation and migration.

## Results

- **331 NEGs**; small overlap with common essential genes — genuinely neural-specific.
- **GO enrichment**: transcription regulation (61 NEGs) + metabolic processes dominate.
- **PPI clusters**: transcription/chromatin (C1), signaling (C2), histone acetylation (C3), sterol biosynthesis (C4-C5), GPI anchor (C6), nuclear pore (C7).
- **Cell-type expression**: NEG transcription regulators are most enriched in radial glia in developing mouse brain.
- **Mouse KO neuroanatomy**: Dusp26, Dynlrb2, Eml1, Mta3, Sgms1, Slitrk4, Peds1, Vamp3 all show defects; 4 show microcephaly.
- **PEDS1 human family**: bi-allelic variant in consanguineous family, microcephaly + global developmental delay + congenital cataracts. Mouse Peds1 KO recapitulates cell-cycle exit and migration defects.

## Limitations

- Gene-level KO, not variant-level. Does not address how non-coding risk variants act on enhancers or allele-specific expression — the central gap between GWAS hits and mechanism.
- In vitro mESC differentiation lacks in vivo spatial and temporal context.
- Only 32/331 NEGs tested in mice; most candidate NDD genes remain uncharacterized.
- Single KO per cell — no gene × gene interaction.

## Related Papers

- [[neuroscience/jin-2020-in-vivo-perturb-seq]] — in vivo Perturb-seq for autism risk genes, complementary approach using scRNA-seq readout
- [[neuroscience/paulsen-2022-autism-genes-converge]] — organoid KOs showing convergence on shared trajectories
- [[neuroscience/villa-2022-chd8-haploinsufficiency]] — single NDD gene organoid study
- [[neuroscience/martinscosta-2024-arid1b-controls-transcriptional]] — ARID1B-specific mechanism study
- [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] — TRADE, statistical framework relevant when upgrading these screens to Perturb-seq readouts
- [[neuroscience/dubuc-2026-linking-rare-variants-cell-type]] — rare variant interpretation via foundation model, complementary to gene-level screens
