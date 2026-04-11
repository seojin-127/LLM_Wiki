---
title: "CRISPR knockout screens reveal genes and pathways essential for neuronal differentiation and implicate PEDS1 in neurodevelopment"
authors: Alana Amelan, Stephan C. Collins, Nadirah S. Damseh, Nanako Hamada, Ahd Salim, Elad Dvir, Galya Monderer-Rothkoff, Tamar Harel, Koh-ichi Nagata, Binnaz Yalcin, Sagiv Shifman
year: 2026
doi: 10.1038/s41593-025-02165-0
category: neuroscience
pdf_path: papers/amelan-2026-crispr-knockout-screens-reveal.pdf
pdf_filename: amelan-2026-crispr-knockout-screens-reveal.pdf
source_collection: downloads-perturb-batch
---

## One-line Summary

Genome-wide CRISPR KO screens in mouse ESCs differentiating into neural lineage identify 331 neural-differentiation-essential genes (NEGs) — enriched for known NDD genes but mostly novel — and implicate PEDS1 (plasmalogen biosynthesis) as a recessive microcephaly gene, validated in mice and a consanguineous human family.

## 1. Document Info
- Journal: Nature Neuroscience, Vol 29, March 2026, 592-603
- Published online: 5 January 2026

## 2. Key Contributions

- First genome-scale CRISPR KO screen specifically targeting neural differentiation (day 0 / 4 / 10 of mESC → neural lineage).
- Defines 331 NEGs (neural-differentiation-essential) and 110 NGGs (neural-differentiation growth-restricting). NEGs show small overlap with common essential genes — they are specifically required for the neural trajectory.
- NEGs enriched for known dominant NDD genes (transcriptional regulators); recessive NDD genes more metabolic.
- 8/32 tested NEGs produce significant mouse neuroanatomical defects (FDR <0.1): Dusp26, Dynlrb2, Eml1, Mta3, Sgms1, Slitrk4, Peds1, Vamp3. Half show microcephaly.
- **PEDS1**: bi-allelic variant identified in consanguineous family with microcephaly + global delay + congenital cataracts. Mouse KO: accelerated cell-cycle exit, impaired neuronal differentiation and migration.
- Plasmalogen biosynthesis (lipid metabolism) as a new NDD mechanism.

## 3. Methods & Architecture

- **Library**: 19,674 mouse genes × 4 sgRNAs per gene; mESC transfection.
- **Time course**: day 0 (mESC), day 4 (neural commitment), day 10 (early neuronal).
- **Analysis**: log2FC of sgRNA abundance vs. day 0 baseline; FDR < 0.05 cutoffs; separate NEG/NGG classification.
- **Validation**: Sox1-GFP reporter + flow cytometry for 4 hit genes; MARIS-style neuroanatomy for 8 hit genes in mouse knockouts.
- **Human genetics**: whole exome sequencing of consanguineous family with microcephaly; homozygous PEDS1 variant segregation.

## 4. Key Results & Benchmarks

- 1,752 day-4/10 depleted genes → 331 NEGs after removing mESC-essential overlap.
- NEGs enriched for transcription/chromatin regulation and metabolic processes (GO).
- STRING PPI network: largest cluster is transcription/chromatin; other clusters are sterol biosynthesis, histone acetylation, GPI-anchor biosynthesis, nuclear pore.
- NEG transcription regulators are most expressed in radial glia in the developing mouse brain.
- NEG-mouse-KO: 8/32 tested produce neuroanatomical defects; half microcephalic.
- PEDS1 bi-allelic human variant: microcephaly + delay + cataracts; mouse Peds1-/- recapitulates accelerated cell cycle exit, impaired differentiation and migration.

## 5. Limitations & Future Work

- Screen is gene-level KO: does not capture variant effects or allele-specific regulation.
- In vitro mESC differentiation — may miss in vivo spatial/temporal context.
- Only 32 of 331 NEGs tested in mouse; most candidates unvalidated.
- PEDS1 mechanism: lipid biosynthesis → neural differentiation link is correlative.
- Does not capture gene × gene interactions (single KO only).

## 6. Related Work

- Jin et al. 2020 in vivo Perturb-seq for autism genes — complementary in vivo approach.
- Paulsen 2022, Villa 2022, Martins-Costa 2024 — individual NDD gene organoid perturbations.
- Replogle 2022 genome-scale Perturb-seq — scRNA-seq readout of CRISPRi screens.

## 7. Glossary

- **NEG (neural differentiation essential gene)**: gene whose KO depletes sgRNAs specifically during neural differentiation, not during mESC proliferation.
- **NGG (neural differentiation growth-restricting gene)**: KO increases sgRNA abundance — cells gain a proliferative advantage.
- **PEDS1 / TMEM189**: plasmanylethanolamine desaturase 1, a key enzyme in plasmalogen biosynthesis.
- **Plasmalogen**: a class of glycerophospholipids critical for neuronal membranes.
- **NDD**: neurodevelopmental disorder.
