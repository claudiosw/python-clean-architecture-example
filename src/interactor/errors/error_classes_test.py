# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import pytest
from src.interactor.errors.error_classes \
    import FieldValueNotPermittedException
from src.interactor.errors.error_classes import ItemNotCreatedException


def test_empty_field_exception():
    with pytest.raises(FieldValueNotPermittedException) as exception_info:
        raise FieldValueNotPermittedException("name", "Profession")
    assert str(exception_info.value) == "Name: Profession is not permitted"


def test_item_not_created_exception():
    with pytest.raises(ItemNotCreatedException) as exception_info:
        raise ItemNotCreatedException("profession name", "profession")
    assert str(exception_info.value) == \
        "Profession 'profession name' was not created correctly"
