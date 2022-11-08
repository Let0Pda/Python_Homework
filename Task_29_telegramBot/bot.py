import os
import asyncio
import logging
import json
import string

import requests
from env import TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Объект бота
bot = Bot(token=TOKEN)

# Диспетчер
dp = Dispatcher(bot)

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

# Хэндлер на команду /start


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    # try: # Для группы
    await bot.send_message(message.from_user.id, 'Я бот. Приятно познакомиться')
    await message.delete()
    # except:
    #     await message.reply('Напишите боту в ЛС: \nhttps: // t.me/vidll_python_bot')


@dp.message_handler(commands=['santiment'])
async def ask_wikipedia_question(message: types.Message):
    await bot.send_message(message.from_user.id, 'введите текст запроса')
    # def request_sentiment(message):
    API_URL = 'https://7015.deeppavlov.ai/model'
    data = message.text
    res = requests.post(API_URL, json=data).json()
    santiment = res[0][0]
    await message.answer(santiment)

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
