---
title: "Molecular logic of cellular diversification in the mouse cerebral cortex"
authors: Daniela J. Di Bella, Ehsan Habibi, Robert R. Stickels, Gabriele Scalia, Juliana Brown, Payman Yadollahpour, Sung Min Yang, Catherine Abbate, Tommaso Biancalani, Evan Z. Macosko, Fei Chen, Aviv Regev, Paola Arlotta
year: 2021
doi: 10.1038/s41586-021-03670-5
source: dibella-2021-molecular-logic-of-cellular.md
category: brain-development
tags: [mouse-cortex, developmental-atlas, trajectory, Slide-seq, post-mitotic-diversification, projection-neuron, corticogenesis]
---

## Summary

A complete developmental atlas of the mouse somatosensory cortex — scRNA-seq at 11 timepoints from E10.5 to P4, scATAC-seq, and Slide-seq spatial transcriptomes at four stages. The central biological finding: projection neurons diversify **post-mitotically**, not from pre-committed progenitors. Apical progenitors form a continuum ordered by age rather than subtype; PN subtypes diverge only after cell-cycle exit. The same map is then used as a reference to localize which lineage and timepoint is disrupted in mutant corticogenesis.

## Key Contributions

- Settles the progenitor-commitment debate for mouse cortex: APs are not strictly fate-restricted — the evidence is that clustering and embedding of APs/IPs is ordered by age, not by future PN subtype, and that known PN markers (Fezf2, Satb2) do not segregate AP populations.
- Glial vs. neuronal branch divergence at E13.5 is earlier than previously appreciated: primed neurogenic APs (Btg2+, Neurog2+, Hes6+) coexist with naive radial-glial-like APs.
- Spatially maps transient migrating states: 5 substates of migrating neurons at E15.5 occupy sequential radial positions, showing a spatiotemporal gradient.
- Provides a reference atlas that localizes mutant defects to specific lineages and timepoints.

## Methods & Architecture

- **Profiling**: 98,047 scRNA-seq cells × 11 timepoints E10.5-P4; matched scATAC-seq; Slide-seq v2 at E12.5/E13.5/E15.5/P1.
- **Trajectories**: URD branched tree on pseudotime-ordered cells; Monocle3 cross-validation.
- **Spatial mapping**: Tangram maps scRNA-seq cell-type identities onto Slide-seq pucks.
- **Branch-point analysis**: cells at bifurcations examined for differentially expressed regulators.

## Results

- **Full cell type coverage**: APs, IPs, Cajal-Retzius, CFuPN subtypes (CThPN, SCPN, layer 6b, near-projecting), CPN subtypes (layers 2/3, 5/6, stellate layer 4), interneurons by origin (MGE, CGE, pallial-subpallial), OPCs, astrocytes, microglia, vasculature.
- **Post-mitotic PN diversification**: AP clustering driven by age, not by subtype; neuronal progenies progressively separate at the post-mitotic level rather than at progenitor level. Known markers Fezf2, Pou3f3 co-expressed in progenitors; segregation happens after exit.
- **Early glial/neuronal branching at E13.5**: coexisting primed neurogenic and naive glial-leaning AP states in the ventricular zone.
- **Sequential interneuron invasion**: MGE E13.5 → CGE E15.5 → pallial-subpallial E18.5.
- **Migrating neuron spatial gradient**: 5 E15.5 migration substates occupy sequential apical-to-distal positions.
- **CPN layer 5/6 perinatal divergence**: P1 layer 5 and layer 6 CPNs become molecularly distinct in the postnatal window.

## Limitations

- Mouse only — human cortex has much longer developmental windows and different temporal architecture ([[brain-development/herring-2022-human-prefrontal-cortex-gene]]).
- Post-mitotic diversification claim relies on transcriptomes; epigenetic priming in progenitors is not fully ruled out.
- Trajectory inference from snapshots, not true lineage tracing.
- Slide-seq v2 resolution limits single-cell-level spatial assignment to probabilistic mapping.

## Related Papers

- [[brain-development/trevino-2020-chromatin-accessibility-forebrain]] — human fetal cortex chromatin accessibility, complementary modality
- [[brain-development/herring-2022-human-prefrontal-cortex-gene]] — human PFC prenatal-adult transcriptomics
- [[brain-development/zhang-2025-pfc-single-cell-spatiotemporal]] — human PFC spatiotemporal atlas
- [[brain-atlas/braun-2023-comprehensive-cell-atlas-first]] — first-trimester human brain atlas
- [[brain-development/kanton-2019-organoid-single-cell-genomic]] — cross-species cortical organoid comparison
- [[brain-development/fleck-2023-inferring-perturbing-cell-fate]] — organoid trajectory + in silico perturbation
- [[neuroscience/amelan-2026-crispr-knockout-screens-reveal]] — neural differentiation essential genes, complementary loss-of-function screen
