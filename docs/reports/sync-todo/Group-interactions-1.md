# Sync todo — `interactions` (group 1 of 2)

**10 classes** · ✅ 0 archived · ⬜ 10 open

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
| 1 | `irp_message_api_report` | IRPMessage | `elements/interactions/model_interactions.py` | 32 | 36 | 1/8 (②) | ⬜ open |
| 2 | `irp_event_api_report` | IRPEvent | `rhapsody_cli/models/elements/interactions/model_interactions.py` | 4 | 4 | 1/8 (②) | ⬜ open |
| 3 | `irp_transition_api_report` | IRPTransition | `rhapsody_cli/models/elements/interactions/model_interactions.py` | 13 | 23 | 1/8 (②) | ⬜ open |
| 4 | `irp_event_reception_api_report` | IRPEventReception | `rhapsody_cli/models/elements/interactions/model_interactions.py` | 2 | 2 | 1/8 (②) | ⬜ open |
| 5 | `irp_interaction_operator_api_report` | IRPInteractionOperator | `rhapsody_cli/models/elements/interactions/model_interactions.py` | 3 | 3 | 1/8 (②) | ⬜ open |
| 6 | `irp_interaction_occurrence_api_report` | IRPInteractionOccurrence | `rhapsody_cli/models/elements/interactions/model_interactions.py` | 3 | 3 | 1/8 (②) | ⬜ open |
| 7 | `irp_trigger_api_report` | IRPTrigger | `rhapsody_cli/models/elements/interactions/model_interactions.py` | 3 | 5 | 1/8 (②) | ⬜ open |
| 8 | `irp_execution_occurrence_api_report` | IRPExecutionOccurrence | `rhapsody_cli/models/elements/interactions/model_interactions.py` | 1 | 1 | 1/8 (②) | ⬜ open |
| 9 | `irp_guard_api_report` | IRPGuard | `rhapsody_cli/models/elements/interactions/model_interactions.py` | 2 | 2 | 1/8 (②) | ⬜ open |
| 10 | `irp_interaction_operand_api_report` | IRPInteractionOperand | `rhapsody_cli/models/elements/interactions/model_interactions.py` | 3 | 3 | 1/8 (②) | ⬜ open |

## Row details

<details>
<summary><code>irp_message_api_report</code> · IRPMessage · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** interaction core (44 src / 48 test, 36 owned methods) with the largest legacy-site count here. Module also holds `RPEvent`/`RPTransition` etc. — only this class migrates in this row.
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
<summary><code>irp_event_api_report</code> · IRPEvent · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 70 src / 32 test refs, 4 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_transition_api_report</code> · IRPTransition · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 41 src / 31 test refs, 23 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_event_reception_api_report</code> · IRPEventReception · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 32 src / 12 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_interaction_operator_api_report</code> · IRPInteractionOperator · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 15 src / 7 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_interaction_occurrence_api_report</code> · IRPInteractionOccurrence · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 15 src / 7 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_trigger_api_report</code> · IRPTrigger · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 11 src / 9 test refs, 5 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_execution_occurrence_api_report</code> · IRPExecutionOccurrence · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 16 src / 5 test refs, 1 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_guard_api_report</code> · IRPGuard · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 11 src / 6 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_interaction_operand_api_report</code> · IRPInteractionOperand · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 7 src / 7 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7
- [ ] ⑧ §8

</details>
