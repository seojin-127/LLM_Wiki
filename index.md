# LLM Wiki — Index

> AI for Biology research paper knowledge base.
> Claude maintains this file. Do not edit manually.

**Stats**: 95 papers | 95 wiki pages | 26 categories

---

## genomic-dl
*DNA language models, variant effect prediction, regulatory genomics*

- [[genomic-dl/zemke-2023-conserved-and-divergent-gene]] — Cross-species single-cell multiomics (4 species, 200K+ cells); ~80% of human-specific CREs are TE-derived; ML sequence predictors show preserved regulatory syntax rodent→primate (Nature 2023)
- [[genomic-dl/zinati-2024-groundgan-grn-guided]] — GRouNdGAN: GRN-guided causal GAN for realistic scRNA-seq simulation; in silico TF KO; GRN inference benchmarking (Nat. Commun. 2024)
- [[genomic-dl/deng-2024-massively-parallel-regulatory]] — lentiMPRA + DL of >100K regulatory elements; 46,802 active enhancers in developing cortex; 164 psychiatric disorder variants with allele-specific enhancer activity (Science 2024)
- [[genomic-dl/avsec-2021-effective-gene-expression-prediction]] — Enformer: self-attention transformer predicting gene expression + chromatin states from 196kb DNA; integrates distal enhancers; outperforms CNN baselines on eQTL + CRISPRi benchmarks (Nat. Methods 2021)
- [[genomic-dl/yu-2026-chrombert-foundation-model]] — ChromBERT: BERT-based FM pretrained on ~1,000 TFs from ChIP-seq; learns TF interaction syntax; imputes unseen cistromes; context-specific TRN inference without additional ChIP-seq (Cell Genomics 2026)

---

## single-cell-dl
*scRNA-seq deep learning, cell type annotation*

- [[single-cell-dl/wang-2024-scsemiprofiler-advancing-large]] — scSemiProfiler: deep generative model + active learning for cost-effective large-cohort single-cell profiling (Nature Commun. 2024)
- [[single-cell-dl/aivazidis-2025-cell2fate-infers-rna]] — Cell2fate: Bayesian ODE linearization for RNA velocity modules; improved cell fate prediction, applied to developing human brain (Nature Methods 2025)
- [[single-cell-dl/li-2025-uda-seq-universal-droplet]] — UDA-seq: universal post-indexing for droplet multimodal single-cell; 100K+ cells from 36 clinical biopsies in one experiment (Nature Methods 2025)
- [[single-cell-dl/schuster-2024-multidgd-versatile-deep]] — multiDGD: deep generative model for RNA+ATAC joint representation; best reconstruction without feature selection; post-hoc batch integration (Nature Commun. 2024)
- [[single-cell-dl/ergen-2024-consensus-prediction-cell]] — popV: ensemble + ontology-voting for cell type label transfer with calibrated uncertainty; reduces manual review to ambiguous cells only (Nat. Genet. 2024)
- [[single-cell-dl/fischer-2024-sctab-scaling-cross-tissue]] — scTab: tabular DL for cross-tissue cell type annotation; trained on 22.2M cells; scaling laws confirmed; data augmentation improves generalization (Nat. Commun. 2024)

---

## single-cell-foundation
*Geneformer, scGPT, large-scale single-cell foundation models*

- [[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]] — SCimilarity: metric-learning foundation model; rapid search of 23.4M cells from 412 studies; ILD macrophage queries validated cross-tissue (Nature 2025)
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT: generative pretrained transformer on 33M+ cells; state-of-the-art on cell type annotation, multi-batch integration, perturbation prediction, and gene network inference (Nat. Methods 2024)
- [[single-cell-foundation/hao-2024-large-scale-foundation-model]] — scFoundation: 100M parameter asymmetric transformer pretrained on 50M+ human scRNA-seq profiles; state-of-the-art on gene expression enhancement, drug response, perturbation prediction (Nat. Methods 2024)
- [[single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell]] — EpiAgent: first foundation model for scATAC-seq; "cell sentence" encoding; zero-shot annotation; in silico CRE knockout; state-of-the-art on epigenomic tasks (Nat. Methods 2025)

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
- [[neuroscience/de-jong-2021-cortical-overgrowth-preclinical]] — CNTNAP2 homozygous truncating mutation forebrain organoids show cortical overgrowth via progenitor over-proliferation; CRISPR correction rescues (Nat. Commun. 2021)
- [[neuroscience/mato-blanco-2025-early-developmental-origins]] — Human NSC risk gene dynamics across corticogenesis; brain organizer hubs; TF depletion simulation; ASD patient NSC TF alterations (Nat. Commun. 2025)
- [[neuroscience/dubuc-2026-linking-rare-variants-cell-type]] — Framework linking rare variants in profound autism to cell-type function via brain transcriptomics + foundation models; specificity × sensitivity trade-off; AI inference + postmortem validation (Cell Genomics 2026)

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
- [[brain-development/zhang-2025-spatial-dynamics-brain-development]] — Spatial tri-omic (ATAC+RNA+protein + CUT&Tag+RNA+protein) atlas P0-P21 mouse brain; layer TF chromatin persistence; myelin gene priming in corpus callosum; shared dev/neuroinflammation programs (Nature 2025)
- [[brain-development/birey-2017-assembly-functionally-integrated]] — First forebrain assembloid (hCS+hSS); models human interneuron saltatory migration; Timothy syndrome migration defect rescued by roscovitine (Nature 2017)
- [[brain-development/zhang-2025-pfc-single-cell-spatiotemporal]] — Human-macaque postnatal PFC atlas (snRNA+ATAC+spatial); human-specific prolonged maturation via glial progenitor proliferation; NDD risk cell types (Nat. Neurosci. 2025)
- [[brain-development/bhaduri-2020-cell-stress-cortical-organoids]] — scRNA-seq comparison primary cortex vs. organoids; organoids lack molecular subtypes + areal specification due to cellular stress; transplantation into mouse cortex partially rescues (Nature 2020)
- [[brain-development/revah-2022-maturation-circuit-integration]] — hCO transplanted into newborn rat somatosensory cortex; mature cell types, thalamocortical + corticocortical integration; optogenetic activation drives reward-seeking; Timothy syndrome defects revealed (Nature 2022)
- [[brain-development/uzquiano-2022-proper-acquisition-cell-class]] — scRNA + ATAC + spatial atlas of hCS organoids; cell class identity matches endogenous cortex; callosal neuron diversity emerges early; human-specific fate specification programs (Cell 2022)
- [[brain-development/wang-2025-molecular-cellular-dynamics]] — Paired snATAC+snRNA atlas of 38 human neocortical samples (first trimester to adolescence); Tri-IPCs discovered (tripotential GABAergic+OPC+astrocyte); ASD GWAS risk in second-trimester intratelencephalic neurons (Nature 2025)
- [[brain-development/keefe-2025-lineage-resolved-atlas-developing]] — Prospective lineage tracing of 6,402 human cortical progenitors; glutamatergic→GABAergic switch at midgestation; truncated RG maintain glutamatergic potential; late-born tRG neurons show deep-layer features (Nature 2025)
- [[brain-development/fleck-2023-inferring-perturbing-cell-fate]] — Pando GRN framework from multiome time course in organoids; pooled CRISPR screen identifies GLI3 required for cortical fate; two GLI3 regulomes (dorsoventral patterning + ganglionic eminence) (Nature 2023)
- [[brain-development/amiri-2018-transcriptome-epigenome-landscape]] — PsychENCODE cortical organoid epigenome atlas; 96,375 gene-linked enhancers; A-reg/R-reg enhancer categories; ASD de novo variants in homeodomain/Hes1/Sox3 binding sites (Science 2018)
- [[brain-development/glass-2026-human-cortical-organoids-recapitulate]] — iPSC cortical organoids from infants with longitudinal MRI; early fate decisions (cell-type proportions, cell cycle genes) correlate with individual cortical surface area in vivo (Cell Stem Cell 2026)

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
- [[brain-atlas/braun-2023-comprehensive-cell-atlas-first]] — BICCN first-trimester human brain atlas: 1.67M cells (5–14 pcw), 616 clusters; MGE→thalamus migration; regional glioblast diversity; early OPC regionalization (Science 2023)
- [[brain-atlas/winter-2023-transcriptomic-taxonomy-mouse]] — Brain-wide SPN taxonomy: 65,002 neurons, 76 types, 3-component organization; LIM homeobox TF code for reticulospinal neurons (Nature 2023)
- [[brain-atlas/zhou-2023-brain-wide-correspondence-neuronal]] — epi-retro-seq: 33,034 neurons linking epigenomes to projections; 32 source regions × 24 targets; integrated into BICCN atlas (Nature 2023)
- [[brain-atlas/yao-2023-high-resolution-transcriptomic-spatial]] — Allen Brain Cell Atlas: ~4M scRNA-seq + 4.3M MERFISH cells, 5,322 clusters; dorsal-ventral dichotomy; combinatorial TF code; whole adult mouse brain (Nature 2023)
- [[brain-atlas/chen-2024-brain-cell-atlas-integrating]] — Brain Cell Atlas: 26.3M cells from 70 human + 103 mouse studies; ML consensus annotation; PCDH9-high microglia; hippocampus vs. PFC GRN differences (Nat. Med. 2024)
- [[brain-atlas/chen-2025-whole-cortex-in-situ]] — BARseq: 10.3M cells, 4.2M cortical neurons; transcriptomic type composition predicts area identity; sensory input sharpens area identity (enucleation) (Nature 2025)
- [[brain-atlas/domcke-2020-human-cell-atlas-fetal]] — sci-ATAC-seq3: ~800K fetal chromatin accessibility profiles, 15 organs; TF activator/repressor classification; organ-specific endothelial chromatin (Science 2020)
- [[brain-atlas/shi-2023-spatial-atlas-mouse-cns]] — STARmap PLUS in situ sequencing (194 nm voxels); 1.09M cells, 1,022 genes, adult mouse brain + spinal cord; 230 cell types + 106 molecular regions; AAV tropism mapped (Nature 2023)
- [[brain-atlas/kronman-2024-developmental-mouse-brain]] — DevCCF: 3D developmental mouse brain atlas (E11.5–P56); MRI + light-sheet templates; 3D anatomical segmentations; maps Allen CCFv3; open-access web visualizer (Nat. Commun. 2024)

---

## long-read
*PacBio, Oxford Nanopore sequencing methods*

*(no papers yet)*

---

## lrRNA
*Long-read RNA-seq: Iso-seq, MAS-seq, ONT*

- [[lrRNA/joglekar-2024-single-cell-long-read]] — Single-cell long-read brain isoform atlas: 72% of genes isoform-variable; cell-type-specific splicing dominant; P21→P28 adolescent transition peaks; mouse→human conservation (Nat. Neurosci. 2024)
- [[lrRNA/foord-2025-spatial-long-read-approach]] — Spl-ISO-Seq: spatial long-read isoform mapping at near-single-cell resolution; layer 4 excitatory neurons have most pubertal splicing changes; post-synaptic function linked (Nat. Commun. 2025)

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

- [[statistics/sumanaweera-2025-gene-level-alignment-single-cell]] — Genes2Genes: Bayesian information-theoretic DP for gene-level single-cell trajectory alignment; captures insertions/deletions per gene; in vitro vs. in vivo T cell comparison (Nat. Methods 2025)

---

## sex-differences-biology
*Sex-specific genetic architecture, XWAS*

*(no papers yet)*

---

## reproductive-biology
*Germ cell development, PGC, genomic imprinting*

- [[reproductive-biology/wang-2026-single-cell-spatiotemporal-dissection]] — 인간 MFI 전 임신 기간(GW5~39) snRNA+ATAC 멀티오믹스(191K 핵) + Stereo-seq 공간 전사체(1.1M 세포) atlas; EVT/SCT toggle switch 모델; spiral artery R0→R1→R2 endothelial state 발견; GWAS 통합 (Nature 2026)

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

- [[aging/jin-2025-brain-wide-cell-type-specific]] — Brain-wide aging atlas: ~1.2M cells from young+aged mice; 847 clusters, 14 age-biased; hypothalamic third-ventricle as aging hub; 2,449 age-DE genes (Nature 2025)

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
- [[other/pagliaro-2025-emerging-approaches-enhance]] — Review: emerging approaches to enhance brain organoid physiology; assembloids, ECM, morphogens, xenotransplantation (Trends Cell Biol. 2025)
- [[other/lancaster-2013-cerebral-organoids-model-human]] — Landmark: first hPSC cerebral organoid system; discrete brain regions; oRG-like cells; primary microcephaly model (Nature 2013)
- [[other/ekvall-2024-spatial-landmark-detection-tissue]] — ELD: unsupervised DL landmark detection + tissue registration using neural network + thin-plate splines; works with <10 samples; handles nonlinear deformations + multimodal spatial omics (Nat. Methods 2024)
- [[other/brancati-2020-resolving-neurodevelopmental-vision-disorders]] — Perspective: single-cell multi-omics for brain + retina organoid characterization; fidelity assessment vs. in vivo; applications to congenital CNS malformations and vision disorders (Neuron 2020)
- [[other/maoz-2018-linked-organ-on-chip-model]] — Linked NVU organ-on-chip (2 BBB chips + brain chip); dissects cell-type contributions; reveals endothelial-neuronal metabolic coupling; models methamphetamine pharmacokinetics (Nat. Biotechnol. 2018)
- [[other/ullah-2025-generating-characterizing-human-telencephalic]] — Protocol: human telencephalic organoids from single isolated neural rosettes; reproducible cellular composition; functional neural networks; SHANK3 deletion ASD model (Nat. Protocols 2026)
- [[other/nowakowski-2025-new-frontier-understanding-human]] — Perspective: advances in human + mammalian brain development atlases; novel cell populations; cross-species conservation/divergence; links to NDD mechanisms (Nature 2025)
- [[other/klingler-2022-mapping-molecular-cellular-complexity]] — Review: molecular + cellular mechanisms of cortical malformations (microcephaly, lissencephaly, polymicrogyria, dysplasia, heterotopia); centrosome/mTOR/actin pathways (Science 2022)
- [[other/ding-2026-scgpt-end-to-end-protocol]] — Protocol: scGPT fine-tuning for retinal cell type annotation; 99.5% F1-score; command-line + Jupyter workflow; accessible deployment guide (Nat. Protocols 2026)
