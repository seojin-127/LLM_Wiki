---
title: "Continuous cell-type diversification in mouse visual cortex development"
authors: Zizhen Yao, Kimberly A. Smith, Trygve E. Bakken, et al. (Allen Institute / Gao et al.)
year: 2025
doi: 10.1038/s41586-025-08757-x
category: brain-atlas
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/1017084828/Gao-2025-Continuous cell-type diversification.pdf
pdf_filename: Gao-2025-Continuous cell-type diversification.pdf
source_collection: endnote
---

## One-line Summary
Comprehensive single-cell transcriptomic and epigenomic atlas (568K RNA + 200K Multiome nuclei) of mouse visual cortex across embryonic E11.5 to postnatal P56, revealing continuous cell-type diversification driven by late-emerging neuronal subtypes at eye-opening and critical period onset.

## 1. Document Info
- Journal/Conference: Nature
- Published: 2025

## 2. Key Contributions
- Comprehensive developmental atlas: 568,654 scRNA-seq cells + 200,061 snMultiome nuclei, densely sampled E11.5–P56
- Reconstructed full transcriptomic developmental trajectory map for all excitatory, inhibitory, and non-neuronal cell types
- Identified branching points marking emergence of new cell types at specific developmental ages
- Revealed continuous cell-type diversification: many subtypes emerge late (eye-opening, critical period onset ~P14–P28)
- Cell-type-specific, temporally resolved gene regulatory networks (TF → chromatin motif → target gene)

## 3. Methods & Architecture
- Single-cell RNA-seq (568K cells) + single-nucleus Multiome (RNA + ATAC, 200K nuclei)
- Dense temporal sampling: 10 embryonic stages (E11.5–E18.5) + 10 postnatal stages (P0–P56)
- Trajectory reconstruction: pseudotime + lineage-informed methods
- GRN inference: TF motif accessibility in ATAC + gene expression correlation
- Comparison to adult mouse cortical taxonomy (~28 subclasses)

## 4. Key Results & Benchmarks
- All cell classes and nearly all subclasses established during embryonic neurogenesis (staggered parallel manner)
- Increasingly refined subtypes emerge postnatally: many glutamatergic and GABAergic subtypes appear at P14–P28
- Eye-opening and critical period trigger wave of cell-type maturation (activity-dependent)
- Cooperative changes in gene expression and chromatin accessibility are cell-type-specific and temporally resolved
- Cell-type-specific GRNs identified for each temporal window

## 5. Limitations & Future Work
- Mouse visual cortex only; generalizability to other cortical areas or human cortex requires further study
- Single-cell resolution but no spatial mapping within cortical layers
- GRN inference is correlative (not causal)

## 6. Related Work
- Yao et al. 2023: adult mouse cortex cell type taxonomy (BICCN)
- Trevino et al. 2020: chromatin accessibility in forebrain organoids (comparable approach)
- Herring et al. 2022: human PFC development scRNA-seq + scATAC-seq

## 7. Glossary
- **Multiome**: Joint RNA + ATAC-seq from same nucleus (10x Genomics)
- **GRN**: Gene regulatory network — TF → accessible motif → target gene
- **Critical period**: Developmental window of heightened plasticity (visual cortex: ~P14–P28 in mouse)
- **T-type**: Transcriptomic cell type defined by gene expression
