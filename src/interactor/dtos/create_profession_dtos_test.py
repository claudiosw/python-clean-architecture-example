# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from .create_profession_dtos import CreateProfessionInputDto


def test_create_profession_input_dto_valid(fixture_profession_developer):
    input_dto = CreateProfessionInputDto(
        name=fixture_profession_developer["name"],
        description=fixture_profession_developer["description"]
    )
    assert input_dto.name == fixture_profession_developer["name"]
    assert input_dto.description == fixture_profession_developer["description"]
    assert input_dto.to_dict() == {
        "name": fixture_profession_developer["name"],
        "description": fixture_profession_developer["description"]
    }
