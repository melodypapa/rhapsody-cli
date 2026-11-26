# Rhapsody API Validation: IRPCollaboration

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPCollaboration` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collaboration.py`)
- Members: Python `39`, Java `39`, pywin32 `40`
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
<summary>Correct items (39) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| activation_condition (property) -> activationCondition | getActivationCondition (method) | activationCondition (property) | MATCH | — |
| activation_mode (property) -> activationMode | getActivationMode (method) | activationMode (property) | MATCH | — |
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
| associations (property) -> associations | getAssociations (method) | associations (property) | MATCH | — |
| classifier (property) -> classifier | getClassifier (method) | classifier (property) | MATCH | — |
| execution_occurrences (property) -> executionOccurrences | getExecutionOccurrences (method) | executionOccurrences (property) | MATCH | — |
| generate_sequence() -> generateSequence | generateSequence (method) | generateSequence (method) | MATCH | — |
| get_activator() -> getActivator | getActivator (method) | getActivator (method) | MATCH | — |
| get_concurrent_group() -> getConcurrentGroup | getConcurrentGroup (method) | getConcurrentGroup (method) | MATCH | — |
| get_predecessor() -> getPredecessor | getPredecessor (method) | getPredecessor (method) | MATCH | — |
| get_successor() -> getSuccessor | getSuccessor (method) | getSuccessor (method) | MATCH | — |
| interaction_occurrences (property) -> interactionOccurrences | getInteractionOccurrences (method) | interactionOccurrences (property) | MATCH | — |
| interaction_operators (property) -> interactionOperators | getInteractionOperators (method) | interactionOperators (property) | MATCH | — |
| message_points (property) -> messagePoints | getMessagePoints (method) | getMessagePoints (method); messagePoints (property) | MATCH | — |
| messages (property) -> messages | getMessages (method) | messages (property) | MATCH | — |
| mode (property) -> mode | getMode (method) | mode (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
