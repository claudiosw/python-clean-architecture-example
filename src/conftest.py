# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import uuid
import pytest


@pytest.fixture
def fixture_profession_developer():
    """ Fixture with Profession example """
    return {
        "profession_id": uuid.uuid4(),
        "name": "Developer - Test",
        "description": "Developer is a person that write software code. This \
        professional needs to know at least one programming language."
    }
