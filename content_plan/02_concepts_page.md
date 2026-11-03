# 02. Concepts Page

## Purpose

One page holding **every concept** used in the review's argument, each defined once. All concept keywords on the landing page link here. Examples hang under their concept, **folded by default**: a reader first reads the definition, then chooses whether to see examples.

## Layout

- **Default order**: the review's order (by the term's `section`, then by its source claim), so the page reads like a second, deeper pass through the paper.
- **Alternative views**: A–Z index; search box; **filter by review section** (opened by "Terms in this section (n) →" on the landing page); **filter by design element** (opened by the row labels of the five-element beats); filter to a section's evidence examples (opened by "See the evidence →").
- **One entry per term**, with a stable anchor so any link can land on it directly (e.g., `/concepts#masked-language-modeling`).
- **Deep link behavior**: when arriving from a landing-page keyword, scroll to the entry and highlight it briefly. Offer "Back to beat" to return.

## Anatomy of an entry

```
[Term name]                                     [tag: concept | concept + technique]
Short definition (1–3 sentences)
Where in the review →  (link to the home beat on the landing page, or for a section term to the beat of its section; plus other beats that reuse it)
How it's done →        (only if the term also has a technique block; goes to Techniques page)
Related concepts:  link · link

▸ Examples (3)         ← collapsed by default
    ▾ (when opened)
    Example 1 text … [model link] … [ref numbers]  [tag: success | limitation | illustration]
    Example 2 …
    Example 3 …
```

## Rules for definitions

- **Length**: at most 3 sentences. If it needs more, the extra belongs in a technique block or an example.
- **Wording**: written for a biologist who is not an AI specialist, and for an AI researcher who is not a biologist (the review's two audiences).
- **No model descriptions inside definitions.** Mention a model only as a link, and only if needed.
- **Use other concept links** rather than re-explaining them.
- **Define once.** If a term is needed in two places, link; never copy the definition.

## Rules for examples

- **Every example hangs under exactly one term.** (If an example has no natural term, see open decision 1 in `00`: add a small concept rather than orphaning it.)
- **Folded by default.** The count is visible on the fold control (e.g., "Examples (3)"), so readers know what they are opting into.
- **Long lists**: if a term has more than about 5 examples, show the first 3 and put the rest behind "Show more".
- **Each example carries tags**: the models it involves (these become links and feed the Models page), a direction (`success`, `limitation`, `illustration`), and its reference numbers.
- **Models in examples are links only.** The example says what happened; the model's description lives on its own page.
- **Examples are short**: one to three sentences, with the key number or result stated.
- **Grouping by finding**: examples that came from one demoted claim share a one-line `finding` (e.g., "Observed states do not predict interventions"). When several examples share a finding, show the finding as a small subheading above them. Each example also carries a `design_element` tag (data, architecture, training scheme, evaluation, post-analysis), so readers can filter the evidence the way the review organizes it.

## How a term connects to the landing page

After the beats were merged, the landing page no longer writes every term's name. Each term is in one of three states (see `04`, Section 5, and `05`):

- **Linked**: its word appears in a beat and links here. The entry's "Where in the review →" returns to that **home beat**. (37 terms.)
- **Section term**: no beat writes its word. It is listed here in review order and is reached from the landing page through "Terms in this section (n) →", which opens this page filtered to the term's review section. "Where in the review →" returns to the beat that covers that section. (27 terms.)
- **Example-only** (*sampling bias*, *circular annotation*, *systematic variation*): no landing link and no section link; they exist only to host evidence. They are labeled "Evidence concept" on the page and reached from examples, filters, and model pages. (3 terms.)

If a later beat uses a term that is linked elsewhere and the authors want it linked there too, they mark it as reused (see `05`). The entry then lists all beats where it appears under "Where in the review".

## What does not belong on this page

- Descriptions of individual models (→ Models page).
- Step-by-step methods, variants, pitfalls (→ Techniques page; see `04`).
- Anything that is not needed to follow the argument.

## Relation to Supplemental Table S1

The review already has a key-terms table (Supplemental Table S1). The Concepts page should be a **superset**: every S1 term appears here, with identical meaning. Authors should reconcile the two before launch so the paper and the site never disagree.

## Starter content

The full term list (with kind, landing state, source claim, and group) is in `04_techniques_page.md`, Section 5. The definitions and examples, already re-homed so that every example sits under a term, are in `ARBDS_content_rehomed_EN.md`. It is organized by the 72-claim structure; a claim ID maps to its beat through the beat's `covers` list. The 11 demoted claims of §4.2 and §4.3 arrive as examples with suggested host concepts; the table is at the end of `ARBDS_claims_compressed_EN.md`.

## Acceptance checks

1. Every term on the page has exactly one definition and exactly one landing state (linked with a home beat, section term, or example-only).
2. Every example is attached to exactly one term and is collapsed on load.
3. No model is described on this page; every model name is a link that resolves.
4. Every landing-page concept keyword and row link lands on its entry (or on the correctly filtered list), and "Back to beat" returns to the right place.
4b. "Terms in this section (n) →" opens a list of exactly n terms.
5. Terms with a technique block show "How it's done →"; terms without one do not.
