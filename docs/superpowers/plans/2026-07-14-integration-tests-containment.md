# Containment Subpackage Integration Tests Completion Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add integration tests for all remaining untested methods across `RPProject`, `RPPackage` (largest surface — ~82 untested methods), `RPComponent`, `RPComponentInstance`, `RPConfiguration`, `RPCollaboration`, `RPNode`, creating new dedicated test files where none exist. Flip in-source `[ ] integration test` markers to `[x]` as work completes. (`RPModule` and `RPProfile` define no methods of their own — they only inherit from `RPInstance` / `RPPackage` respectively — so they need no test work.)

**Architecture:** Extends `tests/integration/models/elements/containment/test_model_project.py` for `RPProject`/`RPPackage`, adds new test files for the other 5 classes, using shared `rhapsody_app`/`test_project` fixtures.

**Tech Stack:** pytest, pywin32 (win32com), live Rhapsody COM API, `uuid.uuid4().hex[:8]` for unique names.

## Global Constraints

- Windows-only runtime (requires Windows + a running Rhapsody instance)
- All test classes use `@pytest.mark.integration`
- All tests consume the `test_project: RPProject` fixture (session-scoped)
- Use `_unique(prefix)` with `uuid.uuid4().hex[:8]`
- Always `try/finally` cleanup via `element.delete_from_project()` (never `element._com.delete()`)
- Assert both `isinstance()` and read-back values
- Flip `[ ] integration test` to `[x] integration test` per task in the relevant `model_*.py` file
- If a method has no existing checklist row at all (several were added to the source without ever being added to the parity checklist comment block), add the row in the standard format before marking it `[x]`:
  `# [x] method_name  [x] impl  [x] docstring  [x] unit test  [x] integration test`
  (copy the actual `impl`/`docstring`/`unit test` state from what is already true in the file; do not fabricate coverage that doesn't exist)
- Quality gate after each task: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit` (live run: `pytest tests/integration -m integration`, requires attached Rhapsody)
- Import concrete classes via subpackage `__init__.py` re-exports, e.g. `from rhapsody_cli.models.elements.containment import RPComponent, RPProject`

---

## Ground-Truth Scope Notes (read before starting)

- `tests/integration/models/elements/containment/test_model_project.py` already covers, and must **not** be re-tested: `RPProject.add_package`, `RPProject.get_packages` (property-based, no own checklist row), `RPProject.add_component`, `RPPackage.add_nested_package`, `RPPackage.get_nested_packages` (no own checklist row), `RPPackage.add_class`, `RPPackage.get_classes`, `RPPackage.add_module`.
- `tests/integration/models/elements/classifiers/test_model_actor.py` already covers `RPPackage.add_actor` (its checklist row is stale — flip it in Task RPPackage-G).
- `tests/integration/models/elements/classifiers/test_model_usecase.py` already covers `RPPackage.add_use_case` / `get_use_cases` is a separate, still-untested getter (kept in scope).
- `tests/integration/models/elements/classifiers/test_model_signal.py`, `test_model_enumeration.py`, `test_model_interface.py` already cover `RPPackage.add_signal`, `add_enumeration`, `add_interface` as documented `xfail` tests (Rhapsody2.Application.1 does not support these COM calls on a package). These methods have **no checklist row at all** in `model_package.py` — add rows and flip them in Task RPPackage-G; do not write new tests for them.
- `RPProject.save` is inherited from `RPUnit` and out of scope for this plan (tracked under the `common`/core `RPUnit` integration-test plan instead).
- `RPProject.add_class` / `RPProject.add_actor` duplicate `RPPackage.add_class` / `add_actor` behavior (already tested) and are out of scope here.

---

## Tasks

### Task RPPackage-A: RPPackage — Diagram factory/getter/deleter methods (9 diagram types)

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_project.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_package.py` (flip checklist boxes; add rows for `getActivityDiagrams`, `deleteActivityDiagram`, which have none)

**Methods covered:** `add_activity_diagram`, `get_activity_diagrams`, `delete_activity_diagram`, `add_sequence_diagram`, `get_sequence_diagrams`, `delete_sequence_diagram`, `add_use_case_diagram`, `get_use_case_diagrams`, `delete_use_case_diagram`, `add_collaboration_diagram`, `get_collaboration_diagrams`, `delete_collaboration_diagram`, `add_component_diagram`, `get_component_diagrams`, `delete_component_diagram`, `add_deployment_diagram`, `get_deployment_diagrams`, `delete_deployment_diagram`, `add_object_model_diagram`, `get_object_model_diagrams`, `delete_object_model_diagram`, `add_statechart_diagram`, `add_timing_diagram`, `get_timing_diagrams`, `delete_timing_diagram`, `add_panel_diagram`, `get_panel_diagrams`, `delete_panel_diagram`, `get_behavioral_diagrams` (29 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_activity_diagram_lifecycle(self, test_project: RPProject) -> None:
    pkg_name = self._unique("ActDiagPkg")
    diag_name = self._unique("MyActivityDiagram")
    pkg = self._create_package(test_project, pkg_name)
    diagram = pkg.add_activity_diagram(diag_name)
    try:
        assert diagram is not None
        assert diagram.get_name() == diag_name
        diagrams = list(pkg.get_activity_diagrams())
        assert diagram in diagrams
        behavioral = list(pkg.get_behavioral_diagrams())
        assert diagram in behavioral
    finally:
        pkg.delete_activity_diagram(diagram)
        remaining = [d.get_name() for d in pkg.get_activity_diagrams()]
        assert diag_name not in remaining
```

For remaining methods in this task, follow the same established pattern: for each of the other 7 full add/get/delete diagram triples (sequence, use case, collaboration, component, deployment, object model, timing), write one `test_<type>_diagram_lifecycle` following the identical create → assert in getter → delete → assert absent shape. For `add_statechart_diagram` (no matching getter/deleter exist on `RPPackage`) and `add_panel_diagram`/`get_panel_diagrams`/`delete_panel_diagram`, write matching create/getter/delete tests using the same shape (panel diagram triple; statechart create-only test).

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_project.py -m integration -v -k Diagram`
Expected: PASS (or documented xfail)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/containment/model_package.py`, flip the 27 existing rows to `[x] integration test` and add+flip new rows for `getActivityDiagrams` and `deleteActivityDiagram` (both `[x] impl [x] docstring [ ] unit test [x] integration test` — these two have no prior unit test coverage; do not fabricate a `[x]` for unit test).

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_project.py src/rhapsody_cli/models/elements/containment/model_package.py
git commit -m "test: add RPPackage diagram factory/getter/deleter integration tests"
```

---

### Task RPPackage-B: RPPackage — Class/actor/usecase/package CRUD + exception/enumeration

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_project.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_package.py` (flip checklist boxes; add row for `findNestedPackage`)

**Methods covered:** `delete_class`, `delete_actor`, `delete_use_case`, `find_class`, `find_actor`, `find_use_case`, `find_nested_package`, `delete_package`, `add_exception`, `get_enumerations` (10 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_class_find_and_delete(self, test_project: RPProject) -> None:
    pkg_name = self._unique("FindClsPkg")
    class_name = self._unique("FindableClass")
    pkg = self._create_package(test_project, pkg_name)
    new_class = pkg.add_class(class_name)
    found = pkg.find_class(class_name)
    assert found is not None
    assert found.get_name() == class_name
    assert found == new_class
    pkg.delete_class(new_class)
    classes = [c.get_name() for c in pkg.get_classes()]
    assert class_name not in classes
```

For remaining methods in this task, follow the same established pattern: `find_actor`/`delete_actor` and `find_use_case`/`delete_use_case` mirror the class test shape exactly (create via `add_actor`/`add_use_case`, find by name, delete, assert absence from `get_actors`/`get_use_cases`). `find_nested_package`/`delete_package` follow the same shape using `add_nested_package`. `add_exception` should be tested as a plain create + `isinstance`/`get_name` check with `delete_from_project()` cleanup (no documented Rhapsody limitation exists for this one, unlike `add_signal`/`add_enumeration`/`add_interface`). `get_enumerations` should be tested as a read-only getter returning an (empty or non-empty) `RPCollection` without attempting to populate it (since `add_enumeration` is `xfail` elsewhere).

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_project.py -m integration -v -k "Class or Actor or UseCase or Package or Exception or Enumeration"`
Expected: PASS (or documented xfail if `add_exception` turns out to hit the same COM limitation as its siblings — in that case mark it `xfail` following the existing pattern in `tests/integration/models/elements/classifiers/test_model_signal.py`)

- [ ] **Step 3: Flip checklist boxes**

In `model_package.py`, flip `deleteClass`, `deleteActor`, `deleteUseCase`, `findClass`, `findActor`, `findUseCase`, `deletePackage` to `[x] integration test`; add and flip a new row for `findNestedPackage`; add rows for `add_exception`/`addException` and `get_enumerations`/`getEnumerations` if missing (copy actual unit-test state).

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_project.py src/rhapsody_cli/models/elements/containment/model_package.py
git commit -m "test: add RPPackage class/actor/usecase/package CRUD integration tests"
```

---

### Task RPPackage-C: RPPackage — Association & event management

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_project.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_package.py` (flip checklist boxes; add rows for `addAssociation`, `getAssociations`, `deleteAssociation`)

**Methods covered:** `add_association`, `get_associations`, `delete_association`, `add_event`, `get_events`, `find_event`, `delete_event` (7 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_association_lifecycle(self, test_project: RPProject) -> None:
    pkg_name = self._unique("AssocPkg")
    assoc_name = self._unique("MyAssociation")
    pkg = self._create_package(test_project, pkg_name)
    assoc = pkg.add_association(assoc_name)
    try:
        assert assoc is not None
        assert assoc.get_name() == assoc_name
        assocs = list(pkg.get_associations())
        assert assoc in assocs
    finally:
        pkg.delete_association(assoc)
        remaining = [a.get_name() for a in pkg.get_associations()]
        assert assoc_name not in remaining
```

For remaining methods in this task, follow the same established pattern: `add_event`/`get_events`/`find_event`/`delete_event` follow the identical create → assert in getter → find by name → delete → assert absent shape used above for associations.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_project.py -m integration -v -k "Association or Event"`
Expected: PASS

- [ ] **Step 3: Flip checklist boxes**

Add rows for `addAssociation`/`getAssociations`/`deleteAssociation` (no existing rows) and flip them plus `addEvent`, `getEvents`, `findEvent`, `deleteEvent` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_project.py src/rhapsody_cli/models/elements/containment/model_package.py
git commit -m "test: add RPPackage association and event management integration tests"
```

---

### Task RPPackage-D: RPPackage — Global function/variable/object management

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_project.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_package.py` (flip checklist boxes)

**Methods covered:** `add_global_function`, `find_global_function`, `get_global_functions`, `delete_global_function`, `add_global_object`, `get_global_objects`, `find_global_object`, `delete_global_object`, `add_global_variable`, `get_global_variables`, `find_global_variable`, `delete_global_variable` (12 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_global_function_lifecycle(self, test_project: RPProject) -> None:
    pkg_name = self._unique("GlobFuncPkg")
    func_name = self._unique("myGlobalFunction")
    pkg = self._create_package(test_project, pkg_name)
    func = pkg.add_global_function(func_name)
    try:
        assert func is not None
        assert func.get_name() == func_name
        funcs = list(pkg.get_global_functions())
        assert func in funcs
        found = pkg.find_global_function(func_name)
        assert found == func
    finally:
        pkg.delete_global_function(func)
        remaining = [f.get_name() for f in pkg.get_global_functions()]
        assert func_name not in remaining
```

For remaining methods in this task, follow the same established pattern: `add_global_object`/`get_global_objects`/`find_global_object`/`delete_global_object` and `add_global_variable`/`get_global_variables`/`find_global_variable`/`delete_global_variable` mirror the global function test shape exactly.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_project.py -m integration -v -k "Global"`
Expected: PASS

- [ ] **Step 3: Flip checklist boxes**

Flip `add_global_function`, `findGlobalFunction`, `getGlobalFunctions`, `deleteGlobalFunction`, `addGlobalObject`, `getGlobalObjects`, `findGlobalObject`, `deleteGlobalObject`, `addGlobalVariable`, `getGlobalVariables`, `findGlobalVariable`, `deleteGlobalVariable` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_project.py src/rhapsody_cli/models/elements/containment/model_package.py
git commit -m "test: add RPPackage global function/variable/object integration tests"
```

---

### Task RPPackage-E: RPPackage — Node/type/module management

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_project.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_package.py` (flip checklist boxes)

**Methods covered:** `add_node`, `get_nodes`, `find_node`, `delete_node`, `add_type`, `get_types`, `find_type`, `delete_type`, `get_modules` (9 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_node_lifecycle_in_package(self, test_project: RPProject) -> None:
    pkg_name = self._unique("NodePkg")
    node_name = self._unique("MyNode")
    pkg = self._create_package(test_project, pkg_name)
    node = pkg.add_node(node_name)
    try:
        assert node is not None
        assert node.get_name() == node_name
        nodes = list(pkg.get_nodes())
        assert node in nodes
        found = pkg.find_node(node_name)
        assert found == node
    finally:
        pkg.delete_node(node)
        remaining = [n.get_name() for n in pkg.get_nodes()]
        assert node_name not in remaining
```

For remaining methods in this task, follow the same established pattern: `add_type`/`get_types`/`find_type`/`delete_type` mirror the node test shape exactly. `get_modules` should be tested as a read-only getter test: create a module via the already-tested `add_module`, then assert it appears in `pkg.get_modules()`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_project.py -m integration -v -k "Node or Type or Module"`
Expected: PASS

- [ ] **Step 3: Flip checklist boxes**

Flip `addNode`, `getNodes`, `findNode`, `deleteNode`, `addType`, `getTypes`, `findType`, `deleteType`, `getModules` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_project.py src/rhapsody_cli/models/elements/containment/model_package.py
git commit -m "test: add RPPackage node/type/module management integration tests"
```

---

### Task RPPackage-F: RPPackage — Instance specification, links, nested classifiers/components, find operations

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_project.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_package.py` (flip checklist boxes)

**Methods covered:** `add_instance_specification`, `get_instance_specifications`, `add_link`, `get_links`, `get_nested_classifiers`, `get_nested_components`, `find_all_by_name`, `get_source_artifacts`, `find_usage` (9 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_instance_specification_lifecycle(self, test_project: RPProject) -> None:
    pkg_name = self._unique("InstSpecPkg")
    inst_name = self._unique("MyInstanceSpec")
    pkg = self._create_package(test_project, pkg_name)
    inst_spec = pkg.add_instance_specification(inst_name)
    try:
        assert inst_spec is not None
        assert inst_spec.get_name() == inst_name
        specs = list(pkg.get_instance_specifications())
        assert inst_spec in specs
    finally:
        inst_spec.delete_from_project()
        remaining = [s.get_name() for s in pkg.get_instance_specifications()]
        assert inst_name not in remaining
```

For remaining methods in this task, follow the same established pattern: `add_link`/`get_links` mirror the instance specification test shape (link creation between two instance specs may be required depending on the live COM signature; if `add_link(name)` alone is not sufficient, create two instance specifications first and pass them, adjusting the test accordingly). `get_nested_classifiers` and `get_nested_components` are read-only getters — test them by creating a `RPClass`/`RPComponent` respectively as before and asserting collection membership. `find_all_by_name` should create a uniquely-named class and assert it is returned in the `RPCollection`. `get_source_artifacts` is a simple read-only getter test asserting it returns an `RPCollection` without error. `find_usage` should create a class used as another class's type/superclass (or simplest available usage relationship) and assert the collection returned by `find_usage(element)` is non-empty and contains the using element.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_project.py -m integration -v -k "InstanceSpec or Link or Nested or FindAll or SourceArtifact or Usage"`
Expected: PASS (or documented xfail if `add_link`/`find_usage` require preconditions this repo's Rhapsody build doesn't support)

- [ ] **Step 3: Flip checklist boxes**

Flip `addInstanceSpecification`, `getInstanceSpecifications`, `addLink`, `getLinks`, `getNestedClassifiers`, `getNestedComponents`, `findAllByName`, `getSourceArtifacts`, `findUsage` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_project.py src/rhapsody_cli/models/elements/containment/model_package.py
git commit -m "test: add RPPackage instance specification/link/find integration tests"
```

---

### Task RPPackage-G: RPPackage — Reconcile stale checklist rows (no new tests)

**Files:**
- Modify: `src/rhapsody_cli/models/elements/containment/model_package.py` (checklist only; no test code changes)

**Methods covered:** `add_class`, `add_actor`, `add_signal`, `add_enumeration`, `add_interface`, `get_nested_packages` (6 methods — all already have integration test coverage in other files; this task only fixes stale/missing checklist bookkeeping)

**Rationale:** `add_class` and `add_actor` have stale `[ ] integration test` rows despite being covered by `test_model_project.py::test_add_class_to_package` and `test_model_actor.py::test_create_actor_in_package` respectively. `add_signal`, `add_enumeration`, `add_interface` have **no checklist row at all** despite having `xfail`-documented integration tests in `tests/integration/models/elements/classifiers/`. `get_nested_packages` similarly has no row despite being tested in `test_model_project.py::test_create_nested_packages`.

- [ ] **Step 1: Update checklist in `model_package.py`**

Flip `add_actor` and `add_class` rows to `[x] integration test`. Add new rows (in alphabetical position matching existing convention) for `addSignal`/`add_signal`, `addEnumeration`/`add_enumeration`, `addInterface`/`add_interface`, `getNestedPackages`/`get_nested_packages`, each with accurate `impl`/`docstring`/`unit test` state copied from the actual code (all four are `[x] impl [x] docstring`; check `tests/unit/models/elements/containment/test_model_package.py` for the actual unit-test state of each before marking) and `[x] integration test`.

- [ ] **Step 2: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 3: Commit**

```bash
git add src/rhapsody_cli/models/elements/containment/model_package.py
git commit -m "docs: reconcile stale RPPackage integration-test checklist rows"
```

---

### Task RPProject-A: RPProject — Component/node/configuration management

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_project.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_project.py` (flip checklist boxes; add rows for `addNode`, `getNodes`, `findNode`, `deleteNode`, `addConfiguration`, `getConfigurations`, `findConfiguration`, `deleteConfiguration`)

**Methods covered:** `add_profile`, `delete_component`, `find_component`, `get_components`, `get_active_component`, `set_active_component`, `get_active_configuration`, `set_active_configuration`, `add_node`, `get_nodes`, `find_node`, `delete_node`, `add_configuration`, `get_configurations`, `find_configuration`, `delete_configuration` (16 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_node_lifecycle_in_project(self, test_project: RPProject) -> None:
    node_name = self._unique("MyProjectNode")
    node = test_project.add_node(node_name)
    try:
        assert node is not None
        assert node.get_name() == node_name
        nodes = list(test_project.get_nodes())
        assert node in nodes
        found = test_project.find_node(node_name)
        assert found == node
    finally:
        test_project.delete_node(node)
        remaining = [n.get_name() for n in test_project.get_nodes()]
        assert node_name not in remaining
```

For remaining methods in this task, follow the same established pattern: `add_configuration`/`get_configurations`/`find_configuration`/`delete_configuration` mirror the node test shape exactly at project scope. `delete_component`/`find_component`/`get_components` follow the same shape using the already-tested `add_component`. `get_active_component`/`set_active_component` and `get_active_configuration`/`set_active_configuration` should be tested as round-trips: create a component/configuration, `set_active_*`, then assert `get_active_*` returns the same element. `add_profile` should be tested as a simple create + `get_name()` check with cleanup via `delete_from_project()`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_project.py -m integration -v -k "Node or Configuration or Component or Profile"`
Expected: PASS

- [ ] **Step 3: Flip checklist boxes**

In `model_project.py`, flip `addProfile`, `deleteComponent`, `find_component`, `get_components`, `getActiveComponent`, `setActiveComponent`, `getActiveConfiguration`, `setActiveConfiguration` to `[x] integration test`. Add new rows and flip for `addNode`, `getNodes`, `findNode`, `deleteNode`, `addConfiguration`, `getConfigurations`, `findConfiguration`, `deleteConfiguration` (none of these have existing rows — verify actual unit-test state from `tests/unit/models/elements/containment/test_model_project.py` before marking `[x] unit test`).

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_project.py src/rhapsody_cli/models/elements/containment/model_project.py
git commit -m "test: add RPProject component/node/configuration management integration tests"
```

---

### Task RPProject-B: RPProject — Collaboration & profile management

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_project.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_project.py` (flip checklist boxes; add rows for `addCollaboration`, `getCollaborations`, `findCollaboration`, `deleteCollaboration`)

**Methods covered:** `add_collaboration`, `get_collaborations`, `find_collaboration`, `delete_collaboration`, `get_new_collaboration`, `get_profiles`, `get_all_stereotypes` (7 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_collaboration_lifecycle(self, test_project: RPProject) -> None:
    collab_name = self._unique("MyCollaboration")
    collab = test_project.add_collaboration(collab_name)
    try:
        assert collab is not None
        assert collab.get_name() == collab_name
        collabs = list(test_project.get_collaborations())
        assert collab in collabs
        found = test_project.find_collaboration(collab_name)
        assert found == collab
    finally:
        test_project.delete_collaboration(collab)
        remaining = [c.get_name() for c in test_project.get_collaborations()]
        assert collab_name not in remaining
```

For remaining methods in this task, follow the same established pattern: `get_new_collaboration` should be tested as a simple call that returns a non-`None` `RPCollaboration`-typed object. `get_profiles` should be tested by creating a profile via `add_profile` (from Task RPProject-A) and asserting it appears in `get_profiles()`. `get_all_stereotypes` is a read-only getter — test by creating a stereotype on a class (as in `tests/integration/models/elements/classifiers/test_model_stereotype.py`) and asserting it appears in the project-wide collection.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_project.py -m integration -v -k "Collaboration or Profile or Stereotype"`
Expected: PASS

- [ ] **Step 3: Flip checklist boxes**

Flip `getNewCollaboration`, `getProfiles`, `getAllStereotypes` to `[x] integration test`. Add new rows and flip for `addCollaboration`, `getCollaborations`, `findCollaboration`, `deleteCollaboration` (verify actual unit-test state first).

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_project.py src/rhapsody_cli/models/elements/containment/model_project.py
git commit -m "test: add RPProject collaboration and profile management integration tests"
```

---

### Task RPProject-C: RPProject — Find/search operations

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_project.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_project.py` (flip checklist boxes; add rows for `find_by_name`, `find_by_meta_class`, `get_root`)

**Methods covered:** `find_by_name`, `find_by_meta_class`, `find_element_by_guid`, `find_element_by_binary_id`, `find_element_by_file_name`, `get_cg_simplified_model_package`, `get_code_generated_files`, `get_root` (8 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_find_by_name_and_guid(self, test_project: RPProject) -> None:
    class_name = self._unique("FindableProjectClass")
    pkg = test_project.add_package(self._unique("FindPkg"))
    new_class = pkg.add_class(class_name)
    try:
        found_by_name = test_project.find_by_name(class_name)
        assert found_by_name is not None
        assert found_by_name.get_name() == class_name
        guid = new_class.get_guid()
        found_by_guid = test_project.find_element_by_guid(guid)
        assert found_by_guid is not None
        assert found_by_guid.get_guid() == guid
    finally:
        new_class.delete_from_project()
```

For remaining methods in this task, follow the same established pattern: `find_by_meta_class("Class")` should return an `RPCollection` containing `new_class`. `find_element_by_binary_id` and `find_element_by_file_name` are best tested as smoke tests confirming the call succeeds without error and, where possible, returns the expected element found via another documented ID/path (skip/xfail if Rhapsody2.Application.1 does not populate these IDs for pure in-memory elements, following the existing `xfail` documentation convention). `get_cg_simplified_model_package` and `get_code_generated_files` are read-only getters — test them as simple non-`None`/collection-returned smoke tests. `get_root` is trivial (returns `self`, no COM call) — test with `assert test_project.get_root() is test_project`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_project.py -m integration -v -k "Find or Root or CodeGenerated or Simplified"`
Expected: PASS (or documented xfail per the note above)

- [ ] **Step 3: Flip checklist boxes**

Flip `find_element_by_guid`, `findElementByBinaryID`, `findElementByFileName`, `getCgSimplifiedModelPackage`, `getCodeGeneratedFiles` to `[x] integration test`. Add new rows and flip for `find_by_name`, `find_by_meta_class`, `get_root`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_project.py src/rhapsody_cli/models/elements/containment/model_project.py
git commit -m "test: add RPProject find/search operation integration tests"
```

---

### Task RPProject-D: RPProject — Lifecycle (save/close/dirty state)

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_project.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_project.py` (flip checklist boxes; add rows for `get_is_dirty`, `set_dirty`)

**Methods covered:** `become_active_project`, `close`, `save_as`, `allow_auto_save`, `allow_non_unique_names`, `is_modified_recursive`, `locate_in_ide`, `highlight_from_code`, `get_is_dirty`, `set_dirty` (10 methods)

> **Note:** `close` must be tested very carefully — it must **not** close the session-scoped `test_project` fixture used by every other test in the suite. Create a **second, disposable** project (or skip actually invoking `close()` and instead smoke-test that the method exists and is callable against a throwaway project created via `rhapsody_app.create_new_project` in a temp directory, cleaning that directory up in `finally`) rather than calling `test_project.close()`.

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_dirty_flag_roundtrip(self, test_project: RPProject) -> None:
    original = test_project.get_is_dirty()
    try:
        test_project.set_dirty(1)
        assert test_project.get_is_dirty() == 1
        test_project.set_dirty(0)
        assert test_project.get_is_dirty() == 0
    finally:
        test_project.set_dirty(original)
```

For remaining methods in this task, follow the same established pattern: `allow_auto_save(1)`/`allow_auto_save(0)` and `allow_non_unique_names(1)`/`allow_non_unique_names(0)` are smoke tests confirming the calls succeed without error (these configure global engine behavior with no directly observable getter). `is_modified_recursive` should be tested as a smoke test asserting it returns a `bool`. `locate_in_ide` and `highlight_from_code(file_path, line_number)` are smoke tests confirming the call succeeds without raising (use a dummy path/line number; wrap in `pytest.mark.xfail` if the live IDE integration is unavailable in the test environment). `become_active_project` is a smoke test confirming the call succeeds without error on the already-active `test_project`. `save_as` and `close` should use the disposable second-project pattern described in the Note above — create a temp project, `save_as` a scratch path, then optionally `close()` it, cleaning up the directory in `finally`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_project.py -m integration -v -k "Dirty or AutoSave or NonUnique or Modified or Ide or Highlight or ActiveProject or SaveAs or Close"`
Expected: PASS (or documented xfail)

- [ ] **Step 3: Flip checklist boxes**

Flip `become_active_project`, `close`, `saveAs`, `allowAutoSave`, `allowNonUniqueNames`, `isModifiedRecursive`, `locateInIDE`, `highlightFromCode` to `[x] integration test`. Add new rows and flip for `get_is_dirty`, `set_dirty`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_project.py src/rhapsody_cli/models/elements/containment/model_project.py
git commit -m "test: add RPProject lifecycle (save/close/dirty) integration tests"
```

---

### Task RPComponent-A: RPComponent — Configuration and file management (new file)

**Files:**
- Create: `tests/integration/models/elements/containment/test_model_component.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_component.py` (flip checklist boxes)

**Methods covered:** `add_configuration`, `add_file`, `add_folder`, `add_nested_component`, `delete_configuration`, `delete_file`, `find_configuration`, `get_configurations`, `get_file`, `get_file_name`, `get_files`, `get_nested_components`, `get_package_file`, `get_panel_diagrams`, `get_path`, `set_path` (16 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPComponent, RPConfiguration, RPProject


@pytest.mark.integration
class TestRPComponentIntegration:
    """Integration tests for RPComponent with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_configuration_lifecycle(self, test_project: RPProject) -> None:
        comp_name = self._unique("ConfigComp")
        config_name = self._unique("MyConfig")
        comp = test_project.add_component(comp_name)
        try:
            config = comp.add_configuration(config_name)
            assert config is not None
            assert isinstance(config, RPConfiguration)
            assert config.get_name() == config_name
            configs = list(comp.get_configurations())
            assert config in configs
            found = comp.find_configuration(config_name)
            assert found == config
            comp.delete_configuration(config)
            remaining = [c.get_name() for c in comp.get_configurations()]
            assert config_name not in remaining
        finally:
            comp.delete_from_project()
```

For remaining methods in this task, follow the same established pattern: `add_file`/`get_files`/`get_file`/`delete_file` mirror the configuration test shape (get_file by name after add_file). `add_folder` is a simple create + `isinstance`/`get_name` smoke test. `add_nested_component` should create a nested `RPComponent` and assert it appears in `get_nested_components()`. `get_file_name`, `get_package_file`, `get_path`/`set_path` are getter/setter round-trip tests on the component itself (set then get for `set_path`/`get_path`; simple non-`None` assertions for the read-only ones). `get_panel_diagrams` is a read-only getter smoke test returning an `RPCollection`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_component.py -m integration -v`
Expected: PASS (or documented xfail)

- [ ] **Step 3: Flip checklist boxes**

In `model_component.py`, flip `addConfiguration`, `addFile`, `addFolder`, `addNestedComponent`, `deleteConfiguration`, `deleteFile`, `findConfiguration`, `getConfigurations`, `getFile`, `getFileName`, `getFiles`, `getNestedComponents`, `getPackageFile`, `getPanelDiagrams`, `getPath`, `setPath` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_component.py src/rhapsody_cli/models/elements/containment/model_component.py
git commit -m "test: add RPComponent configuration/file management integration tests"
```

---

### Task RPComponent-B: RPComponent — Scope element management

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_component.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_component.py` (flip checklist boxes)

**Methods covered:** `add_scope_element`, `add_scope_element_without_aggregates`, `add_to_scope`, `all_elements_in_scope`, `get_scope_by_selected_elements`, `get_scope_elements`, `get_scope_elements_by_category`, `remove_scope_element`, `set_scope_by_selected_elements` (9 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_scope_element_lifecycle(self, test_project: RPProject) -> None:
    comp_name = self._unique("ScopeComp")
    pkg_name = self._unique("ScopePkg")
    class_name = self._unique("ScopeClass")
    comp = test_project.add_component(comp_name)
    pkg = test_project.add_package(pkg_name)
    scoped_class = pkg.add_class(class_name)
    try:
        comp.add_scope_element(scoped_class)
        scope = list(comp.get_scope_elements())
        assert scoped_class in scope
        comp.remove_scope_element(scoped_class)
        scope_after = list(comp.get_scope_elements())
        assert scoped_class not in scope_after
    finally:
        comp.delete_from_project()
        scoped_class.delete_from_project()
```

For remaining methods in this task, follow the same established pattern: `add_scope_element_without_aggregates` and `add_to_scope` are alternate scope-add entry points — test each the same way as `add_scope_element` (add, assert membership in `get_scope_elements()`). `all_elements_in_scope` and `get_scope_elements_by_category` are read-only getters — test after populating scope, asserting the scoped element is present (for category, pass the scoped element's `get_meta_class()` as the category filter). `get_scope_by_selected_elements`/`set_scope_by_selected_elements` should be tested as a round-trip: build an `RPCollection`-compatible list/selection, call `set_scope_by_selected_elements`, then assert `get_scope_elements()` reflects it (if Rhapsody's live COM API cannot construct an `RPCollection` argument outside of one it already returned, mark as `xfail` documenting the limitation).

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_component.py -m integration -v -k Scope`
Expected: PASS (or documented xfail)

- [ ] **Step 3: Flip checklist boxes**

Flip `addScopeElement`, `addScopeElementWithoutAggregates`, `addToScope`, `allElementsInScope`, `getScopeBySelectedElements`, `getScopeElements`, `getScopeElementsByCategory`, `removeScopeElement`, `setScopeBySelectedElements` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_component.py src/rhapsody_cli/models/elements/containment/model_component.py
git commit -m "test: add RPComponent scope element management integration tests"
```

---

### Task RPComponent-C: RPComponent — Build/variant metadata properties

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_component.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_component.py` (flip checklist boxes)

**Methods covered:** `get_additional_sources`, `get_build_type`, `get_config_by_dependency`, `get_include_path`, `get_libraries`, `get_model_element_file_name`, `get_possible_variants`, `get_standard_headers`, `get_variant`, `get_variation_points`, `is_directory_per_model_component`, `set_additional_sources`, `set_build_type`, `set_include_path`, `set_libraries`, `set_standard_headers`, `set_variant`, `update_contained_diagrams_on_server` (18 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_build_type_roundtrip(self, test_project: RPProject) -> None:
    comp_name = self._unique("BuildTypeComp")
    comp = test_project.add_component(comp_name)
    try:
        comp.set_build_type("Executable")
        assert comp.get_build_type() == "Executable"
    finally:
        comp.delete_from_project()
```

For remaining methods in this task, follow the same established pattern: `set_additional_sources`/`get_additional_sources`, `set_include_path`/`get_include_path`, `set_libraries`/`get_libraries`, `set_standard_headers`/`get_standard_headers`, `set_variant`/`get_variant` are all get/set round-trip tests identical in shape to `build_type` above. `get_config_by_dependency`, `get_model_element_file_name`, `get_possible_variants`, `get_variation_points`, `is_directory_per_model_component` are read-only getter smoke tests (assert non-`None`/expected type, no round-trip possible). `update_contained_diagrams_on_server` is a smoke test confirming the call succeeds without raising (mark `xfail` if it requires a remote server connection unavailable in the test environment).

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_component.py -m integration -v -k "roundtrip or Variant or Dependency or Possible"`
Expected: PASS (or documented xfail)

- [ ] **Step 3: Flip checklist boxes**

Flip `getAdditionalSources`, `getBuildType`, `getConfigByDependency`, `getIncludePath`, `getLibraries`, `getModelElementFileName`, `getPossibleVariants`, `getStandardHeaders`, `getVariant`, `getVariationPoints`, `isDirectoryPerModelComponent`, `setAdditionalSources`, `setBuildType`, `setIncludePath`, `setLibraries`, `setStandardHeaders`, `setVariant`, `updateContainedDiagramsOnServer` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_component.py src/rhapsody_cli/models/elements/containment/model_component.py
git commit -m "test: add RPComponent build/variant metadata integration tests"
```

---

### Task RPComponentInstance: RPComponentInstance — Component type and node navigation (new file)

**Files:**
- Create: `tests/integration/models/elements/containment/test_model_component_instance.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_component_instance.py` (flip checklist boxes)

**Methods covered:** `get_component_type`, `get_node`, `set_component_type` (3 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPComponent, RPComponentInstance, RPNode, RPProject


@pytest.mark.integration
class TestRPComponentInstanceIntegration:
    """Integration tests for RPComponentInstance with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_component_type_roundtrip(self, test_project: RPProject) -> None:
        node_name = self._unique("CompInstNode")
        comp_name = self._unique("MyComponentType")
        inst_name = self._unique("MyComponentInstance")
        node = test_project.add_node(node_name)
        comp = test_project.add_component(comp_name)
        try:
            instance = node.add_component_instance(inst_name)
            assert instance is not None
            assert isinstance(instance, RPComponentInstance)
            instance.set_component_type(comp)
            comp_type = instance.get_component_type()
            assert comp_type == comp
            assert isinstance(comp_type, RPComponent)
            owning_node = instance.get_node()
            assert owning_node == node
            assert isinstance(owning_node, RPNode)
        finally:
            node.delete_from_project()
            comp.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_component_instance.py -m integration -v`
Expected: PASS

- [ ] **Step 3: Flip checklist boxes**

In `model_component_instance.py`, flip `getComponentType`, `getNode`, `setComponentType` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_component_instance.py src/rhapsody_cli/models/elements/containment/model_component_instance.py
git commit -m "test: add RPComponentInstance integration tests"
```

---

### Task RPConfiguration-A: RPConfiguration — Instance/component linkage and instrumentation scope (new file)

**Files:**
- Create: `tests/integration/models/elements/containment/test_model_configuration.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_configuration.py` (flip checklist boxes)

**Methods covered:** `add_initial_instance`, `delete_initial_instance`, `get_initial_instances`, `get_its_component`, `set_its_component`, `add_package_to_instrumentation_scope`, `add_to_instrumentation_scope`, `remove_from_instrumentation_scope`, `remove_package_from_instrumentation_scope`, `get_all_elements_in_instrumentation_scope`, `get_instrumentation_scope`, `get_instrumentation_type`, `set_instrumentation_type` (13 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPComponent, RPConfiguration, RPProject


@pytest.mark.integration
class TestRPConfigurationIntegration:
    """Integration tests for RPConfiguration with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_its_component_roundtrip(self, test_project: RPProject) -> None:
        comp_name = self._unique("ConfComp")
        config_name = self._unique("MyItsConfig")
        comp = test_project.add_component(comp_name)
        try:
            config = comp.add_configuration(config_name)
            assert isinstance(config, RPConfiguration)
            config.set_its_component(comp)
            owner = config.get_its_component()
            assert owner == comp
            assert isinstance(owner, RPComponent)
        finally:
            comp.delete_from_project()
```

For remaining methods in this task, follow the same established pattern: `add_initial_instance`/`delete_initial_instance`/`get_initial_instances` should create an `RPInstance` (e.g. via `RPNode.add_component_instance` or a package `add_instance_specification`), add it as an initial instance, assert membership in `get_initial_instances()`, then delete it and assert absence. `add_package_to_instrumentation_scope`/`add_to_instrumentation_scope`/`remove_from_instrumentation_scope`/`remove_package_from_instrumentation_scope`/`get_all_elements_in_instrumentation_scope`/`get_instrumentation_scope` mirror the scope-element pattern used in Task RPComponent-B (add a package/class to instrumentation scope, assert membership, remove, assert absence). `get_instrumentation_type`/`set_instrumentation_type` is a simple integer round-trip test.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_configuration.py -m integration -v`
Expected: PASS (or documented xfail)

- [ ] **Step 3: Flip checklist boxes**

Flip `addInitialInstance`, `deleteInitialInstance`, `getInitialInstances`, `getItsComponent`, `setItsComponent`, `addPackageToInstrumentationScope`, `addToInstrumentationScope`, `removeFromInstrumentationScope`, `removePackageFromInstrumentationScope`, `getAllElementsInInstrumentationScope`, `getInstrumentationScope`, `getInstrumentationType`, `setInstrumentationType` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_configuration.py src/rhapsody_cli/models/elements/containment/model_configuration.py
git commit -m "test: add RPConfiguration instance linkage and instrumentation scope integration tests"
```

---

### Task RPConfiguration-B: RPConfiguration — Build/compile properties

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_configuration.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_configuration.py` (flip checklist boxes)

**Methods covered:** `get_additional_sources`, `get_build_set`, `get_compiler_switches`, `get_directory`, `get_executable_name`, `get_include_path`, `get_libraries`, `get_link_switches`, `get_main_name`, `get_makefile_name`, `get_path`, `get_standard_headers`, `get_target_name`, `set_additional_sources`, `set_build_set`, `set_compiler_switches`, `set_directory`, `set_include_path`, `set_libraries`, `set_link_switches`, `set_standard_headers` (21 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_directory_roundtrip(self, test_project: RPProject) -> None:
    comp_name = self._unique("DirComp")
    config_name = self._unique("MyDirConfig")
    comp = test_project.add_component(comp_name)
    try:
        config = comp.add_configuration(config_name)
        config.set_directory("build_output")
        assert config.get_directory() == "build_output"
    finally:
        comp.delete_from_project()
```

For remaining methods in this task, follow the same established pattern: `set_additional_sources`/`get_additional_sources`, `set_build_set`/`get_build_set`, `set_compiler_switches`/`get_compiler_switches`, `set_include_path`/`get_include_path`, `set_libraries`/`get_libraries`, `set_link_switches`/`get_link_switches`, `set_standard_headers`/`get_standard_headers` are all get/set string round-trips identical in shape to `directory` above. `get_executable_name`, `get_main_name`, `get_makefile_name`, `get_path`, `get_target_name` are read-only getter smoke tests asserting they return `str` without error.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_configuration.py -m integration -v -k "roundtrip or Name or Path"`
Expected: PASS

- [ ] **Step 3: Flip checklist boxes**

Flip `getAdditionalSources`, `getBuildSet`, `getCompilerSwitches`, `getDirectory`, `getExecutableName`, `getIncludePath`, `getLibraries`, `getLinkSwitches`, `getMainName`, `getMakefileName`, `getPath`, `getStandardHeaders`, `getTargetName`, `setAdditionalSources`, `setBuildSet`, `setCompilerSwitches`, `setDirectory`, `setIncludePath`, `setLibraries`, `setLinkSwitches`, `setStandardHeaders` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_configuration.py src/rhapsody_cli/models/elements/containment/model_configuration.py
git commit -m "test: add RPConfiguration build/compile property integration tests"
```

---

### Task RPConfiguration-C: RPConfiguration — Misc/codegen properties

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_configuration.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_configuration.py` (flip checklist boxes)

**Methods covered:** `get_generate_code_for_actors`, `get_scope_type`, `get_statechart_implementation`, `get_time_model`, `needs_code_generation`, `set_all_elements_in_instrumentation_scope`, `set_generate_code_for_actors`, `get_initialization_code`, `set_initialization_code`, `set_scope_type`, `set_statechart_implementation`, `set_time_model` (12 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_generate_code_for_actors_roundtrip(self, test_project: RPProject) -> None:
    comp_name = self._unique("ActorCgComp")
    config_name = self._unique("MyActorCgConfig")
    comp = test_project.add_component(comp_name)
    try:
        config = comp.add_configuration(config_name)
        config.set_generate_code_for_actors(1)
        assert config.get_generate_code_for_actors() == 1
        config.set_generate_code_for_actors(0)
        assert config.get_generate_code_for_actors() == 0
    finally:
        comp.delete_from_project()
```

For remaining methods in this task, follow the same established pattern: `set_scope_type`/`get_scope_type`, `set_statechart_implementation`/`get_statechart_implementation`, `set_time_model`/`get_time_model`, `set_initialization_code`/`get_initialization_code` are all get/set round-trip tests identical in shape to `generate_code_for_actors` above. `needs_code_generation` is a read-only getter smoke test asserting it returns an `int`. `set_all_elements_in_instrumentation_scope` should be tested by passing the component's own `all_elements_in_scope()` (or an empty `RPCollection`) and confirming the call succeeds without error (mark `xfail` if constructing a valid `RPCollection` argument outside one returned by a getter isn't supported by the live COM API).

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_configuration.py -m integration -v -k "roundtrip or CodeGeneration or Instrumentation"`
Expected: PASS (or documented xfail)

- [ ] **Step 3: Flip checklist boxes**

Flip `getGenerateCodeForActors`, `getScopeType`, `getStatechartImplementation`, `getTimeModel`, `needsCodeGeneration`, `setAllElementsInInstrumentationScope`, `setGenerateCodeForActors`, `getInitializationCode`, `setInitializationCode`, `setScopeType`, `setStatechartImplementation`, `setTimeModel` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_configuration.py src/rhapsody_cli/models/elements/containment/model_configuration.py
git commit -m "test: add RPConfiguration misc/codegen property integration tests"
```

---

### Task RPCollaboration-A: RPCollaboration — Message and classifier role factory methods (new file)

**Files:**
- Create: `tests/integration/models/elements/containment/test_model_collaboration.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_collaboration.py` (flip checklist boxes)

**Methods covered:** `add_classifier_role`, `add_classifier_role_by_name`, `add_classifier_role_for_instance`, `add_message`, `add_found_message`, `add_lost_message`, `add_reply_message`, `get_messages`, `get_message_points`, `get_classifier`, `get_activator`, `get_associations` (12 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
import uuid

import pytest

from rhapsody_cli.models.elements.common import RPClassifierRole
from rhapsody_cli.models.elements.containment import RPCollaboration, RPProject
from rhapsody_cli.models.elements.common import RPMessage


@pytest.mark.integration
class TestRPCollaborationIntegration:
    """Integration tests for RPCollaboration with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_classifier_role_and_message_lifecycle(self, test_project: RPProject) -> None:
        collab_name = self._unique("MsgCollab")
        role_name = self._unique("MyRole")
        msg_name = self._unique("MyMessage")
        collab = test_project.add_collaboration(collab_name)
        try:
            assert isinstance(collab, RPCollaboration)
            role = collab.add_classifier_role(role_name)
            assert role is not None
            assert isinstance(role, RPClassifierRole)
            assert role.get_name() == role_name
            message = collab.add_message(msg_name)
            assert message is not None
            assert isinstance(message, RPMessage)
            messages = list(collab.get_messages())
            assert message in messages
        finally:
            test_project.delete_collaboration(collab)
```

For remaining methods in this task, follow the same established pattern: `add_classifier_role_by_name` and `add_classifier_role_for_instance` mirror `add_classifier_role` (the latter requires creating an `RPInstance`, e.g. via `RPNode.add_component_instance`, to pass in). `add_found_message`/`add_lost_message`/`add_reply_message` mirror `add_message`, each asserting membership in `get_messages()`. `get_message_points`, `get_classifier`, `get_activator`, `get_associations` are read-only getter smoke tests asserting the expected type or `RPCollection`/`None`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_collaboration.py -m integration -v`
Expected: PASS (or documented xfail)

- [ ] **Step 3: Flip checklist boxes**

Flip `addClassifierRole`, `addClassifierRoleByName`, `addClassifierRoleForInstance`, `addMessage`, `addFoundMessage`, `addLostMessage`, `addReplyMessage`, `getMessages`, `getMessagePoints`, `getClassifier`, `getActivator`, `getAssociations` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_collaboration.py src/rhapsody_cli/models/elements/containment/model_collaboration.py
git commit -m "test: add RPCollaboration message/classifier role integration tests"
```

---

### Task RPCollaboration-B: RPCollaboration — Interaction structure factory methods

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_collaboration.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_collaboration.py` (flip checklist boxes)

**Methods covered:** `add_action_block`, `add_cancelled_timeout`, `add_condition_mark`, `add_ctor`, `add_data_flow`, `add_destruction_event`, `add_dtor`, `add_duration_constraint`, `add_duration_observation`, `add_interaction_occurrence`, `add_interaction_operator`, `add_state_invariant`, `add_system_border`, `add_time_constraint`, `add_time_interval`, `add_time_observation`, `add_timeout`, `get_interaction_occurrences`, `get_interaction_operators`, `get_execution_occurrences` (20 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_interaction_occurrence_lifecycle(self, test_project: RPProject) -> None:
    collab_name = self._unique("InterOccCollab")
    occ_name = self._unique("MyInteractionOccurrence")
    collab = test_project.add_collaboration(collab_name)
    try:
        occurrence = collab.add_interaction_occurrence(occ_name)
        assert occurrence is not None
        assert occurrence.get_name() == occ_name
        occurrences = list(collab.get_interaction_occurrences())
        assert occurrence in occurrences
    finally:
        test_project.delete_collaboration(collab)
```

For remaining methods in this task, follow the same established pattern: `add_action_block`, `add_cancelled_timeout`, `add_condition_mark`, `add_ctor`, `add_data_flow`, `add_destruction_event`, `add_dtor`, `add_duration_constraint`, `add_duration_observation`, `add_state_invariant`, `add_system_border`, `add_time_constraint`, `add_time_interval`, `add_time_observation`, `add_timeout` are all simple create + `isinstance`/`get_name` smoke tests with no dedicated getter (assert the element is created without error; use `delete_from_project()` for cleanup where the returned wrapper supports it). `add_interaction_operator`/`get_interaction_operators` mirrors the `add_interaction_occurrence` test shape above. `get_execution_occurrences` is a read-only getter smoke test asserting an `RPCollection` is returned.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_collaboration.py -m integration -v -k "Interaction or Timeout or Constraint or Observation or Ctor or Dtor or Border or Invariant or DataFlow or ActionBlock or ConditionMark"`
Expected: PASS (or documented xfail)

- [ ] **Step 3: Flip checklist boxes**

Flip `addActionBlock`, `addCancelledTimeout`, `addConditionMark`, `addCtor`, `addDataFlow`, `addDestructionEvent`, `addDtor`, `addDurationConstraint`, `addDurationObservation`, `addInteractionOccurrence`, `addInteractionOperator`, `addStateInvariant`, `addSystemBorder`, `addTimeConstraint`, `addTimeInterval`, `addTimeObservation`, `addTimeout`, `getInteractionOccurrences`, `getInteractionOperators`, `getExecutionOccurrences` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_collaboration.py src/rhapsody_cli/models/elements/containment/model_collaboration.py
git commit -m "test: add RPCollaboration interaction structure integration tests"
```

---

### Task RPCollaboration-C: RPCollaboration — Metadata and sequencing navigation

**Files:**
- Modify: `tests/integration/models/elements/containment/test_model_collaboration.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_collaboration.py` (flip checklist boxes)

**Methods covered:** `generate_sequence`, `get_activation_condition`, `get_activation_mode`, `get_concurrent_group`, `get_mode`, `get_predecessor`, `get_successor` (7 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_generate_sequence_and_metadata(self, test_project: RPProject) -> None:
    collab_name = self._unique("MetaCollab")
    collab = test_project.add_collaboration(collab_name)
    try:
        collab.generate_sequence()
        assert isinstance(collab.get_activation_condition(), str)
        assert isinstance(collab.get_activation_mode(), int)
        assert isinstance(collab.get_concurrent_group(), int)
        assert isinstance(collab.get_mode(), int)
    finally:
        test_project.delete_collaboration(collab)
```

For remaining methods in this task, follow the same established pattern: `get_predecessor`/`get_successor` are read-only getter smoke tests asserting they return `None` or a valid `RPUnit`-typed object without error for a freshly-created, unlinked collaboration.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_collaboration.py -m integration -v -k "Sequence or Metadata or Predecessor or Successor"`
Expected: PASS

- [ ] **Step 3: Flip checklist boxes**

Flip `generateSequence`, `getActivationCondition`, `getActivationMode`, `getConcurrentGroup`, `getMode`, `getPredecessor`, `getSuccessor` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_collaboration.py src/rhapsody_cli/models/elements/containment/model_collaboration.py
git commit -m "test: add RPCollaboration metadata and sequencing navigation integration tests"
```

---

### Task RPNode: RPNode — Component instance management and CPU type (new file)

**Files:**
- Create: `tests/integration/models/elements/containment/test_model_node.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_node.py` (flip checklist boxes)

**Methods covered:** `add_component_instance`, `delete_component_instance`, `find_component_instance`, `get_cpu_type`, `get_component_instances`, `set_cpu_type` (6 methods)

- [ ] **Step 1: Write the failing/new integration tests**

```python
import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPComponentInstance, RPNode, RPProject


@pytest.mark.integration
class TestRPNodeIntegration:
    """Integration tests for RPNode with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_component_instance_lifecycle(self, test_project: RPProject) -> None:
        node_name = self._unique("MyNode")
        inst_name = self._unique("MyCompInst")
        node = test_project.add_node(node_name)
        assert isinstance(node, RPNode)
        try:
            instance = node.add_component_instance(inst_name)
            assert instance is not None
            assert isinstance(instance, RPComponentInstance)
            assert instance.get_name() == inst_name
            instances = list(node.get_component_instances())
            assert instance in instances
            found = node.find_component_instance(inst_name)
            assert found == instance
            node.delete_component_instance(instance)
            remaining = [i.get_name() for i in node.get_component_instances()]
            assert inst_name not in remaining
        finally:
            node.delete_from_project()

    def test_cpu_type_roundtrip(self, test_project: RPProject) -> None:
        node_name = self._unique("CpuNode")
        node = test_project.add_node(node_name)
        try:
            node.set_cpu_type("x86_64")
            assert node.get_cpu_type() == "x86_64"
        finally:
            node.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/containment/test_model_node.py -m integration -v`
Expected: PASS

- [ ] **Step 3: Flip checklist boxes**

In `model_node.py`, flip `addComponentInstance`, `deleteComponentInstance`, `findComponentInstance`, `getCPUtype`, `getComponentInstances`, `setCPUtype` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/containment/test_model_node.py src/rhapsody_cli/models/elements/containment/model_node.py
git commit -m "test: add RPNode integration tests"
```

---

### Task Final: Full Subpackage Verification

- [ ] **Step 1: Run the entire containment integration suite**

Run: `pytest tests/integration/models/elements/containment -m integration -v`
Expected: All tests PASS (or explicitly documented `xfail`)

- [ ] **Step 2: Confirm every checklist row across all 9 containment files shows `[x] integration test`**

Verify no remaining `[ ] integration test` rows exist for implemented (`[x] impl`) methods in `model_project.py`, `model_package.py`, `model_component.py`, `model_component_instance.py`, `model_configuration.py`, `model_collaboration.py`, `model_node.py` (grep for `\[ \] integration test` alongside `\[x\] impl` in each file — any remaining hits indicate a missed task).

- [ ] **Step 3: Run unit tests to confirm no regressions**

Run: `pytest tests/unit -q`
Expected: All unit tests PASS

- [ ] **Step 4: Run full quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit final verification note (if any stragglers were found and fixed)**

```bash
git add -A
git commit -m "test: complete containment subpackage integration test coverage"
```

## Success Criteria

- Every implemented (`[x] impl`) method across `RPProject`, `RPPackage`, `RPComponent`, `RPComponentInstance`, `RPConfiguration`, `RPCollaboration`, `RPNode` has an integration test (or a documented `xfail` where the live Rhapsody COM API does not support the operation, following the existing pattern in `tests/integration/models/elements/classifiers/test_model_signal.py`)
- `RPModule` and `RPProfile` require no new work (inheritance-only wrappers)
- No test leaves behind orphan elements in the Rhapsody model or closes the shared `test_project` fixture
- All existing integration tests continue to pass
- Unit tests are unaffected (0 regressions)
