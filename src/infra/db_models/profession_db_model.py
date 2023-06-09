""" Defines the professions database model.
"""


import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from src.infra.db_models.db_base import Base


class ProfessionsDBModel(Base):
    """ Defines the professions database model.
    """

    __tablename__ = "professions"

    profession_id: Mapped[uuid.UUID] = \
        mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(200), nullable=False)
