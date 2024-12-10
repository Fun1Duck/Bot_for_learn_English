import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN as token
from handlers import router


logging.basicConfig(level=logging.INFO)

dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)

bot = Bot(token=token)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())