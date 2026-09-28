---
name: knowledge-refactor
description: Restructure existing scientific knowledge notes when the user explicitly asks to split, reorganize, or repair note granularity while preserving evidence, bilingual content, and links.
slash: true
metadata:
  opencode/autoinvoke: "false"
---

# Knowledge Refactor

Use only when the user explicitly asks to restructure existing `Knowledge/` notes, or asks to apply specific note-granularity findings from a lint report. Do not refactor the vault automatically during paper ingestion or ordinary linting.

Read `references/refactor-safety.md` before changing notes. Read the applicable `knowledge-write` note-format and provenance guidance as well.

## 1. Resolve scope and inspect

- Identify the exact target notes from the user's request. If the scope is clear, proceed without asking for confirmation.
- Read each target note fully. Search for aliases, related notes, inbound links, source IDs, and relevant source manifests.
- If a claim's provenance or meaning is unclear, inspect the cited source pages with OpenCode's built-in PDF `read`; use `pdf_pages` as a focused fallback.
- Do not use model memory to fill gaps or add new scientific claims.

## 2. Plan the new structure

Before editing, record a compact plan in `.research/work/` containing:
- the current note and proposed destination notes;
- the scientific boundary and why each resulting note answers a distinct reusable question;
- which claims and citations move, remain, or are summarized in an overview;
- the links to add or update;
- any unresolved evidence or identity questions.

Split by durable scientific topic, not by paper or heading. A material can warrant separate notes for phase behavior, local structure, mechanisms, measurement methods, or other independently useful topics when the evidence supports them. Do not split a section that would become a trivial or unsupported page.

## 3. Apply the refactor

- Create or update notes according to the bilingual format: complete English block first, then a semantically matching Russian block in the same file.
- Move claims with their exact source IDs and page provenance. Preserve quantitative conditions, source-specific distinctions, author interpretations, uncertainty, and contradictions.
- Do not invent, generalize, or silently drop claims during translation or reorganization.
- Keep the original note as a concise overview when it adds value; summarize with citations and link to the focused notes. If it would be empty or redundant, preserve its useful content in the focused notes and update links rather than retaining a hollow hub.
- Add only meaningful `[[wikilinks]]`. Update relevant existing backlinks when their target or scope changes. Do not link source PDFs or manifests.
- Preserve human-written content and unrelated note structure. Do not modify `Papers/` or delete notes automatically.

## 4. Audit

Re-read every created or modified note and verify:
- every original substantive claim is preserved or intentionally summarized with provenance;
- every citation retains the correct source ID and page numbers;
- English and Russian blocks match in claims, conditions, uncertainty, and links;
- links resolve and the resulting notes are not duplicates or trivial fragments;
- contradictions remain visible and no unrequested sources were added.

Report the old-to-new note mapping, links changed, preserved uncertainty, and any claims left in place because their scope or evidence was unclear.
