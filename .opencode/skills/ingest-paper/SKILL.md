---
name: ingest-paper
description: Integrate one scientific paper from Papers/ into the concept-centered Knowledge/ base with provenance, deduplication, contradiction handling, and safe incremental edits.
slash: true
metadata:
  opencode/autoinvoke: "false"
---

# Ingest Paper

Use this skill when the user asks to ingest, process, integrate, or add a scientific paper to the knowledge base.

Do not reduce the task to a paper summary.

## Required helper skills

Load these helper skills in this order as their phase begins:

1. `paper-extract`
2. `knowledge-reconcile`
3. `knowledge-write`

Do not skip a phase.

## 1. Resolve the source

Locate the requested source inside `Papers/`.

- If the user gave an exact path, use it.
- If they gave a title, author, year, or partial filename, search only `Papers/`.
- If more than one plausible source remains, ask which one.
- Do not modify the source file.

Before starting, check `.research/sources/` for an existing manifest that appears to describe the same paper by DOI, exact title, or source path.

## 2. Create or resume compact working state

Use `.research/work/<source-id>.md`.

The work file is a compact state store, not a copy of the paper. It should contain source path, bibliographic identity found so far, extraction progress, compact claims with page provenance, reconciliation decisions, and pending uncertainties.

If a work file already exists, inspect it before restarting.

## 3. Extract

Load `paper-extract` and follow it. Read the original PDF with OpenCode’s built-in `read` first, allowing its PDF handling to inspect the document as a whole. Preserve page provenance; extract only substantive knowledge; keep raw source text out of persistent working state. Use `pdf_pages` only if built-in PDF reading is unavailable or a focused text range is needed.

## 4. Reconcile

After extraction is complete enough to understand the source, load `knowledge-reconcile`.

For every useful claim, determine whether it is already represented, adds detail to an existing note, contradicts existing evidence, belongs as a relationship/link, justifies a genuinely new note, or should be discarded as mention-only/redundant/too weak.

Write the reconciliation plan into the work file before changing `Knowledge/`.

## 5. Write

Load `knowledge-write`. Apply only the reconciled changes. Create or update `.research/sources/<source-id>.md`. The source manifest is machine/audit state and must not become a node in the scientific knowledge graph.

## 6. Audit

Before finishing, re-read every modified knowledge note; verify source IDs and page numbers; verify no old human content disappeared; verify no duplicate claim or note was introduced; verify contradictions were preserved; verify no source file was changed; mark the work file as completed.

Report notes created/updated, genuinely new corroborating sources added to existing claims, same-source evidence skipped as already integrated, contradictions or unresolved questions, and any extraction limitations. Never report a new source as skipped merely because its proposition matches an existing note.
