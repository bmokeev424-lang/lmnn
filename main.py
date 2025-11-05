import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher  # Исправлена опечатка "aicgram"
from handlers import common, knb, kub, book

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("Токен не найден! Убедитесь, что BOT_TOKEN указан в .env")

async def main() -> None:
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # ИСПРАВЛЕНО: убрали дублирование knb.router и добавили kub.router
    dp.include_router(kub.router)  # Добавляем роутер кубика
    dp.include_router(knb.router)
    dp.include_router(book.router)
    dp.include_router(common.router)

    print("Бот запущен! Нажмите Ctrl+C для остановки.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен.")