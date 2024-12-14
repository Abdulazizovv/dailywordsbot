from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from bot.loader import dp
from bot.utils.requests_ import create_category
from bot.keyboards.default.cancel_creating_category_kb import cancel_creating_category_btn as cancel_btn


@dp.message_handler(Command("create_category"), state="*")
@dp.callback_query_handler(text="create_category", state="*")
async def add_category(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Enter the title of the category", reply_markup=cancel_btn)
    await state.set_state("add_category:title")


@dp.message_handler(state="add_category:title")
async def add_category_title(message: types.Message, state: FSMContext):
    title = message.text
    await state.update_data(title=title)
    await message.answer("Enter the description of the category")
    await state.set_state("add_category:description")


@dp.message_handler(state="add_category:description")
async def add_category_description(message: types.Message, state: FSMContext):
    description = message.text
    data = await state.get_data()
    title = data.get("title")
    user_id = message.from_user.id
    response = create_category(
        {
            "user_id": user_id,
            "title": title,
            "description": description
        }
    )
    if response:
        await message.answer("Category created successfully")
    else:
        await message.answer("Failed to create category")
    await state.finish()

    
    