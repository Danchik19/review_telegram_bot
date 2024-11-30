# Review Telegram Bot

## Описание

Review Telegram Bot — это проект, который предоставляет инфраструктуру для интеграции с Telegram API и обработки файлов и архивов.

## Установка

1. **Клонируйте репозиторий**:

   ```sh
   git clone https://github.com/Danchik19/review_telegram_bot.git
   cd review_telegram_bot

   ```

2. **Создайте виртуальное окружение**:

   ```sh
   python -m venv env
   source env/bin/activate  # Для Windows: env\Scripts\activate

   ```

3. **Установите пакет**:
   ```sh
   cd components/review_telegram_bot_backend
   pip install .
   ```

## Использование

1. **Создайте файл конфигурации**:

   Создайте файл .env в корневой директории проекта и добавьте туда необходимые переменные окружения, например:

   ```sh
   TELEGRAM_TOKEN=your_telegram_token_here

   ```

2. **Запустите бота**:
   ```sh
   review_telegram_bot.exe
   ```
