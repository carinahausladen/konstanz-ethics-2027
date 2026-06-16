# Corpus construction protocol (shared across all four corpora)

*Generalized from the corpus-2 protocol used in the IC2S2 paper. Every group
follows the same rules so the four corpora stay **comparable** — that
comparability is what makes the final cross-corpus paper possible.*

**The goal is not "scrape everything."** It is: build a **defensible, documented**
corpus that lets us compare how the eight philosophical values are translated
across four stakeholders — research, companies, government, and the public.
A second person re-running your steps should rebuild (almost) the same corpus.

---

## 1. Unit of analysis

**One document = one row.** A self-contained, publicly available text artifact
(PDF / HTML / post) with a stable URL that can be snapshotted locally. Each
group defines its document type concretely in its own README (a paper, a policy
instrument, a news article, a forum thread, …).

## 2. Strata — tag every document

Each corpus splits into sub-strata so the analysis can report per-stratum and
flag **divergence** between them as a finding. Use the `stratum` column.
(Corpus 1 strata = the eight themes; corpus 2 = research vs. public-facing;
corpus 3 = supranational / multilateral / national / standards; etc.)

## 3. Inclusion criteria — a document is IN iff ALL four hold

1. **Attribution.** Authored/published by an in-scope source (defined in your
   README's *source frame*). A third-party text merely *about* a source does
   **not** qualify.
2. **Topical relevance.** Its primary subject materially addresses ≥1 of the
   eight toolkit themes (metaethics, preference/welfare, character, fairness,
   pluralism, agency, uncertainty, long-termism).
3. **Accessibility.** Retrievable at a stable URL and snapshot-able. Gated/
   blocked items are recorded with `accessible: false`, never silently dropped.
4. **Time window.** Inside your stated sample window, with a carve-out for one
   **foundational anchor** per source (canonical origin) at any date.

## 4. Exclusion criteria (log every rejection)

Third-party authorship; off-topic capability/product/marketing material;
secondary coverage *about* a source; duplicates (collapse to one canonical
record). Every screened-but-rejected candidate goes to `exclusions.csv` with a
reason code (`third-party` / `off-topic` / `inaccessible` / `out-of-window` /
`duplicate`).

## 5. Source frame (freeze where you look)

Reproducibility requires fixing the search universe. Each README lists the exact
channels/APIs/queries swept. Enlarging the corpus = widening this frame on
purpose and recording the change — not ad-hoc additions.

## 6. The repeatable sweep

1. **Enumerate** candidates per source × channel using defined queries.
2. **Screen** titles/abstracts against §3.2.
3. **Filter** by attribution (§3.1) and accessibility (§3.3).
4. **Dedup** — one work across preprint/blog/journal = one record.
5. **Snapshot** raw → text; record provenance.
6. **Log exclusions** (§4).

## 7. Manifest schema (the shared columns — see `manifest_schema.csv`)

| column | meaning |
|--------|---------|
| `id` | stable identifier (DOI / arXiv id / doc slug) |
| `corpus` | `1-cs` … `4-media` |
| `stratum` | sub-category within the corpus (§2) |
| `type` | paper / report / framework / article / post / … |
| `source` | the institution / outlet / venue / author org |
| `title` | document title |
| `year` | publication year |
| `url` | stable source URL |
| `accessible` | `true` / `false` (gated → false, keep the row) |
| `inclusion_reason` | why it's in — the auditable justification |
| `notes` | dedup notes, substitutions, block type |

Corpus 2 is the **reference implementation**: it carries extra provenance
columns (`anchor`, `arxiv_id`, `sha256`, `authorship_ok`, `local_stem`). Add
those to your corpus when you start snapshotting raw files.

## 8. QA before you call a corpus "done"

- **Attribution audit** on every document (the guardrail that caught a
  mislabeled third-party paper in corpus 2).
- **Inter-coder spot check**: a second person re-applies §3–§4 to a random 20%
  and to *all* borderline calls; resolve against the written rule.
- **Exclusion-log review**: confirm no in-scope statement was dropped as
  "off-topic."

---

### How groups enlarge their corpus week by week

The seed in each folder is a *starting point*, not a finished corpus. Each week,
as a new theme is covered, extend the source frame and re-run the sweep, screen
the new candidates against §3, and log what you reject. The corpus grows with the
syllabus; by the cross-corpus week (W11) each group has a defensible, documented
dataset and a clean exclusion log.
