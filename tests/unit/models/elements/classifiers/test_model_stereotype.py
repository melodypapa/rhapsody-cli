"""Tests for rhapsody_cli.models.elements.classifiers.RPStereotype."""

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.elements.classifiers import RPStereotype
from tests.unit.models.fakes import make_fake_element


def test_stereotype_is_a_classifier() -> None:
    fake = make_fake_element("Stereotype", properties={"name": "MyStereo"})
    stereo = RPStereotype(fake)

    assert isinstance(stereo, IRPClassifier)
    assert stereo.get_name() == "MyStereo"


def test_stereotype_is_registered_for_meta_class_stereotype() -> None:
    fake = make_fake_element("Stereotype", properties={"name": "MyStereo"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, RPStereotype)


def test_stereotype_set_is_new_term_raises_not_implemented() -> None:
    """RPStereotype.set_is_new_term raises NotImplementedError: setIsNewTerm is not exposed
    in the Rhapsody COM automation type library (get_is_new_term is)."""
    fake = make_fake_element("Stereotype")
    stereo = RPStereotype(fake)

    with pytest.raises(NotImplementedError):
        stereo.set_is_new_term(1)

    fake.setIsNewTerm.assert_not_called()
