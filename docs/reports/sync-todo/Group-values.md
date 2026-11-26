# Sync todo — `values`

**5 classes** · ✅ 0 archived · ⬜ 5 open

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
| 1 | `irp_literal_specification_api_report` | IRPLiteralSpecification | `rhapsody_cli/models/elements/values/model_values.py` | 2 | 2 | 1/8 (②) | ⬜ open |
| 2 | `irp_instance_specification_api_report` | IRPInstanceSpecification | `rhapsody_cli/models/elements/values/model_values.py` | 0 | 6 | 1/8 (②) | ⬜ open |
| 3 | `irp_instance_slot_api_report` | IRPInstanceSlot | `rhapsody_cli/models/elements/values/model_values.py` | 0 | 5 | 1/8 (②) | ⬜ open |
| 4 | `irp_instance_value_api_report` | IRPInstanceValue | `rhapsody_cli/models/elements/values/model_values.py` | 0 | 2 | 1/8 (②) | ⬜ open |
| 5 | `irp_value_specification_api_report` | IRPValueSpecification | `rhapsody_cli/models/elements/values/model_values.py` | 0 | 0 | 1/8 (②) | ⬜ open |

## Row details

<details>
<summary><code>irp_literal_specification_api_report</code> · IRPLiteralSpecification · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 17 src / 5 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_instance_specification_api_report</code> · IRPInstanceSpecification · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 13 src / 10 test refs, 6 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_instance_slot_api_report</code> · IRPInstanceSlot · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 14 src / 9 test refs, 5 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_instance_value_api_report</code> · IRPInstanceValue · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 17 src / 5 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_value_specification_api_report</code> · IRPValueSpecification · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 12 src / 4 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7
- [ ] ⑧ §8

</details>
