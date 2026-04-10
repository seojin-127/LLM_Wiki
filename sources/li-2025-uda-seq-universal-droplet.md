---
title: "UDA-seq: universal droplet microfluidics-based combinatorial indexing for massive-scale multimodal single-cell sequencing"
authors: Yun Li, Zheng Huang, Lubin Xu, Yanling Fan, Jun Ping, Guochao Li, Yanjie Chen, Chengwei Yu, Qifei Wang, Turun Song, Tao Lin, Mengmeng Liu, Yangqing Xu, Na Ai, Xini Meng, Qin Qiao, Hongbin Ji, Zhen Qin, Shuo Jin, Nan Jiang, Minxian Wang, Shaokun Shu, Feng Zhang, Weiqi Zhang, Guang-Hui Liu, Limeng Chen, Lan Jiang
year: 2025
doi: 10.1038/s41592-024-02586-y
category: single-cell-dl
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/1513783380/Li-2025-UDA-seq_ universal droplet microfluidi.pdf
pdf_filename: Li-2025-UDA-seq_ universal droplet microfluidi.pdf
source_collection: endnote
---

## One-line Summary
UDA-seq is a universal post-indexing workflow for droplet microfluidics that adapts any existing single-cell multimodal method for massive-scale throughput, enabling RNA+VDJ, RNA+ATAC, and RNA+CRISPR co-assays on 100K+ cells from clinical specimens in a single experiment.

## 1. Document Info
- Journal/Conference: Nature Methods
- Published: June 2025

## 2. Key Contributions
- Universal post-indexing step added to any droplet-based single-cell multimodal protocol to greatly increase throughput and automation
- Benchmarked across RNA+VDJ, RNA+ATAC, RNA+CRISPR perturbation modality combinations
- Demonstrated at clinical scale: 100K+ high-quality cells from 3 dozen frozen clinical biopsy specimens in a single experiment
- Identifies rare cell subpopulations associated with clinical phenotypes; applied to cancer vulnerability analysis

## 3. Methods & Architecture
- Adds a universal post-indexing step to existing droplet microfluidics platforms (e.g., 10x Genomics)
- Combinatorial indexing for increased cell throughput without per-well reagents
- Benchmarked on multiple tissue types and species
- Downstream: standard scRNA-seq + modality-specific analysis pipelines

## 4. Key Results & Benchmarks
- >100K high-quality single-cell multimodal profiles from 36 frozen clinical biopsies in 1 experiment
- RNA+ATAC: well-clustered joint representations matching reference atlases
- Rare cell type detection: clinical subpopulations not identified by single-modality approaches
- Cost and scalability advantages vs. standard combinatorial methods

## 5. Limitations & Future Work
- Post-indexing step adds handling complexity; optimization needed per modality
- Frozen clinical biopsies: cell quality varies; batch effects from clinical specimens
- Currently validated for specific modality pairs; generalization to new modalities requires adaptation

## 6. Related Work
- 10x Multiome: standard RNA+ATAC platform (UDA-seq extends this)
- Schuster et al. 2024 (multiDGD): deep generative model for multi-omics analysis
- SHARE-seq, SNARE-seq: earlier combinatorial indexing approaches

## 7. Glossary
- **Combinatorial indexing**: Uses multiple sequential barcoding steps to label cells without physical isolation
- **Post-indexing**: Adding barcodes after droplet encapsulation to increase throughput
- **VDJ**: V(D)J recombination sequencing — immune receptor diversity profiling
- **CRISPR co-assay**: Simultaneous sequencing of guide RNA identity + transcriptome for pooled screens
