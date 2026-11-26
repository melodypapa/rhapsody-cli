# Rhapsody API Validation: IRPState

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPState` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_statemachine.py`)
- Members: Python `48`, Java `48`, pywin32 `42`
- Deviation items: `18` (actionable `18`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| create_sub_statechart() -> createSubStatechart | createSubStatechart (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_default_transition() -> defaultTransition | getDefaultTransition (method) | defaultTransition (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_entry_action() -> entryAction; set_entry_action() -> entryAction | getEntryAction (method); setEntryAction (method) | entryAction (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_exit_action() -> exitAction; set_exit_action() -> exitAction | getExitAction (method); setExitAction (method) | exitAction (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_is_overridden() -> isOverridden | getIsOverridden (method) | isOverridden (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_is_reference_activity() -> isReferenceActivity | getIsReferenceActivity (method) | isReferenceActivity (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_its_statechart() -> itsStatechart | getItsStatechart (method) | itsStatechart (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_its_swimlane() -> itsSwimlane; set_its_swimlane() -> setItsSwimlane | getItsSwimlane (method); setItsSwimlane (method) | itsSwimlane (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_nested_statechart() -> nestedStatechart | getNestedStatechart (method) | nestedStatechart (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_reference_to_activity() -> referenceToActivity; set_reference_to_activity() -> setReferenceToActivity | getReferenceToActivity (method); setReferenceToActivity (method) | referenceToActivity (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_state_type() -> stateType; set_state_type() -> stateType | getStateType (method); setStateType (method) | stateType (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_sub_state_vertices() -> subStateVertices | getSubStateVertices (method) | subStateVertices (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| add_internal_transition() -> addInternalTransition | — | addInternalTransition (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| add_static_reaction() -> addStaticReaction | — | addStaticReaction (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| create_default_transition() -> createDefaultTransition | — | createDefaultTransition (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| delete_connector() -> deleteConnector | — | deleteConnector (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| delete_internal_transition() -> deleteInternalTransition | — | deleteInternalTransition (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| delete_static_reaction() -> deleteStaticReaction | — | deleteStaticReaction (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (31) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_activity_final() -> addActivityFinal | addActivityFinal (method) | addActivityFinal (method) | MATCH | — |
| add_connector() -> addConnector | addConnector (method) | addConnector (method) | MATCH | — |
| add_internal_transition() -> addInternalTransition | addInternalTransition (method) | addInternalTransition (method) | MATCH | — |
| add_state() -> addState | addState (method) | addState (method) | MATCH | — |
| add_static_reaction() -> addStaticReaction | addStaticReaction (method) | addStaticReaction (method) | MATCH | — |
| add_termination_state() -> addTerminationState | addTerminationState (method) | addTerminationState (method) | MATCH | — |
| create_default_transition() -> createDefaultTransition | createDefaultTransition (method) | createDefaultTransition (method) | MATCH | — |
| create_nested_statechart() (no static COM member) | createNestedStatechart (method) | createNestedStatechart (method) | MATCH | — |
| delete_connector() -> deleteConnector | deleteConnector (method) | deleteConnector (method) | MATCH | — |
| delete_internal_transition() -> deleteInternalTransition | deleteInternalTransition (method) | deleteInternalTransition (method) | MATCH | — |
| delete_static_reaction() -> deleteStaticReaction | deleteStaticReaction (method) | deleteStaticReaction (method) | MATCH | — |
| get_full_name_in_statechart() -> getFullNameInStatechart | getFullNameInStatechart (method) | getFullNameInStatechart (method) | MATCH | — |
| get_inherits_from() -> getInheritsFrom | getInheritsFrom (method) | getInheritsFrom (method) | MATCH | — |
| set_internal_transition() -> setInternalTransition | setInternalTransition (method) | setInternalTransition (method) | MATCH | — |
| get_internal_transitions() -> getInternalTransitions | getInternalTransitions (method) | getInternalTransitions (method) | MATCH | — |
| is_and() -> isAnd | isAnd (method) | isAnd (method) | MATCH | — |
| is_compound() -> isCompound | isCompound (method) | isCompound (method) | MATCH | — |
| is_leaf() -> isLeaf | isLeaf (method) | isLeaf (method) | MATCH | — |
| is_root() -> isRoot | isRoot (method) | isRoot (method) | MATCH | — |
| is_send_action_state() -> isSendActionState | isSendActionState (method) | isSendActionState (method) | MATCH | — |
| get_logical_states() -> getLogicalStates | getLogicalStates (method) | getLogicalStates (method) | MATCH | — |
| override_inheritance() -> overrideInheritance | overrideInheritance (method) | overrideInheritance (method) | MATCH | — |
| reset_entry_action_inheritance() -> resetEntryActionInheritance | resetEntryActionInheritance (method) | resetEntryActionInheritance (method) | MATCH | — |
| reset_exit_action_inheritance() -> resetExitActionInheritance | resetExitActionInheritance (method) | resetExitActionInheritance (method) | MATCH | — |
| get_send_action() -> getSendAction | getSendAction (method) | getSendAction (method) | MATCH | — |
| set_static_reaction() -> setStaticReaction | setStaticReaction (method) | setStaticReaction (method) | MATCH | — |
| get_static_reactions() -> getStaticReactions | getStaticReactions (method) | getStaticReactions (method) | MATCH | — |
| get_sub_states() -> getSubStates | getSubStates (method) | getSubStates (method) | MATCH | — |
| get_the_entry_action() -> getTheEntryAction | getTheEntryAction (method) | getTheEntryAction (method) | MATCH | — |
| get_the_exit_action() -> getTheExitAction | getTheExitAction (method) | getTheExitAction (method) | MATCH | — |
| unoverride_inheritance() -> unoverrideInheritance | unoverrideInheritance (method) | unoverrideInheritance (method) | MATCH | — |

</details>

## AI Fix Guidance

### PYWIN32_MEMBER_MISSING (1 finding)
- **Target:** `IRPState` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_statemachine.py`
- **Affected call(s):** create_sub_statechart() -> createSubStatechart
- **Java signature(s):** `IRPState.createSubStatechart()`
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (11 findings)
- **Target:** `IRPState` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_statemachine.py`
- **Affected call(s):** get_default_transition() -> defaultTransition; get_entry_action() -> entryAction; set_entry_action() -> entryAction; get_exit_action() -> exitAction; set_exit_action() -> exitAction; get_is_overridden() -> isOverridden; get_is_reference_activity() -> isReferenceActivity; get_its_statechart() -> itsStatechart; get_its_swimlane() -> itsSwimlane; set_its_swimlane() -> setItsSwimlane; get_nested_statechart() -> nestedStatechart; get_reference_to_activity() -> referenceToActivity; set_reference_to_activity() -> setReferenceToActivity; get_state_type() -> stateType; set_state_type() -> stateType; get_sub_state_vertices() -> subStateVertices
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (6 findings)
- **Target:** `IRPState` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_statemachine.py`
- **Affected call(s):** add_internal_transition() -> addInternalTransition; add_static_reaction() -> addStaticReaction; create_default_transition() -> createDefaultTransition; delete_connector() -> deleteConnector; delete_internal_transition() -> deleteInternalTransition; delete_static_reaction() -> deleteStaticReaction
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
