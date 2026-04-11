---
title: "Zero-shot prediction of drug response in cancer using a biologically interpretable deep learning model of transcription factor activity"
authors: Antonopoulos, Alexis S., Collins, Mark O.
year: 2026
doi: 10.1371/journal.pcbi.1014100
source: antonopoulos-2026-zero-shot-prediction-of-drug.md
category: drug-resistance
tags: [drug-response, phosphoproteomics, RNN, zero-shot, transcription-factors, signaling-networks]
---

## Summary

LEMBAS is a biologically-constrained recurrent neural network whose architecture mirrors a prior-knowledge signaling network. This paper extends LEMBAS to time-resolved phosphoproteomics by adding a phosphosite mapping layer and a monotonic time mapping layer, then uses simulated drug perturbations of the trained network to zero-shot predict cancer drug responses. TF activity signatures derived from network node states achieve Pearson r up to 0.79 on held-out drugs from GDSC2.

## Key Contributions

- Phosphosite mapping and monotonic time layers enable LEMBAS to ingest time-course phosphoproteomics data
- Zero-shot drug response prediction by perturbing network edges without drug-specific retraining
- Transcription factor activities as interpretable biomarkers linking signaling to drug sensitivity
- Discovery of non-canonical FOXO3:S7 modulation by the RAS inhibitor SHP099 via RAS→p38→PI3K crosstalk

## Methods & Architecture

The model encodes a prior-knowledge signaling network as an RNN: each node is a protein/kinase, each edge is a regulatory relationship. Phosphoproteomic measurements from EGF-stimulated MCF10A cells are mapped onto node activities via the phosphosite layer. The monotonic time mapping layer imposes temporal ordering on the RNN dynamics. After training on EGF data, drug effects are simulated by silencing or activating specific enzyme-substrate edges, producing predicted TF activity profiles. These TF profiles are then correlated with cell-line drug sensitivity (AUC) from GDSC2 for zero-shot response prediction.

## Results

- Zero-shot prediction Pearson r up to 0.79 for individual drugs (GDSC2 benchmark)
- Performance competitive with supervised models trained directly on cancer cell line data
- FOXO3:S7 identified as novel SHP099-responsive phosphosite, tracing RAS→p38→PI3K pathway
- Interpretable: specific signaling paths can be read off the RNN to explain TF activity changes

## Limitations

- Single-cell-line / single-stimulus training (MCF10A + EGF); cell-type generalizability untested
- Sparse phosphoproteomics coverage constrains the fraction of network nodes that can be activated
- Zero-shot transfer assumes conserved signaling topology between MCF10A and cancer cell lines

## Related Papers

- [[single-cell-dl/li-2025-uda-seq]] — domain adaptation for cross-condition generalization in single-cell data; complementary to zero-shot transfer approaches
- [[neuroscience/paulsen-2022]] — perturbation-based functional genomics; shared theme of gene/protein network perturbation
- [[genomic-dl/zemke-2023]] — regulatory genomics DL; interpretable neural architectures applied to biology
