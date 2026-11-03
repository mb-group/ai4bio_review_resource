# 00. Site Overview (read this first)

**Project**: online resource for the review *AI for Biologists: The Knowledge Boundaries of Foundation Models in the Age of Agentic Systems*.

## 1. The idea in one paragraph

The review makes 72 main claims (after compression; see `ARBDS_claims_compressed_EN.md`). For the scrolling story, these are merged into **26 beats**, one scroll step each, written as a short headline plus optional supporting text (see `ARBDS_claims_beats_v2_EN.md`). Each beat leans on terms that need defining, and each term is illustrated by models and studies. If all of that sits on one page, readers drown. So we split it: **one clean scrolling story (the beats only)**, and **three reference pages** that hold everything else. Readers follow the story, and only click out when they want to know what a word means, what a model is, or how a method is done.

## 2. Site map

```
LANDING PAGE (scrollytelling)         the review's argument; 26 beats in 8 scenes
   │   keywords are links, nothing expands in place
   ├──► CONCEPTS page                 every concept, defined once; examples folded under each
   ├──► MODELS page (catalog)         one entry per model; its configuration and evidence
   └──► TECHNIQUES page               "how it is done" entries, for people who implement

CONCEPTS  ⇄  TECHNIQUES               the same term seen at two depths (see 04)
anything  →  MODELS                   every model name, anywhere, is a link
```

## 3. What each page is for

| Page | Main reader | Answers the question | Contains | Deliberately does not contain |
|---|---|---|---|---|
| Landing | Everyone | "What is the argument?" | Beats in the review's order (headline, supporting text, rows); figure anchors; keyword links | Definitions, examples, model descriptions, method detail |
| Concepts | PIs, any reader following the argument | "What does this term mean, and why does it matter here?" | Short definitions; folded examples under each concept; filters by review section and by design element | Model descriptions (link instead); step-by-step method detail (link to Techniques) |
| Models | Everyone who meets a model name | "What is this model and where does it work or fail?" | One entry per model, organized by the review's five design elements | Concept definitions (link instead) |
| Techniques | Staff/trainees who build or apply things | "How is this done, what are the variants, what are the pitfalls?" | Method-level entries, grouped by design element | Argument-level framing (link back to Concepts) |

## 4. Design principles

1. **Landing = spine only.** If it is not part of the argument, it is not on the landing page.
2. **Headline first.** Every beat has a one-sentence headline. Reading only the headlines gives the whole argument (about 2 minutes); supporting text and rows are for readers who want more (about 6 minutes in all).
3. **One home for every explanation.** A term is defined in exactly one place. Everywhere else only links.
4. **Links, not repeats.** A model name is a link to the Models page; it is never described inline. A concept word is a link to the Concepts page.
5. **Progressive disclosure.** Depth increases only when the reader asks: beat → concept → example (folded) → technique.
6. **Content is data, not HTML.** Beats, terms, examples, models live in structured files; pages are generated from them. Pages never hold hand-copied text.
7. **IDs follow the review's own numbering** (e.g., `2.1.2-04`), so every item can be traced to the paper. A beat takes the ID of its first source claim; old claim IDs still resolve to their beat.
8. **Every link has a way back.** From any destination, the reader can return to the exact beat they came from.
9. **Merging must not lose content.** Every one of the 72 compressed claims appears in exactly one beat's `covers` list; the build checks this.

## 5. The kinds of content

| Entity | What it is | Lives on | Example |
|---|---|---|---|
| **Beat** | One scroll step of the argument: headline, optional supporting text, optional rows | Landing | "Five design elements describe nearly every biological foundation model, and each sets part of its knowledge boundary." (`2.1.2-01`) |
| **Source claim** | One of the 72 compressed claims (plus 20 demoted); kept for traceability, covered by a beat | Data only | `2.1.2-04` ("Training scheme determines what the model is rewarded to learn.") |
| **Term** | A concept, a technique, or both (one record, two views, see 04) | Concepts and/or Techniques | Masked language modeling |
| **Example** | A specific piece of evidence or illustration, hanging under a term | Concepts (folded) | "ESM2 predicts hidden amino acids from the surrounding sequence" |
| **Model** | A named model, agent, or resource | Models | ESM2 |
| **Reference** | A citation from the review's Literature Cited | Attached to examples and models | Lin et al. 2023 |

Detailed fields: see `05_data_and_linking.md`.

## 6. Link rules

| From → To | Concepts | Techniques | Models | Landing |
|---|---|---|---|---|
| **Landing** | Concept keyword in a beat; row label; "Terms in this section (n) →"; "See the evidence →" | Only for technique-only words (rare) | Model name in a beat (currently none) | n/a |
| **Concepts** | Another concept inside a definition | "How it's done →" (only if the term has a technique block) | Model name in a definition or example | "Where in the review →" (jumps to the beat) |
| **Techniques** | "What it means →" | Related technique | "Used by" list; model name in text | "Mentioned in" (beats) |
| **Models** | Concept term in the entry | Technique term in the entry | Related model | "Mentioned in" (examples; beats if any) |

Two automatic features follow from the data (no hand-writing):
- **Backlinks**: every term and model page shows "Mentioned in" (which beats and examples).
- **Aggregation**: each model page lists every example tagged with that model, so evidence is written once under a concept but also visible per model.

## 7. Two kinds of readers (this drives the Concepts/Techniques split)

| Reader | Needs | Stops at |
|---|---|---|
| PI / senior reader | To follow the argument and judge it | Concepts |
| Staff / trainee who will use or build | To choose, implement, and evaluate methods | Techniques |

## 8. One walk-through

A reader is on beat **2.1.2-01** ("Five design elements describe nearly every biological foundation model, and each sets part of its knowledge boundary"):
1. The beat shows its headline, then five rows that appear one by one (Data, Architecture, Training scheme, Evaluation scheme, Post-analysis). The words *Five design elements* are a link, each row label is a link, and a small link at the bottom reads "Terms in this section (10) →". Nothing else.
2. They click the **Training scheme** row → **Concepts page**, filtered to the training-scheme design element. *Masked language modeling* is one of the entries: a 2 to 3 sentence definition, "Where in the review →", and a collapsed "Examples (n)".
3. They open the examples (or not). Example text mentions ESM2 as a link.
4. A staff member clicks "How it's done →" → **Techniques page**, same term: the same short definition, plus how it works, variants, pitfalls, and "Used by" models.
5. They click ESM2 → **Models page**: ESM2's data, architecture, training scheme, evaluation, post-analysis, what it has shown, where its knowledge stops.
6. "Back to beat 2.1.2-01" returns them to where they were.

(The reader could also have opened "Terms in this section (10) →" and found the same term in the list of §2.1.2 terms.)

## 9. Who does what

| Role | Responsibility |
|---|---|
| **Authors** | Final wording of beats (headline, supporting text, rows) and claims; concept definitions; deciding concept vs. technique; deciding which terms are linked from a beat and which are section terms; assigning a design element to concept-only terms; tagging examples; checking model entries against the paper |
| **Software engineer** | Data format and validation (including the coverage and word-limit checks); build of all four page types; linking, backlinks, and filters; hosting and long-term maintenance |
| **Front-end / scrollytelling designer** (may be the same person) | Scroll behavior, rows revealed one at a time, figure anchors, visual identity of the link types |
| **Content curators** (authors or trainees) | Filling model and technique entries from the review and its references |

## 10. Open decisions for the authors (not for the engineer)

1. **Evidence-type examples with no natural concept (partly resolved by the compression).** The 11 claims demoted from §4.2 and §4.3 now become folded examples, each with a suggested host concept (table at the end of `ARBDS_claims_compressed_EN.md`). Three small new concepts are needed: *sampling bias*, *circular annotation*, *systematic variation*. Because they appear only inside examples, they are `example_only` (no landing link; see `05`). The re-homing of all examples is done in `ARBDS_content_rehomed_EN.md`.
   **Path from story to evidence**: "See the evidence →" on `4.2-01` and `4.3-08` opens the Concepts page filtered to that section's examples (see `01`).
2. **Databases and benchmarks** (UniRef, PDB, ProteinGym, CASP, BixBench...). **Recommendation**: include them in the Models catalog as a "Resource" type, so they get links without a fifth page.
3. **Scroll length and scenes.** 26 beats. **Default**: 8 scenes, one per top-level part (Abstract, §1 to §7); beats appear one by one within a scene, and rows appear one by one within a beat. The earlier design had 19 scenes; the authors may keep sub-section scenes instead (see `01`).
4. **Concept/technique single record.** **Recommendation**: one record per term with optional concept and technique blocks (see `04`), rather than two separate records.
5. **Reconcile with Supplemental Table S1** (the review's key-term table): the Concepts page should be a superset of it.
6. **Which terms are linked from the story (new).** After merging, 37 concepts are linked from a beat and 27 are "section terms" reached through one link per section (the assignment is in `04`, Section 5). The authors should review it: a section term the authors consider essential can be promoted by writing its word into a headline or supporting line.
7. **The four layers of the boundary (new).** The claim text lists "benchmark performance, confidence scores, transferable embeddings, reliability in application", while the concept entry defines them as missing / hard to learn / hidden by evaluation / inaccessible. Beat `4.3-08` uses the concept's four as rows and keeps the claim's list as a closing line. Confirm against the review.
8. **Rows versus Figure 2A (new).** `2.1.2-01` and `4.1-01` have five rows that restate the five design elements, as does Figure 2A. Decide whether the rows are the text layer of the figure or sit beside it.
9. **Model names on the landing page (new).** The beats contain no model names, so the landing page has no model links. Readers reach models through concept examples and the Models catalog (which needs a top-level navigation entry). If a few model links are wanted on the landing page, `4.2-01` and `5.2-01` are the natural places.
10. **Position of the main finding (new).** The four layers (`4.3-08`) are beat 16 of 26, about 60% of the way down. Options: a progress bar with section jumps, a "Headlines only" switch, or a one-screen preview of three takeaways after the abstract.

## 11. Files

| File | Content |
|---|---|
| `00_overview.md` | This file |
| `01_landing_page.md` | Scrollytelling landing page |
| `02_concepts_page.md` | Concepts page and folded examples |
| `03_models_page.md` | Model catalog |
| `04_techniques_page.md` | Techniques page, the concept/technique rule, and the full term list with landing status |
| `05_data_and_linking.md` | Data fields, link markup, validation rules, a worked sample |

**Content source for the landing page**: `ARBDS_claims_beats_v2_EN.md` (26 beats; each lists the source claims it covers and the terms it links). It supersedes `ARBDS_claims_merged_EN.md`.
**Content source for the 72 claims**: `ARBDS_claims_compressed_EN.md` (its last section lists the 20 demoted claims and where each one goes).
**Content source for concepts, examples, and technique-only entries**: `ARBDS_content_rehomed_EN.md` (72 claims, 67 concepts, 149 examples, 17 technique-only entries; every example sits under exactly one concept). It is organized by the 72-claim structure; claim IDs map to beats through each beat's `covers` list, so it does not need to be rewritten. It supersedes `ARBDS_scrollytelling_3layer_EN.md` and `ARBDS_claims_only_EN.md`, which are kept only for reference.
