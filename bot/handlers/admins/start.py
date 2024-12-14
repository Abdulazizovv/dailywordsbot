from aiogram import types
from bot.loader import dp
from bot.filters import IsAdmin
from aiogram.dispatcher.filters import Command
from bot.keyboards.inline.main_menu import main_menu_kb
from bot.utils.requests_ import create_user


@dp.message_handler(Command("start"), IsAdmin())
async def bot_start(message: types.Message):
    
    create_user(
        {
        "user_id":message.from_user.id,
        "username":message.from_user.username,
        "first_name":message.from_user.first_name,
        "last_name":message.from_user.last_name
        }
    )
    
    await message.answer(f"Hello {message.from_user.full_name}\n", reply_markup=main_menu_kb)

