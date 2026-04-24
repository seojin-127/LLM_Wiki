---
title: "Predicting transcriptional outcomes of novel multigene perturbations with GEARS"
authors: Yusuf Roohani, Kexin Huang, Jure Leskovec
year: 2023
doi: 10.1038/s41587-023-01905-6
source: roohani-2023-predicting-transcriptional-outcomes-of.md
category: single-cell-dl
tags: [perturbation-prediction, combinatorial-perturbation, GNN, knowledge-graph, Perturb-seq, CRISPR, gene-interaction, Gene-Ontology]
---

## Summary

GEARS (Graph-Enhanced Gene Activation and Repression Simulator) is the first deep learning method that can predict transcriptional outcomes of combinatorial genetic perturbations, including combinations where one or both genes have never been experimentally perturbed. It achieves this by integrating two biological knowledge graphs — a gene coexpression graph and a Gene Ontology-derived pathway similarity graph — into a GNN-based architecture, enabling inductive generalization to unseen perturbations.

## Key Contributions

- First method to predict multigene perturbation outcomes for genes with **no prior experimental perturbation data**
- Dual knowledge graph architecture: gene coexpression (for gene embeddings) + GO pathway similarity (for perturbation embeddings)
- 40% higher precision in detecting four genetic interaction subtypes; 2× better at identifying the strongest interactions
- >30% improvement over baselines across all combinatorial generalization scenarios (both-seen, one-unseen, both-unseen)
- Bayesian uncertainty quantification flags unreliable predictions for poorly connected genes

## Methods & Architecture

### Inputs and Outputs
- **Input**: unperturbed gene expression vector (K genes) + perturbation set {P1, ..., PM}
- **Output**: predicted post-perturbation gene expression vector

### Model Components

1. **Gene coexpression graph encoder** — builds graph from Pearson correlations between genes; GNN propagates embeddings among coexpressed neighbors → captures response heterogeneity

2. **GO perturbation graph encoder** — builds gene similarity graph from Jaccard index of GO pathway annotations; GNN on perturbation embeddings → enables generalization to genes never perturbed before (key innovation)

3. **Compositional perturbation module** — sequentially combines each perturbation embedding with every gene embedding → handles arbitrary-size perturbation sets

4. **Cross-gene decoder** — maps all K perturbed gene embeddings → post-perturbation expression; captures transcriptome-wide effects

5. **Autofocus direction-aware loss** — custom training objective

### Why It Works for Unseen Genes
The GO graph provides inductive bias: if gene A shares pathways with previously perturbed gene B, A's perturbation embedding inherits information from B through GNN message passing. This is the core mechanism enabling zero-shot combinatorial prediction.

## Results

### Datasets
- Replogle et al. genome-scale Perturb-seq: RPE-1 (1,543 perturbations) and K562 (1,092 perturbations), >170K cells each
- Norman et al. combinatorial screen: two-gene perturbation combinations

### Benchmarks
| Scenario | Improvement over baselines |
|----------|---------------------------|
| Both genes seen individually | >30% |
| One seen + one unseen | >30% |
| Both genes unseen | **53%** (highest) |
| Genetic interaction detection | 40% higher precision |
| Top DE gene enrichment | 50% greater enrichment |

### Baselines Compared
- CPA (Lotfollahi et al., 2023)
- No-perturbation model
- CellOracle-adapted GRN linear propagation

## Limitations

- Performance depends on knowledge graph connectivity — genes poorly connected in GO graph yield lower prediction accuracy
- Currently limited to CRISPR knockout; CRISPRi/CRISPRa/epigenome editing not yet supported
- Linear scaling of perturbation set composition may miss higher-order non-linear interactions
- Knowledge graphs (GO, coexpression) are incomplete and context-dependent; alternative graphs may improve domain-specific predictions

## Related Papers

- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle: GRN-based in silico perturbation (used as baseline)
- [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] — Squidiff: diffusion model for perturbation prediction (cites GEARS as baseline)
- [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]] — PerturBERT: BERT-based perturbation foundation model (benchmarks against GEARS)
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT: foundation model with perturbation prediction task
- [[single-cell-foundation/hao-2024-large-scale-foundation-model]] — scFoundation: perturbation prediction as downstream task
- [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] — TRADE: quantifying perturbation effect sizes from Perturb-seq
- [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]] — MrVI: sample-level perturbation stratification
- [[drug-resistance/alsulami-2026-predicting-and-interpreting-cell]] — drug perturbation prediction (cites GEARS)
- [[brain-development/fleck-2023-inferring-perturbing-cell-fate]] — perturbation in brain organoids (cited by GEARS)
