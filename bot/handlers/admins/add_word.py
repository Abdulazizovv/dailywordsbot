from aiogram import types
from bot.loader import dp
from aiogram.dispatcher.filters import Command
from bot.filters.is_admin import IsAdmin


@dp.message_handler(Command("/add_word"), IsAdmin())
@dp.message_handler(text="📝 Add new word")
def add_word(message: types.Message):
    pass