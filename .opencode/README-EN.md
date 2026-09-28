# Setup and usage

This package is designed for OpenCode V2 and an Obsidian vault with `Papers/` and `Knowledge/` folders. The model is connected through a ChatGPT Plus/Pro account.

## 1. Where to extract the files

Copy the contents of the archive into the root of your vault:

```text
<Vault>/
├── AGENTS.md
├── opencode.jsonc
├── Papers/
├── Knowledge/
├── .opencode/
└── .research/
```

Do not replace your existing `Papers/` or `Knowledge/` folders.

## 2. Connect ChatGPT

In OpenCode, run `/connect`, choose `OpenAI` → `ChatGPT Plus/Pro`, and complete sign-in in your browser. Then open `/models` and select an OpenAI model. You do not need to enter an API key or server address.

## 3. How PDFs are read

When processing a paper, the agent first uses OpenCode's built-in `read` tool on the original PDF. In the tested workflow, OpenCode extracted the text, detected problems with the embedded OCR, and applied additional recognition. This is the preferred path because it can process the document as a whole instead of relying only on text extracted by `pypdf`.

If built-in PDF reading is unavailable, use the fallback `pdf_pages` tool. It extracts text in small page ranges, but does not perform OCR or visually interpret charts. Install this dependency once for the fallback mode:

```bash
pip install pypdf
```

With either reading method, verify important numbers, tables, equations, and conclusions against the original pages. Store concise claims with page references in `.research/work/`, not the full paper text.

## 4. Main commands

### Integrate a paper

Run the custom `/import-paper` command and provide the PDF path: `/import-paper Papers/Reisman-1955.pdf`. If the PDF is already attached to the message, you can run `/import-paper` without an argument. The command explicitly tells OpenCode to load the `ingest-paper` skill and follow its `paper-extract` → `knowledge-reconcile` → `knowledge-write` stages. Notes in `Knowledge/` are written in English and Russian in the same file: the English block comes first, followed by the Russian block. Sources and intermediate technical files in `.research/` are not duplicated in both languages.

### Ask the knowledge base

```text
Answer using the Knowledge base: what is known about the KNbO3-KTaO3 phase diagram?
```

### Check and restructure notes

```text
Audit the quality of the Knowledge base and save a report.
```

For an audit, the agent uses `knowledge-lint`: it writes a report to `.research/lint/` and does not modify `Knowledge/`.

If an existing note has become too broad, explicitly request a structural refactor, for example:

```text
Review the granularity of Knowledge/KNbO3.md. If it combines independent scientific topics, split them into separate notes, retain a useful overview, and update the links. Preserve both English and Russian versions, all citations, and page numbers.
```

The `knowledge-refactor` skill is used for this explicitly requested restructuring. Routine audits and paper imports do not run it automatically.

## 5. How note granularity is chosen

When processing a paper, the agent checks whether the sources support multiple independent topics that answer different questions and are useful on their own. The number of notes is not predetermined: closely related claims stay together, while sufficiently independent topics become separate pages even if they concern the same material. If a new source supports a claim already in the knowledge base, the agent adds the new source and page references instead of discarding the corroboration as a duplicate. Short results are also retained when they add a new method or type of evidence, such as a Raman spectrum for a structure already discussed.

## 6. Switching models

Use `/models` to change the OpenAI model. This package is configured for ChatGPT Plus/Pro sign-in. If you use the API instead of a subscription, choose manual API-key entry during `/connect`; API usage is billed separately from the ChatGPT subscription.

## 7. What the system deliberately does not do

- It does not create one note per paper.
- It does not create a note for a passing mention of a term.
- It does not turn PDF sources into central graph nodes.
- It does not average out conflicting papers.
- It does not guess numbers from broken tables or charts.
- It does not rewrite entire user notes without an explicit restructuring request.
- It keeps the English and Russian versions in one note: the English block comes first, followed by its Russian equivalent.
- It does not use model memory as a source of scientific facts.

## 8. Keep the Obsidian graph clean

Skills prohibit `[[wikilinks]]` to source files. To keep the service file `AGENTS.md` out of regular Obsidian search and graph views, add it to Obsidian's built-in Excluded files list. `.opencode/` and `.research/` are service directories and are hidden.

## 9. Why there is no index.md or shared log.md

These files are intentionally omitted because they continuously inflate context in a large knowledge base. OpenCode can use `glob`/`grep`; provenance and idempotency are stored in `.research/sources/`, while intermediate state is stored separately for each paper in `.research/work/`.

## 10. If a PDF is scanned or its OCR is unreliable

Start with OpenCode's built-in PDF reading: in the tested workflow, it detected a defective OCR layer and used additional recognition. If that path does not work, `pdf_pages` can show whether extractable text is present, but it does not perform OCR itself. Do not add unreadable passages to the knowledge base as established facts; record the limitation and identify the pages that need review.
