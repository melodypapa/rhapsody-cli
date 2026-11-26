# Rhapsody API Validation: IRPMatrixLayout

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPMatrixLayout` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`)
- Members: Python `14`, Java `14`, pywin32 `14`
- Deviation items: `9` (actionable `9`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_cell_element_types() -> getCellElementTypes; set_cell_element_types() -> setCellElementTypes | getCellElementTypes (method); setCellElementTypes (method) | GetCellElementTypes (method); SetCellElementTypes (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_from_element_types() -> getFromElementTypes; set_from_element_types() -> setFromElementTypes | getFromElementTypes (method); setFromElementTypes (method) | GetFromElementTypes (method); SetFromElementTypes (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_from_element_types_query_to_use() -> getFromElementTypesQueryToUse; set_from_element_types_query_to_use() -> setFromElementTypesQueryToUse | getFromElementTypesQueryToUse (method); setFromElementTypesQueryToUse (method) | GetFromElementTypesQueryToUse (method); SetFromElementTypesQueryToUse (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_from_element_types_use_query_or_elements_list() -> getFromElementTypesUseQueryOrElementsList; set_from_element_types_use_query_or_elements_list() -> setFromElementTypesUseQueryOrElementsList | getFromElementTypesUseQueryOrElementsList (method); setFromElementTypesUseQueryOrElementsList (method) | GetFromElementTypesUseQueryOrElementsList (method); SetFromElementTypesUseQueryOrElementsList (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_to_element_types() -> getToElementTypes; set_to_element_types() -> setToElementTypes | getToElementTypes (method); setToElementTypes (method) | GetToElementTypes (method); SetToElementTypes (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_to_element_types_query_to_use() -> getToElementTypesQueryToUse; set_to_element_types_query_to_use() -> setToElementTypesQueryToUse | getToElementTypesQueryToUse (method); setToElementTypesQueryToUse (method) | GetToElementTypesQueryToUse (method); SetToElementTypesQueryToUse (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_to_element_types_use_query_or_elements_list() -> getToElementTypesUseQueryOrElementsList; set_to_element_types_use_query_or_elements_list() -> setToElementTypesUseQueryOrElementsList | getToElementTypesUseQueryOrElementsList (method); setToElementTypesUseQueryOrElementsList (method) | GetToElementTypesUseQueryOrElementsList (method); SetToElementTypesUseQueryOrElementsList (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| set_from_element_types_query_to_use() -> setFromElementTypesQueryToUse | — | setFromElementTypesQueryToUse (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| set_to_element_types_query_to_use() -> setToElementTypesQueryToUse | — | setToElementTypesQueryToUse (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH (7 findings)
- **Target:** `IRPMatrixLayout` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_cell_element_types() -> getCellElementTypes; set_cell_element_types() -> setCellElementTypes; get_from_element_types() -> getFromElementTypes; set_from_element_types() -> setFromElementTypes; get_from_element_types_query_to_use() -> getFromElementTypesQueryToUse; set_from_element_types_query_to_use() -> setFromElementTypesQueryToUse; get_from_element_types_use_query_or_elements_list() -> getFromElementTypesUseQueryOrElementsList; set_from_element_types_use_query_or_elements_list() -> setFromElementTypesUseQueryOrElementsList; get_to_element_types() -> getToElementTypes; set_to_element_types() -> setToElementTypes; get_to_element_types_query_to_use() -> getToElementTypesQueryToUse; set_to_element_types_query_to_use() -> setToElementTypesQueryToUse; get_to_element_types_use_query_or_elements_list() -> getToElementTypesUseQueryOrElementsList; set_to_element_types_use_query_or_elements_list() -> setToElementTypesUseQueryOrElementsList
- **Java signature(s):** `IRPMatrixLayout.getCellElementTypes()`, `IRPMatrixLayout.setToElementTypesUseQueryOrElementsList(int)`
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (2 findings)
- **Target:** `IRPMatrixLayout` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** set_from_element_types_query_to_use() -> setFromElementTypesQueryToUse; set_to_element_types_query_to_use() -> setToElementTypesQueryToUse
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
