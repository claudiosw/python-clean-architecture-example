# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from .profession import Profession


def test_profession_creation(fixture_profession_developer):
    profession = Profession(
        profession_id=fixture_profession_developer["profession_id"],
        name=fixture_profession_developer["name"],
        description=fixture_profession_developer["description"]
    )
    assert profession.name == fixture_profession_developer["name"]
    assert (profession.description
            == fixture_profession_developer["description"])


def test_profession_from_dict(fixture_profession_developer):
    profession = Profession.from_dict(fixture_profession_developer)
    assert profession.name == fixture_profession_developer["name"]
    assert (profession.description
            == fixture_profession_developer["description"])


def test_profession_to_dict(fixture_profession_developer):
    profession = Profession.from_dict(fixture_profession_developer)
    assert profession.to_dict() == fixture_profession_developer


def test_profession_comparison(fixture_profession_developer):
    profession_1 = Profession.from_dict(fixture_profession_developer)
    profession_2 = Profession.from_dict(fixture_profession_developer)
    assert profession_1 == profession_2
