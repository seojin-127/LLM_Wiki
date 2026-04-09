---
title: "NeMO Analytics: a compendium of transcriptomic data for the exploration of neocortical development"
authors: Shreyash Sonthalia, Brian Herb, Ricky S. Adkins, Joshua Orvis, Guangyan Li, Xiangyu Liao, Qingjie Yu, Xoel Mato Blanco, Alex Casella, Jinrui Liu, Genevieve Stein-O'Brien, Brian Caffo, Ronna Hertzano, Anup Mahurkar, Jin-Chong Xu, Jesse Gillis, Jonathan Werner, Shaojie Ma, Suel-Kee Kim, Nicola Micali, Nenad Sestan, Pasko Rakic, Gabriel Santpere, Seth A. Ament, Carlo Colantuoni
year: 2026
doi: 10.1038/s41593-026-02204-4
category: brain-development
pdf_path: C:/Users/SAMSUNG/Documents/My EndNote Library.Data/PDF/0447030320/Sonthalia-2026-NeMO Analytics_ a compendium of.pdf
pdf_filename: Sonthalia-2026-NeMO Analytics_ a compendium of.pdf
source_collection: endnote
---

## One-line Summary
NeMO Analytics compiles ~200 neocortical development studies (mouse, macaque, human) and applies joint matrix decomposition to identify conserved transcriptome dynamics, including a primate-specific oRG program; also benchmarks cerebral organoids showing absence of many layer-specific maturation programs in vitro.

## 1. Document Info
- Journal/Conference: Nature Neuroscience
- Published: April 2026 (Vol. 29, 978–991)

## 2. Key Contributions
- Assembled gene-level transcriptomic data from ~200 studies of neocortical development and in vitro models
- Joint matrix decomposition across mouse, macaque, human data defines conserved transcriptome dynamics
- Identified primate-specific program: emerges in ventricular progenitors, expressed in outer/basal radial glia (oRG) in primates but limited to gliogenic precursors in rodents
- Decomposition of adult human neocortex identified layer-specific excitatory neuron signatures and charted their developmental emergence
- Organoid benchmark: broad in vivo development recapitulated in vitro, but many layer-specific neuronal maturation programs absent
- Web tool at nemoanalytics.org/landing/neocortex for non-coder access

## 3. Methods & Architecture
- Multi-study data aggregation (~200 studies)
- Joint matrix decomposition (NMF-based) across species and datasets
- Cross-species conserved program identification
- Organoid vs in vivo comparison via decomposition factors

## 4. Key Results & Benchmarks
- Conserved transcriptome dynamics defined across neurogenesis in mouse, macaque, human
- Primate-specific oRG program identified (absent/limited in rodents)
- Layer-specific excitatory neuron signatures: late-peaking expression vs early-peaking TF expression (dissociation between specification and maturation)
- Cerebral organoids: broad elements recapitulated, but layer-specific maturation programs largely absent

## 5. Limitations & Future Work
- Aggregation of heterogeneous datasets may introduce batch effects
- Matrix decomposition assumptions may not capture all biological variation
- Web tool dependent on continued maintenance

## 6. Related Work
- Herring et al. 2022: PFC developmental dynamics
- BICCN: cross-species cortical atlas
- Gordon et al. 2021: long-term organoid maturation

## 7. Glossary
- **oRG**: Outer radial glia — basal radial glia; key for cortical expansion in primates
- **NMF**: Non-negative matrix factorization — decomposition method for identifying latent programs
- **Layer-specific signatures**: Gene expression patterns defining cortical layers (L2/3, L4, L5, L6)
- **NeMO**: Neuroscience Multi-Omics
