from aiogram import types
from bot.loader import dp
from bot.keyboards.inline import main_menu_kb as main_kb
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="Cancel creating category❌", state="*")
async def cancel_creating_category(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Creating category was canceled❌", reply_markup=main_kb)
