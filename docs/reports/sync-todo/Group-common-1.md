# Sync todo — `common` (group 1 of 1)

**7 classes** · ✅ 2 archived · ⬜ 5 open

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
| 2 | `irp_classifier_role_api_report` | IRPClassifierRole | `rhapsody_cli/models/elements/common/model_other_model.py` | 1 | 8 | 1/8 (②) | ⬜ open |
| 3 | `irp_enumeration_literal_api_report` | IRPEnumerationLiteral | `rhapsody_cli/models/elements/common/model_misc.py` | 1 | 2 | 1/8 (②) | ⬜ open |
| 4 | `irp_constraint_api_report` | IRPConstraint | `rhapsody_cli/models/elements/common/model_misc.py` | 1 | 1 | 1/8 (②) | ⬜ open |
| 5 | `irp_comment_api_report` | IRPComment | `rhapsody_cli/models/elements/common/model_misc.py` | 0 | 0 | 1/8 (②) | ⬜ open |
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
<summary><code>irp_classifier_role_api_report</code> · IRPClassifierRole · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 34 src / 13 test refs, 8 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_enumeration_literal_api_report</code> · IRPEnumerationLiteral · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 21 src / 11 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_constraint_api_report</code> · IRPConstraint · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 9 src / 8 test refs, 1 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_comment_api_report</code> · IRPComment · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 8 src / 7 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
