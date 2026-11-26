## SWR_ELEM_00050: IRPClassifierRole Wrapper

**ID:** SWR_ELEM_00050
**Title:** IRPClassifierRole exposes realized classifier, instance, referenced diagram, and role type through the pywin32 contract
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPClassifierRole` JavaDoc interface represents lifelines in sequence
diagrams and objects in communication diagrams. The Python `IRPClassifierRole`
shall extend `IRPModelElement`, register itself for meta class
`"ClassifierRole"`, and expose the classifier or instance it realizes, its
referenced sequence diagram, and its role type.

Pywin32 exposes four JavaDoc accessor pairs as properties (`formalClassifier`,
`formalInstance`, `referencedSequenceDiagram`, `roleType`); the first three are
read/write and `roleType` is read-only. `get_referencing_classifier_roles_recursively`
remains a method-shaped `call_com` binding. The module uses
`from __future__ import annotations` with unquoted type references and local
imports for names used only in `cast()`.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_classifier_role.py`;
the class was split out of the shared `irp_other_model.py` module in its own
sync run. With this split the empty `irp_other_model.py` shim was removed.
Unit tests in the mirrored unit path use only fake COM objects and give 100%
statement/branch coverage of the wrapper. Integration tests in the mirrored
integration path create real lifelines through `IRPCollaboration.add_classifier_role`
and assert populated getter values by identity/value, deleting the owning
package during cleanup. Live assertions are CI-only on Windows and are
unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_classifier_role.py:IRPClassifierRole
**Last Changed:** 2026-11-27
