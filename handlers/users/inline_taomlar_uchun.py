from aiogram import types
from aiogram.types import CallbackQuery

from loader import dp,bot
from keyboards.default.taom_nomlari import taomlar_button

# Echo bot
@dp.callback_query_handler(text='menu1')
async def bot_echo(xabar: CallbackQuery):
    matn_id = xabar
    user_id = xabar.from_user.id
    await xabar.message.answer(text=f'{matn_id}')
