# 03. Models Page (catalog)

## Purpose

One page for **every model named in the review**. Wherever a model name appears (a beat, a concept, an example, a technique), it is only a link here. A model's description, configuration, and track record live here and nowhere else.

## How readers reach this page

The landing page's beats currently contain no model names, so readers do not arrive here from the story. They arrive from model names inside concept examples, from "Used by" lists on the Techniques page, and from a **top-level navigation entry for the catalog**, which the site needs. (If the authors add model links to the landing page, the natural places are beats `4.2-01` and `5.2-01`.)

## Layout

- **Catalog view**: a filterable, searchable list (cards or table). One row/card per model.
- **Detail view**: one dedicated URL per model (e.g., `/models/esm2`), so any model can be linked directly.
- **Filters**:
  - Type: foundation model · task-specific model · multimodal LLM · agent · resource (see decision below)
  - Data type: DNA · RNA · protein · single-cell · bulk & spatial · multi-omics
  - Task: representation · prediction · generation
  - Technique used (e.g., masked language modeling, contrastive learning)

## Group introductions (carry the demoted §2.2 content)

The review's "tour" of data types (§2.2.1) and tasks (§2.2.2) is no longer in the scroll; it lives here. The catalog is grouped by data type and by task, and **each group opens with a one-line takeaway** taken from the demoted claims:

| Group | One-line takeaway comes from |
|---|---|
| DNA | 2.2.1-02 (how to define a token) |
| RNA | 2.2.1-03 (a model built for non-coding RNA need not capture what governs mRNA function) |
| Single-cell | 2.2.1-04 (representing expression levels; fixed gene vocabulary) |
| Bulk and spatial | 2.2.1-05 |
| Protein | 2.2.1-06 (vocabulary is settled, so innovation moves to other elements) |
| Multi-omics | 2.2.1-07 (no shared vocabulary; models take different routes to align modalities) |
| Representation / Prediction / Generation | 2.2.2-02, 2.2.2-03, 2.2.2-04 |

These intros are stored as group-level text in the data (a `group_intro` field), not typed into the template. Model-level detail goes into each model's *Data* and *Training scheme* fields.

## A model entry mirrors the review's own framework

"Configuration" means the **five design elements**. The entry is organized by them, because that is the review's central framework and it makes every entry comparable.

```
[Model name]   [type]  [data type]  [task]   (year, key reference)
One-line description

CONFIGURATION (the five design elements)
  Data               corpus, tokenization/vocabulary
  Architecture       what it is, context length where relevant
  Training scheme    objective   → links to Techniques
  Evaluation         how the original paper evaluated; independent evaluations if the review cites any
  Post-analysis      how it has been used (probing, fine-tuning, zero-shot, in silico perturbation, interpretability)

WHAT IT HAS SHOWN         bullets; each links to its example
WHERE ITS KNOWLEDGE STOPS bullets; each links to its example
RELATED MODELS            links
MENTIONED IN              (automatic) examples, concepts, techniques, and beats if any
REFERENCES
```

Why this matters beyond the website: the review's main recommendation (§6.2) is a **structured boundary statement** per model, organized by these same five elements. This entry layout is effectively a prototype of that statement. **Design the fields once, cleanly, and keep them machine-readable** (see `05`); this will be the part of the site most worth reusing.

## Rules for entries

1. **Source discipline.** Fill each field only from the review and the references it cites. If the review does not cover a field for that model, show "Not covered in the review" rather than filling it from memory. Each field records where it came from.
2. **Evidence is not written twice.** "What it has shown" and "Where its knowledge stops" are **generated** from examples tagged with the model (the examples live under concepts). Curators tag; they do not retype.
3. **Technique and concept words inside entries are links** to the Techniques and Concepts pages.
4. **No argument in model entries.** They describe; the beats interpret.

## Inventory (all names appearing in the review text)

All of these get an entry. Suggested phasing: Phase 1 = models; Phase 2 = agents and multimodal LLMs; Phase 3 = resources.

**Protein**: ESM2 (including ESMFold) · ESM3 · ProtTrans · SaProt · ProGen · ProGen2 · Ankh
**DNA**: Nucleotide Transformer · DNABERT-2 · GROVER · HyenaDNA · Caduceus · Evo · Evo 2 · GPN-MSA
**RNA**: RNA-FM · RiNALMo · Orthrus · CodonTransformer · gRNAde · regLM
**Single-cell**: Geneformer · scGPT · UCE · scBERT · SCimilarity · GenePT
**Bulk and spatial**: BulkFormer · Nicheformer · VirTues
**Multi-omics**: GeneCompass · PINNACLE · AIDO
**Sequence-to-function**: Enformer · Borzoi · Scooby · AlphaGenome · ChromBPNet
**Structure**: AlphaFold (AlphaFold 2, AlphaFold 3) · AlphaFold-Multimer
**Variant effect**: EVE · AlphaMissense · popEVE
**Perturbation / virtual cell**: CellOT · GEARS · State
**Multimodal LLMs (encoder route)**: ChatNT · CellWhisperer · BioReason · BioReason-Pro
**Agents and agentic systems**: Biomni · Virtual Biotech · Paper2Agent · Virtual Lab · AI co-scientist · Robin · GeneAgent · rbio1 (verifier route)
**Resources (decision pending, recommended to include)**:
- Databases: UniRef · UniProt · Protein Data Bank · CZ CELLxGENE Discover · Kipoi
- Benchmarks and assessments: ProteinGym · CASP · CAGI · BixBench · Virtual Cell Challenge
- Software: Rosetta

**Not catalogued** (general-purpose LLMs mentioned only for comparison; stay as plain text): Llama 3, ChatGPT, Claude.

Agents that the review cites only by reference number (e.g., CellVoyager, TxAgent, and the chemistry and gene-editing agents) can be added by reading the Literature Cited list.

## Acceptance checks

1. Every model name anywhere on the site is a link that resolves to an entry.
2. Every entry has all five configuration fields, either filled with a source or marked "Not covered in the review".
3. "What it has shown / Where it stops" are generated from tagged examples, not typed in.
4. Filters work, and each model has its own stable URL.
5. Each entry's "Mentioned in" list is automatic and complete.
6. The catalog is reachable from the main navigation, not only through links.
