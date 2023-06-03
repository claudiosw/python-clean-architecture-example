""" This module contains the interface for the ProfessionRepository
"""


from abc import ABC, abstractmethod
from typing import Optional
from src.domain.value_objects import ProfessionId
from src.domain.entities.profession import Profession


class ProfessionRepositoryInterface(ABC):
    """ This class is the interface for the ProfessionRepository
    """

    @abstractmethod
    def get(self, profession_id: ProfessionId) -> Optional[Profession]:
        """ Get a Profession by id

        :param profession_id: ProfessionId
        :return: Profession
        """

    @abstractmethod
    def create(self, name: str, description: str) -> Optional[Profession]:
        """ Create a Profession

        :param name: Profession Name
        :param description: Profession Description
        :return: ProfessionId
        """

    @abstractmethod
    def update(self, profession: Profession) -> Optional[Profession]:
        """ Save a Profession

        :param Profession: Profession
        :return: Profession
        """
