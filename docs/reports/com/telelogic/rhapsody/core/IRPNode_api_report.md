# Rhapsody API Validation: IRPNode

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPNode` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_node.py`)
- Members: Python `6`, Java `6`, pywin32 `5`
- Deviation items: `3` (actionable `3`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_cpu_type() -> CPUtype; set_cpu_type() -> CPUtype | getCPUtype (method); setCPUtype (method) | CPUtype (property) | PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_component_instances() -> getComponentInstances | getComponentInstances (method) | componentInstances (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the componentInstances property or a getter/setter fallback instead of calling getComponentInstances directly. |
| delete_component_instance() -> deleteComponentInstance | — | deleteComponentInstance (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['str']. Match the documented COM parameter types. |

<details>
<summary>Correct items (3) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_component_instance() -> addComponentInstance | addComponentInstance (method) | addComponentInstance (method) | MATCH | — |
| delete_component_instance() -> deleteComponentInstance | deleteComponentInstance (method) | deleteComponentInstance (method) | MATCH | — |
| find_component_instance() -> findComponentInstance | findComponentInstance (method) | findComponentInstance (method) | MATCH | — |

</details>

## AI Fix Guidance

### PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPNode` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_node.py`
- **Affected call(s):** get_cpu_type() -> CPUtype; set_cpu_type() -> CPUtype
- **Java signature(s):** `IRPNode.getCPUtype()`, `IRPNode.setCPUtype(java.lang.String)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPNode` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_node.py`
- **Affected call(s):** get_component_instances() -> getComponentInstances
- **Java signature(s):** `IRPNode.getComponentInstances()`
- **Recommended change:** Use the componentInstances property or a getter/setter fallback instead of calling getComponentInstances directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPNode` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_node.py`
- **Affected call(s):** delete_component_instance() -> deleteComponentInstance
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['str']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
