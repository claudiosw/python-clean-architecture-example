# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from src.app.cli_memory.controllers.create_profession_controller \
    import CreateProfessionController
from src.interactor.dtos.create_profession_dtos import CreateProfessionInputDto


def test_create_profession(monkeypatch, mocker, fixture_profession_developer):
    name = fixture_profession_developer["name"]
    description = fixture_profession_developer["description"]
    fake_user_inputs = iter([name, description])
    monkeypatch.setattr('builtins.input', lambda _: next(fake_user_inputs))

    mock_repository = mocker.patch(
        'src.app.cli_memory.controllers.create_profession_controller.\
ProfessionInMemoryRepository')
    mock_presenter = mocker.patch(
        'src.app.cli_memory.controllers.create_profession_controller.\
CreateProfessionPresenter')
    mock_use_case = mocker.patch(
        'src.app.cli_memory.controllers.create_profession_controller.\
CreateProfessionUseCase')
    mock_use_case_instance = mock_use_case.return_value
    mock_view = mocker.patch(
        'src.app.cli_memory.controllers.create_profession_controller.\
CreateProfessionView')
    result_use_case = {
        "profession_id": fixture_profession_developer["profession_id"],
        "name": fixture_profession_developer["name"],
        "description": fixture_profession_developer["description"]
    }
    mock_use_case_instance.execute.return_value = result_use_case
    mock_view_instance = mock_view.return_value

    controller = CreateProfessionController()
    controller.execute()

    mock_repository.assert_called_once_with()
    mock_presenter.assert_called_once_with()
    mock_use_case.assert_called_once_with(
        mock_presenter.return_value,
        mock_repository.return_value)
    input_dto = CreateProfessionInputDto(name, description)
    mock_use_case_instance.execute.assert_called_once_with(input_dto)
    mock_view_instance.show.assert_called_once_with(result_use_case)
