from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.loader import dp
from bot.utils.db_api import add_bot_user
from asgiref.sync import sync_to_async


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await sync_to_async(add_bot_user)(
        user_id=message.from_user.id, 
        first_name=message.from_user.first_name, 
        last_name=message.from_user.last_name,
        username=message.from_user.username
        )
    # salomlashish xabari
    await message.answer(f"Salom, {message.from_user.id}!")



