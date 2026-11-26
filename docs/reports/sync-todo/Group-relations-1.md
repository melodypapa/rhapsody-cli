# Sync todo — `relations` (group 1 of 1)

**8 classes** · ✅ 1 archived · ⬜ 7 open

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
| 1 | `irp_instance_api_report` | IRPInstance | `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_instance.py` | — | — | 6/8 (①②③④⑥⑦) | ⬜ open |
| 2 | `irp_relation_api_report` | IRPRelation | `elements/relations/model_relation.py` | 27 | 31 | 1/8 (②) | ⬜ open |
| 3 | `irp_dependency_api_report` | IRPDependency | `rhapsody_cli/models/elements/relations/model_dependency.py` | 2 | 7 | 1/8 (②) | ⬜ open |
| 4 | `irp_generalization_api_report` | IRPGeneralization | `rhapsody_cli/models/elements/relations/model_generalization.py` | 5 | 10 | 1/8 (②) | ⬜ open |
| 5 | `irp_association_role_api_report` | IRPAssociationRole | `rhapsody_cli/models/elements/relations/model_association_role.py` | 3 | 3 | 1/8 (②) | ⬜ open |
| 6 | `irp_hyper_link_api_report` | IRPHyperLink | `rhapsody_cli/models/elements/relations/model_hyperlink.py` | 2 | 5 | 1/8 (②) | ⬜ open |
| 7 | `irp_port_remediation` | IRPPort | — | — | — | 1/8 (②) | ⬜ open |
| 8 | `irp_port_api_report` | IRPPort | `models/elements/relations/model_port.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |

## Row details

<details>
<summary><code>irp_instance_api_report</code> · IRPInstance · 6/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; validator 0 actionable (2 documented-unavailable stubs); Step 5 and Step 8 open (see below).
- **Note:** the wrapper moved to the canonical package. The typelib catalog is merged for IRPInstance; `instantiated_by` is now a property (get/set) backed by `instantiatedBy`; `get_all_nested_elements` and `update_contained_diagrams_on_server` are documented-unavailable stubs.
- [x] ① §1 — 13-member JavaDoc inventory published in the wrapper checklist and the report.
- [x] ② §2 — canonical wrapper and mirrored unit test confirmed; report Java package line present; no compatibility shim.
- [x] ③ §3 — typelib catalog merged for IRPInstance only; validator 0 actionable; 12 Python members vs 13 Java members (2 stubs documented unavailable).
- [x] ④ §4 — 4 new tests failed first (red), then passed; `test_irp_instance.py` 16 passed, `irp_instance.py` 35 statements / 18 branches, 100.00%; full unit suite 2201 passed; ruff/black/mypy clean.
- [ ] ⑤ §5 — `test_irp_instance.py` has 2 live stub tests (`pytest.raises(NotImplementedError)`), both passing. Open blocker: no documented creation path for an `IRPInstance` is exposed by the registered typelib. `IRPPackage.addInstanceSpecification` is JavaDoc-only (pywin32 stub raises NotImplementedError), no catalog member adds an instance, and `add_new_aggr("Instance", …)` is not a valid creation route. The test project contains no instances, so the populated checks for `instantiated_by`, `get_attribute_value`/`set_attribute_value`, links, initializer arguments, and `add_relation_to_the_whole` cannot be built authentically. A second blocker is a design choice: objects returned to the wrapper expose the generic `IRPModelElement` interface, and `win32com.client.CastTo(obj, "IRPInstance")` reaches the instance members (probe-verified). Checked `docs/java_api/rational_rhapsody_api_getting_started.pdf`: its only object-creation sample is `IRPConfiguration.addInitialInstance(class)`. Probe-verified live: the call succeeds, but `initialInstances` returns the class itself (metaClass `Class`), not an IRPInstance, so this route does not create an IRPInstance either.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_instance.md` holds SWR_ELEM_00009 (moved from the legacy monolith, which no longer contains it).
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_instance.rst` documents all 12 public members; toctree entry added in `docs/api/elements.rst`.
- [ ] ⑧ §8 — `validate_interface.py`, `verify_sync.py`, skill harness (85 passed), unit suite (2201 passed), ruff/black/mypy and Sphinx (exit 0) pass. Open: `verify_sync.py --strict-getters` fails on `instantiated_by` (MISSING populated test) until Step 5 is resolved; full Windows integration run not repeated.

</details>

<details>
<summary><code>irp_relation_api_report</code> · IRPRelation · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** foundational relation type (108 src / 47 test, 31 owned methods). Do this before IRPInstance; 27 legacy sites make it the highest cleanup value in this group.
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
<summary><code>irp_dependency_api_report</code> · IRPDependency · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 33 src / 13 test refs, 7 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_generalization_api_report</code> · IRPGeneralization · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 24 src / 8 test refs, 10 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_association_role_api_report</code> · IRPAssociationRole · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 16 src / 8 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_hyper_link_api_report</code> · IRPHyperLink · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 13 src / 8 test refs, 5 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_port_remediation</code> · IRPPort · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 7/8 steps still open.
- **Baseline:** 5 property-shape conversions; the headless full-integration baseline has 2 port-test failures requiring evidence-based triage.
- [ ] ① §1 — member checklist and getter matrix published.
- [x] ② §2
- [ ] ③ §3 — all 5 property members and the two live failures reconciled against JavaDoc/catalog.
- [ ] ④ §4 — fake-COM tests first; full unit suite green; irp_port.py at 100% statements/branches.
- [ ] ⑤ §5 — create real provided/required interfaces and assert returned membership/value; resolve the two baseline failures.
- [ ] ⑥ §6 — irp_port.md checked/updated.
- [ ] ⑦ §7 — irp_port.rst checked/updated for every public member.
- [ ] ⑧ §8 — generated report, verify_sync, gates, live counts, and blockers recorded.

</details>

<details>
<summary><code>irp_port_api_report</code> · IRPPort · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** `getContract`/`setContract` ↔ `contract` — absent from every catalog: blocker unless Windows typelib regen resolves it.
- [x] ① §1
- [x] ② §2
- [x] ③ §3 — baseline `validate_interface.py IRPPort --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
- [x] ④ §4
- [x] ⑤ §5 — add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
- [x] ⑥ §6
- [x] ⑦ §7 — class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPPort:` + deviation list-table)
- [x] ⑧ §8 — `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

</details>
