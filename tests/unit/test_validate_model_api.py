from pathlib import Path
from typing import Dict, List, Optional

import pytest

import scripts.validate_model_api as validator
from scripts.pywin32_authority import AuthorityData
from scripts.validate_model_api import (
    _resolve_generated_interface_source,
    build_arg_parser,
    build_deviation_rows,
    collect_generated_members,
    collect_java_members,
    collect_java_signatures,
    collect_python_members,
    main,
    render_markdown_report,
    render_report,
    resolve_python_wrapper,
)


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


def test_collect_python_members_maps_application_interface_to_application_facade(tmp_path: Path) -> None:
    models_root = tmp_path / "models"
    models_root.mkdir()
    (tmp_path / "application.py").write_text(
        """class RhapsodyApplication:
    def get_version(self):
        return self._com.version()
    def get_build_no(self):
        return self._com.getBuildNo()
""",
        encoding="utf-8",
    )

    members = collect_python_members("IRPApplication", models_root)

    assert "get_version() -> version" in members["version"]
    assert "get_build_no() -> getBuildNo" in members["getBuildNo"]


def test_resolve_python_wrapper_maps_application_interface_to_facade_file(tmp_path: Path) -> None:
    models_root = tmp_path / "models"
    models_root.mkdir()
    application_source = tmp_path / "application.py"
    application_source.write_text("class RhapsodyApplication: pass", encoding="utf-8")

    wrapper_name, wrapper_source = resolve_python_wrapper("IRPApplication", models_root)

    assert wrapper_name == "RhapsodyApplication"
    assert wrapper_source == application_source


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
            "Rename the Python method to the snake_case Java API name or document the alias.",
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
    assert "**Java signature(s):** `IRPApplication.getBuildNo()`" in report
    assert "**Expected Python method(s):** `get_build_no`" in report
    assert "Use the BuildNo property or a getter/setter fallback instead of calling getBuildNo directly." in report
    assert "## AI Fix Guidance" in report


def test_main_writes_markdown_report_to_default_and_requested_directories(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(validator, "resolve_python_wrapper", lambda interface_name, models_root: ("RhapsodyApplication", models_root.parent / "application.py"))
    monkeypatch.setattr(validator, "collect_java_signatures", lambda interface_name, docs_root: {"version": {"IRPApplication.version()"}})
    monkeypatch.setattr(validator, "collect_java_members", lambda interface_name, docs_root: {"version"})
    monkeypatch.setattr(validator, "collect_python_members", lambda interface_name, models_root: {"version": {"version() -> version"}})
    monkeypatch.setattr(validator, "collect_registered_pywin32_members", lambda interface_name: {"version": "method"})

    assert main(["IRPApplication"]) == 0
    default_report = tmp_path / "IRPApplication_api_report.md"
    assert default_report.is_file()
    assert "# Rhapsody API Validation: IRPApplication" in default_report.read_text(encoding="utf-8")

    custom_directory = tmp_path / "reports"
    assert main(["IRPApplication", "--path", str(custom_directory)]) == 0
    custom_report = custom_directory / "IRPApplication_api_report.md"
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
) -> AuthorityData:
    return AuthorityData(
        catalog=catalog or {},
        documented_aliases=aliases or {},
        documented_unavailable=unavailable or {},
    )


def test_apply_pywin32_authority_demotes_expected_differences() -> None:
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

    assert deviations == []
    assert informational == rows
    assert backlog == []


def test_apply_pywin32_authority_suppresses_documented_alias() -> None:
    rows = [
        (
            "get_description_html() -> descriptionHTML; get_description_html() -> getDescriptionHTML",
            "getDescriptionHTML (method)",
            "descriptionHTML (property)",
            "PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
            "Rename the Python method.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(
        rows, "IRPClass", _authority(aliases={"IRPClass": {"get_description_html": "description_html"}})
    )

    assert deviations == []
    assert informational == rows
    assert backlog == []


def test_apply_pywin32_authority_suppresses_documented_unavailable_member() -> None:
    rows = [
        (
            "get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl",
            "getRmmUrl (method)",
            "—",
            "PYWIN32_MEMBER_MISSING",
            "Use a member exposed by the registered type library.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(
        rows, "IRPClass", _authority(unavailable={"IRPClass": ["getRmmUrl"]})
    )

    assert (deviations, informational, backlog) == ([], [], [])


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
            "COM_MEMBER_NOT_EXPOSED",
            "Use the BinaryID property.",
        )
    ]
    assert informational == []
    assert backlog == []


def test_main_authority_source_reports_backlog_without_typelib(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(validator, "load_authority", lambda: _authority(catalog={"IRPClass": {"isAbstract": "property"}}))
    monkeypatch.setattr(validator, "collect_java_signatures", lambda interface_name, docs_root: {"isAbstract": {"IRPClass.isAbstract()"}})
    monkeypatch.setattr(validator, "collect_java_members", lambda interface_name, docs_root: {"isAbstract"})
    monkeypatch.setattr(validator, "collect_python_members", lambda interface_name, models_root: {"isAbstract": {"is_abstract() -> isAbstract"}})

    assert validator.main(["IRPClass", "--source", "authority"]) == 0

    report = (tmp_path / "IRPClass_api_report.md").read_text(encoding="utf-8")
    assert "## Expected Binding Differences" in report
    assert "## Wrapper Backlog" in report
    assert "No deviations require changes." in report


def test_irpclass_report_has_no_actionable_deviations() -> None:
    reports_root = Path(__file__).resolve().parents[2] / "docs" / "reports"
    text = (reports_root / "IRPClass_api_report.md").read_text(encoding="utf-8")
    section = text.split("## Comparison details", 1)[1].split("## Expected Binding Differences", 1)[0]
    rows = [
        line
        for line in section.splitlines()
        if line.startswith("| ") and "Python model wrapper" not in line and "---" not in line
    ]
    assert rows == [], rows
