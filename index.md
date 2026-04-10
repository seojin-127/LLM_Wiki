# LLM Wiki — Index

> AI for Biology research paper knowledge base.
> Claude maintains this file. Do not edit manually.

**Stats**: 60 papers | 60 wiki pages | 26 categories

---

## genomic-dl
*DNA language models, variant effect prediction, regulatory genomics*

- [[genomic-dl/zemke-2023-conserved-and-divergent-gene]] — Cross-species single-cell multiomics (4 species, 200K+ cells); ~80% of human-specific CREs are TE-derived; ML sequence predictors show preserved regulatory syntax rodent→primate (Nature 2023)
- [[genomic-dl/zinati-2024-groundgan-grn-guided]] — GRouNdGAN: GRN-guided causal GAN for realistic scRNA-seq simulation; in silico TF KO; GRN inference benchmarking (Nat. Commun. 2024)

---

## single-cell-dl
*scRNA-seq deep learning, cell type annotation*

- [[single-cell-dl/wang-2024-scsemiprofiler-advancing-large]] — scSemiProfiler: deep generative model + active learning for cost-effective large-cohort single-cell profiling (Nature Commun. 2024)
- [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna]] — Cell2fate: Bayesian ODE linearization for RNA velocity modules; improved cell fate prediction, applied to developing human brain (Nature Methods 2025)
- [[single-cell-dl/li-2025-uda-seq-universal-droplet]] — UDA-seq: universal post-indexing for droplet multimodal single-cell; 100K+ cells from 36 clinical biopsies in one experiment (Nature Methods 2025)
- [[single-cell-dl/schuster-2024-multidgd-versatile-deep]] — multiDGD: deep generative model for RNA+ATAC joint representation; best reconstruction without feature selection; post-hoc batch integration (Nature Commun. 2024)
- [[single-cell-dl/ergen-2024-consensus-prediction-cell]] — popV: ensemble + ontology-voting for cell type label transfer with calibrated uncertainty; reduces manual review to ambiguous cells only (Nat. Genet. 2024)

---

## single-cell-foundation
*Geneformer, scGPT, large-scale single-cell foundation models*

*(no papers yet)*

---

## single-cell-methylation
*Single-cell DNA methylation analysis*

- [[single-cell-methylation/liu-2023-single-cell-dna-methylome]] — Brain-wide single-cell DNA methylome + 3D multi-omic atlas of adult mouse brain: 301K methylomes + 176K snm3C-seq profiles; 4,673 cell groups; 2.6M DMRs; TF→CRE→target regulatory networks (Nature 2023)

---

## protein-ai
*Protein language models, structure prediction*

*(no papers yet)*

---

## gwas
*GWAS, EWAS, rare variant testing, population genetics*

*(no papers yet)*

---

## neuroscience
*ASD, schizophrenia, psychiatric genetics*

- [[neuroscience/jin-2020-in-vivo-perturb-seq]] — In vivo Perturb-Seq of 35 ASD/ND risk genes in mouse cortex; 14 gene modules across neuronal and glial cells; conserved in human ASD brain (Science 2020)
- [[neuroscience/tanabe-2025-role-of-immature-choroid]] — Immature choroid plexus in ASD: CAMDI-KO mice + ASD iPSC organoids; delayed social critical period; metformin rescues ChP maturation and behavior (Cell Reports 2025)
- [[neuroscience/dony-2025-glucocorticoid-amplifies-inhibitory]] — Chronic GC exposure amplifies inhibitory neuron fate via PBX3 in organoids; lasting ASD risk gene dysregulation; genetic + environmental risk convergence (Sci. Adv. 2025)
- [[neuroscience/li-2023-single-cell-brain-organoid]] — CHOOSE system: pooled CRISPR screen of 36 ASD risk genes in mosaic cerebral organoids; dorsal IPs + ventral progenitors most vulnerable; ARID1B disrupts OPC/interneuron fate (Nature 2023)
- [[neuroscience/paulsen-2022-autism-genes-converge]] — 3 ASD genes (KMT5B, ARID1B, CHD8) converge on asynchronous GABAergic/excitatory development in 745K-cell organoid study; genomic context modulates expressivity (Nature 2022)
- [[neuroscience/jourdon-2023-modeling-idiopathic-autism]] — Idiopathic ASD father-son pairs (n=13): macrocephalic vs. normocephalic show opposite E/I neuron imbalances; TF divergence; convergence with rare-variant ASD genes (Nat. Neurosci. 2023)
- [[neuroscience/villa-2022-chd8-haploinsufficiency]] — CHD8 haploinsufficiency: macrocephaly-like organoids; accelerated inhibitory + delayed excitatory neurons; mRNA splicing dysregulation in neurons (Cell Reports 2022)
- [[neuroscience/schafer-2019-pathological-priming-causes]] — Pathological priming: premature activation of late developmental gene networks in idiopathic ASD iPSC-derived NSCs; heterochronicity across ASD individuals (Nat. Neurosci. 2019)
- [[neuroscience/morelli-2022-mecp2-related-pathways-cortical]] — DM1 cortical organoids: CUG foci → CELF2 dysfunction → MECP2 pathway dysregulation in glutamatergic neurons; convergent with Rett syndrome (Sci. Transl. Med. 2022)
- [[neuroscience/martinscosta-2024-arid1b-controls-transcriptional]] — ARID1B haploinsufficiency impairs corpus callosum transcriptional programs and axon projection in callosal organoid model (Cell Stem Cell 2024)

---

## brain-development
*Normal brain development, cortical biology, neurogenesis*

- [[brain-development/kanton-2019-organoid-single-cell-genomic]] — Cross-species organoid atlas (human/chimp/macaque); human neuronal neoteny; human-specific gene expression and chromatin divergence (Nature 2019)
- [[brain-development/mansour-2018-in-vivo-model-of]] — In vivo vascularized organoid model: hPSC organoids transplanted into mouse brain; functional vasculature, axonal outgrowth, graft-host synaptic connectivity (Nat. Biotechnol. 2018)
- [[brain-development/taverna-2014-cell-biology-of-neurogenesis]] — Review: cell biology of cortical neurogenesis; NE→RG→oRG/IP classification; oRG as key evolutionary innovation for neocortex expansion (Annu. Rev. Cell Dev. Biol. 2014)
- [[brain-development/nano-2025-integrated-analysis-molecular]] — Meta-analysis of 23 human cortical datasets; 500+ gene co-expression meta-modules; FEZF2+TSHZ3 drive deep layer specification (validated in chimeroids) (Nat. Neurosci. 2025)
- [[brain-development/mannens-2025-chromatin-accessibility-during]] — First whole-brain first-trimester chromatin atlas (135 clusters, 6–13 weeks); CNN identifies TF binding sites; MDD → midbrain GABAergic neurons most vulnerable (Nature 2025)
- [[brain-development/giandomenico-2019-cerebral-organoids-at]] — ALI-COs: air-liquid interface organoids with improved survival; mm-scale nerve tract formation; functional MEA recordings (Nat. Neurosci. 2019)
- [[brain-development/pasca-2015-functional-cortical-neurons]] — Original hCS protocol: matrix-free 3D cortical organoid; deep+superficial layer neurons; electrophysiologically mature; transcriptional match to fetal cortex (Nat. Methods 2015)
- [[brain-development/jain-2025-morphodynamics-human-early]] — Long-term live light-sheet morphodynamics of brain organoids; matrix→WNT/YAP1→telencephalon; WLS marks earliest non-telencephalic emergence (Nature 2025)
- [[brain-development/gabriel-2021-human-brain-organoids]] — OVB-organoids: self-organized bilateral optic vesicles in brain organoids; retinal cell types + light sensitivity; no extrinsic patterning needed (Cell Stem Cell 2021)
- [[brain-development/gordon-2021-long-term-maturation-of]] — Long-term hCS culture (>20 months) matches early postnatal brain development; intrinsic maturation programs (Nat. Neurosci. 2021)
- [[brain-development/trevino-2020-chromatin-accessibility-forebrain]] — 20-month ATAC-seq + RNA-seq of forebrain organoids; chromatin dynamics match in vivo; disease risk variant mapping (Science 2020)
- [[brain-development/herring-2022-human-prefrontal-cortex-gene]] — snRNA-seq + snATAC-seq of human PFC from gestation to adulthood; protracted cell-type-specific maturation; organoid deficit at postnatal stages (Cell 2022)
- [[brain-development/cakir-2019-engineering-of-human-brain]] — Vascularized cortical organoids via ETV2 co-differentiation; BBB features, improved survival/maturation (Nature Methods 2019)
- [[brain-development/sonthalia-2026-nemo-analytics-compendium]] — NeMO Analytics: ~200-study compendium; joint decomposition finds primate-specific oRG program; organoids lack layer-specific maturation programs (Nat. Neurosci. 2026)
- [[brain-development/liu-2025-human-specific-enhancer-fine]] — HARE5 (HAR enhancer of Frizzled8/WNT) drives human cortical expansion via radial glia self-renewal; 4 human-specific variants increase proliferation (Nature 2025)
- [[brain-development/kaplan-2025-sensory-input-sex-and]] — Hypothalamic preoptic area development: sex shapes trajectories perinatally; vomeronasal sensing required for normal maturation timing (Nature 2025)
- [[brain-development/zeng-2023-single-cell-spatial-transcriptional]] — Single-cell + spatial transcriptomics of human gastrulation (CS7–CS13); NE→RG transformation; spatially resolved RG subtypes; human-specific transcriptional signatures (Cell Stem Cell 2023)
- [[brain-development/ding-2026-dissecting-gene-regulatory-networks]] — CRISPRi screen of 44 TFs in human primary RG; ZNF219 represses premature differentiation; NR2E1/ARX opposing roles; effector genes enriched for NDD risk variants (Nature 2026)
- [[brain-development/zenk-2024-single-cell-epigenomic-reconstruction]] — Single-cell CUT&Tag (H3K27ac/me3, H3K4me3) from pluripotency→neural organoid; H3K27me3 at neuroectoderm stage required for fate restriction; epigenomic changes precede transcriptional identity (Nat. Neurosci. 2024)

---

## brain-atlas
*Brain cell atlases, BICCN, spatial transcriptomics*

- [[brain-atlas/hahn-2023-evolution-of-neuronal-cell]] — Cross-species retinal cell atlas (17 vertebrates); conservation of 6 cell classes; mouse midget RGC orthologues identified (Nature 2023)
- [[brain-atlas/corrigan-2025-conservation-and-alteration]] — TAC3 striatal interneurons conserved across 10 mammalian species; mouse Th interneurons are homologues; evolution via redistribution/fate refinement (Nature 2025)
- [[brain-atlas/van-velthoven-2025-transcriptomic-spatial-organization]] — Mouse telencephalic GABAergic atlas: 7 classes, 52 subclasses, 1,051 clusters, 611K adult + 614K developmental cells; postnatal cortical/striatal diversification; long-distance migration common (Nature 2025)
- [[brain-atlas/steyn-2024-temporal-cortex-cell-atlas]] — Pediatric-adult temporal cortex atlas (75 subtypes, African ancestry); LTK/FREM excitatory neurons with elevated cognition genes in pediatric tissue (Nat. Genet. 2024)
- [[brain-atlas/zhang-2023-molecularly-defined-spatially]] — Whole mouse brain MERFISH atlas: 5,000+ clusters, 300+ cell types, ~10M cells; spatial modules and ligand-receptor interactions (Nature 2023)
- [[brain-atlas/he-2024-integrated-transcriptomic-cell-atlas]] — HNOCA: 1.77M cells from 36 datasets/26 protocols; quantifies organoid fidelity vs. primary brain; cell stress universal in vitro artifact (Nature 2024)
- [[brain-atlas/cao-2020-human-cell-atlas-fetal]] — 4M-cell multi-organ human fetal atlas (121 samples, 15 organs, 657 subtypes); sci-RNA-seq3; circulating trophoblast-like cells discovered (Science 2020)
- [[brain-atlas/gao-2025-continuous-cell-type-diversification]] — Mouse visual cortex development atlas (768K+ cells, E11.5–P56); continuous cell-type diversification; many subtypes emerge at eye-opening/critical period (Nature 2025)
- [[brain-atlas/langlieb-2023-molecular-cytoarchitecture-of]] — Whole adult mouse brain atlas: 92 dissectates snRNA-seq + Slide-seq spatial; highest diversity in midbrain/hypothalamus; psychiatric GWAS heritability enrichment (Nature 2023)

---

## long-read
*PacBio, Oxford Nanopore sequencing methods*

*(no papers yet)*

---

## lrRNA
*Long-read RNA-seq: Iso-seq, MAS-seq, ONT*

- [[lrRNA/joglekar-2024-single-cell-long-read]] — Single-cell long-read brain isoform atlas: 72% of genes isoform-variable; cell-type-specific splicing dominant; P21→P28 adolescent transition peaks; mouse→human conservation (Nat. Neurosci. 2024)

---

## drug-resistance
*Cancer proteomics, drug resistance mechanisms*

*(no papers yet)*

---

## methylation-ai
*Methylation AI/DL models only*

*(no papers yet)*

---

## methylation
*General DNA methylation biology*

*(no papers yet)*

---

## medical-llm
*Medical/clinical LLMs, NLP for EHR*

*(no papers yet)*

---

## statistics
*Statistical methods (FDR, Bayesian, batch effects)*

*(no papers yet)*

---

## sex-differences-biology
*Sex-specific genetic architecture, XWAS*

*(no papers yet)*

---

## reproductive-biology
*Germ cell development, PGC, genomic imprinting*

*(no papers yet)*

---

## meiosis
*Meiotic recombination, crossover mechanisms*

*(no papers yet)*

---

## synapse-evolution
*Synaptic molecular evolution*

*(no papers yet)*

---

## aging
*Longevity genetics, lifespan QTL*

*(no papers yet)*

---

## organoid
*Non-brain organoids*

*(no papers yet)*

---

## concepts
*General ML/DL concepts used across biology*

*(no papers yet)*

---

## overviews
*Synthetic pages spanning multiple papers*

*(no overviews yet)*

---

## other
*Cross-topic, wet biology, reviews, benchmarks*

- [[other/eichmuller-2022-human-cerebral-organoids]] — Review: cerebral organoids for neurological disease modeling; vascularization, microfluidics, applications (2022)
- [[other/adlakha-2023-human-3d-brain-organoids]] — Review: 3D brain organoid advances; vascularization, biomaterials, microfluidics, disease applications (Cell Death Discov. 2023)
- [[other/lawrence-2024-hox-gene-expression]] — HOX gene atlas of developing human spine (scRNA-seq + spatial); neural crest dual HOX code (origin + destination); motor pool mapping (Nat. Commun. 2024)
- [[other/birtele-2025-modelling-human-brain]] — Roadmap review: brain organoid features, bioengineering improvements, CRISPR screens, ethics (Nat. Rev. MCB 2025)
