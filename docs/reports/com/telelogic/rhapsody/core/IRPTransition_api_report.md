# Rhapsody API Validation: IRPTransition

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPTransition` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interactions.py`)
- Members: Python `23`, Java `23`, pywin32 `20`
- Deviation items: `5` (actionable `5`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_is_overridden() -> isOverridden | getIsOverridden (method) | isOverridden (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_its_label() -> itsLabel; set_its_label() -> setItsLabel | getItsLabel (method); setItsLabel (method) | itsLabel (property); setItsLabel (method) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_its_source() -> itsSource; set_its_source() -> itsSource | getItsSource (method); setItsSource (method) | itsSource (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_its_statechart() -> itsStatechart; set_its_statechart() -> itsStatechart | getItsStatechart (method); setItsStatechart (method) | itsStatechart (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_its_target() -> itsTarget; set_its_target() -> itsTarget | getItsTarget (method); setItsTarget (method) | itsTarget (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (11) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_inherits_from() -> getInheritsFrom | getInheritsFrom (method) | getInheritsFrom (method) | MATCH | — |
| is_default_transition() -> isDefaultTransition | isDefaultTransition (method) | isDefaultTransition (method) | MATCH | — |
| is_static_reaction() -> isStaticReaction | isStaticReaction (method) | isStaticReaction (method) | MATCH | — |
| get_its_action() -> getItsAction; set_its_action() -> setItsAction | getItsAction (method); setItsAction (method) | getItsAction (method); setItsAction (method) | MATCH | — |
| its_compound_source() -> itsCompoundSource | itsCompoundSource (method) | itsCompoundSource (method) | MATCH | — |
| get_its_guard() -> getItsGuard; set_its_guard() -> setItsGuard | getItsGuard (method); setItsGuard (method) | getItsGuard (method); setItsGuard (method) | MATCH | — |
| get_its_trigger() -> getItsTrigger; set_its_trigger() -> setItsTrigger | getItsTrigger (method); setItsTrigger (method) | getItsTrigger (method); setItsTrigger (method) | MATCH | — |
| get_of_state() -> getOfState | getOfState (method) | getOfState (method) | MATCH | — |
| override_inheritance() -> overrideInheritance | overrideInheritance (method) | overrideInheritance (method) | MATCH | — |
| reset_label_inheritance() -> resetLabelInheritance | resetLabelInheritance (method) | resetLabelInheritance (method) | MATCH | — |
| unoverride_inheritance() -> unoverrideInheritance | unoverrideInheritance (method) | unoverrideInheritance (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (5 findings)
- **Target:** `IRPTransition` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interactions.py`
- **Affected call(s):** get_is_overridden() -> isOverridden; get_its_label() -> itsLabel; set_its_label() -> setItsLabel; get_its_source() -> itsSource; set_its_source() -> itsSource; get_its_statechart() -> itsStatechart; set_its_statechart() -> itsStatechart; get_its_target() -> itsTarget; set_its_target() -> itsTarget
- **Java signature(s):** `IRPTransition.setItsTarget(com.telelogic.rhapsody.core.IRPStateVertex)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
