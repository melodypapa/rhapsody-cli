import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pytest

import scripts.validate_model_api as validator
from scripts.pywin32_authority import AuthorityData
from scripts.validate_model_api import (
    _resolve_generated_interface_source,
    build_arg_parser,
    build_deviation_rows,
    build_matched_rows,
    collect_generated_members,
    collect_java_members,
    collect_java_signatures,
    collect_python_members,
    main,
    promote_correct_com_bindings,
    render_markdown_report,
    render_report,
    resolve_python_wrapper,
)


def test_resolve_java_interface_docs_uses_declared_package(tmp_path: Path) -> None:
    docs_root = tmp_path / "java_api"
    package_docs = docs_root / "org" / "example" / "rhapsody"
    package_docs.mkdir(parents=True)
    (package_docs / "IRPThing.html").write_text("<html></html>", encoding="utf-8")

    java_package, resolved_docs = validator.resolve_java_interface_docs("IRPThing", docs_root)

    assert java_package == "org.example.rhapsody"
    assert resolved_docs == package_docs


def test_resolve_java_interface_docs_rejects_ambiguous_interface_names(tmp_path: Path) -> None:
    docs_root = tmp_path / "java_api"
    for package in ("org/example/one", "org/example/two"):
        package_docs = docs_root / Path(package)
        package_docs.mkdir(parents=True)
        (package_docs / "IRPThing.html").write_text("<html></html>", encoding="utf-8")

    with pytest.raises(ValueError, match="ambiguous"):
        validator.resolve_java_interface_docs("IRPThing", docs_root)


def test_collect_java_members_includes_superinterfaces(tmp_path: Path) -> None:
    docs_root = tmp_path / "docs"
    docs_root.mkdir()
    (docs_root / "IRPChild.html").write_text(
        '<DT><B>All Superinterfaces:</B><DD><A HREF="IRPBase.html">IRPBase</A></DD>'
        '<DT><B>All Known Subinterfaces:</B><DD><A HREF="IRPUnrelated.html">IRPUnrelated</A></DD>'
        "<!-- ============ METHOD DETAIL ========== -->"
        '<A NAME="childCall()"><!-- --></A><H3>childCall</H3>',
        encoding="utf-8",
    )
    (docs_root / "IRPBase.html").write_text(
        '<!-- ============ METHOD DETAIL ========== --><A NAME="baseCall()"><!-- --></A><H3>baseCall</H3>',
        encoding="utf-8",
    )
    (docs_root / "IRPUnrelated.html").write_text(
        '<!-- ============ METHOD DETAIL ========== --><A NAME="unrelatedCall()"><!-- --></A><H3>unrelatedCall</H3>',
        encoding="utf-8",
    )

    assert collect_java_members("IRPChild", docs_root) == {"childCall", "baseCall"}
    assert collect_java_signatures("IRPChild", docs_root) == {
        "childCall": {"IRPChild.childCall()"},
        "baseCall": {"IRPBase.baseCall()"},
    }


ACTIVE_ROW = (
    "is_active() -> isActive",
    "getIsActive (method); setIsActive (method)",
    "isActive (property)",
    "ALIAS_DOCUMENTED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
    "Documented decision: keep the current binding; no change.",
)


def test_promote_correct_com_bindings_moves_alias_only_row_to_matches() -> None:
    informational: List[Tuple[str, str, str, str, str]] = [
        (
            "description_html (property) -> descriptionHTML",
            "getDescriptionHTML (method)",
            "descriptionHTML (property)",
            "ALIAS_DOCUMENTED; ACCESSOR_ALIAS_MISMATCH",
            "Documented decision: keep the current binding; no change.",
        )
    ]

    remaining, promoted = promote_correct_com_bindings(informational)

    assert remaining == []
    assert promoted == [("description_html (property) -> descriptionHTML", "getDescriptionHTML (method)", "descriptionHTML (property)", "MATCH", "—")]


def test_promote_correct_com_bindings_does_not_promote_property_shape_mismatch() -> None:
    """A method-shaped Python member over a property-shaped COM member is a real deviation."""
    remaining, promoted = promote_correct_com_bindings([ACTIVE_ROW])

    assert promoted == []
    assert remaining == [ACTIVE_ROW]


def test_promote_correct_com_bindings_keeps_unsupported_and_unexposed_rows() -> None:
    unsupported = (
        "—",
        "updateContainedDiagramsOnServer (method)",
        "—",
        "UNAVAILABLE_DOCUMENTED",
        "Documented decision: intentionally unsupported; no change.",
    )
    unexposed = (
        "get_activity_diagram() -> getActivityDiagram",
        "getActivityDiagram (method)",
        "activityDiagram (property)",
        "ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
        "Use a property-aware fallback.",
    )

    remaining, promoted = promote_correct_com_bindings([unsupported, unexposed])

    assert promoted == []
    assert remaining == [unsupported, unexposed]


def test_collect_python_members_includes_bases_helpers_and_local_only_methods(tmp_path: Path) -> None:
    models_root = tmp_path / "models"
    models_root.mkdir()
    (models_root / "model_base.py").write_text(
        """class RPBase:
    def call_base(self):
        return self._com.baseCall()
""",
        encoding="utf-8",
    )
    (models_root / "model_child.py").write_text(
        """class RPChild(RPBase):
    def call_base(self):
        return self._com.childBaseCall()
    def call_child(self):
        return self._com.childCall()
    def get_is_open(self):
        return _get_method_or_property(self._com, 'getIsOpen', 'isOpen')
    def local_helper(self):
        return 'local'
""",
        encoding="utf-8",
    )

    members = collect_python_members("IRPChild", models_root)

    assert "baseCall" not in members
    assert "call_base() -> childBaseCall" in members["childBaseCall"]
    assert "call_child() -> childCall" in members["childCall"]
    assert "get_is_open() -> getIsOpen" in members["getIsOpen"]
    assert "get_is_open() -> isOpen" in members["isOpen"]
    assert "local_helper() (no static COM member)" in members["python-only:local_helper"]


def test_collect_python_members_own_only_excludes_bases(tmp_path: Path) -> None:
    models_root = tmp_path / "models"
    models_root.mkdir()
    (models_root / "model_base.py").write_text(
        """class RPBase:
    def call_base(self):
        return self._com.baseCall()
""",
        encoding="utf-8",
    )
    (models_root / "model_child.py").write_text(
        """class RPChild(RPBase):
    def call_child(self):
        return self._com.childCall()
""",
        encoding="utf-8",
    )

    assert "childCall" in collect_python_members("IRPChild", models_root, include_bases=False)
    assert "baseCall" not in collect_python_members("IRPChild", models_root, include_bases=False)
    assert "baseCall" in collect_python_members("IRPChild", models_root)


def test_collect_java_members_own_only_excludes_superinterfaces(tmp_path: Path) -> None:
    docs_root = tmp_path / "docs"
    docs_root.mkdir()
    (docs_root / "IRPBase.html").write_text('<A NAME="baseCall()"><!-- --></A><H3>baseCall</H3>', encoding="utf-8")
    (docs_root / "IRPChild.html").write_text(
        '<DT><B>All Superinterfaces:</B><DD><A HREF="IRPBase.html">IRPBase</A></DD><A NAME="childCall()"><!-- --></A><H3>childCall</H3>',
        encoding="utf-8",
    )

    assert collect_java_members("IRPChild", docs_root, include_superinterfaces=False) == {"childCall"}
    assert collect_java_members("IRPChild", docs_root) == {"childCall", "baseCall"}


def test_collect_python_members_records_com_property_helper_names(tmp_path: Path) -> None:
    models_root = tmp_path / "models"
    models_root.mkdir()
    (models_root / "model_props.py").write_text(
        """class RPProps:
    def is_abstract(self):
        return self.get_com_property(self._com, 'isAbstract')
    def set_is_active(self, value):
        self.set_com_property(self._com, 'isActive', value)
""",
        encoding="utf-8",
    )

    members = collect_python_members("IRPProps", models_root)

    assert "is_abstract() -> isAbstract" in members["isAbstract"]
    assert "set_is_active() -> isActive" in members["isActive"]


def test_collect_python_members_marks_com_property_accessors(tmp_path: Path) -> None:
    models_root = tmp_path / "models"
    models_root.mkdir()
    (models_root / "model_props.py").write_text(
        """class IRPProps:
    @property
    def display_name(self):
        return self.get_com_property(self._com, 'displayName')
    @display_name.setter
    def display_name(self, value):
        self.set_com_property(self._com, 'displayName', value)
""",
        encoding="utf-8",
    )

    members = collect_python_members("IRPProps", models_root)

    assert members["displayName"] == {"display_name (property) -> displayName"}


def test_stub_setter_shares_row_with_getter(tmp_path: Path) -> None:
    models_root = tmp_path / "models"
    models_root.mkdir()
    (models_root / "model_accessors.py").write_text(
        """class RPAccessors:
    def get_description_html(self):
        return _get_method_or_property(self._com, 'getDescriptionHTML', 'descriptionHTML')
    def set_description_html(self, description_html):
        \"\"\"Not implemented in the COM binding.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setDescriptionHTML(java.lang.String descriptionHTML)
        \"\"\"
        raise NotImplementedError
    def local_helper(self):
        return 'local'
""",
        encoding="utf-8",
    )

    members = collect_python_members("IRPAccessors", models_root)
    rows = build_deviation_rows(members, {"getDescriptionHTML", "setDescriptionHTML"}, {"descriptionHTML": "property"})

    assert "set_description_html() (no static COM member)" in members["setDescriptionHTML"]
    assert "python-only:set_description_html" not in members
    assert "local_helper() (no static COM member)" in members["python-only:local_helper"]
    accessor_rows = [row for row in rows if "set_description_html()" in row[0]]
    assert len(accessor_rows) == 1, rows
    assert "get_description_html() -> descriptionHTML" in accessor_rows[0][0]
    assert "set_description_html() (no static COM member)" in accessor_rows[0][0]
    assert "getDescriptionHTML (method); setDescriptionHTML (method)" == accessor_rows[0][1]


def test_collect_python_members_resolves_irp_application_canonically(tmp_path: Path) -> None:
    """IRPApplication resolves like every other interface: the canonical
    models package wrapper (the application.py facade special case is gone)."""
    models_root = tmp_path / "models"
    models_root.mkdir()
    (models_root / "irp_application.py").write_text(
        """class IRPApplication:
    def get_version(self):
        return self.call_com(lambda: self._com.version())
    def get_build_no(self):
        return self.get_com_property(self._com, "BuildNo")
""",
        encoding="utf-8",
    )

    members = collect_python_members("IRPApplication", models_root)

    assert "get_version() -> version" in members["version"]
    assert "get_build_no() -> BuildNo" in members["BuildNo"]


def test_resolve_python_wrapper_resolves_irp_application_canonically(tmp_path: Path) -> None:
    models_root = tmp_path / "models"
    models_root.mkdir()
    canonical_source = models_root / "irp_application.py"
    canonical_source.write_text("class IRPApplication: pass", encoding="utf-8")

    wrapper_name, wrapper_source = resolve_python_wrapper("IRPApplication", models_root)

    assert wrapper_name == "IRPApplication"
    assert wrapper_source == canonical_source


def test_collect_generated_members_lists_methods_and_properties(tmp_path: Path) -> None:
    generated_source = tmp_path / "IRPExample.py"
    generated_source.write_text(
        """class IRPExample:
    def getFoo(self):
        return None
    _prop_map_get_ = {"Bar": (1,)}
    _prop_map_put_ = {"Bar": (2,)}
""",
        encoding="utf-8",
    )

    assert collect_generated_members(generated_source, "IRPExample") == {"getFoo": "method", "Bar": "property"}


def test_resolve_generated_interface_source_handles_package_and_monolithic_layouts(tmp_path: Path) -> None:
    package_dir = tmp_path / "generated_package"
    package_dir.mkdir()
    package_init = package_dir / "__init__.py"
    interface_source = package_dir / "IRPClass.py"
    package_init.write_text("", encoding="utf-8")
    interface_source.write_text("class IRPClass: pass", encoding="utf-8")
    coclass_module = package_dir / "RPApplication.py"
    coclass_module.write_text("class RPApplication: pass", encoding="utf-8")

    monolithic_source = tmp_path / "typelib.py"
    monolithic_source.write_text("class IRPClass: pass", encoding="utf-8")

    assert _resolve_generated_interface_source(package_init, "IRPClass") == interface_source
    assert _resolve_generated_interface_source(coclass_module, "IRPClass") == interface_source
    assert _resolve_generated_interface_source(monolithic_source, "IRPClass") == monolithic_source


def test_build_matched_rows_lists_complete_matches() -> None:
    rows = build_matched_rows(
        {"addClass": {"add_class() -> addClass"}},
        {"addClass"},
        {"addClass": "method"},
    )

    assert rows == [("add_class() -> addClass", "addClass (method)", "addClass (method)", "MATCH", "—")]


def test_build_matched_rows_excludes_deviations() -> None:
    rows = build_matched_rows(
        {"getBuildNo": {"get_build_no() -> getBuildNo"}},
        {"getBuildNo"},
        {"BuildNo": "property"},
    )

    assert rows == []


def test_build_deviation_rows_omits_only_complete_matches() -> None:
    python_members = {"sameCall": {"same_call() -> sameCall"}, "python-only:local": {"local() (no static COM member)"}}
    java_members = {"sameCall", "javaOnly"}
    pywin32_members = {"sameCall": "method", "pywinOnly": "property"}

    rows = build_deviation_rows(python_members, java_members, pywin32_members)

    assert rows == [
        (
            "—",
            "javaOnly (method)",
            "—",
            "JAVA_ONLY_MEMBER",
            "Verify the Java documentation against the installed COM type library.",
        ),
        (
            "local() (no static COM member)",
            "—",
            "—",
            "PYTHON_ONLY_MEMBER",
            "Keep this as a local facade helper or map it to a documented API member.",
        ),
        (
            "—",
            "—",
            "pywinOnly (property)",
            "PYWIN32_ONLY_MEMBER",
            "Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.",
        ),
    ]
    report = render_report(rows)
    header = report.splitlines()[0]
    assert "Python model wrapper" in header
    assert "Java API" in header
    assert "pywin32" in header


def test_build_deviation_rows_reports_python_method_name_mismatch() -> None:
    rows = build_deviation_rows(
        {"sameCall": {"wrong_wrapper() -> sameCall"}},
        {"sameCall"},
        {"sameCall": "method"},
    )

    assert rows == [
        (
            "wrong_wrapper() -> sameCall",
            "sameCall (method)",
            "sameCall (method)",
            "PYTHON_METHOD_NAME_MISMATCH",
            "Rename the Python method to the snake_case Java API name or document the alias.",
        )
    ]


def test_build_deviation_rows_prefers_com_exposed_member_over_java_probe_name() -> None:
    rows = build_deviation_rows(
        {
            "getMainDiagram": {"get_main_diagram() -> getMainDiagram"},
            "mainDiagram": {"get_main_diagram() -> mainDiagram", "set_main_diagram() -> mainDiagram"},
            "setMainDiagram": {"set_main_diagram() -> setMainDiagram"},
        },
        {"getMainDiagram", "setMainDiagram"},
        {"mainDiagram": "property"},
    )

    assert len(rows) == 1, rows
    python_cell = rows[0][0]
    assert "get_main_diagram() -> mainDiagram" in python_cell
    assert "set_main_diagram() -> mainDiagram" in python_cell
    assert "getMainDiagram" not in python_cell
    assert "setMainDiagram" not in python_cell


def test_build_deviation_rows_reports_build_no_method_property_deviation() -> None:
    rows = build_deviation_rows(
        {"getBuildNo": {"get_build_no() -> getBuildNo"}},
        {"getBuildNo"},
        {"BuildNo": "property"},
    )

    assert rows == [
        (
            "get_build_no() -> getBuildNo",
            "getBuildNo (method)",
            "BuildNo (property)",
            "COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
            "Use the BuildNo property or a getter/setter fallback instead of calling getBuildNo directly.",
        )
    ]


def test_build_deviation_rows_groups_python_java_getter_and_setter_aliases() -> None:
    rows = build_deviation_rows(
        {
            "getBuildNo": {"get_build_no() -> getBuildNo"},
            "setBuildNo": {"set_build_no() -> setBuildNo"},
        },
        {"getBuildNo", "setBuildNo"},
        {"BuildNo": "property"},
    )

    assert rows == [
        (
            "get_build_no() -> getBuildNo; set_build_no() -> setBuildNo",
            "getBuildNo (method); setBuildNo (method)",
            "BuildNo (property)",
            "COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
            "Use the BuildNo property or a getter/setter fallback instead of calling getBuildNo and setBuildNo directly.",
        )
    ]


def test_build_deviation_rows_accepts_python_property_for_java_accessors() -> None:
    python_members = {"name": {"name (property) -> name"}}
    java_members = {"getName", "setName"}
    pywin32_members = {"name": "property"}

    assert build_deviation_rows(python_members, java_members, pywin32_members) == []
    assert build_matched_rows(python_members, java_members, pywin32_members) == [
        (
            "name (property) -> name",
            "getName (method); setName (method)",
            "name (property)",
            "MATCH",
            "—",
        )
    ]


def test_irp_model_element_com_property_families_are_classified_as_matches() -> None:
    project_root = Path(__file__).resolve().parents[2]
    models_root = project_root / "src" / "rhapsody_cli" / "models"
    authority_path = project_root / "docs" / "reports" / "pywin32_authority.json"
    authority = json.loads(authority_path.read_text(encoding="utf-8"))

    python_members = collect_python_members("IRPModelElement", models_root)
    pywin32_members = authority["catalog"]["IRPModelElement"]
    # The generated Javadocs are not included in CI checkouts. Derive a getter
    # name for each catalog property to exercise all real wrapper/property
    # families without making this unit test depend on that optional directory.
    java_members = {f"get{name[0].upper()}{name[1:]}" for name, kind in pywin32_members.items() if kind == "property"}

    rows = build_deviation_rows(python_members, java_members, pywin32_members)
    property_deviations = [
        row for row in rows if "(property)" in row[2] and set(row[3].split("; ")) & {"PYTHON_METHOD_NAME_MISMATCH", "COM_MEMBER_NOT_EXPOSED", "ACCESSOR_ALIAS_MISMATCH", "METHOD_PROPERTY_MISMATCH"}
    ]

    assert property_deviations == []


def test_build_deviation_rows_reports_java_method_vs_pywin32_property() -> None:
    rows = build_deviation_rows(
        {"version": {"get_version() -> version"}},
        {"version"},
        {"version": "property"},
    )

    assert rows == [
        (
            "get_version() -> version",
            "version (method)",
            "version (property)",
            "PYTHON_METHOD_NAME_MISMATCH; METHOD_PROPERTY_MISMATCH",
            "Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.",
        )
    ]


def test_markdown_report_includes_status_and_recommendation_for_build_no() -> None:
    rows = build_deviation_rows(
        {"getBuildNo": {"get_build_no() -> getBuildNo"}},
        {"getBuildNo"},
        {"BuildNo": "property"},
    )

    report = render_markdown_report(
        "IRPApplication",
        rows,
        "RhapsodyApplication",
        "src/rhapsody_cli/application.py",
        {"getBuildNo": {"IRPApplication.getBuildNo()"}},
        (1, 1, 1),
    )

    assert report.startswith("# Rhapsody API Validation: IRPApplication")
    assert report.index("## Summary") < report.index("| Python model wrapper")
    assert "| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |" in report
    assert "Target wrapper: `RhapsodyApplication` (`src/rhapsody_cli/application.py`)" in report
    assert "### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)" in report
    assert "**Affected call(s):** get_build_no() -> getBuildNo" in report
    assert "**Java signature(s):** `IRPApplication.getBuildNo()`" in report
    assert "Use the BuildNo property or a getter/setter fallback instead of calling getBuildNo directly." in report
    assert "## AI Fix Guidance" in report


def test_markdown_report_includes_java_package() -> None:
    report = render_markdown_report(
        "IRPClass",
        [],
        "IRPClass",
        "src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_class.py",
        {},
        (0, 0, 0),
    )

    assert "- Java package: `com.telelogic.rhapsody.core`" in report


def test_markdown_report_counts_deviation_items_across_all_tables() -> None:
    """Deviations count items, not kinds: actionable rows, expected binding
    differences, and wrapper backlog members all add to the total."""
    report = render_markdown_report(
        "IRPClass",
        [("—", "save (method)", "save (method)", "MISSING_PYTHON_WRAPPER", "Implement the Python wrapper.")],
        "IRPClass",
        "src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_class.py",
        {},
        (214, 222, 201),
        authoritative=True,
        informational_rows=[("get_build_no() -> getBuildNo", "getBuildNo (method)", "BuildNo (property)", "COM_MEMBER_NOT_EXPOSED", "Document.")],
        backlog_rows=[("—", "moveToDesignManager (method)", "moveToDesignManager (method)", "MISSING_PYTHON_WRAPPER", "Implement the Python wrapper.")],
    )

    assert "- Deviation items: `3` (actionable `1`, expected binding differences `1`, wrapper backlog `1`)" in report


def test_main_writes_markdown_report_to_default_and_requested_directories(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.chdir(tmp_path)
    java_package = "org.example.rhapsody"
    package_docs = tmp_path / "java_api" / Path(*java_package.split("."))
    monkeypatch.setattr(validator, "resolve_java_interface_docs", lambda interface_name, docs_root: (java_package, package_docs))
    monkeypatch.setattr(validator, "resolve_python_wrapper", lambda interface_name, models_root: ("RhapsodyApplication", models_root.parent / "application.py"))
    monkeypatch.setattr(validator, "collect_java_signatures", lambda interface_name, docs_root, **kwargs: {"version": {"IRPApplication.version()"}})
    monkeypatch.setattr(validator, "collect_java_members", lambda interface_name, docs_root, **kwargs: {"version"})
    monkeypatch.setattr(validator, "collect_python_members", lambda interface_name, models_root, **kwargs: {"version": {"version() -> version"}})
    monkeypatch.setattr(validator, "collect_registered_pywin32_members", lambda interface_name: {"version": "method"})

    assert main(["IRPApplication"]) == 0
    package_path = Path(*java_package.split("."))
    default_report = tmp_path / package_path / "IRPApplication_api_report.md"
    assert default_report.is_file()
    default_text = default_report.read_text(encoding="utf-8")
    assert "# Rhapsody API Validation: IRPApplication" in default_text
    assert f"- Java package: `{java_package}`" in default_text

    custom_directory = tmp_path / "reports"
    assert main(["IRPApplication", "--path", str(custom_directory)]) == 0
    custom_report = custom_directory / package_path / "IRPApplication_api_report.md"
    assert custom_report.is_file()
    assert capsys.readouterr().out == ""


def test_argument_parser_requires_one_interface_and_optional_report_directory() -> None:
    parser = build_arg_parser()
    default_args = parser.parse_args(["IRPClass"])
    assert default_args.java_interface == "IRPClass"
    assert default_args.path is None
    assert default_args.source == "typelib"
    args = parser.parse_args(["IRPApplication", "--path", "out"])
    assert args.java_interface == "IRPApplication"
    assert args.path == Path("out")
    with pytest.raises(SystemExit):
        parser.parse_args([])
    with pytest.raises(SystemExit):
        parser.parse_args(["IRPClass", "IRPActor"])


def _authority(
    catalog: Optional[Dict[str, Dict[str, str]]] = None,
    aliases: Optional[Dict[str, Dict[str, str]]] = None,
    unavailable: Optional[Dict[str, List[str]]] = None,
    signatures: Optional[Dict[str, Dict[str, Dict[str, object]]]] = None,
) -> AuthorityData:
    """Build an AuthorityData carrying only the documented-decision maps under test."""
    return AuthorityData(
        catalog=catalog or {},
        documented_aliases=aliases or {},
        documented_unavailable=unavailable or {},
        signatures=signatures or {},
    )


def test_apply_pywin32_authority_keeps_property_shape_mismatch_as_deviation() -> None:
    rows = [
        (
            "get_activity_diagram() -> activityDiagram; get_activity_diagram() -> getActivityDiagram",
            "getActivityDiagram (method)",
            "activityDiagram (property)",
            "ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
            "Use a property-aware getter/setter fallback.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(rows, "IRPClass", _authority())

    assert deviations == [
        (
            "get_activity_diagram() -> activityDiagram; get_activity_diagram() -> getActivityDiagram",
            "getActivityDiagram (method)",
            "activityDiagram (property)",
            "METHOD_PROPERTY_MISMATCH",
            "Use a property-aware getter/setter fallback.",
        )
    ]
    assert informational == []
    assert backlog == []


def test_apply_pywin32_authority_marks_documented_alias_in_row() -> None:
    rows = [
        (
            "get_description_html() -> descriptionHTML; get_description_html() -> getDescriptionHTML",
            "getDescriptionHTML (method)",
            "descriptionHTML (property)",
            "PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
            "Rename the Python method.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(rows, "IRPClass", _authority(aliases={"IRPClass": {"get_description_html": "description_html"}}))

    assert deviations == [
        (
            "get_description_html() -> descriptionHTML; get_description_html() -> getDescriptionHTML",
            "getDescriptionHTML (method)",
            "descriptionHTML (property)",
            "ALIAS_DOCUMENTED; METHOD_PROPERTY_MISMATCH",
            "Rename the Python method.",
        )
    ]
    assert backlog == []
    assert informational == []


def test_apply_pywin32_authority_marks_documented_unavailable_member() -> None:
    rows = [
        (
            "get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl",
            "getRmmUrl (method)",
            "—",
            "PYWIN32_MEMBER_MISSING",
            "Use a member exposed by the registered type library.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(rows, "IRPClass", _authority(unavailable={"IRPClass": ["getRmmUrl"]}))

    assert deviations == []
    assert backlog == []
    assert informational == [
        (
            "get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl",
            "getRmmUrl (method)",
            "—",
            "UNAVAILABLE_DOCUMENTED",
            "Documented decision: intentionally unsupported; no change.",
        )
    ]


def test_apply_pywin32_authority_marks_partial_accessor_unavailable() -> None:
    rows = [
        (
            "get_unit_path() (no static COM member); set_unit_path() -> setUnitPath",
            "getUnitPath (method); setUnitPath (method)",
            "setUnitPath (method)",
            "ACCESSOR_ALIAS_MISMATCH",
            "Review the related API spellings.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(rows, "IRPUnit", _authority(unavailable={"IRPUnit": ["getUnitPath"]}))

    assert deviations == []
    assert backlog == []
    assert informational == [
        (
            "get_unit_path() (no static COM member); set_unit_path() -> setUnitPath",
            "getUnitPath (method); setUnitPath (method)",
            "setUnitPath (method)",
            "UNAVAILABLE_DOCUMENTED",
            "Documented decision: intentionally unsupported; no change.",
        )
    ]


def test_apply_pywin32_authority_marks_documented_unavailable_java_only_member() -> None:
    rows = [
        (
            "—",
            "addEventReceptionWithEvent (method)",
            "—",
            "JAVA_ONLY_MEMBER",
            "Verify the Java documentation against the installed COM type library.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(rows, "IRPClass", _authority(unavailable={"IRPClass": ["addEventReceptionWithEvent"]}))

    assert deviations == []
    assert backlog == []
    assert informational == [
        (
            "—",
            "addEventReceptionWithEvent (method)",
            "—",
            "UNAVAILABLE_DOCUMENTED",
            "Documented decision: intentionally unsupported; no change.",
        )
    ]


def test_apply_pywin32_authority_moves_documented_unavailable_backlog_to_informational() -> None:
    rows = [
        (
            "—",
            "createOSLCLink (method)",
            "createOSLCLink (method)",
            "MISSING_PYTHON_WRAPPER",
            "Implement the Python wrapper or mark this API member intentionally unsupported.",
        ),
        (
            "—",
            "deleteStatechart (method)",
            "deleteStatechart (method)",
            "MISSING_PYTHON_WRAPPER",
            "Implement the Python wrapper or mark this API member intentionally unsupported.",
        ),
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(rows, "IRPClass", _authority(unavailable={"IRPClass": ["createOSLCLink"]}))

    assert deviations == []
    assert informational == [
        (
            "—",
            "createOSLCLink (method)",
            "createOSLCLink (method)",
            "UNAVAILABLE_DOCUMENTED",
            "Documented decision: intentionally unsupported; no change.",
        )
    ]
    assert backlog == [rows[1]]


def test_apply_pywin32_authority_keeps_actionable_deviation_alongside_documented_alias() -> None:
    rows = [
        (
            "get_binary_id() -> binaryID; get_binary_id() -> getBinaryID",
            "getBinaryID (method)",
            "BinaryID (property)",
            "COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
            "Use the BinaryID property.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(rows, "IRPClass", _authority(aliases={"IRPClass": {"get_binary_id": "binary_id"}}))

    assert deviations == [
        (
            "get_binary_id() -> binaryID; get_binary_id() -> getBinaryID",
            "getBinaryID (method)",
            "BinaryID (property)",
            "COM_MEMBER_NOT_EXPOSED; METHOD_PROPERTY_MISMATCH",
            "Use the BinaryID property.",
        )
    ]
    assert informational == []
    assert backlog == []


def test_apply_pywin32_authority_keeps_unexposed_member_as_deviation() -> None:
    rows = [
        (
            "get_binary_id() -> binaryID; get_binary_id() -> getBinaryID",
            "getBinaryID (method)",
            "BinaryID (property)",
            "COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
            "Use the BinaryID property.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(rows, "IRPClass", _authority())

    assert deviations == [
        (
            "get_binary_id() -> binaryID; get_binary_id() -> getBinaryID",
            "getBinaryID (method)",
            "BinaryID (property)",
            "COM_MEMBER_NOT_EXPOSED; METHOD_PROPERTY_MISMATCH",
            "Use the BinaryID property.",
        )
    ]
    assert informational == []
    assert backlog == []


def test_main_authority_source_reports_backlog_without_typelib(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(validator, "load_authority", lambda: _authority(catalog={"IRPClass": {"isAbstract": "property"}}))
    monkeypatch.setattr(validator, "resolve_java_interface_docs", lambda interface_name, docs_root: ("com.telelogic.rhapsody.core", docs_root))
    monkeypatch.setattr(validator, "collect_java_signatures", lambda interface_name, docs_root, **kwargs: {"isAbstract": {"IRPClass.isAbstract()"}})
    monkeypatch.setattr(validator, "collect_java_members", lambda interface_name, docs_root, **kwargs: {"isAbstract"})
    monkeypatch.setattr(validator, "collect_python_members", lambda interface_name, models_root, **kwargs: {"isAbstract": {"is_abstract (property) -> isAbstract"}})

    assert validator.main(["IRPClass", "--source", "authority"]) == 0

    report = (tmp_path / Path(*validator.JAVA_PACKAGE.split(".")) / "IRPClass_api_report.md").read_text(encoding="utf-8")
    assert "## Expected Binding Differences" in report
    assert "## Wrapper Backlog" in report
    assert "No deviations require changes." in report


def test_main_authority_source_fails_on_property_shape_mismatch(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A plain Python method over a property-shaped COM member is actionable, never MATCH."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(validator, "load_authority", lambda: _authority(catalog={"IRPClass": {"isAbstract": "property"}}))
    monkeypatch.setattr(validator, "resolve_java_interface_docs", lambda interface_name, docs_root: ("com.telelogic.rhapsody.core", docs_root))
    monkeypatch.setattr(validator, "collect_java_signatures", lambda interface_name, docs_root, **kwargs: {"isAbstract": {"IRPClass.isAbstract()"}})
    monkeypatch.setattr(validator, "collect_java_members", lambda interface_name, docs_root, **kwargs: {"isAbstract"})
    monkeypatch.setattr(validator, "collect_python_members", lambda interface_name, models_root, **kwargs: {"isAbstract": {"is_abstract() -> isAbstract"}})

    assert validator.main(["IRPClass", "--source", "authority"]) == 1

    report = (tmp_path / Path(*validator.JAVA_PACKAGE.split(".")) / "IRPClass_api_report.md").read_text(encoding="utf-8")
    assert "METHOD_PROPERTY_MISMATCH" in report.split("## Expected Binding Differences", 1)[0]


def test_irpclass_report_has_no_actionable_deviations() -> None:
    reports_root = Path(__file__).resolve().parents[2] / "docs" / "reports"
    text = (reports_root / Path(*validator.JAVA_PACKAGE.split(".")) / "IRPClass_api_report.md").read_text(encoding="utf-8")
    section = text.split("## Comparison details", 1)[1].split("## Expected Binding Differences", 1)[0]
    rows = [line for line in section.splitlines() if line.startswith("| ") and "Python model wrapper" not in line and "---" not in line]
    assert rows == [], rows


def test_signature_findings_are_actionable_deviations(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Signature findings flow through the deviation bucketing: they count in
    the Summary, land in Comparison details, and fail the run (exit 1) —
    they are never parked in a side section that nothing enforces."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        validator,
        "load_authority",
        lambda: _authority(
            catalog={"IRPExample": {"FindThing": "method"}},
            signatures={"IRPExample": {"FindThing": {"count": 2, "names": ["a", "b"], "types": ["str", "str"], "codes": [8, 8]}}},
        ),
    )
    monkeypatch.setattr(validator, "resolve_java_interface_docs", lambda interface_name, docs_root: ("com.telelogic.rhapsody.core", docs_root))
    monkeypatch.setattr(validator, "collect_java_signatures", lambda interface_name, docs_root, **kwargs: {"FindThing": {"IRPExample.FindThing(a, b)"}})
    monkeypatch.setattr(validator, "collect_java_members", lambda interface_name, docs_root, **kwargs: {"FindThing"})
    monkeypatch.setattr(validator, "collect_python_members", lambda interface_name, models_root, **kwargs: {"FindThing": {"find_thing() -> FindThing"}})
    monkeypatch.setattr(validator, "collect_wrapper_call_arities", lambda interface_name, models_root: {"FindThing": [1]})
    monkeypatch.setattr(validator, "collect_wrapper_arg_types", lambda interface_name, models_root: {})
    real_wrapper = Path(validator.__file__).resolve().parents[1] / "src" / "rhapsody_cli" / "application.py"
    monkeypatch.setattr(validator, "resolve_python_wrapper", lambda interface_name, models_root: ("IRPExample", real_wrapper))

    assert validator.main(["IRPExample", "--source", "authority"]) == 1

    report = (tmp_path / Path(*validator.JAVA_PACKAGE.split(".")) / "IRPExample_api_report.md").read_text(encoding="utf-8")
    assert "SIGNATURE_ARITY_MISMATCH" in report.split("## Expected Binding Differences", 1)[0]
    assert "## Signature Validation" not in report
    assert "(actionable `1`" in report


def test_build_signature_rows_skips_members_without_declared_count() -> None:
    """A malformed signature entry is insufficient evidence — skip the member,
    never fall back to expecting zero parameters."""
    rows = validator.build_signature_rows({"FindThing": {"find_thing() -> FindThing"}}, {"FindThing": {"names": ["a"], "types": ["str"]}}, {"FindThing": [1]}, {})

    assert rows == []


def test_build_signature_rows_treats_numeric_variants_as_coercible() -> None:
    """COM automation converts between numeric/bool variants at the boundary;
    only a real vocabulary difference (e.g. str vs numeric) is a mismatch."""
    signatures = {"SetThing": {"count": 1, "names": ["v"], "types": ["int"], "codes": [3]}}
    arities = {"SetThing": [1]}
    python_members = {"SetThing": {"set_thing() -> SetThing"}}

    assert validator.build_signature_rows(python_members, signatures, arities, {"SetThing": ["bool"]}) == []
    assert validator.build_signature_rows(python_members, signatures, arities, {"SetThing": ["float"]}) == []
    rows = validator.build_signature_rows(python_members, signatures, arities, {"SetThing": ["str"]})
    assert any("SIGNATURE_TYPE_MISMATCH" in row[3] for row in rows)


def test_build_signature_rows_accepts_arg_counts_within_optional_defaults() -> None:
    """makepy declares COM optional parameters with Python defaults: any count
    from `required` up to `count` is a legal call."""
    signatures = {"DoThing": {"count": 3, "required": 1, "names": ["a", "b", "c"], "types": ["str", "int", "int"], "codes": [8, 3, 3]}}
    python_members = {"DoThing": {"do_thing() -> DoThing"}}

    assert validator.build_signature_rows(python_members, signatures, {"DoThing": [1]}, {}) == []
    assert validator.build_signature_rows(python_members, signatures, {"DoThing": [3]}, {}) == []
    rows = validator.build_signature_rows(python_members, signatures, {"DoThing": [4]}, {})
    assert any("SIGNATURE_ARITY_MISMATCH" in row[3] for row in rows)


def test_build_signature_rows_keeps_pywin32_cell_parseable() -> None:
    """The pywin32 cell stays `name (method)` so the report-based catalog
    export keeps parsing signature rows like every other table row."""
    signatures = {"FindThing": {"count": 2, "names": ["a", "b"], "types": ["str", "str"], "codes": [8, 8]}}
    rows = validator.build_signature_rows({"FindThing": {"find_thing() -> FindThing"}}, signatures, {"FindThing": [1]}, {})

    assert rows and rows[0][2] == "FindThing (method)"
    assert "; " not in rows[0][2]


def test_collect_wrapper_arg_types_maps_float_annotations(tmp_path: Path) -> None:
    source = tmp_path / "model_thing.py"
    source.write_text(
        "class IRPThing:\n    def set_scale(self, v: float):\n        return self.call_com(lambda: self._com.SetScale(v))\n",
        encoding="utf-8",
    )

    assert validator.collect_wrapper_arg_types("IRPThing", tmp_path) == {"SetScale": ["float"]}


def test_collect_generated_signatures_counts_required_parameters(tmp_path: Path) -> None:
    """`count` is every declared parameter; `required` excludes trailing
    parameters that makepy gives Python defaults for."""
    source = tmp_path / "generated.py"
    source.write_text(
        "class IRPThing:\n"
        "    def DoThing(self, a, b, c=None):\n"
        "        return self._oleobj_.InvokeTypes(101, 0, 2, ((8, 0, 2, 'IN'),), ((8, 1, 0, 'IN'), (3, 1, 0, 'IN'), (3, 1, 0, 'IN')), a, b, c)\n",
        encoding="utf-8",
    )

    signatures = validator.collect_generated_signatures(source, "IRPThing")

    assert signatures["DoThing"]["count"] == 3
    assert signatures["DoThing"]["required"] == 2
    assert signatures["DoThing"]["types"] == ["str", "int", "int"]
