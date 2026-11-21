# RPClass Python Property Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace `RPClass`'s own `get_is_*` / `set_is_*` methods with snake_case Python `@property` accessors, one class at a time, starting with `RPClass`.

**Architecture:** This is a deliberate breaking API change for one wrapper class only. The COM calls stay exactly as they are (Java-style name first, pywin32 property name second via `_get_method_or_property` / `_set_method_or_property`); only the Python-facing surface changes from methods to attributes. Callers in the CLI action layer, unit tests, and integration tests are migrated in the same change so the repository stays green.

**Tech Stack:** Python 3.8+ (`@property`, snake_case per `docs/CODE_GUIDELINES.md`), pytest, ruff/black/mypy strict.

---

## Scope

`RPClass` defines 10 methods to convert, forming **6 properties**:

| Property | Getter replaced | Setter replaced | Type |
|---|---|---|---|
| `is_abstract` | `get_is_abstract()` | `set_is_abstract()` (always raises `NotImplementedError`) | `bool` |
| `is_active` | `get_is_active()` | `set_is_active()` | `int` |
| `is_behavior_overriden` | `get_is_behavior_overriden()` | `set_is_behavior_overriden()` | `int` |
| `is_composite` | `get_is_composite()` | — (read-only) | `int` |
| `is_final` | `get_is_final()` | `set_is_final()` | `int` |
| `is_reactive` | `get_is_reactive()` | — (read-only) | `int` |

`is_abstract` uses `bool` for both getter and setter because mypy requires the setter argument type to be compatible with the getter return type; the setter converts `bool` to `1`/`0` for COM. The always-raising behavior of the old `set_is_abstract` is preserved.

**Non-goals:**
- No other class is converted in this plan (`RPOperation`, `RPActor`, `RPUseCase` keep their methods). A follow-up plan handles each class separately.
- No generic `@property` infrastructure, descriptors, or changes to `RPModelElement`.
- No change to COM call shapes — the pywin32-authoritative binding work in PR #122 stays on its own branch.

**Dependency on PR #122:** that plan records a `documented_aliases` entry `get_is_abstract → is_abstract`. Once this migration lands, the Python name *is* `is_abstract`, so that alias becomes obsolete. Task 6 verifies and removes it if the authority file is present. Merge order: PR #122 first, then this one, then rebase if needed.

## File structure

| File | Responsibility |
|---|---|
| `src/rhapsody_cli/models/elements/classifiers/model_class.py` | 6 properties replace 10 methods; parity checklist updated. |
| `tests/unit/models/elements/classifiers/test_model_class.py` | 10 tests updated to attribute access. |
| `src/rhapsody_cli/actions/class_action.py` | 9 CLI call sites updated to attribute access. |
| `tests/integration/models/elements/classifiers/test_model_class.py` | Live tests updated to attribute access. |
| `docs/reports/pywin32_authority.json` (only if present) | Remove obsolete `get_is_abstract` alias after merge. |

## Preflight

```bash
git switch refactor/rpclass-python-properties
git fetch origin
```

---

### Task 1: Failing unit tests for RPClass properties

**Files:** `tests/unit/models/elements/classifiers/test_model_class.py`

- [ ] **Step 1: Replace the getter tests with property tests**

Replace `test_class_get_is_abstract_delegates_to_com` (line 56) with:

```python
def test_class_is_abstract_property_delegates_to_com() -> None:
    fake = make_fake_element("Class", getIsAbstract=1)
    klass = RPClass(fake)

    assert klass.is_abstract is True
```

Replace the five getter tests at lines 258-289 with:

```python
def test_class_is_active_property_delegates_to_com() -> None:
    fake = make_fake_element("Class", getIsActive=1)
    klass = RPClass(fake)

    assert klass.is_active == 1


def test_class_is_behavior_overriden_property_delegates_to_com() -> None:
    fake = make_fake_element("Class", getIsBehaviorOverriden=0)
    klass = RPClass(fake)

    assert klass.is_behavior_overriden == 0


def test_class_is_composite_property_delegates_to_com() -> None:
    fake = make_fake_element("Class", getIsComposite=1)
    klass = RPClass(fake)

    assert klass.is_composite == 1


def test_class_is_final_property_delegates_to_com() -> None:
    fake = make_fake_element("Class", getIsFinal=0)
    klass = RPClass(fake)

    assert klass.is_final == 0


def test_class_is_reactive_property_delegates_to_com() -> None:
    fake = make_fake_element("Class", getIsReactive=1)
    klass = RPClass(fake)

    assert klass.is_reactive == 1
```

- [ ] **Step 2: Replace the setter tests with property-assignment tests**

Replace the four setter tests at lines 292-327 with:

```python
def test_class_is_abstract_setter_raises_not_implemented() -> None:
    fake = make_fake_element("Class")
    klass = RPClass(fake)

    with pytest.raises(NotImplementedError):
        klass.is_abstract = True

    fake.setIsAbstract.assert_not_called()


def test_class_is_active_setter_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    klass = RPClass(fake)

    klass.is_active = 0

    fake.setIsActive.assert_called_once_with(0)


def test_class_is_behavior_overriden_setter_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    klass = RPClass(fake)

    klass.is_behavior_overriden = 1

    fake.setIsBehaviorOverriden.assert_called_once_with(1)


def test_class_is_final_setter_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    klass = RPClass(fake)

    klass.is_final = 1

    fake.setIsFinal.assert_called_once_with(1)
```

- [ ] **Step 3: Run the tests to verify they fail**

```bash
pytest tests/unit/models/elements/classifiers/test_model_class.py -q -k 'is_abstract or is_active or is_behavior_overriden or is_composite or is_final or is_reactive'
```

Expected: failures because `RPClass` has no such attributes.

- [ ] **Step 4: Commit the failing tests**

```bash
git add tests/unit/models/elements/classifiers/test_model_class.py
git commit -m "test(unit): expect RPClass boolean flags as properties"
```

---

### Task 2: Implement the six properties in RPClass

**Files:** `src/rhapsody_cli/models/elements/classifiers/model_class.py`

- [ ] **Step 1: Replace `get_is_abstract` and `set_is_abstract` with one property**

Replace both methods (lines 86-95 and 390-411) with:

```python
    @property
    def is_abstract(self) -> bool:
        """Checks whether this class is abstract."""
        return bool(AbstractRPModelElement._get_method_or_property(self._com, "getIsAbstract", "isAbstract"))

    @is_abstract.setter
    def is_abstract(self, is_abstract: bool) -> None:
        """Unimplemented: the COM write is accepted but never persists.

        See the original Rhapsody2.Application.1 investigation: the type library declares
        PROPERTYGET and PROPERTYPUT for ``isAbstract`` under the same DISPID, but writes do not
        survive read-back, ``saveAll()``, or a fresh re-fetch. Raises rather than silently
        no-opping.
        """
        raise NotImplementedError("RPClass.is_abstract setter is unimplemented: Rhapsody2.Application.1 accepts the write but never persists it.")
```

- [ ] **Step 2: Replace the remaining getter/setter pairs with properties**

Replace `get_is_active` (lines 328-339) and `set_is_active` (lines 413-422) with:

```python
    @property
    def is_active(self) -> int:
        """``1`` if the class runs on its own thread, ``0`` if sequential."""
        return int(AbstractRPModelElement._get_method_or_property(self._com, "getIsActive", "isActive"))

    @is_active.setter
    def is_active(self, is_active: int) -> None:
        """Set to ``1`` for active, ``0`` for sequential."""
        AbstractRPModelElement._set_method_or_property(self._com, "setIsActive", "isActive", is_active)
```

Replace `get_is_behavior_overriden` (lines 341-350) and `set_is_behavior_overriden` (lines 424-433) with:

```python
    @property
    def is_behavior_overriden(self) -> int:
        """``1`` if the class does not inherit its base statechart behavior, else ``0``."""
        return int(AbstractRPModelElement._get_method_or_property(self._com, "getIsBehaviorOverriden", "isBehaviorOverriden"))

    @is_behavior_overriden.setter
    def is_behavior_overriden(self, is_behavior_overriden: int) -> None:
        """Set to ``1`` to not inherit the base statechart behavior, ``0`` to inherit."""
        AbstractRPModelElement._set_method_or_property(self._com, "setIsBehaviorOverriden", "isBehaviorOverriden", is_behavior_overriden)
```

Replace `get_is_final` (lines 363-374) and `set_is_final` (lines 435-446) with:

```python
    @property
    def is_final(self) -> int:
        """``1`` if the class is final, ``0`` otherwise (relevant for Java classes)."""
        return int(AbstractRPModelElement._get_method_or_property(self._com, "getIsFinal", "isFinal"))

    @is_final.setter
    def is_final(self, new_val: int) -> None:
        """Set to ``1`` to make the class final, ``0`` otherwise."""
        AbstractRPModelElement._set_method_or_property(self._com, "setIsFinal", "isFinal", new_val)
```

Replace the two read-only getters `get_is_composite` (lines 352-361) and `get_is_reactive` (lines 376-388) with:

```python
    @property
    def is_composite(self) -> int:
        """``1`` if the class is a composite class, ``0`` otherwise."""
        return int(AbstractRPModelElement._get_method_or_property(self._com, "getIsComposite", "isComposite"))
```

```python
    @property
    def is_reactive(self) -> int:
        """``1`` if the class has a statechart or activity diagram, ``0`` otherwise."""
        return int(AbstractRPModelElement._get_method_or_property(self._com, "getIsReactive", "isReactive"))
```

- [ ] **Step 3: Update the parity checklist**

Replace these rows in the class docstring checklist:

```python
    # [x] get_is_abstract            [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_is_active              [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_is_behavior_overriden   [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_is_composite           [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_is_final               [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_is_reactive            [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_is_abstract (unimplemented -- raises not_implemented_error, see docstring)  [ ] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_is_active              [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_is_behavior_overriden   [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_is_final               [x] impl  [x] docstring  [x] unit test  [x] integration test
```

with:

```python
    # [x] is_abstract                [x] impl (property) [x] docstring [x] unit test [x] integration test
    # [x] is_active                  [x] impl (property) [x] docstring [x] unit test [x] integration test
    # [x] is_behavior_overriden      [x] impl (property) [x] docstring [x] unit test [x] integration test
    # [x] is_composite               [x] impl (property) [x] docstring [x] unit test [x] integration test
    # [x] is_final                   [x] impl (property) [x] docstring [x] unit test [x] integration test
    # [x] is_reactive                [x] impl (property) [x] docstring [x] unit test [x] integration test
```

- [ ] **Step 4: Run the unit tests to verify they pass**

```bash
pytest tests/unit/models/elements/classifiers/test_model_class.py -q
```

Expected: all tests pass.

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/models/elements/classifiers/model_class.py
git commit -m "refactor: expose RPClass boolean flags as Python properties"
```

---

### Task 3: Migrate CLI call sites

**Files:** `src/rhapsody_cli/actions/class_action.py`

- [ ] **Step 1: Update attribute writes**

Apply these exact replacements (keep the existing `# type: ignore[attr-defined]` comments):

```python
            cls.set_is_abstract(1 if attrs["isAbstract"] else 0)  # type: ignore[attr-defined]
```
→
```python
            cls.is_abstract = bool(attrs["isAbstract"])  # type: ignore[attr-defined]
```

```python
            cls.set_is_final(1 if attrs["isFinal"] else 0)  # type: ignore[attr-defined]
```
→
```python
            cls.is_final = 1 if attrs["isFinal"] else 0  # type: ignore[attr-defined]
```

```python
            cls.set_is_active(1 if attrs["isActive"] else 0)  # type: ignore[attr-defined]
```
→
```python
            cls.is_active = 1 if attrs["isActive"] else 0  # type: ignore[attr-defined]
```

In the third occurrence block, replace:

```python
                cls.set_is_abstract(1 if value else 0)  # type: ignore[attr-defined]
```
→
```python
                cls.is_abstract = bool(value)  # type: ignore[attr-defined]
```

```python
                cls.set_is_final(1 if value else 0)  # type: ignore[attr-defined]
```
→
```python
                cls.is_final = 1 if value else 0  # type: ignore[attr-defined]
```

```python
                cls.set_is_active(1 if value else 0)  # type: ignore[attr-defined]
```
→
```python
                cls.is_active = 1 if value else 0  # type: ignore[attr-defined]
```

- [ ] **Step 2: Update attribute reads**

Replace the five reads in `_collect_class_data`:

```python
            "isAbstract": int(cls.get_is_abstract()),  # type: ignore[attr-defined]
            "isActive": int(cls.get_is_active()),  # type: ignore[attr-defined]
            "isFinal": int(cls.get_is_final()),  # type: ignore[attr-defined]
            "isComposite": int(cls.get_is_composite()),  # type: ignore[attr-defined]
            "isReactive": int(cls.get_is_reactive()),  # type: ignore[attr-defined]
```

with:

```python
            "isAbstract": int(cls.is_abstract),  # type: ignore[attr-defined]
            "isActive": int(cls.is_active),  # type: ignore[attr-defined]
            "isFinal": int(cls.is_final),  # type: ignore[attr-defined]
            "isComposite": int(cls.is_composite),  # type: ignore[attr-defined]
            "isReactive": int(cls.is_reactive),  # type: ignore[attr-defined]
```

Do **not** change `operation_action.py` — `RPOperation` is not converted in this plan.

- [ ] **Step 3: Run CLI unit tests**

```bash
pytest tests/unit/actions -q
```

Expected: all pass.

- [ ] **Step 4: Commit**

```bash
git add src/rhapsody_cli/actions/class_action.py
git commit -m "refactor: use RPClass properties in class CLI actions"
```

---

### Task 4: Migrate RPClass integration tests

**Files:** `tests/integration/models/elements/classifiers/test_model_class.py`

- [ ] **Step 1: Replace method calls with attribute access**

Apply these replacements throughout the file (live assertions keep the same values):

- `test_class.get_is_abstract()` → `test_class.is_abstract`
- `test_class.get_is_active()` → `test_class.is_active`
- `test_class.get_is_behavior_overriden()` → `test_class.is_behavior_overriden`
- `test_class.get_is_composite()` → `test_class.is_composite`
- `test_class.get_is_final()` → `test_class.is_final`
- `test_class.get_is_reactive()` → `test_class.is_reactive`
- `test_class.set_is_active(1)` → `test_class.is_active = 1`
- `test_class.set_is_active(0)` → `test_class.is_active = 0`
- `test_class.set_is_behavior_overriden(1)` → `test_class.is_behavior_overriden = 1`
- `test_class.set_is_behavior_overriden(0)` → `test_class.is_behavior_overriden = 0`
- `test_class.set_is_final(1)` → `test_class.is_final = 1`
- `test_class.set_is_final(0)` → `test_class.is_final = 0`

For the abstract flag, keep the documented failure expectation but use assignment:

```python
            with pytest.raises(NotImplementedError):
                test_class.is_abstract = True
```

Leave tests for `RPActor`, `RPOperation`, and `RPUseCase` unchanged — those classes retain methods.

- [ ] **Step 2: Verify collection offline**

```bash
pytest tests/integration/models/elements/classifiers/test_model_class.py --collect-only -q
```

Expected: collection succeeds.

- [ ] **Step 3: Commit**

```bash
git add tests/integration/models/elements/classifiers/test_model_class.py
git commit -m "test(integration): use RPClass boolean properties"
```

---

### Task 5: Validator and report compatibility

**Files:** none unless `docs/reports/pywin32_authority.json` is present.

- [ ] **Step 1: Confirm the validator still recognizes the wrappers**

`@property` methods remain `ast.FunctionDef` nodes, so `collect_python_members` sees `is_abstract` instead of `get_is_abstract`. The canonical Java name `getIsAbstract` also becomes `is_abstract`, so the label now matches and no validator code change is needed.

Run:

```bash
python scripts/validate_model_api.py IRPClass --path /tmp/rpclass-property-report
```

Expected: a report is generated; the `get_is_abstract` `PYTHON_METHOD_NAME_MISMATCH` row is gone. Live pywin32 is required for this command — on non-Windows, skip and rely on Task 1 unit tests.

- [ ] **Step 2: Remove the obsolete alias if PR #122 has merged**

If `docs/reports/pywin32_authority.json` exists, delete the `get_is_abstract` entry from `documented_aliases.IRPClass` — the Python name is now exactly the canonical name. Keep the rest of the alias map unchanged.

- [ ] **Step 3: Commit (only if a file changed)**

```bash
git add docs/reports/pywin32_authority.json
git commit -m "docs: drop obsolete get_is_abstract alias after property migration"
```

---

### Task 6: Quality gate and push

**Files:** none.

- [ ] **Step 1: Install deps if needed**

```bash
pip install -e ".[dev,cli]"
```

- [ ] **Step 2: Run the gate**

```bash
ruff check src/ tests/ scripts/ && black --check src/ tests/ scripts/ && mypy src/ tests/ scripts/ && pytest tests/unit/
```

On macOS/Linux, inject a temporary `pywintypes` stub:

```bash
STUB=$(mktemp -d); printf 'class com_error(Exception):\n    def __init__(self, *args):\n        self.args = args\n        super().__init__(*args)\n' > "$STUB/pywintypes.py"; PYTHONPATH="${STUB}:src" python -m pytest tests/unit/ -q; rm -rf "$STUB"
```

Expected: all checks pass.

- [ ] **Step 3: Push**

```bash
git push -u origin refactor/rpclass-python-properties
```

## Self-review

**Spec coverage:** All 10 RPClass methods are replaced by 6 properties; unit tests, CLI call sites, and integration tests are migrated in the same change. Other classes are explicitly untouched, including the intentionally failing `set_is_abstract` behavior.

**Placeholder scan:** Every code-changing step includes complete replacement code; no TBD steps.

**Type consistency:** `is_abstract` is `bool` on both getter and setter (setter converts to `1`/`0` for COM) to satisfy mypy strict; all other flags are `int` on both sides. The CLI reads keep `int(...)` so the JSON output format does not change.

**Breaking-change note:** Any external caller of the removed methods must migrate to attribute access. This is intentional and is the reason for a separate branch and tracking issue.
