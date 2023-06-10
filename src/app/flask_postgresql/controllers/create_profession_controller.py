"""Create Profession Controller Module"""


from typing import Dict
from src.interactor.use_cases.create_profession import CreateProfessionUseCase
from src.infra.repositories.profession_postgresql_repository \
    import ProfessionPostgresqlRepository
from src.interactor.dtos.create_profession_dtos import CreateProfessionInputDto
from src.app.flask_postgresql.interfaces.flask_postgresql_controller_interface\
    import FlaskPostgresqlControllerInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.app.flask_postgresql.presenters.create_profession_presenter import \
    CreateProfessionPresenter


class CreateProfessionController(FlaskPostgresqlControllerInterface):
    """ Create Profession Controller Class
    """
    def __init__(self, logger: LoggerInterface):
        self.logger = logger
        self.input_dto: CreateProfessionInputDto

    def get_profession_info(self, json_input) -> None:
        """ Get Profession Info
        :param json_input: Input data
        :raises: ValueError if profession name or description are missing.
        """
        if "name" in json_input:
            name = json_input["name"]
        else:
            raise ValueError("Missing Profession Name")
        if "description" in json_input:
            description = json_input["description"]
        else:
            raise ValueError("Missing Profession Description")
        self.input_dto = CreateProfessionInputDto(name, description)

    def execute(self) -> Dict:
        """ Execute the create profession controller
        :returns: Profession created
        """
        repository = ProfessionPostgresqlRepository()
        presenter = CreateProfessionPresenter()
        use_case = CreateProfessionUseCase(presenter, repository, self.logger)
        result = use_case.execute(self.input_dto)
        return result
