# Sync todo — `containment` (group 1 of 2)

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
| 1 | `irp_component_api_report` | IRPComponent | `elements/containment/model_component.py` | 17 | 43 | 7/8 (①②③④⑥⑦⑧) | ⬜ open |
| 2 | `irp_collaboration_api_report` | IRPCollaboration | `elements/containment/model_collaboration.py` | 1 | 39 | 7/8 (①②③④⑥⑦⑧) | ⬜ open |
| 3 | `irp_configuration_api_report` | IRPConfiguration | `rhapsody_cli/models/elements/containment/model_configuration.py` | 23 | 46 | 7/8 (①②③④⑥⑦⑧) | ⬜ open |
| 4 | `irp_node_api_report` | IRPNode | `rhapsody_cli/models/elements/containment/model_node.py` | 2 | 6 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 5 | `irp_component_instance_api_report` | IRPComponentInstance | `rhapsody_cli/models/elements/containment/model_component_instance.py` | 0 | 3 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 6 | `irp_profile_api_report` | IRPProfile | `rhapsody_cli/models/elements/containment/model_profile.py` | 0 | 0 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 7 | `irp_module_api_report` | IRPModule | `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_module.py` | 0 | 0 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ evidenced |
| 8 | `irp_package_remediation` | IRPPackage | — | — | 69 | 5/8 (②③④⑥⑦) | ⬜ open |
| 9 | `irp_project_remediation` | IRPProject | — | — | — | 6/8 (①②③④⑥⑦) | ⬜ open |
| 10 | `irp_package_api_report` | IRPPackage | `models/elements/containment/model_package.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |

## Row details

<details>
<summary><code>irp_component_api_report</code> · IRPComponent · 7/8 steps · ⬜ open</summary>

- **Status (2026-11-27):** verify_sync passes; 7/8 steps complete. §5 stays open on two populated-getter blockers.
- **Note:** core structural element (118 src / 29 test, 43 JavaDoc members). Wrapper stays canonical; 12 accessor pairs migrated to COM properties, three JavaDoc-only members become documented `NotImplementedError` stubs.
- [x] ① §1 — 43 owned members reconciled; 12 getter-matrix rows covered (10 populated, 2 blocked).
- [x] ② §2 — canonical wrapper/tests/exports verified; no module move required.
- [x] ③ §3 — report regenerated from authority: 0 actionable deviations, 2 expected binding differences; `get_path`, `set_path`, `update_contained_diagrams_on_server` recorded in the stub ledger.
- [x] ④ §4 — 42 fake-COM unit tests, 100% statements/branches (110 statements, 0 branches); full unit suite 2231 passed.
- [ ] ⑤ §5 — 13 integration tests with real components/configurations/files/scope elements; `panel_diagrams` and `variation_points` have no documented child-attachment API (P0 blockers in `index.md`); live execution is Windows-only.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_component.md`.
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_component.rst` documents all 37 public members; toctree entry added.
- [x] ⑧ §8 — validator 0 actionable; `verify_sync.py IRPComponent --strict-getters` green; skill harness 90 passed; integration collection 13 tests; ruff/black/mypy clean.

</details>

<details>
<summary><code>irp_collaboration_api_report</code> · IRPCollaboration · 7/8 steps · ⬜ open</summary>

- **Status (2026-11-27):** verify_sync passes; 7/8 steps complete. §5 stays open on read-only getter blockers.
- **Note:** common containment wrapper (77 src / 11 test, 39 owned members). Ten JavaDoc getters map to pywin32 properties; the rest stay method-shaped.
- [x] ① §1 — 39 owned members reconciled; 10 getter-matrix rows (1 populated, 9 blocked).
- [x] ② §2 — canonical wrapper/tests/exports verified; no module move required.
- [x] ③ §3 — report regenerated from authority: 0 actionable deviations.
- [x] ④ §4 — 43 fake-COM unit tests, 100% statements/branches (104 statements, 6 branches); full unit suite 2277 passed.
- [ ] ⑤ §5 — 10 integration tests with a real collaboration; `messages` populated via `add_message`, nine read-only getters blocked by absent population APIs (P0 in `index.md`); live execution is Windows-only.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_collaboration.md`.
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_collaboration.rst` documents all 39 public members; toctree entry added.
- [x] ⑧ §8 — validator 0 actionable; `verify_sync.py IRPCollaboration --strict-getters` green; ruff/black/mypy clean.

</details>

<details>
<summary><code>irp_configuration_api_report</code> · IRPConfiguration · 7/8 steps · ⬜ open</summary>

- **Status (2026-11-27):** verify_sync passes; 7/8 steps complete. §5 stays open on read-only getter blockers.
- **Note:** usage 73 src / 16 test refs, 46 owned members. Sixteen accessor pairs mapped to COM properties; `get_path`/`set_path` are documented unavailable stubs.
- [x] ① §1 — 46 owned members reconciled; 16 getter-matrix rows (all empty/default with blockers).
- [x] ② §2 — canonical wrapper/tests/exports verified; no module move required.
- [x] ③ §3 — report regenerated from authority: 0 actionable deviations; path stubs recorded in the ledger.
- [x] ④ §4 — 48 fake-COM unit tests, 100% statements/branches (129 statements, 0 branches); full unit suite 2315 passed.
- [ ] ⑤ §5 — 17 integration tests with a real configuration; populated fixtures for read-only getters blocked by absent APIs (P0 in `index.md`); live execution is Windows-only.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_configuration.md`.
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_configuration.rst` documents all 33 public members; toctree entry added.
- [x] ⑧ §8 — validator 0 actionable; `verify_sync.py IRPConfiguration --strict-getters` green; skill harness 90 passed; ruff/black/mypy clean.

</details>

<details>
<summary><code>irp_node_api_report</code> · IRPNode · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-27):** verify_sync passes; all steps archived.
- **Note:** usage 30 src / 13 test refs, 6 owned members. Two accessor pairs mapped to pywin32 properties; component-instance methods stay method-shaped.
- [x] ① §1
- [x] ② §2 — canonical wrapper unchanged; tests/exports verified.
- [x] ③ §3 — report regenerated from authority: 0 actionable deviations.
- [x] ④ §4 — 8 fake-COM unit tests, 100% statements/branches; full unit suite 2314 passed.
- [x] ⑤ §5 — 3 integration tests with real nodes and component instances; macOS = collection-only.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_node.md`.
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_node.rst` + toctree entry.
- [x] ⑧ §8 — validator 0 actionable; verify_sync + --strict-getters green; ruff/black/mypy clean.

</details>

<details>
<summary><code>irp_component_instance_api_report</code> · IRPComponentInstance · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-27):** verify_sync passes; all steps archived.
- **Note:** usage 21 src / 11 test refs, 3 owned members. Two accessor pairs mapped to COM-backed properties.
- [x] ① §1
- [x] ② §2 — canonical wrapper/tests/exports verified.
- [x] ③ §3 — report regenerated from authority: 0 actionable deviations.
- [x] ④ §4 — 4 fake-COM unit tests, 100% statements/branches; full unit suite 2313 passed.
- [x] ⑤ §5 — 2 integration tests with real nodes and component instances; macOS = collection-only.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_component_instance.md`.
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_component_instance.rst` + toctree entry.
- [x] ⑧ §8 — validator 0 actionable; verify_sync + --strict-getters green; ruff/black/mypy clean.

</details>

<details>
<summary><code>irp_profile_api_report</code> · IRPProfile · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-27):** verify_sync passes; all steps archived.
- **Note:** usage 12 src / 8 test refs, 0 owned members. Inheritance-only wrapper extending IRPPackage.
- [x] ① §1
- [x] ② §2 — canonical wrapper/tests/exports verified; `from __future__` header added.
- [x] ③ §3 — no owned JavaDoc members or catalog members; 0 actionable deviations.
- [x] ④ §4 — existing fake-COM registration tests pass; full unit suite 2313 passed.
- [x] ⑤ §5 — 1 integration test creating a real profile via `IRPProject.add_profile`; macOS = collection-only.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_profile.md`.
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_profile.rst` + toctree entry.
- [x] ⑧ §8 — validator 0 actionable; verify_sync + --strict-getters green; ruff/black/mypy clean.

</details>

<details>
<summary><code>irp_module_api_report</code> · IRPModule · 8/8 steps evidenced · ✅ evidenced</summary>

- **Status (2026-11-26):** verify_sync passes; validator 0 actionable. IRPModule declares no own members (extends IRPInstance); its only owned behavior, live registration via `IRPPackage.add_module`, is covered by `tests/integration/models/com/telelogic/rhapsody/core/test_irp_module.py`.
- **Note:** usage 8 src / 8 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [x] ① §1 — no own members; inherited members owned by IRPInstance/IRPRelation/IRPUnit/IRPModelElement.
- [x] ② §2 — canonical package, mirrored unit/integration tests, RST toctree entry; `from __future__` header added.
- [x] ③ §3 — typelib catalog entry merged (inherited surface only); validator 0 actionable.
- [x] ④ §4 — unit `test_irp_module.py` 2 passed, `irp_module.py` 6 statements / 0 branches, 100.00%.
- [x] ⑤ §5 — live `add_module` integration test passes (1 passed).
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_module.md` holds SWR_ELEM_00041.
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_module.rst` added to the toctree.
- [x] ⑧ §8 — `verify_sync.py IRPModule` and `--strict-getters` pass; skill harness 90 passed; unit suite 2201 passed; ruff/black/mypy clean.

</details>

<details>
<summary><code>irp_package_remediation</code> · IRPPackage · 5/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 7/8 steps still open.
- **Baseline:** 8 arity mismatches; 8 disallowed integration exception assertions; 30 property-shape conversions; add_association is a COM-only extension (D2 default: retain and document).
- [ ] ① §1 — member checklist and getter matrix published.
- [x] ② §2
- [x] ③ §3 — 94 matched and six documented-unavailable; no actionable rows, signature mismatches, or property-shape mismatches remain. Inherited `add_association` is supplied by `IRPModelElement`.
- [x] ④ §4 — the inheritance assertion failed with the child override, then passed after removing it; the documented remote-mode string test failed against the old `int` conversion, then passed after correcting the wrapper to `str`. Focused unit file 174 passed with 100% statement/branch coverage (261 statements; 0 branch points); full unit suite 2201 passed.
- [ ] ⑤ §5 — 98 passed; all 30/30 getter properties have populated identity/value assertions. `add_link` and `add_link_between_sysml_ports` have real live tests. A local `get_remote_requirements_populate_mode` probe after setting `"None"` returned `""`; a Design Manager server is required for a valid value. Full integration suite: 491 passed, 0 failed (baseline 481 passed, 6 failed).
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_package.md` updated to record inherited `add_association` ownership, generic-factory getter fixtures, and populated `links` integration coverage.
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_package.rst` has valid directives for the 69 owned methods and 30 properties; the inherited `add_association` directive was removed. `verify_sync.py` passes and `sphinx-build -b dummy docs docs/_build/irppackage` succeeds with no IRPPackage page autodoc failures (52 repository-wide warnings remain).
- [ ] ⑧ §8 — the P0 Design Manager getter precondition remains; do not archive until it has valid live evidence. The full integration suite passes 491 tests.

</details>

<details>
<summary><code>irp_project_remediation</code> · IRPProject · 6/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** validator reports zero actionable deviations; five JavaDoc-only pywin32-absent methods are documented stubs. Keep open for live preconditions listed below.
- **Baseline:** 2201 unit tests and 493 live integration tests passed before this sync; the validator had 12 actionable deviations.
- [x] ① §1 — direct JavaDoc inventory and owned getter matrix are recorded in the API report and getter matrix; inherited package members are not child-owned.
- [x] ② §2 — canonical wrapper/test/doc paths and `IRPPackage` inheritance verified.
- [x] ③ §3 — all 72 Java members reconciled; zero actionable deviations; exact signatures corrected and six duplicate package-member overrides removed.
- [x] ④ §4 — focused fake-COM suite passed; `irp_project.py` coverage is 100% (162 statements, 116 branches); full unit suite 2204 passed.
- [ ] ⑤ §5 — full live integration suite 489 passed. Keep open: active component/configuration reads and string setters fault on this Rhapsody build; no populated project-root node fixture or simplified-model package exists; deprecated Design Manager methods lack a supported server fixture. Other documented environment blockers remain in the P0 table.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_project.md` updated with inherited members, exact bindings, stubs, and live blockers.
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_project.rst` documents the current public wrapper surface, including `save`, resolve-on-demand stubs, and deprecated bindings.
- [ ] ⑧ §8 — validator, `verify_sync`, strict getter/inherited checks pass; Sphinx succeeds with 133 existing repository-wide warnings. Do not archive while the live preconditions in §5 remain open.

</details>

<details>
<summary><code>irp_package_api_report</code> · IRPPackage · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** 4 method-shaped (`getNamespace`, `getRemoteRequirementsPopulateMode`, `setRemoteRequirementsPopulateMode`, `getAllNestedElements`); `getRootInstanceSpecifications`/`rootInstanceSpecifications` absent from every catalog: blocker unless Windows typelib regen resolves it.
- [x] ① §1
- [x] ② §2
- [x] ③ §3 — baseline `validate_interface.py IRPPackage --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
- [x] ④ §4
- [x] ⑤ §5 — add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
- [x] ⑥ §6
- [x] ⑦ §7 — class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPPackage:` + deviation list-table)
- [x] ⑧ §8 — `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

</details>
