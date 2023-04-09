import logging

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types

#Telegram bot token

api = '6021754722:AAG8Ej5RSc3C2p47pWolc3adGeyn__BajPE'

usdollar = KeyboardButton('$')
euro = KeyboardButton('€')
rubl = KeyboardButton('₽')

cur = ReplyKeyboardMarkup(resize_keyboard=True).add(usdollar).add(euro).add(rubl)

usd = 11395.00
eu = 12027.31
rub = 149.27