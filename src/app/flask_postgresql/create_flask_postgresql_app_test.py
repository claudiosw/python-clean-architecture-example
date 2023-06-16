# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from unittest import mock
import pytest
from src.infra.loggers.logger_default import LoggerDefault
from src.interactor.errors.error_classes import UniqueViolationError


with mock.patch(
    "sqlalchemy.create_engine"
) as mock_create_engine:
    from src.app.flask_postgresql.controllers.create_profession_controller \
        import CreateProfessionController
    from .create_flask_postgresql_app import create_flask_postgresql_app


logger = LoggerDefault()


@pytest.fixture(name="flask_postgresql_app")
def fixture_flask_postgresql_app():
    """ Fixture for flask app with blueprint
    """
    app = create_flask_postgresql_app(logger)
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture(name="client_flask_postgresql_app")
def fixture_client_flask_postgresql_app(flask_postgresql_app):
    """ Fixture to test app_flask_with_blueprint
    """
    return flask_postgresql_app.test_client()


def test_request_profession(
        mocker,
        client_flask_postgresql_app,
        fixture_profession_developer
):
    """ Test request example
    """
    input_data = {
        "name": fixture_profession_developer["name"],
        "description": fixture_profession_developer["description"]
    }
    profession_dict = {
        "profession_id": fixture_profession_developer["profession_id"],
        "name": fixture_profession_developer["name"],
        "description": fixture_profession_developer["description"]
    }
    controller_mock = mocker.patch(
        "src.app.flask_postgresql.blueprints.create_profession_blueprint.\
CreateProfessionController"
    )
    controller_mock.return_value.execute.return_value = profession_dict
    response = client_flask_postgresql_app.post(
        "/v1/profession/",
        json=input_data
    )
    assert response.status_code == 201
    controller_mock.assert_called_once()
    controller_mock.return_value.get_profession_info.assert_called_once_with(
        input_data
    )
    assert b"Developer" in response.data
    assert b"Developer is a person that write software code" in response.data


def test_request_profession_missing_name_error(
        client_flask_postgresql_app,
        fixture_profession_developer
):
    """ Test request example
    """
    input_data = {
        "nam": fixture_profession_developer["name"],
        "description": fixture_profession_developer["description"]
    }
    response = client_flask_postgresql_app.post(
        "/v1/profession/",
        json=input_data
    )
    assert b"Missing Profession Name" in response.data


def test_request_profession_invalid_name_error(
        client_flask_postgresql_app,
        fixture_profession_developer
):
    """ Test request invalid name
    """
    input_data = {
        "name": "Profession",
        "description": fixture_profession_developer["description"]
    }
    response = client_flask_postgresql_app.post(
        "/v1/profession/",
        json=input_data
    )
    assert b"Name: Profession is not permitted" in response.data
    assert response.status_code == 400


def test_request_profession_wrong_url_error(
        client_flask_postgresql_app,
        fixture_profession_developer
):
    """ Test request HTTPException error
    """
    input_data = {
        "name": fixture_profession_developer["name"],
        "description": fixture_profession_developer["description"]
    }
    response = client_flask_postgresql_app.post(
        "/v1/professio/",
        json=input_data
    )
    assert b"The requested URL was not found on the server" in response.data
    assert response.status_code == 404


def test_request_profession_unique_error(
        client_flask_postgresql_app,
        fixture_profession_developer,
        mocker
):
    """ Test handling of unique exception (UniqueViolationError)
    """
    blueprint_mock = mocker.patch.object(
        CreateProfessionController,
        "execute"
    )
    blueprint_mock.side_effect = UniqueViolationError("Unique error!")
    input_data = {
        "name": fixture_profession_developer["name"],
        "description": fixture_profession_developer["description"]
    }
    response = client_flask_postgresql_app.post(
        "/v1/profession/",
        json=input_data
    )
    assert b"Unique error!" in response.data
    assert b'"status_code":409' in response.data
    assert response.status_code == 409


def test_request_profession_500_status_code(
        client_flask_postgresql_app,
        fixture_profession_developer,
        mocker
):
    """ Test handling of exception that should return a 500 status code
    """
    blueprint_mock = mocker.patch.object(
        CreateProfessionController,
        "get_profession_info"
    )
    blueprint_mock.side_effect = Exception('Unexpected error!')
    input_data = {
        "name": fixture_profession_developer["name"],
        "description": fixture_profession_developer["description"]
    }
    response = client_flask_postgresql_app.post(
        "/v1/profession/",
        json=input_data
    )
    assert b'"status_code":500' in response.data
    assert response.status_code == 500
