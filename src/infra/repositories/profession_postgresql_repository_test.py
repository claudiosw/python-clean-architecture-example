# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import pytest
from sqlalchemy.exc import IntegrityError
from src.domain.entities.profession import Profession
from src.infra.db_models.profession_db_model import ProfessionsDBModel
from src.interactor.errors.error_classes import UniqueViolationError
from .profession_postgresql_repository import ProfessionPostgresqlRepository


def test_profession_postgresql_repository(
        mocker,
        fixture_profession_developer
):

    mocker.patch(
        'uuid.uuid4',
        return_value=fixture_profession_developer["profession_id"]
    )
    professions_db_model_mock = mocker.patch(
        'src.infra.repositories.profession_postgresql_repository.\
ProfessionsDBModel')
    session_mock = mocker.patch(
        'src.infra.repositories.profession_postgresql_repository.Session')
    professions_db_model = ProfessionsDBModel(
        profession_id=fixture_profession_developer["profession_id"],
        name=fixture_profession_developer["name"],
        description=fixture_profession_developer["description"]
    )
    professions_db_model_mock.return_value = professions_db_model
    repository = ProfessionPostgresqlRepository()
    result = repository.create(
        fixture_profession_developer["name"],
        fixture_profession_developer["description"]
    )
    profession = Profession(
        professions_db_model_mock.return_value.profession_id,
        professions_db_model_mock.return_value.name,
        professions_db_model_mock.return_value.description
    )
    session_mock.add.assert_called_once_with(professions_db_model_mock())
    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(professions_db_model_mock())
    assert result == profession

    # Testing create return None
    professions_db_model_mock.return_value = None
    result = repository.create(
        fixture_profession_developer["name"],
        fixture_profession_developer["description"]
    )
    assert result is None

    # Testing successful update
    professions_edited_db_model = ProfessionsDBModel(
        profession_id=fixture_profession_developer["profession_id"],
        name="Edited Profession name",
        description="Edited Description"
    )
    professions_db_model_mock.return_value = professions_edited_db_model
    edited_profession = Profession(
        professions_db_model_mock.return_value.profession_id,
        professions_db_model_mock.return_value.name,
        professions_db_model_mock.return_value.description
    )
    repository = ProfessionPostgresqlRepository()
    result = repository.update(
        edited_profession
    )
    session_mock.query.assert_called_once_with(professions_db_model_mock)
    session_mock.query.return_value.filter_by.return_value.update.\
        assert_called_once_with(
            {
                "name": edited_profession.name,
                "description": edited_profession.description
            }
        )
    assert result == edited_profession

    # Testing update with invalid profession_id
    invalid_profession = Profession(
            profession_id="Dont exist profession_id",
            name="Edited Profession name",
            description="Edited Description"
    )
    session_mock.query.return_value.filter_by.return_value.update.return_value\
        = 0
    repository = ProfessionPostgresqlRepository()
    result_invalid_id = repository.update(
        invalid_profession
    )
    assert result_invalid_id is None

    # Testing create with name that violate unique
    session_mock.add.side_effect = IntegrityError(
        None, None,
        'psycopg2.errors.UniqueViolation: duplicate key value violates unique \
constraint "professions_name_key"')
    professions_db_model_mock.return_value = None
    with pytest.raises(UniqueViolationError) as exception_info:
        result = repository.create(
            fixture_profession_developer["name"],
            fixture_profession_developer["description"]
        )
    assert str(exception_info.value) == \
        "Profession with the same name already exists"

    # Testing create raising another IntegrityError
    session_mock.add.side_effect = IntegrityError(None, None, "test error")
    with pytest.raises(IntegrityError) as exception_info:
        result = repository.create("", "")
    assert "test error" in str(exception_info.value)


def test_profession_postgresql_repository_get(
        mocker,
        fixture_profession_developer
):

    session_mock = mocker.patch(
        'src.infra.repositories.profession_postgresql_repository.Session'
    )
    professions_db_model_mock = mocker.patch(
        'src.infra.db_models.profession_db_model.ProfessionsDBModel'
    )
    session_mock.query.return_value.get.return_value = \
        professions_db_model_mock
    profession_mock = Profession(
            profession_id=professions_db_model_mock.profession_id,
            name=professions_db_model_mock.name,
            description=professions_db_model_mock.description
    )
    repository = ProfessionPostgresqlRepository()
    result = repository.get(
        professions_db_model_mock.profession_id
    )
    assert result == profession_mock

    # Testing the case that the query returns None
    session_mock.query.return_value.get.return_value = None
    repository = ProfessionPostgresqlRepository()
    result = repository.get(
        professions_db_model_mock.profession_id
    )
    assert result is None
