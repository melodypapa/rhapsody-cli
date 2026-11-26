# Rhapsody API Validation: IRPGraphNode

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPGraphNode` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`)
- Members: Python `7`, Java `7`, pywin32 `6`
- Deviation items: `2` (actionable `2`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_is_panel_widget() -> isPanelWidget | getIsPanelWidget (method) | isPanelWidget (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_panel_widget_instance_path() -> getPanelWidgetInstancePath; set_panel_widget_instance_path() -> setPanelWidgetInstancePath | getPanelWidgetInstancePath (method); setPanelWidgetInstancePath (method) | panelWidgetInstancePath (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the panelWidgetInstancePath property or a getter/setter fallback instead of calling getPanelWidgetInstancePath and setPanelWidgetInstancePath directly. |

<details>
<summary>Correct items (4) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| bring_to_front() -> bringToFront | bringToFront (method) | bringToFront (method) | MATCH | — |
| hide_all_ports() -> hideAllPorts | hideAllPorts (method) | hideAllPorts (method) | MATCH | — |
| send_to_back() -> sendToBack | sendToBack (method) | sendToBack (method) | MATCH | — |
| show_all_ports() -> showAllPorts | showAllPorts (method) | showAllPorts (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPGraphNode` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_is_panel_widget() -> isPanelWidget
- **Java signature(s):** `IRPGraphNode.getIsPanelWidget()`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPGraphNode` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_panel_widget_instance_path() -> getPanelWidgetInstancePath; set_panel_widget_instance_path() -> setPanelWidgetInstancePath
- **Java signature(s):** `IRPGraphNode.getPanelWidgetInstancePath()`, `IRPGraphNode.setPanelWidgetInstancePath(com.telelogic.rhapsody.core.IRPCollection)`
- **Recommended change:** Use the panelWidgetInstancePath property or a getter/setter fallback instead of calling getPanelWidgetInstancePath and setPanelWidgetInstancePath directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
