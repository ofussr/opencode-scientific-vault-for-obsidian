---
name: knowledge-reconcile
description: Helper skill for matching extracted claims to existing Knowledge/ notes, resolving aliases and identity, preventing duplicate or over-atomic notes, and preserving conflicts.
slash: false
metadata:
  opencode/autoinvoke: "false"
  opencode/slash: "false"
---

# Knowledge Reconcile

Read `references/identity-resolution.md`. Input is the compact claim set in `.research/work/<source-id>.md`.

Do not edit `Knowledge/` during this phase. First write a reconciliation plan into the work file.

## Topic-boundary review

Before assigning claims to notes, identify the distinct reusable topics supported by the source and compare them with existing notes. A topic may deserve its own note even when it concerns the same material or paper as another topic.

For each candidate boundary, ask:

- Does it answer a scientifically distinct question (for example, phase-transition thermodynamics versus local-structure mechanisms)?
- Is it substantively supported by enough evidence to remain useful outside this one paragraph or paper?
- Would placing it in the broader note make retrieval and future synthesis harder?

If these criteria support a split, plan separate concept-centered notes and meaningful links. Do not split only by source, section heading, or mentioned term. A concise overview note is optional and should contain useful synthesis, not only links. Record the proposed note map and rationale in the reconciliation plan.

## For each useful claim

1. Derive plausible lookup forms in both English and Russian: canonical scientific name and its Russian equivalent, formula, abbreviation, spelling/transliteration variants, and existing aliases.
2. Search `Knowledge/`: filenames/paths with glob, note text and YAML aliases with grep, then directly read plausible notes.
3. Compare both the scientific proposition and its evidence record. These are different things: a proposition already stated in `Knowledge/` does not make evidence from a newly processed source redundant. Explicitly compare the source's reported methods and evidence domains with the target note: a new characterization method or measurement domain is a new contribution even when the structure/material itself is already known.
4. Decide one action: `SKIP_ALREADY_KNOWN`, `UPDATE_EXISTING`, `ADD_CORROBORATING_EVIDENCE`, `ADD_CONTRADICTION`, `ADD_RELATIONSHIP`, `CREATE_NEW_NOTE`, `DISCARD_MENTION_ONLY`, or `UNRESOLVED_IDENTITY`.
5. Record target notes, identity reasoning, exact claim or evidence to add, source/page provenance, and meaningful links.


## Claim deduplication versus evidence accumulation

Deduplicate repeated wording and propositions; do not deduplicate away new sources.

- Use `SKIP_ALREADY_KNOWN` only when this same source ID has already been integrated for the equivalent claim and it contributes no unrecorded evidence or detail. This is the idempotency case. A short result is not a reason to skip it; assess whether it adds a method, evidence domain, condition, result, or interpretation.
- When a different source reports or supports a proposition already present, use `ADD_CORROBORATING_EVIDENCE`. This includes evidence from a new characterization method (for example Raman evidence for a structure already discussed using XRD). Keep one concise proposition where appropriate, but record the new method/domain, source ID, and exact page(s) in the existing note and source manifest. The new source is a real addition even if its reported value matches.
- Preserve source-specific sample, method, composition, conditions, uncertainty, and author interpretation when these are reported. If these differ materially, add a separate attributed evidence statement rather than attaching a bare citation that could imply identical conditions.
- Do not call evidence an independent replication unless the source establishes that. Corroboration adds support; it does not by itself prove consensus or erase limitations.
- Apply the same evidence addition in both language blocks, with matching citations and meaning. Update the English and Russian text together.

In the reconciliation plan, state whether the source is new corroboration, a new detail, a contradiction, or already-integrated evidence. Never classify a different source as `SKIP_ALREADY_KNOWN` solely because the main proposition or numerical result appears in an existing note.

## Note-creation gate

A new note is justified only when the concept is genuinely distinct, has durable reuse value, is substantively treated by the source, and would not be clearer as a section or claim inside a broader note.

Do not create a page merely because a noun exists in the paper. If the candidate would contain only a trivial definition, one passing statement, or one attribute that naturally belongs to a broader concept, integrate it into the broader note instead.

## Conflict handling

A contradiction is knowledge, not a cleanup problem. Keep source-specific results and their conditions side by side. Do not silently select, average, or merge incompatible claims.
