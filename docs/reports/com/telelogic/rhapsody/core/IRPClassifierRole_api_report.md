# Rhapsody API Validation: IRPClassifierRole

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPClassifierRole` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_other_model.py`)
- Members: Python `8`, Java `8`, pywin32 `5`
- Deviation items: `4` (actionable `4`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_formal_classifier() -> getFormalClassifier; set_formal_classifier() -> setFormalClassifier | getFormalClassifier (method); setFormalClassifier (method) | formalClassifier (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the formalClassifier property or a getter/setter fallback instead of calling getFormalClassifier and setFormalClassifier directly. |
| get_formal_instance() -> getFormalInstance; set_formal_instance() -> setFormalInstance | getFormalInstance (method); setFormalInstance (method) | formalInstance (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the formalInstance property or a getter/setter fallback instead of calling getFormalInstance and setFormalInstance directly. |
| get_referenced_sequence_diagram() -> getReferencedSequenceDiagram; set_referenced_sequence_diagram() -> setReferencedSequenceDiagram | getReferencedSequenceDiagram (method); setReferencedSequenceDiagram (method) | referencedSequenceDiagram (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the referencedSequenceDiagram property or a getter/setter fallback instead of calling getReferencedSequenceDiagram and setReferencedSequenceDiagram directly. |
| get_role_type() -> roleType | getRoleType (method) | roleType (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_referencing_classifier_roles_recursively() -> getReferencingClassifierRolesRecursively | getReferencingClassifierRolesRecursively (method) | getReferencingClassifierRolesRecursively (method) | MATCH | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (3 findings)
- **Target:** `IRPClassifierRole` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_other_model.py`
- **Affected call(s):** get_formal_classifier() -> getFormalClassifier; set_formal_classifier() -> setFormalClassifier; get_formal_instance() -> getFormalInstance; set_formal_instance() -> setFormalInstance; get_referenced_sequence_diagram() -> getReferencedSequenceDiagram; set_referenced_sequence_diagram() -> setReferencedSequenceDiagram
- **Java signature(s):** `IRPClassifierRole.getFormalClassifier()`, `IRPClassifierRole.setReferencedSequenceDiagram(com.telelogic.rhapsody.core.IRPSequenceDiagram)`
- **Recommended change:** Use the formalClassifier property or a getter/setter fallback instead of calling getFormalClassifier and setFormalClassifier directly.
- **Recommended change:** Use the formalInstance property or a getter/setter fallback instead of calling getFormalInstance and setFormalInstance directly.
- **Recommended change:** Use the referencedSequenceDiagram property or a getter/setter fallback instead of calling getReferencedSequenceDiagram and setReferencedSequenceDiagram directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPClassifierRole` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_other_model.py`
- **Affected call(s):** get_role_type() -> roleType
- **Java signature(s):** `IRPClassifierRole.getRoleType()`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
