""" Defines the validator for the create profession input data.
"""


from typing import Dict
from src.interactor.validations.base_input_validator import BaseInputValidator
from src.interactor.errors.error_classes import FieldValueNotPermittedException


class CreateProfessionInputDtoValidator(BaseInputValidator):
    """ Validates the create profession input data.
    :param input_data: The input data to be validated.
    """

    def __init__(self, input_data: Dict) -> None:
        super().__init__(input_data)
        self.input_data = input_data
        self.__schema = {
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

    def validate(self) -> None:
        """ Validates the input data
        """
        # Verify the input data using BaseInputValidator method
        super().verify(self.__schema)
        # This is an example of a custom validation
        if self.input_data["name"] == "Profession":
            raise FieldValueNotPermittedException("name", "Profession")
