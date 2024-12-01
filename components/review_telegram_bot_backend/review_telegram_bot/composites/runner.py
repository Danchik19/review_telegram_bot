import asyncio
from ..adapters.api import Settings, TelegramAdapter
from ..adapters.logger import Logger, DEBUG


class BotComposite:
    def __init__(self):
        """
        BotComposite загружает настройки, инициализирует адаптер Telegram и логгер
        """

        self.settings = Settings()
        
        self.telegram_adapter = TelegramAdapter(
            token=self.settings.telegram_token          
        )

        self.logger = Logger(name="BotComposite", level=DEBUG, log_file="bot_composite.log")
    

    async def run(self):
        """
        Запуск Telegram бота
        """

        self.logger.info("Bot started")
        await self.telegram_adapter.start_polling()


def main():
    composite = BotComposite()
    asyncio.run(composite.run())


if __name__ == "__main__":
    main()
