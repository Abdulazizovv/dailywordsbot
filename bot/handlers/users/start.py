from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.loader import dp
from bot.keyboards.inline import main_menu_kb as menu_kb
from bot.utils.requests_ import create_user


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    # creating user if not exists
    # if user exists return user
    user = create_user(
        {
        "user_id":message.from_user.id,
        "username":message.from_user.username,
        "first_name":message.from_user.first_name,
        "last_name":message.from_user.last_name
        }
    )

    if not user:
        return await message.answer("Nimadir xato ketdi. Iltimos qaytadan urinib ko'ring /start buyrug'ini bosing.")
    # salomlashish xabari
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\n"
                         "Siz bosh menyudasiz!", reply_markup=menu_kb)



