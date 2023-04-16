from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import API_TOKEN


bot = Bot(token=API_TOKEN, parse_mode = types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())