## SWR_CORE_00003: IRPClassifier Shared Base

**ID:** SWR_CORE_00003
**Title:** IRPClassifier wraps IRPClassifier, the shared base of Class/Actor/UseCase
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPClassifier` JavaDoc interface represents the shared base for classifiable
elements. The Python `IRPClassifier` shall extend `IRPUnit` and expose Java-mirrored
members: creation/deletion (`add_attribute`, `delete_attribute`, `add_operation`,
`delete_operation`, `add_relation`, `add_relation_to`, `delete_relation`,
`add_generalization`, `delete_generalization`, `add_statechart`, `add_activity_diagram`,
`add_flow_items`, `add_flows`), lookup (`find_attribute`, `find_operation`,
`find_generalization`, `find_relation`, `find_interface_item`, `find_trigger`,
`find_nested_classifier`, `find_base_classifier`, `find_derived_classifier`), and
collection getters (`get_attributes`, `get_operations`, `get_relations`,
`get_generalizations`, `get_interface_items`, `get_ports`, `get_nested_classifiers`,
`get_flows`, `get_flow_items`, `get_links`, `get_source_artifacts`,
`get_behavioral_diagrams`, `get_sequence_diagrams`, `get_activity_diagram`,
`get_statechart`).
Every COM call shall target exactly one pywin32-exposed member from
`docs/reports/pywin32_authority.json`, with no runtime name probing or Java-name
fallback. The three JavaDoc method-shaped getters (`getAttributesIncludingBases`,
`getInterfaceItemsIncludingBases`, `getRelationsIncludingBases`) are invoked via
`call_com`; the remaining getters are pywin32 **properties** and are read via
`get_com_property` using the exact catalogued name (for example `attributes`,
`operations`, `relations`, `ports`, `statechart`) while keeping the Python-facing
`get_*` method names. `add_port()` calls the pywin32 `addNewAggr` method directly;
this member is absent from the JavaDoc and is recorded as a `JAVA_DOC_MISSING`
deviation in the API report. The module uses `from __future__ import annotations`
with unquoted type references; names used only in `cast()` are imported locally
inside the method to avoid circular imports.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_classifier.py:IRPClassifier
(class renamed from `RPClassifier`; §2 canonical package move completed; 20 legacy
dual-binding call sites migrated to single pywin32 members)
**Last Changed:** 2026-11-22
