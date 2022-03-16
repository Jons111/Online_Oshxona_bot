from aiogram import types

from loader import dp
from keyboards.default.taom_nomlari import taomlar_button

# Echo bot
@dp.message_handler(text='Taomlar')
async def bot_echo(message: types.Message):
    await message.answer(text='quyidagi taomlardan tanlang',reply_markup=taomlar_button)