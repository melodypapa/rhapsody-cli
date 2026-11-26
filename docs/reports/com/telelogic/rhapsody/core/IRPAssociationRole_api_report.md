# Rhapsody API Validation: IRPAssociationRole

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPAssociationRole` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_association_role.py`)
- Members: Python `3`, Java `3`, pywin32 `3`
- Deviation items: `1` (actionable `1`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_role_type() -> roleType | getRoleType (method) | roleType (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (2) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_classifier_roles() -> getClassifierRoles | getClassifierRoles (method) | getClassifierRoles (method) | MATCH | — |
| get_formal_relations() -> getFormalRelations | getFormalRelations (method) | getFormalRelations (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPAssociationRole` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_association_role.py`
- **Affected call(s):** get_role_type() -> roleType
- **Java signature(s):** `IRPAssociationRole.getRoleType()`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
