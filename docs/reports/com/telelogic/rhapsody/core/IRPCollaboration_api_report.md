# Rhapsody API Validation: IRPCollaboration

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPCollaboration` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collaboration.py`)
- Members: Python `39`, Java `39`, pywin32 `40`
- Deviation items: `20` (actionable `20`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_activation_condition() -> activationCondition | getActivationCondition (method) | activationCondition (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_activation_mode() -> getActivationMode | getActivationMode (method) | activationMode (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the activationMode property or a getter/setter fallback instead of calling getActivationMode directly. |
| get_associations() -> getAssociations | getAssociations (method) | associations (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the associations property or a getter/setter fallback instead of calling getAssociations directly. |
| get_classifier() -> getClassifier | getClassifier (method) | classifier (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the classifier property or a getter/setter fallback instead of calling getClassifier directly. |
| get_execution_occurrences() -> getExecutionOccurrences | getExecutionOccurrences (method) | executionOccurrences (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the executionOccurrences property or a getter/setter fallback instead of calling getExecutionOccurrences directly. |
| get_interaction_occurrences() -> getInteractionOccurrences | getInteractionOccurrences (method) | interactionOccurrences (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the interactionOccurrences property or a getter/setter fallback instead of calling getInteractionOccurrences directly. |
| get_interaction_operators() -> getInteractionOperators | getInteractionOperators (method) | interactionOperators (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the interactionOperators property or a getter/setter fallback instead of calling getInteractionOperators directly. |
| get_message_points() -> getMessagePoints | getMessagePoints (method) | getMessagePoints (method); messagePoints (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_messages() -> getMessages | getMessages (method) | messages (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the messages property or a getter/setter fallback instead of calling getMessages directly. |
| get_mode() -> getMode | getMode (method) | mode (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the mode property or a getter/setter fallback instead of calling getMode directly. |
| add_action_block() -> addActionBlock | — | addActionBlock (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| add_cancelled_timeout() -> addCancelledTimeout | — | addCancelledTimeout (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| add_condition_mark() -> addConditionMark | — | addConditionMark (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| add_destruction_event() -> addDestructionEvent | — | addDestructionEvent (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| add_found_message() -> addFoundMessage | — | addFoundMessage (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| add_interaction_occurrence() -> addInteractionOccurrence | — | addInteractionOccurrence (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 0 parameter(s) (0 required; params: —; types: —). Pass the documented parameters. |
| add_interaction_operator() -> addInteractionOperator | — | addInteractionOperator (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 0 parameter(s) (0 required; params: —; types: —). Pass the documented parameters. |
| add_lost_message() -> addLostMessage | — | addLostMessage (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| add_system_border() -> addSystemBorder | — | addSystemBorder (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 0 parameter(s) (0 required; params: —; types: —). Pass the documented parameters. |
| add_time_interval() -> addTimeInterval | — | addTimeInterval (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (29) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_activator() -> getActivator | getActivator (method) | getActivator (method) | MATCH | — |
| add_action_block() -> addActionBlock | addActionBlock (method) | addActionBlock (method) | MATCH | — |
| add_cancelled_timeout() -> addCancelledTimeout | addCancelledTimeout (method) | addCancelledTimeout (method) | MATCH | — |
| add_classifier_role() -> addClassifierRole | addClassifierRole (method) | addClassifierRole (method) | MATCH | — |
| add_classifier_role_by_name() -> addClassifierRoleByName | addClassifierRoleByName (method) | addClassifierRoleByName (method) | MATCH | — |
| add_classifier_role_for_instance() -> addClassifierRoleForInstance | addClassifierRoleForInstance (method) | addClassifierRoleForInstance (method) | MATCH | — |
| add_condition_mark() -> addConditionMark | addConditionMark (method) | addConditionMark (method) | MATCH | — |
| add_ctor() -> addCtor | addCtor (method) | addCtor (method) | MATCH | — |
| add_data_flow() -> addDataFlow | addDataFlow (method) | addDataFlow (method) | MATCH | — |
| add_destruction_event() -> addDestructionEvent | addDestructionEvent (method) | addDestructionEvent (method) | MATCH | — |
| add_dtor() -> addDtor | addDtor (method) | addDtor (method) | MATCH | — |
| add_duration_constraint() -> addDurationConstraint | addDurationConstraint (method) | addDurationConstraint (method) | MATCH | — |
| add_duration_observation() -> addDurationObservation | addDurationObservation (method) | addDurationObservation (method) | MATCH | — |
| add_found_message() -> addFoundMessage | addFoundMessage (method) | addFoundMessage (method) | MATCH | — |
| add_interaction_occurrence() -> addInteractionOccurrence | addInteractionOccurrence (method) | addInteractionOccurrence (method) | MATCH | — |
| add_interaction_operator() -> addInteractionOperator | addInteractionOperator (method) | addInteractionOperator (method) | MATCH | — |
| add_lost_message() -> addLostMessage | addLostMessage (method) | addLostMessage (method) | MATCH | — |
| add_message() -> addMessage | addMessage (method) | addMessage (method) | MATCH | — |
| add_reply_message() -> addReplyMessage | addReplyMessage (method) | addReplyMessage (method) | MATCH | — |
| add_state_invariant() -> addStateInvariant | addStateInvariant (method) | addStateInvariant (method) | MATCH | — |
| add_system_border() -> addSystemBorder | addSystemBorder (method) | addSystemBorder (method) | MATCH | — |
| add_time_constraint() -> addTimeConstraint | addTimeConstraint (method) | addTimeConstraint (method) | MATCH | — |
| add_time_interval() -> addTimeInterval | addTimeInterval (method) | addTimeInterval (method) | MATCH | — |
| add_time_observation() -> addTimeObservation | addTimeObservation (method) | addTimeObservation (method) | MATCH | — |
| add_timeout() -> addTimeout | addTimeout (method) | addTimeout (method) | MATCH | — |
| get_concurrent_group() -> getConcurrentGroup | getConcurrentGroup (method) | getConcurrentGroup (method) | MATCH | — |
| generate_sequence() -> generateSequence | generateSequence (method) | generateSequence (method) | MATCH | — |
| get_predecessor() -> getPredecessor | getPredecessor (method) | getPredecessor (method) | MATCH | — |
| get_successor() -> getSuccessor | getSuccessor (method) | getSuccessor (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPCollaboration` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collaboration.py`
- **Affected call(s):** get_activation_condition() -> activationCondition; get_message_points() -> getMessagePoints
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (8 findings)
- **Target:** `IRPCollaboration` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collaboration.py`
- **Affected call(s):** get_activation_mode() -> getActivationMode; get_associations() -> getAssociations; get_classifier() -> getClassifier; get_execution_occurrences() -> getExecutionOccurrences; get_interaction_occurrences() -> getInteractionOccurrences; get_interaction_operators() -> getInteractionOperators; get_messages() -> getMessages; get_mode() -> getMode
- **Recommended change:** Use the activationMode property or a getter/setter fallback instead of calling getActivationMode directly.
- **Recommended change:** Use the associations property or a getter/setter fallback instead of calling getAssociations directly.
- **Recommended change:** Use the classifier property or a getter/setter fallback instead of calling getClassifier directly.
- **Recommended change:** Use the executionOccurrences property or a getter/setter fallback instead of calling getExecutionOccurrences directly.
- **Recommended change:** Use the interactionOccurrences property or a getter/setter fallback instead of calling getInteractionOccurrences directly.
- **Recommended change:** Use the interactionOperators property or a getter/setter fallback instead of calling getInteractionOperators directly.
- **Recommended change:** Use the messages property or a getter/setter fallback instead of calling getMessages directly.
- **Recommended change:** Use the mode property or a getter/setter fallback instead of calling getMode directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (7 findings)
- **Target:** `IRPCollaboration` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collaboration.py`
- **Affected call(s):** add_action_block() -> addActionBlock; add_cancelled_timeout() -> addCancelledTimeout; add_condition_mark() -> addConditionMark; add_destruction_event() -> addDestructionEvent; add_found_message() -> addFoundMessage; add_lost_message() -> addLostMessage; add_time_interval() -> addTimeInterval
- **Recommended change:** Wrapper passes types ['str'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_ARITY_MISMATCH (3 findings)
- **Target:** `IRPCollaboration` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collaboration.py`
- **Affected call(s):** add_interaction_occurrence() -> addInteractionOccurrence; add_interaction_operator() -> addInteractionOperator; add_system_border() -> addSystemBorder
- **Recommended change:** Wrapper passes [1] arg(s) but pywin32 declares 0 parameter(s) (0 required; params: —; types: —). Pass the documented parameters.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
