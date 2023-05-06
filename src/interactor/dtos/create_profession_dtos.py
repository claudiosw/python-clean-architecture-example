""" Module for CreateProfession Dtos
"""


from dataclasses import dataclass, asdict
from src.domain.entities.profession import Profession


@dataclass
class CreateProfessionInputDto:
    """ Input Dto for create profession """
    name: str
    description: str

    def to_dict(self):
        """ Convert data into dictionary
        """
        return asdict(self)


@dataclass
class CreateProfessionOutputDto:
    """ Output Dto for create profession """
    profession: Profession
