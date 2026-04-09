---
title: "Organoid single-cell genomic atlas uncovers human-specific features of brain development"
authors: Sabina Kanton, Michael James Boyle, Zhisong He, Malgorzata Santel, Anne Weigert, Fátima Sanchís-Calleja, Patricia Guijarro, Leila Sidow, Jonas Simon Fleck, Dingding Han, Zhengzong Qian, Michael Heide, Wieland B. Huttner, Philipp Khaitovich, Svante Pääbo, Barbara Treutlein, J. Gray Camp
year: 2019
doi: 10.1038/s41586-019-1654-9
source: kanton-2019-organoid-single-cell-genomic.md
category: brain-development
tags: [organoid, human-specific, scRNA-seq, ATAC-seq, evolution, chimpanzee, neoteny, primate]
---

## Summary
Single-cell transcriptomic and chromatin accessibility atlas of human, chimpanzee, and macaque cerebral organoids from pluripotency to 4 months. Human neuronal maturation is slower (neoteny) relative to other primates. Human-specific gene expression is linked to divergent chromatin accessibility and persists into adult prefrontal cortex.

## Key Contributions
- Temporal scRNA-seq atlas of human organoid development (43,498 cells, 0–4 months)
- Human neuronal maturation slower than chimp/macaque; more astrocytes in chimp at 4 months
- Human-specific gene expression in distinct progenitor/neuron cell states in cortex
- ATAC-seq reveals human-chimp chromatin divergence correlating with human-specific expression
- Some human-specific patterns persist into adult prefrontal cortex (snRNA-seq validation)

## Methods & Architecture
scRNA-seq (10x) time course + force-directed graph; chimpanzee/macaque organoid comparison; time warping for pseudotime alignment; ATAC-seq chromatin accessibility; adult PFC snRNA-seq cross-validation.

## Results
- Each iPSC line contributes to multiple differentiation trajectories; gene expression patterns highly correlated across lines
- Human neurons at same timepoint are less mature than chimp neurons
- Chromatin accessibility divergence identified between human and chimpanzee in cortex

## Limitations
Organoids lack vasculature, microglia, complete lamination; brain-region composition varies across iPSC lines.

## Related Papers
- [[brain-development/gordon-2021-long-term-maturation-of]] — long-term maturation of hCS
