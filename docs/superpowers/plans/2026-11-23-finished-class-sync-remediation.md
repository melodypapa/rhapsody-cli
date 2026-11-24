# Finished-Class Sync-Rule Remediation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring all 16 finished (synced) interfaces back into compliance with the *current* `.agents/skills/rhapsody-sync/SKILL.md` rules — 9 wrappers fail the current verifier, 12 carry property-shape drift, and getter integration tests must create and relate authentic model data before asserting retrieval — then lock the rules into CI so drift cannot recur.

**Architecture:** Each interface gets its own rhapsody-sync remediation run following SKILL.md §1–§8 (one interface per run), recorded in `docs/reports/sync-todo/Group-unfinished-14.md`. Binding arity is fixed wrapper-first (TDD, fake-COM unit tests); integration tests build the real child/state required by each getter, relate it to the real parent, call the getter, and assert identity or expected content. Invalid exception assertions are replaced with positive behavior checks or documented blockers. Property-shaped members follow Decision Gate D1. A final CI task validates every catalog interface.

**Tech Stack:** Python 3.9+ (project targets 3.8–3.13), pytest + fakes (`tests/unit/models/fakes.py`), pywin32 COM on Windows + live IBM Rhapsody, ruff/black(line-length 200)/mypy strict, Sphinx RST docs, the skill-local validators `validate_interface.py` / `verify_sync.py`.

## Decision Gates (user sign-off required before the affected tasks run)

- **D1 — Python member shape (Tasks 2–16). CONFIRMED by the user:** expose a pywin32 `property` as Python `@property`; expose a pywin32 `method` as a Python method. Do not retain both `get_xxx()` and property aliases. The corrected report/wrapper audit finds **142 COM-property members across 14 interfaces** currently exposed through methods. A pre-migration Python-AST caller snapshot for `IRPModelElement` found **617 getter calls across 30 members**, including **491 `get_name()` calls**, plus **52 setter-method call sites** (49 property-backed setters and 3 calls to the JavaDoc-unsupported `set_description_html()` stub); the already-converted `all_tags`/`binary_id` references were excluded. Convert every member and migrate its callers. Use `@<name>.setter` only when pywin32 exposes a writable property; retain a separate method-shaped COM setter as a Python method. This is an intentional, broad public API change and follows the current skill's COM-shape rule.
- **D2 — `JAVA_DOC_MISSING` dispositions (Tasks 3, 4, 5).** Nine wrapper members call COM members that exist in pywin32 but not in the JavaDoc (`Classifier.add_port→addNewAggr`; `Package.add_association→addAssociation`; `Project.add_actor/add_class/add_node/delete_node/find_node/get_nodes/get_packages`). Default: keep them and document each as a supported COM extension in the regenerated report's Expected Binding Differences table. Confirm or override.
- **D3 — blockers.** Individual integration sites that cannot be exercised live (modal dialogs, external toolchains, an uncreatable AssociationClass fixture) come back to the user per site for approved-skip-or-remove, recorded in the ledger (Group-unfinished-1 precedent).

## Global Constraints (every task, verbatim from SKILL.md / AGENTS.md)

- One interface per remediation run; complete and review it before starting another (SKILL.md §8).
- No `@pytest.mark.xfail`, no `pytest.skip(...)`, no unconditional early returns in model-class tests. Skips require explicit user approval in-session **plus** a ledger entry (§4).
- Integration tests must not assert `AttributeError` / `RhapsodyRuntimeException` / `TypeError` / `ValueError` / `IndexError` or any "documented failure". Only `pytest.raises(NotImplementedError)` for a JavaDoc-defined, pywin32-absent stub is allowed (§5). No `try`/`except` in test bodies; `try`/`finally` without `except` is allowed.
- Integration tests use authentic data built from live Rhapsody objects — never `"arg"`-style placeholders; clean up created objects (§5).
- **Getter integration invariant:** for each model-backed `get_xxx()` member, first create a real `xxx` model element/state, attach or relate it to the real parent through the documented API, then call that parent’s getter and assert the returned object is the created object (or that the returned collection contains it). `is not None` alone is not sufficient when the getter's contract is to retrieve related model data. If D1 converts a getter-shaped member to `@property`, the same fixture/assertion applies through the approved public shape.
- Unit layer alone must give 100% statement and branch coverage of the wrapper module; integration layer has no coverage gate (§4).
- Wrapper calls exactly one pywin32-exposed COM member, method-shaped via `self.call_com(lambda: self._com.Name(...))`, property-shaped via inherited `ComHelper.get_com_property`/`set_com_property`; names confirmed against `docs/reports/pywin32_authority.json`; no runtime probing (AGENTS.md, §3).
- **Python shape follows COM shape** (§3): catalog `property` → Python `@property` (+ `@<name>.setter` only for writable properties); catalog `method` → Python method. A separate method-shaped COM setter remains a method even when paired with a property getter. Conversions rename accessors to the snake_case of the COM property name and migrate every caller in `src/` and `tests/` in the same run. No compatibility shims.
- API reports are generated — regenerate with `python scripts/validate_model_api.py <INTERFACE> --source authority`, never hand-edit (§3, §8).
- No `Any` in annotations; no AI attribution in commits; no direct commits to `main` (AGENTS.md).
- Tick each ledger/checklist box in the same response where its evidence lands (§1).
- Unit suite must be green before advancing any step (§4, §8).

## Preflight prerequisite: stabilize the live integration project fixture

Baseline before the GitHub merge: `2118 passed` in unit tests and `392 failed, 121 passed` in the visible full integration run, exposing a stale session-project wrapper. After merging `origin/main` at `258468d`, `pytest tests/unit` passes `2121` tests. The project-switch reproducer and seven focused CLI/application/model tests pass. With the fixture lifecycle correction and opt-in `--rhapsody-hidden-ui` run, the full integration suite completes without popups: `480 passed, 32 failed`. Remaining failures are: IRPModelElement (`test_high_light_element_binding`, `test_open_features_dialog_binding`); IRPPackage (`test_delete_sequence_diagram`, `test_delete_use_case_diagram`, `test_delete_collaboration_diagram`, `test_delete_component_diagram`, `test_delete_deployment_diagram`, `test_delete_object_model_diagram`, `test_delete_timing_diagram`, `test_delete_panel_diagram`, `test_delete_package`, `test_delete_node`, `test_delete_global_object`, `test_add_link_between_sysml_ports`); IRPPort (`test_port_state_and_contract`, `test_provided_and_required_interfaces`); IRPProject (`test_set_active_configuration`, `test_set_active_component`, `test_gateway_export_to_xml`, `test_gateway_export_to_xml2`, `test_generate_report`, `test_add_custom_view_on_diagram`, `test_set_object_explicit`, `test_set_object_implicit`); IRPType (`test_add_enumeration_literal`, `test_delete_enumeration_literal`, `test_set_is_typedef_constant`, `test_set_is_typedef_ordered`, `test_set_is_typedef_reference`, `test_set_kind`, `test_set_typedef_multiplicity`); and one legacy `tests/integration/models/elements/requirements/test_model_requirements.py::test_requirement_id_roundtrip` outside the 16-interface scope. The focused `test_build_entire_project` also passes with its local `set_hidden_ui(True)`/restore guard and no visible popup. The first four collected tests are CLI tests that open the shared project; therefore the former no-project application integration assertion had an invalid suite precondition and was replaced by a positive active-project assertion (the no-project branch remains unit-tested). The project-switch reproducer showed that a session-scoped `test_project` wrapper became stale after `create_new_project`; the function-scoped wrapper fixture fixes that cascade.

Before Task 1, use the existing red reproductions above and implement this test-harness correction TDD-first:

1. In `tests/integration/conftest.py`, split session-owned project-directory creation/cleanup from the function-scoped `test_project` wrapper fixture. On each test setup, return a fresh wrapper for the active test project or reopen `demos/test_project/TestProject.rpyx` when another project is active. Keep autosave enabled and preserve the session-level artifact cleanup.
2. In `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py`, make `live_fixtures` function-scoped and clean up the package it creates. Keep the positive active-project assertion using the real `test_project`; the no-active-project branch remains unit-tested. Call `rhapsody_app.save_all()` immediately before `create_new_project()` in the project-switching integration test to prevent the modal “Save changes?” prompt; this behavior is documented in `AGENTS.md`. For the code-generation modal, the opt-in `--rhapsody-hidden-ui` run controls launch with `show_gui=False` plus `set_hidden_ui(True)`, and `test_build_entire_project` additionally restores the prior hidden state in `finally`. The `test_irp_application.py` module also has an autouse hidden-UI default that restores the prior state at module teardown; its explicit visibility tests restore the hidden state they received. The shared `show_gui` fixture remains unchanged.
3. Run the exact red reproducer (`test_create_new_project_returns_the_created_project` then `test_argument_direction_roundtrip`), the focused application integration file, then the full integration suite. The prerequisite is complete only when project-switching no longer invalidates later fixtures and no order-dependent COM cascade remains. Record any independent integration failures separately; do not hide them as fixture skips.

## Audit Baseline (evidence collected 2026-11-23)

### Family A/B — `verify_sync.py` failures (9 classes)

`python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE>` over all 16 catalog interfaces:

| Result | Classes |
| --- | --- |
| PASS (7) | IRPApplication, IRPArgument, IRPAttribute, IRPClassifier, IRPInterfaceItem, IRPPort, IRPType |
| FAIL (9) | IRPModelElement, IRPPackage, IRPProject, IRPCollection, IRPAssociationClass, IRPOperation, IRPClass, IRPUseCase, IRPUnit |

Two violation families: **30 COM binding-arity bugs** (real runtime defects) and **66 disallowed exception-assertion sites** in integration tests:

| Class | Arity bugs (member: called → catalog) | Exception-assertion sites (file:line → exception) |
| --- | --- | --- |
| IRPModelElement | `getErrorMessage`: 0 → 1 | test_irp_model_element.py: 361, 397, 511, 520, 529, 615, 673, 675, 684, 686, 695, 697, 706, 723, 732, 741, 941, 977, 986, 1011, 1370 → `RhapsodyRuntimeException`; 1422 → `AttributeError` (22 sites) |
| IRPPackage | `deletePackage` 1→0, `findAllByName` 1→2, `addActivityDiagram` 1→0, `addStatechart` 1→0, `addAssociation` 1→3, `addGlobalObject` 1→3, `addLink` 1→5, `addLinkBetweenSYSMLPorts` 2→5 | test_irp_package.py: 107, 157, 382, 531, 622, 637, 667, 712 |
| IRPProject | `locateInIDE` 0→3, `GatewayExportToXML` 1→2, `GatewayExportToXML2` 2→3, `GenerateReport` 2→6, `addCustomViewOnDiagram` 1→2, `applyBrowserCustomViewsOnDiagrams` 0→1, `saveAsPrevVersion` 1→2, `removeCustomViewOnDiagram` 1→2, `reloadCSVFile` 0→1, `importProjectFromRose` 1→2, `importPackageFromRose` 1→3, `getRoundtripShadowModel` 0→1, `getRequirementsByID` 1→2, `getNewProgressBar` 0→2, `getActiveCustomViewsOnDiagram` 0→1, `findElementsWithOSLCLink` 1→2, `findElementByFileName` 1→2, `closeCSVFile` 0→1, `cleanUnresolvedElements` 0→1, `applyRoundtripDiffMerge` 0→3, `addSpellCheckerResult` 2→1 | test_irp_project.py: 154, 161, 197, 278, 292, 323, 380, 393, 400, 413, 420, 434, 447, 467, 474, 501, 521, 534, 549 → `RhapsodyRuntimeException`; 285, 481, 494 → `TypeError`; 216 → `AttributeError`; 514 → `ValueError` (24 sites) |
| IRPCollection | — | test_irp_collection.py: 36 → `IndexError` |
| IRPAssociationClass | — | test_irp_association_class.py: 52 → `AttributeError`; stale docstring claims "marked ``xfail``" (no marker exists) |
| IRPOperation | — | test_irp_operation.py: 118 → `AttributeError` |
| IRPClass | — | test_irp_class.py: 313, 315 → `RhapsodyRuntimeException` |
| IRPUseCase | — | test_irp_use_case.py: 55, 177, 186 → `TypeError` |
| IRPUnit | — | test_irp_unit.py: 257, 260, 262, 264 → `RhapsodyRuntimeException` |

### Family C — property-shape drift (14 interfaces, 142 COM properties)

The initial count missed multi-accessor report rows such as `getName`/`setName` → one COM `name` property. A complete report-to-wrapper AST audit finds these COM-property members currently exposed through Python methods; the COM bindings themselves exist, and the deviation is the Python-facing shape (§3).

| Interface | COM properties to expose as Python properties |
| --- | --- |
| IRPPackage (30) | actors, behavioral_diagrams, classes, collaboration_diagrams, component_diagrams, deployment_diagrams, events, events_base_id, flow_items, flows, global_functions, global_objects, global_variables, instance_specifications, links, modules, nested_classifiers, nested_components, nodes, packages, object_model_diagrams, panel_diagrams, saved_in_seperate_directory, sequence_diagrams, source_artifacts, timing_diagrams, types, use_case_diagrams, use_cases, user_defined_stereotypes |
| IRPModelElement (32) | all_tags, annotations, association_classes, binary_id, constraints, constraints_by_him, controlled_files, dependencies, description, description_html, description_plain_text, description_rtf, display_name, guid, hyper_links, interface_name, is_external, is_show_display_name, is_unresolved, local_tags, main_diagram, meta_class, name, of_template, owner, project, references, requirement_traceability_handle, stereotypes, template_parameters, ti, user_defined_meta_class |
| IRPClassifier (17) | activity_diagram, attributes, base_classifiers, behavioral_diagrams, derived_classifiers, flow_items, flows, generalizations, interface_items, links, nested_classifiers, operations, ports, relations, sequence_diagrams, source_artifacts, statechart |
| IRPOperation (15) | body, flowchart, initializer, is_abstract, is_cg_derived, is_const, is_ctor, is_dtor, is_final, is_inline, is_static, is_trigger, is_virtual, returns, visibility |
| IRPProject (10) | active_component, active_configuration, all_stereotypes, cg_simplified_model_package, components, default_directory_scheme, nodes, packages, profiles, use_unique_stereotype_and_ref_cache (writable) |
| IRPType (10) | declaration, enumeration_literals, is_predefined, is_typedef, is_typedef_constant, is_typedef_ordered, is_typedef_reference, kind, typedef_base_type, typedef_multiplicity |
| IRPUnit (6) | cm_header, current_directory, filename, include_in_next_load, is_stub, structure_diagrams |
| IRPAttribute (6) | is_constant, is_ordered, is_reference, is_static, multiplicity, visibility |
| IRPPort (5) | is_behavioral, is_reversed, port_contract, provided_interfaces, required_interfaces |
| IRPUseCase (4) | describing_diagrams, entry_points, extension_points, is_behavior_overriden |
| IRPAssociationClass (3) | end1, end2, is_class |
| IRPInterfaceItem (2) | arguments, signature |
| IRPCollection (1) | count |
| IRPArgument (1) | argument_direction |

### Family D — `validate_interface.py` deviations (6 classes)

`python .agents/skills/rhapsody-sync/scripts/validate_interface.py <INTERFACE> --source authority` exits 1 for IRPClassifier, IRPCollection, IRPModelElement, IRPPackage, IRPProject, IRPUseCase:

- **Actionable:** `IRPModelElement` — Java `getStereotype`/`setStereotype` map to a single read/write pywin32 property `stereotype` with **no Python wrapper member** (`MISSING_PYTHON_WRAPPER` + `METHOD_PROPERTY_MISMATCH`). Task 2 adds `stereotype` as a `@property` with setter.
- **`JAVA_DOC_MISSING` (9, Decision Gate D2):** Classifier `add_port→addNewAggr`; Package `add_association→addAssociation`; Project `add_actor→addActor`, `add_class→addClass`, `add_node→addNode`, `delete_node→deleteNode`, `find_node→findNode`, `get_nodes→nodes`, `get_packages→packages`.
- **Documented stubs (acceptable, no action):** Collection `add_graphical_item`/`to_list`, ModelElement `get_rmm_url`, UseCase `add_event_reception_with_event`/`update_contained_diagrams_on_server` — `UNAVAILABLE_DOCUMENTED` rows, already covered by `NotImplementedError` stubs + tests.

### Environment facts

This machine is Windows with Rhapsody available (live integration runs possible — ledger records 69 live passes on 2026-11-23); all 16 RST pages are listed in `docs/api/elements.rst`; the skill harness self-tests pass (31 passed); ledger index is `docs/reports/sync-todo/index.md` (groups 1–13 + `Group-finished.md`).

### Getter integration-data findings

The existing tests demonstrate why a data-backed getter pass is needed:

- `test_irp_package.py` creates an empty package, calls `get_classes()` / `get_actors()` / `get_use_cases()`, and only asserts the returned collections are non-`None`. Each case should create the corresponding child with `add_class` / `add_actor` / `add_use_case`, call the getter on that package, and assert the created child is present.
- `test_irp_classifier.py` already has good examples for `get_statechart()` and `get_activity_diagram()`: create the diagram on the classifier, call the getter, assert identity. Use this pattern for every model-backed collection/getter, not just those two.
- `test_irp_application.py` has a module-scoped `live_fixtures` with a package and class, but `get_list_of_selected_elements()` and `get_diagram_of_selected_element()` only assert non-`None` and do not establish/select the required model/diagram state. The fixture's package/class also is not consistently used by the getter tests. The replacement tests must create a class, select it (after consulting JavaDoc for the selection contract), and assert it appears in the returned selection; the diagram getter must create/open/select a real diagram element and assert the corresponding diagram. Review `get_application_name("0", "0")`, `get_error_message("0")`, `expand_string_keywords("0")`, and `get_helper_status("0")` against JavaDoc/authority and replace placeholder inputs with documented real values or record a genuine prerequisite blocker. Environment/system getters (for example install paths and version strings) should be asserted against their real environment, not supplied with model objects.

For every interface, §1/§3 must add an owned-getter inventory to the per-run checklist: JavaDoc getter → required parent/related object → setup API → getter invocation → identity/value assertion. Use per-test setup and `try/finally` cleanup; extract a typed helper only when the same setup is repeated. Do not rely on one module/session-wide mutable model fixture to hide missing setup or couple test order.

**Execution order:** IRPModelElement first (base class — its 32 property conversions, `stereotype`, and arity fix are inherited surface), then the binding-bug clusters (IRPPackage, IRPProject), IRPClassifier, the remaining model classes including IRPArgument and IRPAttribute, IRPApplication's existing Group 1 getter closeout, then the CI guardrail.

---

### Task 1: Create the remediation ledger batch

**Files:**

- Create: `docs/reports/sync-todo/Group-unfinished-14.md`
- Modify: `docs/reports/sync-todo/index.md`

- [x] **Step 1: Create `Group-unfinished-14.md`** with these 15 row identifiers, in execution order: `irp_model_element_remediation`, `irp_package_remediation`, `irp_project_remediation`, `irp_classifier_remediation`, `irp_collection_remediation`, `irp_association_class_remediation`, `irp_operation_remediation`, `irp_class_remediation`, `irp_use_case_remediation`, `irp_unit_remediation`, `irp_port_remediation`, `irp_interface_item_remediation`, `irp_type_remediation`, `irp_argument_remediation`, and `irp_attribute_remediation`. For each row, copy the actual deviation counts and member names from this plan's audit tables; include all eight §1–§8 checkboxes, the Getter fixture matrix rows, measured unit coverage, and the live integration pass/fail count. The IRPApplication work in Task 17 continues its existing open row in `Group-unfinished-1.md`; do not duplicate it. Use each class's exact module and mirrored test path from its task.

- [x] **Step 2: Add the batch to `index.md`** table: a row for `Group-unfinished-14.md` (15 rows, `IRPModelElement → IRPAttribute`, rule-drift remediation) and update the progress total from `15/129` to `15/144 rows tracked`. Keep IRPApplication in its existing Group 1 row.

- [x] **Step 3: Stage only the ledger paths for the eventual documentation commit** (do not use `git add -A`; this branch contains other task files):

```bash
git add docs/reports/sync-todo/Group-unfinished-14.md docs/reports/sync-todo/index.md
```

---

### Task 2: IRPModelElement remediation (base class — arity bug, 32 property conversions, `stereotype`, 20 remaining assertion sites)

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_model_element.py`
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_model_element.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py` (22 baseline exception sites; two invalid-type cases now use real roundtrips; 20 remaining sites + conversion call sites)
- Modify: regenerated report, requirement doc, RST
- Migrate callers: `grep -rnE 'get_(all_tags|annotations|association_classes|binary_id|constraints|constraints_by_him|controlled_files|dependencies|description|description_html|description_plain_text|description_rtf|display_name|guid|hyper_links|interface_name|is_external|is_show_display_name|is_unresolved|local_tags|main_diagram|meta_class|name|of_template|owner|project|references|requirement_traceability_handle|stereotypes|template_parameters|ti|user_defined_meta_class)\\(' src/rhapsody_cli tests/unit tests/integration`.
- Ledger: `Group-unfinished-14.md` (IRPModelElement row)

**Interfaces:**

- Produces: a `get_error_message` COM call that passes the catalog-required `_MIDL__IRPModelElement0002_` string buffer while preserving its documented Python return behavior; 32 COM-property-backed `@property` members; and a read/write `stereotype` property typed as the `RPStereotype` wrapper. These accessors are inherited by every subclass — later tasks build on this surface.

- [ ] **Step 1: §1 — publish the per-run checklist** (one subtask per owned member, including each conversion) before any edit.
- [ ] **Step 2: §3 — reconcile the arity site.** Dump the pywin32 signature and baseline:

```bash
python -c "import json; d=json.load(open('docs/reports/pywin32_authority.json',encoding='utf-8')); print(json.dumps(d['signatures']['IRPModelElement']['getErrorMessage'], indent=2))"
python .agents/skills/rhapsody-sync/scripts/validate_interface.py IRPModelElement --source authority
```

  Pre-migration wrapper code (before this run):

```python
    def get_error_message(self) -> str:
        return str(ComHelper.call_com(lambda: self._com.getErrorMessage()))
```

  If the signature is the same MIDL out-buffer artifact as `IRPApplication.getErrorMessage` (1 required `str`), the fix is:

```python
    def get_error_message(self, _midl__irp_model_element0002_: str) -> str:
        return str(ComHelper.call_com(lambda: self._com.getErrorMessage(_midl__irp_model_element0002_)))
```

  (naming per `irp_application.py:1272`; if evidence disagrees — e.g. the member is property-shaped — record it and stop for a decision, do not guess.)
- [ ] **Step 3: §3 — implement Family C conversions + `stereotype`.** Conversion pattern (before → after), e.g.:

```python
    # before
    def get_binary_id(self) -> bytes:
        return bytes(ComHelper.get_com_property(self._com, "BinaryID"))

    # after
    @property
    def binary_id(self) -> bytes:
        return bytes(ComHelper.get_com_property(self._com, "BinaryID"))
```

  For `stereotype` (no existing member — Java `getStereotype`/`setStereotype`, pywin32 property `stereotype`):

```python
    @property
    def stereotype(self) -> RPStereotype | None:
        """Returns the deprecated single stereotype associated with this element, if any."""
        from rhapsody_cli.models.elements.classifiers.model_stereotype import RPStereotype

        raw_stereotype = ComHelper.get_com_property(self._com, "stereotype")
        if raw_stereotype is None:
            return None
        return cast(RPStereotype, ComHelper.wrap(raw_stereotype))

    @stereotype.setter
    def stereotype(self, value: RPStereotype) -> None:
        ComHelper.set_com_property(self._com, "stereotype", value._com)
```

  Keep `set_description_html()` as the JavaDoc-defined `NotImplementedError` stub: JavaDoc says it is not implemented and pywin32 exposes no setter method for `descriptionHTML`; the `description_html` property remains read-only. Then migrate every supported caller found by the explicit caller search above in `src/`, `tests/unit`, and `tests/integration`. Update fakes: property reads/writes use the `properties=` channel of `make_fake_element`.
- [x] **Step 4: §4 — failing unit tests first** for the arity fix, each conversion, and `stereotype`; then green; then coverage. Evidence: focused unit file 153 passed, 306 statements and 136 branches at 100.00%; full unit suite 2120 passed; `mypy src/ tests/` clean:

```bash
PYTHONPATH=src python -m pytest tests/unit/models/com/telelogic/rhapsody/core/test_irp_model_element.py -q -o addopts=
PYTHONPATH=src python -m pytest tests/unit/models/com/telelogic/rhapsody/core/test_irp_model_element.py --cov=rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element --cov-report=term-missing -o addopts=
```

  Expected: all pass, **100% statements and 100% branches**.
- [x] **Step 5: §5 — rewrite the 20 remaining disallowed exception-assertion sites** (audit lines) with this decision procedure per site. Evidence: all sites rewritten to positive outcomes; `grep -n "pytest.raises"` on the integration file shows only `NotImplementedError` matches; first live rerun after the rewrite measured 85 passed / 21 failed and produced the evidence used to fix fixtures (dot-syntax property keys, `set_size`/`set_string` token collections, `getTag` re-query for typed `IRPTag` value reads, `meta_class` assertions for `add_relation_to` results, `ComHelper.call_com` patch targets, `TemplateParameter` precondition for template fixtures); final live rerun pending (orphaned rhapsody.exe processes must be closed first); remaining blockers recorded in Group-unfinished-14.
  - Failure caused by **wrong binding/arguments** → wrapper fix (Step 2 pattern); assert the real result.
  - Failure caused by **deliberate misuse** → delete the misuse case; assert a real call with authentic data (misuse guards stay in the unit layer).
  - Precondition **cannot be met live** → leave Step 5 open, present the blocker (Decision Gate D3).
  - Verify: `grep -n "pytest.raises" tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py` — only `NotImplementedError` matches may remain.
- [x] **Step 6: §6/§7 — refresh requirement doc and RST** for every renamed/added member (signature lines; RST `autofunction`/`autoattribute` directives follow the new names; `verify_sync.py` fails if any public member name is missing from the RST). Evidence: requirement page rewritten; RST regenerated with 33 `autoattribute` + 70 `automethod` directives; `verify_sync.py IRPModelElement` exits 0.
- [ ] **Step 7: §8 — verify.** Static portions green (validator exits 0 with 0 actionable deviations after property-shape support; verify_sync exits 0; skill harness 31 passed; ruff/black/mypy clean; unit suite 2124 passed); the focused live rerun is pending until the orphaned Rhapsody processes are closed.

```bash
python .agents/skills/rhapsody-sync/scripts/verify_sync.py IRPModelElement
python .agents/skills/rhapsody-sync/scripts/validate_interface.py IRPModelElement --source authority
python -m pytest -o addopts= .agents/skills/rhapsody-sync/tests -q
PYTHONPATH=src python -m pytest tests/unit -q -o addopts=
PYTHONPATH=src python -m pytest tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py -q -o addopts=
ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/
```

- [ ] **Step 8: regenerate the report, commit, tick the ledger row.**

```bash
python scripts/validate_model_api.py IRPModelElement --source authority --path docs/reports
# Stage only the wrapper, mirrored tests, generated report/docs, and audited caller paths from Step 3.
# Do not use git add -A; preserve unrelated staged and unstaged work.
git commit -m "fix(sync): IRPModelElement arity, property shapes, stereotype member, integration assertions"
```

---

### Task 3: IRPPackage remediation (8 arity bugs, 30 property conversions, 1 deviation, 8 assertion sites)

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_package.py` (8 call sites + 30 property conversions)
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_package.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py` (sites 107, 157, 382, 531, 622, 637, 667, 712 + conversion call sites)
- Modify: regenerated report, requirement doc, RST; migrate callers
- Ledger: `Group-unfinished-14.md` (IRPPackage row)

**Interfaces:**

- Produces: 8 arity-conformant methods (Family A table), 30 `@property` accessors (Family C), `add_association→addAssociation` documented as a COM extension (D2).

- [ ] **Step 1: §1 — publish the checklist** with a subtask for every owned JavaDoc member and a Getter fixture matrix row for every getter.
- [ ] **Step 2: §3 — dump the 8 signatures and reconcile each call site:**

```bash
python -c "import json; d=json.load(open('docs/reports/pywin32_authority.json',encoding='utf-8')); [print(m, json.dumps(s)) for m, s in d['signatures']['IRPPackage'].items() if m in {'deletePackage','findAllByName','addActivityDiagram','addStatechart','addAssociation','addGlobalObject','addLink','addLinkBetweenSYSMLPorts'}]"
```

  Map each catalog parameter to the wrapper's snake_case parameter; rewrite the `call_com(lambda: ...)` to pass exactly the catalog band. Where makepy gives Python defaults for trailing parameters, keep the public signature Java-shaped and pass only catalog-required COM arguments inside the lambda.
- [ ] **Step 3: §3 — 30 property conversions** (Task 2 Step 3 pattern) + caller migration + fakes `properties=` channel.
- [ ] **Step 4: §4 — failing fake-COM unit tests first per member**, then fixes, then green; 100%/100% coverage on `irp_package.py`.
- [ ] **Step 5: §5 — rewrite the 8 exception-assertion sites** (Task 2 Step 5 procedure; `TypeError` sites 107/157/382/622/712 are likely artifacts of the same arity bugs and convert to real-outcome assertions once fixed).
- [ ] **Step 6: §6/§7 — refresh requirement doc + RST** for renamed members and the `add_association` extension disposition (report's Expected Binding Differences; keep deviations out of the RST).
- [ ] **Step 7: §8 — verify** (Task 2 Step 7 command set, `IRPPackage`).
- [ ] **Step 8: regenerate report, commit (`fix(sync): IRPPackage arity, property shapes, integration assertions`), tick the ledger row.**

---

### Task 4: IRPProject remediation (21 arity bugs, 9 read properties + 1 writable property, 7 deviations, 24 assertion sites)

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py` (21 call sites + 10 property members)
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_project.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py` (24 sites: audit table + conversions)
- Modify: regenerated report, requirement doc, RST; migrate callers
- Ledger: `Group-unfinished-14.md` (IRPProject row)

**Interfaces:**

- Produces: 21 arity-conformant methods; `active_component`, `active_configuration`, `all_stereotypes`, `cg_simplified_model_package`, `components`, `default_directory_scheme`, `nodes`, `packages`, `profiles` read properties; `use_unique_stereotype_and_ref_cache` read/write property; 7 extensions documented (D2).

- [ ] **Step 1: §1 — publish the checklist** with a subtask for every owned JavaDoc member and a Getter fixture matrix row for every getter.
- [ ] **Step 2: §3 — reconcile all 21 call sites** (Task 3 Step 2 procedure; `addSpellCheckerResult` runs the band check in reverse: called with 2, catalog declares 1 — fold the second wrapper argument into the single COM argument or drop it per JavaDoc evidence).
- [ ] **Step 3: §3 — 9 read-property conversions + `use_unique_stereotype_and_ref_cache` property with setter** (Task 2 Step 3 pattern; the setter currently lives as `set_use_unique_stereotype_and_ref_cache()`).
- [ ] **Step 4: §4 — failing unit tests first, then green; 100%/100% coverage.**
- [ ] **Step 5: §5 — rewrite the 24 sites** (Task 2 Step 5 procedure; expect D3 blockers for Rose/Gateway/Roundtrip/spell-checker members needing external toolchains — present for sign-off, remove with ledger entry if approved).
- [ ] **Step 6: §6/§7 — refresh docs. §7 stays deviation-free; the 7 extensions go into the report only.**
- [ ] **Step 7: §8 — verify (Task 2 Step 7 command set, `IRPProject`).**
- [ ] **Step 8: regenerate report, commit (`fix(sync): IRPProject arity, property shapes, integration assertions`), tick the ledger row.**

---

### Task 5: IRPClassifier remediation (17 conversions, 1 deviation; verify_sync already PASS)

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_classifier.py` (17 conversions)
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_classifier.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py` (conversion call sites)
- Modify: regenerated report, requirement doc, RST; migrate callers (subclasses overriding/inheriting these accessors re-verify in their own tasks)
- Ledger: `Group-unfinished-14.md` (IRPClassifier row)

**Interfaces:**

- Produces: 17 `@property` accessors (Family C); `add_port→addNewAggr` documented as a COM extension (D2).

- [ ] **Step 1: §1 — publish the checklist.**
- [ ] **Step 2: §3 — 17 conversions + extension disposition** (Task 2 Step 3 pattern; `validate_interface.py IRPClassifier --source authority` must drop to documented-only deviations).
- [ ] **Step 3: §4 — unit tests first (property reads against fakes), then green; 100%/100% coverage.**
- [ ] **Step 4: §5 — update integration call sites to attribute access.**
- [ ] **Step 5: §6/§7 — refresh docs. §8 — verify (Task 2 Step 7 command set, `IRPClassifier`).**
- [ ] **Step 6: regenerate report, commit (`fix(sync): IRPClassifier property shapes`), tick the ledger row.**

---

### Task 6: IRPCollection remediation (1 conversion, 1 assertion site)

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collection.py` (`get_count` → `count`)
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_collection.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_collection.py` (site 36 + `get_count()` call sites)
- Migrate callers: `get_count()` is used across wrappers and CLI — `grep -rn "get_count(" src/rhapsody_cli tests/`
- Ledger: `Group-unfinished-14.md` (IRPCollection row)

- [ ] **Step 1: §1 — publish the checklist.**
- [ ] **Step 2: §3 — convert `get_count()` → `@property count`** (keep `__len__`; migrate every `get_count()` call site in `src/`, `tests/`).
- [ ] **Step 3: §5 — rewrite site 36.** Current code:

```python
        with pytest.raises(IndexError, match="negative indices"):
            collection[-1]
```

  Replace with real-outcome assertions (the wrapper's negative-index guard stays and remains unit-layer covered):

```python
        assert collection[0] is not None
        assert collection[2] is not None  # after set_size(3): highest valid zero-based index
```

- [ ] **Step 4: §4 — unit tests first, then green; 100%/100% coverage. §8 — verify; regenerate report; commit (`fix(sync): IRPCollection count property + integration assertions`); tick the ledger row.**

---

### Task 7: IRPAssociationClass remediation (3 property conversions, 1 assertion site, stale docstring)

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_association_class.py` (`get_end1`/`get_end2`/`get_is_class` → `end1`/`end2`/`is_class`)
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_association_class.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_association_class.py` (site 52 + docstring lines ~20-26)
- Ledger: `Group-unfinished-14.md` (IRPAssociationClass row)

- [ ] **Step 1: §1 — publish the checklist.**
- [ ] **Step 2: §3 — 3 property conversions; resolve how this Rhapsody build creates a true AssociationClass.** Read `IRPAssociationClass` + `IRPClassifier.addRelationTo` JavaDoc and the catalog. The current test wraps a plain association (`IRPAssociationClass(cls._com)`) whose metaclass is not `AssociationClass`, then asserts `AttributeError` when the four owned methods are probed — exactly the "blessing a wrong binding" pattern §5 bans. Evidence order: (a) profile/metaclass-based creation, (b) `addRelationTo` with an explicit association-class argument, (c) model built via file import. If no live path exists, present D3: approved skip + ledger entry, or case removal per the Group-unfinished-1 precedent. The `AttributeError` assertion may not survive in any outcome.
- [ ] **Step 3: §5 — rewrite `test_owned_methods_via_wrapped_com_object`** to create the authentic fixture and assert `end1`/`end2` return the real ends and `is_class` can be read/written through the property — or record the approved blocker. Delete the docstring sentence claiming the test "is marked ``xfail``".
- [ ] **Step 4: §4 — unit tests for the conversions first; §8 — verify; commit (`fix(sync): IRPAssociationClass end properties + integration assertions`); tick the ledger row.**

---

### Task 8: IRPOperation remediation (15 property conversions, 1 assertion site)

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_operation.py` (`get_body`, `get_flowchart`, `get_initializer`, `get_is_abstract`, `get_is_cg_derived`, `get_is_const`, `get_is_ctor`, `get_is_dtor`, `get_is_final`, `get_is_inline`, `get_is_static`, `get_is_trigger`, `get_is_virtual`, `get_returns`, `get_visibility` → properties)
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_operation.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py` (site 118 + conversions)
- Ledger: `Group-unfinished-14.md` (IRPOperation row)

- [ ] **Step 1: §1 — publish the checklist.**
- [ ] **Step 2: §3 — 15 property conversions; inspect site 118** (`pytest.raises(AttributeError)`): whether it masks a missing wrapper member (→ add it per §4) or probes a pywin32-absent Java member (→ `NotImplementedError` stub; the assertion becomes the one permitted `pytest.raises(NotImplementedError)`).
- [ ] **Step 3: §4 — unit tests first; §5 — real-assertion rewrite with an authentic operation fixture (`pkg.add_class(...).add_operation(...)`); §8 — verify; commit (`fix(sync): IRPOperation flag properties + integration assertions`); tick the ledger row.**

---

### Task 9: IRPClass remediation (2 assertion sites only — property-shape already conformant)

**Files:**

- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_class.py:313,315`
- Ledger: `Group-unfinished-14.md` (IRPClass row)

- [ ] **Step 1: §1 — publish the checklist.**
- [ ] **Step 2: §3/§5 — rewrite both `RhapsodyRuntimeException` sites** (Task 2 Step 5 procedure).
- [ ] **Step 3: §8 — verify; commit (`test(sync): IRPClass integration asserts real outcomes`); tick the ledger row.**

---

### Task 10: IRPUseCase remediation (4 property conversions, 3 assertion sites)

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_use_case.py` (`get_describing_diagrams`, `get_entry_points`, `get_extension_points`, `get_is_behavior_overriden` → properties)
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_use_case.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_use_case.py` (sites 55, 177, 186 + conversions)
- Modify: regenerated report/requirement/RST if signatures change
- Ledger: `Group-unfinished-14.md` (IRPUseCase row)

- [ ] **Step 1: §1 — publish the checklist.**
- [ ] **Step 2: §3 — reconcile the three `TypeError` sites.** Site 55 is `find_extension_point(ep_name)` called right after `add_extension_point(ep_name)` — check `IRPUseCase.findExtensionPoint` in the catalog; if the pywin32 signature differs from the wrapper's (element-vs-string argument), fix the wrapper first (TDD), then assert the real lookup result. Sites 177/186 get the same treatment.
- [ ] **Step 3: §3 — 4 property conversions; §4 — unit tests first; §5 — assert real outcomes; §6/§7 — refresh docs if signatures changed; §8 — verify; commit (`fix(sync): IRPUseCase properties, find_extension_point binding, integration assertions`); tick the ledger row.**

---

### Task 11: IRPUnit remediation (6 property conversions, 4 assertion sites)

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_unit.py` (`get_cm_header`, `get_current_directory`, `get_filename`, `get_include_in_next_load`, `get_is_stub`, `get_structure_diagrams` → properties)
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_unit.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_unit.py` (sites 257, 260, 262, 264 + conversions)
- Ledger: `Group-unfinished-14.md` (IRPUnit row)

- [ ] **Step 1: §1 — publish the checklist.**
- [ ] **Step 2: §3 — 6 property conversions; §3/§5 — rewrite the four `RhapsodyRuntimeException` sites.** Cross-check the 2026-11-22 Group-finished note: two IRPUnit live tests were removed once for being unexecutable in this build — if these four are the same family, present D3 (approved removal + ledger entry) instead of rewriting.
- [ ] **Step 3: §4 — unit tests first; §8 — verify; commit (`fix(sync): IRPUnit properties + integration assertions`); tick the ledger row.**

---

### Task 12: IRPPort remediation (5 property conversions)

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_port.py` (`get_is_behavioral`, `get_is_reversed`, `get_port_contract`, `get_provided_interfaces`, `get_required_interfaces` → properties)
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_port.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_port.py` (conversion call sites)
- Ledger: `Group-unfinished-14.md` (IRPPort row)

- [ ] **Step 1: §1 — publish the checklist.**
- [ ] **Step 2: §3 — 5 property conversions (Task 2 Step 3 pattern); §4 — unit tests first; §5 — integration attribute access; §6/§7 — docs; §8 — verify; commit (`fix(sync): IRPPort interface properties`); tick the ledger row.**

---

### Task 13: IRPInterfaceItem remediation (2 conversions)

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interface_item.py` (`get_arguments`/`get_signature` → properties)
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_interface_item.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_interface_item.py` (conversion call sites)
- Ledger: `Group-unfinished-14.md` (IRPInterfaceItem row)

- [ ] **Step 1: §1 — publish the checklist.**
- [ ] **Step 2: §3 — 2 conversions; §4 — unit tests first; §5 — integration attribute access; §8 — verify; commit (`fix(sync): IRPInterfaceItem argument/signature properties`); tick the ledger row.**

---

### Task 14: IRPType remediation (10 property conversions)

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_type.py` (`get_declaration`, `get_enumeration_literals`, `get_is_predefined`, `get_is_typedef`, `get_is_typedef_constant`, `get_is_typedef_ordered`, `get_is_typedef_reference`, `get_kind`, `get_typedef_base_type`, `get_typedef_multiplicity` → properties)
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_type.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_type.py` (conversion call sites)
- Ledger: `Group-unfinished-14.md` (IRPType row)

- [ ] **Step 1: §1 — publish the checklist.**
- [ ] **Step 2: §3 — 10 property conversions; §4 — unit tests first; §5 — integration attribute access; §8 — verify; commit (`fix(sync): IRPType properties`); tick the ledger row.**

---

### Task 15: IRPArgument property-shape remediation

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_argument.py` (`get_argument_direction`/`set_argument_direction` → read/write `argument_direction` property)
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_argument.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_argument.py`
- Modify: regenerated report, `docs/requirements/com/telelogic/rhapsody/core/irp_argument.md`, and `docs/api/com/telelogic/rhapsody/core/irp_argument.rst`
- Ledger: `Group-unfinished-14.md` (`irp_argument_remediation`)

- [ ] **Step 1: §1 — publish the IRPArgument member checklist** and its getter fixture matrix row.
- [ ] **Step 2: §3 — confirm `getArgumentDirection`/`setArgumentDirection` JavaDoc signatures and the single pywin32 `argumentDirection` property.**
- [ ] **Step 3: §4 — write fake-COM tests first** for `argument_direction` read/write through the fake's `properties=` channel; make them fail, then expose the property using `ComHelper.get_com_property`/`set_com_property`, unwrapping the real value only if the catalog/property type requires it. Preserve `get_argument_direction` only if JavaDoc and COM report it as a method; here the catalog property shape means the public surface is the property.
- [ ] **Step 4: §5 — create a real package, class, operation, and argument; set a JavaDoc-valid direction, read `argument.argument_direction`, and assert the live value.** Clean up the owning class in `finally`.
- [ ] **Step 5: §6/§7 — refresh the per-class requirement and RST API reference** to document `argument_direction`.
- [ ] **Step 6: §8 — require 100%/100% focused unit coverage, full unit suite green, `validate_interface.py`/`verify_sync.py` green, and record live counts; regenerate the report and tick the ledger.**

---

### Task 16: IRPAttribute property-shape remediation

**Files:**

- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_attribute.py` (`get/set_is_constant`, `get/set_is_ordered`, `get/set_is_reference`, `get/set_is_static`, `get/set_multiplicity`, and `get/set_visibility` → properties)
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_attribute.py`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_attribute.py`
- Modify: regenerated report, `docs/requirements/com/telelogic/rhapsody/core/irp_attribute.md`, and `docs/api/com/telelogic/rhapsody/core/irp_attribute.rst`
- Ledger: `Group-unfinished-14.md` (`irp_attribute_remediation`)

- [ ] **Step 1: §1 — publish the IRPAttribute member checklist** with six Getter fixture matrix rows.
- [ ] **Step 2: §3 — verify the six pywin32 property names/types and the JavaDoc values.** Use the live integration file's real attribute setup; use only documented values for multiplicity and visibility.
- [ ] **Step 3: §4 — write/update fake-COM property read/write tests first** using `properties=`; make them fail, expose the six Python properties with their setters, migrate callers, then get 100%/100% coverage on `irp_attribute.py` and run the full unit suite.
- [ ] **Step 4: §5 — for each property, create a real class attribute, set a documented value, read the property, and assert the value.** Clean up the class in `finally`; never substitute type-only or empty-state checks for the getter.
- [ ] **Step 5: §6/§7 — refresh requirement and RST pages** to document the six properties and setters.
- [ ] **Step 6: §8 — require `validate_interface.py`/`verify_sync.py` green, full quality gates, focused live pass/fail counts, and a regenerated report; tick the ledger.**

---

### Task 17: IRPApplication getter integration-data remediation

**Files:**

- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py`
- Modify: `tests/integration/conftest.py` only if a small, reusable function-scoped fixture is needed; do not change the shared `test_project` lifecycle without evidence
- Ledger: `docs/reports/sync-todo/Group-unfinished-1.md` (existing IRPApplication row; preserve its earlier evidence and add the current getter-data findings)

**Interfaces:**

- Produces: application getter tests that establish authentic application/model state before reading it; no placeholder inputs.

- [ ] **Step 1: §1/§3 — publish the member checklist and inventory every owned `get_*` member.** For each getter, record whether its contract is model-backed, app/environment-backed, or takes a documented lookup/input value. Read JavaDoc and catalog evidence before choosing setup data.
- [ ] **Step 2: Make selected-element retrieval data-backed.** Create a unique package and class under `test_project`, put the class in an `IRPCollection`, call `rhapsody_app.select_model_elements(collection)`, then call `get_list_of_selected_elements()` and assert that the created class (or its documented stable identifier) is present. Restore selection state and delete the test package in `finally`.
- [ ] **Step 3: Make selected-diagram retrieval data-backed.** Create a real class and diagram using documented APIs, open/activate the diagram and select a real graphical/model element according to the JavaDoc selection contract, then call `get_diagram_of_selected_element()` and assert it resolves to the created diagram. If the live API cannot establish that precondition, record a concrete blocker; do not assert only non-`None` or use a fabricated value.
- [ ] **Step 4: Preserve and strengthen project retrieval assertions.** `active_project()` and `projects` already use `test_project`; assert the retrieved object is the fixture project (or its actual name/path), not merely that the result exists.
- [ ] **Step 5: Replace placeholder getter inputs.** Resolve `get_application_name("0", "0")`, `get_error_message("0")`, `expand_string_keywords("0")`, and `get_helper_status("0")` against JavaDoc + pywin32 signatures. Use a valid installed helper, real keyword syntax/value, or correct MIDL output-buffer contract. If a valid live precondition is unavailable, record a genuine blocker rather than retaining `"0"`. Use a unique descriptive progress-bar name for `create_progress_bar` and remove it through the documented API if cleanup is required.
- [ ] **Step 6: Scope live fixtures to the test that needs them.** Replace the module-scoped mutable `live_fixtures` with function-scoped setup where it creates or selects model state; cleanup the created root package and restore app selection in `finally`. Do not reuse mutable setup across unrelated getter tests.
- [ ] **Step 7: Verify.** Run the focused Windows live test file, all unit tests, `verify_sync.py IRPApplication`, `validate_interface.py IRPApplication --source authority`, and the repository quality gate. Keep report/requirements/RST unchanged unless the public wrapper contract changes.
- [ ] **Step 8: Commit and tick the ledger row** with the getter inventory, exact live pass/fail counts, and any approved blocker.

---

### Task 18: CI drift guardrail (only after Tasks 2–17 are green)

**Files:**

- Modify: `.github/workflows/python-package.yml` (insert after the `Type check with mypy` step, line ~38)

**Interfaces:**

- Produces: CI fails when any catalog interface regresses against `verify_sync.py` or the skill harness tests.

- [ ] **Step 1: add the workflow steps:**

```yaml
    - name: Sync-rule conformance (verify_sync + skill harness)
      run: |
        $fails = 0
        foreach ($iface in (Get-ChildItem docs/reports/com/telelogic/rhapsody/core/*_api_report.md | ForEach-Object { $_.BaseName -replace '_api_report$','' })) {
          python .agents/skills/rhapsody-sync/scripts/verify_sync.py $iface
          if ($LASTEXITCODE -ne 0) { $fails++ }
        }
        python -m pytest -o addopts= .agents/skills/rhapsody-sync/tests -q
        if ($fails -gt 0) { exit 1 }
```

- [ ] **Step 2: verify locally first:**

```bash
for f in docs/reports/com/telelogic/rhapsody/core/*_api_report.md; do python .agents/skills/rhapsody-sync/scripts/verify_sync.py "$(basename $f _api_report.md)" || echo FAIL; done
```

  Expected: 16× exit 0, no FAIL lines.
- [ ] **Step 3: commit (`ci: enforce sync-rule conformance via verify_sync`) and confirm the PR run goes green.**

---

## Out of scope (separate planning efforts)

- The **113 unsynced interfaces** queued in `Group-unfinished-2..13.md` — continue per the existing ledger's importance order. Note: their queued sync runs should apply the property-shape rule from the start, and inherit the renamed base-class accessors from Tasks 2–5.
- **AGENTS.md modernization** — it still documents the pre-sync layout (`models/elements/` domains, `core.py` as base, `test_model_association_class.py` as the reference pattern) which the skill's canonical-package rules supersede. Propose a docs pass after this remediation; needs user sign-off.

## Self-Review

- Coverage: every `verify_sync` FAIL maps to a task; every Family C member list is assigned to exactly one task; Family D dispositions are assigned (Tasks 3, 4, 5) and the actionable `stereotype` gap lands in Task 2; every interface's getter tests must include the per-member setup→retrieval→identity/value audit, with IRPApplication's selected-element/diagram cases explicit in Task 17; the CI guardrail closes the loop. IRPClass needs no shape work (already 5/5 conformant). ✅
- Plan review: D1 is confirmed, D2 uses the documented-extension default, the ComHelper migration from the GitHub merge is reflected in Task 2 examples, and GUI/live blockers remain explicit under D3. ✅
- Consistency: D1 is confirmed as COM-shape-only (no dual API); the new batch has 15 rows for Tasks 2–16; IRPApplication Task 17 remains in Group 1; adding 15 rows changes the index total from 129 to 144; CI is Task 18. ✅
