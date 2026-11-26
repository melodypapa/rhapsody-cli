# Sync todo — `common` (group 1 of 1)

**7 classes** · ✅ 5 archived · ⬜ 2 open

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
| 1 | `irp_sys_ml_port_api_report` | IRPSysMLPort | `rhapsody_cli/models/elements/common/model_other_model.py` | 3 | 7 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 2 | `irp_classifier_role_api_report` | IRPClassifierRole | `rhapsody_cli/models/elements/common/model_other_model.py` | 1 | 8 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 3 | `irp_enumeration_literal_api_report` | IRPEnumerationLiteral | `rhapsody_cli/models/elements/common/model_misc.py` | 1 | 2 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 4 | `irp_constraint_api_report` | IRPConstraint | `rhapsody_cli/models/elements/common/model_misc.py` | 1 | 1 | 1/8 (②) | ⬜ open |
| 5 | `irp_comment_api_report` | IRPComment | `rhapsody_cli/models/elements/common/model_misc.py` | 0 | 0 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 6 | `irp_type_remediation` | IRPType | — | — | — | 1/8 (②) | ⬜ open |
| 7 | `irp_type_api_report` | IRPType | `models/elements/common/model_other_model.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |

## Row details

<details>
<summary><code>irp_sys_ml_port_api_report</code> · IRPSysMLPort · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-27):** verify_sync passes; all steps archived.
- **Note:** usage 42 src / 21 test refs, 7 owned members. Split `IRPSysMLPort` into `irp_sysml_port.py`; `IRPClassifierRole` stays in `irp_other_model.py` for its own row. Three JavaDoc accessor pairs map to read/write pywin32 properties; `add_link` uses `call_com`.
- [x] ① §1
- [x] ② §2 — canonical module `irp_sysml_port.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 8 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 4 integration tests with real flowports/instances/links; macOS = collection-only
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_sysml_port.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_sysml_port.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; unit suite 2198 passed; skill harness 90 passed; mypy/ruff/black clean

</details>

<details>
<summary><code>irp_classifier_role_api_report</code> · IRPClassifierRole · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-27):** verify_sync passes; all steps archived.
- **Note:** usage 34 src / 13 test refs, 8 owned members. Split `IRPClassifierRole` into `irp_classifier_role.py`; this was the last class in `irp_other_model.py`, so the empty shim was removed. Four JavaDoc accessor pairs map to pywin32 properties; the recursive-roles getter remains a method.
- [x] ① §1
- [x] ② §2 — canonical module `irp_classifier_role.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 9 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 5 integration tests with real lifelines/diagrams; macOS = collection-only
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_classifier_role.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_classifier_role.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; unit suite 2197 passed; skill harness 90 passed; mypy/ruff/black clean

</details>

<details>
<summary><code>irp_enumeration_literal_api_report</code> · IRPEnumerationLiteral · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-27):** verify_sync passes; all steps archived.
- **Note:** usage 21 src / 11 test refs, 2 owned members. Split `IRPEnumerationLiteral` into `irp_enumeration_literal.py`; siblings stay in `irp_misc.py`. The JavaDoc `getValue`/`setValue` pair maps to the pywin32 `value` property.
- [x] ① §1
- [x] ② §2 — canonical module `irp_enumeration_literal.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 3 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 1 integration test with a real enumeration literal; macOS = collection-only
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_enumeration_literal.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_enumeration_literal.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; unit suite 2196 passed; skill harness 90 passed; mypy/ruff/black clean

</details>

<details>
<summary><code>irp_constraint_api_report</code> · IRPConstraint · 7/8 steps · ⬜ open</summary>

- **Status (2026-11-27):** verify_sync passes; 7/8 steps complete. §5 stays open on the populated-getter blocker.
- **Note:** usage 9 src / 8 test refs, 1 owned member. Split `IRPConstraint` into `irp_constraint.py`; `IRPComment` stays in `irp_misc.py`. JavaDoc `getConstraintsByMe` maps to the read-only pywin32 `constraintsByMe` property.
- [x] ① §1
- [x] ② §2 — canonical module `irp_constraint.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 2 fake-COM unit tests, 100% statements/branches
- [ ] ⑤ §5 — 1 integration test asserts the documented empty state; populated `constraints_by_me` fixture blocked (no documented API attaches an affected element), recorded as P0 in `index.md`
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_constraint.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_constraint.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; unit suite 2195 passed; skill harness 90 passed; mypy/ruff/black clean

</details>

<details>
<summary><code>irp_comment_api_report</code> · IRPComment · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-27):** verify_sync passes; all steps archived.
- **Note:** usage 8 src / 7 test refs, 0 owned members. Split `IRPComment` into `irp_comment.py`; this was the last class in `irp_misc.py`, so the empty shim and its mirrored unit test were removed. Inheritance-only wrapper with no COM bindings.
- [x] ① §1
- [x] ② §2 — canonical module `irp_comment.py`; exports and direct imports updated
- [x] ③ §3 — 0 owned JavaDoc members, 0 catalog members, 0 actionable deviations
- [x] ④ §4 — 2 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 1 integration test creating a real comment via the generic factory; macOS = collection-only
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_comment.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_comment.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; unit suite 2195 passed; skill harness 90 passed; mypy/ruff/black clean

</details>

<details>
<summary><code>irp_type_remediation</code> · IRPType · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 7/8 steps still open.
- **Baseline:** 10 property-shape conversions; the headless full-integration baseline has 7 type-test failures requiring evidence-based triage.
- [ ] ① §1 — member checklist and getter matrix published.
- [x] ② §2
- [ ] ③ §3 — all 10 property members and seven live failures reconciled against JavaDoc/catalog.
- [ ] ④ §4 — fake-COM tests first; full unit suite green; irp_type.py at 100% statements/branches.
- [ ] ⑤ §5 — create a real enumeration/type fixture and assert getter values/identity; resolve the seven baseline failures.
- [ ] ⑥ §6 — irp_type.md checked/updated.
- [ ] ⑦ §7 — irp_type.rst checked/updated for every public member.
- [ ] ⑧ §8 — generated report, verify_sync, gates, live counts, and blockers recorded.

</details>

<details>
<summary><code>irp_type_api_report</code> · IRPType · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** RPClassifierRole (1) and RPSysMLPort (3) sites in the same module are uncovered — out of this row's scope.
- [x] ① §1
- [x] ② §2
- [x] ③ §3 — baseline `validate_interface.py IRPType --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
- [x] ④ §4
- [x] ⑤ §5 — add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
- [x] ⑥ §6
- [x] ⑦ §7 — class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPType:` + deviation list-table)
- [x] ⑧ §8 — `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

</details>
