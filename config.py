from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = config("TOKEN")

storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMINS = (980797645, )