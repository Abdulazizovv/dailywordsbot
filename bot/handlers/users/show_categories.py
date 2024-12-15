from aiogram import types
from aiogram.dispatcher.filters import Command
from bot.loader import dp
from bot.keyboards.inline.categories import get_categories_keyboard, show_category_keyboard, create_category_keyboard
from bot.utils.requests_ import get_categories, get_public_categories, get_user_categories


CATEGORY_PER_PAGE = 5

@dp.callback_query_handler(text="categories")
async def show_categories(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Choose 👇", reply_markup=show_category_keyboard())


@dp.callback_query_handler(text="all_categories")
async def show_all_categories(call: types.CallbackQuery):
    categories = get_public_categories()
    await call.message.delete()
    if not categories:
        await call.message.answer("There are no public categories yet😔", reply_markup=create_category_keyboard())
        return
    categories_list_text = ""
    for idx, category in enumerate(categories[:CATEGORY_PER_PAGE]):
        categories_list_text += f"{idx+1}. {category['title']} - {category['description']}\n"
    await call.message.answer(f"Public categories\n"
                              f"{categories_list_text}", reply_markup=get_categories_keyboard(categories, per_page=CATEGORY_PER_PAGE))


@dp.callback_query_handler(text="my_categories")
async def show_my_categories(call: types.CallbackQuery):
    await call.message.delete()
    categories = get_user_categories(call.message.from_user.id)[0]['category']
    if not categories:
        await call.message.answer("You don't have any categories yet😔", reply_markup=create_category_keyboard())
        return
    categories_list_text = ""
    for idx, category in enumerate(categories[:CATEGORY_PER_PAGE]):
        categories_list_text += f"{idx+1}. {category['title']} - {category['description']}\n"
    await call.message.answer("Your categories:\n"
                              f"{categories_list_text}", reply_markup=get_categories_keyboard(categories, per_page=CATEGORY_PER_PAGE))


@dp.callback_query_handler(text_startswith="page_")
async def show_page(call: types.CallbackQuery):
    page = int(call.data.split("_")[1])
    categories = get_public_categories()
    categories_list_text = ""
    for category in categories[(page - 1) * CATEGORY_PER_PAGE:page * CATEGORY_PER_PAGE]:
        categories_list_text += f"{category['id']}. {category['title']} - {category['description']}\n"
    await call.message.edit_text(f"Categories| page: {page}👇\n"
                                 f"{categories_list_text}", reply_markup=get_categories_keyboard(categories, page=page, per_page=CATEGORY_PER_PAGE))