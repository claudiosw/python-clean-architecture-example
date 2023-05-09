""" Module for LoggerDefault class."""


import logging
from src.interactor.interfaces.logger.logger import LoggerInterface


class LoggerDefault(LoggerInterface):
    """ LoggerDefault class.
    """

    def __init__(self):
        logging.basicConfig(
            filename='app.log',
            filemode='a',
            format='%(asctime)-s - %(name)s - %(levelname)s - %(message)s'
        )

    def log_debug(self, message: str) -> None:
        """ Log debug message.
        :param message: Message to log.
        """
        logging.debug(message)

    def log_info(self, message: str) -> None:
        """ Log info message.
        :param message: Message to log.
        """
        logging.info(message)

    def log_warning(self, message: str) -> None:
        """ Log warning message.
        :param message: Message to log.
        """
        logging.warning(message)

    def log_error(self, message: str) -> None:
        """ Log error message.
        :param message: Message to log.
        """
        logging.error(message)

    def log_critical(self, message: str) -> None:
        """ Log critical message.
        :param message: Message to log.
        """
        logging.critical(message)
