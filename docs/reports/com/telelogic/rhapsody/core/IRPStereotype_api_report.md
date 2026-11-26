# Rhapsody API Validation: IRPStereotype

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPStereotype` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_stereotype.py`)
- Members: Python `5`, Java `6`, pywin32 `5`
- Deviation items: `0` (actionable `0`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | PASS | No change needed. |

<details>
<summary>Correct items (5) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_meta_class() -> addMetaClass | addMetaClass (method) | addMetaClass (method) | MATCH | — |
| icon (property) -> icon | getIcon (method) | icon (property) | MATCH | — |
| is_new_term (property) -> isNewTerm | getIsNewTerm (method); setIsNewTerm (method) | isNewTerm (property) | MATCH | — |
| of_meta_class (property) -> ofMetaClass | getOfMetaClass (method) | ofMetaClass (property) | MATCH | — |
| remove_meta_class() -> removeMetaClass | removeMetaClass (method) | removeMetaClass (method) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
