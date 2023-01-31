from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
import os

BOT_TOKEN = str(os.environ.get('TOKEN'))
ADMINS = list(os.environ.get('ADMINS'))
IP = os.environ.get('ip')
kanallar = ['@sinov003','@sinov0033']
