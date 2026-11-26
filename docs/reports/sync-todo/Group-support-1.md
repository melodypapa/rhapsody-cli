# Sync todo — `support` (group 1 of 3)

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
| 1 | `irp_search_query_api_report` | IRPSearchQuery | `rhapsody_cli/models/support/model_codegen.py` | 31 | 68 | 1/8 (②) | ⬜ open |
| 2 | `irp_file_api_report` | IRPFile | `rhapsody_cli/models/support/model_files.py` | 6 | 15 | 1/8 (②) | ⬜ open |
| 3 | `irp_internal_oem_plugin_api_report` | IRPInternalOEMPlugin | `rhapsody_cli/models/support/model_ide.py` | 0 | 14 | 1/8 (②) | ⬜ open |
| 4 | `irp_selection_api_report` | IRPSelection | `rhapsody_cli/models/support/model_ide.py` | 0 | 8 | 1/8 (②) | ⬜ open |
| 5 | `irp_diag_synth_api_api_report` | IRPDiagSynthAPI | `rhapsody_cli/models/support/model_codegen.py` | 0 | 7 | 1/8 (②) | ⬜ open |
| 6 | `irp_plug_in_window_api_report` | IRPPlugInWindow | `rhapsody_cli/models/support/model_ide.py` | 6 | 8 | 1/8 (②) | ⬜ open |
| 7 | `irp_search_manager_api_report` | IRPSearchManager | `rhapsody_cli/models/support/model_codegen.py` | 0 | 4 | 1/8 (②) | ⬜ open |
| 8 | `ir_pow_pane_mgr_api_report` | IRPowPaneMgr | `rhapsody_cli/models/support/model_ide.py` | 0 | 4 | 1/8 (②) | ⬜ open |
| 9 | `irp_external_ide_registry_api_report` | IRPExternalIDERegistry | `rhapsody_cli/models/support/model_ide.py` | 0 | 3 | 1/8 (②) | ⬜ open |
| 10 | `irp_file_fragment_api_report` | IRPFileFragment | `rhapsody_cli/models/support/model_files.py` | 4 | 5 | 1/8 (②) | ⬜ open |

## Row details

<details>
<summary><code>irp_search_query_api_report</code> · IRPSearchQuery · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 87 src / 73 test refs, 68 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_file_api_report</code> · IRPFile · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 29 src / 24 test refs, 15 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_internal_oem_plugin_api_report</code> · IRPInternalOEMPlugin · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 18 src / 16 test refs, 14 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_selection_api_report</code> · IRPSelection · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 19 src / 12 test refs, 8 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_diag_synth_api_api_report</code> · IRPDiagSynthAPI · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 18 src / 11 test refs, 7 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_plug_in_window_api_report</code> · IRPPlugInWindow · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 12 src / 10 test refs, 8 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_search_manager_api_report</code> · IRPSearchManager · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 16 src / 8 test refs, 4 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>ir_pow_pane_mgr_api_report</code> · IRPowPaneMgr · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 15 src / 8 test refs, 4 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7 — `ir_pow_pane_mgr.rst` (anchor + deviation list-table) and toctree entry
- [ ] ⑧ §8

</details>

<details>
<summary><code>irp_external_ide_registry_api_report</code> · IRPExternalIDERegistry · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 14 src / 7 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_file_fragment_api_report</code> · IRPFileFragment · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 9 src / 7 test refs, 5 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7
- [ ] ⑧ §8

</details>
