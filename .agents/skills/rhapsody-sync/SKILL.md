---
name: rhapsody-sync
description: "Sync Rhapsody Python wrappers against JavaDoc. Use for IRP* method parity, pywin32/COM mismatches, Java-derived Python package paths, or RST deviation docs—even when the user says 'bring IRPClass up to date' rather than 'sync'. Do not use for read-only API questions, CLI usage, user-guide edits, or unrelated code. Handle one interface per run and create a class-specific TODO list."
license: MIT
author: rhapsody-cli maintainers
repository: https://github.com/melodypapa/rhapsody-cli
version: 0.1.0
product-version: 0.1.0
spec-version: 1.0.0
keywords: [rhapsody, javadoc, com, api-sync, python]
agents: [pi]
---

# Rhapsody API sync

Sync one requested Java API interface with its Python wrapper in this project. The input is the JavaDoc interface name (such as `IRPClass`), not a hard-coded Python class. Treat `RPClass` as an example pattern, never as the default target.

## 1. Resolve the target and publish its TODOs

If the interface name is missing or ambiguous, ask for it before editing. Find its JavaDoc in `docs/java_api/`, read the declared package, then resolve the matching wrapper, base class, tests, and current exports. Do not infer the Java package or wrapper mapping from the existing Python folder alone.

Before analysis, create a visible TODO list using an available task-list tool; otherwise show a Markdown checklist in the response and keep it current. Keep the shared steps concise, then add a subtask for every target-owned JavaDoc member so no method is silently skipped:

```markdown
## Sync TODO — IRPClass (`com.telelogic.rhapsody.core`)
- [ ] Resolve JavaDoc package, class description, and member inventory.
- [ ] Locate wrapper, inheritance, exports, tests, and current package path.
- [ ] Compare every owned member across JavaDoc, COM exposure, and Python implementation.
- [ ] Add/update focused tests before implementation or package changes.
- [ ] Mirror the Java package in Python; preserve existing import paths.
- [ ] Update class checklist and JavaDoc-derived class/method descriptions.
- [ ] Update package-organized RST entry and list each verified deviation.
- [ ] Run focused validation and summarize unresolved items.
- [ ] Member: addExample() — [ ] JavaDoc [ ] COM [ ] wrapper [ ] disposition
```

Only mark a task done after checking its evidence. Keep inherited-member notes separate from owned-member tasks.

## 2. Compare evidence efficiently, without skipping coverage

Run the skill-local wrapper once for a baseline and use its report as the member-by-member index:

```bash
python .agents/skills/rhapsody-sync/scripts/validate_interface.py <INTERFACE> --source authority
```

The helper locates the project root and delegates to the canonical `scripts/validate_model_api.py`; it does not duplicate that logic. A nonzero exit of `1` means actionable deviations were found, not that validation crashed. On Windows with Rhapsody available, use `--source typelib` to inspect the registered binding; otherwise use the committed `docs/reports/pywin32_authority.json` snapshot. The current repository validator is hard-coded to Java package `com.telelogic.rhapsody.core`; if the selected JavaDoc declares another package, the helper stops rather than generating a misleading report.

Use these sources for different questions:

| Source | Trust it for | Do not infer |
| --- | --- | --- |
| JavaDoc HTML | Declared package, Java API, signatures, descriptions | That COM exposes a callable member |
| pywin32 catalog/type library | COM member presence and method/property shape | The complete Java contract or wrapper behavior |
| Python wrapper | Actual facade, COM calls, conversions, and return wrapping | That an absent wrapper is intentionally unsupported |

Reconcile every member declared by the target interface against the validator inventory. To save time, inspect implementation bodies and secondary references deeply for deviations, missing coverage, unsupported members, and code you will change; do not reread unrelated wrappers or inherited implementations. Check JavaDoc descriptions for the class and each method being added or changed. If evidence conflicts, record the sources and ask rather than guessing.

For each target-owned JavaDoc member, track: Java name/signature and description; inherited vs owned; COM method/property/alias/unavailable status; Python method and actual COM call; result type/wrapping; and a disposition. Use concise dispositions such as matched, inherited, intentional facade helper, binding mismatch, JavaDoc-only, COM-only, missing wrapper, intentionally unsupported, or unresolved.

Never add a direct COM call for a member absent from the binding. Keep exact camelCase COM identifiers and snake_case Python names. Follow `AGENTS.md` for `call_com`, method/property helpers, argument unwrapping, result wrapping, collection handling, annotations, and exception handling. In particular, do not add `Any` or `from __future__ import annotations`.

## 3. Apply the smallest safe class change

Follow TDD: write or update a focused fake-COM unit test before changing behavior or import wiring. Unit tests must not use real COM. For each wrapper method added or changed, use JavaDoc for its description, arguments, and return contract while retaining project-specific usage notes and known runtime limitations. Add integration coverage only for supported behavior owned by this wrapper; inherited methods may set up fixtures but are not child assertions. Respect the integration-test ownership rules in `AGENTS.md`, including child overrides with different return contracts.

The canonical Python package mirrors every Java package segment beneath `rhapsody_cli.models.elements`. For example:

- Java: `com.telelogic.rhapsody.core`
- Python import: `rhapsody_cli.models.elements.com.telelogic.rhapsody.core`
- Directory: `src/rhapsody_cli/models/elements/com/telelogic/rhapsody/core/`

Move the wrapper only if it is not already in the canonical package. Add package `__init__.py` exports, preserve registration/import side effects, and update relevant internal references. Keep the existing module naming convention where practical. Preserve established domain imports through thin re-exports, and verify old and canonical imports resolve to the same class. Migrate only the requested interface; avoid unrelated package moves and refactors. If moving it safely requires broad changes or would break public imports, stop and ask before expanding scope.

## 4. Update the two class documents

### Requirement entry

Update the selected class in `docs/requirements/swr_elem_requirements.md`. Use the JavaDoc class description for the summary, but retain project-specific requirements and implementation facts that JavaDoc cannot express. Add an entry in the existing format if one is missing.

### Package-organized RST

Update `docs/api/elements.rst` under the Java package heading, not the current Python domain grouping. Start the class entry with the verifier-recognized anchor `.. _rhapsody-java-interface-<INTERFACE>:`. Include the Java interface, Java package, JavaDoc-derived description, Python wrapper, canonical import path, and maintained legacy import path.

List each verified deviation between JavaDoc, COM/pywin32, and Python implementation in a valid reStructuredText `list-table` with headers `JavaDoc member/signature`, `COM/pywin32 exposure`, `Python implementation`, and `Deviation and treatment`. Include method-vs-property shape and evidence-backed resolution; if there are no deviations, say so explicitly. The verifier checks that the section contains every member reported by the API validator. If the class is already listed under a legacy domain heading, move its entry to the Java-package section instead of duplicating it; leave unrelated and not-yet-migrated classes unchanged. Keep RST navigation valid.

## 5. Verify and report

After edits, run final validation and artifact checks:

```bash
python .agents/skills/rhapsody-sync/scripts/validate_interface.py <INTERFACE> --source authority
python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE>
python -m pytest -o addopts= .agents/skills/rhapsody-sync/tests -q
```

`verify_sync.py` checks Java-package-derived wrapper placement, the class requirement entry, and the RST anchor/table coverage against the generated report. An exit code of `1` lists incomplete or mismatched artifacts. Also run focused project unit tests, import/registration checks, relevant lint/type checks, and RST/Sphinx validation when available. If live Rhapsody integration tests cannot run, say so explicitly; collection-only is not a live test. Leave TODO items open when blocked, with the reason.

Finish with a compact report: Java interface/package, old and canonical Python paths, compatibility imports, files changed, checks run, and remaining deviations. Sync one interface per run; complete and review it before starting another.
