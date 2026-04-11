---
title: "RNA-seq analysis in seconds with GPU-accelerated kallisto"
authors: Melsted, Páll, Booeshaghi, A. Sina, Pachter, Lior
year: 2026
doi: 10.64898/2026.03.04.709526
category: other
pdf_path: papers/melsted-2026-rna-seq-analysis-in-seconds.pdf
pdf_filename: melsted-2026-rna-seq-analysis-in-seconds.pdf
source_collection: desktop-upload-2026-04-11
---

## One-line Summary

GPU-accelerated kallisto reimplements pseudoalignment, EC intersection (prefix-scan + shared memory), and EM transcript quantification on NVIDIA GPUs, achieving 30-50× speedup over CPU kallisto (295M reads: 40 minutes → 50 seconds) at 3.6M paired-end reads/sec.

## 1. Document Info
- Journal/Conference: bioRxiv preprint
- Received/Published: March 6, 2026 (DOI: 10.64898/2026.03.04.709526)

## 2. Key Contributions
- Full GPU reimplementation of kallisto's pseudoalignment pipeline, including k-mer lookup, equivalence class (EC) intersection, and EM transcript abundance estimation
- Novel EC intersection algorithm using GPU prefix-scan and shared memory, replacing the CPU-side set-intersection bottleneck
- 30-50× speedup over CPU kallisto on standard RNA-seq datasets; 295M reads processed in 50 seconds (vs. ~40 minutes on CPU)
- Throughput: 3.6M paired-end reads/second on an NVIDIA GeForce RTX 5090 (Blackwell architecture)
- Practical note: bgzip-compressed input needed to avoid I/O becoming the bottleneck

## 3. Methods & Architecture
- **Pseudoalignment**: k-mer lookup into a compact hash index; for each read, identifies the set of transcripts compatible with all k-mers → equivalence class (EC)
- **GPU k-mer hashing**: parallel hash table lookups per read fragment; thousands of reads processed concurrently
- **EC intersection**: novel prefix-scan algorithm on GPU shared memory to intersect k-mer-level transcript sets into per-read ECs efficiently; avoids global memory bandwidth bottleneck of CPU approach
- **EM algorithm**: GPU-parallelized expectation-maximization for estimating transcript-level abundances (TPM/estimated counts) from EC-count matrix
- **Hardware**: benchmarked on NVIDIA GeForce RTX 5090 (Blackwell, 2025); also tested on RTX 4090 (Ada) and A100
- **I/O**: standard FASTQ I/O is the bottleneck; bgzip + parallel decompression required to feed GPU at full throughput

## 4. Key Results & Benchmarks
- 295M reads: ~40 minutes (CPU kallisto) → ~50 seconds (GPU kallisto) — ~48× speedup
- 3.6M paired-end reads/second sustained throughput (RTX 5090)
- Quantification accuracy identical to CPU kallisto (same pseudoalignment index, same EM)
- I/O-bound without bgzip; with bgzip input, GPU compute is the bottleneck

## 5. Limitations & Future Work
- Requires NVIDIA GPU (CUDA); not portable to AMD/Intel GPUs or CPU-only systems
- bgzip compression of input FASTQ required for full performance (pre-processing step)
- Currently benchmarked on bulk RNA-seq; single-cell (STARsolo, kb-python) integration in progress
- Memory capacity limits index size for very large reference genomes on consumer GPUs

## 6. Related Work
- kallisto (Bray et al., 2016) — original CPU pseudoalignment tool; this paper is the GPU successor
- STAR (Dobin et al., 2013) — full read alignment RNA-seq tool; different approach from pseudoalignment
- Salmon (Patro et al., 2017) — quasi-mapping + EM; complementary transcript quantification approach
- kb-python / bustools — single-cell extension of kallisto

## 7. Glossary
- **Pseudoalignment**: lightweight RNA-seq read assignment that determines transcript compatibility via k-mer matching without full read alignment; orders of magnitude faster than full alignment
- **Equivalence class (EC)**: the set of transcripts compatible with all k-mers in a read; the basic unit of kallisto's counting step
- **EM (Expectation-Maximization)**: iterative algorithm for estimating transcript abundance from multi-mapping reads; alternates between assigning reads to transcripts (E-step) and updating abundance estimates (M-step)
- **Prefix-scan**: parallel algorithm on GPU for computing running totals across an array; used here for efficient EC intersection
- **bgzip**: block-compressed gzip format (BGZF) supporting random access and parallel decompression; preferred for GPU I/O
- **RTX 5090**: NVIDIA GeForce RTX 5090, Blackwell architecture (GB202 die), released 2025; highest-end consumer GPU
- **TPM**: Transcripts Per Million — normalized unit of transcript abundance in RNA-seq
