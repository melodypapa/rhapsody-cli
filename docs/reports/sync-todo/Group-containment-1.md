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
| 1 | `irp_component_api_report` | IRPComponent | `elements/containment/model_component.py` | 17 | 43 | 1/8 (②) | ⬜ open |
| 2 | `irp_collaboration_api_report` | IRPCollaboration | `elements/containment/model_collaboration.py` | 1 | 39 | 1/8 (②) | ⬜ open |
| 3 | `irp_configuration_api_report` | IRPConfiguration | `rhapsody_cli/models/elements/containment/model_configuration.py` | 23 | 46 | 1/8 (②) | ⬜ open |
| 4 | `irp_node_api_report` | IRPNode | `rhapsody_cli/models/elements/containment/model_node.py` | 2 | 6 | 1/8 (②) | ⬜ open |
| 5 | `irp_component_instance_api_report` | IRPComponentInstance | `rhapsody_cli/models/elements/containment/model_component_instance.py` | 0 | 3 | 1/8 (②) | ⬜ open |
| 6 | `irp_profile_api_report` | IRPProfile | `rhapsody_cli/models/elements/containment/model_profile.py` | 0 | 0 | 1/8 (②) | ⬜ open |
| 7 | `irp_module_api_report` | IRPModule | `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_module.py` | 0 | 0 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ evidenced |
| 8 | `irp_package_remediation` | IRPPackage | — | — | 69 | 5/8 (②③④⑥⑦) | ⬜ open |
| 9 | `irp_project_remediation` | IRPProject | — | — | — | 1/8 (②) | ⬜ open |
| 10 | `irp_package_api_report` | IRPPackage | `models/elements/containment/model_package.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |

## Row details

<details>
<summary><code>irp_component_api_report</code> · IRPComponent · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** core structural element (118 src / 29 test, 43 owned methods). Extends the synced `IRPUnit`, so this is a leaf-style migration with no base-class dependency.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7
- [ ] ⑧ §8

</details>

<details>
<summary><code>irp_collaboration_api_report</code> · IRPCollaboration · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** common containment wrapper (77 src / 11 test, 39 owned methods). Extends the synced `IRPUnit`; low legacy-site count but high structural use closes the group.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7
- [ ] ⑧ §8

</details>

<details>
<summary><code>irp_configuration_api_report</code> · IRPConfiguration · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 73 src / 16 test refs, 46 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7
- [ ] ⑧ §8

</details>

<details>
<summary><code>irp_node_api_report</code> · IRPNode · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 30 src / 13 test refs, 6 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7
- [ ] ⑧ §8

</details>

<details>
<summary><code>irp_component_instance_api_report</code> · IRPComponentInstance · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 21 src / 11 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7
- [ ] ⑧ §8

</details>

<details>
<summary><code>irp_profile_api_report</code> · IRPProfile · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 12 src / 8 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7
- [ ] ⑧ §8

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
<summary><code>irp_project_remediation</code> · IRPProject · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 7/8 steps still open. Duplicate row for IRPProject also in Group-containment-2.md.
- **Baseline:** 21 arity mismatches; 24 disallowed integration exception assertions; 9 read-only and 1 writable property-shape conversions; 7 COM-only extensions (D2 default: retain and document).
- [ ] ① §1 — member checklist and getter matrix published.
- [x] ② §2
- [ ] ③ §3 — all 21 signatures, 9 read properties plus the writable property, and 7 extension dispositions reconciled.
- [ ] ④ §4 — fake-COM tests first; full unit suite green; irp_project.py at 100% statements/branches.
- [ ] ⑤ §5 — project getters establish live project state and assert returned identity/value; all 24 exception sites resolved or blocked.
- [ ] ⑥ §6 — irp_project.md checked/updated.
- [ ] ⑦ §7 — irp_project.rst checked/updated for every public member.
- [ ] ⑧ §8 — generated report, verify_sync, gates, live counts, and blockers recorded.

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
