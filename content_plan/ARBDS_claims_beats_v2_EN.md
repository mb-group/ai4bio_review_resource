# Scroll beats v2: headline + supporting (L1 spine)

Built from `ARBDS_claims_compressed_EN.md` (72 claims). This file is the **landing-page content source**: the engineer's `engineer_brief/` files (00 to 05) refer to it. It supersedes `ARBDS_claims_merged_EN.md` (the earlier 28-beat draft).

**How a beat works** (changes in this revision are listed in Notes)
- **H (headline)**: one sentence, large type, ≤ 20 words. Fills the screen on its own. Reading only the H lines gives the whole argument.
- **S (supporting)**: small type under the headline, ≤ 35 words. Optional for the reader.
- **Rows**: short parallel lines (≤ 12 words each) that appear one at a time as the reader scrolls inside the same beat. They are not separate data items.
- **Links lines** (new): which terms are linked from this beat, by term id, and which terms belong to this beat's section but are not linked in the text (**Section terms**, reached through a "Terms in this section (n) →" link). Prose (H and S) links at most 3 terms (a list of up to 4 is accepted); each row may carry one link.
- **ID rule**: a beat takes the ID of its first source claim. `covers` lists every source claim, so nothing is lost and every item can be traced to the review.

**Total: 26 beats** (measured). Headlines average 17 words (max 20). Headline + supporting + rows average 49 words per beat (earlier 28-beat draft: 61); the longest are the row beats (`4.3-08` at 94 words, `4.1-01` at 78), whose rows appear one at a time. Reading headlines only takes about 2 minutes; reading everything takes about 6.

---

## Abstract

- **A-01** *(covers A-01 to A-04)*
  **H:** AI is reshaping biological research, but it is unclear when to trust it; we call this the knowledge boundary.
  **S:** Five design elements set the boundary. The review gathers evidence on where foundation models succeed or fail, and proposes standard descriptions of model limits for researchers and for agentic systems.
  *Links:* knowledge-boundary · biological-foundation-model · agentic-system

## 1. Introduction

- **1-01** *(covers 1-01 to 1-03)*
  **H:** Computation has moved from processing data to contributing to discovery, and two AI tools extend that shift.
  **S:** Foundation models offer versatility; agentic systems offer accessibility. The field is young, and even experts on each side lack a clear picture of what these models have learned.
  *Section terms (1):* knowledge-extraction

- **1-04** *(covers 1-04 to 1-07)*
  **H:** Foundation models compress data, agents compose tools, and the two are beginning to meet.
  **S:** Each is bounded differently: models by data, architecture, and training objective; agents by their tools and the LLM's documented knowledge. Open question: how should an agent choose the right model and interpret its output?
  *Links:* compression-vs-composability · llm

- **1-08** *(covers 1-08 to 1-10)*
  **H:** What limits broader use is the lack of an explicit account of each model's knowledge boundary.
  **S:** Making it explicit helps researchers decide when to trust a model, and lets agents use foundation models as reliable components. Roadmap: framework → agents → evidence → practical steps.

## 2. Landscape of Biological Foundation Models

- **2.1-01** *(covers 2.1-01, 2.1-02)*
  **H:** A foundation model is trained once on large unlabeled data, then reused for many tasks.
  **S:** Self-supervised learning suits biology, where unlabeled data are abundant and labels are scarce. Reuse comes through probing, fine-tuning, or zero-shot use.
  *Links:* self-supervised-learning · probing · fine-tuning · zero-shot-prediction
  *Section terms (1):* supervised-learning

- **2.1.1-01** *(covers 2.1.1-01 to 2.1.1-05)*
  **H:** Biological models borrow the language of LLMs, but the analogy breaks at every step, and each break foreshadows a boundary.
  **Rows:**
  - Vocabulary / token: DNA has no word boundaries
  - Grammar: the rules are largely unknown
  - Corpus: smaller and more biased than it looks
  - Embedding: unreadable numbers that place similar inputs close
  *Row links:* vocabulary · token · grammar · corpus · embedding
  *Section terms (3):* regulatory-dna · tf-binding-motif · sparse-autoencoder

- **2.1.2-01** *(covers 2.1.2-01 to 2.1.2-06)*
  **H:** Five design elements describe nearly every biological foundation model, and each sets part of its knowledge boundary.
  **Rows:**
  - **Data:** what information goes in, and in what form
  - **Architecture:** how it is processed and stored
  - **Training scheme:** what the model is rewarded to learn
  - **Evaluation scheme:** how the model is judged
  - **Post-analysis:** how a trained model is used
  *Links:* five-design-elements
  *Row links (open Concepts filtered by design element):* data · architecture · training-scheme · evaluation · post-analysis
  *Section terms (10):* generalization · transformer · inductive-bias · masked-language-modeling · autoregressive-modeling · contrastive-learning · intrinsic-vs-downstream-evaluation · transfer-learning · in-silico-perturbation · interpretability-analysis

- **2.2-01** *(covers 2.2-01, 2.2.1-01, 2.2.2-01)*
  **H:** Models differ by what goes in and what comes out, and are foundational mainly within that range.
  **S:** From DNA and protein to cells and tissue, the vocabulary unit grows and the grammar changes. Each output task carries its own limit.
  **Rows:**
  - Representation: serves only the questions its embedding encodes
  - Prediction: predicts only what has been measured
  - Generation: writes only what its vocabulary allows
  *Links:* inputs-vs-outputs
  *Row links:* representation-model · predictive-model · generative-model
  *Section terms (4):* bulk-rna-seq · spatial-transcriptomics · graph-neural-network · perturbation-model

## 3. Where a Foundation Model Enters Agentic Systems

- **3-01** *(covers 3-01 to 3-04)*
  **H:** An agent is not a model: it coordinates an LLM, the user, and tools, and only external components add knowledge.
  **S:** Reasoning models make answers more reliable but add no information. Agents are now assembled quickly, but access to a tool does not teach an agent to use it well.
  *Links:* reasoning-model
  *Section terms (7):* hallucination · rag · function-calling · mcp · skill-files · agent-harness · multi-agent-system

- **3-05** *(covers 3-05, 3-06)*
  **H:** A foundation model can enter an agent in four ways, and each way decides whose knowledge boundary the agent inherits.
  **S:** The routes: tool, text, encoder, verifier. Only the encoder route lets the LLM work with raw data, which matters when the answer lies beyond its textual knowledge.
  *Links:* tool-route · text-route · encoder-route · verifier-route

- **3-07** *(covers 3-07)*
  **H:** Better agents do not move a foundation model's boundary; an agent is only as useful as our understanding of it.
  **S:** More reasoning, reinforcement learning, and packaging neither move the boundary nor tell an agent when to trust the model. Humans stay in the loop.
  *Links:* reinforcement-learning

## 4. Knowledge Boundaries Revealed by Existing Studies

- **4-01** *(covers 4-01, 4-02)*
  **H:** Every model has a knowledge boundary, and for foundation models it is the least characterized.
  **S:** LLM boundaries are rarely visible, but learning biology from data is closer to deciphering an extinct language. Agents add an orchestration boundary that benchmarks cannot yet measure separately.
  *Links:* decipherment-questions · orchestration-boundary

- **4.1-01** *(covers 4.1-01 to 4.1-06)*
  **H:** Each design element sets a different limit, and the limits travel with the model wherever it is reused.
  **Rows:**
  - **Data** sets what can be known
  - **Architecture** sets which relationships can be captured; an interaction longer than the input window cannot be learned
  - **Training scheme** sets what is rewarded; none directly rewards cause and effect
  - **Evaluation** sets what becomes visible
  - **Post-analysis** sets what is accessible; a correct prediction does not show the mechanism was learned
  *Links:* correlation-vs-causation
  *Row links (open Concepts filtered by design element):* data · architecture · training-scheme · evaluation · post-analysis
  *Section terms (1):* cnn

- **4.2-01** *(covers 4.2-01, 4.2-07)*
  **H:** Without labels, foundation models capture real biological patterns, most clearly in proteins, but not the physical mechanisms behind them.
  **S:** From residue chemistry to evolutionary constraint, reusable for variant interpretation and design. Proteins lead because the corpus is largest and the rules are written most directly into sequence.
  *Link: "See the evidence" → Concepts page, §4.2 examples.*

- **4.3-01** *(covers 4.3-01)*
  **H:** When do predictions stay reliable? Independent studies test foundation models against simple baselines.
  **S:** The limits they reveal are organized by design element.
  *Links:* simple-baselines

- **4.3-08** *(covers 4.3-08)*
  **H:** The question shifts from whether models learn biology to what they have learned and where it stops.
  **S:** The boundary has four layers.
  **Rows (one per scroll tick):**
  - **Missing:** observations were never, or rarely, collected
  - **Hard to learn:** the architecture cannot span it, or the objective does not reward it
  - **Hidden or exaggerated:** evaluation hides or inflates what the model can do
  - **Inaccessible:** the knowledge is in the model, out of reach of current analysis
  **Closing line:** Benchmark performance, confidence scores, transferable embeddings, and reliability in application must each be established separately.
  *Link: "See the evidence" → Concepts page, §4.3 examples.*
  *Links:* four-layers

## 5. Open Challenges: A Balanced Assessment

- **5-01** *(covers 5-01, 5.1-01, 5.1-02)*
  **H:** Three broader limitations: how models are evaluated, the bet on one general-purpose model, and the field's early stage.
  **S:** First, evaluation. Independent tests cluster in a few areas and usually probe only one design element; few models report when a query lies outside their boundary.

- **5.1-03** *(covers 5.1-03)*
  **H:** Agents that use foundation models are barely evaluated.
  **S:** Benchmarks test general analysis, not whether the right model is chosen or its output correctly interpreted.

- **5.2-01** *(covers 5.2-01 to 5.2-03)*
  **H:** The bet on one general-purpose model comes from the LLM analogy, but biology is more heterogeneous than language.
  **S:** Scaling laws promise gains from larger models, yet larger protein language models do not consistently predict mutational effects better. The analogy holds only partly; multimodal proposals bridge only subsets.
  *Links:* scaling-laws

- **5.3-01** *(covers 5.3-01 to 5.3-03)*
  **H:** AI for biology is in its infancy, so today's strengths and limits belong to a transient stage.
  **Rows:**
  - **Lens 1, scientific maturity:** most work is still descriptive, consistent with simple baselines repeatedly matching foundation models
  - **Lens 2, evolutionary competition:** the field may still be in an open-niche phase; whether it moves toward specialized, boundary-filling models matters for resources and priorities
  *Row links:* stages-of-biological-science · adaptive-radiation

## 6. Future Directions and Recommendations

- **6.1-01** *(covers 6.1-01, 6.1-02)*
  **H:** No need to wait for one general model: use a portfolio of broad and specialized models, coordinated by agents.
  **S:** Broad models supply transferable embeddings; narrower models are fitted to boundary regions. Agents are well placed to manage the portfolio.

- **6.2-01** *(covers 6.2-01, 6.2-02)*
  **H:** Proposal: release every foundation model with a structured boundary statement, organized by the five design elements.
  **S:** Without it, an agent cannot route correctly, and errors from outside a boundary propagate silently.
  *Links:* boundary-statement

- **6.2-03** *(covers 6.2-03 to 6.2-05)*
  **H:** In machine-readable form, the boundary statement becomes the interface between foundation models and agents.
  **S:** It helps a biologist decide whether to trust a result and an agent whether to call a model, and shows where new data are most needed. Closed experimental loops can extend a boundary with new measurements.
  *Links:* self-driving-lab

- **6.3-01** *(covers 6.3-01 to 6.3-03)*
  **H:** Making boundaries explicit is a community task: shared literacy, and a living registry of each model's boundary.
  **S:** Open science offers precedents. Training should aim at shared literacy, not at making every biologist a model builder. The registry links each model to its boundary statement, independent evaluations, known limitations, and replications.
  *Links:* shared-literacy · model-registry

## 7. Conclusion

- **7-01** *(covers 7-01, 7-02)*
  **H:** Foundation models compress and agents compose; integrating the two depends on making knowledge boundaries explicit.
  **S:** Agents are bounded by what is documented, models by the five design elements. The five elements give a common template, inputs and outputs locate a model, and published evidence shows where boundaries lie.

- **7-03** *(covers 7-03)*
  **H:** Explicit boundaries give biologists a basis for trust, builders a target, and agents the information to select models.
  **S:** As measurement expands, they can become a shared language between AI and biology.

---

# Notes

## Moved out of the scroll (nothing deleted; goes to the Concepts page)

| Detail removed from a beat | Source | Goes to |
|---|---|---|
| Leading architecture adapts widely but generally needs more data | 2.1.2-03 | Concept: Transformer and self-attention |
| Evaluation works at two levels that do not always agree | 2.1.2-05 | Concept: Evaluation scheme |
| Examples of per-data-type design problems (tokenizing DNA, representing expression, aligning modalities) | 2.2.1-01 | Already on Models page; add to Concepts: Token |
| Standards and management layers for tools; multi-agent systems | 3-03, 3-04 | Concepts: new entries for tool standards and multi-agent systems |
| Why the language analogy breaks, in full (shortcut risk, species/tissue/assay bias) | 2.1.1-03, 2.1.1-04 | Concepts: Grammar, Corpus |

## Things to check against the review

1. **The four layers (`4.3-08`).** The claim lists "benchmark performance, confidence scores, transferable embeddings, reliability in application", while the concept entry `four-layers` in `ARBDS_content_rehomed_EN.md` defines the layers as missing / hard to learn / hidden by evaluation / inaccessible. These look like two different lists. I used the concept's definition for the four rows and kept the claim's list as the closing line. Please confirm with the review's own text.
2. **Parallel structure.** The four layers line up with the design elements (missing = data, hard to learn = architecture and training, hidden = evaluation, inaccessible = post-analysis). If the authors agree, `2.1.2-01`, `4.1-01`, and `4.3-08` can share one visual, so the reader sees the same frame three times. This is a suggestion, not something the review states.

## Open design decision

The payoff (`4.3-08`) is beat 16 of 26, about 60% of the way down. Shortening the text does not change that position; it only makes the first 15 beats faster to read. Options: a progress bar with section jumps; or a one-screen "three takeaways" preview after the abstract.

## Changes in this revision (after checking the design files against the beats)

1. **Terms lost their landing links.** The first v2 draft dropped many keywords, so about 35 of the 64 non-evidence concepts no longer appeared in their home claim's text. Fix: **37 concepts are linked from a beat** (see the `Links` lines); the other **27 are "section terms"**, reached through one "Terms in this section (n) →" link on the beat of their section. No concept is lost; the full table is in `04_techniques_page.md`.
2. **Three supporting lines were adjusted** so they carry a keyword that deserves a link: `A-01` (foundation models, agentic systems), `3-05` (names the four routes), `5.2-01` (scaling laws).
3. **"See the evidence" for §4.3 moved from `4.3-01` to `4.3-08`**, back to where the original design had it (after the summary).
4. **No model names appear on the landing page any more.** Headlines state claims; models are reached through concept examples and the Models catalog. If the authors want a few model links on the landing page, the natural places are `4.2-01` (protein models) and `5.2-01` (protein language models).
