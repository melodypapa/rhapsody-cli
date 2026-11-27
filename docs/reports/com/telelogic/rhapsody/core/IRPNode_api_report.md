# Rhapsody API Validation: IRPNode

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPNode` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_node.py`)
- Members: Python `5`, Java `6`, pywin32 `5`
- Deviation items: `1` (actionable `1`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| cpu_type (property) -> CPUtype | getCPUtype (method); setCPUtype (method) | CPUtype (property) | PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

<details>
<summary>Correct items (4) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_component_instance() -> addComponentInstance | addComponentInstance (method) | addComponentInstance (method) | MATCH | — |
| component_instances (property) -> componentInstances | getComponentInstances (method) | componentInstances (property) | MATCH | — |
| delete_component_instance() -> deleteComponentInstance | deleteComponentInstance (method) | deleteComponentInstance (method) | MATCH | — |
| find_component_instance() -> findComponentInstance | findComponentInstance (method) | findComponentInstance (method) | MATCH | — |

</details>

## AI Fix Guidance

### PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPNode` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_node.py`
- **Affected call(s):** cpu_type (property) -> CPUtype
- **Java signature(s):** `IRPNode.getCPUtype()`, `IRPNode.setCPUtype(java.lang.String)`
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
