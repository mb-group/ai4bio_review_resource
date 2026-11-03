# 05. Data Model and Linking

Everything on the site is generated from structured files. Format (YAML, JSON, a database, a headless CMS) is the engineer's choice; the **fields and rules** below are what matter. The sample at the end uses YAML only for readability.

## 1. IDs

| Item | ID pattern | Example |
|---|---|---|
| Source claim | `{review section}-{nn}` | `2.1.2-04` |
| **Beat** | the ID of its first source claim | `2.1.2-01` |
| Term | lowercase slug | `masked-language-modeling` |
| Example | `{source claim id}e{n}`, assigned to a term | `2.1.2-04e1` |
| Model | lowercase slug | `esm2` |
| Reference | the review's number | `6` |

Claim IDs use the review's own section numbers (Abstract = `A`). Keep both claim IDs and beat IDs stable forever; they are the permanent anchors for deep links. **An old claim ID still works as a link**: the build resolves it to the beat whose `covers` list contains it (`/#2.1.2-04` lands on beat `2.1.2-01`).

## 2. Entities and fields

### Source claim (traceability; not shown on its own)
The 72 claims of `ARBDS_claims_compressed_EN.md` plus the 20 demoted ones (92 in the review's structure). A claim has no text on the landing page of its own; it is kept so that every item can be traced to the review.

| Field | Notes |
|---|---|
| `id` | e.g., `2.1.2-04` |
| `section` | review section, e.g., `2.1.2` |
| `status` | `in_beat` (covered by a beat) \| `demoted` (never rendered on the landing page; its content appears as examples or model-entry text) |
| `beat` | **derived**: the beat whose `covers` contains this claim (empty for demoted claims) |
| `demoted_to` | for demoted claims: where the content went (optional note) |

### Beat (landing page)
| Field | Notes |
|---|---|
| `id` | the first covered claim, e.g., `2.1.2-01` |
| `scene` | the scene it belongs to (default: one of 8 top-level parts) |
| `section` | review section of the first covered claim, shown as the small label (e.g., `2.2`) |
| `order` | position in the scroll (1 to 26) |
| `covers` | list of source claim ids; **every non-demoted claim appears in exactly one beat** |
| `headline` | at most 20 words, with link markup (section 3) |
| `supporting` | optional, at most about 35 words, with link markup |
| `rows` | optional list of `{label, text, link}`; each row at most 12 words; each row has at most one link |
| `closing_line` | optional (`4.3-08`) |
| `figure` | optional, e.g., `Fig2A` |
| `evidence_link` | optional: the review section whose examples "See the evidence →" opens (`4.2-01`, `4.3-08`) |
| `section_terms` | **derived**: the terms with `landing_link: false` whose `section` is one of this beat's covered sections; drives "Terms in this section (n) →" |

### Term (Concepts and/or Techniques)
| Field | Notes |
|---|---|
| `id`, `name`, `aliases` | aliases help search ("MLM") |
| `kind` | `concept` \| `both` \| `technique` |
| `definition` | short, at most 3 sentences, **stored once**, shown on both pages |
| `landing_state` | `linked` (a word in a beat is a link to it) \| `section` (reached through "Terms in this section") \| `example_only` (evidence concepts: no landing link, no section link) |
| `home_beat` | required when `landing_state` is `linked`; the beat whose headline, supporting text, or a row label contains the marker |
| `source_claim` | the claim of the 72-claim structure where the term first appeared (traceability) |
| `section` | review section used to order the Concepts page and to group section terms; derived from `source_claim`, overridable by authors |
| `design_element` | `data` \| `architecture` \| `training_scheme` \| `evaluation` \| `post_analysis`, for the design-element filter; derived from `technique.group` where there is one, assigned by authors otherwise (agent-component terms have none) |
| `reused_in` | other beats that link it (authors decide) |
| `related_terms` | list of term ids |
| `concept` (block, optional) | `why_it_matters` (1 to 2 sentences) |
| `technique` (block, optional) | `group` (data / architecture / training / evaluation / post-analysis / agent), `how_it_works`, `variants`, `pitfalls`, `used_by` (model ids) |
| `source_status` | per block: `from_review` \| `from_references` \| `not_covered` |

Current counts: 67 concepts = 37 `linked` + 27 `section` + 3 `example_only`. The assignment is in `04`, Section 5.

### Example (folded under a term)
| Field | Notes |
|---|---|
| `id` | e.g., `2.1.2-04e1` |
| `term` | **required**, exactly one term id |
| `source_claim` | the original claim ID in the review structure; may be a demoted claim (e.g., `4.3-04`) |
| `landing_claim` | the claim this evidence ultimately supports (e.g., `4.3-08`); the build resolves it to `landing_beat` (via `covers`) for "Where in the review" and "See the evidence" |
| `design_element` | data \| architecture \| training_scheme \| evaluation \| post_analysis (filter on the Concepts page) |
| `finding` | optional one-line finding shared by examples from the same demoted claim; examples with the same `finding` display grouped |
| `text` | 1 to 3 sentences, key result stated, with link markup |
| `models` | model ids involved (feeds the Models page) |
| `direction` | `success` \| `limitation` \| `illustration` |
| `refs` | reference numbers |

### Model (Models page)
| Field | Notes |
|---|---|
| `id`, `name`, `aliases` | |
| `type` | `foundation_model` \| `task_specific` \| `multimodal_llm` \| `agent` \| `resource` |
| `data_types` | DNA, RNA, protein, single-cell, bulk-spatial, multi-omics |
| `tasks` | representation, prediction, generation |
| `description` | one line |
| `configuration.data` | corpus, vocabulary/tokenization |
| `configuration.architecture` | |
| `configuration.training_scheme` | link to term(s) |
| `configuration.evaluation` | |
| `configuration.post_analysis` | |
| `each configuration field` | has `text` and `source_status` (`from_review` \| `from_references` \| `not_covered`) |
| `related_models` | model ids |
| `refs` | reference numbers |

"What it has shown" and "Where its knowledge stops" are **not stored**; they are generated from examples whose `models` include this model, split by `direction`.

### Reference
`number`, `citation`, `doi_or_url` (copied from the review's Literature Cited).

## 3. Link markup inside text

Authors write plain text with simple markers; the build resolves them.

```
{{t:masked-language-modeling}}              → term link, shows the term's name
{{t:masked-language-modeling|masked}}        → term link with custom display text
{{d:training_scheme|Training scheme}}        → design-element link: opens the Concepts page filtered by that element
{{m:esm2}}                                   → model link, shows the model's name
{{m:esm2|ESM2}}                              → model link with custom display text
{{ref:6}}                                    → reference number(s), shown as superscript
```

Two links are **not written by hand**: "Terms in this section (n) →" (computed from `section_terms`) and "See the evidence →" (from the beat's `evidence_link`).

Rules:
- A marker is a **link only**; it never expands in place.
- In a beat's `headline` and `supporting`, link at most about 3 terms (a list such as probing, fine-tuning, zero-shot may carry 4); the build **warns** above 4. Each **row** may carry one link, which does not count toward that limit.
- A term's own definition must not contain a link to itself.
- Model markers may appear in examples, definitions, and technique entries. The landing page currently has none (see `01`).

## 4. What is generated automatically

| Output | Computed from |
|---|---|
| "Mentioned in" on every term and model | all markers pointing at it |
| "Where in the review" on a term | `home_beat` + `reused_in` for linked terms; the beat covering the term's `section` for section terms |
| "Terms in this section (n) →" on a beat | `section_terms` of that beat |
| "What it has shown / Where it stops" on a model | examples with that model, split by `direction` |
| "Used by" on a technique | `technique.used_by`, cross-checked against model `configuration.training_scheme` links |
| Concepts page order | by `section`, then by `source_claim` |
| Design-element filter | `term.design_element` and `example.design_element` |
| Techniques page groups | `technique.group` |
| Landing keyword list for a beat | markers present in `headline`, `supporting`, and `rows` |
| Old claim ID → beat | `covers` |

## 5. Validation (fail the build, or warn, on these)

**Fail**
1. A marker points to a term/model/reference that does not exist.
2. An example has no `term`, or more than one.
3. A term with `landing_state: linked` has no `home_beat`, or its `home_beat` does not contain a marker for the term (in `headline`, `supporting`, or a row).
3a. A term with `landing_state: section` has a `section` that no beat covers (the "Terms in this section" link would have no home).
3b. An `example_only` term has a `home_beat`, or has no examples (it would be empty).
3c. An example's `landing_claim` does not resolve to a beat.
4. A `both` term lacks either block, or a `technique` term lacks the technique block.
5. A model name appears as plain text in a beat, term, or example while a catalog entry exists (should be a marker).
6. Duplicate definitions: the same term defined in two places.
7. **Coverage**: a non-demoted source claim appears in no beat's `covers`, or in more than one. (This is what guarantees that merging beats lost no content.)
8. A beat's `order` values are not exactly 1 to 26 without gaps or repeats.

**Warn**
1. More than 4 term links in the prose (headline plus supporting) of one beat.
2. A headline over 20 words, supporting text over about 35 words, or a row over 12 words.
3. A model entry has a configuration field with no `source_status`.
4. A term with no examples and no technique block (fine for some, worth a look).
5. A claim ID whose section does not exist in the review's heading list.
6. A `section` term whose beat has more than about 10 section terms (the "Terms in this section" list is getting long).

## 6. Worked sample: beat `2.1.2-01` through every page

The beat replaces the old claim `2.1.2-04`. *Masked language modeling* is a **section term** here: no beat writes its name, so the reader reaches it from the "Training scheme" row or from "Terms in this section (10)".

```yaml
beat:
  id: 2.1.2-01
  scene: s2
  section: "2.1.2"
  order: 7
  covers: [2.1.2-01, 2.1.2-02, 2.1.2-03, 2.1.2-04, 2.1.2-05, 2.1.2-06]
  headline: >
    {{t:five-design-elements|Five design elements}} describe nearly every
    biological foundation model, and each sets part of its knowledge boundary.
  rows:
    - label: "Data"
      text: "what information goes in, and in what form"
      link: "{{d:data|Data}}"
    - label: "Architecture"
      text: "how it is processed and stored"
      link: "{{d:architecture|Architecture}}"
    - label: "Training scheme"
      text: "what the model is rewarded to learn"
      link: "{{d:training_scheme|Training scheme}}"
    - label: "Evaluation scheme"
      text: "how the model is judged"
      link: "{{d:evaluation|Evaluation scheme}}"
    - label: "Post-analysis"
      text: "how a trained model is used"
      link: "{{d:post_analysis|Post-analysis}}"
  figure: Fig2A
  # section_terms (derived, 10): generalization, transformer, inductive-bias,
  # masked-language-modeling, autoregressive-modeling, contrastive-learning,
  # intrinsic-vs-downstream-evaluation, transfer-learning, in-silico-perturbation,
  # interpretability-analysis

terms:
  - id: masked-language-modeling
    name: Masked language modeling
    aliases: [MLM, masked prediction]
    kind: both
    definition: >
      A training approach in which randomly hidden tokens are predicted from the
      surrounding sequence.
    landing_state: section
    source_claim: 2.1.2-04
    section: "2.1.2"
    design_element: training_scheme
    related_terms: [autoregressive-modeling, self-supervised-learning]
    concept:
      why_it_matters: >
        What a model is rewarded for sets what it is good at; this objective
        rewards filling in what occurs together, not what causes what.
    technique:
      group: training
      how_it_works: "Randomly hidden amino acids are predicted from the surrounding sequence. (Further detail: authors to extend from the references.)"
      used_by: [esm2]
      source_status: from_review

examples:
  - id: 2.1.2-04e1
    term: masked-language-modeling
    source_claim: 2.1.2-04
    landing_claim: 2.1.2-04        # resolves to landing_beat 2.1.2-01
    design_element: training_scheme
    text: "{{m:esm2}} is trained by masked language modeling: hidden amino acids are predicted from the surrounding sequence {{ref:38}}."
    models: [esm2]
    direction: illustration
    refs: [38]

models:
  - id: esm2
    name: ESM2
    type: foundation_model
    data_types: [protein]
    tasks: [representation, prediction]
    description: Protein language model trained on UniRef sequences.
    configuration:
      data:
        text: "UniRef protein sequences; each amino acid is a token (20-letter vocabulary)."
        source_status: from_review
      training_scheme:
        text: "{{t:masked-language-modeling}}"
        source_status: from_review
      # architecture, evaluation, post_analysis filled likewise, or "not_covered"
```

What the reader gets from this data, with no extra writing:
- Landing: the beat, its headline link to *The five design elements*, five row links, and "Terms in this section (10) →".
- Concepts page: opened from the "Training scheme" row, a list filtered to that design element; opened from "Terms in this section", a list of the 10 terms of §2.1.2. Either way the *Masked language modeling* entry shows its definition, "Where in the review →" (back to beat `2.1.2-01`), the folded example `2.1.2-04e1`, and "How it's done →".
- Techniques page: the same term under *Training scheme*, with "Used by: ESM2".
- Models page: ESM2's entry, whose training scheme links back to the term, and whose "Mentioned in" lists the example `2.1.2-04e1` (no beat names ESM2).

## 7. Build recommendations (suggestions, engineer decides)

- **A static site generated from the data files** fits this scope: no accounts, no user submissions, content changes only when the authors change it. Hosting stays cheap and long-lived.
- **Keep content in files under version control**, so the authors can review changes as text.
- **Client-side search** over the generated index is sufficient (term names, aliases, model names).
- **Do not hard-code text in page templates.** If a sentence appears on a page, it came from a field above.
- **Check word limits in the build** (headline, supporting, rows): they protect the pacing the authors chose.
- **Out of scope for now**: community submissions and a live model registry (the review's §6.3 idea). The data model above is deliberately compatible with adding them later.
