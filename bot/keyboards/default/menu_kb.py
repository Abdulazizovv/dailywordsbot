from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="📝 Add new word"),
            KeyboardButton(text="✏️ Edit word")
        ],
        [
            KeyboardButton(text="🔍 Search word"),
            KeyboardButton(text="📖 All words")
        ],
        [
            KeyboardButton(text="📊 Statistics"),
        ]
    ]
)