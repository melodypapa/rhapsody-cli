# Sync todo — `support`

**27 classes** · ✅ 0 archived · ⬜ 27 open

One row per sync run. A step is ticked only when its evidence lands; a row is archived only after all eight steps pass. Binding rule: one pywin32-exposed COM member per call — `call_com(lambda: self._com.Name(...))` for methods, `get_com_property` / `set_com_property` for properties; catalog-absent sites are blockers, never blind migrations. Canonical package: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/`, mirrored tests under `tests/{unit,integration}/models/com/telelogic/rhapsody/core/`.

Merged from `Group-support-1.md`, `Group-support-2.md`, `Group-support-3.md`; the per-row content is unchanged.

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
| 11 | `irp_external_check_registry_api_report` | IRPExternalCheckRegistry | `rhapsody_cli/models/support/model_codegen.py` | 0 | 2 | 1/8 (②) | ⬜ open |
| 12 | `irp_code_gen_simplifiers_registry_api_report` | IRPCodeGenSimplifiersRegistry | `rhapsody_cli/models/support/model_codegen.py` | 0 | 1 | 1/8 (②) | ⬜ open |
| 13 | `irp_search_result_api_report` | IRPSearchResult | `rhapsody_cli/models/support/model_codegen.py` | 3 | 4 | 1/8 (②) | ⬜ open |
| 14 | `irp_progress_bar_api_report` | IRPProgressBar | `rhapsody_cli/models/support/model_ide.py` | 0 | 2 | 1/8 (②) | ⬜ open |
| 15 | `ir_pow_text_listener_api_report` | IRPowTextListener | `rhapsody_cli/models/support/model_ide.py` | 1 | 2 | 1/8 (②) | ⬜ open |
| 16 | `ir_pow_list_listener_api_report` | IRPowListListener | `rhapsody_cli/models/support/model_ide.py` | 1 | 2 | 1/8 (②) | ⬜ open |
| 17 | `irp_rhapsody_server_api_report` | IRPRhapsodyServer | `rhapsody_cli/models/support/model_codegen.py` | 0 | 4 | 1/8 (②) | ⬜ open |
| 18 | `irp_base_external_code_generator_tool_api_report` | IRPBaseExternalCodeGeneratorTool | `rhapsody_cli/models/support/model_codegen.py` | 0 | 3 | 1/8 (②) | ⬜ open |
| 19 | `irp_controlled_file_api_report` | IRPControlledFile | `rhapsody_cli/models/support/model_files.py` | 2 | 3 | 1/8 (②) | ⬜ open |
| 20 | `irp_external_roundtrip_invoker_api_report` | IRPExternalRoundtripInvoker | `rhapsody_cli/models/support/model_codegen.py` | 0 | 0 | 1/8 (②) | ⬜ open |
| 21 | `irpascii_file_api_report` | IRPASCIIFile | `rhapsody_cli/models/support/model_files.py` | 0 | 3 | 1/8 (②) | ⬜ open |
| 22 | `irp_code_generator_api_report` | IRPCodeGenerator | `rhapsody_cli/models/support/model_codegen.py` | 0 | 2 | 1/8 (②) | ⬜ open |
| 23 | `irpax_view_ctrl_api_report` | IRPAXViewCtrl | `rhapsody_cli/models/support/model_ide.py` | 0 | 2 | 1/8 (②) | ⬜ open |
| 24 | `irp_round_trip_api_report` | IRPRoundTrip | `rhapsody_cli/models/support/model_codegen.py` | 0 | 1 | 1/8 (②) | ⬜ open |
| 25 | `irp_external_code_generator_invoker_api_report` | IRPExternalCodeGeneratorInvoker | `rhapsody_cli/models/support/model_codegen.py` | 0 | 1 | 1/8 (②) | ⬜ open |
| 26 | `irp_java_plugins_api_report` | IRPJavaPlugins | `rhapsody_cli/models/support/model_ide.py` | 0 | 0 | 1/8 (②) | ⬜ open |
| 27 | `irp_integrator_api_report` | IRPIntegrator | `rhapsody_cli/models/support/model_codegen.py` | 0 | 0 | 1/8 (②) | ⬜ open |

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

<details>
<summary><code>irp_external_check_registry_api_report</code> · IRPExternalCheckRegistry · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 13 src / 6 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_code_gen_simplifiers_registry_api_report</code> · IRPCodeGenSimplifiersRegistry · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 12 src / 5 test refs, 1 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_search_result_api_report</code> · IRPSearchResult · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 8 src / 6 test refs, 4 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_progress_bar_api_report</code> · IRPProgressBar · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 11 src / 4 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>ir_pow_text_listener_api_report</code> · IRPowTextListener · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 9 src / 5 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7 — `ir_pow_text_listener.rst` (anchor + deviation list-table) and toctree entry
- [ ] ⑧ §8

</details>

<details>
<summary><code>ir_pow_list_listener_api_report</code> · IRPowListListener · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 9 src / 5 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7 — `ir_pow_list_listener.rst` (anchor + deviation list-table) and toctree entry
- [ ] ⑧ §8

</details>

<details>
<summary><code>irp_rhapsody_server_api_report</code> · IRPRhapsodyServer · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 8 src / 6 test refs, 4 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_base_external_code_generator_tool_api_report</code> · IRPBaseExternalCodeGeneratorTool · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 9 src / 5 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_controlled_file_api_report</code> · IRPControlledFile · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 7 src / 5 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_external_roundtrip_invoker_api_report</code> · IRPExternalRoundtripInvoker · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 11 src / 2 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irpascii_file_api_report</code> · IRPASCIIFile · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 7 src / 5 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7 — `irpascii_file.rst` (anchor + deviation list-table) and toctree entry
- [ ] ⑧ §8

</details>

<details>
<summary><code>irp_code_generator_api_report</code> · IRPCodeGenerator · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 6 src / 4 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irpax_view_ctrl_api_report</code> · IRPAXViewCtrl · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 6 src / 4 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7 — `irpax_view_ctrl.rst` (anchor + deviation list-table) and toctree entry
- [ ] ⑧ §8

</details>

<details>
<summary><code>irp_round_trip_api_report</code> · IRPRoundTrip · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 5 src / 3 test refs, 1 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_external_code_generator_invoker_api_report</code> · IRPExternalCodeGeneratorInvoker · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 5 src / 3 test refs, 1 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_java_plugins_api_report</code> · IRPJavaPlugins · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 4 src / 0 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_integrator_api_report</code> · IRPIntegrator · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 4 src / 0 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7
- [ ] ⑧ §8

</details>
