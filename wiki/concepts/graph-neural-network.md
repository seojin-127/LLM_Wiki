---
title: "Graph Neural Network (GNN)"
type: concept
created: 2026-04-24
category: concepts
tags: [GNN, graph, message-passing, knowledge-graph, deep-learning, network]
used_in:
  - single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of
  - single-cell-dl/kamimoto-2023-dissecting-cell-identity-via
  - drug-resistance/alsulami-2026-predicting-and-interpreting-cell
  - genomic-dl/zinati-2024-groundgan-grn-guided
---

## What Is a GNN?

A Graph Neural Network (GNN) is a neural network that operates on **graph-structured data** — data where entities (nodes) are connected by relationships (edges). Unlike standard neural networks that process vectors, images, or sequences, GNNs process **networks of relationships**.

## Why Graphs Matter in Biology

Biological data is inherently relational:

```
Gene regulatory networks:    TF_A ──→ Gene_B ──→ Gene_C
Protein interactions:        Protein_X ── binds ── Protein_Y
Cell-cell communication:     Neuron_1 ── synapse ── Neuron_2
Pathway membership:          Gene_A ── member_of ── GO:apoptosis
```

Standard neural networks (MLP, CNN) cannot naturally handle these structures. They need fixed-size input vectors — but a gene can have 2 neighbors or 200 neighbors. GNNs handle this variable connectivity natively.

## Core Mechanism: Message Passing

Every GNN works through the same fundamental operation — **message passing** (also called neighborhood aggregation):

```
Round 0: Each node starts with its own features

  A[0.5]───B[0.3]───C[0.8]
  │
  D[0.1]

Round 1: Each node collects information from its direct neighbors

  A_new = f(A_self, messages from B, D)
  B_new = f(B_self, messages from A, C)
  C_new = f(C_self, messages from B)
  D_new = f(D_self, messages from A)

Round 2: Each node collects from already-updated neighbors

  A_new = f(A', messages from B', D')
  → A now indirectly "knows about" C (through B)
     and has no new info (D has no other neighbors)
```

### Analogy: Neighborhood Gossip

```
Round 1: You learn what your direct neighbors know
Round 2: You learn what your neighbors' neighbors know
Round 3: Three hops away...
...
Round K: You have information from K hops away
```

After K rounds of message passing, each node's representation encodes information about its **K-hop neighborhood** in the graph.

## How a GNN Layer Works (Simplified)

```python
# Pseudocode for one GNN layer
for each node v:
    # 1. Collect messages from neighbors
    messages = [transform(neighbor.features) for neighbor in v.neighbors]
    
    # 2. Aggregate messages (sum, mean, or max)
    aggregated = sum(messages)  # or mean() or max()
    
    # 3. Update node representation
    v.new_features = update(v.features, aggregated)
```

The `transform`, `aggregate`, and `update` functions are learned during training. Different GNN variants differ in how they implement these three steps:

| GNN Variant | Key Idea | Used in Wiki |
|-------------|----------|-------------|
| **GCN** (Graph Convolutional Network) | Normalized mean of neighbors | General purpose |
| **GAT** (Graph Attention Network) | Learned attention weights per neighbor | [[drug-resistance/alsulami-2026-predicting-and-interpreting-cell]] (PrePR-CT) |
| **GraphSAGE** | Samples fixed number of neighbors | [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] (GEARS) |
| **GIN** (Graph Isomorphism Network) | Sum aggregation, maximally expressive | Theoretical baseline |

## GNN vs MLP vs VAE — When to Use What

| | MLP | VAE | GNN |
|---|---|---|---|
| Input | Fixed-size vector | Fixed-size vector | Graph (variable neighbors) |
| Structure | No relationships | No relationships | Explicit relationships |
| Strength | Simple, fast | Smooth latent space, generation | Captures relational structure |
| Biology use | Gene expression → prediction | Cell embedding, generation | Gene networks, pathway graphs |

**Key insight**: GNN and VAE are not alternatives — they answer different questions:
- VAE asks: "what is this data point like?" (compression/generation)
- GNN asks: "what is this data point's neighborhood like?" (relational reasoning)

## GNN in GEARS — Detailed Walkthrough

[[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]]

GEARS uses **two separate GNNs** on two different graphs:

### GNN 1: Gene Coexpression Graph

**Purpose**: learn which genes respond similarly to perturbation

```
Step 1: Build graph from data
  - Compute Pearson correlation between all gene pairs
  - For each gene, connect to top-H most correlated genes (above threshold δ)
  
  Result:
    FOXO1 ─── FOXO3        (correlation = 0.85)
      │         │
    BCL2 ───── BAX          (correlation = 0.79)
      │
    CASP3                   (correlation = 0.71)

Step 2: Initialize each gene with a learnable embedding vector
    FOXO1 → [0.1, 0.3, -0.2, ...]  (random at start)
    FOXO3 → [0.5, -0.1, 0.4, ...]  (random at start)

Step 3: Run GNN message passing
    FOXO1_new = GNN(FOXO1_self, [FOXO3, BCL2])
    → FOXO1's representation now encodes:
      "I am coexpressed with FOXO3 and BCL2"

Step 4: After training
    FOXO1 → [0.7, 0.2, -0.1, ...]  (learned: captures coexpression context)
```

**What this embedding means**: genes that share coexpression partners end up with similar embeddings → the model assumes they will respond similarly to perturbation.

### GNN 2: GO Perturbation Graph

**Purpose**: enable prediction for genes never seen perturbed

```
Step 1: Build graph from Gene Ontology
  - Compute Jaccard similarity of GO term annotations between gene pairs
  - For each gene, connect to top-H most similar genes
  
  Result:
    BRCA1 ─── RAD51        (shared: DNA repair, response to DNA damage, ...)
      │
    TP53 ──── MDM2         (shared: apoptosis, cell cycle, ...)

Step 2: Initialize perturbation embeddings (one per gene)
    BRCA1_pert → [random...]
    RAD51_pert → [random...]

Step 3: Run GNN message passing
    BRCA1_pert_new = GNN(BRCA1_pert_self, [RAD51, TP53])

Step 4: Key benefit — unseen gene prediction
    If BRCA2 was never perturbed in training, but BRCA2 is connected 
    to BRCA1 and RAD51 in the GO graph:
    → BRCA2's perturbation embedding inherits information from its 
      neighbors who WERE perturbed
    → The model can make a prediction for BRCA2 knockout
```

### How the Two GNNs Combine

```
Predict: "What happens when we knock out gene X?"

  GNN 1 (coexpression)          GNN 2 (GO)
       │                              │
  gene embedding              perturbation embedding
  "how gene X behaves          "what pathways gene X
   with other genes"            affects when perturbed"
       │                              │
       └──────────┬───────────────────┘
                  │
            Combined per gene
                  │
         Cross-gene decoder
                  │
    Predicted post-perturbation expression
```

## GNN in Other Wiki Papers

### PrePR-CT (Graph Attention Network)
[[drug-resistance/alsulami-2026-predicting-and-interpreting-cell]]

```
Graph: cell-type-specific gene coexpression network
Nodes: genes
Edges: coexpression within a cell type
GNN type: GAT (attention-weighted neighbors)

Key difference from GEARS:
- GEARS builds ONE coexpression graph from all cells
- PrePR-CT builds SEPARATE graphs per cell type
  → captures cell-type-specific gene relationships
```

### CellOracle (not exactly GNN, but graph-based)
[[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]]

```
Graph: directed GRN (TF → target)
  - Direction comes from motif scans on open chromatin (scATAC)
  - Not a GNN (uses linear propagation instead)
  - But same principle: propagating signal along a graph of gene relationships
```

### GRouNdGAN
[[genomic-dl/zinati-2024-groundgan-grn-guided]]

```
Graph: ground-truth or inferred GRN
  - GRN structure guides the GAN's generator
  - Causal masking: generator can only use TF→target edges
```

## GNN vs VAE for Encoding Gene Relationships: Summary

This is the core architectural difference between GEARS and PerturbNet:

```
GEARS (GNN approach):
  
  Genes as NODES in a graph, GO similarity as EDGES
  
     A ─── B ─── C ─── D
  
  Information flows along edges (message passing)
  → Structure matters: who is connected to whom
  → Isolated nodes get poor representations
  → Explicit network reasoning

PerturbNet (VAE approach):

  Genes as VECTORS (GO annotations), no graph structure
  
     A[0,1,1,0,1]    B[0,1,0,0,1]    C[1,0,0,1,0]
           ↓                ↓               ↓
         VAE              VAE             VAE
           ↓                ↓               ↓
         z_A              z_B             z_C
  
  Similar vectors → nearby z points (by training)
  → Distance matters: how similar are the annotation vectors
  → Every gene gets a representation (no isolation problem)
  → Smooth interpolation between genes
```

| Property | GNN (GEARS) | VAE (PerturbNet) |
|----------|-------------|------------------|
| Handles variable #neighbors | Yes (native) | N/A (no neighbors) |
| Captures network topology | Yes | No |
| Smooth interpolation | Limited | Yes |
| Isolated nodes/genes | Poor representation | Still gets representation |
| Multi-hop reasoning | Yes (K rounds = K hops) | No (each gene encoded independently) |
| Scalability | Depends on graph size | Fixed vector dimension |

**Neither is strictly better** — GNNs excel when the graph structure itself is informative (as in gene regulatory networks); VAEs excel when smooth interpolation between data points matters (as in generating novel perturbation predictions).

---

*Used in: [[single-cell-dl/roohani-2023-predicting-transcriptional-outcomes-of]] (GEARS — dual GNN), [[drug-resistance/alsulami-2026-predicting-and-interpreting-cell]] (PrePR-CT — GAT), [[genomic-dl/zinati-2024-groundgan-grn-guided]] (GRouNdGAN), [[single-cell-dl/kamimoto-2023-dissecting-cell-identity-via]] (CellOracle — graph-based but not GNN)*
