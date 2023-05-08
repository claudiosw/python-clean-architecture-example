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


class CreateProfessionUseCase():
    """ This class is responsible for creating a new profession.
    """

    def __init__(
            self,
            presenter: CreateProfessionPresenterInterface,
            repository: ProfessionRepositoryInterface
    ):
        self.presenter = presenter
        self.repository = repository

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
        return self.presenter.present(output_dto)
