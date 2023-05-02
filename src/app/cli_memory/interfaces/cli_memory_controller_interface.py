""" This module contains the CliMemoryControllerInterface class
"""


from abc import ABC, abstractmethod


class CliMemoryControllerInterface(ABC):
    """ This class is the interface for the CliMemoryController class
    """
    @abstractmethod
    def execute(self):
        """ Executes the controller
        """
