# Rhapsody API Validation: IRPMatrixView

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPMatrixView` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`)
- Members: Python `19`, Java `19`, pywin32 `12`
- Deviation items: `14` (actionable `14`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_cell_elements() -> getCellElements | getCellElements (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_cell_string() -> getCellString | getCellString (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_column_count() -> columnCount; get_column_count() -> getColumnCount | getColumnCount (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_content() -> getContent | getContent (method) | GetContent (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_from_scope() -> getFromScope; set_from_scope() -> setFromScope | getFromScope (method); setFromScope (method) | GetFromScope (method); SetFromScope (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_html_content() -> getHTMLContent; get_html_content() -> hTMLContent | getHTMLContent (method) | GetHTMLContent (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_image_collection() -> getImageCollection | getImageCollection (method) | GetImageCollection (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_include_descendants_from_scope() -> includeDescendantsFromScope; set_include_descendants_from_scope() -> includeDescendantsFromScope | getIncludeDescendantsFromScope (method); setIncludeDescendantsFromScope (method) | includeDescendantsFromScope (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_include_descendants_to_scope() -> includeDescendantsToScope; set_include_descendants_to_scope() -> includeDescendantsToScope | getIncludeDescendantsToScope (method); setIncludeDescendantsToScope (method) | includeDescendantsToScope (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_its_matrix_layout() -> getItsMatrixLayout; set_its_matrix_layout() -> setItsMatrixLayout | getItsMatrixLayout (method); setItsMatrixLayout (method) | GetItsMatrixLayout (method); SetItsMatrixLayout (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_row_count() -> getRowCount; get_row_count() -> rowCount | getRowCount (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_to_scope() -> getToScope; set_to_scope() -> setToScope | getToScope (method); setToScope (method) | GetToScope (method); SetToScope (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| update_view_on_server() -> updateViewOnServer | updateViewOnServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| set_its_matrix_layout() -> setItsMatrixLayout | — | setItsMatrixLayout (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| open() -> open | open (method) | open (method) | MATCH | — |

</details>

## AI Fix Guidance

### PYWIN32_MEMBER_MISSING (5 findings)
- **Target:** `IRPMatrixView` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_cell_elements() -> getCellElements; get_cell_string() -> getCellString; get_column_count() -> columnCount; get_column_count() -> getColumnCount; get_row_count() -> getRowCount; get_row_count() -> rowCount; update_view_on_server() -> updateViewOnServer
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH (6 findings)
- **Target:** `IRPMatrixView` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_content() -> getContent; get_from_scope() -> getFromScope; set_from_scope() -> setFromScope; get_html_content() -> getHTMLContent; get_html_content() -> hTMLContent; get_image_collection() -> getImageCollection; get_its_matrix_layout() -> getItsMatrixLayout; set_its_matrix_layout() -> setItsMatrixLayout; get_to_scope() -> getToScope; set_to_scope() -> setToScope
- **Java signature(s):** `IRPMatrixView.setToScope(com.telelogic.rhapsody.core.IRPCollection)`
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPMatrixView` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_include_descendants_from_scope() -> includeDescendantsFromScope; set_include_descendants_from_scope() -> includeDescendantsFromScope; get_include_descendants_to_scope() -> includeDescendantsToScope; set_include_descendants_to_scope() -> includeDescendantsToScope
- **Java signature(s):** `IRPMatrixView.getIncludeDescendantsFromScope()`, `IRPMatrixView.setIncludeDescendantsToScope(int)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPMatrixView` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** set_its_matrix_layout() -> setItsMatrixLayout
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
