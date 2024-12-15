from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


categories_cd = CallbackData("show_category", "category_id")


def get_categories_keyboard(categories: object, page: int = 1, per_page: int = 3) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=4)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_categories = categories[start:end]

    for idx, category in enumerate(paginated_categories, start=start + 1):
        button = InlineKeyboardButton(
            text=str(idx),
            callback_data=categories_cd.new(category_id=category['id'])
        )
        keyboard.insert(button)

    navigation_buttons = []
    if page > 1:
        navigation_buttons.append(InlineKeyboardButton(
            text="⬅️",
            callback_data=f"page_{page - 1}"
        ))

    if end < len(categories):
        navigation_buttons.append(InlineKeyboardButton(
            text="➡️",
            callback_data=f"page_{page + 1}"
        ))

    if navigation_buttons:
        keyboard.row(*navigation_buttons)
    
    keyboard.row(
        InlineKeyboardButton(
            text="Back🔙",
            callback_data="categories"
        )
    )

    return keyboard


def show_category_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="All categories", callback_data="all_categories"),
            ],
            [
                InlineKeyboardButton(text="My categories", callback_data="my_categories"),
            ]
        ]
    )
    return keyboard


def create_category_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Create new public category📦", callback_data="create_public_category"),
            ],
            [
                InlineKeyboardButton(text="Create new private category📦", callback_data="create_private_category"),
            ],
            [
                InlineKeyboardButton(text="Back🔙", callback_data="categories"),
            ]
        ]
    )
    return keyboard