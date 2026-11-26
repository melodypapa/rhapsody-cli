# Rhapsody API Validation: IRPRelation

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPRelation` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_relation.py`)
- Members: Python `22`, Java `31`, pywin32 `22`
- Deviation items: `0` (actionable `0`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | PASS | No change needed. |

<details>
<summary>Correct items (20) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_qualifier() -> addQualifier | addQualifier (method) | addQualifier (method) | MATCH | — |
| get_association_class() -> getAssociationClass | getAssociationClass (method) | getAssociationClass (method) | MATCH | — |
| inverse (property) -> inverse; set_inverse() -> setInverse | getInverse (method); setInverse (method) | inverse (property); setInverse (method) | MATCH | — |
| is_navigable (property) -> isNavigable | getIsNavigable (method); setIsNavigable (method) | isNavigable (property) | MATCH | — |
| is_symmetric (property) -> isSymmetric | getIsSymmetric (method) | isSymmetric (property) | MATCH | — |
| is_typeless_object() -> isTypelessObject | isTypelessObject (method) | isTypelessObject (method) | MATCH | — |
| make_unidirect() -> makeUnidirect | makeUnidirect (method) | makeUnidirect (method) | MATCH | — |
| multiplicity (property) -> multiplicity | getMultiplicity (method); setMultiplicity (method) | multiplicity (property) | MATCH | — |
| object_as_object_type (property) -> ObjectAsObjectType | getObjectAsObjectType (method) | ObjectAsObjectType (property) | MATCH | — |
| of_class (property) -> ofClass | getOfClass (method); setOfClass (method) | ofClass (property) | MATCH | — |
| other_class (property) -> otherClass | getOtherClass (method); setOtherClass (method) | otherClass (property) | MATCH | — |
| qualifier (property) -> qualifier | getQualifier (method); setQualifier (method) | qualifier (property) | MATCH | — |
| get_qualifier_type() -> getQualifierType; set_qualifier_type() -> setQualifierType | getQualifierType (method); setQualifierType (method) | getQualifierType (method); setQualifierType (method) | MATCH | — |
| get_qualifiers() -> getQualifiers | getQualifiers (method) | getQualifiers (method) | MATCH | — |
| relation_label (property) -> relationLabel | getRelationLabel (method); setRelationLabel (method) | relationLabel (property) | MATCH | — |
| relation_link_name (property) -> relationLinkName | getRelationLinkName (method); setRelationLinkName (method) | relationLinkName (property) | MATCH | — |
| relation_role_name (property) -> relationRoleName | getRelationRoleName (method); setRelationRoleName (method) | relationRoleName (property) | MATCH | — |
| relation_type (property) -> relationType | getRelationType (method); setRelationType (method) | relationType (property) | MATCH | — |
| remove_qualifier() -> removeQualifier | removeQualifier (method) | removeQualifier (method) | MATCH | — |
| visibility (property) -> visibility | getVisibility (method) | visibility (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
