# Cell brief: data.promptugal.news source pages that explain themselves

Opened 2026-11-28T02:3xZ by cl-6.maestro@dinis, from Dinis's review typed in cl-6.data's session (28 Nov), recorded at PrompTugal__Agent__Data dev site/factory/dinis-cruz/account-f/feedback/2026-11-28-status-review.md.

## Wanted, per source page (data.promptugal.news/<source>/)
1. Opens with a rendering of the data held: how much, how many files, a scale, a badge at the right.
2. A back link to /status/.
3. A real explanation of what is wrong, each failed request named (from data/<id>/reads.json: name, url, status, bytes, sha).
4. Provenance: the source's own page first (rendered), then the JSON; where it is stored, how many copies, API addresses with past data, an OpenAPI/Swagger link where one exists.
5. Per-run history linked to the GitHub commits, with what changed between runs (a diff).
6. Every raw JSON visualised, embedded.
7. A view per run, then a meta-analysis across runs or per section.
8. Whether the source needs calling more than twice a day.
Also show both the real collection times (07:03 and 18:03 Lisbon) and the cadence each card claims.

## Roles
- Data files: cl-6.data@PrompTugal.dinis (inside data/**: health and failure explanations, run index with commit links, copy counts).
- Design: cl-6.designer@PrompTugal.dinis.
- Developer: cl-6.dev@PrompTugal.dinis (scripts/build/pages.mjs is gated; cl-6.data cannot change it).
- Review: cl-6.maestro@dinis; Dinis via the page.

## Deliverable
One release of the source pages through the data site's gate, plus cl-6.data's new data files. Start with two sources (one healthy, one failing, e.g. euvd and social), then the rest.
