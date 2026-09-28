---
name: knowledge-write
description: Helper skill for safely applying reconciled scientific claims to Knowledge/ with claim-level provenance, minimal diffs, meaningful wiki links, and source manifests.
slash: false
metadata:
  opencode/autoinvoke: "false"
  opencode/slash: "false"
---

# Knowledge Write

Read `references/write-safety.md`. Read `references/note-format.md` before creating a new note. Only execute decisions already recorded in the reconciliation plan.

## Editing principles

Every `Knowledge/` note must have a complete English block followed by a complete Russian block in the same file. Keep claims, conditions, uncertainty, citations, and meaningful links aligned across both blocks. When updating a monolingual note, preserve its existing content and add a faithful counterpart; when adding or changing a claim, update both versions together. Do not create separate translated notes or introduce facts during translation. Prefer small local edits, preserve human wording and organization, and do not rewrite unrelated prose for style. Do not delete an old claim because the current paper omits it or collapse source-specific results into an unsupported general statement. Re-read every modified note.

## Provenance format

Use a stable source ID, for example `SRC:reisman1955`. For a source-grounded claim, use `[SRC:reisman1955, p. 4]` or `[SRC:reisman1955, pp. 4–5]`.

Each affected note should contain a `Sources` section when needed, mapping the source ID to plain-text bibliographic identity and source path, e.g. `- SRC:reisman1955 — Reisman et al. (1955), "..." — source: Papers/...pdf`.

Do not make the source ID or PDF path a `[[wikilink]]`. This keeps provenance auditable without turning papers into graph hubs.

## Source manifest

Create or update `.research/sources/<source-id>.md` with source ID/path, title, authors, year, DOI if present, ingestion status/date if trustworthy, notes created/updated, claim IDs integrated, and unresolved issues.

## Idempotency and corroborating evidence

Deduplicate claims separately from evidence. Before writing, check whether the same source ID already supports the equivalent claim. If it does, do not duplicate that source's evidence; add any genuinely new detail only.

When a different source supports an existing claim, do not skip it because the proposition or value is already present. Update the existing note with the new source ID and page citation. A new measurement method or evidence domain is worth recording even if it is described in only one sentence (for example, Raman characterization of a structure already discussed through XRD). Keep one concise statement of the shared proposition when conditions are comparable, but preserve distinct source-specific methods, samples, conditions, uncertainty, and interpretations in separately attributed evidence. Add the source to the note's `Sources` mapping and its own manifest. Do not overstate corroboration as consensus or independent replication.

Mirror the evidence addition in both English and Russian blocks, with matching source IDs and page references.

## Final audit

Confirm all new claims are grounded or explicitly marked as inference; numbers retain units/conditions; contradictions remain visible; no duplicate note was introduced; no human content was lost; only `Knowledge/` and `.research/` were modified.
