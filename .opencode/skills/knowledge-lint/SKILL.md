---
name: knowledge-lint
description: Audit the scientific knowledge base for duplicates, weak provenance, unsupported quantitative claims, broken structure, artificial graph links, and unresolved contradictions. Writes a report but does not silently repair Knowledge/.
slash: true
metadata:
  opencode/autoinvoke: "false"
---

# Knowledge Lint

Read `references/lint-checklist.md`. Audit `Knowledge/` and `.research/sources/`. Do not modify `Knowledge/` during lint unless the user separately asks to apply specific fixes.

Write the report to `.research/lint/YYYY-MM-DD-lint.md`. If the environment does not provide a trustworthy current date, use a descriptive non-date filename rather than inventing one.

Report high-confidence problems, possible duplicates/identity conflicts, provenance gaps, quantitative-data risks, potentially omitted evidence domains or source-specific findings, contradictions needing clearer representation, note-granularity problems, link/graph quality issues, source-manifest inconsistencies, and suggested fixes with paths.

Do not treat every orphan note as an error and do not create links merely to make the graph denser.
