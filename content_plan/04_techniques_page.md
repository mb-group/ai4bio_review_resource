# 04. Techniques Page (and how it differs from Concepts)

## 1. The problem

Many items are both a *concept* (a PI needs the idea to follow the argument) and a *technique* (staff need to know how it is done). Examples: self-supervised learning, fine-tuning, retrieval-augmented generation. We want a PI to be satisfied by the concept, and a trainee to be able to go deeper, without two disconnected pages saying the same thing twice.

## 2. The rule

Ask one question: **"What does the reader want to do with this?"**

| If the reader wants to... | It is a... | Lives on | Depth |
|---|---|---|---|
| Understand the argument and judge it | **Concept** | Concepts page | Short definition (≤3 sentences) and why it matters in the review |
| Choose, implement, or evaluate it | **Technique** | Techniques page | How it works, variants, requirements, pitfalls, which models use it |

Practical tests (any one is enough):
- *Would the argument fall apart for a PI who didn't know it?* → concept.
- *Would a trainee need it to reproduce or apply something?* → technique.
- *Does it have variants or a choice to make?* (e.g., k-mer vs. learned tokens) → technique.
- *Is it an idea or a label with nothing to "do"?* (e.g., grammar, corpus, knowledge boundary) → concept only.

Result is three kinds:

| Kind | Meaning | Shown on |
|---|---|---|
| **concept** | Idea or label | Concepts page only |
| **both** | Idea that is also a method | Both pages, same short definition, different depth |
| **technique** | Implementation-level detail that the argument does not need | Techniques page only |

## 3. One record, two views (not two records)

For a "both" term, keep **one record** with two optional blocks:

- The **short definition** is written once and shown on both pages (shared, never copied).
- The **concept block** adds: why it matters in the review, examples (folded).
- The **technique block** adds: how it works, variants, requirements and pitfalls, "used by" models.
- Two buttons connect the views: **"How it's done →"** on the Concepts entry, **"What it means →"** on the Techniques entry.

This keeps the two pages from drifting apart and makes the PI/staff handoff one click.

## 4. Techniques page layout

- **Grouped by the review's five design elements, plus agent components.** This reuses the framework readers already know and makes techniques map directly to where a boundary comes from.
  1. Data and tokenization
  2. Architecture
  3. Training scheme
  4. Evaluation
  5. Post-analysis
  6. Agent components
- Filters: group, kind (both / technique-only), model used.
- Entry anatomy:

```
[Technique name]                                   [group]
Short definition (shared with Concepts if "both")   What it means → (if concept exists)
How it works          steps or variants
When to choose it / pitfalls     (link to the relevant design element and, where the review says so, to the boundary it creates)
Used by               model links
Related techniques    links
Mentioned in          (automatic)
References
```

Content discipline: write technique entries only from what the review and its references support; mark gaps as "Not covered in the review" and let authors/curators extend them deliberately.

## 5. Master term list (starter; authors to confirm)

**How to read the Landing column.** The landing page now has 26 beats (`ARBDS_claims_beats_v2_EN.md`), so a term's old "home claim" is no longer always a place where its name is written. Each term is in one of three states:

- **Linked**: the word is written in a beat (in the headline, supporting text, or a row label) and is a link to the term. The beat is the term's *home beat*. 37 terms.
- **Section term**: no beat carries the word. The term sits on the Concepts page in review order and is reached from the beat of its section through one link, "Terms in this section (n) →". 27 terms.
- **Evidence-only** (`example_only`): no landing link and no section link; reached from examples and the Concepts page. 3 terms.

"Source claim" is the claim of the original (72-claim) structure where the term first appeared; it is kept for traceability. IDs match `ARBDS_content_rehomed_EN.md`. A claim ID maps to its beat through the beat's `covers` list.

### 5.1 Concept only (Concepts page)

| Term | Id | Landing | Source claim |
|---|---|---|---|
| Biological foundation model (FM) | `biological-foundation-model` | **linked** in `A-01` | A-01 |
| Agentic system | `agentic-system` | **linked** in `A-01` | A-01 |
| Knowledge boundary | `knowledge-boundary` | **linked** in `A-01` | A-02 |
| Knowledge extraction from data | `knowledge-extraction` | section term, §1 (beat `1-01`) | 1-01 |
| Embedding | `embedding` | **linked** in `2.1.1-01` | 1-04 |
| Compression vs. composability | `compression-vs-composability` | **linked** in `1-04` | 1-04 |
| Correlation vs. causation | `correlation-vs-causation` | **linked** in `4.1-01` | 1-04 |
| Large language model (LLM) | `llm` | **linked** in `1-04` | 1-05 |
| Supervised learning | `supervised-learning` | section term, §2.1 (beat `2.1-01`) | 2.1-01 |
| Vocabulary | `vocabulary` | **linked** in `2.1.1-01` | 2.1.1-02 |
| Token | `token` | **linked** in `2.1.1-01` | 2.1.1-02 |
| Grammar | `grammar` | **linked** in `2.1.1-01` | 2.1.1-03 |
| Regulatory DNA | `regulatory-dna` | section term, §2.1.1 (beat `2.1.1-01`) | 2.1.1-03 |
| Transcription factor (TF) binding motif | `tf-binding-motif` | section term, §2.1.1 (beat `2.1.1-01`) | 2.1.1-03 |
| Corpus | `corpus` | **linked** in `2.1.1-01` | 2.1.1-04 |
| The five design elements | `five-design-elements` | **linked** in `2.1.2-01` | 2.1.2-01 |
| Generalization | `generalization` | section term, §2.1.2 (beat `2.1.2-01`) | 2.1.2-01 |
| Inductive bias | `inductive-bias` | section term, §2.1.2 (beat `2.1.2-01`) | 2.1.2-03 |
| Inputs vs. outputs (data axis, task axis) | `inputs-vs-outputs` | **linked** in `2.2-01` | 2.2-01 |
| Bulk RNA sequencing | `bulk-rna-seq` | section term, §2.2.1 (beat `2.2-01`) | 2.2.1-01 |
| Spatial transcriptomics | `spatial-transcriptomics` | section term, §2.2.1 (beat `2.2-01`) | 2.2.1-01 |
| Representation model | `representation-model` | **linked** in `2.2-01` | 2.2.2-01 |
| Predictive model | `predictive-model` | **linked** in `2.2-01` | 2.2.2-01 |
| Generative model | `generative-model` | **linked** in `2.2-01` | 2.2.2-01 |
| Perturbation model | `perturbation-model` | section term, §2.2.2 (beat `2.2-01`) | 2.2.2-01 |
| Hallucination | `hallucination` | section term, §3 (beat `3-01`) | 3-01 |
| Decipherment questions | `decipherment-questions` | **linked** in `4-01` | 4-01 |
| Orchestration boundary | `orchestration-boundary` | **linked** in `4-01` | 4-02 |
| The four layers of the boundary | `four-layers` | **linked** in `4.3-08` | 4.3-08 |
| Sampling bias | `sampling-bias` | none (`example_only`; hosts §4.3 evidence) | 4.3-08 |
| Circular annotation | `circular-annotation` | none (`example_only`; hosts §4.3 evidence) | 4.3-08 |
| Systematic variation | `systematic-variation` | none (`example_only`; hosts §4.3 evidence) | 4.3-08 |
| Scaling laws | `scaling-laws` | **linked** in `5.2-01` | 5.2-01 |
| Stages of biological science | `stages-of-biological-science` | **linked** in `5.3-01` | 5.3-02 |
| Adaptive radiation | `adaptive-radiation` | **linked** in `5.3-01` | 5.3-03 |
| Boundary statement | `boundary-statement` | **linked** in `6.2-01` | 6.2-02 |
| Shared literacy | `shared-literacy` | **linked** in `6.3-01` | 6.3-02 |
| Model registry (proposed) | `model-registry` | **linked** in `6.3-01` | 6.3-03 |

### 5.2 Both (Concepts page and Techniques page)

| Term | Id | Landing | Source claim | Technique group |
|---|---|---|---|---|
| Self-supervised learning | `self-supervised-learning` | **linked** in `2.1-01` | 2.1-01 | Training scheme |
| Probing | `probing` | **linked** in `2.1-01` | 2.1-02 | Post-analysis |
| Fine-tuning | `fine-tuning` | **linked** in `2.1-01` | 2.1-02 | Post-analysis |
| Zero-shot prediction | `zero-shot-prediction` | **linked** in `2.1-01` | 2.1-02 | Post-analysis |
| Sparse autoencoder | `sparse-autoencoder` | section term, §2.1.1 (beat `2.1.1-01`) | 2.1.1-05 | Post-analysis |
| Transformer and self-attention | `transformer` | section term, §2.1.2 (beat `2.1.2-01`) | 2.1.2-03 | Architecture |
| Masked language modeling | `masked-language-modeling` | section term, §2.1.2 (beat `2.1.2-01`) | 2.1.2-04 | Training scheme |
| Autoregressive modeling | `autoregressive-modeling` | section term, §2.1.2 (beat `2.1.2-01`) | 2.1.2-04 | Training scheme |
| Contrastive / metric learning | `contrastive-learning` | section term, §2.1.2 (beat `2.1.2-01`) | 2.1.2-04 | Training scheme |
| Intrinsic vs. downstream evaluation | `intrinsic-vs-downstream-evaluation` | section term, §2.1.2 (beat `2.1.2-01`) | 2.1.2-05 | Evaluation |
| Transfer learning | `transfer-learning` | section term, §2.1.2 (beat `2.1.2-01`) | 2.1.2-06 | Post-analysis |
| In silico perturbation | `in-silico-perturbation` | section term, §2.1.2 (beat `2.1.2-01`) | 2.1.2-06 | Post-analysis |
| Interpretability analysis | `interpretability-analysis` | section term, §2.1.2 (beat `2.1.2-01`) | 2.1.2-06 | Post-analysis |
| Graph neural network | `graph-neural-network` | section term, §2.2.1 (beat `2.2-01`) | 2.2.1-01 | Architecture |
| Retrieval-augmented generation (RAG) | `rag` | section term, §3 (beat `3-01`) | 3-02 | Agent components |
| Function calling | `function-calling` | section term, §3 (beat `3-01`) | 3-02 | Agent components |
| Reasoning model | `reasoning-model` | **linked** in `3-01` | 3-02 | Agent components |
| Model Context Protocol (MCP) | `mcp` | section term, §3 (beat `3-01`) | 3-03 | Agent components |
| Skill files | `skill-files` | section term, §3 (beat `3-01`) | 3-03 | Agent components |
| Agent harness | `agent-harness` | section term, §3 (beat `3-01`) | 3-03 | Agent components |
| Multi-agent system | `multi-agent-system` | section term, §3 (beat `3-01`) | 3-04 | Agent components |
| Tool route | `tool-route` | **linked** in `3-05` | 3-05 | Agent components |
| Text route | `text-route` | **linked** in `3-05` | 3-05 | Agent components |
| Encoder route | `encoder-route` | **linked** in `3-05` | 3-05 | Agent components |
| Verifier route | `verifier-route` | **linked** in `3-05` | 3-05 | Agent components |
| Reinforcement learning | `reinforcement-learning` | **linked** in `3-07` | 3-07 | Training scheme |
| Convolutional neural network (CNN) | `cnn` | section term, §4.1 (beat `4.1-01`) | 4.1-03 | Architecture |
| Simple baselines | `simple-baselines` | **linked** in `4.3-01` | 4.3-01 | Evaluation |
| Self-driving laboratory | `self-driving-lab` | **linked** in `6.2-03` | 6.2-04 | Agent components |

**Two terms changed home** because of the new text: *Embedding* is first linked in a row of `2.1.1-01` (it was `1-04`), and *Correlation vs. causation* in `4.1-01` (it was `1-04`).

**Design-element filter.** The row labels in `2.1.2-01` and `4.1-01` open the Concepts page filtered by design element, so every term needs a `design_element`. The 29 "both" terms get it from their technique group (data and tokenization → data; architecture; training scheme; evaluation; post-analysis; agent components have none). The concept-only terms *Generalization*, *Inductive bias*, and any others the authors want in a filter need one assigned by the authors.

### 5.3 Technique only (Techniques page; they appear inside examples, not in the argument)

| Term | Technique group | Source in the draft (claim IDs; many are now demoted claims whose content lives as examples or model-entry text) |
|---|---|---|
| *k*-mer tokenization | Data and tokenization | 2.1.1-02, 2.2.1-02 (Nucleotide Transformer) |
| Learned variable-length tokens | Data and tokenization | 2.2.1-02 (DNABERT-2, GROVER) |
| Single-nucleotide tokenization | Data and tokenization | 2.2.1-02 (HyenaDNA, Caduceus, Evo) |
| Expression-rank encoding | Data and tokenization | 2.2.1-04 (Geneformer) |
| Binned expression-value encoding | Data and tokenization | 2.2.1-04 (scGPT) |
| Genes represented by protein embeddings | Data and tokenization | 2.2.1-04, 4.2-05 (UCE) |
| Structure and function tokens | Data and tokenization | 2.2.1-06 (SaProt, ESM3) |
| Prior-knowledge-enriched tokens | Data and tokenization | 2.2.1-07 (GeneCompass) |
| Sequence clustering before training | Data and tokenization | 2.1.1-04 |
| Alignment-augmented input | Data and tokenization | 4.2-05 (GPN-MSA) |
| Long-context architectures | Architecture | 2.1.2-03, 4.1-03 (HyenaDNA, Caduceus) |
| Likelihood scoring of variants | Training scheme | 2.1-02, 4.2-03 |
| Prompting with partial structure or function | Training scheme | 2.2.2-04 (ESM3) |
| Similarity-aware train/test splitting | Evaluation | 4.1-05, 4.3-06 |
| Calibrated metrics (mean baseline + positive control) | Evaluation | 4.3-05 |
| Shuffled-input control | Evaluation | 5.1-03 |
| Packaging a model as an MCP tool | Agent components | 3-05 (Paper2Agent) |

**After compression** (72 claims → 26 beats): claims 2.2.1-02…07, 2.2.2-02…04, 4.2-02…06 and 4.3-02…07 are no longer scroll steps; their content now lives as examples under concepts (suggested hosts are in `ARBDS_claims_compressed_EN.md`) and as text in model entries. The IDs in the "Source" column therefore point to where the item originates in the draft, not to a landing-page claim. *Scaling laws* has its home at 5.2-01 but may also host the 4.3-03 evidence; the authors may move its home earlier.

**Judgement calls to confirm**: *embedding* is kept concept-only (its "how" is covered by probing and sparse autoencoders). *Self-driving laboratory* is marked "both" mainly so the closed-loop idea in §6.2 has a technique home; it could be concept-only. Adding "co-expression" as a concept (it is used in 2.2.1-04) is optional.

## 6. Acceptance checks

1. Each "both" term exists once, and its short definition is stored once (not duplicated across pages).
2. The two buttons ("How it's done →", "What it means →") appear only where the other view exists.
3. Every technique entry is placed in exactly one group.
4. Every technique-only term that appears in an example is a link from that example.
5. A reader who stops at the Concepts page never meets an unexplained method word: if they might, the word is linked.
