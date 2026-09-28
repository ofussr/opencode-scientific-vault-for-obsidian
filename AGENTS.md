# Scientific Knowledge Vault

This vault is a persistent scientific knowledge base maintained from primary source papers.

## Roles of directories

- `Papers/` — immutable source library. Read sources here; never modify, rename, move, or delete them.
- `Knowledge/` — concept-centered scientific knowledge base. This is the only user-facing knowledge area the agent may maintain.
- `.research/` — hidden machine state: ingest work files, source manifests, and lint reports.
- `.opencode/` — agent configuration, tools, and skills. Do not modify during ordinary research work.

## Non-negotiable rules

1. Treat inspected source material as evidence. Model memory is never a scientific source.
2. Never fabricate citations, metadata, numerical values, units, experimental conditions, or missing text.
3. Distinguish direct observations, author interpretations, synthesis across sources, and agent inference.
4. Preserve contradictory findings and uncertainty. Never silently average or resolve incompatible literature.
5. Prefer small, auditable edits over whole-note rewrites.
6. Never delete human-written scientific content automatically.
7. Search existing knowledge before creating a new note.
8. Similarity does not imply identity. Do not merge distinct concepts merely because they are related.
9. A term being mentioned is not enough reason to create a note.
10. Keep quantitative claims together with the conditions needed to interpret them.
11. Re-processing the same source must not duplicate already integrated claims or evidence. Deduplicate propositions, not sources: a different source that supports an existing claim adds new provenance and must be recorded with its own source ID and page citation, including in both language blocks. Do not omit a short but substantive result because the broader material or structure is already discussed; new methods and evidence domains count as additions.
12. Use `[[wikilinks]]` for meaningful relationships between knowledge notes only. Do not create wiki links to `Papers/` or `.research/`; source provenance must not become the topology of the knowledge graph.
13. Do not use web sources unless the user explicitly asks to research, verify, or expand beyond the local source library. When external information is used, distinguish it clearly from local-source evidence.

## Knowledge-base philosophy

The unit of organization is reusable scientific knowledge: materials, systems, phases, phenomena, methods, mechanisms, properties, models, and relationships.

One paper is not one knowledge note.

Do not maximize note count or graph density, but do not force distinct scientific topics into one note merely because they concern the same material or paper. During reconciliation, check whether the evidence supports separate reusable topics that answer different scientific questions. Create a standalone note when that topic has durable independent value and enough substance to justify a separate page; otherwise keep it as a section in a broader note. Create a concise overview note only when it helps navigation and adds synthesis, not as an empty link index.

Every user-facing note in `Knowledge/` must be bilingual. Put the complete English content first, followed by its complete Russian counterpart in the same note. Keep the two sections semantically aligned, including conditions, uncertainty, citations, and meaningful links. Do not create separate English and Russian notes. Source manifests and temporary work files in `.research/` do not need translation.

## Main operations

- Use `ingest-paper` to integrate a paper from `Papers/`.
- Use `query-knowledge` to answer from the maintained knowledge base.
- Use `knowledge-lint` to audit quality without silently rewriting the wiki.
- Use `knowledge-refactor` when the user explicitly asks to split, reorganize, or restructure existing notes.

For paper ingestion, use OpenCode’s built-in `read` on the original PDF first so its PDF handling can inspect the document as a whole. Use `pdf_pages` only as a fallback when built-in PDF reading is unavailable or when a focused text range is needed.
