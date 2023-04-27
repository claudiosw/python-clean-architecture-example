""" Module for CreateProfession Dtos
"""


from dataclasses import dataclass
from src.domain.entities.profession import Profession


@dataclass
class CreateProfessionInputDto:
    """ Input Dto for create profession """
    name: str
    description: str


@dataclass
class CreateProfessionOutputDto:
    """ Output Dto for create profession """
    profession: Profession
