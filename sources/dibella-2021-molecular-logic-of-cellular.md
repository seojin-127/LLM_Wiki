---
title: "Molecular logic of cellular diversification in the mouse cerebral cortex"
authors: Daniela J. Di Bella, Ehsan Habibi, Robert R. Stickels, Gabriele Scalia, Juliana Brown, Payman Yadollahpour, Sung Min Yang, Catherine Abbate, Tommaso Biancalani, Evan Z. Macosko, Fei Chen, Aviv Regev, Paola Arlotta
year: 2021
doi: 10.1038/s41586-021-03670-5
category: brain-development
pdf_path: papers/dibella-2021-molecular-logic-of-cellular.pdf
pdf_filename: dibella-2021-molecular-logic-of-cellular.pdf
source_collection: downloads-perturb-batch
---

## One-line Summary

A comprehensive scRNA-seq + scATAC-seq + Slide-seq time course of the mouse somatosensory cortex (E10.5 → P4, 98K cells) reconstructs differentiation trajectories of all cortical cell classes, shows that projection neurons diversify post-mitotically (not from pre-committed progenitors), and uses the map to pinpoint lineage-specific origins of aberrant corticogenesis in mutant mice.

## 1. Document Info
- Journal: Nature, Vol 595, 22 July 2021, 554-559
- Published online: 23 June 2021

## 2. Key Contributions

- **Complete cortical development atlas**: 98,047 scRNA-seq cells × 11 timepoints (E10.5-P4) + matched scATAC-seq + Slide-seq spatial transcriptomes at E12.5, 13.5, 15.5, P1.
- **Post-mitotic PN diversification**: apical progenitors form a continuum ordered by age, not by subtype. PN subtypes (CFuPN, CPN) diverge post-mitotically, arguing against strict pre-commitment.
- **Glial-neural branch divergence at E13.5**: progenitors split into neuronal (Btg2, Neurog2, Hes6) and glial (Fabp7, Dbi, Slc1a3) branches earlier than expected.
- **Transient cell states mapped spatially**: Slide-seq places migrating excitatory neuron substates at sequential apical-to-distal positions.
- **Mutant corticogenesis mapping**: the healthy developmental map pinpoints which lineage and timepoint is disrupted in Emx1-cKO and other mutants.

## 3. Methods & Architecture

- **Data**: 98K scRNA-seq, matched scATAC-seq, and Slide-seq v2 spatial at 4 timepoints.
- **Trajectory inference**: URD branched tree + diffusion pseudotime; Monocle3 cross-check.
- **Spatial mapping**: Tangram maps scRNA-seq cell types onto Slide-seq spatial pucks.
- **Lineage bifurcation analysis**: branch-point cells analyzed for differentially expressed regulators.
- **Mutant comparison**: healthy trajectory used as reference; mutant cells projected to identify divergence timepoint and lineage.

## 4. Key Results & Benchmarks

- All known cortical cell types recovered: apical/intermediate progenitors, Cajal-Retzius, CFuPN (CThPN, SCPN, layer 6b, near-projecting), CPN (layers 2/3, 5/6, stellate layer 4), interneurons (MGE, CGE, pallial-subpallial), OPCs, astrocytes, microglia, vascular.
- **Sequential interneuron invasion**: MGE-derived at E13.5, CGE-derived at E15.5, pallial-subpallial at E18.5.
- **Cell-fate branching**: glial/neuronal split visible at E13.5; PN subtypes diverge post-mitotically.
- **Radially ordered migration**: 5 substates of migrating excitatory neurons at E15.5 map to distinct radial positions via Slide-seq.
- **CPN layer 5/6 divergence**: perinatal molecular distinction between layer 5 and layer 6 CPNs.
- **Mutant mapping**: the healthy map localizes lineage-specific defects in aberrant corticogenesis.

## 5. Limitations & Future Work

- Mouse only; extrapolation to human cortex is indirect.
- Trajectories inferred from snapshots + pseudotime — not true lineage tracing.
- Post-mitotic diversification claim depends on the absence of fate-restricted progenitor signatures in transcriptomes; chromatin-level priming is not fully ruled out.
- Slide-seq v2 resolution limits cell-type assignment to Tangram mapping confidence.

## 6. Related Work

- Telley 2019 (FlashTag mouse cortical lineage), Yuzwa 2017 mouse cortex scRNA-seq — predecessors.
- Trevino 2020 human fetal cortex (chromatin) — human counterpart in spirit.
- Zhang 2025 PFC spatiotemporal — human prefrontal cortex counterpart.

## 7. Glossary

- **Apical progenitor (AP)**: radial glia at the ventricular surface; generate intermediate progenitors and neurons.
- **Intermediate progenitor (IP)**: basally located transit-amplifying cells; generate neurons.
- **CFuPN / CPN**: corticofugal vs. callosal projection neurons — two major PN classes.
- **URD**: trajectory inference method producing branched trees.
- **Tangram**: scRNA-seq → spatial transcriptomic mapping method.
- **Slide-seq v2**: high-resolution spatial transcriptomic technology.
