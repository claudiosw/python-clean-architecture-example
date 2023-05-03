""" This module contains the ProcessHandler for Cli that uses Memory repository
"""


from src.app.cli_memory.interfaces.cli_memory_controller_interface \
    import CliMemoryControllerInterface
from src.app.cli_memory.controllers.exit_controller \
    import ExitController
from src.app.cli_memory.controllers.create_profession_controller \
    import CreateProfessionController


class CliMemoryProcessHandler:
    """ The ProcessHandler for Cli that uses Memory repository
    """
    def __init__(self):
        self.options = {}

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
                option.execute()
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    process = CliMemoryProcessHandler()
    process.add_option("0", ExitController())
    process.add_option("1", CreateProfessionController())
    process.execute()
