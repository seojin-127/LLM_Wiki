---
title: "Transcriptomic and phenotypic convergence of neurodevelopmental disorder risk genes in vitro and in vivo"
authors: Meilin Fernandez Garcia, Kayla Retallick-Townsley, April Pruitt, Elizabeth A. Davidson, Novin Balafkan, Jonathan Warrell, Tzu-Chieh Huang, et al.; Laura M. Huckins, Ellen J. Hoffman, Kristen Brennand (corresponding)
year: 2026
doi: 10.1038/s41593-026-02247-7
category: neuroscience
pdf_path: papers/fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence.pdf
pdf_filename: fernandez-garcia-2026-transcriptomic-and-phenotypic-convergence.pdf
source_collection: nature-neuroscience
---

## One-line Summary

Yale Brennand & Hoffman labs apply **pooled CRISPR-KO of 23 NDD risk genes** (chromatin/regulatory class) across iPSC-derived NPCs, glutamatergic and GABAergic neurons (118k cells), find that **transcriptomic convergence is cell-type-specific and strongest in mature glutamatergic neurons** (synaptic + epigenetic + unexpected mitochondrial pathways), with convergence predicted by clinical/co-expression similarity — and 10/11 drugs predicted to reverse convergent signatures rescue zebrafish behavioral phenotypes in vivo.

## 1. Document Info

- Journal: Nature Neuroscience
- DOI: 10.1038/s41593-026-02247-7
- Received: 2024-08-23, Accepted: 2026-02-25
- Corresponding: ellen.hoffman@yale.edu (Hoffman, Yale Child Study), kristen.brennand@yale.edu (Brennand, Yale Psychiatry/Genetics)
- Senior labs: **Brennand lab** (iPSC-derived neuron models for psychiatric disease), **Hoffman lab** (zebrafish models of ASD genetics). Long-standing Yale collaboration on NDD.
- Co-first authors: 5 (Fernandez Garcia, Retallick-Townsley, Pruitt, Davidson, Balafkan)

## 2. Key Contributions

1. **Pooled scCRISPR-KO of 24 NDD genes** (23 successfully resolved across some condition) in **four cell-type contexts**: iNPC, immature iGLUT (day 7), mature iGLUT (day 21), mature iGABA (day 36). 118,436 single cells total. Genes biased toward chromatin modifiers/transcriptional regulators (since >50% of NDD risk genes are in this class).
2. **Convergence is cell-type-specific** — KO effects most correlated and dense in **mature glutamatergic neurons**; iNPC weakest. Different cell types show different "top convergent genes."
3. **Pathway convergence**: in mature iGLUT, convergent DEGs enrich for synaptic, epigenetic, and — unexpectedly — **mitochondrial / OXPHOS** pathways. Mitochondrial finding validated experimentally (Seahorse OCR, mitochondrial membrane potential, OXPHOS protein expression).
4. **Predictors of convergence**: NDD genes that converge most strongly are those with shared **clinical associations** (ASD vs DD vs SCZ vs EPI), shared **biological annotations**, and shared **co-expression patterns in human postmortem brain**. Suggests convergence reflects developmental brain co-expression structure (Werling/Geschwind / Willsey-style developmental trajectories).
5. **Drug reversal in zebrafish** — used Connectivity-Map-style query to find drugs that reverse convergent transcriptomic signatures and/or arousal-sensory behavioral signatures; **10/11 drugs ameliorated at least one mutant zebrafish behavior** (e.g., chd2 + Pravastatin, kdm6b + Paclitaxel, phf21a + Fluvoxamine).
6. **Reverse, not prevent**: drugs work post-mitotically, suggesting convergent networks in mature neurons remain a clinically actionable window even after symptom onset.

## 3. Methods & Architecture

### Cell models
- Control hiPSC line → induced to NPC, immature iGLUT (NGN2, day 7), mature iGLUT (day 21), mature iGABA (day 36)
- Lenti-Cas9v2 transduction first, then pooled lentiviral gRNA library (3-4 gRNAs per gene) 3 days before harvest

### CRISPR library
- 24 target NDD genes (chromatin biology focus): ANK3, ARID1B, ASH1L, ASXL3, BCL11A, CHD2, CHD8, DPYSL2, FOXP2, KMT5B (SUV420H1), KDM5B, KDM6B, KMT2C, MBD5, MED13L, NRXN1, PHF12, PHF21A, SCN2A, SETD5, SIN3A, SKI, SMARCC2, WAC
- 3 (DPYSL2, FOXP2, SCN2A) underrepresented in library

### Single-cell readout
- 10X scRNA-seq, gRNA assignment per cell
- Filtering yields 118,436 cells: 25,402 iNPC, 38,097 immature iGLUT, 28,388 mature iGLUT, 26,549 mature iGABA

### Analysis
- **Differential expression**: pseudobulked counts per (cell type × KO), LIMMA against non-targeting (NT)
- **Convergence definition**: METAL meta-analysis across all KOs in a cell type → DEGs with FDR-adjusted P_meta < 0.05 AND Cochran's Q heterogeneity P_Het > 0.05 (= significant + concordant direction)
- **Multi-combination convergence**: enumerate all C(n,r) combinations of KOs (e.g., 152 unique 2–5-gene combos from the 9 genes resolved across all 4 cell types) → quantify ratio of convergent genes to mean DEG count
- **Network-level convergence**: WGCNA modules + gene set enrichment for convergent DEG sets
- **Cell-type mapping to human brain**: deconvolve convergent gene sets against published human brain scRNA-seq cell types
- **Drug prediction**: Connectivity-Map-style query (transcriptomic signature) + behavioral signature matching from arousal/sensory zebrafish behavior data
- **In vivo validation**: zebrafish F0 crispants + stable mutant lines (e.g., chd8 Δ7/Δ7, ash1l 1i/Δ60/19i, arid1b Δ7/Δ7, kdm5b a/b lines, kmt5b Δ208/1i/Δ5, kmt2c a/b lines, nrxn1a Δ248/30i/Δ248/30i) — high-throughput behavior battery, drug exposure, behavioral rescue scoring
- **Mitochondrial validation**: Seahorse OCR (oxygen consumption rate, basal/maximal/coupled respiration), TMRM/MitoTracker (membrane potential), OXPHOS protein panel by IF, dendrite + mitochondrial morphology imaging in NRXN1, ASH1L, ARID1B mutant neurons

## 4. Key Results & Benchmarks

- **Per-KO DEG overlap is poor** between cell types — at FDR < 0.05, often the **only** common DEG between cell types is the targeted gene itself. Demonstrates effects are highly context-dependent.
- **Convergent gene count by cell type** (across 9 NDDs resolved in all 4 contexts): mature iGLUT highest, iNPC lowest. Magnitude of convergence highly correlated between cell types (P_holm < 2.2 × 10⁻¹⁶), with strongest correlation between immature and mature iGLUT.
- **Cell-type overlap of convergent genes**: >50% of convergent genes in NPC (52%), immature iGLUT (57%), mature iGABA (56%) overlap with mature iGLUT convergent set — but **not necessarily in same direction**.
- **Pathway enrichment in mature iGLUT**: synaptic (pre/post-syn, neurotransmitter regulation), epigenetic (chromatin organization, histone methylation, SWI/SNF complexes), mitochondrial (inner membrane, OXPHOS, ETC, TCA cycle, mito translation, complex I assembly).
- **Mitochondrial validation**: NRXN1, ASH1L, ARID1B mutants show altered OXPHOS protein expression, reduced coupled and maximal respiration on Seahorse, altered mitochondrial morphology in dendrites.
- **Predictors of convergence** (gene-pair level): Pearson correlation of convergence strength positively correlated with shared GO annotation, shared clinical association, postmortem brain co-expression. Independent of effect size.
- **GWAS / rare variant enrichments**: convergent gene sets enriched for SCZ-LoF, ASD-LoF, ID-LoF rare variant burden; SCZ, BIP, BIP-I, BIP-II GWAS signal in MAGMA.
- **Behavioral correlations across zebrafish mutants** clustered into 4 sets — sets 1-2 (large abnormal-behavior counts) over-represented behaviors related to seizure, motor, behavior, speech, cognition.
- **Drug rescue**: 10/11 tested drugs rescue at least one zebrafish mutant behavioral phenotype. Examples: chd2 × Pravastatin, kdm6b × Paclitaxel, ash1l × Sunitinib/Rosiglitazone/Repaglinide/Ezetimibe, phf21a × Fluvoxamine/Amiodarone, kmt5b × Sirolimus/Paclitaxel.

## 5. Limitations & Future Work

- **Single donor hiPSC line** — limits genetic background diversity (which the authors note is critical given expressivity / penetrance differences across genetic backgrounds).
- KO via NGN2 induction → not all developmental contexts (no astrocytes, no organoid 3D context).
- Mature iGLUT day 21 — still a relatively early in vitro neuron, not adult human neuron.
- 23/24 genes biased toward chromatin/transcription regulators (over-representation of one functional class).
- Drug rescue in zebrafish ≠ rescue in human — translational gap remains.
- Convergence definition is statistical (meta-analysis FDR + heterogeneity) — biologically meaningful but may miss non-monotonic shared effects.
- gRNA representation for 3 genes (DPYSL2, FOXP2, SCN2A) was lower → limited statistical power for those.

## 6. Related Work

### Same convergence-of-NDD-genes question
- **Paulsen 2022** (Arlotta lab, Nature) — "Autism genes converge on asynchronous development" in cortical organoids. CHD8, ARID1B, SUV420H1, etc. Shows convergence at developmental timing level, complementary to this paper's mature-neuron focus.
- **Jin 2020** (in vivo Perturb-Seq, Macosko/Arlotta) — in vivo CRISPR-Cas9 + scRNA-seq in mouse cortex. ASD risk gene KO in developing brain.
- **Paulsen 2022, Jourdon 2023, Mato-Blanco 2025, Villa 2022 (CHD8), Martins-Costa 2024 (ARID1B)** — cluster of organoid/neuron NDD modeling papers in this wiki.

### Methodology kin
- **Amelan 2026** — CRISPR knockout screens reveal convergence (similar pooled-screen design)
- **Dubuc 2026** — linking rare variants to cell-type effects

### Postmortem brain co-expression context
- The "convergence reflects co-expression" claim links to BrainSpan / PsychENCODE / Werling-Willsey developmental network analyses (cited in paper, not in this wiki yet).

### NDD GWAS / common variant context
- The MAGMA enrichments connect to the rare-variant–common-variant integration question (Wray, Sullivan, etc.)

## 7. Glossary

- **NDD**: neurodevelopmental disorder — umbrella term covering ASD, DD, ID, epilepsy, SCZ overlap.
- **Convergent gene**: DEG that is significant (FDR_meta < 0.05) AND has consistent direction of effect across multiple gene KOs (Cochran Q P_Het > 0.05).
- **iNPC / iGLUT / iGABA**: hiPSC-induced NPCs / glutamatergic neurons / GABAergic neurons.
- **NGN2 induction**: NEUROG2 transgene-driven rapid conversion of iPSC to glutamatergic-like neurons (Zhang/Südhof protocol).
- **F0 crispant**: zebrafish injected with Cas9 + gRNA at 1-cell stage, generates mosaic mutant in F0 generation (no breeding needed).
- **METAL**: standard meta-analysis tool (Willer 2010), originally for GWAS, here used to combine DEG p-values across KOs.
- **OCR (Seahorse)**: oxygen consumption rate; basal, coupled (oligomycin-inhibited), maximal (FCCP-uncoupled), non-mito (rotenone+antimycin).
- **Connectivity Map**: LINCS L1000 transcriptomic signature database used to query "what perturbation (drug) reverses this signature?"
- **Cochran's Q**: heterogeneity statistic in meta-analysis. Q P > 0.05 means effects are statistically consistent across studies (here: across KOs).
- **MAGMA**: gene-based GWAS enrichment test (de Leeuw 2015).
