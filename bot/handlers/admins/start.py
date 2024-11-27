from aiogram import types
from bot.loader import dp
from bot.filters import IsAdmin
from aiogram.dispatcher.filters import Command
from bot.keyboards.inline.main_menu import main_menu_kb


@dp.message_handler(Command("start"), IsAdmin())
async def bot_start(message: types.Message):
    await message.answer(f"Hello {message.from_user.full_name}\n", reply_markup=main_menu_kb)

