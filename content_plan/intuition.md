# Intuitive Explanations Bank: organized by claims_beats, each beat paired with "reader confusion → our own words"

**Source**: `Cai_ARBDS_Draft_v11_clean`. Every `>` block is v11 text, **verbatim, not reworded**.
**Organization**: matches `ARBDS_claims_beats_v2_EN.md` beat by beat, so it can be merged into the same beats data.

**Conventions**
- `> …` = verbatim v11 text. `[…]` = middle part omitted (used only when skipping sentences within one passage). Citation numbers such as `(25)` and `(9)` are kept as in the draft; they can be stripped in bulk before publishing.
- The line under each quote, `— §x.x · [type]`, gives the source and the device: **[analogy]** compares to something familiar, **[worked example]** a concrete model or experiment, **[numbers]** a numeric contrast, **[counterintuitive]** a result that runs against intuition, **[definition]**, **[contrast]**, **[one-liner]**.
- The **Reader may be stuck on** lines are mine (written from the reader's point of view), not from the draft.

**One thing to know before using this**: the design principle in `00_overview.md` is "Landing = spine only, no examples." Almost everything below is an example or analogy, so it belongs in the folded examples on the Concepts page, or in a new content type (see "What to tell the engineer" at the end).

---

## Start here: the 10 strongest lines (my judgment)

| # | The confusion it answers | Where the passage is |
|---|---|---|
| 1 | Why do we still need foundation models if we have agents? | `1-04`, `3-05` (AlphaFold + BioReason 90% / 49% / 80%) |
| 2 | Why use language as the analogy, and where does it break? | `2.1.1-01` ("the points at which the analogy breaks down foreshadow the knowledge boundaries") |
| 3 | If a model generalizes, why is there still a boundary? | `2.1.2-01` (ESM2 can score a mutation it never saw, but cannot score nucleotide substitutions) |
| 4 | How can a model learn without labels? | `2.1-01` (mask a few amino acids and guess them) |
| 5 | How is learning biology different from learning language? | `4-01` (deciphering an extinct language) |
| 6 | If reasoning gets better, don't agents just understand biology better? | `3-01` (reasoning adds no information) |
| 7 | What are MCP and skill files? | `3-01` (USB; "access to a tool does not teach an agent to use it well") |
| 8 | If a prediction is accurate, does the model understand the mechanism? | `4.2-01`, `1-01` (Fig. 1B caption) |
| 9 | Why can simple baselines match big models? | `4.3-08` ("a model can score well simply by predicting an average response") |
| 10 | Are these limitations permanent? | `5.3-01` (Darwin's cataloguing → mechanism → engineering) |

---

## Two analogies side by side

The two big analogies in v11 answer two different questions, so they should not be merged or used interchangeably.

| | Extinct-language decipherment | Crude oil processing |
|---|---|---|
| **Question it answers** | Why is learning biology from data harder than learning language? | What role does a foundation model play in the whole pipeline? |
| **Where it lives** | `4-01` (§4 opening) | `A-01`, `1-04` (Fig. 1C caption) |
| **How developed in v11** | Developed: a full sentence of mapping, plus it organizes all of §4 | Thin: one caption sentence; the mapping is carried by the figure |

**Extinct-language decipherment** (`4-01`)

> Learning biology from data is closer to deciphering an extinct language: the vocabulary must be inferred, no living speaker can confirm the grammar, and the only surviving texts are the measurements our assays happened to record.

— §4 · [analogy]

> Decipherment asks whether any structure can be recovered, whether it carries meaning, whether it can be used to write, and which parts remain unreadable, and we use the same questions to organize the evidence below.

— §4 · [analogy → organizing principle]

**Crude oil processing** (`A-01`, `1-04`)

> Extraction, processing, and distribution of raw data in the form of a reusable intermediate by analogy to crude oil processing.

— Fig. 1C caption · [analogy]

> Together, the two turn raw biological data (e.g., a protein sequence) into a reusable intermediate form (e.g., a sequence *embedding*) and deliver it to diverse downstream applications and users (Figure 1C).

— §1 · [the sentence the oil analogy illustrates]

---

## Abstract

### A-01 · AI is reshaping biological research, but it is unclear when to trust it

**Reader may be stuck on:** "Foundation models and agents both sound like AI. What does each one do? And what is a 'knowledge boundary'?"

> We frame this as a model’s knowledge boundary: the range of inputs, tasks, and conditions over which its outputs are reliable.

— Abstract · [definition]

> Extraction, processing, and distribution of raw data in the form of a reusable intermediate by analogy to crude oil processing.

— Fig. 1C caption · [analogy]

---

## 1. Introduction

### 1-01 · Computation has moved from processing data to contributing to discovery

**Reader may be stuck on:** "Biology has used computation for decades. What is actually new with AI?"

> Computation initially served to process raw measurements, for example by performing the Fourier calculations that turned X-ray diffraction data into the first protein structure, myoglobin (1). As data grew in volume and variety, computation increasingly helped to interpret that signal: the Protein Data Bank, for example, grew from 7 structures at its founding in 1971 to more than 250,000 today (2, 3), and that growth drove new methods for comparing and classifying structures.

— §1 · [worked example] [numbers]

> AI is now contributing to discovery itself: models that learn from data can propose results not yet tested experimentally, as AlphaFold does when it predicts protein structure from amino acid sequence (4, 5).

— §1 · [worked example]

**Reader may be stuck on:** "One is called 'versatile' and the other 'accessible.' What do those two words mean here?"

> Biological foundation models, trained on millions of sequences, protein structures, or cellular measurements, offer versatility: general patterns are extracted from data once, when a model is developed, and can then be applied to many additional biological problems. Agentic systems, which run analyses from plain-language instructions, offer accessibility: biologists with limited programming experience can now apply advanced computational tools to their own datasets.

— §1 · [contrast]

**Reader may be stuck on:** "If a model predicts very accurately, does that mean it understands the mechanism behind it?"

> Their knowledge develops as a consequence of sophisticated computational approaches for pattern recognition. As such, foundation models can make accurate predictions (e.g., predictions of protein structure from amino acid sequence), without having ‘learned’ the mechanisms driving the phenomenon they predict (e.g., physical and chemical basis of protein folding).

— Fig. 1B caption · [counterintuitive]

---

### 1-04 · Foundation models compress data, agents compose tools, and the two are beginning to meet

**Reader may be stuck on:** "An agent can call all kinds of tools, read the literature, and write code. Why do we still need foundation models?"

First, how each one gets its knowledge:

> Foundation models compress large bodies of raw data into richly organized numeric representations.

— §1 · [one-liner]

> Agentic systems compose tools into workflows: an agent uses a large language model (LLM) as its source of reasoning to plan tasks and carries them out by assembling literature, databases, and software. Agents run tools on raw data, but their choices of which tools to run and how to interpret the results draw on the LLM's knowledge, which is restricted to what has previously been documented.

— §1 · [contrast]

Then the AlphaFold answer (the most direct passage in the whole review for this confusion):

> AlphaFold can accurately predict the structure of an uncharacterized protein from its sequence, which an agent composing existing software cannot do without AlphaFold or a related model. Once a structure is predicted, however, many further analyses, such as comparing it with known structures, relating it to variants or expression data, and planning follow-up experiments, are the kind of multistep work an agent can assemble.

— §1 · [worked example]

> Together, the two turn raw biological data (e.g., a protein sequence) into a reusable intermediate form (e.g., a sequence *embedding*) and deliver it to diverse downstream applications and users (Figure 1C). They are complementary.

— §1 · [analogy: crude oil processing, see Fig. 1C]

A deeper layer of evidence is in `3-05` (the BioReason numbers).

**Reader may be stuck on:** "So just connect them. What is the remaining problem?"

> Yet it remains unclear how an agent, or a researcher, should choose the right foundation model for a task and how to interpret its output.

— §1 · [problem statement]

> Because they function primarily as integrators of existing tools, they take on the properties of the tools they utilize in any specific instance.

— Fig. 1B caption · [one-liner: the agent inherits the tool's properties]

---

### 1-08 · What limits broader use is the lack of an explicit account of each model's knowledge boundary

**Reader may be stuck on:** "Isn't a 'knowledge boundary' just 'models have limitations'? Why give it a name?"

> Such an account would (i) help researchers decide when a model can be trusted and how to evaluate its output and (ii) give agentic systems the information they need to use foundation models as reliable components of larger workflows.

— §1 · [purpose]

(v11 has no ready-made intuitive wording for this one; see "Gaps" at the end.)

---

## 2. Landscape of Biological Foundation Models

### 2.1-01 · A foundation model is trained once on large unlabeled data, then reused for many tasks

**Reader may be stuck on:** "With no labels, how does the model learn?"

> During training, part of each training example is hidden (“masked”), and the model is asked to predict the hidden part from the parts that remain visible. For example, a few amino acids in a protein sequence might be masked; the model predicts which amino acids belong at those positions, its predictions are compared with the true amino acids, and the model is adjusted to reduce its errors. This process is repeated across millions of sequences.

— §2.1 · [worked example]

> Unlike supervised learning, in which humans must annotate (“supervise”) the data, self-supervised learning creates its training targets from the raw data itself. This suits biology, where unlabeled DNA sequences, protein sequences, and single-cell transcriptomes number in the hundreds of millions, whereas validated labels, such as a variant classified as pathogenic or benign, are scarce, labor intensive, and unevenly distributed.

— §2.1 · [contrast]

**Reader may be stuck on:** "Mask-and-guess: what biologically meaningful thing does that actually teach?"

> Training is designed to make the model extract recurring patterns in its data type: for proteins, pairs of amino acids that tend to mutate together because they contact each other in the folded structure; for DNA, short sequence motifs bound by transcription factors, such as the TATA box found in many promoters; for single-cell transcriptomes, groups of genes whose expression rises and falls together because they act in the same pathway.

— §2.1 · [worked example: what is learned in each of three data types]

**Reader may be stuck on:** "With no labels at all, how can zero-shot prediction estimate a mutation's effect?"

> For example, a protein language model can score how plausible a sequence is, given the sequences it was trained on; a mutation that makes a sequence much less plausible is more likely to disrupt protein function, so this score can serve as an estimate of variant effect (25).

— §2.1 · [worked example]

**Reader may be stuck on:** "Why is AlphaFold, which does one thing, discussed alongside foundation models?"

> We also discuss models trained for a specific task that are not typically called foundation models, including AlphaFold for protein structure prediction (4, 5), AlphaGenome for sequence-to-function prediction (23), and perturbation models termed virtual cells (24), because they rest on the same premise and are frequently used as foundation models.

— §2.1 · [scope]

---

### 2.1.1-01 · Biological models borrow the language of LLMs, but the analogy breaks at every step

**Reader may be stuck on:** "Why keep using language as the analogy? Is the analogy reliable?"

> We introduce each concept through the analogy to human language, because the points at which the analogy breaks down foreshadow the knowledge boundaries discussed below.

— §2.1.1 · [meta-analogy: where the analogy breaks is where the boundary is]

**Vocabulary / token. Reader may be stuck on:** "What is a 'word' in a biological sequence?"

> A token is one such unit as it occurs in a particular input, so that an input is read as a sequence of tokens, much as a sentence is read as a sequence of words.

— §2.1.1 · [analogy]

> In ESM2, for example, the 20 standard amino acids comprise the model’s vocabulary, so a protein of 300 amino acids is read as 300 tokens (6).

— §2.1.1 · [worked example]

> In biological foundation models, the equivalent tokens are amino acids, nucleotides, or short sequence motifs; in single-cell models, they are genes, with each cell read as a list of the genes it expresses.

— §2.1.1 · [worked example]

> Unlike human language, in which spaces and punctuation demarcate words, biological sequences such as DNA lack analogous boundaries, so model builders must choose among single nucleotides, fixed-length *k*-mers, or learned multi-nucleotide tokens (26, 27), and the tokenization rule becomes part of the scientific problem itself.

— §2.1.1 · [where the analogy breaks]

**Grammar. Reader may be stuck on:** "DNA and proteins have a 'grammar'? Who set it?"

> For proteins, these rules are dictated by evolution: the gene encoding an amino acid sequence persists only if the translated protein folds into the required structure and adopts the right dynamics to perform its function.

— §2.1.1 · [analogy]

> The grammar lies in how motifs are arranged: the number, spacing, orientation, and order of motifs within a regulatory region determine which TFs bind together and, in turn, how strongly the target gene is expressed and in which cell types.

— §2.1.1 · [worked example]

> Whereas an LLM implements grammar that humans devised and that any fluent reader can check, biological foundation models implement a grammar whose rules are largely unknown. When such a model performs well on a test, it can therefore be difficult to assess whether it has internalized general principles or simply found a shortcut that happens to work on that test.

— §2.1.1 · [where the analogy breaks]

**Corpus. Reader may be stuck on:** "Hundreds of millions of sequences sounds like a lot. Why say the corpus is limited?"

> ESM3, among the largest protein models, was trained on about 771 billion tokens (30), roughly 20-fold fewer than the 15 trillion tokens used to pretrain the LLM Llama 3 (31), although tokens from the two domains are not directly equivalent in information content.

— §2.1.1 · [numbers]

> Many sequences are near-duplicates of close evolutionary relatives, which is why protein databases are clustered by sequence similarity before training (28), and sequences are concentrated in a few well-studied lineages, which biases model likelihoods toward those lineages (32).

— §2.1.1 · [worked example]

> Text corpora are also incomplete, but the incompleteness of the biological corpus differs in kind: whereas text records language directly, biological data are indirect measurements of an underlying system, shaped by assay technology and experimental design. Biological corpora therefore contain only what current methods can measure and what researchers have chosen to study, and consequently they inherit biases in species coverage, cell or tissue sampling, and assay type.

— §2.1.1 · [where the analogy breaks]

**Embedding. Reader may be stuck on:** "What exactly is an embedding? Why can't it be read?"

> An embedding is a long list of numbers, typically in the hundreds to thousands, that a model assigns to each token of a given query. It represents intrinsic properties of that token (e.g., amino acid size and charge) as well as contextual features arising from its relation to the other tokens in the input.

— §2.1.1 · [plain definition]

> Because embeddings are derived from training without human-interpretable labels, they cannot be read directly: a human could not identify which number reflects, say, amino acid polarity, and individual numbers may represent a combination of properties.

— §2.1.1 · [worked example]

> The aim recalls the “Jennifer Aniston neuron” of neuroscience, a single neuron in the human brain that fires selectively to images of one person (33)

— §2.1.1 · [analogy: what sparse autoencoders aim for]

> Because all embeddings from a given model share the same numeric space, inputs with similar properties lie close together. For example, in ESM2, proteins with similar structure or function lie near one another even when their sequences differ (6).

— §2.1.1 · [worked example]

---

### 2.1.2-01 · Five design elements describe nearly every biological foundation model, and each sets part of its knowledge boundary

**Reader may be stuck on:** "If a model generalizes, why is there still a 'boundary'? Where does it come from?" (the single most important example in the review)

> Much of the value of a foundation model lies in its ability to generalize, that is, to make useful predictions for inputs it did not encounter during training. ESM2, for example, can score a mutation in a protein that was absent from its training data. This ability has limits, however, and they are set by how the model was built: ESM2 cannot score nucleotide substitutions, because its vocabulary contains only amino acids.

— §2.1.2 · [worked example, counterintuitive]

**Reader may be stuck on:** "What does each of the five elements concretely mean?"

> **Data** determines what information goes into the model and in which form, including the training corpus and tokenization strategy. ESM2 is trained on UniRef protein sequences tokenized as individual amino acids. Geneformer, by contrast, encodes each cell as a list of genes ranked by expression (9).

— §2.1.2 · Data · [contrast]

> Transformers carry few modality-specific assumptions (inductive biases), which enables them to adapt to very different corpora but means they generally require larger training sets to learn modality-specific patterns. Alternative architectures instead build on features of the data, such as long genomic context (HyenaDNA; 35), the equivalence of the two DNA strands (Caduceus; 36), or protein interaction networks (PINNACLE; 37).

— §2.1.2 · Architecture · [contrast]

> In masked language modeling, used by ESM2, randomly hidden amino acids are predicted from the surrounding sequence (38). In autoregressive modeling, used by ProGen2 and Evo, each token is predicted from those before it (39–41), which makes these models natural generators of new sequences.

— §2.1.2 · Training scheme · [contrast]

> Contrastive and metric learning pull related examples close together in embedding space and push unrelated ones apart. Orthrus, for example, treats splice isoforms and orthologs of the same gene as related RNAs (42), and SCimilarity places cells of the same type near one another (43).

— §2.1.2 · Training scheme · [worked example]

> Intrinsic evaluation asks whether the model has learned the structure of its data, for example whether ESM2 recovers residue contacts (6). Downstream evaluation asks whether the model helps with a practical task, such as predicting the effects of mutations, and is increasingly done on shared benchmarks such as ProteinGym (44). The two do not always agree.

— §2.1.2 · Evaluation · [contrast]

> Its central idea is transfer learning: knowledge captured in the embedding during pretraining is carried over to a new task by probing or fine-tuning (Section 2.1), so that a small labeled dataset suffices where training from scratch would require a large one.

— §2.1.2 · Post-analysis · [one-liner]

> A model can also be used as it is, with no further training, for example to score mutations by likelihood or, as Geneformer does, to simulate deleting a gene and see how a cell's embedding shifts (*in silico* perturbation; 9).

— §2.1.2 · Post-analysis · [worked example]

> Finally, interpretability analysis asks how the model arrives at its outputs, for example which input positions drive a prediction (45) or which internal features match known biology, and can reveal whether a model relies on genuine biology or on shortcuts in the data.

— §2.1.2 · Post-analysis · [one-liner]

---

### 2.2-01 · Models differ by what goes in and what comes out, and are foundational mainly within that range

**Reader may be stuck on:** "Aren't foundation models supposed to be 'general'? Why are they foundational only within a range?"

> Whereas a general-purpose LLM serves many kinds of text and tasks, each biological foundation model is shaped by design choices specific to its data and task and is therefore foundational mainly within that range. This dependence is the basis of the knowledge boundary developed below.

— §2.2 · [contrast]

**Reader may be stuck on:** "RNA models and single-cell models both deal with RNA. What is the difference?"

> RNA language models read the nucleotide sequences of RNA molecules, unlike the single-cell models described below, which read how much of each RNA a cell contains.

— §2.2.1 · [one-line distinction]

> Bulk RNA sequencing measures the average expression of all cells in a tissue sample.

— §2.2.1 · [one-liner]

**Reader may be stuck on:** "How does changing the input actually change the model?"

> Moving from DNA and protein to cells and tissues, the unit of vocabulary grows from a single residue to a gene, a whole cell, and a cell within its neighborhood (Figure 2B), and the learnable grammar changes accordingly.

— §2.2.1 · [stepwise]

> Such multinucleotide tokens can split regulatory motifs across tokens and hide the effect of a single-nucleotide variant.

— §2.2.1 · DNA · [worked example]

> A model built for non-coding RNA structures therefore need not capture what governs mRNA function.

— §2.2.1 · RNA · [one-liner]

> Spatial transcriptomics instead records where each cell sits in a tissue section, so the grammar extends beyond which genes are co-expressed within a cell to which cells sit next to one another.

— §2.2.1 · Spatial · [one-liner]

**Reader may be stuck on:** "What is the limit of each of the three output types: representation, prediction, generation?"

> What a model embeds, whether a residue or protein (ESM2), a DNA segment (Nucleotide Transformer, Evo), a gene in its cellular context (Geneformer, scGPT), or a whole cell (UCE), determines which questions the embedding can serve

— §2.2.2 · Representation · [one-liner]

> A predictive model is trained on paired measurements (supervised training) to answer one fixed question, so it can predict only what has been measured. AlphaFold takes an amino acid sequence and returns three-dimensional coordinates for every atom, based on structures in the Protein Data Bank (4).

— §2.2.2 · Prediction · [worked example]

> A generative model writes new sequences or states rather than scoring existing ones, and its vocabulary determines what it can write.

— §2.2.2 · Generation · [one-liner]

> Perturbation models lie between prediction and generation: given a cell and an intervention, such as a gene knockout, they produce the expected expression profile, a state that was never measured.

— §2.2.2 · Perturbation · [worked example]

---

## 3. Where a Foundation Model Enters Agentic Systems

### 3-01 · An agent is not a model: it coordinates an LLM, the user, and tools, and only external components add knowledge

**Reader may be stuck on:** "Isn't an agent just a ChatGPT that is better at using tools?"

> An agent uses a general-purpose LLM, such as those behind ChatGPT or Claude, to carry out a multistep task: asked which genes respond to a drug in a single-cell dataset, it can plan the analysis, write and run code, call a foundation model, check the results, and return to the user when a decision is needed (Figure 3A). Agentic systems are therefore not models themselves; they coordinate an LLM, the user, and many tools.

— §3 · [worked example]

**Reader may be stuck on:** "Why isn't an ordinary chat LLM enough?"

> a chat model draws only on text fixed at a training cutoff, cannot say where an answer came from, sometimes produces fluent but false statements (hallucinations), and cannot act on data or run software.

— §3 · [one-line list]

> Retrieval-augmented generation (RAG) has the model base its answer on retrieved documents, such as papers or database entries, so that answers are current and traceable to a source (69). Function calling lets the model write a request to an external program, such as a database query or an analysis script, and read back the result (70, 71).

— §3 · [one-liner]

**Reader may be stuck on:** "Reasoning models keep getting stronger. Won't an agent just be able to work out the biology itself?"

> Reasoning models are LLMs trained to write out intermediate steps and rewarded when the final answer to a checkable problem is correct (72); this makes multistep answers more reliable but adds no information absent from training (73). Only external components, such as documents, tools, or a connected foundation model, can extend what the system draws on.

— §3 · [counterintuitive: more reliable ≠ more information]

**Reader may be stuck on:** "What are MCP, skill files, and harnesses?"

> the Model Context Protocol (MCP), released in late 2024, standardized how they connect to models, much as USB did for computer devices: a database, program, or foundation model wrapped once as an MCP tool can be used by any compatible agent (74).

— §3 · [analogy: USB]

> Because access to a tool does not teach an agent to use it well, skill files followed in 2025: written instructions an agent loads when needed, such as the steps of a standard analysis or when a tool’s output should not be trusted (75).

— §3 · [one-liner]

> Agent harnesses manage long-running tasks by repeating the plan–act–revise cycle, providing a workspace for code and files, and asking a human for approval at key decisions (76).

— §3 · [one-liner]

**Reader may be stuck on:** "What does a multi-agent system look like?"

> Multi-agent systems assign roles to separate LLM agents: in the Virtual Lab, agents acting as a principal investigator and specialist scientists designed nanobodies

— §3 · [worked example]

---

### 3-05 · A foundation model can enter an agent in four ways, and each way decides whose knowledge boundary the agent inherits

**Reader may be stuck on:** "How does a foundation model plug into an agent? Can an LLM read an embedding?"

> A foundation model can enter an agent in four ways, which differ in what the LLM receives and thus in whose knowledge boundary the agent inherits. The first acts while the agent works; the others shape the LLM during training.

— §3 · [overview]

> Tool. The agent reads the foundation model's output as text. The Virtual Lab agents called ESM, AlphaFold-Multimer, and Rosetta to refine nanobodies (80), and Paper2Agent's AlphaGenome tools outperformed general agents, showing that packaging matters (77, 83).

— §3 · Tool

> Text. Data are rewritten as language, for example each cell as a list of its top genes (84).

— §3 · Text

> Encoder. Embeddings are converted into the LLM's input, so it reads biological data alongside text (19–21).

— §3 · Encoder

> Verifier. A foundation model scores a reasoning model's answers during training, so its errors become part of the reward (85).

— §3 · Verifier

**Reader may be stuck on:** "The agent's LLM has already read so much of the literature. Does adding a foundation model really help?" (the same confusion as `1-04`; this is the numeric answer)

> Only the encoder route lets the LLM work with raw data, and BioReason shows when this matters. On pathway questions the LLM alone reached 90%, and the encoder made little difference. On variant classification it reached 49%, and adding Evo 2 raised this to 80%, compared with 61% for Nucleotide Transformer (21). When the answer lies within the LLM's textual knowledge, the encoder adds little; when it lies beyond, the encoder sets the ceiling.

— §3 · [numbers] [worked example]

---

### 3-07 · Better agents do not move a foundation model's boundary

**Reader may be stuck on:** "Agents will keep getting stronger (reinforcement learning, more reasoning). Won't the boundary just disappear?"

> Reinforcement learning improves how a system uses the knowledge it can reach but does not move the foundation model's boundary, and more reasoning cannot supply missing premises: a reasoning model's written steps are not guaranteed valid or faithful (86, 87), and biological inference, unlike mathematical proof (88), starts from incomplete premises that only experiments can test.

— §3 · [contrast: mathematical proof vs. biological inference]

**Reader may be stuck on:** "If the model is packaged well, won't the agent know when to trust it?"

> Nor does packaging tell an agent when a model should be trusted; unlike conventional bioinformatics tools, foundation models have little community guidance on this. At an LDL cholesterol locus, the AlphaGenome agent prioritized SORT1 whereas the original paper emphasized CELSR2 and PSRC1 (77). Current agents therefore keep humans in the loop, and an agent is only as useful as our understanding of each model's knowledge boundary.

— §3 · [worked example]

---

## 4. Knowledge Boundaries Revealed by Existing Studies

### 4-01 · Every model has a knowledge boundary, and for foundation models it is the least characterized

**Reader may be stuck on:** "LLMs have boundaries too. Why stress the boundary of foundation models in particular?"

> LLMs trained on human language have knowledge boundaries, but these are rarely visible because modern language is densely represented in their training data. Learning biology from data is closer to deciphering an extinct language: the vocabulary must be inferred, no living speaker can confirm the grammar, and the only surviving texts are the measurements our assays happened to record.

— §4 · [analogy: deciphering an extinct language]

> Decipherment asks whether any structure can be recovered, whether it carries meaning, whether it can be used to write, and which parts remain unreadable, and we use the same questions to organize the evidence below.

— §4 · [analogy → organizing principle]

**Reader may be stuck on:** "If an agent calls a foundation model, whose limits apply?"

> an agent that calls a foundation model inherits that model’s boundary.

— §4 · [one-liner]

---

### 4.1-01 · Each design element sets a different limit, and the limits travel with the model

**Reader may be stuck on:** "Aren't these just the old problems of traditional machine learning?"

> This holds for any model, including conventional machine-learning models; what is new is that foundation models are reused far beyond their original purpose, so these limits travel with them.

— §4.1 · [one-liner]

**Data. Reader may be stuck on:** "Isn't more data enough?"

> Human proteins and model organisms are represented by many related sequences and measured cell states, whereas poorly studied lineages and rarely profiled cell states appear seldom or not at all. Tokenization fixes the smallest unit the model can distinguish: a six-nucleotide token blurs a single-nucleotide variant, and a rank-based input discards how strongly each gene is expressed (Section 2.2.1).

— §4.1 · Data sets what can be known · [worked example]

**Architecture. Reader may be stuck on:** "Give a model enough data and it can learn anything, right?"

> A convolutional neural network detects short local patterns such as a transcription factor binding motif, whereas attention, the core of the Transformer, lets distant positions interact at a cost that grows roughly quadratically with input length (34).

— §4.1 · [contrast]

> An interaction longer than the input window cannot be learned, however much data is available.

— §4.1 · Architecture sets which relationships can be captured · [counterintuitive]

**Training scheme. Reader may be stuck on:** "If a model can score, can it also generate? If it can search for similar cells, can it also predict perturbation?"

> ESM2's likelihoods score how well a mutation is tolerated (25), but it is not built to write new sequences, whereas ProGen2 and Evo are natural generators of new proteins and genomes (40, 41). SCimilarity's embeddings suit searching an atlas for similar cells but not predicting the response to a perturbation (43). None of these objectives directly rewards learning cause and effect.

— §4.1 · The training scheme sets what is rewarded · [contrast]

**Evaluation. Reader may be stuck on:** "A high test score means the model is good, doesn't it?"

> A model tested only on data resembling its training set can appear strong while failing on new proteins, species, or conditions; if test proteins have close relatives among the training proteins, a high score may reflect recall rather than learned rules.

— §4.1 · Evaluation sets what becomes visible · [counterintuitive: recall vs. rules]

**Post-analysis. Reader may be stuck on:** "If the prediction is right, the model understands the mechanism, right?"

> Knowledge may be present yet hard to extract, and a correct prediction does not show that the model learned the relevant mechanism.

— §4.1 · Post-analysis sets what becomes accessible · [counterintuitive]

> a protein language model that predicts residue contacts has no representation of the forces that drive folding.

— §4.2 · [worked example]

---

### 4.2-01 · Without labels, foundation models capture real biological patterns, most clearly in proteins

**Reader may be stuck on:** "With no labels at all, can a model really learn biology? Or is it coincidence?"

> Protein language models are never told the properties of amino acids, yet their embeddings group residues by hydrophobicity and charge (89). They also recover which residues make physical interactions in the folded protein structure, because such residues tend to mutate together over evolution (89, 90).

— §4.2 · Data · [worked example]

**Reader may be stuck on:** "It can predict structure. Can it predict function?"

> Protein language model likelihoods predict mutational effects without training on mutational data and correlate with deep mutational scanning measurements (25).

— §4.2 · Training scheme · [worked example]

**Reader may be stuck on:** "Is scoring the same thing as designing?"

> Design is a stricter test than scoring, and autoregressive training made it possible. ProGen produced artificial lysozymes with measurable catalytic activity (62), and ESM3, which can be prompted with structure and function tokens, generated a fluorescent protein distant from known natural sequences (30).

— §4.2 · Training scheme · [worked example]

**Reader may be stuck on:** "What about species it has never seen?"

> UCE represents each gene by the ESM2 embedding of its protein rather than by a fixed gene list, so it can place cells from species absent from training in a shared space (11).

— §4.2 · Data · [worked example]

**Reader may be stuck on:** "Can we read out what the model has learned?"

> Sparse autoencoders (Section 2.1.1) have recovered features for active sites, zinc-finger domains, and disulfide bonds in protein language models (93–95).

— §4.2 · Post-analysis · [worked example]

> simulated gene deletion with Geneformer nominated therapeutic targets for cardiomyopathy that were then supported experimentally (9)

— §4.2 · Post-analysis · [worked example]

**Reader may be stuck on:** "Why are the examples all proteins?"

> The clearest successes are in proteins, where the corpus is largest and the rules are written most directly into sequence.

— §4.2 · [one-liner]

---

### 4.3-01 / 4.3-08 · When do predictions stay reliable? Where does model knowledge stop?

**Reader may be stuck on:** "Why compare against baselines as simple as linear regression or 'the training-set average'?"

> Studies addressing it, many conducted by researchers other than the models’ developers, have compared protein, DNA, and single-cell foundation models with simpler alternatives, such as linear or logistic regression, one-hot encodings of sequence, or simply the average of the training data.

— §4.3 · [method]

**Data. Reader may be stuck on:** "Is the model learning biology, or just what people like to study?"

> Protein language model likelihoods partly reflect how often related sequences were sampled across the tree of life rather than fitness alone (32).

— §4.3 · [worked example]

> LLM-based annotators may score well on benchmarks partly because curated databases shaped both their training and the benchmark labels, and they perform worse on orphan genes and non-model organisms (12, 97).

— §4.3 · [worked example: circularity]

> more parameters cannot recover patterns the data never contain.

— §4.3 · [one-liner]

**Architecture & scale. Reader may be stuck on:** "A model trained on whole protein families: can it see the effect of a single mutation?"

> AlphaFold2 relies heavily on related sequences and largely fails to predict the structural disruption caused by destabilizing point mutations (98).

— §4.3 · [worked example]

> larger protein language models do not consistently improve zero-shot fitness prediction (44)

— §4.3 · [counterintuitive]

> AlphaGenome reads one megabase of DNA at a time, an advance that underlies its state-of-the-art performance (23), yet regulation acting over longer distances or between chromosomes lies outside a single input.

— §4.3 · [worked example]

**Training scheme. Reader may be stuck on:** "A model trained on observational data: can it predict the result of an intervention?"

> Masked and autoregressive objectives reward predicting what occurs together, not what causes what. Enformer predicts regulatory signals across the genome well, yet it poorly explains differences in gene expression between individuals and often predicts even the wrong direction of effect (100, 101).

— §4.3 · [counterintuitive]

> In predicting responses to genetic perturbations, simple linear models and even the average of the training data match or outperform foundation models (103–105).

— §4.3 · [counterintuitive]

> GenePT suggests that part of what these models learn is already recorded in text (109).

— §4.3 · [one-liner]

**Evaluation. Reader may be stuck on:** "When a baseline ties a big model, is the model weak, or is the test flawed?"

> Common perturbation metrics are dominated by systematic expression differences unrelated to the specific perturbation, so a model can score well simply by predicting an average response (114). Conversely, when metrics are calibrated against both an uninformative mean baseline and a positive control, several deep-learning perturbation models do outperform simple baselines (115), so part of the reported parity reflects the metric rather than the model.

— §4.3 · [counterintuitive + reversal]

**Reader may be stuck on:** "Beyond benchmark evaluation, what about real applications?"

> AlphaMissense showed meaningful discordance with curated clinical evidence across 5,845 missense variants in 59 disease genes (116). Structure-confidence scores poorly separated successes from failures among 614 experimentally characterized de novo protein designs (117). Most of 21 pretrained RNA language models did not outperform a one-hot encoding for secondary-structure prediction once closely related sequences were removed from the test set (118).

— §4.3 · [numbers]

**Post-analysis. Reader may be stuck on:** "A high score after fine-tuning: does it mean pretraining learned something?"

> Fine-tuning can add knowledge from the new labels, so a strong fine-tuned score does not show how much was learned during pretraining. Attention weights should not be read as biological mechanisms

— §4.3 · [one-liner]

> For most models, it remains unknown whether a correct prediction reflects real biology or a shortcut that happens to work on the test.

— §4.3 · [one-liner]

**Four-layer summary. Reader may be stuck on:** "So did the models learn biology or not?"

> These studies shift the question from whether foundation models learn biology to what they have learned and where that knowledge stops holding. The boundary has several layers: knowledge missing because observations were never or rarely collected; knowledge hard to learn because the architecture cannot span it or the objective does not reward it, as with cause and effect; capability hidden or exaggerated by evaluation; and knowledge present in the model but inaccessible to current analysis.

— §4.3 · [framing sentence]

---

## 5. Open Challenges

### 5-01 / 5.1-03 · Evaluation is uneven, and agents using foundation models are barely evaluated

**Reader may be stuck on:** "Has anyone tested agents that use foundation models? What did they find?"

> Agent benchmarks test general bioinformatics analysis (15, 16), not whether an agent chooses the right foundation model or interprets its output correctly.

— §5.1 · [one-liner]

> when such controls were applied to six systems, BioReason and BioReason-Pro were as accurate with shuffled biological inputs as with intact ones (121).

— §5.1 · [counterintuitive: just as accurate with scrambled inputs]

**Reader may be stuck on:** "Does a model know when it is out of its depth?"

> Few models report whether they can signal that a query lies outside their boundary.

— §5.1 · [one-liner]

---

### 5.2-01 · The bet on one general-purpose model comes from the LLM analogy

**Reader may be stuck on:** "For LLMs, bigger is better. Why not for biological models?"

> Much of the field's momentum comes from an analogy with LLMs, whose performance improves predictably as parameters, training data, and computing budget grow, a relationship known as scaling laws (124). Biological foundation models have followed a similar trajectory, yet larger protein language models do not consistently predict mutational effects better than their predecessors (44, 99).

— §5.2 · [contrast]

> Language has a comparatively unified structure, with a shared grammar and stable vocabulary, and this supports a single general-purpose model. Biology is heterogeneous across scale, from molecule to cell to tissue to organism, and across data type, species, and experimental condition. The language analogy therefore only partially holds: biology's vocabulary is not fixed, its grammar is largely unknown, and its corpus is incomplete.

— §5.2 · [where the analogy breaks]

> Unlike text, biology's corpus is still being defined as new measurement technologies emerge, so the LLM trajectory is instructive but only one reference point among several.

— §5.2 · [one-liner]

---

### 5.3-01 · AI for biology is in its infancy

**Reader may be stuck on:** "Are these limitations permanent, or just a feature of the current stage?"

> Positioning the field on a developmental trajectory lets us read its present strengths and limitations as features of a transient stage rather than as a fixed outcome.

— §5.3 · [one-liner]

**Lens 1. Reader may be stuck on:** "If simple baselines match big models, why doesn't that mean big models are useless?"

> Biology has historically progressed from observation and classification, as in Darwin's cataloguing of species, to mechanistic understanding of structure, function, and causality, and ultimately to engineering: the design of biological systems from first principles. Much of the foundation-model work surveyed here sits at the first stage, offering pattern-level prediction from observational data, and the repeated finding that simple baselines match foundation models is consistent with this reading.

— §5.3 · [analogy: scientific maturity]

> claims framed in engineering-stage language, such as "de novo design," should be read with this stage in mind.

— §5.3 · [one-liner]

**Lens 2. Reader may be stuck on:** "Why is everyone building big, do-everything models right now?"

> Periods of open ecological opportunity have historically favored large, generalist strategies, whereas the adaptive radiation that follows favors smaller organisms fitted to specific niches (Figure 3B). The current expansion of biological foundation models resembles the first, open-niche phase.

— §5.3 · [analogy: ecological niches]

> Early evolutionary specialization favors large-scale differences (niche colonization, analogous to current foundation models), whereas later adaptation produces small-scale differences optimized for specific niches (analogous to task-specific models).

— Fig. 3B caption · [analogy]

---

## 6. Future Directions and Recommendations

### 6.1-01 · Use a portfolio of broad and specialized models, coordinated by agents

**Reader may be stuck on:** "So what do we do now? Wait for a stronger general model?"

> Because biological data are so heterogeneous, the field need not wait for a single general-purpose model.

— §6.1 · [one-liner]

> Agents are well placed to manage such a portfolio. They can route each question to the model whose boundary covers it, combine outputs from complementary models, and fall back to a simple baseline when no model applies.

— §6.1 · [worked example: the agent's new role]

> GPN-MSA, which draws on evolutionary alignments (92), and ChromBPNet, which targets a single assay at base resolution (45), already follow this pattern.

— §6.1 · [worked example]

---

### 6.2-01 / 6.2-03 · A structured boundary statement for every model

**Reader may be stuck on:** "Agent tools already come with descriptions. What is missing?"

> Current tool descriptions state what a tool does but seldom where it fails, so errors from outside a model's boundary can propagate silently: a variant score from a model trained without population data looks as authoritative as a well-supported result

— §6.2 · [worked example]

**Reader may be stuck on:** "What would a boundary statement actually look like?"

> We propose that each foundation model be released with a structured boundary statement, in the spirit of model cards and datasheets (126, 127). Organized by the five design elements, it would record the species, assays, and conditions in the training data; the context length and tokenization of the architecture; the training objective; the benchmarks used, including comparisons with simple baselines; and the post-analysis methods under which the reported results hold.

— §6.2 · [checklist]

**Reader may be stuck on:** "How would an agent use it?"

> Just as GeneAgent checks its claims against curated databases (12), an agent could confirm that a query lies within a model's training and evaluation domain before relying on its output.

— §6.2 · [analogy]

**Reader may be stuck on:** "Can a boundary be extended?"

> Self-driving laboratories, in which robotic platforms run experiments chosen by a model and return the results for the next round, can target these regions directly (128, 129); combined with agents that plan experiments and foundation models that propose candidates, such closed loops could extend a model’s knowledge boundary with new measurements rather than more of the same data. The knowledge boundary would then become the interface between foundation models and agentic systems.

— §6.2 · [worked example]

---

### 6.3-01 · Making boundaries explicit is a community task

**Reader may be stuck on:** "Does every biologist have to learn to build models?"

> The aim is shared literacy, not making every biologist a model builder.

— §6.3 · [one-liner]

**Reader may be stuck on:** "Has this kind of community infrastructure worked before?"

> UniProt and the Protein Data Bank became trusted infrastructure (2, 28), open-source ecosystems made models widely reusable (130), and blind assessments such as CASP and CAGI established credible measures of progress (91, 131).

— §6.3 · [worked example]

---

## 7. Conclusion (7-01, 7-03)

The conclusion is summary, and v11 has no new intuitive explanation here. The closest thing to a one-sentence version is:

> Making these boundaries explicit gives biologists a principled basis for deciding when to trust a model, gives model builders a concrete target for improvement, and gives agents the information they need to select and interpret models appropriately.

— §7 · [summary]

---

## Gaps: places where v11 has no ready-made intuitive wording

These are places where readers are likely to get stuck, but the draft has only a definition or a framing sentence, nothing that makes people say "oh, I get it." Filling them means writing something new rather than mining v11:

1. **"Knowledge boundary" itself** (`A-01`, `1-08`). There is a one-sentence definition and the "extinct language" analogy (which explains why the problem is hard, not what a boundary is). This is the first term the reader must understand, and it has no small example. The closest is "ESM2 cannot score nucleotide substitutions" in `2.1.2-01`; consider moving it to the very front as the opening example.
2. **Why "simple baselines match big models" is a signal** (`4.3-01`). The draft lists many results but has no sentence on why using the training-set average as the opponent is itself persuasive.
3. **The difference between foundation models and agents in "efficiency and depth of knowledge extraction"** (your example). In v11 this idea is spread over three places: the AlphaFold passage in `1-04`, "adds no information" in `3-01`, and the BioReason numbers in `3-05`. There is no single summarizing sentence. For a Q&A card on the site, these three would need to be strung together; I cross-referenced `1-04` and `3-05` for this reason.
4. **The crude oil analogy** (`A-01`, `1-04`). In v11 it is a single caption sentence (Fig. 1C); the body text never spells out the mapping (raw data ↔ crude oil, embedding ↔ the intermediate product, downstream applications ↔ finished products). It is likely to work well when told aloud with the figure, but on the website it needs a few written sentences to stand alone as a card.
5. **Embedding** (`2.1.1-01`). It has "a long list of numbers" and "similar things lie close together," but no picture such as coordinates on a map.
6. **Probing vs. fine-tuning vs. zero-shot** (`2.1-01`). Only zero-shot has a concrete example; probing and fine-tuning are defined abstractly.
7. **Why the way a benchmark is split matters** (`4.1-01` Evaluation). The draft's "recall rather than learned rules" is good, but it has no concrete example (such as an exam repeating the textbook's worked problems).
8. **Conclusion** (`7-01`, `7-03`): no new material, since it is a summary.

---

## What to tell the engineer (the part relevant to this file)

- This file is **a new content type**: each beat carries 1 to N entries of "reader confusion + our own words." The current data model (`05_data_and_linking.md`) has beat, term, example, and model, but nothing like this. Ask the engineer whether to put these in the folded examples on the Concepts page (least work) or to add a new entry point, something like "Common questions."
- **There is a conflict with the existing design principles**: `00_overview.md` says Landing carries no examples and "nothing expands in place." These explanations are essentially examples, so either they live on the page a beat's link opens, or the principle changes (for example, each beat gets a "Common confusions here →" link that jumps to the matching card). This is a product decision for you and your co-authors to make first, and then tell the engineer.
- Every quote carries its source (§x.x) and beat ID, so it fits the existing rule "IDs follow the review's numbering" and needs no new numbering scheme.