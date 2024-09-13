from aiogram import types
from bot.loader import dp
from bot.filters import IsAdmin
from aiogram.dispatcher.filters import Command
from bot.keyboards.default import menu_kb


@dp.message_handler(Command("start"), IsAdmin())
async def bot_start(message: types.Message):
    await message.answer("Hello, Admin!", reply_markup=menu_kb)

