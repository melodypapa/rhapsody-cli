# Rhapsody API Validation: IRPAttribute

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPAttribute` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_attribute.py`)
- Members: Python `6`, Java `12`, pywin32 `6`
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
| is_constant (property) -> isConstant | getIsConstant (method); setIsConstant (method) | isConstant (property) | MATCH | — |
| is_ordered (property) -> isOrdered | getIsOrdered (method); setIsOrdered (method) | isOrdered (property) | MATCH | — |
| is_reference (property) -> isReference | getIsReference (method); setIsReference (method) | isReference (property) | MATCH | — |
| is_static (property) -> isStatic | getIsStatic (method); setIsStatic (method) | isStatic (property) | MATCH | — |
| multiplicity (property) -> multiplicity | getMultiplicity (method); setMultiplicity (method) | multiplicity (property) | MATCH | — |
| visibility (property) -> visibility | getVisibility (method); setVisibility (method) | visibility (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
