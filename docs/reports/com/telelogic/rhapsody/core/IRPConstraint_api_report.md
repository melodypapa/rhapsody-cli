# Rhapsody API Validation: IRPConstraint

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPConstraint` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_misc.py`)
- Members: Python `1`, Java `1`, pywin32 `1`
- Deviation items: `1` (actionable `1`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_constraints_by_me() -> constraintsByMe | getConstraintsByMe (method) | constraintsByMe (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPConstraint` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_misc.py`
- **Affected call(s):** get_constraints_by_me() -> constraintsByMe
- **Java signature(s):** `IRPConstraint.getConstraintsByMe()`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
