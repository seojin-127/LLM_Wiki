---
title: "Reference-based analysis of lung single-cell sequencing reveals a transitional profibrotic macrophage"
authors: Aran, Dvir, Looney, Agnieszka P., Liu, Leqian, Wu, Esther, Fong, Valerie, Hsu, Austin, Chak, Suzanna, Naikawadi, Ram P., Wolters, Paul J., Abate, Adam R., Butte, Atul J., Bhattacharya, Mallar
year: 2019
doi: 10.1038/s41590-018-0276-y
source: aran-2019-reference-based-analysis-of.md
category: single-cell-dl
tags: [SingleR, annotation, reference-based, Spearman, macrophage, fibrosis, lung]
---

## Summary

SingleR annotates scRNA-seq cells by iteratively correlating single-cell transcriptomes to bulk RNA-seq references (ImmGen for mouse; ENCODE/Blueprint for human) via Spearman correlation, refining the comparison to the most similar cell types at each step. The method enables unbiased, automated annotation without manual marker curation. Applied here to lung fibrosis, it discovers CX3CR1+SiglecF+ transitional macrophages that localize to the fibrotic niche and drive fibroblast proliferation via Pdgf-aa.

## Key Contributions

- SingleR: iterative Spearman correlation against bulk transcriptome references; no supervised training required
- Validated on mouse (ImmGen) and human (ENCODE, Blueprint) reference databases
- Corrects a prior misclassification: BMDC-culture cells incorrectly labeled as DCs by flow cytometry → macrophages by SingleR
- Biological discovery: scar-associated macrophages (SAMs) required for lung fibrosis; depletion prevents fibrosis; Pdgf-aa myeloid-mesenchymal crosstalk mechanism

## Methods & Architecture

For each cell: compute Spearman correlation against all samples in the reference using variable genes; retain top cell types; re-compute Spearman using only genes variable among top types; repeat until one type remains. SingleR correlation scores also used as a distance matrix for hierarchical subclustering within broad cell types (macrophage subcluster discovery).

## Results

- Accurate annotation on BMDC, PBMC, and lung cell datasets; corrects flow cytometry labels
- Discovers SAMs: CX3CR1+SiglecF+ transitional macrophage unique to fibrotic lung
- SAM depletion prevents bleomycin-induced fibrosis in mice
- Human IPF: SAM ortholog genes upregulated in patient samples

## Limitations

- Limited by reference completeness; cell types absent from bulk reference cannot be annotated
- Bulk references may not resolve fine-grained single-cell-level cell states
- Computationally slow for large references; later Bioconductor package addressed this

## Related Papers

- [[single-cell-dl/dominguez-conde-2022-cross-tissue-immune-cell]] — CellTypist: logistic regression annotation; faster and scalable alternative
- [[single-cell-dl/ergen-2024-consensus-prediction-cell]] — popV: ensemble including SingleR as one component
- [[single-cell-dl/xu-2021-probabilistic-harmonization-and]] — scANVI: probabilistic annotation with uncertainty; complementary
