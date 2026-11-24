# Sync todo: Group-unfinished-14 (finished-class current-rule remediation)

Baseline after merging origin/main at 258468d: unit suite 2121 passed; the full integration suite run with --rhapsody-hidden-ui completed 480 passed, 32 failed. The project-switch fixture regression reproducer passes, as do the seven focused CLI/application/model integration tests. IRPApplication.test_build_entire_project passes with the per-test hidden-UI guard. The 32 remaining live failures are recorded in docs/superpowers/plans/2026-11-23-finished-class-sync-remediation.md; target-interface failures remain open until their own runs. One failure in the legacy test_model_requirements.py is outside this batch.

This batch contains 15 remediation rows. IRPApplication remains in its existing open row in Group-unfinished-1.md; do not duplicate or archive that row here. Each interface run publishes its complete member-level sync TODO before analysis or edits. For every owned getter, the TODO includes the Getter fixture matrix required by the rhapsody-sync skill Section 1: real parent/child, JavaDoc-verified setup, getter result identity/value assertion, test path, and cleanup.

## Shared steps

1. Publish one-interface Sections 1-8 checklist with a subtask for every owned JavaDoc member and a Getter fixture matrix row for every getter.
2. Verify JavaDoc package, canonical wrapper/test/doc paths, exports, and inherited-member ownership.
3. Run `validate_interface.py INTERFACE --source authority`; reconcile JavaDoc, current pywin32 catalog/signatures, wrapper shape and result wrapping.
4. Write failing fake-COM tests first; implement; run the focused unit file at 100% statement and branch coverage and the full unit suite.
5. Create/relate real live data for each model-backed getter; replace disallowed exception assertions; run the focused live file. Keep blockers open.
6. Refresh the generated API report, requirement page, and RST API reference; add the RST toctree entry only if missing.
7. Run `verify_sync.py INTERFACE`, skill harness tests, relevant quality gates, and focused live integration.
8. Record measured unit coverage, live result, permitted NotImplementedError assertions, and blockers. Regenerate reports with the validator; never hand-edit them.

## Remediation rows

- [ ] irp_model_element_remediation - IRPModelElement
  - Baseline before this remediation: getErrorMessage call arity 0 to 1; 22 disallowed integration exception assertions; 32 COM properties used method shape; Java getStereotype/setStereotype mapped to the missing read/write COM property stereotype. The invalid `set_ti` and `set_main_diagram` cases were already replaced with real relationship roundtrips.
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, exports, and inherited-member scope verified.
  - [ ] Section 3 arity, property shape, stereotype member, and every owned member reconciled against JavaDoc/catalog.
  - [x] Section 4 fake-COM tests first; full unit suite green; irp_model_element.py at 100% statements/branches. Evidence: focused unit file 154 passed; coverage 308 statements/136 branches, 100.00%; full unit suite 2124 passed; mypy found no issues in 274 files.
  - [ ] Section 5 populated getter matrix and live assertions complete; final live result or blockers recorded. Evidence: post-fix focused live run (hidden UI, no dialogs interacted with): **103 passed, 0 failed**. The remaining populated-assertion gaps are constraints / constraints_by_him (empty-state collection reads only), local_tags (type-only), and hyper_links (empty-state). Live blockers recorded after systematic probes: `add_remote_dependency_to` needs an external Design Manager remote-requirements fixture; `set_description_and_hyperlinks` faults E_INVALIDARG for every documented input form (minimal and canonical RTF, empty and populated app collections), so its live positive test was removed pending a typelib-level investigation; the GUID property put silently resets the GUID to a placeholder (destructive, unsupported live) so the write roundtrip was removed; `add_link_to_element` faults E_FAIL with null ports even though JavaDoc documents them, and `addRedefines` only works at feature level, so the live test was rewritten to redefine an attribute against its inherited base after a generalization. `high_light_element` / `open_features_dialog` remain mock-based due to their modal UI.
  - [x] Section 6 irp_model_element.md checked/updated. Evidence: requirement page rewritten for the property surface, get_error_message MIDL buffer, add_link_to_element None-ports contract, and documented-unavailable get_rmm_url.
  - [x] Section 7 irp_model_element.rst checked/updated for every public member. Evidence: RST regenerated with 33 autoattribute and 70 automethod directives; verify_sync.py exits 0.
  - [x] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded. Evidence: validate_interface.py exits 0 (report regenerated with 0 actionable deviations); verify_sync.py exits 0; skill harness 31 passed; ruff/black/mypy clean; full unit suite 2124 passed; focused live file 103 passed / 0 failed with hidden UI. Remaining open items are the §5 getter-matrix gaps and the unrelated full-suite integration baseline.

- [ ] irp_package_remediation - IRPPackage
  - Baseline: 8 arity mismatches; 8 disallowed integration exception assertions; 30 property-shape conversions; add_association is a COM-only extension (D2 default: retain and document).
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, exports, and inherited-member scope verified.
  - [ ] Section 3 all 8 signatures, 30 property members, and add_association disposition reconciled.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_package.py at 100% statements/branches.
  - [ ] Section 5 each package getter has a populated related child and identity assertion; all 8 exception sites resolved or blocked.
  - [ ] Section 6 irp_package.md checked/updated.
  - [ ] Section 7 irp_package.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_project_remediation - IRPProject
  - Baseline: 21 arity mismatches; 24 disallowed integration exception assertions; 9 read-only and 1 writable property-shape conversions; 7 COM-only extensions (D2 default: retain and document).
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, exports, and inherited-member scope verified.
  - [ ] Section 3 all 21 signatures, 9 read properties plus the writable property, and 7 extension dispositions reconciled.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_project.py at 100% statements/branches.
  - [ ] Section 5 project getters establish live project state and assert returned identity/value; all 24 exception sites resolved or blocked.
  - [ ] Section 6 irp_project.md checked/updated.
  - [ ] Section 7 irp_project.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_classifier_remediation - IRPClassifier
  - Baseline: 17 property-shape conversions; add_port maps to COM addNewAggr absent from JavaDoc (D2 default: retain and document).
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, exports, and inherited-member scope verified.
  - [ ] Section 3 all 17 property members and add_port disposition reconciled.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_classifier.py at 100% statements/branches.
  - [ ] Section 5 each collection getter creates its target attribute/operation/port/diagram/relationship and asserts membership/identity.
  - [ ] Section 6 irp_classifier.md checked/updated.
  - [ ] Section 7 irp_classifier.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_collection_remediation - IRPCollection
  - Baseline: COM Count property is exposed as get_count; integration test asserts forbidden IndexError for a negative index.
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 COM property/method shape and collection index contract reconciled.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_collection.py at 100% statements/branches.
  - [ ] Section 5 populated collection getter test asserts the created item/count; negative-index behavior stays unit-tested.
  - [ ] Section 6 irp_collection.md checked/updated.
  - [ ] Section 7 irp_collection.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_association_class_remediation - IRPAssociationClass
  - Baseline: end1, end2, and is_class are property-shaped; integration test asserts AttributeError on a regular association; test docstring contains stale xfail text.
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 establish whether a real AssociationClass can be created through documented live APIs.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_association_class.py at 100% statements/branches.
  - [ ] Section 5 assert both ends and class flag on a real AssociationClass, or leave a user-approved blocker open; remove stale xfail claim.
  - [ ] Section 6 irp_association_class.md checked/updated.
  - [ ] Section 7 irp_association_class.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_operation_remediation - IRPOperation
  - Baseline: 15 property-shaped members; integration test asserts AttributeError for get_flowchart.
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 all 15 properties and the get_flowchart/catalog disposition reconciled.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_operation.py at 100% statements/branches.
  - [ ] Section 5 create a real operation/flowchart fixture and assert live outcome, or document the verified unavailable-member stub.
  - [ ] Section 6 irp_operation.md checked/updated.
  - [ ] Section 7 irp_operation.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_class_remediation - IRPClass
  - Baseline: property shape already conforms; 2 integration tests assert RhapsodyRuntimeException.
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 resolve both failing members against JavaDoc and pywin32 signatures.
  - [ ] Section 4 full unit suite green; irp_class.py at 100% statements/branches.
  - [ ] Section 5 assert positive live outcomes for both members with authentic setup, or leave verified blockers open.
  - [ ] Section 6 irp_class.md checked/updated.
  - [ ] Section 7 irp_class.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_use_case_remediation - IRPUseCase
  - Baseline: 4 property-shape conversions; 3 integration tests assert TypeError; two JavaDoc-only methods already have unavailable stubs.
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 reconcile find_extension_point and both other failing signatures against JavaDoc/catalog.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_use_case.py at 100% statements/branches.
  - [ ] Section 5 create entry/extension points and assert getter identity/content; replace all three exception assertions.
  - [ ] Section 6 irp_use_case.md checked/updated.
  - [ ] Section 7 irp_use_case.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_unit_remediation - IRPUnit
  - Baseline: 6 property-shape conversions; 4 integration tests assert RhapsodyRuntimeException.
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 all 6 properties and four failing cases reconciled against the report/catalog.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_unit.py at 100% statements/branches.
  - [ ] Section 5 replace the four exception assertions with authentic live outcomes or evidence-backed blockers.
  - [ ] Section 6 irp_unit.md checked/updated.
  - [ ] Section 7 irp_unit.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_port_remediation - IRPPort
  - Baseline: 5 property-shape conversions; the headless full-integration baseline has 2 port-test failures requiring evidence-based triage.
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 all 5 property members and the two live failures reconciled against JavaDoc/catalog.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_port.py at 100% statements/branches.
  - [ ] Section 5 create real provided/required interfaces and assert returned membership/value; resolve the two baseline failures.
  - [ ] Section 6 irp_port.md checked/updated.
  - [ ] Section 7 irp_port.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_interface_item_remediation - IRPInterfaceItem
  - Baseline: arguments and signature are property-shaped; verify_sync.py passes.
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 both property members reconciled against JavaDoc/catalog.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_interface_item.py at 100% statements/branches.
  - [ ] Section 5 create a real operation argument/signature and assert retrieved content/identity.
  - [ ] Section 6 irp_interface_item.md checked/updated.
  - [ ] Section 7 irp_interface_item.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_type_remediation - IRPType
  - Baseline: 10 property-shape conversions; the headless full-integration baseline has 7 type-test failures requiring evidence-based triage.
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 all 10 property members and seven live failures reconciled against JavaDoc/catalog.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_type.py at 100% statements/branches.
  - [ ] Section 5 create a real enumeration/type fixture and assert getter values/identity; resolve the seven baseline failures.
  - [ ] Section 6 irp_type.md checked/updated.
  - [ ] Section 7 irp_type.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_argument_remediation - IRPArgument
  - Baseline: argumentDirection is a COM property but is exposed by Java-style get_argument_direction()/set_argument_direction() methods; verify_sync.py otherwise passes.
  - [ ] Section 1 member checklist and populated getter fixture matrix row published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 Java getter/setter and COM property type/shapes reconciled.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_argument.py at 100% statements/branches.
  - [ ] Section 5 create a real operation argument, set a JavaDoc-valid direction, and assert the live property value.
  - [ ] Section 6 irp_argument.md checked/updated.
  - [ ] Section 7 irp_argument.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_attribute_remediation - IRPAttribute
  - Baseline: 6 COM properties are exposed through Java-style getter/setter methods; verify_sync.py otherwise passes.
  - [ ] Section 1 member checklist and six populated getter fixture matrix rows published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 six property names/types and JavaDoc-valid values reconciled.
  - [ ] Section 4 fake-COM property read/write tests first using properties=; full unit suite green; irp_attribute.py at 100% statements/branches.
  - [ ] Section 5 create a real attribute attached to a class, set a documented value, and assert each getter returns it.
  - [ ] Section 6 irp_attribute.md checked/updated.
  - [ ] Section 7 irp_attribute.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_argument_remediation - IRPArgument
  - Baseline: argumentDirection is a COM property but is exposed by Java-style get_argument_direction()/set_argument_direction() methods; verify_sync.py otherwise passes.
  - [ ] Section 1 member checklist and populated getter fixture matrix row published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 Java getter/setter and COM property type/shapes reconciled.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_argument.py at 100% statements/branches.
  - [ ] Section 5 create a real operation argument, set a JavaDoc-valid direction, and assert the live property value.
  - [ ] Section 6 irp_argument.md checked/updated.
  - [ ] Section 7 irp_argument.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.

- [ ] irp_attribute_remediation - IRPAttribute
  - Baseline: 6 COM properties are exposed through Java-style getter/setter methods; verify_sync.py otherwise passes.
  - [ ] Section 1 member checklist and six populated getter fixture matrix rows published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 six property names/types and JavaDoc-valid values reconciled.
  - [ ] Section 4 fake-COM property read/write tests first using properties=; full unit suite green; irp_attribute.py at 100% statements/branches.
  - [ ] Section 5 create a real attribute attached to a class, set a documented value, and assert each getter returns it.
  - [ ] Section 6 irp_attribute.md checked/updated.
  - [ ] Section 7 irp_attribute.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
