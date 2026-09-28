---
name: paper-extract
description: Helper skill for extracting compact, page-grounded scientific claims from one PDF without overflowing local-model context.
slash: false
metadata:
  opencode/autoinvoke: "false"
  opencode/slash: "false"
---

# Paper Extract

This is an ingestion helper. Its output is a compact claim set in `.research/work/<source-id>.md`.

Read `references/source-grounding.md`. Read `references/quantitative-data.md` when the source contains measurements, tables, figures, fitted values, phase diagrams, or equations.

## Context discipline

For an ordinary paper, first use OpenCode’s built-in `read` on the original PDF. Do not split a paper into tiny chunks solely to satisfy an arbitrary page-count rule: OpenCode’s PDF path can process the document as a whole and may use OCR or visual handling when its text layer is defective.

Use `pdf_pages` as a fallback when built-in PDF reading is unavailable, or to inspect a focused text range. That helper extracts text only, at most 4 pages and up to the configured character limit per call; it does not perform OCR and does not preserve page layout. If fallback output is truncated, retry a smaller range.

Keep the compact claim set in `.research/work/<source-id>.md`; never copy raw article prose there. Retain page numbers for every claim. Check tables, equations, figures, and any suspicious OCR-derived values against the original PDF before treating them as evidence. If a value cannot be read reliably, record the uncertainty rather than guessing.

## Evidence coverage and extraction order

Do not let the number of sentences determine whether a result is extracted. A single sentence can report a consequential new observation, measurement, structural assignment, or characterization method.

1. Read the PDF with the built-in `read` tool and identify title, authors, year, DOI if present, abstract, and article structure.
2. Extract substantive claims across the full paper, retaining page provenance.
3. Read methods and experimental details closely enough to preserve conditions needed to interpret results.
4. Check tables, figure captions, equations, and conclusions; verify important numerical claims against their source pages.
5. Make an evidence-coverage pass across the paper's reported methods and result types (for example Raman, XRD, microscopy, spectroscopy, dielectric or transport measurements, calculations, and phase/structure assignments). Record each meaningful result, including concise results mentioned only once and evidence shown primarily in figures or captions. Note which concept or existing topic it bears on.
6. If OCR, layout, or a figure is unclear, inspect the relevant PDF page again. If the built-in path cannot expose it, use a focused `pdf_pages` extraction as a text fallback and mark unresolved visual information.
7. If the full PDF cannot be read, continue with `pdf_pages` in manageable ranges and persist compact state as you go. Do not assume a scan has been read when no reliable text or visual evidence is available.
8. At the end, inspect the compact claim set for missing methods/evidence domains, missing conditions, and unsupported generalization. Do not omit a finding just because its text is brief or the broader topic is already discussed elsewhere; let reconciliation determine whether it is new evidence.

## Claim gate

Extract a result when the source reports or interprets actual evidence, even briefly. A passing mention is a term or topic reference without a result, measurement, data-supported assignment, or meaningful author conclusion. A one-sentence report of a measurement or structure assignment is substantive and should be captured with method, interpretation, uncertainty, and page provenance. Relevance and redundancy must be decided against existing knowledge during reconciliation, not inferred from sentence length.

## Work-file claim schema

### C-001
- Kind: observation | author-interpretation | synthesis-candidate | agent-inference
- Claim: ...
- Method / evidence domain: ...
- Target concept or existing topic: ...
- Conditions: ...
- Pages: 4–5
- Evidence: direct | indirect | ambiguous
- Notes: ...

Use `agent-inference` sparingly. It is not eligible to become an unqualified fact in `Knowledge/`.

## Bibliographic identity

Capture only what the source itself supports: title, authors, year, DOI or another stable identifier if visible, and source path. Do not guess missing metadata.
