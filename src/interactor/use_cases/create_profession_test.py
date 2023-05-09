# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import pytest
from src.interactor.use_cases import create_profession
from src.domain.entities.profession import Profession
from src.interactor.dtos.create_profession_dtos \
    import CreateProfessionInputDto, CreateProfessionOutputDto
from src.interactor.interfaces.presenters.create_profession_presenter \
    import CreateProfessionPresenterInterface
from src.interactor.interfaces.repositories.profession_repository \
    import ProfessionRepositoryInterface
from src.interactor.interfaces.logger.logger import LoggerInterface


def test_create_profession(mocker, fixture_profession_developer):
    profession = Profession(
        profession_id=fixture_profession_developer["profession_id"],
        name=fixture_profession_developer["name"],
        description=fixture_profession_developer["description"]
    )
    presenter_mock = mocker.patch.object(
        CreateProfessionPresenterInterface,
        "present"
    )
    repository_mock = mocker.patch.object(
        ProfessionRepositoryInterface,
        "create"
    )
    logger_mock = mocker.patch.object(
        LoggerInterface,
        "log_info"
    )
    repository_mock.create.return_value = profession
    presenter_mock.present.return_value = "Test output"
    use_case = create_profession.CreateProfessionUseCase(
        presenter_mock,
        repository_mock,
        logger_mock
    )
    input_dto = CreateProfessionInputDto(
        name=fixture_profession_developer["name"],
        description=fixture_profession_developer["description"]
    )
    result = use_case.execute(input_dto)
    repository_mock.create.assert_called_once()
    logger_mock.log_info.assert_called_once_with(
        "Profession created successfully")
    output_dto = CreateProfessionOutputDto(profession)
    presenter_mock.present.assert_called_once_with(output_dto)
    assert result == "Test output"


def test_create_profession_empty_field(mocker, fixture_profession_developer):
    presenter_mock = mocker.patch.object(
        CreateProfessionPresenterInterface,
        "present"
    )
    repository_mock = mocker.patch.object(
        ProfessionRepositoryInterface,
        "create"
    )
    logger_mock = mocker.patch.object(
        LoggerInterface,
        "log_info"
    )
    use_case = create_profession.CreateProfessionUseCase(
        presenter_mock,
        repository_mock,
        logger_mock
    )
    input_dto = CreateProfessionInputDto(
        name="",
        description=fixture_profession_developer["description"]
    )
    with pytest.raises(ValueError) as exception_info:
        use_case.execute(input_dto)
    assert str(exception_info.value) == "Name: empty values not allowed"

    repository_mock.create.assert_not_called()
    presenter_mock.present.assert_not_called()
