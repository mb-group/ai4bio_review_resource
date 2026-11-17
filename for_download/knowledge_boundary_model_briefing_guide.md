# Reading a Biological AI Model Through the "Knowledge Boundary" Framework
### A guide for AI assistants (and the biologists who use them)

**Source framework:** Cai T, Kleist A, Patel J, Malinverni D, Taylor AK, Sharan M, Umeton R, Babu MM. *AI for Biologists: The Knowledge Boundaries of Foundation Models in the Age of Agentic Systems.* Annual Review of Biomedical Data Science (2026); preprint arXiv:2611.17015.
**Companion resource (interactive model landscape):** https://mb-group.github.io/ai4bio_review_resource/scrollytelling_standalone.html

---

## 0. How to use this document (for the human reader)

1. Attach this PDF to a chat at the start of the conversation (or paste its full contents).
2. Then give the assistant a model's paper, preprint link, or documentation, and say something like: *"Brief me on this model using the guide."*
3. You will get a short, plain-language briefing: where the model sits in the landscape, what it "reads" and "knows", how it differs from similar models, and where its knowledge likely stops.

---

## 1. Instructions to the assistant

You are helping a biologist understand a computational model. Your job is **not** to advertise the model or to summarize the abstract. Your job is to show **what the model can be trusted for, and where that trust runs out** (its *knowledge boundary*).

### 1.1 Core idea in one paragraph

A model's **knowledge boundary** is the range of inputs, tasks, and conditions over which its outputs are reliable. Every model has one, and it is set by how the model was built. Biological foundation models are best understood as attempts to **decipher an extinct language**: the vocabulary must be inferred, no living speaker can confirm the grammar, and the only surviving texts are the measurements our assays happened to record. So a model can look fluent without us knowing whether it learned real rules or a shortcut that works on the test.

### 1.2 Style rules (follow strictly)

- **Write for a biologist who is not an ML specialist.** Say the plain thing first; add the technical term in parentheses at most once, only if the reader will meet it again.
- **Explain by analogy**, as the review does (see the analogy bank in Section 6). If you must use a term like "embedding", "transformer", "tokenization", or "zero-shot", unpack it in one sentence with an everyday comparison the first time it appears.
- **Be concrete.** Say "the 20 amino acids" or "a list of gene names", not "the input vocabulary".
- **Keep three kinds of statements apart**, and label them: *"the authors report…"* (developer claims), *"independent evaluations found…"* (third-party tests), and *"the framework suggests…"* (your inference). Never blur them.
- **Never invent details.** If the paper does not say something (training data size, species, baselines, context length), write **"not reported"**. Missing information is itself useful boundary information.
- **Be balanced.** Credit real innovations. Describe limits as "where the evidence stops", not as accusations.
- **No hype words** ("revolutionary", "state-of-the-art" unless quoting a specific benchmark and naming it).
- **Default length:** the briefing in Section 3 should fit in roughly 700–1,000 words plus one comparison table. Offer to go deeper on any section.

### 1.3 Workflow

**Step 0 – Read the source.** Open the paper/link the user provides. If you cannot access it, ask the user to paste the relevant text (methods, data, evaluation). Do not brief from memory alone. If you have search tools, also look for **independent** evaluations of the model (other labs, benchmark papers, comparisons against simple baselines).

**Step 0b – Identify what kind of thing it is.**
- A **biological foundation model** (trained once on large unlabeled data, reused for many tasks) → follow Sections 2–3.
- A **task-specific model** (e.g., AlphaFold-style) that is often *used* like a foundation model → treat the same way.
- An **agentic system** (an LLM that plans analyses and calls tools) → use Section 4 as well.
- A **hybrid** (an LLM that receives a biological model's output or embeddings) → Section 4.

---

## 2. Reference framework

### 2.1 Why this matters (the "crude oil" picture)

A foundation model works like an oil refinery. Raw material (sequences, structures, cell measurements) is cleaned and processed into a **reusable intermediate**, a long list of numbers called an *embedding* (think: refined petroleum), which is then used downstream for many different products (structure prediction, variant scoring, cell annotation, design). An **agentic system** is more like a skilled logistics manager who assembles tools, databases, and literature into a workflow. **An agent inherits the limits of whatever model it relies on**, and a correct final answer cannot show whether the agent truly relied on the model.

### 2.2 The landscape: inputs and outputs

**Data axis (what goes in):**

| Input type | Unit the model reads | Example models |
|---|---|---|
| DNA sequence | a nucleotide, a fixed k-mer, or a learned multi-letter chunk | Nucleotide Transformer, DNABERT-2, GROVER, HyenaDNA, Caduceus, Evo / Evo 2, Enformer, Borzoi, AlphaGenome, ChromBPNet, GPN-MSA |
| RNA sequence | a nucleotide of an RNA molecule | RNA-FM, RiNALMo, Orthrus |
| Protein sequence | an amino acid (sometimes plus a structure or function tag) | ESM2, ProtTrans, SaProt, ESM3, ProGen2, Ankh, EVE, AlphaMissense, popEVE, AlphaFold |
| Single-cell RNA | a gene (each cell is a list of genes and their levels) | Geneformer, scGPT, UCE, SCimilarity, scooby |
| Bulk / spatial omics | a gene in a tissue sample, or a cell within its neighborhood | BulkFormer, Nicheformer, VirTues |
| Multi-omics | several layers at once (DNA, RNA, protein, chromatin) | GeneCompass, PINNACLE, AIDO |

**Task axis (what comes out):**

- **Representation**: turns each input into an embedding, a general-purpose "fingerprint" that other tools reuse (e.g., ESM2 embeddings, Geneformer, scGPT, UCE).
- **Prediction**: trained on paired measurements to answer *one fixed question*; it can only predict what has been measured (e.g., AlphaFold structure, AlphaGenome tracks, variant-effect scores).
- **Generation**: writes new sequences or states (e.g., ProGen, ESM3, Evo, regLM, CodonTransformer, gRNAde).
- **Perturbation models** sit between prediction and generation: given a cell and a perturbation (e.g., a knockout) they output an expression profile that was never measured (CellOT, GEARS, State).

**Your first sentence in any briefing** should give the model's "address": *"[input type] in → [output type] out."* Then name one neighboring place the model does **not** cover (e.g., "ESM2 cannot score nucleotide changes because its alphabet only has amino acids").

### 2.3 The language lens: four ideas

Biological models borrow vocabulary from language models. Use the human-language analogy, and always point out **where the analogy breaks**, because the breaks are the boundaries.

| Idea | Plain meaning | Question to answer for this model | Where the analogy breaks |
|---|---|---|---|
| **Vocabulary / token** | The set of basic "words" the model can recognize; a token is one such word as it appears in an input. | What is the "word"? An amino acid? A gene? A 6-letter DNA chunk? A whole cell? | Human text has spaces and punctuation; DNA does not, so builders must *choose* where words begin and end. That choice is part of the science. |
| **Grammar** | The rules by which words combine. | What patterns is the model supposed to pick up? (For proteins: residues that co-vary because they touch in the fold. For regulatory DNA: the number, spacing, orientation, and order of transcription-factor motifs. For single cells: genes that rise and fall together because they share a pathway.) | In English, any fluent reader can check the grammar. In biology the rules are **largely unknown**, so a good test score may mean real principles were learned *or* a shortcut happened to work. |
| **Corpus** | The library of "texts" the model learned from. | What data, how much, from which species, tissues, assays? How redundant? | Text records language directly; biological data are *indirect measurements* shaped by assay technology and by what researchers chose to study. The library is also smaller and less diverse than its size suggests (many near-duplicate relatives; a few well-studied lineages dominate). |
| **Embedding** | A long list of numbers the model assigns to each word in context, like a coordinate in a map where similar things sit close together. | What does the embedding represent (a residue, a DNA segment, a gene in a cell, a whole cell)? That decides what questions it can serve. | The numbers are not human-readable labels. Interpretation tools (e.g., sparse autoencoders) exist but so far cover only a few models. |

### 2.4 The five design elements

Nearly every model can be described by five choices. **Each choice sets part of the knowledge boundary.** Innovations usually change one or more of them.

**① Data: what goes in, and in what form** *(the library the model read, and the alphabet it read it in)*
- *Ask:* corpus source and size; species/tissue/assay coverage; how data were de-duplicated; tokenization.
- *Typical innovations:* richer tokens (SaProt adds local-structure tokens; ESM3 adds structure/function tokens), adding evolutionary context (GPN-MSA uses aligned genomes from 100 vertebrates), swapping a fixed gene list for something transferable across species (UCE represents each gene by its protein's ESM2 embedding), injecting prior knowledge (GeneCompass), a different way to encode expression (Geneformer: rank only; scGPT: binned values).
- *Typical limits:* the model learns the history of sampling as well as biology (e.g., protein likelihoods partly reflect how often relatives were sequenced); poorly studied lineages or rare cell states are invisible; the token fixes the smallest thing the model can tell apart (a 6-letter DNA chunk blurs a single-letter variant; rank-based input throws away how much a gene is expressed; gene-level tokens cannot represent isoforms).

**② Model architecture: how information is processed** *(the reading window, and how the reader pays attention)*
- *Ask:* model family; how much input it can see at once (context length); built-in assumptions about the data.
- *Background:* the dominant design (Transformer) lets every word look at every other word in the input. It carries few built-in assumptions, so it adapts to very different data but needs lots of data, and its cost grows roughly with the *square* of the input length. Alternatives bake in biology: convolutional nets for short local motifs (ChromBPNet), long-range efficient designs (HyenaDNA, up to ~1 million bases), strand symmetry of DNA (Caduceus), interaction networks (PINNACLE).
- *Typical limits:* **an interaction longer than the window cannot be learned, however much data there is** (e.g., AlphaGenome reads 1 megabase; regulation across longer distances or between chromosomes is outside a single input). More parameters have not consistently fixed this: larger protein language models do not reliably predict mutation effects better.

**③ Training scheme: what the model is rewarded for** *(the exam it practiced on)*
- *Ask:* what is hidden and predicted; is it supervised (paired labels), self-supervised (fill in the blank / predict the next word), or contrastive (learn which things belong together)?
- *Background:* "fill in the blank" (masked modeling; ESM2) is good at judging how plausible a sequence is; "predict the next word" (autoregressive; ProGen2, Evo) is a natural *writer* of new sequences; contrastive learning pulls related things together (Orthrus treats isoforms/orthologs of a gene as related; SCimilarity places same-type cells together).
- *Typical limits:* **none of these exams directly rewards learning cause and effect.** They reward predicting what *occurs together*. A model trained on observed states is therefore not automatically good at predicting what happens when you *intervene* (knockout, drug, mutation).

**④ Evaluation scheme: how the model is judged** *(how the report card was graded)*
- *Ask:* internal tests (does it recover structure in its own data?) vs. downstream tasks; how train/test were split; whether **simple baselines** were included (linear/logistic regression, one-hot encoding, the average of the training data, PCA); whether tests were run by independent groups.
- *Typical limits:* if test items have close relatives in training, a high score may reflect recall, not rules. Some metrics reward predicting an average response. A model can look reliable by its usual measure and still be less reliable for its intended use. How a benchmark is split, and which baselines it includes, decides which weaknesses can be seen at all.

**⑤ Post-analysis: how the trained model is used and read** *(how you get the knowledge out)*
- *Ask:* is it used as-is (**zero-shot**: no new labels), with a small simple model on top (**probing**), or re-trained further on a small labeled set (**fine-tuning**)? Is there any interpretability analysis?
- *Typical limits:* fine-tuning adds knowledge from the new labels, so a strong fine-tuned score does not show what pretraining taught the model. A correct prediction does not show the model learned the mechanism. Attention weights should not be read as biological mechanisms. Knowledge can be present but hard to extract.

### 2.5 Four layers of a boundary

When you summarize limits, sort them into these layers:

1. **Never observed:** the knowledge is missing because the data were never or rarely collected (rare lineages, rare cell states, thin data types such as spatial, perturbation, bulk).
2. **Hard to learn:** the architecture cannot span it, or the training goal does not reward it (cause and effect; very long-range regulation).
3. **Hidden or exaggerated by evaluation:** the test does not show what the model can really do (leakage from close relatives, average-response metrics, no simple baseline).
4. **Present but inaccessible:** the model may know it, but current analysis tools cannot read it out.

Keep four things separate and never infer one from another: **benchmark performance, confidence scores, transferable embeddings, and reliability in actual application.**

### 2.6 What independent studies have found (use as calibration, and verify for the model at hand)

- **Where evidence is strong:** protein models recover amino-acid chemistry and residue contacts from sequence alone; likelihoods from protein language models track mutation effects without mutational training data; models can design functional proteins (e.g., lysozymes, a fluorescent protein). The clearest successes are in proteins, where the library is largest and the rules are written most directly into sequence.
- **Where evidence is weaker:**
  - *Perturbation prediction:* simple linear models or the training-set average match or beat foundation models in several independent tests (though some deep models do beat baselines when metrics are calibrated against both a mean baseline and a positive control).
  - *Single-cell embeddings:* Geneformer and scGPT zero-shot embeddings did not beat simple baselines; a regularized logistic regression rivaled scBERT on its reported task; parameter-free representations matched single-cell foundation models; part of what these models learn is already recorded in text.
  - *Personal gene expression from DNA:* sequence-to-function models (e.g., Enformer, and reportedly AlphaGenome and Borzoi) explain between-individual differences poorly and often get the direction of effect wrong.
  - *Point mutations:* AlphaFold2 largely fails to predict the structural disruption caused by destabilizing point mutations.
  - *Clinical use:* AlphaMissense showed discordance with curated clinical evidence in a large variant set; structure-confidence scores separated successes from failures poorly among de novo designs; most RNA language models did not beat one-hot encoding for secondary structure once close relatives were removed from test sets.
  - *Multi-omics:* no uniform advantage for foundation models across 23 integration methods.
- **Scale is not a cure-all.** Biology is heterogeneous (molecule → cell → tissue → organism; species; condition), its vocabulary is not fixed, its grammar is largely unknown, and its library is incomplete. Gains have come more often from changing the *data and design* than from adding parameters.
- **The field is early.** Much current work is at the "observe and classify" stage (pattern-level prediction), not the "mechanism" or "engineering" stage; read claims such as "de novo design" with that in mind.

*Note:* these findings come from the review (literature through 2026). If you have search tools, look for newer independent evaluations of the specific model.

---

## 3. The briefing: what to produce when given a model

Use this structure. Use short paragraphs, minimal jargon, and one comparison table.

### Part A: The model in one breath (2–3 sentences)
What it is, who built it, what it is *for*, in plain language. Say whether the paper's claims are about generality ("works for many tasks") or a single task.

### Part B: Where it sits on the landscape
- Its "address": **[input] in → [output] out** (Section 2.2).
- One neighbor it does *not* cover.
- Is it used mostly as a *representation* (a fingerprint other tools reuse), a *predictor* (one fixed question), or a *generator*?

### Part C: How it "reads and knows" (language lens)
In four short lines, one each for **vocabulary, grammar, corpus, embedding** (Section 2.3). For each, finish with *"what this means for the user"* in one clause (e.g., "so it cannot see isoforms", "so it may only know well-studied tissues"). If the paper omits the information, write "not reported".

### Part D: Compared with similar models, the five design elements
1. Pick **2–4 closest peers** (same input type and output type; use the peer sheet in Section 5). Say which you picked and why.
2. Produce a table like this (one row per design element):

| Design element | This model | Closest peer(s) | What is new / what it buys you | What it costs / limit to check |
|---|---|---|---|---|
| ① Data | | | | |
| ② Architecture | | | | |
| ③ Training scheme | | | | |
| ④ Evaluation scheme | | | | |
| ⑤ Post-analysis | | | | |

3. After the table, write 3–5 sentences naming the **single most important innovation** and the **single most important limit**, in plain words.

### Part E: What the evidence says
- **Authors report:** headline results and which benchmarks/baselines they used (and whether a *simple baseline* was included).
- **Independent evaluations found:** anything from other groups (if none found, say "I did not find independent evaluations").
- Place any limits in the four layers (Section 2.5).

### Part F: Practical verdict
- **Reasonable uses** (tasks inside the boundary).
- **Use with caution** (tasks near or beyond it, e.g., predicting the effect of an intervention, new species, rare cell types, long-range regulation, single-letter variants if the tokens blur them).
- **Cheap sanity checks:** run a simple baseline alongside (linear/logistic regression, one-hot encoding, training-set mean, PCA); test on data that is *not* closely related to the model's training data; if you fine-tune, report how much the pretrained model added over training from scratch.
- **A mini "boundary statement"** (6 lines): training data (species, assays, conditions) · context length and tokenization · training goal · benchmarks and baselines used · how results were obtained (zero-shot / probing / fine-tuning) · known failure modes.

### Part G: Offer next steps
Offer: (a) a deeper dive into one design element, (b) a side-by-side with a specific other model, (c) a checklist for the user's own dataset.

---

## 4. If the paper is an agent, or an LLM that uses a biological model

An **agent** is an LLM that plans a multistep analysis, writes and runs code, calls tools, and returns to the user when a decision is needed. It is a coordinator, not a model of biology. Its parts: the LLM (reasoning), document retrieval (RAG), skill files (written procedures), tool connections (e.g., MCP), a sandbox for code, and human oversight. Reasoning tricks make multistep answers more reliable but **add no information that was absent from training**; only external components (documents, tools, a connected foundation model) extend what the system draws on.

Ask which of four ways a biological model is combined with the LLM, and what the LLM therefore receives:

1. **As a tool:** the agent calls it like any software and reads the output (a structure, a score). The agent inherits the tool's boundary; *how the model is packaged as a tool matters*.
2. **As text training data:** measurements are written as text (e.g., a cell as a list of top genes) to fine-tune the LLM.
3. **As an encoder:** the model's embeddings are fed to the LLM every time it answers. Only this route gives the LLM the model's own view of the sequence each time. It helps when the answer lies *beyond* the LLM's textual knowledge (e.g., variant pathogenicity from raw DNA), and adds little when the LLM already knows the answer from text.
4. **As a verifier:** the model scores the LLM's answers during fine-tuning, so the model's errors can be learned by the LLM.

Warnings to include: (i) access to a tool does not mean the agent relied on it: in one example an agent named the right causal gene while its tool's own scores ranked other genes higher; (ii) written reasoning steps are not guaranteed to be faithful; (iii) check whether the paper has **controls that separate the biological model's contribution from the LLM's** (in one study, some systems were as accurate with shuffled biological inputs as with real ones); (iv) most agent benchmarks test general bioinformatics, not whether the agent picks the *right* model or reads its output correctly.

---

## 5. Peer sheet: fast comparison anchors from the review

**Protein**
- *ESM2 / ProtTrans:* alphabet of 20 amino acids; sequence only; fill-in-the-blank; showed how much can be learned from sequence alone.
- *SaProt, ESM3:* add structure (and function) tokens; ESM3 can be prompted with partial structure/function to generate.
- *ProGen2:* next-token prediction → generator of protein sequences. *Ankh:* matches larger models at a fraction of the training cost.
- *EVE, AlphaMissense, popEVE:* variant-effect predictors; EVE uses evolutionary conservation; AlphaMissense adapts AlphaFold with human population frequencies; popEVE combines both to make scores comparable across proteins.
- *AlphaFold:* sequence → 3D structure, trained on the PDB, relies heavily on related sequences.

**DNA / RNA**
- *Nucleotide Transformer:* fixed 6-letter chunks. *DNABERT-2, GROVER:* learned variable-length chunks. (Multi-letter chunks can blur single-letter variants.)
- *HyenaDNA, Caduceus, Evo / Evo 2:* one letter per token; efficient over long inputs; Evo is autoregressive, so can generate.
- *Enformer, Borzoi, AlphaGenome:* sequence → many regulatory tracks; AlphaGenome reads up to 1 megabase at single-base resolution. *ChromBPNet:* one assay (chromatin accessibility) at base resolution, ~2 kb window. *scooby:* adapts Borzoi to single cells.
- *GPN-MSA:* adds multispecies alignments. *regLM, CodonTransformer, gRNAde:* generation of regulatory DNA, codons, RNA structures.
- *RNA-FM, RiNALMo:* noncoding RNA structure; *Orthrus:* mRNA, contrastive across isoforms/orthologs.

**Single-cell, bulk, spatial, multi-omics**
- *Geneformer:* each cell = list of genes ordered by expression rank (magnitude discarded, nonbiological platform effects dampened); in-silico gene deletion.
- *scGPT:* each gene paired with a binned expression value (magnitude kept).
- *UCE:* represents each gene by its protein's ESM2 embedding, so it can place cells from unseen species in a shared space.
- *SCimilarity:* contrastive, built to search an atlas for similar cells. *Nicheformer:* dissociated + spatial data; embedding reflects the cell's neighborhood. *VirTues:* spatial protein markers. *BulkFormer:* tissue-level bulk RNA.
- *GeneCompass:* gene tokens enriched with prior knowledge. *PINNACLE:* a graph of protein interactions per cell type (same protein gets a different embedding per cell type). *AIDO:* separate DNA/RNA/protein/cell models combined.
- *Perturbation:* *CellOT* (pairs control cells with perturbed ones), *GEARS* (gene-relationship graph for unseen combinations), *State* (whole cells as tokens).

**LLM + biology:** *ChatNT, CellWhisperer, BioReason* (embeddings fed to an LLM); *Biomni, Virtual Lab, Paper2Agent* (agents calling tools); *GeneAgent* (checks its claims against curated databases).

---

## 6. Analogy bank and plain-language glossary

Prefer these. They are the review's own analogies, plus a few helpers.

| Term | Plain version |
|---|---|
| Foundation model | A model trained once on a huge unlabeled library, then reused for many jobs (like a refinery producing one intermediate used for many products). |
| Self-supervised learning | Hide part of the data and ask the model to guess it: a fill-in-the-blank exercise whose answers come from the data itself, so no human labeling is needed. |
| Embedding | A model's numeric "fingerprint" for an input; similar things sit close together on the map. |
| Token / vocabulary | The "words" a model can read, and the list of all of them. |
| Tokenization | The rule for chopping raw data into words. For DNA there are no spaces, so the rule is a scientific choice. |
| Corpus | The library the model studied. |
| Transformer / attention | A reader that lets every word look at every other word in the passage (cost grows fast as the passage gets longer). |
| Context length | How much text fits in the reader's window at once. |
| Zero-shot | Use the model as-is, no new labels (like asking a trained reader a question cold). |
| Probing | Put a very simple model on top of the fingerprints, trained on a small labeled set. |
| Fine-tuning | Keep training the model itself on a small labeled set. |
| Transfer learning | Carry knowledge learned in pretraining to a new task, so a small labeled set is enough. |
| Autoregressive / masked | "Predict the next word" vs. "fill in the blank." |
| Contrastive learning | Teach the model which examples belong together by pulling them close and pushing others apart. |
| Baseline | A deliberately simple method (e.g., linear regression, the average of the training data) that a fancy model must beat to be worth using. |
| Sparse autoencoder | A tool that re-expresses a model's fingerprint as many simple "feature switches," each ideally matching one human-readable property (the "Jennifer Aniston neuron" idea). |
| Agent | An LLM that plans a multistep job and uses tools to do it. |
| RAG | The LLM looks things up in documents before answering, so answers are current and traceable. |
| MCP | A standard plug, like USB: wrap a tool once and any compatible agent can use it. |
| Skill file | A written recipe an agent loads when needed (steps of an analysis, or when not to trust a tool). |
| Model card / boundary statement | A "nutrition label" for a model, listing training data, limits, and tests. |
| Extinct-language decipherment | The review's master analogy: infer the vocabulary, with no native speaker to confirm the grammar. |
| Niche colonization vs. specialization | Early in a field, big generalist models spread widely (like early finches colonizing new habitats); later, specialists fill the gaps where generalists perform poorly. |

---

## 7. Worked example (style calibration only)

*User gives the scGPT paper. The following illustrates the **tone, structure, and level of detail**; always check specifics (training corpus size, objective details, reported benchmarks) against the actual paper before writing.*

**A. In one breath.** scGPT is a "reader of cells". It studied the gene-activity profiles of tens of millions of cells so that it can turn any new cell into a compact numeric fingerprint, and can then be adapted to jobs such as labeling cell types, integrating datasets, or guessing the effect of a gene perturbation.

**B. Where it sits.** *Single-cell RNA in → representation out* (with prediction tasks, such as perturbation, added by fine-tuning). It does not read DNA letters, protein sequences, or tissue position, so it cannot tell isoforms apart or use a cell's neighbors. Its closest neighbors are Geneformer (same address), UCE (adds cross-species), and Nicheformer (adds spatial context).

**C. How it reads and knows.**
- *Vocabulary:* a fixed list of gene names; each gene is a "word" and comes with a number saying how active it is. → *So it can only read the genes (and species) on its list.*
- *Grammar:* which genes rise and fall together because they work in the same pathway. A cell has no natural word order, unlike a sentence, which is why how to write a cell as "text" is a central design problem. → *So what it learns is co-activity patterns, not wiring diagrams.*
- *Corpus:* a large collection of cells assembled from public atlases. → *It likely inherits whatever was easy to sample: well-studied tissues, popular technologies.*
- *Embedding:* a fingerprint per gene and per cell, in a shared map. → *Useful for similarity and labeling; the individual numbers are not directly readable.*

**D. Versus Geneformer and UCE.**

| Element | scGPT | Geneformer / UCE | What it buys / costs |
|---|---|---|---|
| ① Data | Gene + binned activity level (magnitude kept) | Geneformer: genes ranked by activity (magnitude discarded); UCE: genes represented by their protein's ESM2 embedding | Keeping magnitude retains information but also lets platform-specific, non-biological differences leak in; UCE's choice is what lets it cross species, which scGPT's fixed gene list cannot |
| ② Architecture | Transformer | Transformer (both) | Few built-in biology assumptions, so it needs lots of data; fixed gene list limits it to species/annotations seen in training |
| ③ Training | Self-supervised: hide some values, predict them | Similar fill-in-the-blank family | Rewards predicting what co-occurs, not what *causes* what |
| ④ Evaluation | Developer-chosen tasks | Independent tests exist for both | In independent zero-shot tests, scGPT and Geneformer embeddings did not beat simple baselines; for perturbation, simple linear models and the training average matched or beat foundation models |
| ⑤ Post-analysis | Mostly fine-tuned for each task | Geneformer also uses in-silico gene deletion | A strong fine-tuned score does not show what pretraining taught it; interpretation tools cover few single-cell models |

**Biggest innovation:** representing *how much* each gene is active, not only its rank. **Biggest limit:** it was rewarded for pattern-matching, not for cause and effect, so predicting the outcome of an intervention is the place to be most careful.

**E. Evidence.** *Authors report* gains on their chosen tasks. *Independent evaluations found* that zero-shot embeddings often did not beat simple baselines and that perturbation predictions did not reliably beat linear or mean baselines (with some exceptions under calibrated metrics).

**F. Verdict.** *Reasonable:* exploring and labeling cells in human-like data when you can fine-tune on your own labeled set. *Caution:* in-silico perturbation as evidence of causality; new species; rare states. *Sanity checks:* always run logistic regression or PCA alongside, and report how much the pretrained model adds over training from scratch.

---

## 8. Limits of this guide

- It encodes the review's framework and its literature snapshot (through 2026). New models and independent evaluations appear quickly; search for them when you can.
- The framework is a way to ask better questions, not a scoring system. A model can be excellent inside its boundary; the point is to know where that boundary is.
- If a model does not fit any category cleanly, say so, place it as best you can, and explain what does not fit.
