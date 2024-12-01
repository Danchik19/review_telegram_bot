from ...application.etl.services import ModelService
from ..logger import Logger, DEBUG


class JoinPoints:
    def __init__(self):
        """
        Инициализация всех сервисов, которые будут использоваться.
        """

        self.model_service = ModelService()
        self.model_service.load_model()

        self.logger = Logger(name="JoinPoints", level=DEBUG, log_file="join_points.log")


    def create_report(report_path, contents):
        """
        Функция для создания файла репорта.
        """

        with open(report_path, "w") as file:
            file.write(contents)
        return report_path


    def process_file(self, file_content: bytes) -> str:
        """
        Обработка одиночного файла через сервис.
        """

        prompt = file_content.decode("utf-8")
        model_result = self.model_service.generate_text(prompt)
        self.logger.info("Processing file...")
        report = self.create_report("report.md", model_result)
        return report


    def process_archive(self, archive_content: bytes) -> str:
        """
        Обработка архива (пример обработки нескольких файлов внутри).
        """

        model_result = self.model_service.process_multiple_files(archive_content)
        self.logger.info("Processing archive...")
        report = self.create_report("report.md", model_result)
        return report
