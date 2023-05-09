# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import logging
from src.infra.loggers.logger_default import LoggerDefault


def test_logger_default(mocker):
    mocker.patch.object(logging, 'debug')
    logger = LoggerDefault()
    logger.log_debug('testdebug')
    assert logging.debug.call_once_with('testdebug')  # pylint: disable=E1101

    mocker.patch.object(logging, 'info')
    logger = LoggerDefault()
    logger.log_info('testinfo')
    assert logging.info.call_once_with('testinfo')  # pylint: disable=E1101

    mocker.patch.object(logging, 'warning')
    logger = LoggerDefault()
    logger.log_warning('testwarn')
    assert logging.warning.call_once_with('testwarn')  # pylint: disable=E1101

    mocker.patch.object(logging, 'error')
    logger = LoggerDefault()
    logger.log_error('testerror')
    assert logging.error.call_once_with('testerror')  # pylint: disable=E1101

    mocker.patch.object(logging, 'critical')
    logger = LoggerDefault()
    logger.log_critical('testcrit')
    assert logging.critical.call_once_with('testcrit')  # pylint: disable=E1101
