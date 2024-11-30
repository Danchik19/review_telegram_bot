import io
from zipfile import ZipFile
from decouple import config
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile


# Загрузка конфигурации из .env файла
TOKEN = config("TELEGRAM_TOKEN")


def create_report(report_path, contents):
    """
    Функция для создания файла репорта
    """

    with open(report_path, "w") as file:
        file.write(contents)
    return report_path


def process_file(file) -> str:
    """
    Функция для обработки файлов и создания репортов
    """

    print("Processing file...")
    report = create_report("report.txt", "Hello world")
    return report


def process_archive(zip_file) -> str:
    """
    Функция для обработки архивов и создания репортов
    """

    with ZipFile(io.BytesIO(zip_file), "r") as archive:
        for file in archive.namelist():
            with archive.open(file) as nested_file:
                file_contents = nested_file.readlines()

    report = create_report("report.txt", "Hello world")
    return report


# Создание бота и обработка сообщений
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.document)
async def handle_document(message: types.Message):
    try:
        document = message.document
        file_content = await bot.download(document)

        if document.file_name.endswith(".zip"):
            result_report = process_archive(file_content.read())
            r_type = "архив"
        else:
            result_report = process_file(file_content.read())
            r_type = "файл"

        await message.answer(f"Ваш {r_type} был обработан, результаты прикреплены к сообщению.")
        report_file = FSInputFile(result_report)
        await bot.send_document(chat_id=message.chat.id, document=report_file)

    except Exception as e:
        await message.reply(f"Произошла ошибка, попробуйте снова: {e}")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот для проверки проектов. Отправьте мне файл или архив для обработки.")


@dp.message()
async def unknown_command(message: types.Message):
    await message.reply("Я не знаю, что делать с этим. Пожалуйста, отправьте мне файл или архив для обработки.")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Bot started")
    asyncio.run(main())
