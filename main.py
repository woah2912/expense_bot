import asyncio
import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('''Доступные команды:
/start - начать работу
/help - список команд
''')


@dp.message()
async def echo(message: Message):
    if message.text is None:
        await message.answer('Я понимаю только текст')
    else:
        await message.answer(message.text)

async def main():
    bot = Bot(token = TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())