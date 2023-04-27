""" Module for the CreateProfessionPresenterInterface
"""


from typing import Dict
from abc import ABC, abstractmethod
from src.interactor.dtos.create_profession_dtos \
    import CreateProfessionOutputDto


class CreateProfessionPresenterInterface(ABC):
    """ Class for the Interface of the ProfessionPresenter
    """
    @abstractmethod
    def present(self, output_dto: CreateProfessionOutputDto) -> Dict:
        """ Present the Profession
        """
