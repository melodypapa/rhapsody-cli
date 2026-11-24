# Rhapsody API Validation: IRPClass

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPClass` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_class.py`)
- Members: Python `26`, Java `29`, pywin32 `24`
- Deviation items: `2` (actionable `0`, expected binding differences `2`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_event_reception_with_event() (no static COM member) | addEventReceptionWithEvent (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| update_contained_diagrams_on_server() (no static COM member) | updateContainedDiagramsOnServer (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

<details>
<summary>Correct items (23) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_class() -> addClass | addClass (method) | addClass (method) | MATCH | — |
| add_constructor() -> addConstructor | addConstructor (method) | addConstructor (method) | MATCH | — |
| add_destructor() -> addDestructor | addDestructor (method) | addDestructor (method) | MATCH | — |
| add_event_reception() -> addEventReception | addEventReception (method) | addEventReception (method) | MATCH | — |
| add_link() -> addLink | addLink (method) | addLink (method) | MATCH | — |
| add_link_to_part_via_port() -> addLinkToPartViaPort | addLinkToPartViaPort (method) | addLinkToPartViaPort (method) | MATCH | — |
| add_reception() -> addReception | addReception (method) | addReception (method) | MATCH | — |
| add_superclass() -> addSuperclass | addSuperclass (method) | addSuperclass (method) | MATCH | — |
| add_triggered_operation() -> addTriggeredOperation | addTriggeredOperation (method) | addTriggeredOperation (method) | MATCH | — |
| add_type() -> addType | addType (method) | addType (method) | MATCH | — |
| delete_class() -> deleteClass | deleteClass (method) | deleteClass (method) | MATCH | — |
| delete_constructor() -> deleteConstructor | deleteConstructor (method) | deleteConstructor (method) | MATCH | — |
| delete_destructor() -> deleteDestructor | deleteDestructor (method) | deleteDestructor (method) | MATCH | — |
| delete_event_reception() -> deleteEventReception | deleteEventReception (method) | deleteEventReception (method) | MATCH | — |
| delete_reception() -> deleteReception | deleteReception (method) | deleteReception (method) | MATCH | — |
| delete_superclass() -> deleteSuperclass | deleteSuperclass (method) | deleteSuperclass (method) | MATCH | — |
| delete_type() -> deleteType | deleteType (method) | deleteType (method) | MATCH | — |
| get_is_final() -> getIsFinal; set_is_final() -> setIsFinal | getIsFinal (method); setIsFinal (method) | getIsFinal (method); setIsFinal (method) | MATCH | — |
| is_abstract (property) -> isAbstract | getIsAbstract (method); setIsAbstract (method) | isAbstract (property) | MATCH | — |
| is_active (property) -> isActive | getIsActive (method); setIsActive (method) | isActive (property) | MATCH | — |
| is_behavior_overriden (property) -> isBehaviorOverriden | getIsBehaviorOverriden (method); setIsBehaviorOverriden (method) | isBehaviorOverriden (property) | MATCH | — |
| is_composite (property) -> isComposite | getIsComposite (method) | isComposite (property) | MATCH | — |
| is_reactive (property) -> isReactive | getIsReactive (method) | isReactive (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
