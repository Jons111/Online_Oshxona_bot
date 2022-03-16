from aiogram import types

from loader import dp
from googletrans import Translator

tarjimon = Translator()
@dp.message_handler()
async def bot_echo(message: types.Message):
    til = tarjimon.detect(text=message.text).lang
    print(til)
    matn = message.text
    if til=='uz':
        tarjima_qilish = tarjimon.translate(text=matn,dest='en',src='uz').text
        await message.answer(text=f'{tarjima_qilish}')
    elif til =='ru':
        tarjima_qilish = tarjimon.translate(text=matn, dest='en', src='ru').text
        await message.answer(text=f'{tarjima_qilish}')