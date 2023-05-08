# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import pytest
from src.interactor.validations.create_profession_validator \
    import CreateProfessionInputDtoValidator
from src.interactor.errors.error_classes import FieldValueNotPermittedException


def test_create_profession_validator_valid_data(
        mocker,
        fixture_profession_developer
):
    mocker.patch("src.interactor.validations.base_input_validator.\
BaseInputValidator.verify")
    input_data = {
            "name": fixture_profession_developer["name"],
            "description": fixture_profession_developer["description"]
    }
    schema = {
            "name": {
                "type": "string",
                "minlength": 3,
                "maxlength": 80,
                "required": True,
                "empty": False
            },
            "description": {
                "type": "string",
                "minlength": 5,
                "maxlength": 200,
                "required": True,
                "empty": False
            }
    }
    validator = CreateProfessionInputDtoValidator(input_data)
    validator.validate()
    assert validator.verify.call_once_with(schema)  # pylint: disable=E1101


def test_create_profession_validator_empty_input(fixture_profession_developer):
    # We are doing just a simple test as the complete test is done in
    # base_input_validator_test.py
    input_data = {
            "name": fixture_profession_developer["name"],
            "description": "",
        }
    validator = CreateProfessionInputDtoValidator(input_data)
    with pytest.raises(ValueError) as exception_info:
        validator.validate()
    assert str(exception_info.value) == "Description: empty values not allowed"


def test_create_profession_custom_validation(fixture_profession_developer):
    input_data = {
            "name": "Profession",
            "description": fixture_profession_developer["description"],
        }
    validator = CreateProfessionInputDtoValidator(input_data)
    with pytest.raises(FieldValueNotPermittedException) as exception_info:
        validator.validate()
    assert str(exception_info.value) == "Name: Profession is not permitted"
