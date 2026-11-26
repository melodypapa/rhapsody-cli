# Rhapsody API Validation: IRPTableView

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPTableView` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`)
- Members: Python `17`, Java `17`, pywin32 `9`
- Deviation items: `13` (actionable `13`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_cell_elements() -> getCellElements | getCellElements (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_cell_string() -> getCellString | getCellString (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_column_count() -> columnCount; get_column_count() -> getColumnCount | getColumnCount (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_content() -> getContent | getContent (method) | GetContent (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_html_content() -> getHTMLContent; get_html_content() -> hTMLContent | getHTMLContent (method) | GetHTMLContent (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_image_collection() -> getImageCollection | getImageCollection (method) | GetImageCollection (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_include_descendants() -> includeDescendants; set_include_descendants() -> includeDescendants | getIncludeDescendants (method); setIncludeDescendants (method) | includeDescendants (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_its_table_layout() -> getItsTableLayout; set_its_table_layout() -> setItsTableLayout | getItsTableLayout (method); setItsTableLayout (method) | GetItsTableLayout (method); SetItsTableLayout (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_row_count() -> getRowCount; get_row_count() -> rowCount | getRowCount (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_scope() -> getScope; set_scope() -> setScope | getScope (method); setScope (method) | GetScope (method); SetScope (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| update_view_on_server() -> updateViewOnServer | updateViewOnServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_use_owner_scope() -> getUseOwnerScope; get_use_owner_scope() -> useOwnerScope; set_use_owner_scope() -> setUseOwnerScope; set_use_owner_scope() -> useOwnerScope | getUseOwnerScope (method); setUseOwnerScope (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| set_its_table_layout() -> setItsTableLayout | — | setItsTableLayout (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| open() -> open | open (method) | open (method) | MATCH | — |

</details>

## AI Fix Guidance

### PYWIN32_MEMBER_MISSING (6 findings)
- **Target:** `IRPTableView` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_cell_elements() -> getCellElements; get_cell_string() -> getCellString; get_column_count() -> columnCount; get_column_count() -> getColumnCount; get_row_count() -> getRowCount; get_row_count() -> rowCount; update_view_on_server() -> updateViewOnServer; get_use_owner_scope() -> getUseOwnerScope; get_use_owner_scope() -> useOwnerScope; set_use_owner_scope() -> setUseOwnerScope; set_use_owner_scope() -> useOwnerScope
- **Java signature(s):** `IRPTableView.setUseOwnerScope(int)`
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH (5 findings)
- **Target:** `IRPTableView` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_content() -> getContent; get_html_content() -> getHTMLContent; get_html_content() -> hTMLContent; get_image_collection() -> getImageCollection; get_its_table_layout() -> getItsTableLayout; set_its_table_layout() -> setItsTableLayout; get_scope() -> getScope; set_scope() -> setScope
- **Java signature(s):** `IRPTableView.setScope(com.telelogic.rhapsody.core.IRPCollection)`
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPTableView` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_include_descendants() -> includeDescendants; set_include_descendants() -> includeDescendants
- **Java signature(s):** `IRPTableView.getIncludeDescendants()`, `IRPTableView.setIncludeDescendants(int)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPTableView` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** set_its_table_layout() -> setItsTableLayout
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
