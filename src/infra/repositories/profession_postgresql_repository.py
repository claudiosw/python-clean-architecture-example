""" Module for ProfessionPostgresqlRepository
"""

from typing import Optional
import uuid
from sqlalchemy.exc import IntegrityError
from src.domain.entities.profession import Profession
from src.interactor.interfaces.repositories.profession_repository \
    import ProfessionRepositoryInterface
from src.domain.value_objects import ProfessionId
from src.infra.db_models.db_base import Session
from src.infra.db_models.profession_db_model import ProfessionsDBModel
from src.interactor.errors.error_classes import UniqueViolationError


class ProfessionPostgresqlRepository(ProfessionRepositoryInterface):
    """ Postgresql Repository for Profession
    """
    def __init__(self) -> None:
        self.__session = Session

    def __db_to_entity(
            self, db_row: ProfessionsDBModel
    ) -> Optional[Profession]:
        return Profession(
            profession_id=db_row.profession_id,
            name=db_row.name,
            description=db_row.description
        )

    def create(self, name: str, description: str) -> Optional[Profession]:
        """ Create Profession
        :param name: str
        :param description: str
        :return: Optional[Profession]
        """
        profession_id = uuid.uuid4()
        profession_db_model = ProfessionsDBModel(
            profession_id=profession_id,
            name=name,
            description=description
        )

        try:
            self.__session.add(profession_db_model)
            self.__session.commit()
            self.__session.refresh(profession_db_model)
        except IntegrityError as exception:
            if "violates unique constraint" in str(exception.orig):
                raise UniqueViolationError(
                    "Profession with the same name already exists"
                ) from exception
            raise

        if profession_db_model is not None:
            return self.__db_to_entity(profession_db_model)
        return None

    def get(self, profession_id: ProfessionId) -> Optional[Profession]:
        """ Get Profession by id
        :param profession_id: ProfessionId
        :return: Optional[Profession]
        """
        result = self.__session.query(ProfessionsDBModel).get(profession_id)
        if result is not None:
            return self.__db_to_entity(result)
        return None

    def update(self, profession: Profession) -> Optional[Profession]:
        """ Update Profession
        :param profession: Profession
        :return: Optional[Profession]
        """
        profession_db_model = ProfessionsDBModel(
            profession_id=profession.profession_id,
            name=profession.name,
            description=profession.description
        )
        result = self.__session.query(
            ProfessionsDBModel
        ).filter_by(
            profession_id=profession.profession_id
        ).update(
            {
                "name": profession.name,
                "description": profession.description
            }
        )
        if result == 0:
            return None
        self.__session.commit()
        return self.__db_to_entity(profession_db_model)
