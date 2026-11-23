# Rhapsody API Validation: IRPAttribute

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPAttribute` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_attribute.py`)
- Members: Python `12`, Java `12`, pywin32 `6`
- Deviation items: `0` (actionable `0`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

<details>
<summary>Correct items (6) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_is_constant() -> isConstant; set_is_constant() -> isConstant | getIsConstant (method); setIsConstant (method) | isConstant (property) | MATCH | — |
| get_is_ordered() -> isOrdered; set_is_ordered() -> isOrdered | getIsOrdered (method); setIsOrdered (method) | isOrdered (property) | MATCH | — |
| get_is_reference() -> isReference; set_is_reference() -> isReference | getIsReference (method); setIsReference (method) | isReference (property) | MATCH | — |
| get_is_static() -> isStatic; set_is_static() -> isStatic | getIsStatic (method); setIsStatic (method) | isStatic (property) | MATCH | — |
| get_multiplicity() -> multiplicity; set_multiplicity() -> multiplicity | getMultiplicity (method); setMultiplicity (method) | multiplicity (property) | MATCH | — |
| get_visibility() -> visibility; set_visibility() -> visibility | getVisibility (method); setVisibility (method) | visibility (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
