# Rhapsody API Validation: IRPInternalOEMPlugin

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPInternalOEMPlugin` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`)
- Members: Python `14`, Java `14`, pywin32 `14`
- Deviation items: `15` (actionable `15`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| active_project_about_to_change() -> activeProjectAboutToChange | activeProjectAboutToChange (method) | ActiveProjectAboutToChange (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| active_project_has_changed() -> activeProjectHasChanged | activeProjectHasChanged (method) | ActiveProjectHasChanged (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| on_menu_item_select() -> onMenuItemSelect | onMenuItemSelect (method) | OnMenuItemSelect (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| on_menu_item_select_with_parameters() -> onMenuItemSelectWithParameters | onMenuItemSelectWithParameters (method) | OnMenuItemSelectWithParameters (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| rhap_plugin_animation_stopped() -> rhapPluginAnimationStopped | rhapPluginAnimationStopped (method) | RhapPluginAnimationStopped (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| rhp_plugin_animation_started() -> rhpPluginAnimationStarted | rhpPluginAnimationStarted (method) | RhpPluginAnimationStarted (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| rhp_plugin_cleanup() -> rhpPluginCleanup | rhpPluginCleanup (method) | RhpPluginCleanup (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| rhp_plugin_do_command() -> rhpPluginDoCommand | rhpPluginDoCommand (method) | RhpPluginDoCommand (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| rhp_plugin_final_cleanup() -> rhpPluginFinalCleanup | rhpPluginFinalCleanup (method) | RhpPluginFinalCleanup (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| rhp_plugin_init() -> rhpPluginInit | rhpPluginInit (method) | RhpPluginInit (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| rhp_plugin_invoke_item() -> rhpPluginInvokeItem | rhpPluginInvokeItem (method) | RhpPluginInvokeItem (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| rhp_plugin_on_ide_build_done() -> rhpPluginOnIDEBuildDone | rhpPluginOnIDEBuildDone (method) | RhpPluginOnIDEBuildDone (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| rhp_plugin_set_application() -> rhpPluginSetApplication | rhpPluginSetApplication (method) | RhpPluginSetApplication (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| rhp_saving_project() -> rhpSavingProject | rhpSavingProject (method) | RhpSavingProject (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| rhp_plugin_set_application() -> rhpPluginSetApplication | — | rhpPluginSetApplication (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH (14 findings)
- **Target:** `IRPInternalOEMPlugin` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** active_project_about_to_change() -> activeProjectAboutToChange; active_project_has_changed() -> activeProjectHasChanged; on_menu_item_select() -> onMenuItemSelect; on_menu_item_select_with_parameters() -> onMenuItemSelectWithParameters; rhap_plugin_animation_stopped() -> rhapPluginAnimationStopped; rhp_plugin_animation_started() -> rhpPluginAnimationStarted; rhp_plugin_cleanup() -> rhpPluginCleanup; rhp_plugin_do_command() -> rhpPluginDoCommand; rhp_plugin_final_cleanup() -> rhpPluginFinalCleanup; rhp_plugin_init() -> rhpPluginInit; rhp_plugin_invoke_item() -> rhpPluginInvokeItem; rhp_plugin_on_ide_build_done() -> rhpPluginOnIDEBuildDone; rhp_plugin_set_application() -> rhpPluginSetApplication; rhp_saving_project() -> rhpSavingProject
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPInternalOEMPlugin` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** rhp_plugin_set_application() -> rhpPluginSetApplication
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
