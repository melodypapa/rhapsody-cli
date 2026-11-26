## SWR_ELEM_00039: IRPRelation Wrapper

**ID:** SWR_ELEM_00039
**Title:** IRPRelation wraps the base relationship interface between classifiers
**Status:** Implemented
**Priority:** Medium
**Description:**
The JavaDoc `IRPRelation` interface is the base for relationships between classifiers (associations and the instance links derived from them) and extends `IRPUnit`. The Python wrapper shall expose the accessor families that the typelib declares as properties as Python `@property` members, with setters only where the JavaDoc declares a setter: `inverse` (read), `is_navigable` (read/write), `is_symmetric` (read), `multiplicity` (read/write), `object_as_object_type` (read), `of_class` (read/write), `other_class` (read/write), `qualifier` (read/write), `relation_label` (read/write), `relation_link_name` (read/write), `relation_role_name` (read/write), `relation_type` (read/write), and `visibility` (read). Method-shaped members (`add_qualifier`, `remove_qualifier`, `get_association_class`, `get_qualifiers`, `get_qualifier_type`, `set_qualifier_type`, `set_inverse`, `is_typeless_object`, `make_unidirect`) bind exactly one pywin32 method. `inverse` is constructed as `IRPRelation` directly because association ends carry the `AssociationEnd` meta class, which has no registered wrapper. `get_association_class` and `inverse` return `None` when the COM value is absent.
**Implementation:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_relation.py:IRPRelation` (canonical package; legacy `_get_method_or_property` helpers removed; exchange exporter and importer read and write the properties). Live limitations: `object_as_object_type` returns `None` for association ends and needs an object-typed relation; `qualifier` accepts a write, but the read-back stays empty, so the populated round trip is not yet proven.
**Last Changed:** 2026-11-26
