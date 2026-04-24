---
title: "Mapping convergent regulators of melanoma drug resistance by PerturbFate"
authors: Zihan Xu, Ziyu Lu, Aileen Ugurbil, Abdulraouf Abdulraouf, Andrew Liao, Jianxiang Zhang, Wei Zhou, Junyue Cao
year: 2026
doi: 10.1038/s41586-026-10367-0
category: drug-resistance
pdf_path: papers/xu-2026-mapping-convergent-regulators-of.pdf
pdf_filename: xu-2026-mapping-convergent-regulators-of.pdf
source_collection: manual
---

## One-line Summary

PerturbFate is a scalable combinatorial-indexing CRISPRi screening platform with simultaneous multimodal readouts (chromatin accessibility, nascent transcription, steady-state transcriptome, sgRNA identity) that reveals how >140 functionally diverse genetic perturbations converge on a shared dedifferentiated melanoma state driving vemurafenib resistance.

## 1. Document Info
- Journal: Nature
- Received: 7 March 2025
- Accepted: 5 March 2026
- Published: 2026

## 2. Key Contributions

- Introduces **PerturbFate**, a high-throughput, cost-effective CRISPRi platform built on combinatorial indexing (sci) that simultaneously profiles chromatin accessibility (ATAC), nascent RNA (5-EU labeling), steady-state transcriptome, and sgRNA identities in the same single cell
- Profiled >300,000 multimodal melanoma cells with perturbations in >140 vemurafenib resistance-associated genes
- Discovered that diverse genetic perturbations **converge** on a shared dedifferentiated cell state marked by cooperative TF activities (FOSL1, KLF5, RREB1, SMAD3)
- Dissected Mediator complex module-specific effects: kinase module (MED12) vs tail module (MED15/MED24) drive resistance through distinct mechanisms but converge on YAP-mediated transcriptional activation
- Combinatorial inhibition of convergent TF modules (RREB1 + SMAD3 + KLF5) neutralized resistance across diverse perturbations (mean 3.1-fold decrease in growth advantage)
- Identified VEGFC as a convergent downstream effector of Mediator/YAP co-regulated program

## 3. Methods & Architecture

### PerturbFate Platform Design
1. **CRISPRi perturbation**: cells expressing dCas9-BFP-KRAB transduced with pooled dual-sgRNA library (143 target genes + NTC)
2. **Metabolic labeling**: 1-hour 5-EU pulse labels nascent RNA → click chemistry + biotin-streptavidin pulldown separates nascent from pre-existing transcripts
3. **Combinatorial indexing**: two rounds of split-and-pool ligation for cell barcodes → scalable without droplet encapsulation
4. **Multimodal readout per cell**:
   - ATAC (chromatin accessibility via Tn5 tagmentation)
   - Nascent RNA (5-EU-labeled)
   - Pre-existing/steady-state RNA (unlabeled)
   - sgRNA identity

### Analytical Framework
- RNA velocity from nascent + whole transcriptome → infers state transition directions
- GRN reconstruction: TF motif accessibility (ATAC) + nascent expression → state-specific regulatory networks
- Multimodal regulon scoring: chromatin + nascent + steady-state combined TF activity scores
- Perturbation-phenotype mapping: cell-state enrichment analysis per perturbation

### Experimental Design
- A375 melanoma cells (BRAF V600E)
- DMSO (control) vs 1 μM vemurafenib treatment
- Bulk CRISPR screen in parallel for growth advantage validation

## 4. Key Results & Benchmarks

### Cell State Landscape
- Continuous phenotypic transitions: melanocytic → neural crest-like → undifferentiated states
- SOX10 governs melanocytic identity; AP-1 (FOSL1) and TEAD factors drive dedifferentiation
- 24 perturbations confer resistance to both Vem-induced growth arrest and differentiation

### Convergent Resistance Program
- Diverse perturbations (NF2, MED12, SMARCE1, NF1, DUSP6, etc.) converge on shared undifferentiated state
- Convergent TF hub: FOSL1, KLF5, RREB1, SMAD3 — most broadly activated across 24 resistant perturbations
- YAP and KRAS dependency signatures most strongly associated with Vem-resistant dedifferentiation
- TF expression negatively associated with patient overall survival (TCGA SKCM)

### Mediator Complex Dissection
- Kinase module KD (MED12, MED13, CCNC): strong dedifferentiation in DMSO, attenuated in Vem
- Tail module KD (MED15, MED24): promoted dedifferentiation and resistance under Vem
- MED12 uniquely promotes state transitions across conditions through loss of SOX10 activity
- Convergent Mediator/YAP co-regulated transcriptional program includes TGFBR2 and VEGFC

### Combinatorial Validation
- RREB1 KD + SMAD3 inhibition: moderate resistance reduction
- RREB1 KD + KLF5 inhibition + SMAD3 inhibition: largest reduction (mean 3.1-fold decrease)
- Supports convergent regulatory network as therapeutic target

## 5. Limitations & Future Work

- Single cell line (A375) — generalizability to other melanoma subtypes and cancer types untested
- CRISPRi (knockdown, not knockout) — partial loss-of-function, dosage effects not fully controlled
- Combinatorial TF inhibition results may include off-target effects or nonspecific fitness costs
- Static snapshot with metabolic labeling — does not capture full temporal dynamics of resistance emergence
- In vitro only — tumor microenvironment and immune interactions absent
- Platform generalizable to other disease contexts (stated but not demonstrated)

## 6. Related Work

- Dixit et al. (2016) — original Perturb-seq
- Replogle et al. (2022) — genome-scale Perturb-seq
- Xu et al. (2024) — previous work by same group: scalable single-cell RNA profiling of pooled CRISPR screens (Nat. Biotechnol.)
- Norman et al. (2019) — combinatorial CRISPRa screen
- Hugo et al. (2015) — non-genomic melanoma MAPKi resistance
- Pozniak et al. (2024) — TCF4-dependent resistance to immunotherapy in melanoma
- Coelho et al. (2024) — base editing screens for drug resistance

## 7. Glossary

- **PerturbFate**: combinatorial-indexing CRISPRi screening platform with multimodal single-cell readout
- **CRISPRi**: CRISPR interference — dCas9-KRAB fusion represses transcription without cutting DNA
- **5-EU (5-ethynyl uridine)**: nucleoside analog incorporated into nascent RNA; enables metabolic labeling via click chemistry
- **Combinatorial indexing (sci)**: split-and-pool barcoding strategy for scalable single-cell profiling without droplets
- **Vemurafenib (Vem)**: first approved BRAF(V600E) inhibitor for melanoma
- **Dedifferentiation**: loss of lineage-specific identity, associated with drug resistance and invasiveness
- **Mediator complex**: multi-subunit complex bridging TFs to RNA polymerase II; kinase module inhibits, core module facilitates transcription
- **Regulon**: a TF and its set of target genes
- **Convergent regulation**: functionally diverse perturbations producing the same downstream phenotypic outcome through shared regulatory programs
