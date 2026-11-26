# Rhapsody API Validation: IRPDiagSynthAPI

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPDiagSynthAPI` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`)
- Members: Python `7`, Java `8`, pywin32 `8`
- Deviation items: `13` (actionable `13`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_instance() -> addInstance | addInstance (method) | AddInstance (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| add_synth_sd_to_model2() -> addSynthSDToModel2 | addSynthSDToModel2 (method) | AddSynthSDToModel2 (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| create_sd2() -> createSD2 | createSD2 (method) | CreateSD2 (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |
| receive_message() -> receiveMessage | receiveMessage (method) | ReceiveMessage (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| remove_synth_sd_to_model2() -> removeSynthSDToModel2 | removeSynthSDToModel2 (method) | RemoveSynthSDToModel2 (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| s_d_add_condition_mark() -> sDAddConditionMark | sDAddConditionMark (method) | SDAddConditionMark (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| send_message() -> sendMessage | sendMessage (method) | SendMessage (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| add_instance() -> addInstance | — | addInstance (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['int', 'str'] but pywin32 declares ['object', 'str']. Match the documented COM parameter types. |
| add_synth_sd_to_model2() -> addSynthSDToModel2 | — | addSynthSDToModel2 (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object', 'int', 'int'] but pywin32 declares ['com', 'object', 'int']. Match the documented COM parameter types. |
| create_sd2() -> createSD2 | — | createSD2 (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object', 'str'] but pywin32 declares ['com', 'str']. Match the documented COM parameter types. |
| receive_message() -> receiveMessage | — | receiveMessage (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['int', 'int'] but pywin32 declares ['object', 'object']. Match the documented COM parameter types. |
| remove_synth_sd_to_model2() -> removeSynthSDToModel2 | — | removeSynthSDToModel2 (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH (7 findings)
- **Target:** `IRPDiagSynthAPI` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`
- **Affected call(s):** add_instance() -> addInstance; add_synth_sd_to_model2() -> addSynthSDToModel2; create_sd2() -> createSD2; receive_message() -> receiveMessage; remove_synth_sd_to_model2() -> removeSynthSDToModel2; s_d_add_condition_mark() -> sDAddConditionMark; send_message() -> sendMessage
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPDiagSynthAPI` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`
- **Affected call(s):** —
- **Java signature(s):** `IRPDiagSynthAPI.getInterfaceName()`
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (5 findings)
- **Target:** `IRPDiagSynthAPI` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`
- **Affected call(s):** add_instance() -> addInstance; add_synth_sd_to_model2() -> addSynthSDToModel2; create_sd2() -> createSD2; receive_message() -> receiveMessage; remove_synth_sd_to_model2() -> removeSynthSDToModel2
- **Recommended change:** Wrapper passes types ['int', 'str'] but pywin32 declares ['object', 'str']. Match the documented COM parameter types.
- **Recommended change:** Wrapper passes types ['object', 'int', 'int'] but pywin32 declares ['com', 'object', 'int']. Match the documented COM parameter types.
- **Recommended change:** Wrapper passes types ['object', 'str'] but pywin32 declares ['com', 'str']. Match the documented COM parameter types.
- **Recommended change:** Wrapper passes types ['int', 'int'] but pywin32 declares ['object', 'object']. Match the documented COM parameter types.
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
