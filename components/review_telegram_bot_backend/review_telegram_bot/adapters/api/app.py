import io
from zipfile import ZipFile
from ..logger import Logger, DEBUG


logger = Logger(name="App", level=DEBUG, log_file="app.log")


def create_report(report_path, contents):
    """
    Функция для создания файла репорта.
    """

    with open(report_path, "w") as file:
        file.write(contents)
    return report_path


def process_file(file) -> str:
    """
    Функция для обработки файлов и создания репортов.
    """

    logger.info("Processing file...")
    report = create_report("report.md", "Твой файл идеален!")
    return report


def process_archive(zip_file) -> str:
    """
    Функция для обработки архивов и создания репортов.
    """

    with ZipFile(io.BytesIO(zip_file), "r") as archive:
        for file in archive.namelist():
            with archive.open(file) as nested_file:
                file_contents = nested_file.readlines()

    logger.info("Processing archive...")
    report = create_report("report.md", "Твой архив идеален!")
    return report
