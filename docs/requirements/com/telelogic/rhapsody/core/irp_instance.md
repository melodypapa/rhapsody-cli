## SWR_ELEM_00009: IRPInstance Wrapper

**ID:** SWR_ELEM_00009
**Title:** IRPInstance wraps an instance/object in the Rhapsody model
**Status:** Implemented
**Priority:** Medium
**Description:**
The JavaDoc `IRPInstance` interface represents an instance in the model and extends `IRPRelation`. The Python wrapper shall extend `IRPRelation` and register for the meta classes `"Instance"` and `"Object"`. Method-shaped members (`get_attribute_value`, `set_attribute_value`, `get_in_links`, `get_out_links`, `add_relation_to_the_whole`, `get_list_of_initializer_arguments`, `set_explicit`, `set_implicit`, `set_initializer_argument_value`) bind exactly one pywin32 method. `instantiated_by` is the read/write Python property backed by the typelib property `instantiatedBy`. `get_all_nested_elements` and `update_contained_diagrams_on_server` are JavaDoc-only and raise `NotImplementedError` before any COM dispatch, because neither member is present in the registered IRPInstance typelib.
**Implementation:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_instance.py:IRPInstance` (canonical package; registration retained; no legacy `_get_method_or_property` helpers remain). Live note: the registered typelib exposes no member that creates an `IRPInstance` (`IRPPackage.addInstanceSpecification` is absent from pywin32), and the test project contains no instances. Populated live checks are therefore open (see the sync ledger). Objects returned to the wrapper expose the generic `IRPModelElement` interface; `win32com.client.CastTo(obj, "IRPInstance")` reaches the instance members, which the wrapper does not yet perform.
**Last Changed:** 2026-11-26
