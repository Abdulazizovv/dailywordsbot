from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton


main_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📋 Words", callback_data="words"),
            InlineKeyboardButton(text="📝 Add word", callback_data="add_word")
        ],
        [
            InlineKeyboardButton(text="📦 Categories", callback_data="categories"),
            InlineKeyboardButton(text="📦 Add Category", callback_data="add_category")
        ],
        [
            InlineKeyboardButton(text="📊 Statistics", callback_data="statistics")
        ]
    ]
)