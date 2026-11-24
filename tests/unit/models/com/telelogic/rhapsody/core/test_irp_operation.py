"""Tests for rhapsody_cli.elements.operation.IRPOperation."""

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_argument import IRPArgument
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation
from rhapsody_cli.models.elements.activity.model_activity import RPFlowchart
from tests.unit.models.fakes import make_fake_element


def test_operation_is_an_interface_item() -> None:
    fake = make_fake_element("Operation", properties={"name": "doIt"})
    operation = IRPOperation(fake)

    assert isinstance(operation, IRPInterfaceItem)
    assert operation.name == "doIt"


def test_operation_body_reads_com_property() -> None:
    fake = make_fake_element("Operation", properties={"body": "return 0;"})
    operation = IRPOperation(fake)

    assert operation.body == "return 0;"


def test_operation_body_setter_writes_com_property() -> None:
    fake = make_fake_element("Operation")
    operation = IRPOperation(fake)

    operation.body = "return 1;"

    assert fake.body == "return 1;"


def test_operation_is_abstract_reads_com_property() -> None:
    fake = make_fake_element("Operation", properties={"isAbstract": 1})
    operation = IRPOperation(fake)

    assert operation.is_abstract is True


def test_operation_is_abstract_setter_writes_com_property() -> None:
    fake = make_fake_element("Operation")
    operation = IRPOperation(fake)

    operation.is_abstract = 1

    assert fake.isAbstract == 1


def test_operation_is_static_reads_com_property() -> None:
    fake = make_fake_element("Operation", properties={"isStatic": 0})
    operation = IRPOperation(fake)

    assert operation.is_static is False


def test_operation_is_static_setter_writes_com_property() -> None:
    fake = make_fake_element("Operation")
    operation = IRPOperation(fake)

    operation.is_static = 1

    assert fake.isStatic == 1


def test_operation_is_virtual_reads_com_property() -> None:
    fake = make_fake_element("Operation", properties={"isVirtual": 1})
    operation = IRPOperation(fake)

    assert operation.is_virtual is True


def test_operation_is_virtual_setter_writes_com_property() -> None:
    fake = make_fake_element("Operation")
    operation = IRPOperation(fake)

    operation.is_virtual = 1

    assert fake.isVirtual == 1


def test_operation_returns_wraps_result() -> None:
    fake = make_fake_element("Operation")
    return_type = make_fake_element("Class", properties={"name": "int"})
    fake.returns = return_type
    operation = IRPOperation(fake)

    result = operation.returns
    assert result.name == "int"


def test_operation_returns_setter_writes_com_property() -> None:
    fake = make_fake_element("Operation")
    operation = IRPOperation(fake)
    return_type = IRPOperation(make_fake_element("Class", properties={"name": "int"}))

    operation.returns = return_type

    assert fake.returns == return_type._com


def test_operation_get_return_type_declaration_delegates_to_com() -> None:
    fake = make_fake_element("Operation", getReturnTypeDeclaration="int")
    operation = IRPOperation(fake)

    assert operation.get_return_type_declaration() == "int"


def test_operation_set_return_type_declaration_delegates_to_com() -> None:
    fake = make_fake_element("Operation")
    operation = IRPOperation(fake)

    operation.set_return_type_declaration("int")

    fake.setReturnTypeDeclaration.assert_called_once_with("int")


def test_operation_create_auto_flow_chart_delegates_to_com() -> None:
    fake = make_fake_element("Operation")
    operation = IRPOperation(fake)

    operation.create_auto_flow_chart()

    fake.createAutoFlowChart.assert_called_once_with()


def test_operation_is_registered_for_meta_class_operation() -> None:
    fake = make_fake_element("Operation", properties={"name": "doIt"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPOperation)


def test_delete_argument_delegates_to_com() -> None:
    fake = make_fake_element("Operation")
    argument = IRPArgument(make_fake_element("Argument"))
    IRPOperation(fake).delete_argument(argument)
    fake.deleteArgument.assert_called_once_with(argument._com)


def test_delete_flowchart_delegates_to_com() -> None:
    fake = make_fake_element("Operation")
    IRPOperation(fake).delete_flowchart()
    fake.deleteFlowchart.assert_called_once_with()


def test_operation_flowchart_reads_com_property() -> None:
    fake = make_fake_element("Operation", properties={"flowchart": make_fake_element("ActivityDiagram", properties={"name": "Flow"})})
    assert IRPOperation(fake).flowchart.name == "Flow"


def test_operation_flowchart_setter_writes_com_property() -> None:
    fake = make_fake_element("Operation")
    chart = RPFlowchart(make_fake_element("ActivityDiagram"))
    IRPOperation(fake).flowchart = chart
    assert fake.flowchart is chart._com


def test_get_implementation_signature_delegates_to_com() -> None:
    fake = make_fake_element("Operation", getImplementationSignature="void doIt()")
    assert IRPOperation(fake).get_implementation_signature() == "void doIt()"


def test_operation_initializer_reads_com_property() -> None:
    fake = make_fake_element("Operation", properties={"initializer": "init"})
    assert IRPOperation(fake).initializer == "init"


def test_operation_initializer_setter_writes_com_property() -> None:
    fake = make_fake_element("Operation")
    IRPOperation(fake).initializer = "init"
    assert fake.initializer == "init"


def test_integer_flag_properties_read_com_properties() -> None:
    for name, attribute in (
        ("isCgDerived", "is_cg_derived"),
        ("isConst", "is_const"),
        ("isCtor", "is_ctor"),
        ("isDtor", "is_dtor"),
        ("isFinal", "is_final"),
        ("isInline", "is_inline"),
        ("isTrigger", "is_trigger"),
    ):
        fake = make_fake_element("Operation", properties={name: 1})
        assert getattr(IRPOperation(fake), attribute) == 1


def test_operation_visibility_reads_com_property() -> None:
    fake = make_fake_element("Operation", properties={"visibility": "public"})
    assert IRPOperation(fake).visibility == "public"


def test_operation_visibility_setter_writes_com_property() -> None:
    fake = make_fake_element("Operation")
    IRPOperation(fake).visibility = "private"
    assert fake.visibility == "private"


def test_operation_integer_flag_setters_write_com_properties() -> None:
    fake = make_fake_element("Operation")
    operation = IRPOperation(fake)
    operation.is_const = 1
    operation.is_final = 1
    assert fake.isConst == 1
    assert fake.isFinal == 1


def test_converted_members_are_properties_without_get_set_aliases() -> None:
    for name in (
        "body",
        "flowchart",
        "initializer",
        "is_abstract",
        "is_cg_derived",
        "is_const",
        "is_ctor",
        "is_dtor",
        "is_final",
        "is_inline",
        "is_static",
        "is_trigger",
        "is_virtual",
        "returns",
        "visibility",
    ):
        assert isinstance(getattr(IRPOperation, name), property)

    for legacy_name in (
        "get_body",
        "set_body",
        "get_flowchart",
        "set_flowchart",
        "get_initializer",
        "set_initializer",
        "get_is_abstract",
        "set_is_abstract",
        "get_is_cg_derived",
        "get_is_const",
        "set_is_const",
        "get_is_ctor",
        "get_is_dtor",
        "get_is_final",
        "set_is_final",
        "get_is_inline",
        "get_is_static",
        "set_is_static",
        "get_is_trigger",
        "get_is_virtual",
        "set_is_virtual",
        "get_returns",
        "set_returns",
        "get_visibility",
        "set_visibility",
    ):
        assert not hasattr(IRPOperation, legacy_name)


def test_update_contained_diagrams_on_server_raises_not_implemented_without_com_dispatch() -> None:
    fake = make_fake_element("Operation")

    with pytest.raises(NotImplementedError):
        IRPOperation(fake).update_contained_diagrams_on_server(1)

    fake.updateContainedDiagramsOnServer.assert_not_called()
