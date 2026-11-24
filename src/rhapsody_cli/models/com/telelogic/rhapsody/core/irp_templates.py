"""Templates model-element wrappers (auto-generated stubs)."""

from typing import TYPE_CHECKING, Optional, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPVariable
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier


class IRPTemplateInstantiation(IRPModelElement):
    """Wraps ``IRPTemplateInstantiation``."""

    # IRPTemplateInstantiation method parity checklist:
    # [x] get_template_instantiation_parameters [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPTemplateInstantiation methods.

    def get_template_instantiation_parameters(self) -> "IRPCollection":
        """Returns the template instantiation parameters of this template instantiation.

        Returns:
            A ``IRPCollection`` of the template instantiation parameters.

        Raises:
            RhapsodyRuntimeException: If the property cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPTemplateInstantiation::getTemplateInstantiationParameters()
        """
        return IRPCollection(self._get_method_or_property(self._com, "getTemplateInstantiationParameters", "templateInstantiationParameters"))


class IRPTemplateInstantiationParameter(IRPModelElement):
    """Wraps ``IRPTemplateInstantiationParameter``."""

    # IRPTemplateInstantiationParameter method parity checklist:
    # [x] get_arg_value                  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_type                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_arg_value                  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_type                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPTemplateInstantiationParameter methods.

    def get_arg_value(self) -> str:
        """Returns the argument value of this template instantiation parameter.

        Returns:
            The argument value as a string.

        Raises:
            RhapsodyRuntimeException: If the property cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPTemplateInstantiationParameter::getArgValue()
        """
        return str(self._get_method_or_property(self._com, "getArgValue", "argValue"))

    def get_type(self) -> "IRPClassifier":
        """Returns the type of this template instantiation parameter.

        Returns:
            The type of this template instantiation parameter.

        Raises:
            RhapsodyRuntimeException: If the property cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPTemplateInstantiationParameter::getType()
        """
        return cast("IRPClassifier", self.wrap(self._get_method_or_property(self._com, "getType", "type")))

    def set_arg_value(self, arg_value: str) -> None:
        """Sets the argument value of this template instantiation parameter.

        Args:
            arg_value: The argument value to set.

        Raises:
            RhapsodyRuntimeException: If the property cannot be set.

        Reference:
            com.telelogic.rhapsody.core.IRPTemplateInstantiationParameter::setArgValue(java.lang.String argValue)
        """
        self._set_method_or_property(self._com, "setArgValue", "argValue", arg_value)

    def set_type(self, type_: "IRPClassifier") -> None:
        """Sets the type of this template instantiation parameter.

        Args:
            type_: The type to set.

        Raises:
            RhapsodyRuntimeException: If the property cannot be set.

        Reference:
            com.telelogic.rhapsody.core.IRPTemplateInstantiationParameter::setType(com.telelogic.rhapsody.core.IRPClassifier type)
        """
        self._set_method_or_property(self._com, "setType", "type", type_._com)


class IRPTemplateParameter(IRPVariable):
    """Wraps ``IRPTemplateParameter``: represents parameters of a template in Rhapsody models."""

    # IRPTemplateParameter method parity checklist:
    # [x] get_parameter_kind             [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_representative            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_class_type                 [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_parameter_kind             [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_representative            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # [inherited] irp_unit methods (covered by rp_unit checklist)
    # [inherited] irp_variable methods (covered by rp_variable checklist)
    # No deprecated IRPTemplateParameter methods.

    def get_parameter_kind(self) -> str:
        """Returns the type of the template parameter.

        Returns:
            The type of the template parameter.

        Reference:
            com.telelogic.rhapsody.core.IRPTemplateParameter::getParameterKind()
        """
        return str(self._get_method_or_property(self._com, "getParameterKind", "parameterKind"))

    def get_representative(self) -> Optional["IRPModelElement"]:
        """Returns the representative of this template parameter.

        For internal use only.

        Returns:
            The representative model element of this template parameter.

        Reference:
            com.telelogic.rhapsody.core.IRPTemplateParameter::getRepresentative()
        """
        return self.wrap(self._get_method_or_property(self._com, "getRepresentative", "representative"))

    def set_class_type(self, class_type: "IRPClassifier") -> None:
        """Sets the type of the parameter to "class".

        Args:
            class_type: The classifier to set as the class type.

        Reference:
            com.telelogic.rhapsody.core.IRPTemplateParameter::setClassType(com.telelogic.rhapsody.core.IRPClassifier classType)
        """
        self.call_com(lambda: self._com.setClassType(class_type._com))

    def set_parameter_kind(self, parameter_kind: str) -> None:
        """Specifies the type of the template parameter.

        Args:
            parameter_kind: The type to use for the template parameter.

        Reference:
            com.telelogic.rhapsody.core.IRPTemplateParameter::setParameterKind(java.lang.String parameterKind)
        """
        self._set_method_or_property(self._com, "setParameterKind", "parameterKind", parameter_kind)

    def set_representative(self, representative: "IRPModelElement") -> None:
        """Sets the representative of this template parameter.

        For internal use only.

        Args:
            representative: The representative model element to set.

        Reference:
            com.telelogic.rhapsody.core.IRPTemplateParameter::setRepresentative(com.telelogic.rhapsody.core.IRPModelElement representative)
        """
        self._set_method_or_property(self._com, "setRepresentative", "representative", representative._com)


IRPModelElement.register_wrapper("TemplateInstantiation", IRPTemplateInstantiation)
IRPModelElement.register_wrapper("TemplateInstantiationParameter", IRPTemplateInstantiationParameter)
IRPModelElement.register_wrapper("TemplateParameter", IRPTemplateParameter)
