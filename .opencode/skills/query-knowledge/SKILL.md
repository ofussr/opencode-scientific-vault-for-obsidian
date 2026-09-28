---
name: query-knowledge
description: Answer scientific questions from Knowledge/ and its local provenance, reading original Papers/ pages only when verification is needed. Does not modify the knowledge base unless explicitly asked.
slash: true
metadata:
  opencode/autoinvoke: "false"
---

# Query Knowledge

Use this skill when the user asks a scientific question about the maintained vault.

## Default source order
1. Search `Knowledge/`.
2. Read the most relevant notes.
3. Use `.research/sources/` to resolve source IDs and original paper paths when needed.
4. If a claim needs verification, use OpenCode’s built-in `read` on the original PDF first; use `pdf_pages` only as a focused text fallback.

Do not answer from model memory when the user is asking about the local knowledge base. If the knowledge base does not support an answer, say what is missing. Read both language blocks as one note; answer in the language the user used unless they ask for another language. Do not translate uncertainty away or treat parallel translations as independent evidence.

Use filename/path search, grep for canonical terms/aliases/formulas/abbreviations/key phrases, and direct reading of a small set of plausible notes. Do not dump the entire `Knowledge/` tree into context.

When evidence conflicts, report the different supported findings and conditions; do not manufacture a consensus.

Do not create or update `Knowledge/` merely because a question was asked. If the user explicitly asks to save a durable synthesis, reconcile and write it using the same provenance and write-safety rules as ingestion.
