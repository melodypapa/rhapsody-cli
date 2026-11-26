# Rhapsody API Validation: IRPClassifierRole

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPClassifierRole` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_classifier_role.py`)
- Members: Python `5`, Java `8`, pywin32 `5`
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
<summary>Correct items (5) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| formal_classifier (property) -> formalClassifier | getFormalClassifier (method); setFormalClassifier (method) | formalClassifier (property) | MATCH | — |
| formal_instance (property) -> formalInstance | getFormalInstance (method); setFormalInstance (method) | formalInstance (property) | MATCH | — |
| get_referencing_classifier_roles_recursively() -> getReferencingClassifierRolesRecursively | getReferencingClassifierRolesRecursively (method) | getReferencingClassifierRolesRecursively (method) | MATCH | — |
| referenced_sequence_diagram (property) -> referencedSequenceDiagram | getReferencedSequenceDiagram (method); setReferencedSequenceDiagram (method) | referencedSequenceDiagram (property) | MATCH | — |
| role_type (property) -> roleType | getRoleType (method) | roleType (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
