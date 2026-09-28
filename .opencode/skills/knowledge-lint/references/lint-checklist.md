# Lint Checklist

## Duplicate / identity risks
Check formula/common-name splits, abbreviation/expanded-name splits, spelling variants, and overlapping pages that may actually be broader/narrower rather than duplicates.

## Provenance and evidence coverage
Flag substantive claims without source IDs, source IDs missing from a note's Sources mapping, missing/inconsistent source manifests, and missing page provenance where reasonably available. When comparing note claims with source manifests, do not mistake different sources supporting the same proposition for duplicate evidence; check that each integrated source remains cited. Flag cases where the literature note mentions a structure/result but omits a distinct evidence domain reported by an integrated source (for example, a Raman assignment alongside existing XRD evidence). A result's brevity alone does not make it immaterial.

## Evidence coverage
For notes about materials, phases, mechanisms, or properties, compare the cited source manifests and extracted claims against the evidence actually represented in the note. Flag potentially omitted characterization methods, measurements, or source-specific conclusions; give the source and pages. Do not infer an omitted result from a title or mention alone. A result's brevity alone does not make it immaterial.

## Quantitative claims
Flag numbers without required units, measurements without critical conditions, suspicious precision, unclear measured/fitted/calculated/nominal status, and values apparently copied from a graph without explicit digitization.

## Contradictions
Look for incompatible claims silently presented as consensus, newer claims overwriting older supported evidence, and unresolved differences lacking conditions.

## Note granularity
Flag mention-only, trivially small, attribute-only, or excessively broad notes. Where a note combines distinct reusable topics, identify the proposed split boundary and explain why the topics answer different scientific questions. Do not auto-delete, auto-merge, or refactor notes during lint.

## Graph quality
Look for source-paper nodes dominating concept topology, links created only because terms co-occur, and missing links where a clear scientific relationship is actually expressed. Orphan status alone is not a defect.

## Write integrity
Look for duplicated claims from repeated ingestion, empty template sections, source links using `[[wikilinks]]`, and large stylistic rewrites that erased source distinctions. Check that each user-facing `Knowledge/` note has an English block followed by a semantically complete Russian counterpart, with matching citations, conditions, uncertainty, and links. Flag missing or materially inconsistent translations without silently rewriting them.
