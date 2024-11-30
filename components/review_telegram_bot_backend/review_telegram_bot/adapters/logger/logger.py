from .settings import configure_logger, DEBUG, INFO, WARNING, ERROR, CRITICAL


class Logger:
    def __init__(self, name=None, level=INFO, log_file=None):
        """
        Инициализация логгера.

        :param name: Имя логгера.
        :param level: Уровень логирования.
        :param log_file: Путь к файлу для записи логов.
        """
        self.logger = configure_logger(name, level, log_file)


    def debug(self, message):
        """
        Запись сообщения уровня DEBUG
        """

        self.logger.debug(message)


    def info(self, message):
        """
        Запись сообщения уровня INFO
        """

        self.logger.info(message)


    def warning(self, message):
        """
        Запись сообщения уровня WARNING
        """

        self.logger.warning(message)


    def error(self, message):
        """
        Запись сообщения уровня ERROR
        """

        self.logger.error(message)


    def critical(self, message):
        """
        Запись сообщения уровня CRITICAL
        """
        
        self.logger.critical(message)
