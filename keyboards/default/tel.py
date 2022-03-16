from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

tel_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Kontakt',request_contact=True),
            KeyboardButton(text='Lokatsiya', request_location=True),

        ],

    ],
    resize_keyboard=True
)