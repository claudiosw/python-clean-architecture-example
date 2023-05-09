"""Create Profession Controller Module"""


from src.interactor.use_cases.create_profession import CreateProfessionUseCase
from src.infra.repositories.profession_in_memory_repository \
    import ProfessionInMemoryRepository
from src.interactor.dtos.create_profession_dtos import CreateProfessionInputDto
from src.app.cli_memory.interfaces.cli_memory_controller_interface \
    import CliMemoryControllerInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from ..presenters.create_profession_presenter import CreateProfessionPresenter
from ..views.create_profession_view import CreateProfessionView


class CreateProfessionController(CliMemoryControllerInterface):
    """ Create Profession Controller Class
    """
    def __init__(self, logger: LoggerInterface):
        self.logger = logger

    def _get_profession_info(self) -> CreateProfessionInputDto:
        name = input("Enter the profession name:")
        description = input("Enter the profession description:")
        return CreateProfessionInputDto(name, description)

    def execute(self):
        """ Execute the create profession controller
        """
        repository = ProfessionInMemoryRepository()
        presenter = CreateProfessionPresenter()
        input_dto = self._get_profession_info()
        use_case = CreateProfessionUseCase(presenter, repository, self.logger)
        result = use_case.execute(input_dto)
        view = CreateProfessionView()
        view.show(result)
