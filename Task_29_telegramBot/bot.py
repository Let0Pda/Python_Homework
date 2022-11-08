import os
import asyncio
import logging
import json
import string

import requests
from env import TOKEN
from aiogram import Bot, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Объект бота
bot = Bot(token=TOKEN)

# Диспетчер
dp = Dispatcher(bot)

# https://ru.stackoverflow.com/questions/1389231/aiorgam-python-%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0-%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D0%B9-%D0%BE%D1%82-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F


class form(StatesGroup):
    mess = State()

# проверяю startup )))


async def on_startup(_):
    print('Бот вышел в онлайн')


'''
# Эхобот
# @dp.message_handler()
# async def echo_send(message: types.Message):
#     # await message.answer(message.text)  # Эхом повторяет сообщения пользователя
#     # await message.reply(message.text) # Эхом повторяет сообщения пользователя с цитированием пользователя
#     await bot.send_message(message.from_user.id, message.text) # Отвечает эхом в личные сообщения пользователю
'''


def sentiment(message):
    API_URL = 'https://7015.deeppavlov.ai/model'
    data = {'x': [message]}
    res = requests.get(API_URL, json=data).json()
    santiment = res[0][0]
    return santiment
# Хэндлер на команду /start


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    # try: # Для группы
    await bot.send_message(message.from_user.id, 'Я бот. Приятно познакомиться')
    await message.delete()
    # except:
    #     await message.reply('Напишите боту в ЛС: \nhttps: // t.me/vidll_python_bot')


@dp.message_handler(commands=['santiment'])
async def santiment_massage(message: types.Message):
    await message.answer("Введите ваше сообщение: ")
    await form.mess.set()


@dp.message_handler(state=form.mess)
async def Form(message: types.Message, state: FSMContext):
    text = state.set()
    res = sentiment(text)
    await message.answer(res)


# @dp.message_handler(commands=['santiment'])
# # await bot.send_message(message.from_user.id, 'введите текст запроса')
# # dp.message_handler()
# async def ask_wikipedia_question(message: types.Message):
#     await message.answer('введите текст запроса')
#     if message.text.lower() != '':
#         text = message.text.lower()
#         res = sentiment(text)
#     await message.answer(res)

'''
# # Обработка текста
# @dp.message_handler()
# async def echo_send(message: types.Message):
#     if message.text.lower() == 'привет':
#         await message.answer('И тебе привет')
#     else:
#         await message.answer('Не понимаю, что это значит.')
'''


@dp.message_handler()  # + фильтр мата
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()}.intersection(set(json.load(open('cenz.json')))):
        await message.reply('Тут ругаться запрещено!!!')
        await message.delete()
    elif message.text.lower() == 'привет':
        await message.answer('И тебе привет')
    else:
        await message.answer('Не понимаю, что это значит.')

        # if __name__ == '__main__':
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
