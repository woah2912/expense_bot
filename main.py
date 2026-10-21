import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

HELP_TEXT = """Доступные команды:
/start - начать работу
/help - список команд"""

main_kb = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text="➕ Добавить расход"), KeyboardButton(text="📊 Статистика")],
    [KeyboardButton(text="❓ Помощь")],
    ], resize_keyboard=True, input_field_placeholder="Выбери действие",
)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!", reply_markup=main_kb)


@dp.message(F.text == "➕ Добавить расход")
async def add_expenses(message: Message):
    await message.answer("Скоро здесь можно будет добавить расход 🛠")


@dp.message(F.text == "📊 Статистика")
async def show_stats(message: Message):
    await message.answer("Статистика пока пустая 📭")


@dp.message(F.text == "❓ Помощь")
async def button_help(message: Message):
    await message.answer(HELP_TEXT)

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(HELP_TEXT)


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