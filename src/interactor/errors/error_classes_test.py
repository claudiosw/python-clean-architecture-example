# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import pytest
from src.interactor.errors.error_classes \
    import FieldValueNotPermittedException


def test_empty_field_exception():
    with pytest.raises(FieldValueNotPermittedException) as exception_info:
        raise FieldValueNotPermittedException("name", "Profession")
    assert str(exception_info.value) == "Name: Profession is not permitted"
