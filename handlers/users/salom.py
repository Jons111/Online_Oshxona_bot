from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(text='salom')
async def bot_echo(message: types.Message):
    await message.answer(text='Assalomu alaykum botga hush kelibsiz')