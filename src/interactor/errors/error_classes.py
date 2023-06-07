""" This module contains exceptions for the Use Cases layer
"""


class FieldValueNotPermittedException(Exception):
    """ Exception raised when a field is empty """
    def __init__(self, field_name: str, field_value: str) -> None:
        self.field_name = field_name
        self.field_value = field_value

    def __str__(self) -> str:
        return f"{self.field_name.capitalize()}: {self.field_value} is not \
permitted"


class ItemNotCreatedException(Exception):
    """ Exception raised when an item is not created """
    def __init__(self, item_name: str, item_type: str) -> None:
        self.item_name = item_name
        self.item_type = item_type

    def __str__(self) -> str:
        return f"{self.item_type.capitalize()} '{self.item_name}' was not \
created correctly"


class UniqueViolationError(Exception):
    """ Exception raised when a unique constraint is violated """
