---
title: "In vivo Perturb-Seq reveals neuronal and glial abnormalities associated with autism risk genes"
authors: Xin Jin, Sean K. Simmons, Amy Guo, Ashwin S. Shetty, Michelle Ko, Lan Nguyen, Vahbiz Jokhi, Elise Robinson, Paul Oyler, Nathan Curry, Giulio Deangeli, Simona Lodato, Joshua Z. Levin, Aviv Regev, Feng Zhang, Paola Arlotta
year: 2020
doi: 10.1126/science.aaz6063
source: jin-2020-in-vivo-perturb-seq.md
category: neuroscience
tags: [ASD, Perturb-Seq, CRISPR, scRNA-seq, neurodevelopment, mouse-cortex, risk-genes]
---

## Summary
In vivo Perturb-Seq screens 35 ASD/ND risk genes simultaneously in the developing mouse neocortex using pooled CRISPR-Cas9 + single-cell RNA-seq. Identifies 14 gene modules across neuronal and glial cell classes; 9 genes have significant effects. Gene modules and affected cell types are conserved in human ASD patient brain data.

## Key Contributions
- In vivo Perturb-Seq: scalable CRISPR screen in intact developing brain at single-cell resolution
- 14 covarying gene modules across 5 cortical cell classes; both neuronal and glial cells affected
- 9/35 ASD/ND genes show significant transcriptional effects
- Conservation of modules and cell-type phenotypes in human ASD patient brain

## Methods & Architecture
In utero lentiviral pooled CRISPR-Cas9 at E12.5 → scRNA-seq at P7. WGCNA for gene module identification. Joint linear regression for effect size estimation. Co-analysis with Velmeshev et al. 2019 ASD patient data.

## Results
- Both common (pan-cell-class) and cell-type-specific gene modules identified
- Inhibitory neurons, projection neurons, astrocytes, oligodendrocytes all affected
- Human brain and ASD patient single-cell data confirm conservation of modules and phenotypes

## Limitations
- Mouse E12.5 cortex model; LoF only; single brain region

## Related Papers
- [[neuroscience/jin-2020-in-vivo-perturb-seq]] — same paper cross-ref
