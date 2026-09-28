# Knowledge Note Format

Do not force unrelated template sections onto established notes. Every user-facing note in `Knowledge/` must contain two complete, matching language blocks in this order: English first, then Russian. Use one note per concept; do not create separate language copies.

For a new note, use only sections that have content. A useful default is:

```markdown
---
aliases: []
---

# Canonical name

## English

### Current understanding

### Evidence

### Contradictions / uncertainty

### Related

## Русский

### Текущее понимание

### Данные

### Противоречия / неопределённость

### Связанные понятия

## Sources / Источники
```

Translate all substantive prose faithfully. Preserve formulas, symbols, names, units, source IDs, page references, and wikilinks. Every source-grounded claim must have the same citation in both language blocks. The shared `Sources / Источники` section may appear once after both blocks. Keep the canonical filename/title stable; add translated names as aliases when useful.

When updating an existing monolingual note, preserve its existing content and add a faithful counterpart in the other language. When changing one claim, update both language versions together. Do not add information during translation, and do not rewrite unrelated prose for style.

A note should represent a reusable scientific concept, object, method, system, mechanism, property domain, or relationship. Do not create one note per paper, paragraph, or mentioned term, and avoid tiny pages that only restate one attribute of a broader note.
