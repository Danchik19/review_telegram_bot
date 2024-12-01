from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from .join_points import JoinPoints
from ..logger import Logger, DEBUG


class TelegramAdapter:
    def __init__(self, token):
        """
        TelegramAdapter отвечает за интеграцию с Telegram API.
        
        :param token: Токен бота Telegram.
        """

        self.bot = Bot(token=token)
        self.dp = Dispatcher()
        self.join_points = JoinPoints()

        self.dp.message.register(self.cmd_start, Command("start"))
        self.dp.message.register(self.handle_document, F.document)
        self.dp.message.register(self.unknown_command)

        self.logger = Logger(name="TelegramAdapter", level=DEBUG, log_file="telegram_adapter.log")


    async def cmd_start(self, message: types.Message):
        """
        Обработчик команды /start
        """

        await message.answer("Привет! Я бот для проверки проектов. Отправьте мне файл или архив для обработки в форматах: .py или .zip.")


    async def handle_document(self, message: types.Message):
        """
        Обработчик входящих документов
        """

        try:
            document = message.document
            file_content = await self.bot.download(document)

            if document.file_name.endswith(".zip"):
                result_report = self.join_points.process_archive(file_content.read())
                self.logger.info("The archive has been processed")
                r_type = "архив"
            elif document.file_name.endswith(".py"):
                result_report = self.join_points.process_file(file_content.read())
                self.logger.info("The file has been processed")
                r_type = "файл"
            else:
                raise Exception("Поддерживаются только следующие форматы: .py и .zip.")

            await message.answer(f"Ваш {r_type} был обработан, результаты прикреплены к сообщению.")
            report_file = FSInputFile(result_report)
            await self.bot.send_document(chat_id=message.chat.id, document=report_file)

        except Exception as e:
            self.logger.error("Ошибка при обработке документа")
            await message.reply(f"Произошла ошибка: {e}")


    async def unknown_command(self, message: types.Message):
        """
        Обработчик неизвестных команд
        """

        await message.reply("Я не знаю, что делать с этим. Пожалуйста, отправьте мне файл или архив для обработки в форматах: .py или .zip.")


    async def start_polling(self):
        """
        Запуск бота в режиме polling
        """

        await self.dp.start_polling(self.bot)
