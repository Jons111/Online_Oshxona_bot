from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from . guruhlar_bilan_ishlash import Guruh
from .userlar_bilan_ishlash import Shaxsiy
from .kanallar_bilan_ishlash import  Kanal

if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(Guruh)
    dp.filters_factory.bind(Shaxsiy)
    dp.filters_factory.bind(Kanal)
