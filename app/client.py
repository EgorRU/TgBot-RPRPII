from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD
import sqlite3


router_client = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1 модуль', callback_data='1 модуль'),
         InlineKeyboardButton(text='2 модуль', callback_data='2 модуль'),
         InlineKeyboardButton(text='3 модуль', callback_data='3 модуль'),
         InlineKeyboardButton(text='4 модуль', callback_data='4 модуль')],
        [InlineKeyboardButton(text='5 модуль', callback_data='5 модуль'),
         InlineKeyboardButton(text='6 модуль', callback_data='6 модуль'),
         InlineKeyboardButton(text='7 модуль', callback_data='7 модуль'),
         InlineKeyboardButton(text='8 модуль', callback_data='8 модуль')]
    ])

message_dict = {
    "text1": "1 модуль - Принципы функционирования нейронных сетей\n",
    "text2": "2 модуль - Генеративный искусственный интеллект\n",
    "text3": "3 модуль - Анализ данных\n",
    "text4": "4 модуль - Программирование искусственного интелекта\n",
    "text5": "5 модуль - Моделирование бизнес-процессов\n",
    "text6": "6 модуль - Библиотеки Python3\n",
    "text7": "7 модуль - Работа со структурированными данными\n",
    "text8": "8 модуль - Практика в профильной сфере\n",
}


message_text = "".join(message_dict[key] for key in message_dict)


@router_client.message(F.text == '/start')
async def start(message: Message):
    await update_BD(message, "/start")
    await message.answer(message_text, reply_markup=keyboard)


@router_client.callback_query(F.data == 'Меню')
async def menu(callback: CallbackQuery):
    await update_BD(callback, "Меню")
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()