---
title: "Predicting transcriptional outcomes of novel multigene perturbations with GEARS"
authors: Yusuf Roohani, Kexin Huang, Jure Leskovec
year: 2023
doi: 10.1038/s41587-023-01905-6
category: single-cell-dl
pdf_path: papers/roohani-2023-predicting-transcriptional-outcomes-of.pdf
pdf_filename: roohani-2023-predicting-transcriptional-outcomes-of.pdf
source_collection: manual
---

## One-line Summary

GEARS integrates deep learning with gene–gene knowledge graphs to predict transcriptional responses to single and combinatorial genetic perturbations, including combinations involving genes never experimentally perturbed.

## 1. Document Info
- Journal: Nature Biotechnology
- Received: 9 July 2022
- Accepted: 12 July 2023
- Published: 17 August 2023

## 2. Key Contributions

- Introduces GEARS (Graph-Enhanced Gene Activation and Repression Simulator), the first method capable of predicting outcomes of multigene perturbation combinations involving genes with no prior experimental perturbation data
- Incorporates biological prior knowledge via two knowledge graphs: gene coexpression graph (for gene embeddings) and Gene Ontology (GO)-derived graph (for perturbation embeddings)
- Achieves 40% higher precision than existing approaches in predicting four distinct genetic interaction subtypes from combinatorial perturbation screens
- Identifies the strongest genetic interactions twice as well as prior approaches
- Provides uncertainty quantification via Bayesian formulation, inversely correlated with model performance

## 3. Methods & Architecture

### Problem Formulation
- Input: unperturbed single-cell gene expression vector g ∈ ℝ^K + perturbation set P = {P1, ..., PM}
- Output: predicted post-perturbation gene expression vector
- M = 0 for unperturbed cells; M ≥ 1 for single or combinatorial perturbations

### Architecture Components
1. **Gene coexpression graph encoder**: Represents each gene as a learnable embedding x^gene ∈ ℝ^d. Builds coexpression graph G_gene using Pearson correlation (top-H neighbors above threshold δ). GNN propagates information between coexpressed genes.

2. **GO-based perturbation graph encoder**: Constructs perturbation similarity graph G_pert from Gene Ontology. Computes Jaccard index between gene pathway sets. GNN learns perturbation embeddings that capture pathway-level similarity, enabling generalization to unseen perturbations.

3. **Compositional perturbation module**: Combines perturbation embeddings with gene embeddings for each perturbation in the set. Handles multi-gene perturbation sets.

4. **Cross-gene decoder**: Takes set of perturbed gene embeddings across all K genes → predicts post-perturbation gene expression vector. Captures transcriptome-wide interactions.

5. **Autofocus direction-aware loss**: Custom loss function for training.

### Key Design Principles
- Two biological intuitions: (i) coexpressed genes respond similarly to perturbations; (ii) genes in similar pathways perturb similar downstream targets
- Graph-based inductive bias via GNN enables generalization to unseen genes
- Dual embedding (gene + perturbation) provides expressivity for gene-specific heterogeneity

## 4. Key Results & Benchmarks

### Datasets
- Replogle et al. RPE-1 cells: 1,543 perturbations, >170,000 cells
- Replogle et al. K562 cells: 1,092 perturbations, >170,000 cells
- Norman et al. combinatorial screen: two-gene perturbation combinations

### Single-gene Perturbation
- Evaluated on held-out genes never seen perturbed during training
- Outperformed baselines: CPA, no-perturbation model, CellOracle-adapted GRN model

### Combinatorial (Two-gene) Perturbation
- Three generalization scenarios: (1) both genes seen individually, (2) one gene seen + one unseen, (3) both genes unseen
- >30% improvement across all cases; 53% improvement when both genes unseen
- 50% greater enrichment in top differentially expressed genes vs. baselines
- Correctly captured direction and magnitude of perturbation effects (e.g., FOSB + CEBPB example: all 20 DE genes predicted correctly)

### Genetic Interaction Detection
- Predicts five genetic interaction subtypes
- 40% higher precision than existing methods for four subtypes
- Identifies strongest interactions 2× better than prior approaches

### Limitations
- Performance depends on knowledge graph connectivity — poorly connected genes in GO graph yield lower accuracy
- Uncertainty metric helps flag unreliable predictions (Bayesian formulation)

## 5. Limitations & Future Work

- Limited by completeness of knowledge graphs (GO, coexpression); genes poorly connected in the graph are harder to predict
- Currently focused on CRISPR knockout; extension to other perturbation modalities (CRISPRi, CRISPRa, epigenome editing) is future work
- Potential applications: designing perturbational experiments, cell engineering, regenerative medicine, aging reversal, combination therapy design
- Could incorporate larger context-specific networks for improved performance on specific gene sets

## 6. Related Work

- scGen (Lotfollahi et al., 2019) — VAE-based single-cell perturbation prediction
- CPA (Lotfollahi et al., 2023) — compositional perturbation autoencoder
- CellOracle (Kamimoto et al., 2023) — GRN-based in silico perturbation
- SCENIC (Aibar et al., 2017) — GRN inference from single-cell data
- Norman et al. (2019) — combinatorial Perturb-seq screen dataset
- Replogle et al. (2022) — genome-scale Perturb-seq
- Dixit et al. (2016) — original Perturb-seq method
- Fleck et al. (2022) — perturbation in brain organoids

## 7. Glossary

- **GEARS**: Graph-Enhanced Gene Activation and Repression Simulator
- **Perturb-seq**: Pooled CRISPR screen + single-cell RNA-seq readout
- **GNN**: Graph Neural Network — propagates information along graph edges
- **Gene Ontology (GO)**: Hierarchical ontology of gene functions and pathways
- **Genetic interaction**: Non-additive effect when multiple genes are perturbed simultaneously
- **Combinatorial perturbation**: Simultaneous perturbation of two or more genes
- **Inductive bias**: Structural assumptions built into the model (here, graph-based gene relationships)
- **Jaccard index**: Set similarity metric |A∩B| / |A∪B|
