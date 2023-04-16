from aiogram import Dispatcher, types
from utils import db1
from keyboard.user_kb import kb_client, inline_kb


async def send_welcome(message: types.Message):
    await message.answer("Привет! Этот бот создан, чтобы немного поднять тебе настроение. Он может отправлять тебе"
                         " анекдоты, а ты в свою очередь можешь посмеяться и сохранить их в избранное. Приступим...",
                         reply_markup=kb_client)


async def send_joke(message: types.Message):
    global joke_id
    joke = db1.select_joke()
    joke_id = joke[0]
    joke_text = joke[1]
    await message.answer(joke_text, reply_markup=inline_kb)


async def send_fav_joke(message: types.Message):
    await message.answer(db1.select_fav_joke()[0], reply_markup=kb_client)


async def save_joke(call: types.CallbackQuery):
    await call.message.answer('Сохранено👍')
    db1.upd_fav_joke(joke_id)
    await call.answer()


def register_user_handlers(dp:Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 's'])
    dp.register_message_handler(send_joke, commands=['Случайный_анекдот😄', 'random'])
    dp.register_message_handler(send_fav_joke, commands=['Анекдот_из_сохраненных⭐', 'fav'])
    dp.register_callback_query_handler(save_joke, text='save_joke')




