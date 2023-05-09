""" This module provides the base class BaseInputValidator for input validation
"""


from typing import Dict
from cerberus import Validator  # type: ignore


class BaseInputValidator:
    """ This class provides the base class for input validation
    """
    def __init__(self, data: Dict[str, str]):
        self.data = data
        self.errors: Dict = {}

    def verify(self, schema: Dict) -> None:
        """ Validates the input data against the provided schema
        :param schema: The schema to validate against
        :return: None
        :raises ValueError: If the input data is invalid.
        """
        validator = Validator(schema)
        if not validator.validate(self.data):
            self.errors = validator.errors
            self._raise_validation_error()

    def _raise_validation_error(self):
        error_messages = []
        for field, messages in self.errors.items():
            for message in messages:
                error_messages.append(f"{field.capitalize()}: {message}")
        raise ValueError("\n".join(error_messages))
