# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from typing import Dict
import pytest
from src.interactor.validations.base_input_validator import BaseInputValidator


class BaseValidator(BaseInputValidator):
    def __init__(self, data: Dict):
        super().__init__(data)
        self.schema = {
                "name": {
                    "type": "string",
                    "minlength": 3,
                    "maxlength": 10,
                    "required": True,
                    "empty": False
                },
                "description": {
                    "type": "string",
                    "minlength": 3,
                    "maxlength": 10,
                    "required": False,
                    "empty": True
                }
        }

    def validate(self):
        super().verify(self.schema)


def test_base_validator_with_valid_data():
    data = {'name': 'test'}
    validator = BaseValidator(data)
    validator.validate()


def test_base_validator_with_small_data():
    data = {'name': 'a', 'description': 'a'}
    validator = BaseValidator(data)
    with pytest.raises(ValueError) as exception_info:
        validator.validate()
    assert str(exception_info.value) == "Description: min length is 3\n\
Name: min length is 3"


def test_base_validator_with_long_data():
    data = {'name': 'this is a long name'}
    validator = BaseValidator(data)
    with pytest.raises(ValueError) as exception_info:
        validator.validate()
    assert str(exception_info.value) == "Name: max length is 10"


def test_base_validator_with_empty_data():
    data = {'name': ''}
    validator = BaseValidator(data)
    with pytest.raises(ValueError) as exception_info:
        validator.validate()
    assert str(exception_info.value) == "Name: empty values not allowed"


def test_base_validator_without_required_data():
    data = {}
    validator = BaseValidator(data)
    with pytest.raises(ValueError) as exception_info:
        validator.validate()
    assert str(exception_info.value) == "Name: required field"
