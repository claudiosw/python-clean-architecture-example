# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import pytest
from src.app.flask_memory.controllers.create_profession_controller \
    import CreateProfessionController
from src.interactor.dtos.create_profession_dtos import CreateProfessionInputDto
from src.interactor.interfaces.logger.logger import LoggerInterface


def test_create_profession(monkeypatch, mocker, fixture_profession_developer):
    name = fixture_profession_developer["name"]
    description = fixture_profession_developer["description"]
    fake_user_inputs = {
        "name": name,
        "description": description
    }
    monkeypatch.setattr('builtins.input', lambda _: next(fake_user_inputs))

    mock_repository = mocker.patch(
        'src.app.flask_memory.controllers.create_profession_controller.\
ProfessionInMemoryRepository')
    mock_presenter = mocker.patch(
        'src.app.flask_memory.controllers.create_profession_controller.\
CreateProfessionPresenter')
    mock_use_case = mocker.patch(
        'src.app.flask_memory.controllers.create_profession_controller.\
CreateProfessionUseCase')
    mock_use_case_instance = mock_use_case.return_value
    logger_mock = mocker.patch.object(
        LoggerInterface,
        "log_info"
    )
    result_use_case = {
        "profession_id": fixture_profession_developer["profession_id"],
        "name": fixture_profession_developer["name"],
        "description": fixture_profession_developer["description"]
    }
    mock_use_case_instance.execute.return_value = result_use_case

    controller = CreateProfessionController(logger_mock)
    controller.get_profession_info(fake_user_inputs)
    result = controller.execute()

    mock_repository.assert_called_once_with()
    mock_presenter.assert_called_once_with()
    mock_use_case.assert_called_once_with(
        mock_presenter.return_value,
        mock_repository.return_value,
        logger_mock
    )
    input_dto = CreateProfessionInputDto(name, description)
    mock_use_case_instance.execute.assert_called_once_with(input_dto)
    assert result["name"] == name
    assert result["description"] == description

    # Test for missing inputs (name)
    fake_user_inputs = {
        "nam": name,
        "description": description
    }
    with pytest.raises(ValueError) as exception_info:
        controller.get_profession_info(fake_user_inputs)
    assert str(exception_info.value) == "Missing Profession Name"

    # Test for missing inputs (description)
    fake_user_inputs = {
        "name": name,
        "descriptio": description
    }
    with pytest.raises(ValueError) as exception_info:
        controller.get_profession_info(fake_user_inputs)
    assert str(exception_info.value) == "Missing Profession Description"
