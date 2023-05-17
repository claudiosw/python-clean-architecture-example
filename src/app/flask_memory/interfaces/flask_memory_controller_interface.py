""" This module contains the CliMemoryControllerInterface class
"""


from typing import Dict
from abc import ABC, abstractmethod


class FlaskMemoryControllerInterface(ABC):
    """ This class is the interface for the CliMemoryController class
    """

    def get_profession_info(self, json_input) -> None:
        """ Get Profession Info
        :param json_input: Input data
        :raises: ValueError if missing profession name or description.
        """

    @abstractmethod
    def execute(self) -> Dict:
        """ Executes the controller
        """
