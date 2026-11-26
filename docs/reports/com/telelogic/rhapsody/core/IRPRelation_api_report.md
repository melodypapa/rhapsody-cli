# Rhapsody API Validation: IRPRelation

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPRelation` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_relation.py`)
- Members: Python `31`, Java `31`, pywin32 `22`
- Deviation items: `13` (actionable `13`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_inverse() -> inverse; set_inverse() -> setInverse | getInverse (method); setInverse (method) | inverse (property); setInverse (method) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_is_navigable() -> isNavigable; set_is_navigable() -> isNavigable | getIsNavigable (method); setIsNavigable (method) | isNavigable (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_is_symmetric() -> isSymmetric | getIsSymmetric (method) | isSymmetric (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_multiplicity() -> multiplicity; set_multiplicity() -> multiplicity | getMultiplicity (method); setMultiplicity (method) | multiplicity (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_object_as_object_type() -> getObjectAsObjectType; get_object_as_object_type() -> objectAsObjectType | getObjectAsObjectType (method) | ObjectAsObjectType (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the ObjectAsObjectType property or a getter/setter fallback instead of calling getObjectAsObjectType and objectAsObjectType directly. |
| get_of_class() -> ofClass; set_of_class() -> ofClass | getOfClass (method); setOfClass (method) | ofClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_other_class() -> otherClass; set_other_class() -> otherClass | getOtherClass (method); setOtherClass (method) | otherClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_qualifier() -> qualifier; set_qualifier() -> qualifier | getQualifier (method); setQualifier (method) | qualifier (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_relation_label() -> relationLabel; set_relation_label() -> relationLabel | getRelationLabel (method); setRelationLabel (method) | relationLabel (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_relation_link_name() -> relationLinkName; set_relation_link_name() -> relationLinkName | getRelationLinkName (method); setRelationLinkName (method) | relationLinkName (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_relation_role_name() -> relationRoleName; set_relation_role_name() -> relationRoleName | getRelationRoleName (method); setRelationRoleName (method) | relationRoleName (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_relation_type() -> relationType; set_relation_type() -> relationType | getRelationType (method); setRelationType (method) | relationType (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_visibility() -> visibility | getVisibility (method) | visibility (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (7) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_qualifier() -> addQualifier | addQualifier (method) | addQualifier (method) | MATCH | — |
| get_association_class() -> getAssociationClass | getAssociationClass (method) | getAssociationClass (method) | MATCH | — |
| is_typeless_object() -> isTypelessObject | isTypelessObject (method) | isTypelessObject (method) | MATCH | — |
| make_unidirect() -> makeUnidirect | makeUnidirect (method) | makeUnidirect (method) | MATCH | — |
| get_qualifier_type() -> getQualifierType; set_qualifier_type() -> setQualifierType | getQualifierType (method); setQualifierType (method) | getQualifierType (method); setQualifierType (method) | MATCH | — |
| get_qualifiers() -> getQualifiers | getQualifiers (method) | getQualifiers (method) | MATCH | — |
| remove_qualifier() -> removeQualifier | removeQualifier (method) | removeQualifier (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (12 findings)
- **Target:** `IRPRelation` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_relation.py`
- **Affected call(s):** get_inverse() -> inverse; set_inverse() -> setInverse; get_is_navigable() -> isNavigable; set_is_navigable() -> isNavigable; get_is_symmetric() -> isSymmetric; get_multiplicity() -> multiplicity; set_multiplicity() -> multiplicity; get_of_class() -> ofClass; set_of_class() -> ofClass; get_other_class() -> otherClass; set_other_class() -> otherClass; get_qualifier() -> qualifier; set_qualifier() -> qualifier; get_relation_label() -> relationLabel; set_relation_label() -> relationLabel; get_relation_link_name() -> relationLinkName; set_relation_link_name() -> relationLinkName; get_relation_role_name() -> relationRoleName; set_relation_role_name() -> relationRoleName; get_relation_type() -> relationType; set_relation_type() -> relationType; get_visibility() -> visibility
- **Java signature(s):** `IRPRelation.getInverse()`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPRelation` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_relation.py`
- **Affected call(s):** get_object_as_object_type() -> getObjectAsObjectType; get_object_as_object_type() -> objectAsObjectType
- **Java signature(s):** `IRPRelation.getObjectAsObjectType()`
- **Recommended change:** Use the ObjectAsObjectType property or a getter/setter fallback instead of calling getObjectAsObjectType and objectAsObjectType directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
