from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


cancel_creating_category_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Cancel creating category❌")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)