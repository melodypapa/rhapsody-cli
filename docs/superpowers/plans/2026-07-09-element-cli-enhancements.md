# Element CLI Enhancements Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add multi-level (`/` or `\`) path navigation and bulk/recursive operations to the `element` CLI commands (`add`, `view`, `query`, `delete`), replacing the current hardcoded "Default package" lookup and `::`-style paths.

**Architecture:** A new pure-logic `PathResolver` utility (in `src/rhapsody_cli/cli/path_resolver.py`) parses `/`/`\`-separated paths and navigates `getNestedElements()` hierarchies. Each `Element*Action` class in `src/rhapsody_cli/actions/element_action.py` is updated to use `PathResolver` instead of its own inline navigation, and gains new flags: `--path` (add/query), `--bulk` (add), `--recursive` (query/delete), `--force` (delete).

**Tech Stack:** Python 3.8+, argparse (stdlib), pytest with `unittest.mock.MagicMock` fakes (existing convention in `tests/unit/commands/test_element_commands.py`), mypy strict mode, ruff, black.

**Reference spec:** `docs/superpowers/specs/2026-07-09-element-cli-enhancements-design.md`

---

## Task 1: Create the `PathResolver` utility

**Files:**
- Create: `src/rhapsody_cli/cli/path_resolver.py`
- Test: `tests/unit/cli/test_path_resolver.py`

- [ ] **Step 1: Write the failing tests**

Create `tests/unit/cli/test_path_resolver.py`:

```python
"""Tests for PathResolver path parsing and navigation."""

from typing import List, Optional

import pytest

from rhapsody_cli.cli.path_resolver import PathResolver, PathResolverError


class _FakeElement:
    """Minimal stand-in for a wrapped model element with a name and children."""

    def __init__(self, name: str, children: Optional[List["_FakeElement"]] = None) -> None:
        self._name = name
        self._children = children or []

    def getName(self) -> str:
        return self._name

    def getNestedElements(self) -> List["_FakeElement"]:
        return self._children


class TestNormalize:
    """Tests for PathResolver.normalize."""

    def test_converts_backslashes_to_forward_slashes(self) -> None:
        assert PathResolver.normalize("pkg\\subpkg") == "pkg/subpkg"

    def test_strips_leading_and_trailing_slashes(self) -> None:
        assert PathResolver.normalize("/pkg/subpkg/") == "pkg/subpkg"

    def test_handles_mixed_separators(self) -> None:
        assert PathResolver.normalize("pkg/subpkg\\class") == "pkg/subpkg/class"


class TestSplitSegments:
    """Tests for PathResolver.split_segments."""

    def test_splits_simple_path(self) -> None:
        assert PathResolver.split_segments("pkg/subpkg/class") == ["pkg", "subpkg", "class"]

    def test_drops_leading_root_alias(self) -> None:
        assert PathResolver.split_segments("Root/pkg/class") == ["pkg", "class"]

    def test_raises_on_empty_path(self) -> None:
        with pytest.raises(PathResolverError, match="cannot be empty"):
            PathResolver.split_segments("")

    def test_raises_on_double_slash(self) -> None:
        with pytest.raises(PathResolverError, match="Invalid path syntax"):
            PathResolver.split_segments("pkg//class")


class TestResolveContainer:
    """Tests for PathResolver.resolve_container."""

    def test_returns_root_when_path_is_none(self) -> None:
        root = _FakeElement("Root")
        assert PathResolver.resolve_container(root, None) is root

    def test_returns_root_when_path_is_empty_string(self) -> None:
        root = _FakeElement("Root")
        assert PathResolver.resolve_container(root, "") is root

    def test_navigates_single_level(self) -> None:
        pkg = _FakeElement("pkg")
        root = _FakeElement("Root", children=[pkg])
        assert PathResolver.resolve_container(root, "pkg") is pkg

    def test_navigates_multiple_levels(self) -> None:
        subpkg = _FakeElement("subpkg")
        pkg = _FakeElement("pkg", children=[subpkg])
        root = _FakeElement("Root", children=[pkg])
        assert PathResolver.resolve_container(root, "pkg/subpkg") is subpkg

    def test_navigates_using_backslash_separators(self) -> None:
        subpkg = _FakeElement("subpkg")
        pkg = _FakeElement("pkg", children=[subpkg])
        root = _FakeElement("Root", children=[pkg])
        assert PathResolver.resolve_container(root, "pkg\\subpkg") is subpkg

    def test_raises_when_segment_not_found(self) -> None:
        pkg = _FakeElement("pkg")
        root = _FakeElement("Root", children=[pkg])
        with pytest.raises(PathResolverError, match="not found: 'unknown'"):
            PathResolver.resolve_container(root, "pkg/unknown")


class TestResolveElement:
    """Tests for PathResolver.resolve_element."""

    def test_navigates_to_leaf_element(self) -> None:
        cls = _FakeElement("MyClass")
        pkg = _FakeElement("pkg", children=[cls])
        root = _FakeElement("Root", children=[pkg])
        assert PathResolver.resolve_element(root, "pkg/MyClass") is cls

    def test_navigates_single_segment_from_root(self) -> None:
        cls = _FakeElement("MyClass")
        root = _FakeElement("Root", children=[cls])
        assert PathResolver.resolve_element(root, "MyClass") is cls

    def test_raises_on_empty_path(self) -> None:
        root = _FakeElement("Root")
        with pytest.raises(PathResolverError, match="cannot be empty"):
            PathResolver.resolve_element(root, "")

    def test_raises_when_element_not_found(self) -> None:
        pkg = _FakeElement("pkg")
        root = _FakeElement("Root", children=[pkg])
        with pytest.raises(PathResolverError, match="not found: 'Missing'"):
            PathResolver.resolve_element(root, "pkg/Missing")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/unit/cli/test_path_resolver.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'rhapsody_cli.cli.path_resolver'`

- [ ] **Step 3: Write the `PathResolver` implementation**

Create `src/rhapsody_cli/cli/path_resolver.py`:

```python
"""Parses and navigates multi-level element paths using "/" or "\\" separators."""

from typing import List, Optional, Protocol


class PathResolverError(Exception):
    """Raised when a path string cannot be parsed or navigated to an element."""


class _Navigable(Protocol):
    """Structural type for anything PathResolver can navigate: needs a name and children."""

    def getName(self) -> str:
        ...  # pragma: no cover - structural protocol

    def getNestedElements(self) -> object:
        ...  # pragma: no cover - structural protocol


class PathResolver:
    """Parses "/" or "\\"-separated element paths and navigates element hierarchies.

    Paths may optionally start with a "Root" segment (case-insensitive), which is
    ignored since navigation always starts from the caller-supplied root element.
    """

    _ROOT_ALIAS = "root"

    @staticmethod
    def normalize(path: str) -> str:
        """Convert "\\" separators to "/" and strip leading/trailing slashes."""
        normalized = path.replace("\\", "/").strip()
        return normalized.strip("/")

    @staticmethod
    def split_segments(path: str) -> List[str]:
        """Split a path into non-empty segments, dropping a leading "Root" alias.

        Args:
            path: The raw path string (e.g. "pkg/subpkg/class" or "Root\\pkg").

        Returns:
            The list of path segments, excluding a leading "Root" alias.

        Raises:
            PathResolverError: If the path is empty, or contains an empty
                segment (e.g. "pkg//class").
        """
        normalized = PathResolver.normalize(path)
        if not normalized:
            raise PathResolverError("Path cannot be empty")

        raw_segments = normalized.split("/")
        if any(segment == "" for segment in raw_segments):
            raise PathResolverError(f"Invalid path syntax: '{path}'")

        if raw_segments[0].lower() == PathResolver._ROOT_ALIAS:
            raw_segments = raw_segments[1:]

        if not raw_segments:
            raise PathResolverError("Path cannot be empty")

        return raw_segments

    @staticmethod
    def resolve_container(root: _Navigable, path: Optional[str]) -> _Navigable:
        """Navigate from root to the container described by path.

        Args:
            root: The starting element (typically the project root).
            path: A "/" or "\\"-separated path to the container, or None/""
                to mean the root itself.

        Returns:
            The element found at the end of the path (or root if path is empty).

        Raises:
            PathResolverError: If any path segment cannot be found.
        """
        if not path:
            return root
        segments = PathResolver.split_segments(path)
        return PathResolver._navigate(root, segments, path)

    @staticmethod
    def resolve_element(root: _Navigable, path: str) -> _Navigable:
        """Navigate from root to the element described by path.

        Args:
            root: The starting element (typically the project root).
            path: A "/" or "\\"-separated path to the element (the last
                segment is the element itself, not a container).

        Returns:
            The element found at the end of the path.

        Raises:
            PathResolverError: If the path is empty or any segment cannot be found.
        """
        segments = PathResolver.split_segments(path)
        return PathResolver._navigate(root, segments, path)

    @staticmethod
    def _navigate(root: _Navigable, segments: List[str], original_path: str) -> _Navigable:
        """Walk `segments` from `root`, matching each against child getName()."""
        current = root
        visited: List[str] = []
        for segment in segments:
            found = None
            for child in current.getNestedElements():  # type: ignore[attr-defined]
                if child.getName() == segment:
                    found = child
                    break
            if found is None:
                stopped_at = "/".join(visited) if visited else "<root>"
                raise PathResolverError(
                    f"Could not navigate to '{original_path}' — stopped at "
                    f"'{stopped_at}' (not found: '{segment}')"
                )
            current = found
            visited.append(segment)
        return current
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/unit/cli/test_path_resolver.py -v`
Expected: PASS (all 15 tests)

- [ ] **Step 5: Run mypy on the new file**

Run: `mypy src/rhapsody_cli/cli/path_resolver.py`
Expected: `Success: no issues found`

- [ ] **Step 6: Commit**

```bash
git add src/rhapsody_cli/cli/path_resolver.py tests/unit/cli/test_path_resolver.py
git commit -m "feat: add PathResolver for multi-level element path navigation"
```

---

## Task 2: Enhance `ElementAddAction` with `--path` and `--bulk`

**Files:**
- Modify: `src/rhapsody_cli/actions/element_action.py` (imports + `ElementAddAction` class)
- Modify: `tests/unit/commands/test_element_commands.py` (`TestElementAddAction` class)

- [ ] **Step 1: Update existing add tests and write new failing tests**

In `tests/unit/commands/test_element_commands.py`, replace the entire `TestElementAddAction` class with:

```python
class TestElementAddAction:
    """Tests for ElementAddAction."""

    def test_add_action_creates_class_on_active_project(self) -> None:
        """Test: add action creates a class directly on the project root when no --path is given."""
        action = ElementAddAction()
        args = argparse.Namespace(type="class", name="Foo", bulk=None, path=None, verbose=False)

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = []

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            action.execute(args)

        fake_root.addClass.assert_called_once_with("Foo")

    def test_add_action_creates_class_in_nested_path(self) -> None:
        """Test: add action navigates a multi-level --path before creating the element."""
        action = ElementAddAction()
        args = argparse.Namespace(type="class", name="Foo", bulk=None, path="pkg/subpkg", verbose=False)

        fake_subpkg = MagicMock(name="FakeSubPkg")
        fake_subpkg.getName.return_value = "subpkg"
        fake_subpkg.getNestedElements.return_value = []

        fake_pkg = MagicMock(name="FakePkg")
        fake_pkg.getName.return_value = "pkg"
        fake_pkg.getNestedElements.return_value = [fake_subpkg]

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = [fake_pkg]

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            action.execute(args)

        fake_subpkg.addClass.assert_called_once_with("Foo")

    def test_add_action_reports_path_not_found(self) -> None:
        """Test: add action exits with an error when --path cannot be navigated."""
        action = ElementAddAction()
        args = argparse.Namespace(type="class", name="Foo", bulk=None, path="missing", verbose=False)

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = []

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            with pytest.raises(SystemExit) as exc_info:
                action.execute(args)
            assert exc_info.value.code == 1

    def test_add_action_requires_name_or_bulk(self) -> None:
        """Test: add action exits with an error when neither --name nor --bulk is given."""
        action = ElementAddAction()
        args = argparse.Namespace(type="class", name=None, bulk=None, path=None, verbose=False)

        with pytest.raises(SystemExit) as exc_info:
            action.execute(args)
        assert exc_info.value.code == 1

    def test_add_action_rejects_both_name_and_bulk(self) -> None:
        """Test: add action exits with an error when both --name and --bulk are given."""
        action = ElementAddAction()
        args = argparse.Namespace(type="class", name="Foo", bulk="items.txt", path=None, verbose=False)

        with pytest.raises(SystemExit) as exc_info:
            action.execute(args)
        assert exc_info.value.code == 1

    def test_add_action_bulk_creates_multiple_items(self, tmp_path: "Path") -> None:
        """Test: add action with --bulk creates every non-empty line as an element."""
        items_file = tmp_path / "items.txt"
        items_file.write_text("Class1\nClass2\n\nClass3\n")

        action = ElementAddAction()
        args = argparse.Namespace(type="class", name=None, bulk=str(items_file), path=None, verbose=False)

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = []

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            action.execute(args)

        assert fake_root.addClass.call_count == 3
        fake_root.addClass.assert_any_call("Class1")
        fake_root.addClass.assert_any_call("Class2")
        fake_root.addClass.assert_any_call("Class3")

    def test_add_action_bulk_reports_partial_failures(self, tmp_path: "Path") -> None:
        """Test: add action with --bulk continues past per-item failures and reports them."""
        items_file = tmp_path / "items.txt"
        items_file.write_text("Class1\nClass2\n")

        action = ElementAddAction()
        args = argparse.Namespace(type="class", name=None, bulk=str(items_file), path=None, verbose=False)

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = []
        fake_root.addClass.side_effect = [None, RuntimeError("duplicate name")]

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            action.execute(args)

        assert fake_root.addClass.call_count == 2

    def test_add_action_exits_on_connection_error(self) -> None:
        """Test: add action exits when no Rhapsody is running."""
        action = ElementAddAction()
        args = argparse.Namespace(type="class", name="Foo", bulk=None, path=None, verbose=False)

        with patch.object(
            RhapsodyContext,
            "get_active_project",
            side_effect=RhapsodyConnectionError("No running Rhapsody instance found"),
        ):
            with pytest.raises(SystemExit) as exc_info:
                action.execute(args)
            assert exc_info.value.code == 1
```

Also add `from pathlib import Path` to the `TYPE_CHECKING`-guarded imports at the top of the test file (used only for the `tmp_path: "Path"` annotation):

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path
```

Add this block directly under the existing `import pytest` line.

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/unit/commands/test_element_commands.py -k TestElementAddAction -v`
Expected: FAIL — `TypeError` or `AttributeError` (current `ElementAddAction` has no `--path`/`--bulk` handling; `args.bulk`/`args.path` don't exist in the old implementation's expectations, and the "Default package" auto-lookup logic no longer matches the new fake setups).

- [ ] **Step 3: Replace `ElementAddAction` implementation**

In `src/rhapsody_cli/actions/element_action.py`, add these imports near the top of the file (after the existing `from rhapsody_cli.models.core import call_com` line):

```python
from typing import Any, List, Optional, Tuple

from rhapsody_cli.cli.path_resolver import PathResolver, PathResolverError
```

Then replace the entire `ElementAddAction` class with:

```python
class ElementAddAction(ElementManagementAction):
    """Add element action - handles adding new elements to the project."""

    def __init__(self) -> None:
        """Initialize the 'add' action."""
        super().__init__(command_id="add")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'add' subcommand and its arguments."""
        add_parser = sub_parser.add_parser("add", help="Add a new element")
        add_parser.add_argument("--type", required=True, help="Element type (class, actor, package)")
        add_parser.add_argument("--name", default=None, help="Element name (required unless --bulk is used)")
        add_parser.add_argument("--bulk", default=None, help="Path to a file with one element name per line")
        add_parser.add_argument(
            "--path",
            default=None,
            help="Container path using '/' or '\\' separators (default: project root)",
        )
        self.add_verbose_argument(add_parser)

    def execute(self, args: argparse.Namespace) -> None:
        """Add one or more new elements to the project."""
        element_type = args.type
        name = args.name
        bulk_file = args.bulk
        path = args.path

        if not name and not bulk_file:
            print("Error: either --name or --bulk must be provided", file=sys.stderr)
            sys.exit(1)
        if name and bulk_file:
            print("Error: --name and --bulk cannot be used together", file=sys.stderr)
            sys.exit(1)

        try:
            project = self._get_active_project()
            root = project.getRoot()
            container = PathResolver.resolve_container(root, path)
        except SystemExit:
            raise
        except PathResolverError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            self._handle_execution_error(e, "Failed to resolve container path")
            sys.exit(1)

        if bulk_file:
            self._execute_bulk(element_type, bulk_file, container, path)
        else:
            self._execute_single(element_type, name, container, path)

    def _execute_single(self, element_type: str, name: str, container: Any, path: Optional[str]) -> None:
        """Create a single element under `container` and report the result."""
        try:
            self._create_element(element_type, name, container)
        except SystemExit:
            raise
        except Exception as e:
            self._handle_execution_error(e, f"Failed to create {element_type} '{name}'")
            sys.exit(1)

        full_path = f"{path}/{name}" if path else name
        self.logger.info("Created %s: %s", element_type, full_path)
        print(f"Created {element_type}: {full_path}")

    def _execute_bulk(self, element_type: str, bulk_file: str, container: Any, path: Optional[str]) -> None:
        """Create one element per non-empty line of `bulk_file` under `container`."""
        try:
            with open(bulk_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except OSError as e:
            print(f"Error: Could not read bulk file '{bulk_file}': {e}", file=sys.stderr)
            sys.exit(1)

        created: List[Tuple[str, str]] = []
        errors: List[Tuple[int, str, str]] = []
        for line_num, raw_line in enumerate(lines, start=1):
            item_name = raw_line.strip()
            if not item_name:
                continue
            try:
                self._create_element(element_type, item_name, container)
                full_path = f"{path}/{item_name}" if path else item_name
                created.append((item_name, full_path))
                self.logger.info("Created %s: %s", element_type, full_path)
            except Exception as e:
                errors.append((line_num, item_name, str(e)))

        total = len(created) + len(errors)
        if errors:
            print(f"Added {len(created)}/{total} items. Errors:")
            for line_num, item_name, reason in errors:
                print(f"  Line {line_num} ({item_name}): {reason}")
        else:
            print(f"Added {len(created)} items:" if created else "Added 0 items")
            for item_name, full_path in created:
                print(f"  \u2713 {item_name} created at {full_path}")

        if errors and not created:
            sys.exit(1)

    def _create_element(self, element_type: str, name: str, container: Any) -> None:
        """Dispatch element creation to the right container method by type."""
        element_type_lower = element_type.lower()
        if element_type_lower == "class":
            container.addClass(name)
        elif element_type_lower == "actor":
            container.addActor(name)
        elif element_type_lower == "package":
            if hasattr(container, "addPackage"):
                container.addPackage(name)
            else:
                container.addNestedPackage(name)
        else:
            raise ValueError(f"Unknown element type '{element_type}'")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/unit/commands/test_element_commands.py -k TestElementAddAction -v`
Expected: PASS (all 8 tests)

- [ ] **Step 5: Run mypy on the modified file**

Run: `mypy src/rhapsody_cli/actions/element_action.py`
Expected: `Success: no issues found`

- [ ] **Step 6: Commit**

```bash
git add src/rhapsody_cli/actions/element_action.py tests/unit/commands/test_element_commands.py
git commit -m "feat: support multi-level --path and --bulk in element add"
```

---

## Task 3: Enhance `ElementViewAction` with multi-level `--path`

**Files:**
- Modify: `src/rhapsody_cli/actions/element_action.py` (`ElementViewAction` class)
- Modify: `tests/unit/commands/test_element_commands.py` (`TestElementViewAction` class)

- [ ] **Step 1: Update existing view tests and write a new failing test**

Replace the entire `TestElementViewAction` class with:

```python
class TestElementViewAction:
    """Tests for ElementViewAction."""

    def test_view_action_displays_element_details(self) -> None:
        """Test: view action resolves the path and prints element details."""
        action = ElementViewAction()
        args = argparse.Namespace(path="pkg/MyClass", verbose=False)

        fake_class = MagicMock(name="FakeClass")
        fake_class.getName.return_value = "MyClass"
        fake_class.getMetaClass.return_value = "Class"

        fake_pkg = MagicMock(name="FakePkg")
        fake_pkg.getName.return_value = "pkg"
        fake_pkg.getNestedElements.return_value = [fake_class]

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = [fake_pkg]

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            action.execute(args)

    def test_view_action_reports_path_not_found(self) -> None:
        """Test: view action exits with an error when --path cannot be navigated."""
        action = ElementViewAction()
        args = argparse.Namespace(path="missing", verbose=False)

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = []

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            with pytest.raises(SystemExit) as exc_info:
                action.execute(args)
            assert exc_info.value.code == 1

    def test_view_action_exits_on_connection_error(self) -> None:
        """Test: view action exits when no Rhapsody is running."""
        action = ElementViewAction()
        args = argparse.Namespace(path="MyClass", verbose=False)

        with patch.object(
            RhapsodyContext,
            "get_active_project",
            side_effect=RhapsodyConnectionError("No running Rhapsody instance found"),
        ):
            with pytest.raises(SystemExit) as exc_info:
                action.execute(args)
            assert exc_info.value.code == 1
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/unit/commands/test_element_commands.py -k TestElementViewAction -v`
Expected: FAIL — `test_view_action_displays_element_details` and `test_view_action_reports_path_not_found`
fail because the current implementation never calls `PathResolver` and always reports `"type": "unknown"`.

- [ ] **Step 3: Replace `ElementViewAction` implementation**

Replace the entire `ElementViewAction` class with:

```python
class ElementViewAction(ElementManagementAction):
    """View element action - shows details for a single element."""

    def __init__(self) -> None:
        """Initialize the 'view' action."""
        super().__init__(command_id="view")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'view' subcommand and its arguments."""
        view_parser = sub_parser.add_parser("view", help="View element details")
        view_parser.add_argument(
            "--path",
            required=True,
            help="Element path using '/' or '\\' separators (e.g. pkg/subpkg/MyClass)",
        )
        self.add_verbose_argument(view_parser)

    def execute(self, args: argparse.Namespace) -> None:
        """View element details."""
        path = args.path
        try:
            project = self._get_active_project()
            root = project.getRoot()
            element = PathResolver.resolve_element(root, path)
        except SystemExit:
            raise
        except PathResolverError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            self._handle_execution_error(e, f"Failed to view element '{path}'")
            sys.exit(1)

        data = {
            "path": path,
            "name": element.getName(),
            "type": element.getMetaClass(),
        }

        from rhapsody_cli.cli.context import RhapsodyContext

        ctx = RhapsodyContext()

        if ctx.output_format == "json":
            output = OutputFormatter.json_format(data)
        else:
            rows = [["path", path], ["name", data["name"]], ["type", data["type"]]]
            output = OutputFormatter.table(["Property", "Value"], rows)

        print(output)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/unit/commands/test_element_commands.py -k TestElementViewAction -v`
Expected: PASS (all 3 tests)

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/actions/element_action.py tests/unit/commands/test_element_commands.py
git commit -m "feat: support multi-level --path in element view"
```

---

## Task 4: Enhance `ElementQueryAction` with `--path` and `--recursive`

**Files:**
- Modify: `src/rhapsody_cli/actions/element_action.py` (`ElementQueryAction` class)
- Modify: `tests/unit/commands/test_element_commands.py` (`TestElementQueryAction` class)

- [ ] **Step 1: Update existing query tests and write a new failing recursive test**

Replace the entire `TestElementQueryAction` class with:

```python
class TestElementQueryAction:
    """Tests for ElementQueryAction."""

    def test_query_action_lists_elements_from_active_project(self) -> None:
        """Test: query action lists elements from the active project's root."""
        action = ElementQueryAction()
        args = argparse.Namespace(pattern=None, path=None, recursive=False, verbose=False)

        fake_element = MagicMock(name="FakeElement")
        fake_element.getName.return_value = "MyClass"
        fake_element.getMetaClass.return_value = "Class"

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = [fake_element]

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            action.execute(args)

    def test_query_action_recursive_includes_nested_elements(self) -> None:
        """Test: query action with --recursive walks into nested packages."""
        action = ElementQueryAction()
        args = argparse.Namespace(pattern=None, path=None, recursive=True, verbose=False)

        fake_nested_class = MagicMock(name="FakeNestedClass")
        fake_nested_class.getName.return_value = "NestedClass"
        fake_nested_class.getMetaClass.return_value = "Class"
        fake_nested_class.getNestedElements.return_value = []

        fake_pkg = MagicMock(name="FakePkg")
        fake_pkg.getName.return_value = "pkg"
        fake_pkg.getMetaClass.return_value = "Package"
        fake_pkg.getNestedElements.return_value = [fake_nested_class]

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = [fake_pkg]

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            action.execute(args)

        fake_pkg.getNestedElements.assert_called()
        fake_nested_class.getNestedElements.assert_called()

    def test_query_action_reports_path_not_found(self) -> None:
        """Test: query action exits with an error when --path cannot be navigated."""
        action = ElementQueryAction()
        args = argparse.Namespace(pattern=None, path="missing", recursive=False, verbose=False)

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = []

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            with pytest.raises(SystemExit) as exc_info:
                action.execute(args)
            assert exc_info.value.code == 1

    def test_query_action_exits_on_connection_error(self) -> None:
        """Test: query action exits when no Rhapsody is running."""
        action = ElementQueryAction()
        args = argparse.Namespace(pattern=None, path=None, recursive=False, verbose=False)

        with patch.object(
            RhapsodyContext,
            "get_active_project",
            side_effect=RhapsodyConnectionError("No running Rhapsody instance found"),
        ):
            with pytest.raises(SystemExit) as exc_info:
                action.execute(args)
            assert exc_info.value.code == 1
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/unit/commands/test_element_commands.py -k TestElementQueryAction -v`
Expected: FAIL with `AttributeError: 'Namespace' object has no attribute 'path'` (current implementation and test namespaces don't have `path`/`recursive` yet).

- [ ] **Step 3: Replace `ElementQueryAction` implementation**

Replace the entire `ElementQueryAction` class with:

```python
class ElementQueryAction(ElementManagementAction):
    """Query element action - lists elements in the active project."""

    def __init__(self) -> None:
        """Initialize the 'query' action."""
        super().__init__(command_id="query")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'query' subcommand and its arguments."""
        query_parser = sub_parser.add_parser("query", help="Query elements in active project")
        query_parser.add_argument("pattern", nargs="?", default=None, help="Search pattern (optional)")
        query_parser.add_argument(
            "--path",
            default=None,
            help="Container path using '/' or '\\' separators (default: project root)",
        )
        query_parser.add_argument(
            "--recursive",
            action="store_true",
            help="Include elements nested at any depth below the container",
        )
        self.add_verbose_argument(query_parser)

    def execute(self, args: argparse.Namespace) -> None:
        """Query elements in active project."""
        path = args.path
        recursive = args.recursive

        try:
            project = self._get_active_project()
            root = project.getRoot()
            container = PathResolver.resolve_container(root, path)
        except SystemExit:
            raise
        except PathResolverError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            self._handle_execution_error(e, "Failed to query elements")
            sys.exit(1)

        base_path = path or ""
        results = self._collect_elements(container, base_path, recursive)

        from rhapsody_cli.cli.context import RhapsodyContext

        ctx = RhapsodyContext()

        if ctx.output_format == "json":
            data = {
                "elements": [
                    {"name": name, "type": meta_class, "path": elem_path}
                    for name, meta_class, elem_path in results
                ]
            }
            output = OutputFormatter.json_format(data)
        elif recursive:
            rows = [[name, meta_class, elem_path] for name, meta_class, elem_path in results]
            output = OutputFormatter.table(["Name", "Type", "Path"], rows)
        else:
            rows = [[name, meta_class] for name, meta_class, _ in results]
            output = OutputFormatter.table(["Name", "Type"], rows)

        print(output)

    def _collect_elements(self, container: Any, base_path: str, recursive: bool) -> List[Tuple[str, str, str]]:
        """Collect (name, meta_class, path) tuples for direct or recursive children."""
        results: List[Tuple[str, str, str]] = []
        for elem in container.getNestedElements():
            name = elem.getName()
            meta_class = elem.getMetaClass()
            elem_path = f"{base_path}/{name}" if base_path else name
            results.append((name, meta_class, elem_path))
            if recursive:
                results.extend(self._collect_elements(elem, elem_path, recursive))
        return results
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/unit/commands/test_element_commands.py -k TestElementQueryAction -v`
Expected: PASS (all 4 tests)

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/actions/element_action.py tests/unit/commands/test_element_commands.py
git commit -m "feat: support multi-level --path and --recursive in element query"
```

---

## Task 5: Enhance `ElementDeleteAction` with `--recursive` and `--force`

**Files:**
- Modify: `src/rhapsody_cli/actions/element_action.py` (`ElementDeleteAction` class)
- Modify: `tests/unit/commands/test_element_commands.py` (`TestElementDeleteAction` class)

- [ ] **Step 1: Update existing delete tests and write new failing tests**

Replace the entire `TestElementDeleteAction` class with:

```python
class TestElementDeleteAction:
    """Tests for ElementDeleteAction."""

    def test_delete_action_deletes_class_from_active_project(self) -> None:
        """Test: delete action removes a class from the active project's root."""
        action = ElementDeleteAction()
        args = argparse.Namespace(path="TestClass", recursive=False, force=False, verbose=False)

        fake_element_com = MagicMock(name="FakeElementCOM")
        fake_element_to_delete = MagicMock(name="FakeElement")
        fake_element_to_delete.getMetaClass.return_value = "Class"
        fake_element_to_delete.getName.return_value = "TestClass"
        fake_element_to_delete._com = fake_element_com

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = [fake_element_to_delete]

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            action.execute(args)

        fake_element_com.delete.assert_called_once()

    def test_delete_action_reports_path_not_found(self) -> None:
        """Test: delete action exits with an error when the path cannot be navigated."""
        action = ElementDeleteAction()
        args = argparse.Namespace(path="Missing", recursive=False, force=False, verbose=False)

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = []

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            with pytest.raises(SystemExit) as exc_info:
                action.execute(args)
            assert exc_info.value.code == 1

    def test_delete_action_recursive_prompts_and_deletes_with_confirmation(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test: delete action with --recursive counts nested elements and deletes after 'y' confirmation."""
        action = ElementDeleteAction()
        args = argparse.Namespace(path="pkg", recursive=True, force=False, verbose=False)

        fake_child = MagicMock(name="FakeChild")
        fake_child.getNestedElements.return_value = []

        fake_pkg_com = MagicMock(name="FakePkgCOM")
        fake_pkg = MagicMock(name="FakePkg")
        fake_pkg.getName.return_value = "pkg"
        fake_pkg.getMetaClass.return_value = "Package"
        fake_pkg.getNestedElements.return_value = [fake_child]
        fake_pkg._com = fake_pkg_com

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = [fake_pkg]

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        monkeypatch.setattr("builtins.input", lambda _: "y")

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            action.execute(args)

        fake_pkg_com.delete.assert_called_once()

    def test_delete_action_recursive_aborts_without_confirmation(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test: delete action with --recursive does not delete if the user declines to confirm."""
        action = ElementDeleteAction()
        args = argparse.Namespace(path="pkg", recursive=True, force=False, verbose=False)

        fake_pkg_com = MagicMock(name="FakePkgCOM")
        fake_pkg = MagicMock(name="FakePkg")
        fake_pkg.getName.return_value = "pkg"
        fake_pkg.getMetaClass.return_value = "Package"
        fake_pkg.getNestedElements.return_value = []
        fake_pkg._com = fake_pkg_com

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = [fake_pkg]

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        monkeypatch.setattr("builtins.input", lambda _: "n")

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            action.execute(args)

        fake_pkg_com.delete.assert_not_called()

    def test_delete_action_recursive_force_skips_confirmation(self) -> None:
        """Test: delete action with --recursive --force deletes without prompting."""
        action = ElementDeleteAction()
        args = argparse.Namespace(path="pkg", recursive=True, force=True, verbose=False)

        fake_pkg_com = MagicMock(name="FakePkgCOM")
        fake_pkg = MagicMock(name="FakePkg")
        fake_pkg.getName.return_value = "pkg"
        fake_pkg.getMetaClass.return_value = "Package"
        fake_pkg.getNestedElements.return_value = []
        fake_pkg._com = fake_pkg_com

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = [fake_pkg]

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            action.execute(args)

        fake_pkg_com.delete.assert_called_once()

    def test_delete_action_exits_on_connection_error(self) -> None:
        """Test: delete action exits when no Rhapsody is running."""
        action = ElementDeleteAction()
        args = argparse.Namespace(path="TestClass", recursive=False, force=False, verbose=False)

        with patch.object(
            RhapsodyContext,
            "get_active_project",
            side_effect=RhapsodyConnectionError("No running Rhapsody instance found"),
        ):
            with pytest.raises(SystemExit) as exc_info:
                action.execute(args)
            assert exc_info.value.code == 1
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/unit/commands/test_element_commands.py -k TestElementDeleteAction -v`
Expected: FAIL with `AttributeError: 'Namespace' object has no attribute 'recursive'` and related errors (current implementation uses `::`-based path parsing, not `PathResolver`, and has no recursive/force support).

- [ ] **Step 3: Replace `ElementDeleteAction` implementation**

Replace the entire `ElementDeleteAction` class with:

```python
class ElementDeleteAction(ElementManagementAction):
    """Delete element action - removes an element from the project."""

    def __init__(self) -> None:
        """Initialize the 'delete' action."""
        super().__init__(command_id="delete")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'delete' subcommand and its arguments."""
        delete_parser = sub_parser.add_parser("delete", help="Delete an element")
        delete_parser.add_argument("path", help="Element path using '/' or '\\' separators")
        delete_parser.add_argument(
            "--recursive",
            action="store_true",
            help="Delete the element and all elements nested within it",
        )
        delete_parser.add_argument(
            "--force",
            action="store_true",
            help="Skip the confirmation prompt when using --recursive",
        )
        self.add_verbose_argument(delete_parser)

    def execute(self, args: argparse.Namespace) -> None:
        """Delete an element from the project."""
        path = args.path
        recursive = args.recursive
        force = args.force

        try:
            project = self._get_active_project()
            root = project.getRoot()
            element = PathResolver.resolve_element(root, path)
        except SystemExit:
            raise
        except PathResolverError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            self._handle_execution_error(e, f"Failed to delete element at path '{path}'")
            sys.exit(1)

        nested_count = 0
        if recursive:
            nested_count = self._count_nested(element)
            if not force:
                answer = input(f"This will delete '{path}' and {nested_count} nested element(s). Continue? [y/N] ")
                if answer.strip().lower() not in ("y", "yes"):
                    print("Aborted.")
                    return

        try:
            call_com(lambda: element._com.delete())
        except Exception as e:
            self._handle_execution_error(e, f"Failed to delete element at path '{path}'")
            sys.exit(1)

        meta_class = element.getMetaClass()
        if recursive:
            self.logger.info("Deleted %s: %s (and %d nested elements)", meta_class, path, nested_count)
            print(f"Deleted {meta_class.lower()}: {path} and {nested_count} nested element(s)")
        else:
            self.logger.info("Deleted %s: %s", meta_class, path)
            print(f"Deleted {meta_class.lower()}: {path}")

    def _count_nested(self, element: Any) -> int:
        """Recursively count all elements nested within `element`."""
        count = 0
        for child in element.getNestedElements():
            count += 1
            count += self._count_nested(child)
        return count
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/unit/commands/test_element_commands.py -k TestElementDeleteAction -v`
Expected: PASS (all 6 tests)

- [ ] **Step 5: Run the full element command test module**

Run: `pytest tests/unit/commands/test_element_commands.py -v`
Expected: PASS (all tests across Add/View/Query/Delete)

- [ ] **Step 6: Commit**

```bash
git add src/rhapsody_cli/actions/element_action.py tests/unit/commands/test_element_commands.py
git commit -m "feat: support multi-level path, --recursive and --force in element delete"
```

---

## Task 6: Update Sphinx documentation

**Files:**
- Modify: `docs/user_guide/cli_tools.rst`
- Modify: `docs/user_guide/working_with_elements.rst`

- [ ] **Step 1: Update the Element Commands section in `docs/user_guide/cli_tools.rst`**

Find this section:

```rst
Element Commands
----------------

``element view`` - View Element Details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli element view <ELEMENT_ID>

Display detailed information about a specific element.

**Example:**

.. code-block:: bash

   rhapsody-cli element view MyClass
   rhapsody-cli --output json element view MyClass

``element query`` - Query Model Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli element query [FILTER]

Query and list elements from the active project.

**Example:**

.. code-block:: bash

   # List all elements
   rhapsody-cli element query

   # With filter (if supported)
   rhapsody-cli element query --type Class

   # JSON output
   rhapsody-cli --output json element query

``element add`` - Add New Element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli element add <ELEMENT_TYPE> [OPTIONS]

Create a new element in the active project.

**Example:**

.. code-block:: bash

   rhapsody-cli element add Class --name MyClass
   rhapsody-cli element add Package --name MyPackage
```

Replace it with:

```rst
Element Commands
----------------

Multi-Level Paths
~~~~~~~~~~~~~~~~~~

The ``--path`` option (on ``add`` and ``query``) and the ``path`` argument
(on ``view`` and ``delete``) accept "/" or "\\"-separated paths to navigate
nested packages, e.g. ``parent-pkg/pkg/child-pkg``. An optional leading
``Root`` segment is accepted and ignored. When ``--path`` is omitted on
``add`` or ``query``, the project root is used.

``element add`` - Add New Element(s)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli element add --type TYPE --name NAME [--path PATH]
   rhapsody-cli element add --type TYPE --bulk FILE [--path PATH]

Create one new element (``--name``) or many elements at once (``--bulk``)
in the active project. ``--path`` selects the destination container;
defaults to the project root.

**Examples:**

.. code-block:: bash

   # Single element at the root
   rhapsody-cli element add --type class --name MyClass

   # Single element in a nested package
   rhapsody-cli element add --type class --name MyClass --path parent-pkg/pkg

   # Bulk-create classes from a file
   rhapsody-cli element add --type class --bulk items.txt --path pkg

``items.txt`` contains one element name per line, blank lines are skipped::

   Class1
   Class2
   Class3

Output on success::

   Added 3 items:
     ✓ Class1 created at pkg/Class1
     ✓ Class2 created at pkg/Class2
     ✓ Class3 created at pkg/Class3

Output with per-item errors (creation continues past failures)::

   Added 2/3 items. Errors:
     Line 2 (Class2): duplicate name

``element view`` - View Element Details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli element view --path PATH

Display detailed information about a specific element addressed by a
multi-level path.

**Example:**

.. code-block:: bash

   rhapsody-cli element view --path pkg/subpkg/MyClass
   rhapsody-cli --output json element view --path pkg/subpkg/MyClass

``element query`` - Query Model Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli element query [PATTERN] [--path PATH] [--recursive]

Query and list elements directly under ``--path`` (default: project root).
Add ``--recursive`` to include elements nested at any depth; recursive
output includes each element's full path.

**Example:**

.. code-block:: bash

   # List direct children of the root
   rhapsody-cli element query

   # List direct children of a nested package
   rhapsody-cli element query --path pkg/subpkg

   # List the entire hierarchy under a package
   rhapsody-cli element query --path pkg --recursive

   # JSON output
   rhapsody-cli --output json element query --recursive

``element delete`` - Delete Element(s)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli element delete PATH [--recursive] [--force]

Delete the element addressed by ``PATH``. Add ``--recursive`` to also
delete every element nested within it; without ``--force`` this prompts
for confirmation showing how many nested elements will be removed.

**Example:**

.. code-block:: bash

   # Delete a single element
   rhapsody-cli element delete pkg/subpkg/MyClass

   # Delete a package and everything inside it (with confirmation prompt)
   rhapsody-cli element delete pkg/subpkg --recursive

   # Same, but skip the confirmation prompt
   rhapsody-cli element delete pkg/subpkg --recursive --force
```

- [ ] **Step 2: Update `docs/user_guide/working_with_elements.rst`**

Find the "Find Elements by Name" section:

```rst
Find Elements by Name
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Find nested package
   package = project.findNestedPackageByName("MyPackage")

   # Find class in package
   cls = package.findClassByName("MyClass")
```

Add a new subsection directly after it:

```rst
Find Elements by CLI Path
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``rhapsody-cli element`` commands accept "/" or "\\"-separated paths
to address elements nested arbitrarily deep, instead of requiring
Python calls like ``findNestedPackageByName``:

.. code-block:: bash

   # Equivalent to: project.findNestedPackageByName("pkg").findClassByName("MyClass")
   rhapsody-cli element view --path pkg/MyClass

   # Nested two levels deep
   rhapsody-cli element view --path parent-pkg/pkg/MyClass

A path segment is matched by ``getName()`` against each level's
``getNestedElements()``. An optional leading ``Root`` segment is
accepted and ignored.
```

- [ ] **Step 3: Verify Sphinx builds cleanly (if Sphinx is installed)**

Run: `python -c "import sphinx" 2>$null; if ($?) { sphinx-build -b html docs docs/_build/html -q } else { Write-Host 'sphinx not installed, skipping build check' }`
Expected: No errors, or the skip message if Sphinx isn't installed in this environment.

- [ ] **Step 4: Commit**

```bash
git add docs/user_guide/cli_tools.rst docs/user_guide/working_with_elements.rst
git commit -m "docs: document multi-level paths and bulk/recursive element operations"
```

---

## Task 7: Final quality gate

**Files:** None (verification only)

- [ ] **Step 1: Run ruff**

Run: `ruff check src/ tests/`
Expected: `All checks passed!`

If issues are reported, run `ruff check src/ tests/ --fix` and re-run.

- [ ] **Step 2: Run black in check mode**

Run: `black --check src/ tests/`
Expected: `All done!` with no files reformatted.

If files need formatting, run `black src/ tests/` and re-run the check.

- [ ] **Step 3: Run mypy**

Run: `mypy src/ tests/`
Expected: `Success: no issues found in N source files`

- [ ] **Step 4: Run the full test suite**

Run: `pytest -v`
Expected: All tests pass, including the full `tests/unit/commands/test_element_commands.py` and `tests/unit/cli/test_path_resolver.py` modules.

- [ ] **Step 5: Commit any final formatting fixes**

```bash
git add -A
git commit -m "chore: apply final lint/format fixes for element CLI enhancements"
```

(Skip this step if there is nothing to commit.)

---

## Success Criteria Checklist

- [ ] `PathResolver` normalizes `/` and `\` paths and navigates hierarchies with clear errors
- [ ] `element add` supports `--path` for nested containers and `--bulk FILE` for multi-item creation with partial-failure reporting
- [ ] `element view` supports multi-level `--path`
- [ ] `element query` supports `--path` and `--recursive` with full-path output
- [ ] `element delete` supports multi-level path, `--recursive`, and `--force` with a safety confirmation prompt
- [ ] All existing and new tests pass; `ruff`, `black --check`, and `mypy` are clean
- [ ] `docs/user_guide/cli_tools.rst` and `docs/user_guide/working_with_elements.rst` document the new flags and path syntax
