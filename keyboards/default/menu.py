from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

asosiy_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Taomlar'),
            KeyboardButton(text="Ichimliklar")
        ],
        [
            KeyboardButton(text='Shirinliklar'),
            KeyboardButton(text="Admin")
        ]
    ],
    resize_keyboard=True
)