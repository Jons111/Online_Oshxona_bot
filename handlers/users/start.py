from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.Inline_menu import inline_button

from loader import dp,data_base
from filters import Shaxsiy

@dp.message_handler( Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    s = message
    ism = message.from_user.first_name
    surename =message.from_user.full_name
    user_name=message.from_user.username
    idd = message.from_user.id
    try:
        data_base.foydalanuvchi_qoshish(ism=ism,fam=surename,tg_id=idd,username=user_name)
    except Exception as x:
        print(x)
    await message.answer(f"Salom, {s}",reply_markup=inline_button)
