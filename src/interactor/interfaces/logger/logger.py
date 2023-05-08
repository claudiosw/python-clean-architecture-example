""" Module provides a logger interface.
"""


from abc import ABC, abstractmethod


class LoggerInterface(ABC):
    """ LoggerInterface class provides an interface for logging.
    """

    @abstractmethod
    def log_debug(self, message: str) -> None:
        """ Log debug message.
        :param message: Message to log.
        """

    @abstractmethod
    def log_info(self, message: str) -> None:
        """ Log info message.
        :param message: Message to log.
        """

    @abstractmethod
    def log_warning(self, message: str) -> None:
        """ Log warning message.
        :param message: Message to log.
        """

    @abstractmethod
    def log_error(self, message: str) -> None:
        """ Log error message.
        :param message: Message to log.
        """

    @abstractmethod
    def log_critical(self, message: str) -> None:
        """ Log critical message.
        :param message: Message to log.
        """
