from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

taomlar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Osh'),
            KeyboardButton(text="Shorva")
        ],
        [
            KeyboardButton(text='Kabob'),
            KeyboardButton(text="Admin")
        ]
    ],
    resize_keyboard=True
)