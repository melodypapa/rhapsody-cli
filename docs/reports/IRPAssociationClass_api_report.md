# Rhapsody API Validation: IRPAssociationClass

## Summary
- Target wrapper: `RPAssociationClass` (`src/rhapsody_cli/models/elements/classifiers/model_association_class.py`)
- Members: Python `4`, Java `4`, pywin32 `3`
- Deviations: `0`
- Deviations by status:
  - None

- Informational binding differences (expected): `1`
- Wrapper backlog (supported members without wrappers): `0`
- Documented aliases: `0`, documented unavailable: `0`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_is_class() -> isClass; set_is_class() -> setIsClass | getIsClass (method); setIsClass (method) | isClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_end1() -> end1 | getEnd1 (method) | end1 (property) | MATCH | — |
| get_end2() -> end2 | getEnd2 (method) | end2 (property) | MATCH | — |

## AI Fix Guidance
No deviations require changes.
