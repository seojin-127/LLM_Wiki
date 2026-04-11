---
title: "Reference-based analysis of lung single-cell sequencing reveals a transitional profibrotic macrophage"
authors: Aran, Dvir, Looney, Agnieszka P., Liu, Leqian, Wu, Esther, Fong, Valerie, Hsu, Austin, Chak, Suzanna, Naikawadi, Ram P., Wolters, Paul J., Abate, Adam R., Butte, Atul J., Bhattacharya, Mallar
year: 2019
doi: 10.1038/s41590-018-0276-y
category: single-cell-dl
pdf_path: papers/aran-2019-reference-based-analysis-of.pdf
pdf_filename: aran-2019-reference-based-analysis-of.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

SingleR automates scRNA-seq cell type annotation by correlating single-cell transcriptomes to bulk RNA-seq reference datasets of pure cell types via iterative Spearman correlation, enabling unbiased reference-based annotation; applied here to discover profibrotic transitional macrophages in lung fibrosis.

## 1. Document Info
- Journal/Conference: Nature Immunology
- Received/Published: Published February 2019 (DOI: 10.1038/s41590-018-0276-y)

## 2. Key Contributions
- SingleR: reference-based annotation tool using iterative Spearman correlation between single-cell and bulk transcriptome references (ImmGen for mouse; ENCODE/Blueprint for human)
- Unbiased, automated cell type labeling without subjective manual marker gene selection
- Applied to bleomycin-induced lung fibrosis in mice: discovers transitional macrophages (CX3CR1+SiglecF+) with gene expression intermediate between monocyte-derived and alveolar macrophages
- Transitional macrophages localize to fibrotic niche and drive fibroblast proliferation via Pdgf-aa

## 3. Methods & Architecture
- **Input**: single-cell gene expression matrix + reference bulk transcriptome dataset (pure cell types)
- **Step 1**: compute Spearman correlation between each cell and each cell type in the reference using variable genes
- **Step 2**: iterative refinement — retain top-scoring cell types + recompute with variable genes among those types only
- **Repeat** until one cell type remains per cell
- **Reference databases**: ImmGen (mouse immune cells), ENCODE + Blueprint Epigenomics (human)
- **Output**: cell type label per cell; correlation scores as confidence metric
- **Subclustering extension**: SingleR correlations used as a distance matrix for hierarchical clustering within a broadly defined cell type

## 4. Key Results & Benchmarks
- Correctly identifies macrophage vs. DC identity in BMDC/fibroblast culture experiments; corrects prior misclassification
- Discovers scar-associated macrophages (SAMs): CX3CR1+SiglecF+ transitional population absent in healthy lung
- SAMs localize to fibrotic niche; depletion prevents lung fibrosis in vivo
- SAMs are Pdgf-aa source → fibroblast proliferation (myeloid-mesenchymal crosstalk)
- Human ortholog genes of SAMs upregulated in IPF patient samples

## 5. Limitations & Future Work
- Performance depends on quality and completeness of reference datasets; cell types absent from reference cannot be annotated
- Bulk reference transcriptomes may not resolve closely related cell states defined at single-cell resolution
- No uncertainty quantification beyond correlation scores
- Iterative refinement can be slow for very large cell type references
- Later versions: SingleR Bioconductor package (Aran et al., F1000Research 2019)

## 6. Related Work
- CellTypist (Dominguez Conde et al., 2022) — logistic regression-based annotation; faster, requires dedicated training
- scANVI (Xu et al., 2021) — VAE-based annotation with probabilistic uncertainty
- popV (Ergen et al., 2024) — ensemble voting annotation including SingleR as a component
- Seurat label transfer — anchor-based annotation; complementary approach

## 7. Glossary
- **SingleR**: Single-cell Recognition — the annotation method; correlates scRNA-seq to bulk reference
- **Spearman correlation**: rank-based correlation; robust to outliers; measures similarity between single-cell and reference profiles
- **ImmGen**: Immunological Genome Project — comprehensive database of mouse immune cell bulk RNA-seq profiles; used as SingleR reference
- **Transitional macrophage / SAM**: scar-associated macrophage with intermediate transcriptome between monocyte and alveolar macrophage; the key biological discovery
- **Pdgf-aa**: platelet-derived growth factor; mitogen secreted by SAMs driving fibroblast proliferation
- **IPF**: idiopathic pulmonary fibrosis — severe lung disease; human SAM orthologs elevated in IPF patients
- **Blueprint / ENCODE**: human bulk RNA-seq reference databases used by SingleR for human cell type annotation
