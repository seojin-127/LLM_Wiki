---
title: "Mapping convergent regulators of melanoma drug resistance by PerturbFate"
authors: Zihan Xu, Ziyu Lu, Aileen Ugurbil, Abdulraouf Abdulraouf, Andrew Liao, Jianxiang Zhang, Wei Zhou, Junyue Cao
year: 2026
doi: 10.1038/s41586-026-10367-0
source: xu-2026-mapping-convergent-regulators-of.md
category: drug-resistance
tags: [PerturbFate, CRISPRi, multimodal, melanoma, vemurafenib, drug-resistance, nascent-RNA, ATAC, combinatorial-indexing, GRN, convergent-regulation, Mediator-complex, dedifferentiation]
---

## Summary

PerturbFate is a scalable CRISPRi screening platform that simultaneously captures chromatin accessibility, nascent transcription, steady-state transcriptome, and sgRNA identities from the same single cell. Applied to >300,000 melanoma cells with >140 perturbations, it reveals that functionally diverse genetic perturbations converge on a shared dedifferentiated cell state driving vemurafenib resistance, governed by a cooperative TF hub (FOSL1, KLF5, RREB1, SMAD3). Combinatorial disruption of this hub neutralized resistance across diverse perturbations.

## Key Contributions

- **Multimodal Perturb-seq**: first platform to simultaneously profile ATAC + nascent RNA + steady-state RNA + sgRNA in the same cell at scale (>300K cells)
- **Convergent resistance mechanism**: >140 functionally diverse perturbations converge on a shared dedifferentiated state via cooperative TF activities
- **Mediator complex dissection**: module-specific mechanisms (kinase vs tail) drive resistance through distinct paths but converge on YAP-mediated transcription
- **Therapeutic target validation**: combinatorial inhibition of RREB1 + SMAD3 + KLF5 reduces resistance 3.1-fold across diverse perturbations
- **Nascent RNA enables RNA velocity**: metabolic labeling replaces splicing-based velocity with direct nascent/mature separation → more accurate state transition inference

## Methods & Architecture

### What Makes PerturbFate Different from Standard Perturb-seq?

```
Standard Perturb-seq (Dixit 2016, Replogle 2022):
  CRISPRi/KO → scRNA-seq readout only
  → Sees: what genes are expressed after perturbation
  → Misses: chromatin changes, transcription dynamics

PerturbFate:
  CRISPRi → ATAC + nascent RNA + steady-state RNA + sgRNA
  → Sees: chromatin opening → new transcription → accumulated mRNA
  → Captures the full regulatory cascade in one cell
```

### Multimodal Readout Explained

```
                        Time →
Gene regulation:  Chromatin opens → TF binds → Nascent RNA made → Steady-state mRNA accumulates
                       ↑               ↑              ↑                    ↑
PerturbFate reads:   ATAC          (inferred       5-EU labeled         Unlabeled
                   (Tn5 tagment.)  from ATAC       RNA (1hr pulse)     RNA
                                   motif analysis)
```

This temporal ordering within a single cell allows reconstruction of the regulatory cascade: which chromatin changes come first, which TFs drive transcription, and which genes accumulate.

### Scalability via Combinatorial Indexing

Unlike droplet-based platforms (10x Chromium), PerturbFate uses split-and-pool combinatorial indexing → no microfluidics needed → higher throughput, lower cost per cell.

## Results

### The Convergence Story

The central finding: >140 perturbations in functionally unrelated genes (chromatin remodelers, kinases, signaling components, Mediator subunits) all push melanoma cells toward the **same** dedifferentiated state.

```
Perturbation diversity:           Convergent outcome:
  NF2 (Hippo pathway)     ─┐
  MED12 (Mediator complex) ─┤
  SMARCE1 (SWI/SNF)       ─┤──→  Shared undifferentiated state
  NF1 (MAPK pathway)      ─┤      (FOSL1+, KLF5+, RREB1+, SMAD3+)
  DUSP6 (MAPK phosphatase) ─┤
  ...24 total              ─┘
```

This convergence was invisible to standard Perturb-seq — only the multimodal readout (ATAC + nascent + steady-state) revealed the shared chromatin and transcriptional architecture.

### Mediator Complex: Same Outcome, Different Paths

```
Kinase module (MED12, MED13, CCNC):
  → Loss of SOX10 activity (melanocytic identity)
  → Strong dedifferentiation in DMSO
  → Attenuated under Vem

Tail module (MED15, MED24):
  → Direct activation of YAP targets
  → Dedifferentiation + resistance under Vem

Both converge on:
  → Mediator/YAP co-regulated transcriptional program
  → TGFBR2, VEGFC as downstream effectors
```

## Limitations

- Single cell line (A375) — other melanoma subtypes untested
- In vitro only — no tumor microenvironment or immune context
- CRISPRi = partial knockdown, not complete knockout
- Combinatorial TF inhibition may have off-target or additive fitness effects
- 1-hour 5-EU pulse captures a snapshot, not full temporal dynamics

## Related Papers

- [[drug-resistance/alsulami-2026-predicting-and-interpreting-cell]] — PrePR-CT: computational drug response prediction (PerturbFate provides experimental ground truth that these models try to predict)
- [[drug-resistance/chen-2022-deep-transfer-learning-of]] — scDEAL: bulk→single-cell drug response transfer
- [[drug-resistance/antonopoulos-2026-zero-shot-prediction-of-drug]] — LEMBAS: zero-shot drug response via signaling networks
- [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] — GEARS: predicts perturbation outcomes computationally (PerturbFate generates the multimodal data these models lack)
- [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] — PerturbNet: distributional perturbation prediction
- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle: GRN-based perturbation simulation (PerturbFate reconstructs state-specific GRNs from multimodal data)
- [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] — TRADE: Perturb-seq effect size quantification
- [[neuroscience/jin-2020-in-vivo-perturb-seq]] — in vivo Perturb-seq in brain (single-modality contrast)
- [[neuroscience/amelan-2026-crispr-knockout-screens-reveal]] — CRISPR KO screens in neural differentiation
