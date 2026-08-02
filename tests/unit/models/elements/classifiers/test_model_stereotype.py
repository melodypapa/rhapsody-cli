"""Tests for rhapsody_cli.models.elements.classifiers.RPStereotype."""

import pytest

from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.classifiers import RPClassifier, RPStereotype
from tests.unit.models.fakes import make_fake_element


def test_stereotype_is_a_classifier() -> None:
    fake = make_fake_element("Stereotype", getName="MyStereo")
    stereo = RPStereotype(fake)

    assert isinstance(stereo, RPClassifier)
    assert stereo.get_name() == "MyStereo"


def test_stereotype_is_registered_for_meta_class_stereotype() -> None:
    fake = make_fake_element("Stereotype", getName="MyStereo")

    wrapped = AbstractRPModelElement.wrap(fake)

    assert isinstance(wrapped, RPStereotype)


def test_stereotype_set_is_new_term_raises_not_implemented() -> None:
    """RPStereotype.set_is_new_term raises NotImplementedError: setIsNewTerm is not exposed
    in the Rhapsody COM automation type library (get_is_new_term is)."""
    fake = make_fake_element("Stereotype")
    stereo = RPStereotype(fake)

    with pytest.raises(NotImplementedError):
        stereo.set_is_new_term(1)

    fake.setIsNewTerm.assert_not_called()
