import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from curvars import *


logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot)
start = 'Выберите валюту'

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(start, reply_markup=cur)

@dp.message_handler(text='$')
async def idk(message: types.Message):
    await message.answer('Введите сумму')
@dp.message_handler()
async def text_message(msg: types.Message):
    x1 = int(msg.text)
    c1 = x1 * usd
    await bot.send_message(msg.from_user.id, f'{x1} (Американские доллары) = {c1} (cум)', reply_markup=cur)

@dp.message_handler(text='€')
async def idk(message: types.Message):
    await message.answer('Введите сумму')
@dp.message_handler()
async def text_message(msg: types.Message):
    x2 = int(msg.text)
    c2 = x2 * euro
    await bot.send_message(msg.from_user.id, f'{x2} (евро) = {c2} (cум)', reply_markup=cur)

@dp.message_handler(text='₽')
async def idk(message: types.Message):
    await message.answer('Введите сумму')
@dp.message_handler()
async def text_message(msg: types.Message):
    x3 = int(msg.text)
    c3 = x3 * rubl
    await bot.send_message(msg.from_user.id, f'{x3} (рубль) = {c3} (cум)', reply_markup=cur)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
