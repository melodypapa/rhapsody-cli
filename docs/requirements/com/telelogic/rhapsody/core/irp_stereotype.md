## SWR_ELEM_00037: IRPStereotype Wrapper

**ID:** SWR_ELEM_00037
**Title:** IRPStereotype represents stereotypes in Rhapsody models
**Status:** Implemented
**Priority:** Medium
**Description:**
The JavaDoc `IRPStereotype` interface represents stereotypes in Rhapsody models and extends `IRPClassifier`. The Python wrapper shall expose the owned methods `add_meta_class(meta_class)` and `remove_meta_class(meta_class)`, plus the catalog-shaped properties `icon`, `is_new_term`, and `of_meta_class`. The `is_new_term` property is read/write: its getter and setter map to the typelib property `isNewTerm` (the JavaDoc declares `getIsNewTerm()` and `setIsNewTerm(int)`). The `icon` and `of_meta_class` properties are read-only. Inherited classifier/unit/model-element members remain owned by their respective wrappers.
All COM calls use exactly one catalogued member: methods use `call_com`, and properties use `get_com_property` / `set_com_property`. The wrapper registers for meta class `"Stereotype"`.
**Implementation:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_stereotype.py:IRPStereotype` (canonical package; class registration retained; `isNewTerm` writable-property setter implemented instead of the prior unsupported stub).
**Last Changed:** 2026-11-25

---

## SWR_ELEM_00038: IRPStereotype icon getter populated fixture

**ID:** SWR_ELEM_00038
**Title:** IRPStereotype.icon has no documented live setup for a non-empty image path
**Status:** Blocked
**Priority:** Low
**Description:**
JavaDoc says `getIcon()` returns the full path of the image associated with the stereotype. The registered typelib exposes `icon` as a read-only property (no `PROPERTYPUT`), and JavaDoc defines no icon setter. A real stereotype created with the documented package `add_stereotype(name, "Package")` returns an empty icon path. The mirrored integration test records this empty-state observation, but it does not close the required populated getter fixture. A positive icon-path assertion remains blocked until a documented live API or authentic stereotype fixture with an assigned icon is available; no fabricated path or mocked COM value is substituted.
**Implementation:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_stereotype.py:IRPStereotype.icon`; `tests/integration/models/com/telelogic/rhapsody/core/test_irp_stereotype.py::test_icon_empty_for_stereotype_without_custom_icon`.
**Last Changed:** 2026-11-25
