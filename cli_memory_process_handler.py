""" This module contains the ProcessHandler for Cli that uses Memory repository
"""


from typing import Dict
from src.app.cli_memory.interfaces.cli_memory_controller_interface \
    import CliMemoryControllerInterface
from src.app.cli_memory.controllers.exit_controller \
    import ExitController
from src.app.cli_memory.controllers.create_profession_controller \
    import CreateProfessionController
from src.interactor.errors.error_classes import FieldValueNotPermittedException
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.infra.loggers.logger_default import LoggerDefault


class CliMemoryProcessHandler:
    """ The ProcessHandler for Cli that uses Memory repository
    """
    def __init__(self, logger: LoggerInterface) -> None:
        self.logger = logger
        self.options: Dict = {}

    def add_option(
        self,
        option: str,
        controller: CliMemoryControllerInterface
    ) -> None:
        """ Add an option to the ProcessHandler
        :param option: The option
        :param controller: The controller for the option
        :return: None
        """
        self.options[option] = controller

    def show_options(self):
        """ Print  the options to the ProcessHandler
        :return: None
        """
        for option, controller in self.options.items():
            print(f"{option}: {controller.__class__.__name__}")

    def execute(self) -> None:
        """ Execute the ProcessHandler
        :return: None
        """
        while True:
            print("Please choose an option:")
            self.show_options()
            choice = input("> ")
            option = self.options.get(choice)
            if option:
                try:
                    option.execute()
                except (
                    ValueError,
                    FieldValueNotPermittedException
                ) as exception:
                    print(f'\nERROR: {str(exception)}\n')
                    self.logger.log_error(str(exception))
            else:
                print("Invalid choice.")
                self.logger.log_info(f"Invalid user choice: {option}")


if __name__ == "__main__":
    logger_default = LoggerDefault()
    process = CliMemoryProcessHandler(logger_default)
    process.add_option("0", ExitController())
    process.add_option("1", CreateProfessionController(logger_default))
    process.execute()
