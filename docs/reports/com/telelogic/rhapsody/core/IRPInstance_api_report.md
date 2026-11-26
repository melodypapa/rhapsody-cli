# Rhapsody API Validation: IRPInstance

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPInstance` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_instance.py`)
- Members: Python `12`, Java `13`, pywin32 `10`
- Deviation items: `2` (actionable `0`, expected binding differences `2`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | PASS | No change needed. |

<details>
<summary>Correct items (9) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_relation_to_the_whole() -> addRelationToTheWhole | addRelationToTheWhole (method) | addRelationToTheWhole (method) | MATCH | — |
| get_attribute_value() -> getAttributeValue; set_attribute_value() -> setAttributeValue | getAttributeValue (method); setAttributeValue (method) | getAttributeValue (method); setAttributeValue (method) | MATCH | — |
| set_explicit() -> setExplicit | setExplicit (method) | setExplicit (method) | MATCH | — |
| set_implicit() -> setImplicit | setImplicit (method) | setImplicit (method) | MATCH | — |
| get_in_links() -> getInLinks | getInLinks (method) | getInLinks (method) | MATCH | — |
| set_initializer_argument_value() -> setInitializerArgumentValue | setInitializerArgumentValue (method) | setInitializerArgumentValue (method) | MATCH | — |
| instantiated_by (property) -> instantiatedBy | getInstantiatedBy (method); setInstantiatedBy (method) | instantiatedBy (property) | MATCH | — |
| get_list_of_initializer_arguments() -> getListOfInitializerArguments | getListOfInitializerArguments (method) | getListOfInitializerArguments (method) | MATCH | — |
| get_out_links() -> getOutLinks | getOutLinks (method) | getOutLinks (method) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
