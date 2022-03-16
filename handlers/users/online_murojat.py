from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from keyboards.default.tasdiqlash import tasdiq_button
from keyboards.default.tel import tel_button
from states.holatlar import Forma
from loader import dp, bot
from filters import Shaxsiy

# Echo bot
@dp.message_handler( Shaxsiy(),commands='murojat')
async def bot_echo(message: types.Message):
    await message.answer(text='Adminga murojat qilish uchun anketa toldiring')
    await message.answer(text='Ismni kiriting')
    await Forma.ism_qabul_qilish.set()

@dp.message_handler(state=Forma.ism_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    ism  = message.text

    await state.update_data({'ism':ism})
    await message.answer(text='Familyani kiriting')
    await Forma.fam_qabul_qilish.set()


@dp.message_handler(state=Forma.fam_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
    familya = message.text

    await state.update_data({'fam': familya})
    await message.answer(text='yoshni kiriting')
    await Forma.yosh_qabul_qilish.set()


@dp.message_handler(state=Forma.yosh_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
    yosh = message.text

    await state.update_data({'yosh': yosh})
    await message.answer(text='telni kiriting',reply_markup=tel_button)
    await Forma.tel_qabul_qilish.set()

@dp.message_handler(state=Forma.tel_qabul_qilish,content_types=ContentType.CONTACT)
async def bot_echo(message: types.Message, state: FSMContext):
    tel = message.contact.phone_number

    await state.update_data({'tel':tel})
    await message.answer(text='murojatni kiriting')
    await Forma.murojat_qabul_qilish.set()

@dp.message_handler(state=Forma.murojat_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
    matn = message.text
    await state.update_data({'matn': matn})

    malumotlar = await state.get_data()

    user_ismim = malumotlar.get('ism')
    user_fam = malumotlar.get('fam')
    user_yosh =malumotlar.get('yosh')
    user_tel = malumotlar.get('tel')

    await message.answer(text=f'Quyidagi malumotlarni adminga yuborish uchun tasdiqlash tugamasini bosing\n'
                              f'Ism : {user_ismim} \n'
                              f'Fam : {user_fam} \n'
                              f'Yosh : {user_yosh} \n'
                              f'Tel : {user_tel} \n\n'
                              f'Murojat : {matn} \n',reply_markup=tasdiq_button)
    await Forma.tasadiqlash.set()



@dp.message_handler(text ='Tasdiqlash',state=Forma.tasadiqlash)
async def bot_echo(message: types.Message, state: FSMContext):
    malumotlar = await state.get_data()
    matn = malumotlar.get('matn')
    user_ismim = malumotlar.get('ism')
    user_fam = malumotlar.get('fam')
    user_yosh = malumotlar.get('yosh')
    user_tel = malumotlar.get('tel')
    user_name = message.from_user.first_name

    await bot.send_message(chat_id=1892438581,text=f"Ushbu foydalanuvchi {user_name} quyidagi  habar yubordi"
                                                 f"\n {matn}"
                                                   f"{user_ismim}"
                                                   f"{user_tel}"
                                                   f"{user_yosh}"
                                                   f"{user_fam}")
    await state.finish()