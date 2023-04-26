""" This module has definition of the Profession entity
"""


from dataclasses import dataclass, asdict
from src.domain.value_objects import ProfessionId


@dataclass
class Profession:
    """ Definition of the Profession entity
    """
    profession_id: ProfessionId
    name: str
    description: str

    @classmethod
    def from_dict(cls, data):
        """ Convert data from a dictionary
        """
        return cls(**data)

    def to_dict(self):
        """ Convert data into dictionary
        """
        return asdict(self)
