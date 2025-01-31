from aiogram import Router, F, BaseMiddleware

from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    TelegramObject,
)

from typing import Callable, Awaitable, Dict, Any

from dbrequests import update_db

router_client = Router()


def create_module_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1 модуль', callback_data='1 модуль'),
         InlineKeyboardButton(text='2 модуль', callback_data='2 модуль'),
         InlineKeyboardButton(text='3 модуль', callback_data='3 модуль'),
         InlineKeyboardButton(text='4 модуль', callback_data='4 модуль')],

        [InlineKeyboardButton(text='5 модуль', callback_data='5 модуль'),
        InlineKeyboardButton(text='6 модуль', callback_data='6 модуль'),
        InlineKeyboardButton(text='7 модуль', callback_data='7 модуль'),
        InlineKeyboardButton(text='8 модуль', callback_data='8 модуль')]
    ])


MODULES_DESCRIPTION = """Курс-хаб: https://e.vyatsu.ru/course/view.php?id=31976

1 модуль - Принципы функционирования нейронных сетей
2 модуль - Генеративный искусственный интеллект
3 модуль - Анализ данных
4 модуль - Программирование искусственного интелекта
5 модуль - Моделирование бизнес-процессов
6 модуль - Библиотеки Python3
7 модуль - Работа со структурированными данными
8 модуль - Практика в профильной сфере"""


async def send_or_edit_modules_message(message, keyboard):
    if isinstance(message, Message):
        await message.answer(MODULES_DESCRIPTION, reply_markup=keyboard)
    elif isinstance(message, CallbackQuery):
        await message.message.edit_text(MODULES_DESCRIPTION, reply_markup=keyboard)
        await message.answer()


@router_client.message(F.text == '/start')
async def start_handler(message: Message):
    keyboard = create_module_keyboard()
    await send_or_edit_modules_message(message, keyboard)


@router_client.callback_query(F.data == 'Меню')
async def menu_handler(callback: CallbackQuery):
    keyboard = create_module_keyboard()
    await send_or_edit_modules_message(callback, keyboard)
