---
title: "RNA-seq analysis in seconds with GPU-accelerated kallisto"
authors: Melsted, Páll, Booeshaghi, A. Sina, Pachter, Lior
year: 2026
doi: 10.64898/2026.03.04.709526
source: melsted-2026-rna-seq-analysis-in-seconds.md
category: other
tags: [RNA-seq, GPU, kallisto, pseudoalignment, transcript-quantification, CUDA, EM]
---

## Summary

GPU-accelerated kallisto reimplements the full pseudoalignment pipeline — k-mer lookup, equivalence class (EC) intersection, and EM transcript quantification — on NVIDIA CUDA GPUs. A novel prefix-scan algorithm in shared memory solves the EC intersection bottleneck. On an RTX 5090, 295M reads are quantified in ~50 seconds vs. ~40 minutes on CPU (≈48× speedup), at 3.6M paired-end reads/second with identical quantification accuracy.

## Key Contributions

- Full GPU reimplementation of kallisto (k-mer hash lookup, EC intersection, EM)
- Novel GPU prefix-scan algorithm for EC intersection using shared memory
- 30-50× speedup; 3.6M paired-end reads/sec on RTX 5090
- bgzip-compressed FASTQ input required to prevent I/O bottleneck

## Methods & Architecture

Pseudoalignment assigns each read to an equivalence class (EC) — the intersection of transcript sets compatible with each k-mer. The CPU bottleneck is EC intersection (set operations on transcript lists). The GPU solution uses prefix-scan in shared memory: each thread handles one transcript in the intersection, and prefix-scan computes cumulative intersection sizes in parallel. The EM algorithm for abundance estimation is also parallelized across ECs. Benchmarked on RTX 5090 (Blackwell), RTX 4090 (Ada), and A100. Input must be bgzip-compressed to feed the GPU at full speed.

## Results

- 295M reads: 40 min (CPU) → 50 sec (GPU); ~48× speedup
- Throughput: 3.6M paired-end reads/sec (RTX 5090)
- Quantification accuracy: identical to CPU kallisto
- I/O bottleneck eliminated with bgzip input

## Limitations

- CUDA-only; no AMD/Intel GPU support
- bgzip pre-processing required for full performance
- Single-cell (STARsolo/kb-python) integration in progress; currently bulk RNA-seq
- Large genome indices may exceed consumer GPU VRAM

## Related Papers

- [[lrRNA/joglekar-2024]] — long-read RNA-seq; complementary to kallisto for short-read bulk quantification
- [[lrRNA/foord-2025]] — long-read transcriptomics; different sequencing modality but related RNA-seq pipeline context
