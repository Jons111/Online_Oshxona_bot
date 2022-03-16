from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Taomlar',callback_data='menu1'),
            InlineKeyboardButton(text='Ichimliklar', callback_data='menu2')
        ],
        [
            InlineKeyboardButton(text='Shirinliklar',callback_data='menu3'),
            InlineKeyboardButton(text='Ulashish',switch_inline_query="Zo'r bot ekan"),
            InlineKeyboardButton('Xamkorlarimiz',url='https://t.me/UstozShogird')

        ]
    ]
)