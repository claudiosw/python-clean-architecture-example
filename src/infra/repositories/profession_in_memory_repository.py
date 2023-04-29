""" Module for ProfessionInMemoryRepository
"""


from typing import Dict
import copy
import uuid
from src.domain.entities.profession import Profession
from src.interactor.interfaces.repositories.profession_repository \
    import ProfessionRepositoryInterface
from src.domain.value_objects import ProfessionId


class ProfessionInMemoryRepository(ProfessionRepositoryInterface):
    """ InMemory Repository for Profession
    """
    def __init__(self) -> None:
        self._data: Dict[ProfessionId, Profession] = {}

    def get(self, profession_id: ProfessionId) -> Profession:
        """ Get Profession by id

        :param profession_id: ProfessionId
        :return: Profession
        """
        return copy.deepcopy(self._data[profession_id])

    def create(self, name: str, description: str) -> Profession:
        profession = Profession(
            profession_id=uuid.uuid4(),
            name=name,
            description=description
        )
        self._data[profession.profession_id] = copy.deepcopy(profession)
        return copy.deepcopy(self._data[profession.profession_id])

    def update(self, profession: Profession) -> Profession:
        self._data[profession.profession_id] = copy.deepcopy(profession)
        return copy.deepcopy(self._data[profession.profession_id])
