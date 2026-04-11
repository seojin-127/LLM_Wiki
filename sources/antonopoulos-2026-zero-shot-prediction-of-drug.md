---
title: "Zero-shot prediction of drug response in cancer using a biologically interpretable deep learning model of transcription factor activity"
authors: Antonopoulos, Alexis S., Collins, Mark O.
year: 2026
doi: 10.1371/journal.pcbi.1014100
category: drug-resistance
pdf_path: papers/antonopoulos-2026-zero-shot-prediction-of-drug.pdf
pdf_filename: antonopoulos-2026-zero-shot-prediction-of-drug.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

LEMBAS-extended recurrent neural network models time-resolved phosphoproteomic signaling to zero-shot predict cancer drug responses via transcription factor activity, achieving Pearson r up to 0.79 on held-out drugs.

## 1. Document Info
- Journal/Conference: PLOS Computational Biology
- Received/Published: Published March 18, 2026 (DOI: 10.1371/journal.pcbi.1014100)

## 2. Key Contributions
- Extends the LEMBAS (biologically-informed RNN) framework to time-resolved phosphoproteomics by adding a phosphosite mapping layer and monotonic time mapping layer
- Demonstrates zero-shot generalization: models trained on EGF-stimulated MCF10A cells predict drug responses for unseen drugs using network perturbation simulations
- Identifies transcription factor (TF) activity signatures as informative biomarkers of drug response at the signaling level
- Uncovers non-canonical FOXO3:S7 modulation by SHP099 (a RAS inhibitor) via RAS→p38→PI3K crosstalk, confirmed by network analysis

## 3. Methods & Architecture
- **Base model**: LEMBAS (Logical and Explainable Model Based on Attention and Signaling) — a recurrent neural network with architecture constrained by a prior knowledge signaling network
- **Phosphosite mapping layer**: maps phosphoproteomics measurements onto network node activities
- **Monotonic time mapping layer**: ensures temporal ordering of signaling dynamics
- **Training data**: EGF stimulation time-course phosphoproteomics in MCF10A breast epithelial cells
- **Zero-shot inference**: drug effects simulated by perturbing network edges (enzyme-substrate relationships) without retraining; no drug-specific data used
- **Downstream**: TF activities inferred from RNN node states; correlated against GDSC2 drug sensitivity (AUC) across cancer cell lines

## 4. Key Results & Benchmarks
- Zero-shot drug response prediction: Pearson r up to 0.79 for some drugs (GDSC2 benchmark)
- Performance competitive with supervised models that use cancer cell line data directly
- Discovery of FOXO3:S7 as a novel non-canonical target modulated by SHP099
- Model interpretability: specific signaling paths traceable from drug perturbation to TF output

## 5. Limitations & Future Work
- Training limited to a single cell line/stimulus (MCF10A + EGF); generalizability across cell types uncertain
- Phosphosite coverage depends on available experimental data; sparse phosphoproteomics limit network node activation
- Zero-shot transfer to cancer cells assumes conserved signaling topology
- Future: multi-cell-line training, integration with transcriptomics for broader coverage

## 6. Related Work
- LEMBAS original (Morris et al.) — biological RNN constrained by signaling prior knowledge
- GDSC2 (Garnett et al.) — drug sensitivity database used for benchmarking
- NCI-60 pharmacogenomics — related drug response prediction frameworks
- DeepSynergy, DRPreter — supervised drug response prediction models

## 7. Glossary
- **LEMBAS**: Logical and Explainable Model Based on Attention and Signaling — a biologically-informed RNN whose architecture mirrors a prior knowledge signaling network
- **Phosphoproteomics**: large-scale measurement of protein phosphorylation states, used to map kinase-substrate signaling activity
- **Zero-shot prediction**: applying a trained model to a new task/condition without task-specific training examples
- **Transcription factor (TF) activity**: inferred activity level of transcription factors based on upstream signaling node states in the RNN
- **SHP099**: a RAS inhibitor (SHP2 phosphatase inhibitor) used as a drug perturbation example
- **FOXO3:S7**: non-canonical phosphorylation site on FOXO3 transcription factor identified as a drug response biomarker
- **GDSC2**: Genomics of Drug Sensitivity in Cancer 2 — large pharmacogenomics dataset
