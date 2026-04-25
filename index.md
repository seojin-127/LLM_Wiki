# LLM Wiki — Index

> AI for Biology research paper knowledge base.
> Claude maintains this file. Do not edit manually.

**Stats**: 127 papers | 127 wiki pages | 26 categories

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
- [[single-cell-dl/caskey-2026-single-cell-genomics-decontamination]] — CellSweep: multinomial mixture model (EM) for ambient RNA decontamination; 98.84% cross-species removal; 25 sec on 16 threads; works on 10x, Smart-seq2, scATAC, Visium HD (bioRxiv 2026)
- [[single-cell-dl/ge-2026-prototype-based-continual-learning-for]] — scEvolver: prototype-based continual learning on scGPT backbone (LoRA+MoE); memory-augmented prototypes + hard-sample replay + MAPPL loss; +24.5% macro-F1 in 5-shot; discovers SF-like metaplastic cells in IBD gut (bioRxiv 2026)
- [[single-cell-dl/lopez-2018-deep-generative-modeling-for]] — scVI: foundational VAE+ZINB generative model for scRNA-seq; batch correction, normalization, clustering, DE in one framework; scales to 1M+ cells (Nat. Methods 2018)
- [[single-cell-dl/korsunsky-2019-fast-sensitive-and-accurate]] — Harmony: iterative soft-clustering linear batch correction on PCA embeddings; ~1M cells on laptop; LISI metric introduced; best scATAC-seq integrator (Nat. Methods 2019)
- [[single-cell-dl/aran-2019-reference-based-analysis-of]] — SingleR: iterative Spearman correlation reference-based annotation; discovers profibrotic transitional macrophages (CX3CR1+SiglecF+) in lung fibrosis (Nat. Immunol. 2019)
- [[single-cell-dl/xu-2021-probabilistic-harmonization-and]] — scANVI: semi-supervised extension of scVI for joint harmonization + annotation; best labeled integration in scIB benchmark (Mol. Syst. Biol. 2021)
- [[single-cell-dl/hao-2021-integrated-analysis-of-multimodal]] — Seurat v4 WNN: per-cell modality-weighted multimodal integration; 211K PBMC CITE-seq atlas; resolves T cell subtypes invisible to RNA alone (Cell 2021)
- [[single-cell-dl/lotfollahi-2022-mapping-single-cell-data]] — scArches: transfer learning "architecture surgery" for privacy-preserving reference atlas mapping; 4 orders of magnitude fewer updated parameters (Nat. Biotechnol. 2022)
- [[single-cell-dl/luecken-2022-benchmarking-atlas-level-data]] — scIB: definitive integration benchmark (68 methods × 13 atlas tasks); scANVI tops labeled; Scanorama/scVI tops unsupervised; Harmony best scATAC (Nat. Methods 2022)
- [[single-cell-dl/dominguez-conde-2022-cross-tissue-immune-cell]] — CellTypist + cross-tissue immune atlas (360K cells, 16 tissues, 101 immune types); logistic regression SGD annotation scales to millions; erythrophagocytic macrophage convergence (Science 2022)
- [[single-cell-dl/dedonno-2023-population-level-integration-of]] — scPoli: prototype-loss + sample embeddings for population-level integration; +5% over scANVI; open-world novel cell types; scales to 7.8M cells (Nat. Methods 2023)
- [[single-cell-dl/liu-2024-discovery-of-optimal-cell]] — NS-Forest v4.0: random forest + decision tree minimal marker gene selection; On-Target Fraction metric; outperforms DE-based markers on brain/kidney/lung atlases (BMC Methods 2024)
- [[single-cell-dl/boyeau-2025-deep-generative-modeling-of]] — MrVI: hierarchical Bayesian VAE with per-cell sample distance matrices for annotation-free cohort stratification; COVID-19 T cell severity grouping; IBD pericyte discovery (Nat. Methods 2025)
- [[single-cell-dl/setty-2019-characterization-of-cell-fate]] — Palantir: probabilistic fate mapping on diffusion-map manifold; per-cell branch probabilities + differentiation potential (entropy); human CD34+ hematopoiesis continuous fate model (Nat. Biotechnol. 2019)
- [[single-cell-dl/lange-2022-cellrank-for-directed-single]] — CellRank: directed Markov chain on phenotypic manifold combining RNA velocity + similarity; auto-detects initial/terminal states via GPCCA; works on regeneration/reprogramming (Nat. Methods 2022)
- [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] — CellOracle: cluster-specific directional GRNs from scRNA+scATAC; signal propagation simulates TF KO as 2D cell-state transition vectors; validates novel noto prechordal phenotype (Nature 2023)
- [[single-cell-dl/klein-2025-mapping-cells-through-time]] — moscot: scalable multimodal optimal-transport framework (W/GW/FGW); 1.7M-cell mouse embryogenesis on a laptop; unifies temporal, spatial, spatiotemporal mapping (Nature 2025)
- [[single-cell-dl/vinyard-2025-learning-cell-dynamics-with]] — scDiffEq: neural SDE with cell-state-dependent drift and diffusion networks; 54.8% LARRY fate prediction (+6% over PRESCIENT); optimal drift/diffusion ratio ~2.5 (Nat. Mach. Intell. 2025)
- [[single-cell-dl/nadig-2025-transcriptome-wide-analysis-of]] — TRADE: ash-based effect-size distribution for Perturb-seq; transcriptome-wide impact metric; typical perturbation hits ~45 genes (essentials >500); only 13-36% of TI in FDR-sig genes (Nat. Genet. 2025)
- [[single-cell-dl/gorin-2025-monod-model-based-discovery]] — Monod: fits biophysical stochastic transcription models (bursty default) to joint nascent/mature counts; distinguishes noise vs. mean modulation; cross-platform integration without distortive normalization (Nat. Methods 2025)
- [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] — GEARS: GNN + gene coexpression/GO knowledge graphs for combinatorial perturbation prediction; predicts unseen gene combinations; 40% higher precision on genetic interaction detection (Nat. Biotechnol. 2023)
- [[single-cell-dl/yu-2025-perturbnet-predicts-single-cell-responses]] — PerturbNet: modular cINN framework for distributional perturbation prediction; supports chemical/genetic/missense variants; outperforms GEARS; first to predict coding-variant effects via ESM (Mol. Syst. Biol. 2025)
- [[single-cell-dl/he-2026-squidiff-predicting-cellular-development]] — Squidiff: conditional denoising diffusion model for scRNA-seq; predicts differentiation, gene perturbation, drug response via semantic latent manipulation; captures transient states VAE/GNN methods miss (Nat. Methods 2026)
- [[single-cell-dl/dimitrov-2026-interpretation-extrapolation-and-perturbation-of]] — **Review (Stegle lab)**: unifying ontology of ~150 ML methods for single-cell perturbation modelling; 5 modelling concepts (repr. learning, disentanglement, causal inference, mechanistic discovery, population tracing) × 3 aims (understand/extrapolate/guide); critical evaluation showing simple baselines often beat foundation models on extrapolation (Nat. Rev. Genet. 2026)

---

## single-cell-foundation
*Geneformer, scGPT, large-scale single-cell foundation models*

- [[single-cell-foundation/heimberg-2025-cell-atlas-foundation-model]] — SCimilarity: metric-learning foundation model; rapid search of 23.4M cells from 412 studies; ILD macrophage queries validated cross-tissue (Nature 2025)
- [[single-cell-foundation/cui-2024-scgpt-toward-building-foundation]] — scGPT: generative pretrained transformer on 33M+ cells; state-of-the-art on cell type annotation, multi-batch integration, perturbation prediction, and gene network inference (Nat. Methods 2024)
- [[single-cell-foundation/hao-2024-large-scale-foundation-model]] — scFoundation: 100M parameter asymmetric transformer pretrained on 50M+ human scRNA-seq profiles; state-of-the-art on gene expression enhancement, drug response, perturbation prediction (Nat. Methods 2024)
- [[single-cell-foundation/chen-2025-epiagent-foundation-model-single-cell]] — EpiAgent: first foundation model for scATAC-seq; "cell sentence" encoding; zero-shot annotation; in silico CRE knockout; state-of-the-art on epigenomic tasks (Nat. Methods 2025)
- [[single-cell-foundation/szalata-2026-perturbert-learning-gene-co]] — PerturBERT: BERT encoder (57.6M params) pretrained on ~1M perturbation signatures (L1000+Perturb-seq); masked-gene modeling; SOTA gene dependency R²=0.8805; beats scGPT on 10/15 tasks with 30× less data (ICLR 2026)

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
- [[neuroscience/amelan-2026-crispr-knockout-screens-reveal]] — Genome-wide CRISPR KO screen in mESC → neural lineage; 331 neural-differentiation-essential genes (NEGs); 8 mouse KO hits with neuroanatomy defects; PEDS1 recessive microcephaly validated in family (Nat. Neurosci. 2026)

---

## brain-development
*Normal brain development, cortical biology, neurogenesis*

- [[brain-development/kanton-2019-organoid-single-cell-genomic]] — Cross-species organoid atlas (human/chimp/macaque); human neuronal neoteny; human-specific gene expression and chromatin divergence (Nature 2019)
- [[brain-development/mansour-2018-in-vivo-model-of]] — In vivo vascularized organoid model: hPSC organoids transplanted into mouse brain; functional vasculature, axonal outgrowth, graft-host synaptic connectivity (Nat. Biotechnol. 2018)
- [[brain-development/taverna-2014-cell-biology-of-neurogenesis]] — Review: cell biology of cortical neurogenesis; NE→RG→oRG/IP classification; oRG as key evolutionary innovation for neocortex expansion (Annu. Rev. Cell Dev. Biol. 2014)
- [[brain-development/nano-2025-integrated-analysis-molecular]] — Meta-analysis of 23 human cortical datasets; 500+ gene co-expression meta-modules; FEZF2+TSHZ3 drive deep layer specification (validated in chimeroids) (Nat. Neurosci. 2025)
- [[brain-development/mannens-2025-chromatin-accessibility-during]] — First whole-brain first-trimester chromatin atlas (135 clusters, 6–13 weeks); CNN identifies TF binding sites; MDD → midbrain GABAergic neurons most vulnerable (Nature 2025)
- [[brain-development/dibella-2021-molecular-logic-of-cellular]] — Mouse somatosensory cortex E10.5–P4 atlas (98K scRNA + scATAC + Slide-seq); PNs diversify post-mitotically (APs ordered by age, not subtype); glial/neuronal split at E13.5 (Nature 2021)
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

- [[drug-resistance/antonopoulos-2026-zero-shot-prediction-of-drug]] — LEMBAS RNN (phosphoproteomics + signaling network) zero-shot predicts cancer drug response via TF activity; Pearson r up to 0.79; discovers non-canonical FOXO3:S7 via SHP099 (PLoS Comput. Biol. 2026)
- [[drug-resistance/chen-2022-deep-transfer-learning-of]] — scDEAL: bulk→single-cell transfer learning (DaNN + MMD) for drug response; cell-cluster regularization preserves heterogeneity; F1 0.89 across 6 scRNA-seq benchmarks (Nat. Commun. 2022)
- [[drug-resistance/alsulami-2026-predicting-and-interpreting-cell]] — PrePR-CT: graph attention network with cell-type-specific co-expression graphs as inductive bias; unseen-cell-type generalization beats scGen/CPA/chemCPA; SMILES-conditioned drug embedding (Nat. Mach. Intell. 2026)
- [[drug-resistance/xu-2026-mapping-convergent-regulators-of]] — PerturbFate: multimodal CRISPRi platform (ATAC+nascent RNA+transcriptome+sgRNA) at 300K cell scale; >140 perturbations converge on shared dedifferentiated melanoma state; FOSL1/KLF5/RREB1/SMAD3 TF hub (Nature 2026)

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

- [[reproductive-biology/wang-2026-single-cell-spatiotemporal-dissection]] — Full-gestation MFI atlas: snRNA+ATAC multiomics (191K nuclei) + Stereo-seq spatial transcriptomics (1.1M cells); EVT/SCT toggle switch model; novel R0→R1→R2 arterial endothelial states; GWAS integration for pregnancy complications (Nature 2026)

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

- [[concepts/variational-autoencoder]] — VAE: probabilistic encoder-decoder for smooth latent representations; backbone of scVI ecosystem, PerturbNet ChemicalVAE/GenotypeVAE/CellVAE
- [[concepts/graph-neural-network]] — GNN: message-passing neural network on graph-structured data; used in GEARS (dual coexpression+GO graph), PrePR-CT (GAT), GRouNdGAN
- [[concepts/uncertainty-quantification]] — Epistemic vs aleatoric uncertainty; Bayesian NN, MC Dropout, ensemble, distributional output, Fisher information; wiki-wide survey of which methods provide uncertainty
- [[concepts/multimodal-temporal-readout]] — ATAC → nascent RNA → steady-state RNA as three different time windows (potential / present / accumulated identity); pair = RNA velocity, triplet = causal cascade
- [[concepts/factorial-perturbation-design]] — 2×2 (perturb × context) screens reveal constitutive vs contingent drivers; same outcome can hide different conditional logic; interaction term is the key new information

---

## overviews
*Synthetic pages spanning multiple papers*

- [[overviews/single-cell-integration-methods]] — 4가지 패러다임(Harmony/scVI계열/WNN/FM) 비교; scIB 벤치마크 결과 요약; 상황별 결정 프레임워크; scVI→scANVI→scArches→scPoli→MrVI 계보 정리
- [[overviews/brain-organoid-fidelity]] — 오가노이드 fidelity 6개 층위별 평가; 스트레스 아티팩트의 이중성(보편적이지만 분리 가능); 공학적 해결책(이식·혈관화·어셈블로이드) 비교; 연구 질문별 적합성 결정 트리
- [[overviews/convergent-regulation-across-systems]] — Why do hundreds of mutations converge on one phenotype? ASD (35 genes→14 modules) + melanoma (140+ genes→1 state); attractor landscape; TF hubs; PerturbFate multimodal evidence; brain×PerturbFate as next experiment
- [[overviews/endogenous-variation-as-natural-perturbation]] — **Sister overview to convergent-regulation**: endogenous variation = natural perturbation; gene effect = f(perturb, context); divergence (same perturb→different effects) and convergence (different perturbs→same effect) as two faces of context-dependence; reframes "what does gene X do?" as "what does X do given Y?"

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
- [[other/melsted-2026-rna-seq-analysis-in-seconds]] — GPU-accelerated kallisto: prefix-scan EC intersection + EM on NVIDIA GPU; 48× speedup (295M reads: 40 min→50 sec); 3.6M paired-end reads/sec on RTX 5090; bgzip input required (bioRxiv 2026)
