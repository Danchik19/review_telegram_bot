import logging
from pythonjsonlogger import jsonlogger


# Определение уровней логирования
DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL


def configure_logger(name=None, level=INFO, log_file=None):
    """
    Настройка логгера для использования python-json-logger.

    :param name: Имя логгера.
    :param level: Уровень логирования.
    :param log_file: Путь к файлу для записи логов.
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = jsonlogger.JsonFormatter('%(asctime)s %(name)s %(levelname)s %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
