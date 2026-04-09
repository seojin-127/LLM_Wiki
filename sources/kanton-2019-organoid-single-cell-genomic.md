---
title: "Organoid single-cell genomic atlas uncovers human-specific features of brain development"
authors: Sabina Kanton, Michael James Boyle, Zhisong He, Malgorzata Santel, Anne Weigert, Fátima Sanchís-Calleja, Patricia Guijarro, Leila Sidow, Jonas Simon Fleck, Dingding Han, Zhengzong Qian, Michael Heide, Wieland B. Huttner, Philipp Khaitovich, Svante Pääbo, Barbara Treutlein, J. Gray Camp
year: 2019
doi: 10.1038/s41586-019-1654-9
category: brain-development
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/0222100246/Kanton-2019-Organoid single-cell genomic atlas.pdf
pdf_filename: Kanton-2019-Organoid single-cell genomic atlas.pdf
source_collection: endnote
---

## One-line Summary
Single-cell transcriptomic and chromatin accessibility atlas of human, chimpanzee, and macaque cerebral organoids reveals human-specific slower neuronal maturation, distinct chromatin accessibility divergence, and human-specific gene expression persisting into adulthood.

## 1. Document Info
- Journal/Conference: Nature
- Published: 17 October 2019 (Vol. 574)

## 2. Key Contributions
- Generated scRNA-seq atlas of human organoid development from pluripotency to 4 months (43,498 cells); identified differentiation trajectories across forebrain, midbrain, hindbrain
- Compared human, chimpanzee, and macaque organoids; human neuronal development is slower (neoteny)
- Identified human-specific gene expression in distinct cell states along progenitor-to-neuron lineages in cortex
- Chromatin accessibility profiling revealed human-chimpanzee divergence correlated with human-specific gene expression and genetic changes
- Mapped human-specific expression in adult prefrontal cortex via snRNA-seq; some differences persist into adulthood

## 3. Methods & Architecture
- scRNA-seq (10x Genomics) time course: H9 ESC + iPSC (409b2); 0–4 months
- Force-directed k-nearest neighbour graph for temporal visualization
- Chimpanzee and macaque organoid generation + scRNA-seq (36,884 cells for chimp)
- Time warping to align human-chimp pseudotime trajectories
- ATAC-seq for chromatin accessibility; comparison of human vs chimpanzee accessibility
- snRNA-seq of adult human prefrontal cortex for cross-validation

## 4. Key Results & Benchmarks
- Human organoids recapitulate forebrain, midbrain, hindbrain, retina progenitor fates
- Chimpanzee neurons express higher levels of maturation genes at same timepoints; more astrocytes at 4 months
- Human-specific gene expression resolves to distinct progenitor and neuron cell states in cortex
- Chromatin accessibility divergence between human and chimpanzee correlates with human-specific expression
- Some human-specific gene expression patterns persist into adult prefrontal cortex

## 5. Limitations & Future Work
- Organoids lack vascularization, microglia, and complete lamination; miss some in vivo features
- Brain-region composition varies across iPSC lines
- Limited to early stages; longer culture needed for mature neuron phenotypes

## 6. Related Work
- Cerebral organoid model: Lancaster et al. 2013 (Nature)
- Human-specific brain development: Geschwind & Rakic 2013
- Primate scRNA-seq comparisons: Sousa et al. 2017, Zhu et al. 2018

## 7. Glossary
- **Neoteny**: Retention of juvenile features; here, slower maturation of human neurons relative to other primates
- **Pseudotime**: Computational ordering of cells along developmental trajectory
- **ATAC-seq**: Assay for Transposase-Accessible Chromatin — maps open chromatin regions
- **iPSC**: Induced pluripotent stem cell
- **NPC**: Neural progenitor cell
