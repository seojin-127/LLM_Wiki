---
title: "Continuous cell-type diversification in mouse visual cortex development"
authors: Gao et al.
year: 2025
doi: 10.1038/s41586-025-08757-x
source: gao-2025-continuous-cell-type-diversification.md
category: brain-atlas
tags: [mouse, cortex, scRNA-seq, ATAC-seq, multiome, GRN, development, critical-period]
---

## Summary
A comprehensive single-cell atlas of mouse visual cortex development (568K RNA cells + 200K Multiome nuclei, E11.5–P56) reveals that while all cell classes are established embryonically, cell-type diversification continues postnatally — with many neuronal subtypes emerging specifically at eye-opening and critical period onset. Cell-type-specific GRNs are resolved across the full timeline.

## Key Contributions
- Largest developmental atlas of mouse visual cortex: 768K+ cells/nuclei, 20 timepoints
- Continuous cell-type diversification: late subtypes emerge at P14–P28 (activity-dependent)
- Temporally resolved GRNs linking TFs, chromatin accessibility, and target genes
- All subclasses established embryonically; refinement into subtypes is postnatal

## Methods & Architecture
- scRNA-seq (568K) + snMultiome RNA+ATAC (200K), E11.5–P56 dense sampling
- Trajectory reconstruction + lineage inference; GRN from ATAC motifs + expression

## Results
- Cell classes/subclasses emerge in staggered parallel during embryonic stage
- Many glutamatergic and GABAergic subtypes: late postnatal (P14–P28, eye-opening/critical period)
- GRNs are cell-type-specific and temporally restricted
- Chromatin and transcriptomic changes co-occur in cell-type-specific manner

## Limitations
- Mouse visual cortex only; spatial resolution absent
- GRN inference is correlative

## Related Papers
- [[brain-development/trevino-2020-chromatin-accessibility-forebrain]] — complementary ATAC+RNA approach in human organoids
- [[brain-development/herring-2022-human-prefrontal-cortex-gene]] — human PFC development atlas for cross-species comparison
- [[brain-atlas/zhang-2023-molecularly-defined-spatially]] — adult mouse brain whole-atlas (complementary spatial view)
