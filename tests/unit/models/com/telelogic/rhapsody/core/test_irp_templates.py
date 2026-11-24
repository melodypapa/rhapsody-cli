"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.irp_templates classes."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import (
    IRPTemplateInstantiation,
    IRPTemplateInstantiationParameter,
    IRPTemplateParameter,
)
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


class TestRPTemplateInstantiation:
    def test_is_registered(self) -> None:
        fake = make_fake_element("TemplateInstantiation", properties={"name": "TI1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPTemplateInstantiation)

    def test_get_template_instantiation_parameters_returns_collection(self) -> None:
        fake = make_fake_element("TemplateInstantiation")
        p = make_fake_element("TemplateInstantiationParameter", properties={"name": "p1"})
        fake.getTemplateInstantiationParameters.return_value = make_fake_collection([p])
        ti = IRPTemplateInstantiation(fake)
        result = ti.get_template_instantiation_parameters()
        assert isinstance(result, IRPCollection)


class TestRPTemplateInstantiationParameter:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("TemplateInstantiationParameter", properties={"name": "p1"})
        param = IRPTemplateInstantiationParameter(fake)
        assert isinstance(param, IRPModelElement)
        assert param.name == "p1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("TemplateInstantiationParameter", properties={"name": "p1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPTemplateInstantiationParameter)

    def test_get_arg_value_returns_string(self) -> None:
        fake = make_fake_element("TemplateInstantiationParameter", getArgValue="int")
        param = IRPTemplateInstantiationParameter(fake)
        assert param.get_arg_value() == "int"

    def test_get_type_wraps_result(self) -> None:
        fake = make_fake_element("TemplateInstantiationParameter")
        clf = make_fake_element("Class", properties={"name": "C1"})
        fake.getType.return_value = clf
        param = IRPTemplateInstantiationParameter(fake)
        wrapped = param.get_type()
        assert wrapped.name == "C1"

    def test_set_arg_value_delegates(self) -> None:
        fake = make_fake_element("TemplateInstantiationParameter")
        param = IRPTemplateInstantiationParameter(fake)
        param.set_arg_value("int")
        fake.setArgValue.assert_called_once_with("int")

    def test_set_type_delegates(self) -> None:
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier

        fake = make_fake_element("TemplateInstantiationParameter")
        clf = make_fake_element("Class", properties={"name": "C1"})
        param = IRPTemplateInstantiationParameter(fake)
        param.set_type(IRPClassifier(clf))
        fake.setType.assert_called_once_with(clf)


class TestRPTemplateParameter:
    def test_is_registered(self) -> None:
        fake = make_fake_element("TemplateParameter", properties={"name": "tp1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPTemplateParameter)

    def test_get_parameter_kind_returns_string(self) -> None:
        fake = make_fake_element("TemplateParameter", getParameterKind="class")
        tp = IRPTemplateParameter(fake)
        assert tp.get_parameter_kind() == "class"

    def test_get_representative_wraps_result(self) -> None:
        fake = make_fake_element("TemplateParameter")
        rep = make_fake_element("Class", properties={"name": "C1"})
        fake.getRepresentative.return_value = rep
        tp = IRPTemplateParameter(fake)
        wrapped = tp.get_representative()
        assert wrapped is not None and wrapped.name == "C1"

    def test_set_parameter_kind_delegates(self) -> None:
        fake = make_fake_element("TemplateParameter")
        tp = IRPTemplateParameter(fake)
        tp.set_parameter_kind("class")
        fake.setParameterKind.assert_called_once_with("class")

    def test_set_representative_delegates(self) -> None:
        fake = make_fake_element("TemplateParameter")
        rep = make_fake_element("Class", properties={"name": "C1"})
        tp = IRPTemplateParameter(fake)
        tp.set_representative(IRPModelElement(rep))
        fake.setRepresentative.assert_called_once_with(rep)

    def test_set_class_type_delegates(self) -> None:
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier

        fake = make_fake_element("TemplateParameter")
        clf = make_fake_element("Class", properties={"name": "C1"})
        tp = IRPTemplateParameter(fake)
        tp.set_class_type(IRPClassifier(clf))
        fake.setClassType.assert_called_once_with(clf)
