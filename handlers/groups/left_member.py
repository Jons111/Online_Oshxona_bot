from aiogram import types
from aiogram.types import ContentType

from loader import dp
from filters import Guruh

# Echo bot
@dp.message_handler( Guruh(), content_types= ContentType.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    ism = message.left_chat_member.first_name
    await message.answer(text=f'Guruhni tark etdi  {ism} ')