# Sync todo — `classifiers` (group 1 of 2)

**10 classes** · ✅ 1 archived · ⬜ 9 open

One row per sync run. A step is ticked only when its evidence lands; a row is archived only after all eight steps pass. Binding rule: one pywin32-exposed COM member per call — `call_com(lambda: self._com.Name(...))` for methods, `get_com_property` / `set_com_property` for properties; catalog-absent sites are blockers, never blind migrations. Canonical package: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/`, mirrored tests under `tests/{unit,integration}/models/com/telelogic/rhapsody/core/`.

## Step legend

| Step | Meaning |
| --- | --- |
| ① §1 | publish the per-run checklist with a subtask per target-owned JavaDoc member |
| ② §2 | resolve the wrapper, inheritance, exports, and tests; move to the canonical package |
| ③ §3 | reconcile every owned member against JavaDoc, pywin32, and the Python wrapper |
| ④ §4 | failing fake-COM unit tests first, then migrate the legacy sites |
| ⑤ §5 | integration coverage on the mirrored path; live run on Windows |
| ⑥ §6 | update the per-class requirement document |
| ⑦ §7 | update the per-class RST page and its toctree entry |
| ⑧ §8 | run the validator, `verify_sync.py`, skill tests, both suites, and the quality gate |

`[x] §2` on every row records the 2026-11-24 bulk package move; other steps show their evidence inline when it differs from the legend.

## At a glance

| # | Class | Interface | Legacy source | Sites | Owned | Steps | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `irp_statechart_api_report` | IRPStatechart | `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_statechart.py` | — | — | 7/8 (①②③④⑥⑦⑧) | ⬜ open |
| 2 | `irp_stereotype_api_report` | IRPStereotype | `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_stereotype.py` | — | — | 6/8 (①②③④⑥⑦) | ⬜ open |
| 3 | `irp_actor_api_report` | IRPActor | `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_actor.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 4 | `irp_exception_api_report` | IRPException | — | — | 0 | 0/8 | ⬜ open |
| 5 | `irp_extension_point_api_report` | IRPExtensionPoint | — | — | 0 | 0/8 | ⬜ open |
| 6 | `irp_classifier_remediation` | IRPClassifier | — | — | — | 7/8 (①②③④⑤⑥⑦) | ⬜ open |
| 7 | `irp_association_class_remediation` | IRPAssociationClass | — | — | — | 6/8 (①②③④⑥⑦) | ⬜ open |
| 8 | `irp_operation_remediation` | IRPOperation | — | — | — | 6/8 (①②③④⑥⑦) | ⬜ open |
| 9 | `irp_class_remediation` | IRPClass | — | — | — | 6/8 (①②③④⑥⑦) | ⬜ open |
| 10 | `irp_use_case_remediation` | IRPUseCase | — | — | — | 6/8 (①②③④⑥⑦) | ⬜ open |

## Row details

<details>
<summary><code>irp_statechart_api_report</code> · IRPStatechart · 7/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 1/8 steps still open.
- **Note:** the wrapper/tests had already been moved to the canonical package. Registered typelib was available on 2026-11-25; `docs/reports/com/telelogic/rhapsody/core/IRPStatechart_api_report.md` and the catalog entry were generated. JavaDoc declares 32 owned members; validator reports 0 actionable deviations after the sync.
- **Audit (2026-11-26):** compliant with the current rhapsody-sync rules. Validator 0 actionable (2 `not-exposed` stubs: `addNewAcceptEventAction`, `addNewAcceptTimeEvent`); every catalog-exposed member keeps its COM binding, including `overrideInheritance`, `unoverrideInheritance`, and `addNewEdgeByType`, whose live failures stay open blockers. `verify_sync` passes, including `--strict-getters`. Unit 33 passed at 96 statements / 50 branches (100%); skill harness 90 passed; live statechart integration 26 passed. Step 5 stays open on live blockers only.
- [x] ① §1 — per-run checklist published with all 32 owned JavaDoc members and 9 getter fixture rows; inherited APIs tracked separately.
- [x] ② §2 — JavaDoc package, canonical wrapper, exports, mirrored unit/integration paths confirmed; no shim or class move required.
- [x] ③ §3 — typelib catalog refreshed and manual exception decisions preserved; all 32 JavaDoc members reconciled. `addNewAcceptEventAction` and `addNewAcceptTimeEvent` are documented-unavailable; all other bindings match catalog member and shape. `validate_interface.py IRPStatechart --source authority`: 0 actionable deviations.
- [x] ④ §4 — updated fake-COM tests failed first (21 red), then passed; focused file 33 passed; full unit suite 2192 passed. Coverage: `PYTHONPATH=src python -m pytest tests/unit/models/com/telelogic/rhapsody/core/test_irp_statechart.py --cov=rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart --cov-report=term-missing -q -o addopts=` → 96 statements, 50 branches, 0 missing/partial, 100.00%.
- [ ] ⑤ §5 — mirrored test file passes 26 live tests. Open live blockers (no skip/xfail/exception-accepting tests): `AddNewEdgeByType` returns COM error `-2147221498` for JavaDoc-listed edge types; `OpenDiagramView` returns `-2147221504` outside the Rhapsody-Eclipse integration; `getInheritsFrom` did not return the base chart with real class generalization and base/derived charts; `overrideInheritance` / `unoverrideInheritance` return `-2147467263` (`E_NOTIMPL`) in that setup. These require a working live fixture/runtime or user approval before any runtime stub. Getter matrix row for `getInheritsFrom` remains open.
- [x] ⑥ §6 — moved stable `SWR_ELEM_00011` into `docs/requirements/com/telelogic/rhapsody/core/irp_statechart.md`; added blocked live-limitation requirement `SWR_ELEM_00036`.
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_statechart.rst` documents all 32 public members; added to the package toctree and updated the legacy element label.
- [x] ⑧ §8 — report regenerated with `python scripts/validate_model_api.py IRPStatechart --source authority --path docs/reports` (0 actionable; 2 documented-unavailable stubs; 30 correct bindings); getter matrix/diff regenerated by script. `verify_sync.py IRPStatechart --strict-getters` green (5 property rows OK); skill harness 90 passed; full unit suite 2199 passed; focused coverage 96 statements / 50 branches, 100.00%; integration collection 26 tests; ruff/black/mypy clean. Row stays open only for §5 live blockers above.

</details>

<details>
<summary><code>irp_stereotype_api_report</code> · IRPStereotype · 6/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 2/8 steps still open.
- **Note:** wrapper and unit test were already in the canonical package; report-declared package verified against JavaDoc. The typelib reports 6 Java-owned members, 5 COM members (2 methods + 3 properties), with `isNewTerm` readable and writable.
- [x] ① §1 — published a six-member checklist and getter matrix; inherited IRPClassifier/IRPUnit/IRPModelElement members kept separate.
- [x] ② §2 — canonical wrapper and unit test confirmed; no compatibility shim. Added the missing mirrored integration test package file and per-class docs.
- [x] ③ §3 — generated `IRPStereotype_api_report.md` and appended only the live typelib catalog/signature entry, preserving other interfaces. Converted `icon`, `is_new_term` (read/write), and `of_meta_class` to properties; report has 0 actionable deviations. `setIsNewTerm` maps to the writable `isNewTerm` property setter.
- [x] ④ §4 — three property-shape tests failed first; implementation then passed focused unit (7 passed) and full unit (2198 passed). Coverage: `PYTHONPATH=src python -m pytest tests/unit/models/com/telelogic/rhapsody/core/test_irp_stereotype.py --cov=rhapsody_cli.models.com.telelogic.rhapsody.core.irp_stereotype --cov-report=term-missing -q -o addopts=` → 21 statements, 4 branches, 0 missing/partial, 100.00%.
- [ ] ⑤ §5 — 5 live tests pass (add/remove metaclass, `is_new_term` round-trip, populated `of_meta_class`, and new stereotype icon empty-state). Open populated getter blocker: a newly created stereotype has no icon, `icon` is typelib read-only, JavaDoc defines no setter, and no documented API attaches an icon file; the empty-state case is additional only. Recorded as `SWR_ELEM_00038`.
- [x] ⑥ §6 — created `docs/requirements/com/telelogic/rhapsody/core/irp_stereotype.md` with `SWR_ELEM_00037` and blocked getter requirement `SWR_ELEM_00038`; no Stereotype entry existed in the legacy monolith to move.
- [x] ⑦ §7 — added `docs/api/com/telelogic/rhapsody/core/irp_stereotype.rst` documenting all 5 Python public members and linked it in the package toctree; `verify_sync.py IRPStereotype` passes.
- [ ] ⑧ §8 — pending full quality and suite run for the group before this class commit; focused coverage/integration and targeted validator/verifier already pass. Keep the class row open for the populated icon getter fixture until a documented source is available.
- Getter fixture matrix: `is_new_term`—package stereotype, writable property set to 1 then 0, assert both values, `test_is_new_term`, delete package; `of_meta_class`—package stereotype plus documented `add_meta_class("Class")`, assert `Class` in returned comma-separated metaclasses, `test_of_meta_class`, delete package; `icon`—new package stereotype returns empty, `test_icon_empty_for_stereotype_without_custom_icon`, delete package; positive icon attachment remains blocked under `SWR_ELEM_00038`.

</details>

<details>
<summary><code>irp_actor_api_report</code> · IRPActor · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** wrapper and tests were already canonical. Typelib confirms four Java-owned members; pywin exposes `isBehaviorOverriden` as a writable property and lacks the other two Java methods.
- [x] ① §1 — expanded checklist for all four owned members; documented-unavailable members and the behavior-override getter fixture tracked separately.
- [x] ② §2 — JavaDoc package, canonical wrapper/unit/integration paths, inheritance and Actor registration confirmed; no compatibility shim.
- [x] ③ §3 — generated report/catalog/signatures; 0 actionable deviations. `is_behavior_overriden` now maps to the property; `addEventReceptionWithEvent` and `updateContainedDiagramsOnServer(int)` are documented-unavailable stubs with preserved Java signatures.
- [x] ④ §4 — property/unavailable-member tests failed first, then focused unit passed 5 tests; coverage 14 statements / 0 branches, 100.00%.
- [x] ⑤ §5 — 3 tests pass, including the property round-trip and both documented-unavailable stubs through a real actor fixture; no skip/xfail or non-NotImplementedError assertions.
- [x] ⑥ §6 — moved stable `SWR_ELEM_00005` into `docs/requirements/com/telelogic/rhapsody/core/irp_actor.md`.
- [x] ⑦ §7 — added `docs/api/com/telelogic/rhapsody/core/irp_actor.rst` for the 3 Python public members and linked it in the package toctree.
- [x] ⑧ §8 — validator and `verify_sync.py` report 0 actionable deviations; skill harness 49 passed. Full unit suite 2197 passed; full integration suite 468 passed / 8 failed, the same 8 application failures as baseline (467 passed / 8 failed); focused Actor integration 3 passed. Full ruff/black/mypy passed. Sphinx dummy build exited 0 with expected H2 requirement/report-toctree warnings and no API RST diagnostics.
- Getter fixture matrix: `getIsBehaviorOverriden()` / `is_behavior_overriden` — real package-owned actor; set writable property to `True`; assert property reads `True` and round-trip back to `False`; `tests/integration/models/com/telelogic/rhapsody/core/test_irp_actor.py::test_is_behavior_overriden`; delete actor/package.

</details>

<details>
<summary><code>irp_exception_api_report</code> · IRPException · 0/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** blocked: JavaDoc HTML absent under `docs/java_api/`; verify_sync fails.
- **Note:** The group ledger's earlier "0 owned methods" note is not JavaDoc evidence and is not accepted as a disposition.
- [ ] ① §1 — blocked because the target JavaDoc file is absent; no owned members can be safely enumerated.
- [ ] ② §2 — `python .agents/skills/rhapsody-sync/scripts/validate_interface.py IRPException --source typelib` exits 2: `IRPException` JavaDoc not found under `docs/java_api`; package cannot be verified against JavaDoc.
- [ ] ③ §3 — blocked by missing `docs/java_api/com/telelogic/rhapsody/core/IRPException.html`; no report was generated. Do not infer the interface has zero owned members from the former ledger note.
- [ ] ④ §4 — not started; wrapper/tests unchanged because JavaDoc evidence is missing.
- [ ] ⑤ §5 — not started; member inventory unavailable.
- [ ] ⑥ §6 — not changed; cannot verify whether an entry exists or determine JavaDoc summary.
- [ ] ⑦ §7 — not changed; cannot document unverified public members.
- [ ] ⑧ §8 — blocked, validator exit 2. Resume only after JavaDoc is restored under `docs/java_api/<package>/IRPException.html`.

</details>

<details>
<summary><code>irp_extension_point_api_report</code> · IRPExtensionPoint · 0/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** blocked: JavaDoc HTML absent under `docs/java_api/`; verify_sync fails.
- **Note:** The group ledger's earlier “0 owned methods” note is not JavaDoc evidence and is not accepted as a disposition.
- [ ] ① §1 — blocked because the target JavaDoc file is absent; no owned members can be safely enumerated.
- [ ] ② §2 — `python .agents/skills/rhapsody-sync/scripts/validate_interface.py IRPExtensionPoint --source typelib` exits 2: JavaDoc not found under `docs/java_api`; package cannot be verified against JavaDoc.
- [ ] ③ §3 — blocked by missing `docs/java_api/com/telelogic/rhapsody/core/IRPExtensionPoint.html`; no report was generated. Do not infer the interface has zero owned members from the former ledger note.
- [ ] ④ §4 — not started; wrappers/tests unchanged because JavaDoc evidence is missing.
- [ ] ⑤ §5 — not started; member inventory unavailable.
- [ ] ⑥ §6 — not changed; cannot verify whether an entry exists or determine JavaDoc summary.
- [ ] ⑦ §7 — not changed; cannot document unverified public members.
- [ ] ⑧ §8 — blocked, validator exit 2. Resume only after JavaDoc is restored under `docs/java_api/<package>/IRPExtensionPoint.html`.

</details>

<details>
<summary><code>irp_classifier_remediation</code> · IRPClassifier · 7/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 1/8 steps still open. Duplicate row for IRPClassifier also in Group-classifiers-2.md.
- **Note:** Closed by PR #168 (merged) — removes the COM-only `add_port` wrapper, adds the positive `find_trigger` live assertion, and records the populated `source_artifacts`, `sequence_diagrams`, and `links` fixtures added upstream in #164/#166.
- [x] ① §1 — 46 Java-owned members are inventoried; the 17 Python collection properties have populated identity/value rows in `docs/reports/sync-todo/getter-matrix.md`. The three method getters `get_attributes_including_bases`, `get_interface_items_including_bases`, and `get_relations_including_bases` each have populated assertions.
- [x] ② §2 — canonical wrapper/tests/exports and inherited scope verified; no compatibility shim.
- [x] ③ §3 — 46 Java members match 46 Python members and 46 pywin32 members; 0 actionable deviations. `add_port` is absent; the CLI uses inherited `add_new_aggr`.
- [x] ④ §4 — fake-COM tests and full unit suite pass; focused classifier unit coverage is 132 statements / 58 branches, 100.00%.
- [x] ⑤ §5 — classifier integration file passes 22 tests. Populated getter assertions include attributes, base/derived/generalizations, interface items (including bases), links, nested classifiers, operations, ports, relations (including bases), sequence diagrams, source artifacts, statechart, activity/behavioral diagrams, flows/flow items; `find_trigger` now finds a real triggered operation. Fixtures clean up their test packages.
- [x] ⑥ §6 — `irp_classifier.md` describes the wrapper without the removed `add_port` helper.
- [x] ⑦ §7
- [ ] ⑧ §8 — unit 2200 passed on Windows; classifier integration 22 passed; `validate_interface.py` and `verify_sync.py IRPClassifier` pass; ruff/black/mypy clean. Full integration run on Windows: 472 passed / 15 failed. The 7 failures outside this class (`test_irp_package`, `test_irp_project`, `test_irp_application`) reproduce in isolation on `main`; 8 are pre-existing application failures. Row stays open until those are resolved or accepted as blockers under `docs/superpowers/specs/2026-11-25-integration-test-failures-design.md`.

</details>

<details>
<summary><code>irp_association_class_remediation</code> · IRPAssociationClass · 6/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 2/8 steps still open. Duplicate row for IRPAssociationClass also in Group-classifiers-2.md.
- **Baseline:** end1, end2, and is_class are property-shaped; integration test asserts AttributeError on a regular association; test docstring contains stale xfail text.
- [x] ① §1 — 3 owned members (`end1`, `end2`, `is_class` getter/setter) rendered in the 2026-11-24 sync report; getter matrix rows name the two real relation ends from `add_relation_to` / `get_inverse`, the `add_association` fixture, identity assertions, mirrored test path, and package cleanup.
- [x] ② §2
- [x] ③ §3 — `validate_interface.py IRPAssociationClass --source authority` — 3 MATCH, 0 actionable, 0 deviations; `IRPModelElement.add_association(end1, end2, name)` is the documented fixture used by the mirrored integration test.
- [x] ④ §4 — focused unit 6 passed, 20 statements / 0 branches, 100.00%; full unit 2164 passed.
- [ ] ⑤ §5 — `test_add_association_with_real_relation_ends` fails because `IRPPackage.add_association(end1, end2, name)` returns an `IRPModelElement`, not `IRPAssociationClass`. The `end1`/`end2`/`is_class` getters are unverified on a real association class until that return type is resolved. No exception assertion or xfail is used.
- [x] ⑥ §6 — per-class requirement entry documents the three property-shaped owned members and the `add_association` fixture; Last Changed 2026-11-24.
- [x] ⑦ §7 — anchor + API reference with `end1`, `end2`, `is_class`; `verify_sync.py IRPAssociationClass` exits 0.
- [ ] ⑧ §8 — validator 0 actionable deviations; `verify_sync.py IRPAssociationClass` passes; skill harness 85 passed; unit 2200 passed on Windows. Open: the Section 5 live blocker above. Full integration on Windows: 472 passed / 15 failed (failures outside this class are listed under IRPClassifier Section 8).

</details>

<details>
<summary><code>irp_operation_remediation</code> · IRPOperation · 6/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 2/8 steps still open. Duplicate row for IRPOperation also in Group-classifiers-2.md.
- **Baseline:** 15 property-shaped members; integration test asserts AttributeError for get_flowchart.
- [x] ① §1 — 21-member checklist rendered in the 2026-11-24 sync report; getter matrix rows for `body`, `flowchart`, `initializer`, `returns`, `visibility`, all flags, and the documented-unavailable server-diagram method.
- [x] ② §2
- [x] ③ §3 — report regenerated — 20 MATCH, 0 actionable, 1 `UNAVAILABLE_DOCUMENTED` (`update_contained_diagrams_on_server`); `get_flowchart` is now the `flowchart` pywin32 property with a real `create_auto_flow_chart` fixture; no exception assertion remains.
- [x] ④ §4 — focused unit 28 passed, 96 statements / 0 branches, 100.00%; full unit 2164 passed.
- [ ] ⑤ §5 — `test_flowchart_getters` creates an operation, generates a real flowchart, asserts the getter returns it and `delete_flowchart` succeeds; `update_contained_diagrams_on_server` stub asserted in the mirrored integration file. Blocker: no Rhapsody on macOS — 472 integration tests collect only; live assertions unverified.
- [x] ⑥ §6 — `SWR_ELEM_00006` description corrected to the `UNAVAILABLE_DOCUMENTED` `NotImplementedError` stub (was stale `PYWIN32_MEMBER_MISSING` direct-call text); Last Changed 2026-11-24.
- [x] ⑦ §7 — anchor `.. _rhapsody-java-interface-IRPOperation:` plus 15 `autoproperty` and 6 `automethod` directives; `verify_sync.py IRPOperation` exits 0.
- [ ] ⑧ §8 — report regenerated (0 actionable), verify_sync exit 0, skill harness 49 passed, full unit 2164, ruff/black clean, integration collection 472. Blocker: Windows live integration closeout per the machine-split decision.

</details>

<details>
<summary><code>irp_class_remediation</code> · IRPClass · 6/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 2/8 steps still open. Duplicate row for IRPClass also in Group-core-1.md.
- **Baseline:** property shape already conforms; 2 integration tests assert RhapsodyRuntimeException.
- [x] ① §1 — 26 Python members rendered in the 2026-11-24 sync report; getter matrix rows for `attributes`, `operations`, `nested_classifiers`, `interface_items`, `ports`, `relations`, all collection/identity getters with real created children and package cleanup.
- [x] ② §2
- [x] ③ §3 — report regenerated — 0 actionable, 2 `UNAVAILABLE_DOCUMENTED` (`add_event_reception_with_event`, `update_contained_diagrams_on_server`), both JavaDoc-present / pywin32-absent stubs asserted at both layers; no `RhapsodyRuntimeException` assertion remains in the mirrored integration file.
- [x] ④ §4 — focused unit 34 passed, 77 statements / 0 branches, 100.00%; full unit 2164 passed.
- [ ] ⑤ §5 — all integration cases use authentic created classes/packages and assert real outcomes; no exception assertions remain. Blocker: no Rhapsody on macOS — 472 integration tests collect only; live assertions unverified. Open data item: `pywin32_authority.json` still lists OSLC members in `documented_unavailable` although the catalog exposes them (validator warns, entry ignored).
- [x] ⑥ §6 — per-class requirement entry documents the owned members and the two documented-unavailable stubs; Last Changed 2026-11-24.
- [x] ⑦ §7 — anchor + API reference covering all 26 public members; `verify_sync.py IRPClass` exits 0.
- [ ] ⑧ §8 — report regenerated (0 actionable), verify_sync exit 0, skill harness 49 passed, full unit 2164, ruff/black clean, integration collection 472. Blocker: Windows live integration closeout per the machine-split decision.

</details>

<details>
<summary><code>irp_use_case_remediation</code> · IRPUseCase · 6/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 2/8 steps still open. Duplicate row for IRPUseCase also in Group-classifiers-2.md.
- **Baseline:** 4 property-shape conversions; 3 integration tests assert TypeError; two JavaDoc-only methods already have unavailable stubs.
- [x] ① §1 — 15-member checklist rendered in the 2026-11-24 sync report; getter matrix rows for `extension_points`, `entry_points`, `describing_diagrams`, `is_behavior_overriden` with real created use cases/generalizations, identity assertions, mirrored test path, and package cleanup.
- [x] ② §2
- [x] ③ §3 — JavaDoc shows `findEntryPoint/findExtensionPoint(IRPGeneralization gen) -> String` and pywin32 declares a `com` parameter; wrapper now unwraps `gen._com` and returns `str`; report regenerated — 0 actionable, 2 `UNAVAILABLE_DOCUMENTED`; no `TypeError` assertion remains.
- [x] ④ §4 — focused unit 22 passed, 39 statements / 0 branches, 100.00%; both find-method unit cases assert the COM object argument and string result; full unit 2164 passed.
- [ ] ⑤ §5 — mirrored integration file now builds a real `IRPGeneralization` from two classes for both find cases and asserts the documented `str` outcome; entry/extension point cases use unique authentic names. Blocker: no Rhapsody on macOS — 472 integration tests collect only; live assertions unverified.
- [x] ⑥ §6 — `SWR_ELEM_00012` now records the corrected `IRPGeneralization`/`String` contract for both find methods; Last Changed 2026-11-24.
- [x] ⑦ §7 — anchor + `automethod` entries for all 15 public members; `verify_sync.py IRPUseCase` exits 0.
- [ ] ⑧ §8 — report regenerated (0 actionable), verify_sync exit 0, skill harness 49 passed, full unit 2164, ruff/black clean, integration collection 472. Blocker: Windows live integration closeout per the machine-split decision.

</details>
