import datetime

from aiogram import types
from aiogram.types import ContentType

from loader import dp, bot
from filters import Guruh

# Echo bot
@dp.message_handler( Guruh(), content_types= ContentType.PHOTO)
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await message.answer(text=f'Guruhni tark etdi   ')
    await  bot.kick_chat_member(chat_id='@salom23443',user_id=user_id,)

@dp.message_handler( Guruh(), content_types= ContentType.STICKER)
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await message.answer(text=f'Guruhni tark etdi   ')
    await  bot.kick_chat_member(chat_id='@salom23443',user_id=user_id,)