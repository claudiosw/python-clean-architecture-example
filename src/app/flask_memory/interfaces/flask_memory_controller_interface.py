""" This module contains the FlaskMemoryControllerInterface class
"""


from typing import Dict
from abc import ABC, abstractmethod


class FlaskMemoryControllerInterface(ABC):
    """ This class is the interface for the Flask Memory Controller class
    """

    def get_profession_info(self, json_input) -> None:
        """ Get Profession Info
        :param json_input: Input data
        :raises: ValueError if profession name or description are missing.
        """

    @abstractmethod
    def execute(self) -> Dict:
        """ Executes the controller
        :returns: Profession created
        """
