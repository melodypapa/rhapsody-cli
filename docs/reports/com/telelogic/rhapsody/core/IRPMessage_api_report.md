# Rhapsody API Validation: IRPMessage

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPMessage` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interactions.py`)
- Members: Python `36`, Java `37`, pywin32 `26`
- Deviation items: `21` (actionable `21`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_actual_parameter_list() -> actualParameterList; set_actual_parameter_list() -> setActualParameterList | getActualParameterList (method); setActualParameterList (method) | actualParameterList (property); setActualParameterList (method) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_communication_connection() -> communicationConnection | getCommunicationConnection (method) | communicationConnection (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_condition() -> condition | getCondition (method); setCondition (method) | condition (property) | PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_duration_constraint() -> durationConstraint; set_duration_constraint() -> durationConstraint | getDurationConstraint (method); setDurationConstraint (method) | durationConstraint (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_duration_observation() -> durationObservation; set_duration_observation() -> durationObservation | getDurationObservation (method); setDurationObservation (method) | durationObservation (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_flow_port() -> flowPort; set_flow_port() -> flowPort | getFlowPort (method); setFlowPort (method) | flowPort (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_formal_interface_item() -> formalInterfaceItem; set_formal_interface_item() -> formalInterfaceItem; set_formal_interface_item() -> setFormalInterfaceItem | getFormalInterfaceItem (method); setFormalInterfaceItem (method) | formalInterfaceItem (property); setFormalInterfaceItem (method) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_formal_type() -> formalType; set_formal_type() -> formalType | getFormalType (method); setFormalType (method) | formalType (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_invariant() -> invariant; set_invariant() -> invariant | getInvariant (method); setInvariant (method) | invariant (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_message_type() -> messageType | getMessageType (method) | messageType (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_port() -> getPort; get_port() -> port; set_port() -> port; set_port() -> setPort | getPort (method); setPort (method) | Port (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the Port property or a getter/setter fallback instead of calling getPort and port and setPort directly. |
| get_return_value() -> returnValue; set_return_value() -> returnValue | getReturnValue (method); setReturnValue (method) | returnValue (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_sequence_number() -> sequenceNumber | getSequenceNumber (method) | sequenceNumber (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_source() -> source | getSource (method) | source (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_source_execution_occurrence() -> sourceExecutionOccurrence | getSourceExecutionOccurrence (method) | sourceExecutionOccurrence (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_target() -> target | getTarget (method) | target (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_target_execution_occurrence() -> targetExecutionOccurrence | getTargetExecutionOccurrence (method) | targetExecutionOccurrence (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_time_constraint() -> timeConstraint; set_time_constraint() -> timeConstraint | getTimeConstraint (method); setTimeConstraint (method) | timeConstraint (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_time_observation() -> timeObservation; set_time_observation() -> timeObservation | getTimeObservation (method); setTimeObservation (method) | timeObservation (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_timer_value() -> timerValue; set_timer_value() -> timerValue | getTimerValue (method); setTimerValue (method) | timerValue (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| set_actual_parameter_list() -> setActualParameterList | — | setActualParameterList (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (4) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_source_execution_occurrence() -> addSourceExecutionOccurrence | addSourceExecutionOccurrence (method) | addSourceExecutionOccurrence (method) | MATCH | — |
| add_target_execution_occurrence() -> addTargetExecutionOccurrence | addTargetExecutionOccurrence (method) | addTargetExecutionOccurrence (method) | MATCH | — |
| reroute() -> reroute | reroute (method) | reroute (method) | MATCH | — |
| get_signature() -> getSignature | getSignature (method) | getSignature (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (18 findings)
- **Target:** `IRPMessage` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interactions.py`
- **Affected call(s):** get_actual_parameter_list() -> actualParameterList; set_actual_parameter_list() -> setActualParameterList; get_communication_connection() -> communicationConnection; get_duration_constraint() -> durationConstraint; set_duration_constraint() -> durationConstraint; get_duration_observation() -> durationObservation; set_duration_observation() -> durationObservation; get_flow_port() -> flowPort; set_flow_port() -> flowPort; get_formal_interface_item() -> formalInterfaceItem; set_formal_interface_item() -> formalInterfaceItem; set_formal_interface_item() -> setFormalInterfaceItem; get_formal_type() -> formalType; set_formal_type() -> formalType; get_invariant() -> invariant; set_invariant() -> invariant; get_message_type() -> messageType; get_return_value() -> returnValue; set_return_value() -> returnValue; get_sequence_number() -> sequenceNumber; get_source() -> source; get_source_execution_occurrence() -> sourceExecutionOccurrence; get_target() -> target; get_target_execution_occurrence() -> targetExecutionOccurrence; get_time_constraint() -> timeConstraint; set_time_constraint() -> timeConstraint; get_time_observation() -> timeObservation; set_time_observation() -> timeObservation; get_timer_value() -> timerValue; set_timer_value() -> timerValue
- **Java signature(s):** `IRPMessage.getActualParameterList()`, `IRPMessage.setTimerValue(java.lang.String)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPMessage` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interactions.py`
- **Affected call(s):** get_condition() -> condition
- **Java signature(s):** `IRPMessage.getCondition()`, `IRPMessage.setCondition(java.lang.String)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPMessage` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interactions.py`
- **Affected call(s):** get_port() -> getPort; get_port() -> port; set_port() -> port; set_port() -> setPort
- **Java signature(s):** `IRPMessage.getPort()`, `IRPMessage.setPort(com.telelogic.rhapsody.core.IRPPort)`
- **Recommended change:** Use the Port property or a getter/setter fallback instead of calling getPort and port and setPort directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPMessage` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interactions.py`
- **Affected call(s):** set_actual_parameter_list() -> setActualParameterList
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
