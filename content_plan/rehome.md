# Content File: claims, concepts, and examples (re-homed to the compressed structure)

**Paper**: AI for Biologists: The Knowledge Boundaries of Foundation Models in the Age of Agentic Systems

**Contents**: 72 landing-page claims · 67 concept records (29 of them also techniques; 3 are evidence-only concepts) · 149 examples (every one under exactly one concept) · 17 technique-only entries.

## How to read this file

- Headings follow the review's numbering. Under each **claim** (landing page), the concepts whose **home claim** it is are listed. Each concept has a short definition and its **folded examples**. This is the order of the Concepts page.
- Examples carry: a **direction** (`success`, `limitation`, `illustration`), a **design element** where relevant, the **models** they mention (auto-tagged; authors please check), and, for examples that came from a demoted claim, `from {original claim} → shown with {landing claim}`.
- `▸ Finding:` lines group examples that came from one demoted claim of the review.
- `both` = the concept is also a technique (see `engineer_brief/04`); the technique block (how it works, variants, pitfalls) is **not yet written** beyond the shared definition and is for authors/curators to extend from the references.
- Concepts marked `example_only` have no home claim and no landing-page link.
- Technique-only entries (terms the argument does not need but staff do) are at the end.
- Demoted claims (20) are not repeated here; their headlines appear as `Finding:` lines. The full list is at the end of `ARBDS_claims_compressed_EN.md`.

---


## Abstract

**A-01** AI is changing how biological research is done, through two kinds of tools: foundation models and agentic systems.

- **Biological foundation model (FM)** `biological-foundation-model`  ·  concept
  - *Definition:* A model trained on millions of DNA, protein, or single-cell measurements, whose general patterns are extracted once and then reused for many downstream problems. The term "foundation model" (2021) describes models trained on broad data and adaptable to a wide range of tasks.
  - *Examples (4, folded):*
    - `A-01e1` [illustration] FMs predict protein structures, mutation effects, and cellular responses to genetic perturbations.
    - `1-02e1` [illustration] FMs: general patterns extracted once at development, then applied to many problems (ESM2, Geneformer, Evo 2...). · models: evo-2, geneformer, esm2
    - `1-10e2` [illustration] Scope of the review: molecular sequences, macromolecular structures, single-cell data, and other omics; the concepts likely apply more broadly in biology and medicine.
    - `2.1-01e3` [illustration] Task-specific models also covered because they rest on the same premise and are frequently used as FMs: AlphaFold (structure), AlphaGenome (sequence-to-function), virtual cells (perturbation). · models: alphagenome, alphafold
- **Agentic system** `agentic-system`  ·  concept
  - *Definition:* An AI assistant built on a large language model that runs multistep analyses from plain-language requests and increasingly calls FMs as tools. It is not a model itself: it coordinates an LLM, the user, and many tools.
  - *Examples (10, folded):*
    - `1-02e2` [illustration] Agents: biologists with limited programming experience can apply advanced computational tools to their own datasets.
    - `1-05e1` [illustration] Recognized successes are in conventional bioinformatics and biostatistics (GeneAgent, CellVoyager, TxAgent). · models: geneagent
    - `1-05e2` [illustration] Independent benchmarks (BixBench, HeurekaBench) show agents remain brittle on realistic analysis tasks. · models: bixbench
    - `1-06e1` [illustration] AlphaFold + Biomni: both draw on public resources (UniProt, PDB). AlphaFold can predict an uncharacterized protein's structure, which an agent composing existing software cannot do; the multistep work after that (compare with known structures, link to variants/expression data, plan follow-up experiments) is what an agent can assemble. · models: biomni, uniprot, pdb, alphafold
    - `3-01e1` [illustration] Typical task: "which genes respond to a drug in this single-cell dataset?" → plan the analysis, write and run code, call an FM, check results, return to the user when a decision is needed.
    - `3-04e1` [illustration] Biomni: composes workflows from tools and protocols mined from thousands of publications. Paper2Agent: turns a paper's codebase into MCP tools. · models: biomni, paper2agent
    - `3-04e2` [illustration] Other agents target chemistry, gene-set annotation, gene editing, single-cell reanalysis, therapeutics.
    - `5.1-03e2` [limitation] Evidence on adoption by biologists remains limited to surveys.
    - `6.1-02e1` [illustration] Route each question to the model whose boundary covers it; combine outputs from complementary models; fall back to a simple baseline when no model applies.
    - `6.2-01e2` [illustration] Recent high-profile agent studies still rely on human scientists to run experiments and interpret results.

**A-02** It is often unclear when these models' outputs can be trusted; we frame this as the model's knowledge boundary.

- **Knowledge boundary** `knowledge-boundary`  ·  concept
  - *Definition:* The range of inputs, tasks, and conditions over which a model's outputs can be relied upon.
  - *Examples (3, folded):*
    - `3-07e2` [limitation] Unlike conventional bioinformatics tools, FMs have little community guidance on when to trust them.
    - `3-07e3` [limitation] At an LDL cholesterol locus, the AlphaGenome agent prioritized SORT1, whereas the original paper emphasized CELSR2 and PSRC1. · models: alphagenome
    - `6.1-01e1` [illustration] GPN-MSA (evolutionary alignments) and ChromBPNet (single assay at base resolution) already follow this pattern. · models: gpn-msa, chrombpnet

**A-03** Five design elements (data, architecture, training scheme, evaluation scheme, post-analysis) set the boundary.


**A-04** The review examines evidence of where models succeed or fail, and proposes standardized descriptions of model limits so researchers, and the agents acting for them, can use these tools reliably.



## 1. Introduction


### Paragraph 1: the shift in computation's role; two complementary tools

**1-01** Computation's role in biology has deepened in three stages: processing raw data → interpreting signal → contributing to discovery itself.

- **Knowledge extraction from data** `knowledge-extraction`  ·  concept
  - *Definition:* The goal that has driven each stage of computation in biology: getting from raw data to signal, to interpretation, and now to discovery.
  - *Examples (3, folded):*
    - `1-01e1` [illustration] Processing: Fourier calculations turned X-ray diffraction data into the first protein structure (myoglobin).
    - `1-01e2` [illustration] Interpreting: the Protein Data Bank grew from 7 structures (1971) to 250,000+, driving new methods for comparing and classifying structures; new disciplines formed (biostatistics, bioinformatics, computational biology). · models: pdb
    - `1-01e3` [illustration] Discovering: AlphaFold predicts protein structure from sequence, producing results not yet tested experimentally. · models: alphafold

**1-02** Two complementary AI tools extend this shift: FMs offer *versatility*, agentic systems offer *accessibility*.


**1-03** AI for biology is an emerging interdisciplinary field, and even experts on each side lack a clear picture of what these models have learned and where they fail.



### Paragraph 2: two ways of extracting knowledge; complementary and merging

**1-04** FMs *compress* raw data into richly organized numeric representations; what they "know" is bounded by training data, architecture, and training objective.

- **Embedding** `embedding`  ·  concept
  - *Definition:* A long list of numbers (hundreds to thousands) that a model assigns to each token of an input, capturing the token's intrinsic properties and its context. Embeddings cannot be read directly, but because all embeddings from one model share a numeric space, inputs with similar properties lie close together. They serve as the reusable intermediate form of raw data (a protein sequence becomes a sequence embedding).
  - *Examples (3, folded):*
    - `1-04e3` [illustration] Crude-oil analogy (Fig 1C): raw data are refined into a reusable intermediate and distributed to diverse downstream users.
    - `2.1.1-05e1` [illustration] Individual numbers may combine properties; a human could not identify which number reflects, say, polarity.
    - `2.1.1-05e3` [illustration] In ESM2, proteins with similar structure or function lie near one another in embedding space even when their sequences differ. · models: esm2
- **Compression vs. composability** `compression-vs-composability`  ·  concept
  - *Definition:* Two ways of building a tool that extracts knowledge: FMs compress data into one learned representation, whereas agents compose separate existing tools into a workflow.
  - *Examples (1, folded):*
    - `1-04e1` [illustration] ESM2 is trained on UniRef sequences; Nucleotide Transformer and Evo 2 learn from genomes across species; Geneformer, scGPT, UCE learn from tens of millions of cells. · models: nucleotide-transformer, evo-2, geneformer, scgpt, uce, esm2, uniref
- **Correlation vs. causation** `correlation-vs-causation`  ·  concept
  - *Definition:* Two ways of extracting knowledge from data: FMs learn patterns of what occurs together (correlation), and can predict accurately without having learned the mechanism that drives the phenomenon (causation).
  - *Examples (4, folded):*
    - `1-04e2` [illustration] AlphaFold predicts structure accurately without "learning" the physical and chemical basis of folding (Fig 1B). · models: alphafold
    - `4.2-01e2` [illustration] Not captured: a protein language model predicting residue contacts has no representation of the forces driving folding.
    - ▸ *Finding: Observed states rarely predict the effect of an intervention beyond simple baselines*
      - `4.3-04e1` [limitation · training scheme · from 4.3-04 → shown with 4.3-08] Enformer predicts regulatory signals across the genome well but poorly explains differences in expression between individuals and often predicts the wrong direction of effect; a 2026 preprint reports the same for AlphaGenome and Borzoi. · models: enformer, borzoi, alphagenome
      - `4.3-04e5` [illustration · training scheme · from 4.3-04 → shown with 4.3-08] Masked and autoregressive objectives reward predicting what occurs together, not what causes what.

**1-05** Agents *compose* tools into workflows, so they inherit the properties of the tools and the limits of the LLM's documented knowledge.

- **Large language model (LLM)** `llm`  ·  concept
  - *Definition:* The language model an agent uses as its source of reasoning to plan tasks. Its knowledge is restricted to what has previously been documented.
  - *Examples (1, folded):*
    - `3-01e2` [illustration] Starting point, the limits of chat LLMs (widely available from late 2022): knowledge fixed at a training cutoff, no source for answers, hallucinations, cannot act on data or run software.

**1-06** The two are complementary, and beginning to meet.


**1-07** Unresolved: how should an agent, or a researcher, choose the right FM for a task and interpret its output?



### Paragraph 3: problem statement and roadmap

**1-08** What limits broader use of FMs and agents is the lack of an explicit account of each model's knowledge boundary.


**1-09** Making the boundary explicit would (i) help researchers decide when to trust a model and how to evaluate its output, and (ii) give agents the information to use FMs as reliable components.


**1-10** The review: design-element framework → how agents are assembled and interface with FMs → evidence (including independent reassessments against simple baselines) → practical ways to make boundaries explicit.



## 2. Landscape of Biological Foundation Models


### 2.1. What Is a Foundation Model and What Is Its Premise?

**2.1-01** An FM is trained on broad data, commonly through self-supervised learning, which suits biology because unlabeled data are abundant and labels are scarce.

- **Self-supervised learning** `self-supervised-learning`  ·  both · technique group: Training scheme
  - *Definition:* A way of training in which part of each training example is hidden ("masked") and the model predicts it from the parts that remain visible, so the training targets come from the raw data itself and no human labels are needed.
  - *Examples (7, folded):*
    - `2.1-01e1` [illustration] Masking example: hide a few amino acids → model predicts them → compare with the truth → adjust → repeat across millions of sequences.
    - `2.1-01e2` [illustration] Why it suits biology: hundreds of millions of unlabeled DNA/protein sequences and single-cell transcriptomes vs. scarce, labor-intensive, unevenly distributed validated labels (e.g., a variant classified pathogenic or benign).
    - `2.1-02e1` [illustration] Patterns the training is designed to extract: pairs of amino acids that mutate together because they contact each other in the fold; TF-bound short motifs in DNA (e.g., the TATA box in many promoters); groups of genes whose expression rises and falls together in a pathway.
    - `4.2-01e1` [success] Captured: amino acid chemistry, which residues contact each other in a fold, which mutations a protein tolerates.
    - ▸ *Finding: Known patterns can be recovered from unlabeled sequence*
      - `4.2-02e1` [success · data · from 4.2-02 → shown with 4.2-07] Protein language models are never told amino acid properties, yet embeddings group residues by hydrophobicity and charge.
      - `4.2-02e2` [success · data · from 4.2-02 → shown with 4.2-07] They recover which residues physically interact in the fold, because such residues tend to mutate together over evolution.
      - `4.2-02e3` [success · data · from 4.2-02 → shown with 4.2-07] ESMFold predicts atomic-level structure from a single sequence; AlphaFold, which also uses alignments of related sequences, reached near-experimental accuracy in blind CASP14. · models: esm2, alphafold
- **Supervised learning** `supervised-learning`  ·  concept
  - *Definition:* Training in which humans annotate ("supervise") the data.
  - *Examples: none (definition only)*

**2.1-02** The premise: train once on large unlabeled data, reuse for many tasks, in three ways (probing, fine-tuning, zero-shot).

- **Probing** `probing`  ·  both · technique group: Post-analysis
  - *Definition:* Passing a model's embedding of each input to a separate, much simpler model (e.g., a linear regression) that is trained on a small labeled dataset to predict a property of interest.
  - *Examples: none (definition only)*
- **Fine-tuning** `fine-tuning`  ·  both · technique group: Post-analysis
  - *Definition:* Training the FM itself further on a small labeled dataset.
  - *Examples (1, folded):*
    - ▸ *Finding: A correct answer does not show the model knows why*
      - `4.3-07e1` [limitation · post-analysis · from 4.3-07 → shown with 4.3-08] Fine-tuning can add knowledge from the new labels, so a strong fine-tuned score does not show how much was learned in pretraining.
- **Zero-shot prediction** `zero-shot-prediction`  ·  both · technique group: Post-analysis
  - *Definition:* Using a model with no labeled data at all, for example scoring how plausible a sequence is and using that score as an estimate of variant effect.
  - *Examples (5, folded):*
    - `2.1-02e2` [illustration] Zero-shot example: a protein language model scores how plausible a sequence is; a mutation that makes it much less plausible is more likely to disrupt function, so the score estimates variant effect.
    - ▸ *Finding: Models largely capture what is functional*
      - `4.2-03e1` [success · training scheme · from 4.2-03 → shown with 4.2-07] Protein language model likelihoods predict mutational effects without mutational training data and correlate with deep mutational scanning measurements.
      - `4.2-03e2` [success · training scheme · from 4.2-03 → shown with 4.2-07] EVE (unsupervised model of evolutionary variation) matched or exceeded supervised methods at classifying human variants as pathogenic or benign. · models: eve
      - `4.2-03e3` [success · training scheme · from 4.2-03 → shown with 4.2-07] ProteinGym turned this into a shared test of more than 200 deep mutational scanning assays. · models: proteingym
    - ▸ *Finding: Early studies suggest learned knowledge can be read out*
      - `4.2-06e3` [success · post-analysis · from 4.2-06 → shown with 4.2-07] General protein language models guided antibody evolution toward improved binding without task-specific training.


#### 2.1.1. Key concepts to understand biological foundation models

**2.1.1-01** Biological FMs borrow LLM architecture and terminology; four concepts (vocabulary/token, grammar, corpus, embedding) describe the process, and the points where the language analogy breaks foreshadow the knowledge boundaries.


**2.1.1-02** Vocabulary and token: DNA has no word boundaries, so the tokenization rule becomes part of the scientific problem itself.

- **Vocabulary** `vocabulary`  ·  concept
  - *Definition:* The set of basic units a model can recognize, analogous to the words of a language.
  - *Examples (2, folded):*
    - `2.1.1-02e2` [illustration] ESM2: the 20 standard amino acids are the vocabulary, so a 300-aa protein is 300 tokens. · models: esm2
    - ▸ *Finding: Single-cell: representing expression levels; fixed gene vocabulary*
      - `2.2.1-04e3` [illustration · data · from 2.2.1-04 → shown with 2.2.1-01] Fixed gene identities from specific genome annotations restrict models to species seen in training; UCE addresses this. · models: uce
- **Token** `token`  ·  concept
  - *Definition:* One vocabulary unit as it occurs in a particular input, so that an input is read as a sequence of tokens, much as a sentence is read as a sequence of words.
  - *Examples (8, folded):*
    - `2.1.1-02e1` [illustration] LLMs: tokens = words or word fragments. Biological FMs: tokens = amino acids, nucleotides, or short motifs; in single-cell models, genes (each cell read as a list of the genes it expresses).
    - `2.1.1-02e3` [illustration] DNA: model builders must choose among single nucleotides, fixed-length *k*-mers, or learned multi-nucleotide tokens.
    - ▸ *Finding: DNA: how to define a token*
      - `2.2.1-02e1` [illustration · data · from 2.2.1-02 → shown with 2.2.1-01] Nucleotide Transformer: fixed six-nucleotide *k*-mers. DNABERT-2 and GROVER: learned variable-length tokens. · models: nucleotide-transformer, dnabert-2, grover
      - `2.2.1-02e2` [illustration · data · from 2.2.1-02 → shown with 2.2.1-01] Multinucleotide tokens can split regulatory motifs and hide the effect of a single-nucleotide variant.
      - `2.2.1-02e3` [illustration · data · from 2.2.1-02 → shown with 2.2.1-01] HyenaDNA, Caduceus, Evo: one nucleotide per token, with architectures efficient over long inputs. · models: hyenadna, caduceus, evo
    - ▸ *Finding: Single-cell: representing expression levels; fixed gene vocabulary*
      - `2.2.1-04e1` [illustration · data · from 2.2.1-04 → shown with 2.2.1-01] Why hard: a cell has no inherent order, each gene carries a continuous value, and platform/processing details create strong non-biological confounders.
      - `2.2.1-04e2` [illustration · data · from 2.2.1-04 → shown with 2.2.1-01] Geneformer: genes ordered by expression rank. scGPT: each gene paired with a binned expression value. · models: geneformer, scgpt
    - `4.1-02e2` [illustration · data] Tokenization fixes the smallest unit: a six-nucleotide token blurs a single-nucleotide variant; a rank-based input discards how strongly each gene is expressed.

**2.1.1-03** Grammar: unlike an LLM's human-devised grammar, a biological FM implements a grammar whose rules are largely unknown, so good performance may reflect a shortcut rather than a general principle.

- **Grammar** `grammar`  ·  concept
  - *Definition:* The set of rules by which a model's units are combined. In biology these rules are largely unknown, unlike human language.
  - *Examples (3, folded):*
    - `2.1.1-03e1` [illustration] Proteins: rules dictated by evolution; a gene persists only if the protein folds into the required structure and adopts the right dynamics.
    - `2.1.1-03e2` [illustration] Regulatory DNA: the grammar lies in the number, spacing, orientation, and order of motifs, determining which TFs bind together, how strongly the gene is expressed, and in which cell types.
    - ▸ *Finding: Single-cell: representing expression levels; fixed gene vocabulary*
      - `2.2.1-04e4` [illustration · data · from 2.2.1-04 → shown with 2.2.1-01] Single-cell models: the grammar is co-expression patterns, the token is a gene, and the corpus is a matrix of expression counts across cells.
- **Regulatory DNA** `regulatory-dna`  ·  concept
  - *Definition:* Noncoding sequences, such as promoters and enhancers, that control when, where, and how strongly a gene is transcribed.
  - *Examples: none (definition only)*
- **Transcription factor (TF) binding motif** `tf-binding-motif`  ·  concept
  - *Definition:* A short sequence, typically 6 to 12 base pairs long, that is preferentially bound by a particular TF.
  - *Examples: none (definition only)*

**2.1.1-04** Corpus: biological corpora are smaller, less diverse than they look, and indirect measurements of the system, so they inherit biases in species, tissue, and assay.

- **Corpus** `corpus`  ·  concept
  - *Definition:* The large repository of data on which a model is trained (plural: corpora).
  - *Examples (7, folded):*
    - `2.1.1-04e1` [illustration] Examples: UniRef (hundreds of millions of protein sequences; trained ESM2); CZ CELLxGENE Discover (150M+ single cells; supplied scGPT's training data). · models: scgpt, esm2, uniref, cz-cellxgene-discover
    - `2.1.1-04e2` [illustration] Size: ESM3 (~771B tokens) vs. Llama 3 (~15T tokens), roughly 20-fold fewer, though tokens from the two domains are not directly equivalent. · models: esm3
    - `2.1.1-04e3` [illustration] Diversity: many sequences are near-duplicates of close relatives (hence clustering before training); sequences concentrate in a few well-studied lineages, biasing model likelihoods toward them.
    - `2.1.1-04e4` [illustration] Nature of the data: text records language directly; biological data are indirect measurements shaped by assay technology and experimental design, containing only what current methods can measure and what researchers chose to study.
    - `4.1-02e1` [illustration · data] Human proteins and model organisms are represented by many related sequences and measured cell states; poorly studied lineages and rarely profiled cell states appear seldom or not at all.
    - ▸ *Finding: Models capture both biology and the history of sampling*
      - `4.3-02e3` [limitation · data · from 4.3-02 → shown with 4.3-08] Spatial, perturbation, and bulk corpora are small compared with sequence databases and single-cell atlases; more parameters cannot recover patterns the data never contain.
    - `5.2-03e2` [illustration] Unlike text, biology's corpus is still being defined as new measurement technologies emerge.

**2.1.1-05** Embedding: a list of numbers that cannot be read directly, but places similar inputs close together.

- **Sparse autoencoder** `sparse-autoencoder`  ·  both · technique group: Post-analysis
  - *Definition:* An auxiliary model that re-expresses each embedding as a combination of a much larger set of features, each of which tends to correspond to a single property.
  - *Examples (2, folded):*
    - `2.1.1-05e2` [illustration] The "Jennifer Aniston neuron" in neuroscience (a single neuron firing selectively to one person) motivates the sparse-autoencoder aim.
    - ▸ *Finding: Early studies suggest learned knowledge can be read out*
      - `4.2-06e1` [success · post-analysis · from 4.2-06 → shown with 4.2-07] Sparse autoencoders have recovered features for active sites, zinc-finger domains, and disulfide bonds in protein language models.


#### 2.1.2. Five Design Elements of Typical Foundation Models

**2.1.2-01** Nearly all biological FMs can be described by five design elements; innovations change one or more of them; and each element sets part of the model's knowledge boundary.

- **The five design elements** `five-design-elements`  ·  concept
  - *Definition:* The five parts that together describe nearly any biological FM, and each of which sets part of its knowledge boundary: data (training corpus and tokenization), model architecture (how information is processed and stored), training scheme (what the model is rewarded to learn), evaluation scheme (how the model is judged), and post-analysis (how a trained model is used).
  - *Examples (1, folded):*
    - `2.1.2-02e1` [illustration · data] ESM2: UniRef sequences, tokenized as individual amino acids. Geneformer: each cell as a list of genes ranked by expression. · models: geneformer, esm2, uniref
- **Generalization** `generalization`  ·  concept
  - *Definition:* Making useful predictions for inputs the model did not encounter during training.
  - *Examples (7, folded):*
    - `2.1.2-01e1` [illustration] ESM2 can score a mutation absent from its training data, but cannot score nucleotide substitutions because its vocabulary contains only amino acids. · models: esm2
    - `4.1-05e1` [illustration · evaluation] A model tested only on data resembling its training set can look strong while failing on new proteins, species, or conditions.
    - `4.1-05e2` [illustration · evaluation] If test proteins have close relatives in the training set, a high score may reflect recall rather than learned rules.
    - ▸ *Finding: Generalization has improved mainly by enriching what each token encodes, rather than by adding parameters*
      - `4.2-05e1` [success · data · from 4.2-05 → shown with 4.2-07] SaProt pairs each amino acid with a token for its local structure. · models: saprot
      - `4.2-05e2` [success · data · from 4.2-05 → shown with 4.2-07] GPN-MSA adds aligned sequences from 100 vertebrate genomes, making conservation visible, and outperforms sequence-only models at predicting deleterious variants. · models: gpn-msa
      - `4.2-05e3` [success · data · from 4.2-05 → shown with 4.2-07] UCE represents each gene by the ESM2 embedding of its protein, so it can place cells from species absent from training in a shared space. · models: uce, esm2
    - ▸ *Finding: One-mutation effects are often missed, and scale has not closed the gap*
      - `4.3-03e1` [limitation · architecture · from 4.3-03 → shown with 4.3-08] AlphaFold2 relies heavily on related sequences and largely fails to predict the structural disruption of destabilizing point mutations. · models: alphafold

**2.1.2-02** Data determines what information goes into the model and in which form.


**2.1.2-03** Model architecture determines how information is processed and stored; the leading architecture adapts widely but generally needs more data.

- **Transformer and self-attention** `transformer`  ·  both · technique group: Architecture
  - *Definition:* The leading architecture, whose self-attention relates every token to every other token in the input. It lets distant positions interact, at a cost that grows roughly quadratically with input length.
  - *Examples (1, folded):*
    - ▸ *Finding: One-mutation effects are often missed, and scale has not closed the gap*
      - `4.3-03e3` [limitation · architecture · from 4.3-03 → shown with 4.3-08] AlphaGenome reads one megabase at a time (underlying its state-of-the-art performance), yet longer-range or inter-chromosomal regulation lies outside a single input. · models: alphagenome
- **Inductive bias** `inductive-bias`  ·  concept
  - *Definition:* Built-in, modality-specific assumptions of an architecture. Transformers have few, which lets them adapt to very different corpora but generally requires larger training sets.
  - *Examples (1, folded):*
    - `2.1.2-03e1` [illustration · architecture] Alternatives built on features of the data: HyenaDNA (long genomic context), Caduceus (equivalence of the two DNA strands), PINNACLE (protein interaction networks). · models: hyenadna, caduceus, pinnacle

**2.1.2-04** Training scheme determines what the model is rewarded to learn.

- **Masked language modeling** `masked-language-modeling`  ·  both · technique group: Training scheme
  - *Definition:* A training approach in which randomly hidden tokens are predicted from the surrounding sequence.
  - *Examples (2, folded):*
    - `2.1.2-04e1` [illustration · training scheme] Masked: ESM2. · models: esm2
    - `4.1-04e1` [illustration · training scheme] ESM2 likelihoods score tolerance of a mutation but ESM2 is not built to write new sequences; ProGen2 and Evo are natural generators of new proteins and genomes. · models: progen2, esm2, evo
- **Autoregressive modeling** `autoregressive-modeling`  ·  both · technique group: Training scheme
  - *Definition:* A training approach in which each token is predicted from those before it, which makes these models natural generators of new sequences.
  - *Examples (3, folded):*
    - `2.1.2-04e3` [illustration · training scheme] Autoregressive: ProGen2, Evo. · models: progen2, evo
    - ▸ *Finding: Models can design new, functional molecules*
      - `4.2-04e1` [success · training scheme · from 4.2-04 → shown with 4.2-07] ProGen produced artificial lysozymes with measurable catalytic activity. · models: progen
      - `4.2-04e2` [success · training scheme · from 4.2-04 → shown with 4.2-07] ESM3, prompted with structure and function tokens, generated a fluorescent protein distant from known natural sequences. · models: esm3
- **Contrastive / metric learning** `contrastive-learning`  ·  both · technique group: Training scheme
  - *Definition:* A training approach that pulls related examples close together in embedding space and pushes unrelated ones apart.
  - *Examples (2, folded):*
    - `2.1.2-04e2` [illustration · training scheme] Contrastive: Orthrus (splice isoforms and orthologs of the same gene as related RNAs); SCimilarity (cells of the same type placed near one another). · models: orthrus, scimilarity
    - `4.1-04e2` [illustration · training scheme] SCimilarity's embeddings suit searching an atlas for similar cells, not predicting perturbation response. · models: scimilarity

**2.1.2-05** Evaluation scheme determines how the model is judged, at two levels that do not always agree.

- **Intrinsic vs. downstream evaluation** `intrinsic-vs-downstream-evaluation`  ·  both · technique group: Evaluation
  - *Definition:* Two levels of evaluating a model. Intrinsic evaluation asks whether the model has learned the structure of its data; downstream evaluation asks whether it helps with a practical task, increasingly on shared benchmarks. The two do not always agree.
  - *Examples (3, folded):*
    - `2.1.2-05e1` [illustration · evaluation] Intrinsic: ESM2 recovering residue contacts. Downstream: predicting mutation effects on ProteinGym. · models: esm2, proteingym
    - `5.1-02e1` [limitation] Bulk transcriptomics has no dedicated FM benchmark; spatial benchmarks are only emerging; multi-omics and RNA models have few head-to-head comparisons.
    - `5.1-02e2` [limitation] Protein structure (CASP), protein fitness (ProteinGym), and perturbation prediction (Virtual Cell Challenge) have blind or community-maintained evaluations; sequence-to-function models are mostly evaluated on developer-defined suites, with cross-individual tests appearing only recently. · models: proteingym, casp

**2.1.2-06** Post-analysis determines how a trained model is used.

- **Transfer learning** `transfer-learning`  ·  both · technique group: Post-analysis
  - *Definition:* Carrying knowledge captured in the embedding during pretraining over to a new task by probing or fine-tuning, so that a small labeled dataset suffices where training from scratch would require a large one.
  - *Examples: none (definition only)*
- **In silico perturbation** `in-silico-perturbation`  ·  both · technique group: Post-analysis
  - *Definition:* Simulating a change, such as deleting a gene, and observing how a cell's embedding shifts.
  - *Examples (2, folded):*
    - `2.1.2-06e1` [illustration · post-analysis] Using a model as is: scoring mutations by likelihood; Geneformer's *in silico* deletion. · models: geneformer
    - ▸ *Finding: Early studies suggest learned knowledge can be read out*
      - `4.2-06e2` [success · post-analysis · from 4.2-06 → shown with 4.2-07] Geneformer's simulated gene deletion nominated therapeutic targets for cardiomyopathy that were then supported experimentally. · models: geneformer
- **Interpretability analysis** `interpretability-analysis`  ·  both · technique group: Post-analysis
  - *Definition:* Analysis of how a model arrives at its outputs, for example which input positions drive a prediction or which internal features match known biology. It can reveal whether a model relies on genuine biology or on shortcuts in the data.
  - *Examples (4, folded):*
    - `2.1.2-06e2` [illustration · post-analysis] Interpretability: which input positions drive a prediction; which internal features match known biology.
    - `4.1-06e1` [illustration · post-analysis] Probing, fine-tuning, and interpretability analysis each expose different knowledge.
    - ▸ *Finding: A correct answer does not show the model knows why*
      - `4.3-07e2` [limitation · post-analysis · from 4.3-07 → shown with 4.3-08] Attention weights should not be read as biological mechanisms; sparse-autoencoder dictionaries so far cover only a few protein and genomic models.
      - `4.3-07e3` [limitation · post-analysis · from 4.3-07 → shown with 4.3-08] For most models it remains unknown whether a correct prediction reflects real biology or a shortcut that works on the test.


### 2.2. A Tour of the Foundation Models

**2.2-01** FMs are differentiated by inputs (data type) and outputs (task); each is shaped by choices specific to its data and task, so it is foundational mainly within that range, and this dependence is the basis of the knowledge boundary.

- **Inputs vs. outputs (data axis, task axis)** `inputs-vs-outputs`  ·  concept
  - *Definition:* Two axes for organizing biological FMs: inputs (the type of biological data) and outputs (the task the model performs). Inputs differ mainly in vocabulary, corpus, and architecture; outputs mainly in training scheme and post-analysis.
  - *Examples (7, folded):*
    - ▸ *Finding: RNA: models read sequence and fold structure; non-coding RNA models need not capture mRNA function*
      - `2.2.1-03e1` [illustration · data · from 2.2.1-03 → shown with 2.2.1-01] Single-stranded RNA folds back on itself; RNA-FM and RiNALMo (trained on tens of millions of non-coding RNAs) recover which bases pair, much as ESM2 recovers protein contacts. · models: rna-fm, rinalmo, esm2
      - `2.2.1-03e2` [illustration · data · from 2.2.1-03 → shown with 2.2.1-01] mRNA: function depends on coding sequence, splicing, regulatory regions; Orthrus uses contrastive learning across splice isoforms and orthologs. · models: orthrus
    - ▸ *Finding: Protein: the vocabulary is settled, so innovation moves to other design elements*
      - `2.2.1-06e1` [illustration · data · from 2.2.1-06 → shown with 2.2.1-01] ESM2 and ProtTrans established how much can be learned from sequence alone at scale. · models: prottrans, esm2
      - `2.2.1-06e2` [illustration · data · from 2.2.1-06 → shown with 2.2.1-01] SaProt and ESM3 add structure/function tokens; ProGen2 adopts next-token prediction for generation; Ankh matches larger models at a fraction of the pretraining cost. · models: progen2, saprot, ankh, esm3
    - ▸ *Finding: Multi-omics: no shared vocabulary; models take different routes to align modalities*
      - `2.2.1-07e1` [illustration · data · from 2.2.1-07 → shown with 2.2.1-01] GeneCompass: enriches gene tokens with prior knowledge. · models: genecompass
      - `2.2.1-07e3` [illustration · data · from 2.2.1-07 → shown with 2.2.1-01] AIDO: separate DNA, RNA, protein, and cell models, with embeddings combined. · models: aido
    - `2.2-01e1` [illustration] Contrast: a general-purpose LLM serves many kinds of text and tasks.


#### 2.2.1. Inputs: Biological Data Types

**2.2.1-01** Moving from DNA and protein to cells and tissues, the vocabulary unit grows (residue → gene → whole cell → cell in its neighborhood) and the learnable grammar changes with it; each data type poses its own design problem, such as how to tokenize DNA, how to represent expression levels, or how to align modalities.

- **Bulk RNA sequencing** `bulk-rna-seq`  ·  concept
  - *Definition:* A measurement of the average expression of all cells in a tissue sample, which loses cellular resolution.
  - *Examples (1, folded):*
    - ▸ *Finding: Bulk and spatial: bulk trades resolution for clinical linkage; spatial adds neighborhood*
      - `2.2.1-05e1` [illustration · data · from 2.2.1-05 → shown with 2.2.1-01] BulkFormer: trained on bulk profiles linked to tissue type, disease, and clinical outcome; gene remains the vocabulary unit. · models: bulkformer
- **Spatial transcriptomics** `spatial-transcriptomics`  ·  concept
  - *Definition:* A measurement that records where each cell sits in a tissue section.
  - *Examples (1, folded):*
    - ▸ *Finding: Bulk and spatial: bulk trades resolution for clinical linkage; spatial adds neighborhood*
      - `2.2.1-05e2` [illustration · data · from 2.2.1-05 → shown with 2.2.1-01] Nicheformer: trained jointly on dissociated and spatial data, so a cell's embedding reflects its expression and its neighborhood. VirTues: extends spatial modeling to protein markers in multiplexed tissue images. · models: nicheformer, virtues
- **Graph neural network** `graph-neural-network`  ·  both · technique group: Architecture
  - *Definition:* A neural network that updates the embedding of each node (here, each protein) with information from its interaction partners.
  - *Examples (1, folded):*
    - ▸ *Finding: Multi-omics: no shared vocabulary; models take different routes to align modalities*
      - `2.2.1-07e2` [illustration · data · from 2.2.1-07 → shown with 2.2.1-01] PINNACLE: protein interaction networks built per cell type; the same protein gets a different embedding in each cell type. · models: pinnacle


#### 2.2.2. Outputs: Tasks

**2.2.2-01** Outputs fall into three tasks (representation, prediction, generation), and each carries its own limit: what a model embeds determines which questions it can serve, a predictive model can predict only what has been measured, and a generative model's vocabulary determines what it can write.

- **Representation model** `representation-model`  ·  concept
  - *Definition:* A model that converts each input into an embedding; because it is trained without labels (self-supervised), it can draw on very large unannotated corpora.
  - *Examples (2, folded):*
    - `2.2.2-02e1` [illustration · from 2.2.2-02 → shown with 2.2.2-01] ESM2 embeddings used to predict structure, annotate function, and score mutations. · models: esm2
    - `2.2.2-02e2` [illustration · from 2.2.2-02 → shown with 2.2.2-01] What is embedded: a residue or protein (ESM2), a DNA segment (Nucleotide Transformer, Evo), a gene in context (Geneformer, scGPT), a whole cell (UCE). · models: nucleotide-transformer, geneformer, scgpt, uce, esm2, evo
- **Predictive model** `predictive-model`  ·  concept
  - *Definition:* A model trained on paired measurements (supervised) to answer one fixed question, so it can predict only what has been measured.
  - *Examples (5, folded):*
    - `2.2.2-03e1` [illustration · from 2.2.2-03 → shown with 2.2.2-01] AlphaFold: amino acid sequence → 3D coordinates of every atom (from PDB structures). · models: pdb, alphafold
    - `2.2.2-03e2` [illustration · from 2.2.2-03 → shown with 2.2.2-01] AlphaGenome: up to 1 Mb of sequence → thousands of tracks (RNA expression, chromatin accessibility, TF binding) at up to single-base resolution; extends Enformer and Borzoi; Scooby adapts Borzoi to single cells. · models: enformer, borzoi, scooby, alphagenome
    - `2.2.2-03e3` [illustration · from 2.2.2-03 → shown with 2.2.2-01] Variant-effect predictors (clinical labels are scarce, so they use other signals): EVE (evolutionary conservation), AlphaMissense (adapts AlphaFold with human population frequencies), popEVE (combines both so scores are comparable across proteins). · models: alphamissense, popeve, eve, alphafold
    - ▸ *Finding: Application-level studies show similar gaps*
      - `4.3-06e1` [limitation · evaluation · from 4.3-06 → shown with 4.3-08] AlphaMissense: meaningful discordance with curated clinical evidence across 5,845 missense variants in 59 disease genes. · models: alphamissense
      - `4.3-06e2` [limitation · evaluation · from 4.3-06 → shown with 4.3-08] Structure-confidence scores poorly separated successes from failures among 614 experimentally characterized de novo protein designs.
- **Generative model** `generative-model`  ·  concept
  - *Definition:* A model that writes new sequences or states rather than scoring existing ones; its vocabulary determines what it can write.
  - *Examples (2, folded):*
    - `2.2.2-04e1` [illustration · from 2.2.2-04 → shown with 2.2.2-01] Proteins: ProGen (protein-family tag → full sequence, one amino acid at a time); ESM3 (prompted with partial structure or function). · models: progen, esm3
    - `2.2.2-04e2` [illustration · from 2.2.2-04 → shown with 2.2.2-01] Nucleic acids: Evo (genomes), regLM (regulatory DNA with specified activity), CodonTransformer (organism-specific codons), gRNAde (RNA that folds into a target structure). · models: codontransformer, grnade, reglm, evo
- **Perturbation model** `perturbation-model`  ·  concept
  - *Definition:* A model that, given a cell and an intervention such as a gene knockout, produces the expected expression profile, a state that was never measured. It lies between prediction and generation.
  - *Examples (1, folded):*
    - `2.2.2-04e3` [illustration · from 2.2.2-04 → shown with 2.2.2-01] Perturbation: CellOT (maps control onto perturbed populations), GEARS (gene-relationship graph for unseen combinations), State (trained on a large perturbation corpus, treats whole cells as tokens). · models: cellot, gears, state


## 3. Where a Foundation Model Enters Agentic Systems

**3-01** An agent is not a model; it coordinates an LLM, the user, and many tools to carry out multistep tasks.

- **Hallucination** `hallucination`  ·  concept
  - *Definition:* A fluent but false statement produced by an LLM.
  - *Examples: none (definition only)*

**3-02** The first responses connected the model to outside information; reasoning models make multistep answers more reliable but add no information, so only external components extend what the system draws on.

- **Retrieval-augmented generation (RAG)** `rag`  ·  both · technique group: Agent components
  - *Definition:* Having the model base its answer on retrieved documents, such as papers or database entries, so that answers are current and traceable to a source.
  - *Examples: none (definition only)*
- **Function calling** `function-calling`  ·  both · technique group: Agent components
  - *Definition:* Letting the model write a request to an external program, such as a database query or an analysis script, and read back the result.
  - *Examples: none (definition only)*
- **Reasoning model** `reasoning-model`  ·  both · technique group: Agent components
  - *Definition:* An LLM trained to write out intermediate steps and rewarded when the final answer to a checkable problem is correct.
  - *Examples (2, folded):*
    - `3-02e1` [illustration] External components that can extend the system: documents, tools, or a connected FM.
    - `3-07e1` [illustration] A reasoning model's written steps are not guaranteed valid or faithful; biological inference, unlike mathematical proof, starts from incomplete premises that only experiments can test.

**3-03** As tools multiplied, standards and management layers followed, but access to a tool does not teach an agent to use it well.

- **Model Context Protocol (MCP)** `mcp`  ·  both · technique group: Agent components
  - *Definition:* A standard way, released in late 2024, of connecting tools to models.
  - *Examples (1, folded):*
    - `3-03e1` [illustration] MCP analogy: like USB for computer devices; a database, program, or FM wrapped once as an MCP tool can be used by any compatible agent.
- **Skill files** `skill-files`  ·  both · technique group: Agent components
  - *Definition:* Written instructions an agent loads when needed, such as the steps of a standard analysis or when a tool's output should not be trusted (introduced in 2025).
  - *Examples (1, folded):*
    - `3-03e2` [illustration] Skill file contents: steps of a standard analysis, or when a tool's output should not be trusted.
- **Agent harness** `agent-harness`  ·  both · technique group: Agent components
  - *Definition:* The layer that manages long-running agent tasks by repeating the plan–act–revise cycle, providing a workspace for code and files, and asking a human for approval at key decisions.
  - *Examples: none (definition only)*

**3-04** Because the components are general-purpose, biological agents are assembled quickly, including multi-agent systems.

- **Multi-agent system** `multi-agent-system`  ·  both · technique group: Agent components
  - *Definition:* A system that assigns roles to separate LLM agents.
  - *Examples (1, folded):*
    - `3-04e3` [illustration] Virtual Lab: agents acting as a principal investigator and specialist scientists designed nanobodies; the AI co-scientist and Robin extend this to hypothesis generation. · models: virtual-lab, ai-co-scientist, robin

**3-05** A foundation model can enter an agent in four ways, which differ in what the LLM receives and thus in whose knowledge boundary the agent inherits.

- **Tool route** `tool-route`  ·  both · technique group: Agent components
  - *Definition:* A way an FM enters an agent: the agent reads the FM's output as text. It acts while the agent works.
  - *Examples (2, folded):*
    - `1-06e2` [illustration] Agents calling FMs as tools: Biomni, Virtual Biotech. · models: biomni, virtual-biotech
    - `3-05e1` [illustration] Tool: Virtual Lab agents called ESM, AlphaFold-Multimer, and Rosetta to refine nanobodies; Paper2Agent's AlphaGenome tools outperformed general agents, showing that packaging matters. · models: alphagenome, alphafold-multimer, paper2agent, virtual-lab, rosetta
- **Text route** `text-route`  ·  both · technique group: Agent components
  - *Definition:* A way an FM enters an agent: data are rewritten as language (e.g., each cell as a list of its top genes). It shapes the LLM during training.
  - *Examples (1, folded):*
    - `3-05e2` [illustration] Text: each cell as a list of its top genes.
- **Encoder route** `encoder-route`  ·  both · technique group: Agent components
  - *Definition:* A way an FM enters an agent: embeddings are converted into the LLM's input, so it reads biological data alongside text. It shapes the LLM during training.
  - *Examples (3, folded):*
    - `3-05e3` [illustration] Encoder: ChatNT, CellWhisperer, BioReason. · models: chatnt, cellwhisperer, bioreason
    - `3-06e1` [illustration] BioReason: on pathway questions the LLM alone reached 90% and the encoder made little difference; on variant classification it reached 49%, rising to 80% with Evo 2 vs. 61% with Nucleotide Transformer. · models: nucleotide-transformer, evo-2, bioreason
    - `5.1-03e1` [limitation] Systems feeding FM embeddings into an LLM rarely report controls separating encoder and LLM contributions; applied to six systems, BioReason and BioReason-Pro were as accurate with shuffled biological inputs as with intact ones. · models: bioreason-pro, bioreason
- **Verifier route** `verifier-route`  ·  both · technique group: Agent components
  - *Definition:* A way an FM enters an agent: an FM scores a reasoning model's answers during training, so its errors become part of the reward. It shapes the LLM during training.
  - *Examples (1, folded):*
    - `3-05e4` [illustration] Verifier: rbio1. · models: rbio1

**3-06** Only the encoder route lets the LLM work with raw data; it matters when the answer lies beyond the LLM's textual knowledge.


**3-07** Reinforcement learning, more reasoning, and packaging do not move the FM's boundary or tell an agent when to trust it; humans stay in the loop, and an agent is only as useful as our understanding of each FM's boundary.

- **Reinforcement learning** `reinforcement-learning`  ·  both · technique group: Training scheme
  - *Definition:* Training that rewards outcomes. Here it improves how a system uses the knowledge it can reach, but does not move the FM's boundary.
  - *Examples: none (definition only)*


## 4. Knowledge Boundaries Revealed by Existing Studies

**4-01** Every model has a knowledge boundary; LLM boundaries are rarely visible, but learning biology from data is closer to deciphering an extinct language.

- **Decipherment questions** `decipherment-questions`  ·  concept
  - *Definition:* The questions used to organize the evidence: can any structure be recovered, does it carry meaning, can it be used to write, and which parts remain unreadable? Two more are added in the review: does knowledge extend beyond the training data, and can researchers read it out?
  - *Examples (3, folded):*
    - `4-01e1` [illustration] Why "extinct": the vocabulary must be inferred, no living speaker can confirm the grammar, and the only surviving texts are the measurements assays happened to record.
    - `4-01e2` [illustration] Why LLM boundaries are hidden: modern language is densely represented in their training data.
    - `4.2-01e3` [illustration] Each answer rests on comparing model outputs with independent data or on laboratory tests of designs.

**4-02** The review focuses on FMs because their boundaries are the least characterized; agents add an orchestration boundary of their own that current benchmarks cannot yet measure separately.

- **Orchestration boundary** `orchestration-boundary`  ·  concept
  - *Definition:* An agent's own limit in selecting and combining tools; agents with the same tools can differ.
  - *Examples (1, folded):*
    - `4-02e1` [illustration] BixBench scores only end-to-end answers. · models: bixbench


### 4.1. How the Five Design Elements Define the Knowledge Boundary

**4.1-01** Each design element sets a different limit on what a model can learn and how it can be used; this holds for any model, but FMs are reused far beyond their original purpose, so the limits travel with them.


**4.1-02** Data sets what can be known.


**4.1-03** Architecture sets which relationships can be captured efficiently; an interaction longer than the input window cannot be learned, however much data is available.

- **Convolutional neural network (CNN)** `cnn`  ·  both · technique group: Architecture
  - *Definition:* A neural network that detects short local patterns, such as a TF binding motif.
  - *Examples (1, folded):*
    - `4.1-03e1` [illustration · architecture] ChromBPNet (CNN): ~2 kb at single-base resolution, suited to motifs and variants within them. Enformer (adds attention): regulatory elements ~100 kb away. HyenaDNA: one million nucleotides. · models: hyenadna, enformer, chrombpnet

**4.1-04** Training scheme sets what is rewarded, and therefore what a model is good at; none of these objectives directly rewards learning cause and effect.


**4.1-05** Evaluation sets what becomes visible.


**4.1-06** Post-analysis sets what becomes accessible: knowledge may be present yet hard to extract, and a correct prediction does not show the model learned the mechanism.



### 4.2. What Foundation Models Have Captured About Biology

**4.2-01** Without labels, FMs capture statistical patterns that reflect general and functional properties of their building blocks, but not the physical mechanisms behind them.


**4.2-07** Together: self-supervised training captures real biological knowledge, from residue chemistry to evolutionary constraint on function, reusable for variant interpretation and design; the clearest successes are in proteins, where the corpus is largest and the rules are written most directly into sequence.



### 4.3. Where Foundation Model Knowledge Stops

**4.3-01** These successes raise the question of when predictions remain reliable; many independent studies compare FMs with simple alternatives, and the limits they reveal are organized by design element.

- **Simple baselines** `simple-baselines`  ·  both · technique group: Evaluation
  - *Definition:* Deliberately simple comparison methods: linear or logistic regression, one-hot encodings of sequence, or simply the average of the training data.
  - *Examples (6, folded):*
    - `4.1-05e3` [illustration · evaluation] How a benchmark is split and which simple baselines it includes decides which weaknesses can be seen.
    - ▸ *Finding: Observed states rarely predict the effect of an intervention beyond simple baselines*
      - `4.3-04e2` [limitation · training scheme · from 4.3-04 → shown with 4.3-08] For genetic perturbation responses, simple linear models and even the average of the training data match or outperform FMs.
      - `4.3-04e3` [limitation · training scheme · from 4.3-04 → shown with 4.3-08] Single-cell: Geneformer and scGPT embeddings did not outperform simple baselines without fine-tuning; L1-regularized logistic regression rivaled scBERT; parameter-free representations match single-cell FMs; GenePT suggests part of what these models learn is already recorded in text. · models: geneformer, scgpt, scbert, genept
      - `4.3-04e4` [limitation · training scheme · from 4.3-04 → shown with 4.3-08] Similar results for mutation-dense protein design and for multi-omics integration (no uniform advantage across 23 methods).
    - ▸ *Finding: Tests sometimes do not measure what they claim*
      - `4.3-05e1` [limitation · evaluation · from 4.3-05 → shown with 4.3-08] DNA language models are spread across competing benchmarks, with inconsistent gains over lightweight supervised models.
    - ▸ *Finding: Application-level studies show similar gaps*
      - `4.3-06e3` [limitation · evaluation · from 4.3-06 → shown with 4.3-08] Most of 21 pretrained RNA language models did not outperform one-hot encoding for secondary-structure prediction once closely related sequences were removed from the test set.

**4.3-08** These studies shift the question from whether FMs learn biology to what they have learned and where it stops; the boundary has four layers, and benchmark performance, confidence scores, transferable embeddings, and reliability in application must be established separately.

- **The layers of the boundary (grouped into four)** `four-layers`  ·  concept
  - *Definition:* (1) Knowledge missing because observations were never or rarely collected; (2) knowledge hard to learn because the architecture cannot span it or the objective does not reward it (e.g., cause and effect); (3) capability hidden or exaggerated by evaluation; (4) knowledge present in the model but inaccessible to current analysis.
  - *Examples: none (definition only)*

*Evidence concepts (hosts for examples of §4.3; no home claim):*
- **Sampling bias** `sampling-bias`  ·  concept · example_only (no home claim, no landing link)
  - *Definition:* A model's patterns partly reflecting how often related examples were sampled, rather than the biology itself (for example, unequal sampling across the tree of life).
  - *Examples (1, folded):*
    - ▸ *Finding: Models capture both biology and the history of sampling*
      - `4.3-02e1` [limitation · data · from 4.3-02 → shown with 4.3-08] Protein language model likelihoods partly reflect how often related sequences were sampled across the tree of life rather than fitness alone.
- **Circular annotation** `circular-annotation`  ·  concept · example_only (no home claim, no landing link)
  - *Definition:* A benchmark or annotator scoring well partly because curated databases shaped both the training data and the benchmark labels.
  - *Examples (1, folded):*
    - ▸ *Finding: Models capture both biology and the history of sampling*
      - `4.3-02e2` [limitation · data · from 4.3-02 → shown with 4.3-08] Gene-function annotation can become circular: curated databases shaped both LLM-based annotators' training and the benchmark labels; they perform worse on orphan genes and non-model organisms.
- **Systematic variation** `systematic-variation`  ·  concept · example_only (no home claim, no landing link)
  - *Definition:* Expression differences shared across perturbations in general, unrelated to any specific perturbation. They can dominate common metrics, so that predicting an average response scores well.
  - *Examples (2, folded):*
    - ▸ *Finding: Tests sometimes do not measure what they claim*
      - `4.3-05e2` [limitation · evaluation · from 4.3-05 → shown with 4.3-08] Common perturbation metrics are dominated by systematic expression differences unrelated to the specific perturbation, so a model can score well by predicting an average response.
      - `4.3-05e3` [success · evaluation · from 4.3-05 → shown with 4.3-08] Conversely, when metrics are calibrated against an uninformative mean baseline and a positive control, several deep-learning perturbation models do outperform simple baselines; part of the reported parity reflects the metric, not the model.


## 5. Open Challenges: A Balanced Assessment

**5-01** Stepping back to the field, three broader limitations: gaps in how models are evaluated, the bet on one ever-larger general-purpose model, and the field's early developmental stage.



### 5.1. Gaps in How Foundation Models Are Evaluated

**5.1-01** Independent evaluation is concentrated in a few areas (protein sequence, single-cell representation, perturbation prediction) and usually tests only one design element, the evaluation scheme.


**5.1-02** Evaluation is uneven across modalities and tasks, and few models report whether they can signal that a query lies outside their boundary.


**5.1-03** Agents and LLMs as users of FMs are barely evaluated: benchmarks test general analysis, not whether the right FM is chosen or its output interpreted correctly.



### 5.2. Betting on a Single General-Purpose Model

**5.2-01** Much of the field's momentum comes from the LLM analogy (scaling laws), yet larger protein language models do not consistently predict mutational effects better.

- **Scaling laws** `scaling-laws`  ·  concept
  - *Definition:* In LLMs, the relationship by which performance improves predictably as parameters, training data, and computing budget grow.
  - *Examples (3, folded):*
    - ▸ *Finding: One-mutation effects are often missed, and scale has not closed the gap*
      - `4.3-03e2` [limitation · architecture · from 4.3-03 → shown with 4.3-08] Larger protein language models do not consistently improve zero-shot fitness prediction; downstream tasks often reuse features learned early in pretraining.
    - `5.2-02e1` [illustration] Scale: molecule → cell → tissue → organism.
    - `5.2-03e1` [illustration] Multimodal proposals: PINNACLE, AIDO. · models: pinnacle, aido

**5.2-02** Language has a unified structure that supports one general model; biology is heterogeneous across scale, data type, species, and experimental condition.


**5.2-03** The language analogy only partially holds (vocabulary not fixed, grammar largely unknown, corpus incomplete); multimodal proposals bridge only subsets, and the LLM trajectory is one reference point among several.



### 5.3. Where Is the Field Developmentally?

**5.3-01** AI for biology is an emerging discipline in its infancy, so present strengths and limitations should be read as features of a transient stage, through two complementary lenses.


**5.3-02** Lens 1, scientific maturity: most FM work sits at the first (descriptive) stage, which is consistent with simple baselines repeatedly matching FMs.

- **Stages of biological science** `stages-of-biological-science`  ·  concept
  - *Definition:* Observation and classification, then mechanistic understanding of structure, function, and causality, and ultimately engineering: the design of biological systems from first principles.
  - *Examples (2, folded):*
    - `5.3-02e1` [illustration] Historical parallel: Darwin's cataloguing of species.
    - `5.3-02e2` [illustration] Claims framed in engineering-stage language, such as "de novo design," should be read with this stage in mind.

**5.3-03** Lens 2, evolutionary competition: the current FM expansion resembles the open-niche phase, and whether the field moves toward specialized, boundary-filling models is a consequential consideration for resources and priorities.

- **Adaptive radiation** `adaptive-radiation`  ·  concept
  - *Definition:* After periods of open ecological opportunity that favor large generalists, the adaptive radiation that follows favors smaller organisms fitted to specific niches.
  - *Examples: none (definition only)*


## 6. Future Directions and Recommendations


### 6.1. Specialized Models, Coordinated by Agents

**6.1-01** Because biological data are heterogeneous, the field need not wait for a single general model; the evidence points to a portfolio of broad models supplying transferable embeddings alongside narrower models fitted to boundary regions.


**6.1-02** Agents are well placed to manage such a portfolio.



### 6.2. Making Knowledge Boundaries Explicit to Agents

**6.2-01** To route correctly, an agent must know where each model's boundary lies; today, errors from outside a boundary can propagate silently.


**6.2-02** Proposal: release each FM with a structured boundary statement, organized by the five design elements.

- **Boundary statement** `boundary-statement`  ·  concept
  - *Definition:* A structured record of an FM's limits, released with the model, in the spirit of model cards and datasheets and organized by the five design elements.
  - *Examples (3, folded):*
    - `6.2-01e1` [illustration] Tool descriptions state what a tool does but seldom where it fails; a variant score from a model trained without population data looks as authoritative as a well-supported result.
    - `6.2-02e1` [illustration] Contents of a boundary statement, organized by the five design elements: species, assays, and conditions in the training data; context length and tokenization; training objective; benchmarks used, including comparisons with simple baselines; and the post-analysis methods under which the reported results hold.
    - `6.2-03e1` [illustration] Just as GeneAgent checks its claims against curated databases, an agent could confirm a query lies within a model's training and evaluation domain before relying on its output. · models: geneagent

**6.2-03** In machine-readable form, the statement helps a biologist decide whether to trust a result and an agent decide whether to call the model.


**6.2-04** Boundary statements also show where new data are most needed, and closed experimental loops can extend a boundary with new measurements rather than more of the same data.

- **Self-driving laboratory** `self-driving-lab`  ·  both · technique group: Agent components
  - *Definition:* Robotic platforms that run experiments chosen by a model and return the results for the next round.
  - *Examples (1, folded):*
    - `6.2-04e1` [illustration] Agents that plan experiments + FMs that propose candidates + self-driving labs = closed loops that could target boundary regions directly and extend the boundary with new measurements.

**6.2-05** The knowledge boundary would then become the interface between foundation models and agentic systems.



### 6.3. Community as Scientific Infrastructure

**6.3-01** Making boundaries explicit is also a problem of community organization; open science offers precedents.


**6.3-02** Cross-disciplinary training should aim at shared literacy, not at making every biologist a model builder.

- **Shared literacy** `shared-literacy`  ·  concept
  - *Definition:* A working understanding of both biology and AI across the two communities. The aim is not to make every biologist a model builder.
  - *Examples (1, folded):*
    - `6.3-02e1` [illustration] Embedded-scientist programs, reciprocal laboratory placements, fellowships, and professional community-management roles offer deeper cross-disciplinary exposure than short courses.

**6.3-03** A community-maintained registry linking each model to its boundary statement, independent evaluations, known limitations, and replication results would give biologists and agents a living record of each model's knowledge boundary.

- **Model registry (proposed)** `model-registry`  ·  concept
  - *Definition:* A proposed community-maintained resource linking each model to its boundary statement, independent evaluations, known limitations, and replication results.
  - *Examples (2, folded):*
    - `6.3-01e1` [illustration] UniProt and the PDB became trusted infrastructure; open-source ecosystems made models widely reusable; blind assessments such as CASP and CAGI established credible measures of progress. · models: uniprot, pdb, casp, cagi
    - `6.3-03e1` [illustration] Existing precedent for model exchange: Kipoi repository. · models: kipoi


## 7. Conclusion

**7-01** AI for biology advances along two complementary paths: FMs compress large datasets into reusable representations, and agents compose literature, databases, and software; agents are bounded by what has been documented, FMs by the five design elements.


**7-02** Integrating the two depends on making FM knowledge boundaries explicit: the five elements provide a common template, inputs and outputs locate a model in the landscape, and published evidence shows where current boundaries lie.


**7-03** Explicit boundaries give biologists a principled basis for trust, builders a concrete target for improvement, and agents the information to select and interpret models; as measurement expands, they can serve as a shared language between AI and biology.


---

# Technique-only entries

Terms that appear inside examples in the review but are not needed to follow the argument. They live on the Techniques page. Definitions are drawn from the review text; technique blocks (variants, pitfalls) are for authors/curators to extend from the references.


## Data and tokenization

- **k-mer tokenization** `k-mer-tokenization`
  - *Definition:* Splitting DNA into fixed-length tokens of k nucleotides. Nucleotide Transformer uses six-nucleotide k-mers; such tokens can split regulatory motifs and hide the effect of a single-nucleotide variant.
  - *Used by:* nucleotide-transformer  ·  *Source in the draft:* 2.1.1-02e3, 2.2.1-02e1
- **Learned variable-length tokens** `learned-variable-length-tokens`
  - *Definition:* Multinucleotide tokens whose lengths are learned from genomic sequences rather than fixed in advance (DNABERT-2, GROVER). Like k-mers, they can split motifs and hide single-nucleotide variants.
  - *Used by:* dnabert-2, grover  ·  *Source in the draft:* 2.2.1-02e1, 2.2.1-02e2
- **Single-nucleotide tokenization** `single-nucleotide-tokenization`
  - *Definition:* Keeping one nucleotide per token to retain single-nucleotide resolution over long distances; it requires architectures that remain efficient over long inputs.
  - *Used by:* hyenadna, caduceus, evo  ·  *Source in the draft:* 2.2.1-02e3
- **Expression-rank encoding** `expression-rank-encoding`
  - *Definition:* Representing a cell as genes ordered by expression rank, so that expression is encoded only by position in the input and not by its quantitative value; this sidesteps platform- and processing-specific confounders.
  - *Used by:* geneformer  ·  *Source in the draft:* 2.2.1-04e1, 2.2.1-04e2
- **Binned expression-value encoding** `binned-expression-encoding`
  - *Definition:* Pairing each gene with a binned expression value, so that expression magnitude is represented explicitly.
  - *Used by:* scgpt  ·  *Source in the draft:* 2.2.1-04e2
- **Genes represented by protein embeddings** `genes-as-protein-embeddings`
  - *Definition:* Representing each gene by the ESM2 embedding of its protein rather than by a fixed gene list, so that cells from species absent from training can be placed in a shared space.
  - *Used by:* uce, esm2  ·  *Source in the draft:* 2.2.1-04e3, 4.2-05e3
- **Structure and function tokens** `structure-function-tokens`
  - *Definition:* Adding tokens for local structure or function alongside amino acids: SaProt pairs each amino acid with a local-structure token, and ESM3 can be prompted with structure and function tokens.
  - *Used by:* saprot, esm3  ·  *Source in the draft:* 2.2.1-06e2, 4.2-05e1
- **Prior-knowledge-enriched tokens** `prior-knowledge-tokens`
  - *Definition:* Enriching gene tokens with prior knowledge before training.
  - *Used by:* genecompass  ·  *Source in the draft:* 2.2.1-07e1
- **Sequence clustering before training** `sequence-clustering`
  - *Definition:* Clustering protein databases by sequence similarity before training, because many sequences are near-duplicates of close evolutionary relatives.
  - *Used by:* uniref  ·  *Source in the draft:* 2.1.1-04e3
- **Alignment-augmented input** `alignment-augmented-input`
  - *Definition:* Adding aligned sequences of related genomes or proteins as input, which makes conservation visible. GPN-MSA adds alignments from 100 vertebrate genomes; AlphaFold also uses alignments of related sequences.
  - *Used by:* gpn-msa, alphafold  ·  *Source in the draft:* 4.2-02e3, 4.2-05e2

## Architecture

- **Long-context architectures** `long-context-architectures`
  - *Definition:* Architectures designed to stay efficient over very long inputs; HyenaDNA reaches one million nucleotides.
  - *Used by:* hyenadna, caduceus  ·  *Source in the draft:* 2.1.2-03e1, 4.1-03e1

## Training scheme

- **Likelihood scoring of variants** `likelihood-scoring-of-variants`
  - *Definition:* Scoring how plausible a sequence is given the sequences a model was trained on; a mutation that makes the sequence much less plausible is more likely to disrupt function.
  - *Used by:* esm2  ·  *Source in the draft:* 2.1-02e2, 4.2-03e1
- **Prompting with partial structure or function** `prompting-partial-structure-function`
  - *Definition:* Generating a sequence by giving the model a partial specification of structure or function as a prompt (ESM3).
  - *Used by:* esm3  ·  *Source in the draft:* 2.2.2-04e1

## Evaluation

- **Similarity-aware train/test splitting** `similarity-aware-splitting`
  - *Definition:* Removing from the test set sequences that have close relatives in the training set, so that a high score reflects learned rules and not recall.
  - *Used by:* (none named in the review)  ·  *Source in the draft:* 4.1-05e2, 4.3-06e3
- **Calibrated metrics (mean baseline + positive control)** `calibrated-metrics`
  - *Definition:* Calibrating a metric against both an uninformative mean baseline and a positive control. Under such metrics several deep-learning perturbation models do outperform simple baselines.
  - *Used by:* (none named in the review)  ·  *Source in the draft:* 4.3-05e3
- **Shuffled-input control** `shuffled-input-control`
  - *Definition:* Replacing biological inputs with shuffled ones to test whether the encoder contributes to a system's accuracy. BioReason and BioReason-Pro were as accurate with shuffled inputs as with intact ones.
  - *Used by:* bioreason, bioreason-pro  ·  *Source in the draft:* 5.1-03e1

## Agent components

- **Packaging a model as an MCP tool** `packaging-as-mcp-tool`
  - *Definition:* Wrapping a database, program, or FM once as an MCP tool so that any compatible agent can use it. Paper2Agent turns a paper's codebase into MCP tools.
  - *Used by:* paper2agent  ·  *Source in the draft:* 3-05e1, 3-03e1

---

# Reconciliation notes

**Merged into term definitions** (were separate concept items before): Attention (quadratic cost) → *Transformer and self-attention*; Added questions (§4.2) → *Decipherment questions*; Data (design element) and the five-element list → *The five design elements* (new concept); Foundation model (term) → *Biological foundation model*; Intrinsic and downstream evaluation → one concept.

**Converted from concept items to examples** (new IDs): `1-10c1` → `1-10e2` (scope), `2.2.1-04c1` → `2.2.1-04e4` (single-cell grammar), `4.3-04c1` → `4.3-04e5` (correlation vs. causation note), `6.2-02c2` → `6.2-02e1` (contents of a boundary statement).

**Split**: 2.1.2-04e1 ("Masked: ESM2. Autoregressive: ProGen2, Evo") → `2.1.2-04e1` (masked) and `2.1.2-04e3` (autoregressive), so each example has one host.

**Dropped as duplicates or site notes**: `1-10e1`: merged into site notes (Supplemental Table S1 reconciliation, see 02); `1-06e3`: duplicate of 3-05e3 (encoder route: ChatNT, CellWhisperer, BioReason); kept once.

**New concepts added to the master list** (and now also listed in `engineer_brief/04`): *The five design elements* (home 2.1.2-01), *Shared literacy* (home 6.3-02).