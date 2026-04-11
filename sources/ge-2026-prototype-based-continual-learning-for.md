---
title: "Prototype-based Continual Learning for Single-cell Annotation with scEvolver"
authors: Ge, Shuangshuang, Guo, Jinyun, Wang, Chong, Ding, Jun, Zhang, Yan
year: 2026
doi: 10.64898/2026.03.05.709973
category: single-cell-dl
pdf_path: papers/ge-2026-prototype-based-continual-learning-for.pdf
pdf_filename: ge-2026-prototype-based-continual-learning-for.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

scEvolver is a prototype-based continual learning framework built on a scGPT backbone with PEFT (LoRA+MoE), using memory-augmented prototypes and a hard-sample replay buffer to annotate new cell types without forgetting old ones — achieving +24.5% macro-F1 in 5-shot settings over next-best baseline.

## 1. Document Info
- Journal/Conference: bioRxiv preprint
- Received/Published: March 8, 2026 (DOI: 10.64898/2026.03.05.709973)

## 2. Key Contributions
- scEvolver: continual learning framework for single-cell annotation that incrementally learns new cell types across platforms, tissues, and modalities without catastrophic forgetting
- Memory-augmented prototypes (Mp): per-class prototype vectors augmented with uncertainty-weighted memory of past class distributions; prevent class boundary drift
- Hard-sample replay buffer: prioritizes difficult/ambiguous training examples for replay; more efficient than random replay in preventing forgetting
- MAPPL loss (Memory-Augmented Prototype-based Plasticity-stability Loss): balances learning new types (plasticity) vs. retaining old types (stability)
- Handles cross-platform, cross-tissue, and cross-modality (ATAC+RNA, ADT+RNA) annotation in a single framework

## 3. Methods & Architecture
- **Backbone**: scGPT pretrained transformer encoder; frozen during continual learning
- **PEFT**: Parameter-Efficient Fine-Tuning with LoRA (Low-Rank Adaptation) + MoE (Mixture of Experts) adapter modules; only adapters updated, backbone frozen — reduces forgetting
- **Prototypes**: for each cell type, maintain a prototype vector (weighted mean of cell embeddings); augmented with a memory component that retains a history of prototype positions
- **Replay buffer**: stores hard samples (high-entropy predictions, near-decision-boundary cells) from previous tasks; replayed during new task training
- **MAPPL loss**: combines cross-entropy for new types + prototype distillation loss (KL divergence between new and old prototype distributions) to enforce stability
- **5-shot setting**: only 5 labeled cells per new cell type at inference/adaptation time
- **Modalities**: tested on scRNA-seq, scATAC-seq (activity scores), CITE-seq (ADT + RNA)

## 4. Key Results & Benchmarks
- 5-shot cell type annotation: +24.5% macro-F1 on PANCREAS dataset vs. next-best baseline
- Consistently outperforms scGPT fine-tuning, EWC, LwF, and other continual learning baselines
- Cross-platform generalization (10x → Smart-seq2 and vice versa) maintained
- IBD gut dataset: discovers SF-like (spasmolytic polypeptide-expressing) metaplastic epithelial cells not annotated in original study
- Cross-modality: ATAC+RNA and ADT+RNA annotation competitive with modality-specific methods

## 5. Limitations & Future Work
- Depends on scGPT backbone quality; performance inherited from pretraining distribution
- Hard-sample replay buffer size fixed; may be insufficient for long task sequences
- 5-shot performance depends on prototype initialization quality
- Future: online continual learning (stream, not task-boundary); extension to spatial transcriptomics

## 6. Related Work
- scGPT (Cui et al., 2024) — backbone pretrained model; scEvolver extends and adapts it
- EWC (Elastic Weight Consolidation, Kirkpatrick et al.) — classic continual learning baseline; regularization-based
- LwF (Learning without Forgetting) — knowledge distillation-based continual learning baseline
- PEFT/LoRA (Hu et al.) — parameter-efficient fine-tuning; used as adaptation strategy
- scFoundation (Hao et al.) — alternative large-scale single-cell foundation model

## 7. Glossary
- **Continual learning**: machine learning paradigm where a model learns sequential tasks without forgetting previously learned tasks; also called lifelong learning or incremental learning
- **Catastrophic forgetting**: phenomenon where a neural network abruptly forgets previously learned information upon training on new data
- **Prototype**: representative embedding vector for a class, typically the (weighted) mean of all training examples in that class
- **LoRA (Low-Rank Adaptation)**: PEFT technique that adds low-rank trainable matrices to frozen pretrained weights; computationally efficient fine-tuning
- **MoE (Mixture of Experts)**: architecture where different expert subnetworks handle different input types; used here as adapter modules in PEFT
- **MAPPL loss**: Memory-Augmented Prototype-based Plasticity-stability Loss — scEvolver's custom loss function balancing new task learning vs. old task retention
- **5-shot learning**: few-shot setting where only 5 labeled examples per class are available for adaptation
- **IBD (Inflammatory Bowel Disease)**: autoimmune gut disease; scEvolver applied to gut scRNA-seq data from IBD patients
- **SF-like metaplastic cells**: spasmolytic polypeptide-expressing metaplastic epithelial cells; a rare cell type associated with inflammatory/metaplastic response in the gut
