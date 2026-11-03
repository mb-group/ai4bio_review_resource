# 01. Landing Page (scrollytelling)

## Purpose

The landing page tells the review's argument, and only the argument. It must be readable top to bottom without ever clicking anything. Everything else is reachable by links.

## Content

- **Items**: **26 beats**, defined in `ARBDS_claims_beats_v2_EN.md`, in the review's order. A beat is one scroll step. The 72 compressed claims in `ARBDS_claims_compressed_EN.md` are all still present, merged into beats; each beat lists the source claims it `covers`. The 20 demoted claims do not appear on the landing page.
- **Scenes**: the default is **8 scenes**, one per top-level part of the review: Abstract, §1, §2, §3, §4, §5, §6, §7. A scene keeps its visual in place while its beats scroll past. A beat may swap the visual when it has a figure of its own (see Figures). *Open decision for the authors*: use these 8 scenes, or keep sub-section scenes (the earlier design had 19). The data model supports either.
- **Section label**: every beat shows the review section of its first source claim in small type (e.g., `§2.2`). A beat that merges several sub-sections shows the first one; the full list is in `covers` and can be shown on hover or in the "Where in the review" view.
- **Navigation**: a progress indicator and a jump menu listing the scenes by their review headings. *Optional*: a "Headlines only" switch that hides supporting text and rows, giving the whole argument in about 2 minutes (the full read is about 6).

## What a beat shows

A beat has three layers, all authored in the beats file:

| Layer | Look | Rule |
|---|---|---|
| **Headline (H)** | Large type, fills the screen | One sentence, at most 20 words. Reading only the headlines gives the whole argument |
| **Supporting (S)** | Small type under the headline | At most about 35 words; optional for the reader |
| **Rows** | Short parallel lines (at most 12 words each) | Appear one at a time as the reader scrolls inside the same beat; not separate scroll steps and not separate data items |

Some beats also have a **closing line** (`4.3-08`) and a **"See the evidence" link** (`4.2-01`, `4.3-08`).

| Shown | Not shown |
|---|---|
| Headline, supporting text, rows | Definitions |
| Small review-section label | Examples or evidence |
| Keywords as links (see below) | Model descriptions |
| The beat's figure, if the review has one | Method details |

## Links: links only, no preview

Per the design decision, **nothing expands in place**. No tooltip, no popover, no hover card. Every link opens its destination.

| Link type | Where it appears | Destination | Looks like |
|---|---|---|---|
| **Concept keyword** | A word in H or S | Concepts page, scrolled to that term | Subtle underline |
| **Row link** | The label of a row | A concept entry, or (for the five design-element rows in `2.1.2-01` and `4.1-01`) the Concepts page filtered by that design element | Subtle underline |
| **Terms in this section (n) →** | Bottom of a beat, only where the beat's section has concepts not linked in the text | Concepts page filtered to that review section | A small plain link, visibly different from keywords |
| **See the evidence →** | `4.2-01` and `4.3-08` only | Concepts page filtered to the section's examples | A small plain link |
| **Technique-only word** | Rare | Techniques page | Same as concept style |
| **Model name** | Currently none on the landing page | Models page, that model's entry | A visibly different treatment (chip or other underline) |

Rules:
- **Link density**: in H and S, link **at most 3 concepts per beat** (a list such as "probing, fine-tuning, zero-shot" may carry up to 4). Each row may carry **one** link. Over-linking recreates the overwhelm we are avoiding.
- **Which words are linked** is decided by the data: the beat's `Links` and `Row links` lines in the beats file. Do not auto-link every occurrence.
- **37 concepts are linked from a beat; 27 are "section terms"**: they belong to a section, appear on the Concepts page in review order, and are reached through "Terms in this section (n) →". The full assignment is in `04`. The 3 evidence-only concepts have no landing link at all.
- **Return path (important)**: after following a link, "back" must return the reader to the exact scroll position and beat. Either open destinations in a new tab, or preserve scroll state when returning. Do not reset the scroll to the top.
- **Old claim IDs still work**: a link to `/#2.1.2-04` must land on the beat that covers it (`2.1.2-01`).

## "See the evidence" (pending decision)

The compression folded 11 evidence claims of §4.2 and §4.3 into examples on the Concepts page. To keep a path from the story to that evidence, two beats carry one extra plain link, **"See the evidence →"**, which opens the Concepts page filtered to that section's examples:
- `4.2-01` → §4.2 examples
- `4.3-08` → §4.3 examples (placed after the four layers, where the reader has the summary and wants the proof)

It is a link only. If the authors decide against it, readers still reach the evidence through keywords such as *simple baselines* and *correlation vs. causation*.

## Figures (visual anchors)

Only the review's existing figures are anchored. Other beats use a plain layout.

| Beat(s) | Figure |
|---|---|
| `1-01`, `1-04`, `1-08` (§1) | Figure 1 (A: complementary roles; B: compression vs. composability, correlation vs. causation; C: crude-oil analogy). Authors assign panels to beats |
| `2.1.2-01` | Figure 2A (five design elements) |
| `2.2-01` | Figure 2B (data × task grid), Figure 2C (model hierarchy) |
| `3-01` | Figure 3A (agent design elements) |
| `5.3-01` | Figure 3B and 3C (evolutionary analogy) |
| `6.1-01` | Figure 3C again |

*Open decision*: `2.1.2-01` and `4.1-01` have five-row structures that say the same thing as Figure 2A in text. Either the rows are the text layer of the figure (the five rows appear as the figure's five parts light up), or the figure is shown beside them. The authors and the designer choose; the data does not change. The four rows of `4.3-08` can use the same visual treatment, so the reader meets one frame three times.

Whether the figures become interactive is a separate design decision and does not change this structure.

## Responsive behavior

- On small screens, the sticky visual collapses above the beat text.
- Rows stack under the headline and still appear one at a time.
- Hover-only behavior is never required (there is none), so mobile needs no special handling for links.

## Acceptance checks

1. Reading only the landing page, with no clicks, tells the whole argument in the review's order. Reading only the headlines tells it in outline.
2. No definition, example, or model description appears on the landing page.
3. Every linked keyword and every row link resolves to an existing Concepts/Models/Techniques entry (no dead links).
4. After clicking any link and returning, the reader is at the same beat.
5. Every beat's section label matches the section of its first covered claim (`2.2-01` is labeled `§2.2`).
6. The page contains exactly the 26 beats in the beats file. Every one of the 72 compressed claims appears in exactly one beat's `covers`; demoted claims never render here.
7. Every headline is at most 20 words; every beat's prose links at most 3 concepts (4 for a list).
8. "Terms in this section (n) →" appears on exactly the beats that have section terms, and n matches the number of concepts it opens.
