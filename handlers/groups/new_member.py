from aiogram import types
from aiogram.types import ContentType

from loader import dp
from filters import Guruh

# Echo bot
@dp.message_handler( Guruh(), content_types= ContentType.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    ism = message.new_chat_members[0].first_name

    await message.answer(text=f'Guruhga hush kelibsiz {ism} ')
