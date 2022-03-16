from aiogram import types
from aiogram.types import ContentType, InputFile

from loader import dp,bot

from filters import Shaxsiy
# Echo bot
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    doc_id = message.document.file_id
    await message.answer(text=f'Dakument yuborildi idda {doc_id}')

@dp.message_handler(Shaxsiy(),content_types=ContentType.STICKER)
async def bot_echo(message: types.Message):
    await message.sticker.download()
    await message.answer(text='stiker yuborildi')

@dp.message_handler(content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message):
    await message.video.download()
    await message.answer(text='video  yuborildi')

@dp.message_handler(Shaxsiy(), content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[0].download()
    rasm_id= message.photo[0].file_id
    await message.answer(text=f'rasm yuborildi {rasm_id}')

@dp.message_handler(commands='rasm')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_id = 'AgACAgIAAxkBAAOoYiC9rntxbeCHMnXVu3XiQ7fy6vgAAoa6MRuacghJEkYjj3qZhDIBAAMCAANzAAMjBA'
    await  bot.send_photo(chat_id=user_id,photo=rasm_id)

@dp.message_handler(commands='video')
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzil = 'BQACAgIAAxkBAAEOb8ZiIMA-ZycmW7olwdUGXeb9OpkB3QACFxcAAj8UCUlzAtulmgqvaSME'
    await bot.send_document(chat_id=user_id,document=video_manzil)