# Sync todo — `diagrams` (group 1 of 2)

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
| 1 | `irp_diagram_api_report` | IRPDiagram | `elements/diagrams/model_diagrams.py` | 2 | 33 | 1/8 (②) | ⬜ open |
| 2 | `irp_sequence_diagram_api_report` | IRPSequenceDiagram | `rhapsody_cli/models/elements/diagrams/model_diagram_types.py` | 0 | 2 | 1/8 (②) | ⬜ open |
| 3 | `irp_activity_diagram_api_report` | IRPActivityDiagram | `rhapsody_cli/models/elements/diagrams/model_diagram_types.py` | 0 | 2 | 1/8 (②) | ⬜ open |
| 4 | `irp_statechart_diagram_api_report` | IRPStatechartDiagram | `rhapsody_cli/models/elements/diagrams/model_diagram_types.py` | 0 | 3 | 1/8 (②) | ⬜ open |
| 5 | `irp_timing_diagram_api_report` | IRPTimingDiagram | `rhapsody_cli/models/elements/diagrams/model_diagram_types.py` | 0 | 2 | 1/8 (②) | ⬜ open |
| 6 | `irp_collaboration_diagram_api_report` | IRPCollaborationDiagram | `rhapsody_cli/models/elements/diagrams/model_diagram_types.py` | 0 | 1 | 1/8 (②) | ⬜ open |
| 7 | `irp_use_case_diagram_api_report` | IRPUseCaseDiagram | `rhapsody_cli/models/elements/diagrams/model_diagram_types.py` | 0 | 0 | 1/8 (②) | ⬜ open |
| 8 | `irp_object_model_diagram_api_report` | IRPObjectModelDiagram | `rhapsody_cli/models/elements/diagrams/model_diagram_types.py` | 0 | 0 | 1/8 (②) | ⬜ open |
| 9 | `irp_deployment_diagram_api_report` | IRPDeploymentDiagram | `rhapsody_cli/models/elements/diagrams/model_diagram_types.py` | 0 | 0 | 1/8 (②) | ⬜ open |
| 10 | `irp_component_diagram_api_report` | IRPComponentDiagram | `rhapsody_cli/models/elements/diagrams/model_diagram_types.py` | 0 | 0 | 1/8 (②) | ⬜ open |

## Row details

<details>
<summary><code>irp_diagram_api_report</code> · IRPDiagram · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** base diagram type (84 src / 14 test, 33 owned methods). Module defines many diagram leaves with zero owned methods — migrate only `RPDiagram` and leave the leaves for a later group.
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
<summary><code>irp_sequence_diagram_api_report</code> · IRPSequenceDiagram · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 33 src / 9 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_activity_diagram_api_report</code> · IRPActivityDiagram · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 20 src / 0 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_statechart_diagram_api_report</code> · IRPStatechartDiagram · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 19 src / 0 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_timing_diagram_api_report</code> · IRPTimingDiagram · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 16 src / 0 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_collaboration_diagram_api_report</code> · IRPCollaborationDiagram · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 15 src / 0 test refs, 1 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_use_case_diagram_api_report</code> · IRPUseCaseDiagram · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 14 src / 0 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_object_model_diagram_api_report</code> · IRPObjectModelDiagram · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 14 src / 0 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_deployment_diagram_api_report</code> · IRPDeploymentDiagram · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 14 src / 0 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_component_diagram_api_report</code> · IRPComponentDiagram · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 14 src / 0 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7
- [ ] ⑧ §8

</details>
