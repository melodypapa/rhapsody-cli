# Sync todo — `relations`

**8 classes** · ✅ 1 archived · ⚠️ 1 complete with deviation · ⬜ 6 open

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
| 1 | `irp_instance_api_report` | IRPInstance | `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_instance.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ⚠️ complete with deviation |
| 2 | `irp_relation_api_report` | IRPRelation | `elements/relations/model_relation.py` | 27 | 31 | 1/8 (②) | ⬜ open |
| 3 | `irp_dependency_api_report` | IRPDependency | `rhapsody_cli/models/elements/relations/model_dependency.py` | 2 | 7 | 1/8 (②) | ⬜ open |
| 4 | `irp_generalization_api_report` | IRPGeneralization | `rhapsody_cli/models/elements/relations/model_generalization.py` | 5 | 10 | 1/8 (②) | ⬜ open |
| 5 | `irp_association_role_api_report` | IRPAssociationRole | `rhapsody_cli/models/elements/relations/model_association_role.py` | 3 | 3 | 1/8 (②) | ⬜ open |
| 6 | `irp_hyper_link_api_report` | IRPHyperLink | `rhapsody_cli/models/elements/relations/model_hyperlink.py` | 2 | 5 | 1/8 (②) | ⬜ open |
| 7 | `irp_port_remediation` | IRPPort | — | — | — | 7/8 (①②③④⑥⑦⑧) | ⬜ open |
| 8 | `irp_port_api_report` | IRPPort | `models/elements/relations/model_port.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |

## Row details

<details>
<summary><code>irp_instance_api_report</code> · IRPInstance · 8/8 steps · ⚠️ complete with deviation</summary>

- **Status (2026-03-19):** API sync is complete with deviation; `verify_sync.py IRPInstance --strict-getters` passes; issue #202 remains open for two live blockers. This is not a live-green claim.
- **Note:** the wrapper moved to the canonical package. `IRPInstance.__init__` casts a generic pywin dispatch to the concrete wrapper interface; integration fixtures use documented `IRPPackage.add_global_object` to create authentic typed objects. `instantiated_by` remains a read/write property backed by `instantiatedBy`; `get_all_nested_elements` and `update_contained_diagrams_on_server` are documented-unavailable stubs.
- [x] ① §1 — 13-member JavaDoc inventory published in the wrapper checklist and the report.
- [x] ② §2 — canonical wrapper and mirrored unit test confirmed; report Java package line present; no compatibility shim.
- [x] ③ §3 — typelib catalog merged for IRPInstance only; validator 0 actionable; 12 Python members vs 13 Java members (2 stubs documented unavailable).
- [x] ④ §4 — added test-first pywin dispatch casting (red then green); `test_irp_instance.py` unit module: 17 passed. The constructor casts to the concrete wrapper's exact Java interface; Ruff, Black, and mypy are clean.
- [x] ⑤ §5 — focused live tests: 6 passed, 2 explicitly user-approved skips. Using `addGlobalObject` and real class attributes verifies attribute-value round-trip, in/out links, initializer arguments, and explicit/implicit transitions. `addRelationToTheWhole` returns `None`; setting `instantiatedBy` to a constructor leaves getter readback `None`. Both live deviations are P0 rows and remain tracked in issue #202; not live-green.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_instance.md` holds SWR_ELEM_00009 (moved from the legacy monolith, which no longer contains it).
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_instance.rst` documents all 12 public members; toctree entry added in `docs/api/elements.rst`.
- [x] ⑧ §8 — `verify_sync.py IRPInstance --strict-getters`, the skill harness (90 passed), focused integration (6 passed / 2 approved skips), unit module (17 passed), subclass regression modules (31 passed), Ruff, Black, and mypy pass. The skipped live behavior is still an open P0 and issue #202; no live-green claim.

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
<summary><code>irp_port_remediation</code> · IRPPort · 7/8 steps · ⬜ open</summary>

- **Status (2026-03-19):** the two baseline live failures are resolved; strict getter verification passes. Step 5 remains open for populated provided/required interface retrieval.
- **Baseline:** both failures came from a generic `IRPModelElement` dispatch lacking `isBehavioral` / `providedInterfaces`; `IRPInstance.__init__` now casts to the concrete `IRPPort` interface. Focused integration is 2 passed. The separate mutator/populated-collection limitation remains tracked in the requirement and P0 index.
- [x] ① §1 — member checklist and getter matrix published.
- [x] ② §2
- [x] ③ §3 — five property bindings and both dispatch failures reconciled against JavaDoc/catalog; no IRPPort binding change was needed.
- [x] ④ §4 — fake-COM unit module: 17 passed; `irp_port.py` coverage is 100% statements and branches.
- [ ] ⑤ §5 — existing live tests pass, but no documented fixture populates `provided_interfaces` / `required_interfaces`; the four interface mutators remain blocked on this Rhapsody build.
- [x] ⑥ §6 — `irp_port.md` checked; the mutator deviation remains explicit.
- [x] ⑦ §7 — `irp_port.rst` checked for every public member.
- [x] ⑧ §8 — validator has 0 actionable deviations; `verify_sync.py IRPPort --strict-getters`, skill harness (90 passed), focused integration (2 passed), unit/coverage, Ruff, Black, and mypy pass. The P0 getter/mutator blocker remains open.

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
