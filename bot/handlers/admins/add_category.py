from aiogram import types
from bot.loader import dp
from bot.states.category_state import CategoryState
from bot.utils.db_api import add_category_db
from aiogram.dispatcher import FSMContext
from asgiref.sync import sync_to_async


@dp.callback_query_handler(text="add_category")
async def add_category(call: types.CallbackQuery):
    await call.message.answer("Please enter the name of the category")
    await CategoryState.title.set()


@dp.message_handler(state=CategoryState.title, content_types=['text'])
async def get_category_title(message: types.Message, state: FSMContext):
    title = message.text
    await state.update_data(title=title)
    await CategoryState.description.set()
    await message.answer("Please enter the description of the category")


@dp.message_handler(state=CategoryState.description, content_types=['text'])
async def get_category_description(message: types.Message, state: FSMContext):
    description = message.text
    data = await state.get_data()
    title = data.get("title")
    if await sync_to_async(add_category_db)(
        title=title,
        description=description,
        author_id=message.from_user.id
    ):
        await message.answer("Category added successfully")
        await state.finish()
    else:
        await message.answer("An error occurred while adding the category")
        await state.finish()

