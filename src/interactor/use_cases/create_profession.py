""" This module is responsible for creating a new profession.
"""


from typing import Dict
from src.interactor.dtos.create_profession_dtos \
    import CreateProfessionInputDto, CreateProfessionOutputDto
from src.interactor.interfaces.presenters.create_profession_presenter \
    import CreateProfessionPresenterInterface
from src.interactor.interfaces.repositories.profession_repository \
    import ProfessionRepositoryInterface
from src.interactor.validations.create_profession_validator \
    import CreateProfessionInputDtoValidator
from src.interactor.interfaces.logger.logger import LoggerInterface


class CreateProfessionUseCase():
    """ This class is responsible for creating a new profession.
    """

    def __init__(
            self,
            presenter: CreateProfessionPresenterInterface,
            repository: ProfessionRepositoryInterface,
            logger: LoggerInterface
    ):
        self.presenter = presenter
        self.repository = repository
        self.logger = logger

    def execute(
            self,
            input_dto: CreateProfessionInputDto
    ) -> Dict:
        """ This method is responsible for creating a new profession.
        :param input_dto: The input data transfer object.
        :type input_dto: CreateProfessionInputDto
        :return: Dict
        """

        validator = CreateProfessionInputDtoValidator(input_dto.to_dict())
        validator.validate()
        profession = self.repository.create(
            input_dto.name,
            input_dto.description
        )
        output_dto = CreateProfessionOutputDto(profession)
        presenter_response = self.presenter.present(output_dto)
        self.logger.log_info("Profession created successfully")
        return presenter_response
