"""Tests for rhapsody_cli.elements.operation.IRPOperation."""

from unittest.mock import MagicMock

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
    assert operation.get_name() == "doIt"


def test_operation_get_body_delegates_to_com() -> None:
    fake = make_fake_element("Operation", properties={"body": "return 0;"})
    operation = IRPOperation(fake)

    assert operation.get_body() == "return 0;"


def test_operation_get_is_abstract_delegates_to_com() -> None:
    fake = make_fake_element("Operation", properties={"isAbstract": 1})
    operation = IRPOperation(fake)

    assert operation.get_is_abstract() is True


def test_operation_get_is_static_delegates_to_com() -> None:
    fake = make_fake_element("Operation", properties={"isStatic": 0})
    operation = IRPOperation(fake)

    assert operation.get_is_static() is False


def test_operation_get_is_virtual_delegates_to_com() -> None:
    fake = make_fake_element("Operation", properties={"isVirtual": 1})
    operation = IRPOperation(fake)

    assert operation.get_is_virtual() is True


def test_operation_set_is_abstract_delegates_to_com() -> None:
    fake = make_fake_element("Operation")
    operation = IRPOperation(fake)

    operation.set_is_abstract(1)

    assert fake.isAbstract == 1


def test_operation_set_is_abstract_falls_back_to_property_when_method_missing() -> None:
    fake = MagicMock(spec=["isAbstract"])
    operation = IRPOperation(fake)

    operation.set_is_abstract(1)

    assert fake.isAbstract == 1


def test_operation_set_is_static_delegates_to_com() -> None:
    fake = make_fake_element("Operation")
    operation = IRPOperation(fake)

    operation.set_is_static(1)

    assert fake.isStatic == 1


def test_operation_set_is_static_falls_back_to_property_when_method_missing() -> None:
    fake = MagicMock(spec=["isStatic"])
    operation = IRPOperation(fake)

    operation.set_is_static(1)

    assert fake.isStatic == 1


def test_operation_set_is_virtual_delegates_to_com() -> None:
    fake = make_fake_element("Operation")
    operation = IRPOperation(fake)

    operation.set_is_virtual(1)

    assert fake.isVirtual == 1


def test_operation_set_is_virtual_falls_back_to_property_when_method_missing() -> None:
    fake = MagicMock(spec=["isVirtual"])
    operation = IRPOperation(fake)

    operation.set_is_virtual(1)

    assert fake.isVirtual == 1


def test_operation_get_returns_wraps_result() -> None:
    fake = make_fake_element("Operation")
    return_type = make_fake_element("Class", properties={"name": "int"})
    fake.returns = return_type
    operation = IRPOperation(fake)

    result = operation.get_returns()
    assert result.get_name() == "int"


def test_operation_get_return_type_declaration_delegates_to_com() -> None:
    fake = make_fake_element("Operation", getReturnTypeDeclaration="int")
    operation = IRPOperation(fake)

    assert operation.get_return_type_declaration() == "int"


def test_operation_set_returns_delegates_to_com() -> None:
    fake = make_fake_element("Operation")
    operation = IRPOperation(fake)
    return_type = IRPOperation(make_fake_element("Class", properties={"name": "int"}))

    operation.set_returns(return_type)

    assert fake.returns == return_type._com


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


def test_get_flowchart_wraps_property_result() -> None:
    fake = make_fake_element("Operation", properties={"flowchart": make_fake_element("ActivityDiagram", properties={"name": "Flow"})})
    assert IRPOperation(fake).get_flowchart().get_name() == "Flow"


def test_get_implementation_signature_delegates_to_com() -> None:
    fake = make_fake_element("Operation", getImplementationSignature="void doIt()")
    assert IRPOperation(fake).get_implementation_signature() == "void doIt()"


def test_get_initializer_reads_property() -> None:
    fake = make_fake_element("Operation", properties={"initializer": "init"})
    assert IRPOperation(fake).get_initializer() == "init"


def test_integer_flag_getters_read_properties() -> None:
    for name, getter in (
        ("isCgDerived", "get_is_cg_derived"),
        ("isConst", "get_is_const"),
        ("isCtor", "get_is_ctor"),
        ("isDtor", "get_is_dtor"),
        ("isFinal", "get_is_final"),
        ("isInline", "get_is_inline"),
        ("isTrigger", "get_is_trigger"),
    ):
        fake = make_fake_element("Operation", properties={name: 1})
        assert getattr(IRPOperation(fake), getter)() == 1


def test_get_visibility_reads_property() -> None:
    fake = make_fake_element("Operation", properties={"visibility": "public"})
    assert IRPOperation(fake).get_visibility() == "public"


def test_set_body_writes_property() -> None:
    fake = make_fake_element("Operation")
    IRPOperation(fake).set_body("return 0;")
    assert fake.body == "return 0;"


def test_set_flowchart_writes_property() -> None:
    fake = make_fake_element("Operation")
    chart = RPFlowchart(make_fake_element("ActivityDiagram"))
    IRPOperation(fake).set_flowchart(chart)
    assert fake.flowchart is chart._com


def test_set_initializer_writes_property() -> None:
    fake = make_fake_element("Operation")
    IRPOperation(fake).set_initializer("init")
    assert fake.initializer == "init"


def test_property_shaped_setters_write_properties() -> None:
    fake = make_fake_element("Operation")
    operation = IRPOperation(fake)
    operation.set_is_const(1)
    operation.set_is_final(1)
    operation.set_visibility("private")
    assert fake.isConst == 1
    assert fake.isFinal == 1
    assert fake.visibility == "private"


def test_update_contained_diagrams_on_server_raises_not_implemented_without_com_dispatch() -> None:
    fake = make_fake_element("Operation")

    with pytest.raises(NotImplementedError):
        IRPOperation(fake).update_contained_diagrams_on_server(1)

    fake.updateContainedDiagramsOnServer.assert_not_called()
