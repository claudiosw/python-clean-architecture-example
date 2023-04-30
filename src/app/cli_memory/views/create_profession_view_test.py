# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from .create_profession_view import CreateProfessionView


def test_create_profession_presenter(capsys, fixture_profession_developer):
    profession_dict = {
        "profession_id": fixture_profession_developer["profession_id"],
        "name": fixture_profession_developer["name"],
        "description": fixture_profession_developer["description"]
    }
    view = CreateProfessionView()
    view.show(profession_dict)
    captured = capsys.readouterr()
    assert captured.out == str(profession_dict) + "\n"
