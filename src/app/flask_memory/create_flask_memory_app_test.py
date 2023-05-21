# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import pytest
from src.infra.loggers.logger_default import LoggerDefault
from src.app.flask_memory.controllers.create_profession_controller import \
    CreateProfessionController
from .create_flask_memory_app import create_flask_memory_app


logger = LoggerDefault()


@pytest.fixture(name="app_flask_memory_app")
def fixture_app_flask_memory_app():
    """ Fixture for flask app with blueprint
    """
    app = create_flask_memory_app(logger)
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture(name="client_flask_memory_app")
def fixture_client_flask_memory_app(app_flask_memory_app):
    """ Fixture to test app_flask_with_blueprint
    """
    return app_flask_memory_app.test_client()


def test_request_profession(
        client_flask_memory_app,
        fixture_profession_developer
):
    """ Test request example
    """
    input_data = {
        "name": fixture_profession_developer["name"],
        "description": fixture_profession_developer["description"]
    }
    response = client_flask_memory_app.post("/v1/profession/", json=input_data)
    assert b"Developer" in response.data
    assert b"Developer is a person that write software code" in response.data


def test_request_profession_missing_name_error(
        client_flask_memory_app,
        fixture_profession_developer
):
    """ Test request example
    """
    input_data = {
        "nam": fixture_profession_developer["name"],
        "description": fixture_profession_developer["description"]
    }
    response = client_flask_memory_app.post("/v1/profession/", json=input_data)
    assert b"Missing Profession Name" in response.data


def test_request_profession_invalid_name_error(
        client_flask_memory_app,
        fixture_profession_developer
):
    """ Test request invalid name
    """
    input_data = {
        "name": "Profession",
        "description": fixture_profession_developer["description"]
    }
    response = client_flask_memory_app.post("/v1/profession/", json=input_data)
    assert b"Name: Profession is not permitted" in response.data


def test_request_profession_wrong_url_error(
        client_flask_memory_app,
        fixture_profession_developer
):
    """ Test request HTTPException error
    """
    input_data = {
        "name": fixture_profession_developer["name"],
        "description": fixture_profession_developer["description"]
    }
    response = client_flask_memory_app.post("/v1/professio/", json=input_data)
    assert b"The requested URL was not found on the server" in response.data


def test_request_profession_500_status_code(
        client_flask_memory_app,
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
    response = client_flask_memory_app.post("/v1/profession/", json=input_data)
    assert b'"status_code":500' in response.data
