# Rhapsody API Validation: IRPCollection

## Summary
- Target wrapper: `RPCollection` (`src/rhapsody_cli/models/core.py`)
- Members: Python `11`, Java `11`, pywin32 `13`
- Deviations: `9`
- Deviations by status:
  - `ACCESSOR_ALIAS_MISMATCH`: 2
  - `JAVA_ONLY_MEMBER`: 1
  - `METHOD_PROPERTY_MISMATCH`: 1
  - `PYTHON_ONLY_MEMBER`: 1
  - `PYWIN32_MEMBER_MISSING`: 1
  - `PYWIN32_ONLY_MEMBER`: 4

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | addGraphicalElementItem (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| add_graphical_item() -> addGraphicalItem | addGraphicalItem (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_count() -> Count; get_count() -> getCount | getCount (method) | Count (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | — | setGraphElement (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | — | interfaceName (property) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| get_item() -> Item; get_item() -> getItem | getItem (method) | Item (method) | ACCESSOR_ALIAS_MISMATCH | Review the related API spellings and document the intended mapping. |
| — | — | Items (property) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| to_list() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| — | toList (method) | — | JAVA_ONLY_MEMBER | Verify the Java documentation against the installed COM type library. |

## AI Fix Guidance

### Finding 1: PYWIN32_ONLY_MEMBER
- **Target:** `RPCollection` in `src/rhapsody_cli/models/core.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** addGraphicalElementItem (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 2: PYWIN32_MEMBER_MISSING
- **Target:** `RPCollection` in `src/rhapsody_cli/models/core.py`
- **Current Python wrapper/COM call:** add_graphical_item() -> addGraphicalItem
- **Expected Python method(s):** `add_graphical_item`
- **Java signature(s):** `IRPCollection.addGraphicalItem(com.telelogic.rhapsody.core.IRPGraphElement)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 3: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPCollection` in `src/rhapsody_cli/models/core.py`
- **Current Python wrapper/COM call:** get_count() -> Count; get_count() -> getCount
- **Expected Python method(s):** `get_count`
- **Java signature(s):** `IRPCollection.getCount()`
- **pywin32 member(s):** Count (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 4: PYWIN32_ONLY_MEMBER
- **Target:** `RPCollection` in `src/rhapsody_cli/models/core.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** setGraphElement (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 5: PYWIN32_ONLY_MEMBER
- **Target:** `RPCollection` in `src/rhapsody_cli/models/core.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** interfaceName (property)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 6: ACCESSOR_ALIAS_MISMATCH
- **Target:** `RPCollection` in `src/rhapsody_cli/models/core.py`
- **Current Python wrapper/COM call:** get_item() -> Item; get_item() -> getItem
- **Expected Python method(s):** `get_item`
- **Java signature(s):** `IRPCollection.getItem(int)`
- **pywin32 member(s):** Item (method)
- **Recommended change:** Review the related API spellings and document the intended mapping.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 7: PYWIN32_ONLY_MEMBER
- **Target:** `RPCollection` in `src/rhapsody_cli/models/core.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** Items (property)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 8: PYTHON_ONLY_MEMBER
- **Target:** `RPCollection` in `src/rhapsody_cli/models/core.py`
- **Current Python wrapper/COM call:** to_list() (no static COM member)
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 9: JAVA_ONLY_MEMBER
- **Target:** `RPCollection` in `src/rhapsody_cli/models/core.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `to_list`
- **Java signature(s):** `IRPCollection.toList()`
- **pywin32 member(s):** —
- **Recommended change:** Verify the Java documentation against the installed COM type library.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
