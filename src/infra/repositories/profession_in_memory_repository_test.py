# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from src.domain.entities.profession import Profession
from .profession_in_memory_repository import ProfessionInMemoryRepository


def test_profession_in_memory_repository(fixture_profession_developer):
    repository = ProfessionInMemoryRepository()
    profession = repository.create(
        fixture_profession_developer["name"],
        fixture_profession_developer["description"]
    )
    response = repository.get(profession.profession_id)
    assert response.name == fixture_profession_developer["name"]
    assert response.description == fixture_profession_developer["description"]
    new_profession = Profession(
        profession.profession_id,
        "new name",
        "new description"
    )
    response_update = repository.update(new_profession)
    assert response_update.name == "new name"
    assert response_update.description == "new description"
