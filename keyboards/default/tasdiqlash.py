from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tasdiq_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Tasdiqlash', ),
            KeyboardButton(text='Bekor qilish', ),

        ],

    ],
    resize_keyboard=True
)