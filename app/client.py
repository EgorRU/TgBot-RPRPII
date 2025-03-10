from aiogram import Router, F, BaseMiddleware
from aiogram.filters import CommandStart
import re

from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    TelegramObject,
)

from typing import Callable, Awaitable, Dict, Any

from dbrequests import update_db

from app.module_1 import send_module_1
from app.module_2 import send_module_2
from app.module_3 import send_module_3

router_client = Router()

MODULES_DESCRIPTION = """Курс-хаб: https://e.vyatsu.ru/course/view.php?id=31976

1 модуль - Принципы функционирования нейронных сетей
2 модуль - Генеративный искусственный интеллект
3 модуль - Анализ данных
4 модуль - Программирование искусственного интелекта
5 модуль - Моделирование бизнес-процессов
6 модуль - Библиотеки Python3
7 модуль - Работа со структурированными данными
8 модуль - Практика в профильной сфере"""

KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1 модуль', callback_data='1 модуль'),
        InlineKeyboardButton(text='2 модуль', callback_data='2 модуль'),
        InlineKeyboardButton(text='3 модуль', callback_data='3 модуль'),
        InlineKeyboardButton(text='4 модуль', callback_data='4 модуль')],

    [InlineKeyboardButton(text='5 модуль', callback_data='5 модуль'),
        InlineKeyboardButton(text='6 модуль', callback_data='6 модуль'),
        InlineKeyboardButton(text='7 модуль', callback_data='7 модуль'),
        InlineKeyboardButton(text='8 модуль', callback_data='8 модуль')],

    [InlineKeyboardButton(text='Ассесмент', callback_data='Ассесмент')]
])


@router_client.message(CommandStart())
async def start_handler(message: Message, command):
    args = command.args if command.args else ''
    if not args:
        await message.answer(MODULES_DESCRIPTION, reply_markup=KEYBOARD)
    else:
        pattern = r"^module_[1-3]$"
        if not re.match(pattern, args):
            await message.answer(MODULES_DESCRIPTION, reply_markup=KEYBOARD)
        else:
            match int(args[-1]):
                case 1:
                    await send_module_1(message)
                case 2:
                    await send_module_2(message)
                case 3:
                    await send_module_3(message)
                # case 4:
                #     await module_4(message)
                # case 5:
                #     await module_5(message)
                # case 6:
                #     await module_6(message)
                # case 7:
                #     await module_7(message)
                # case 8:
                #     await module_8(message)


@router_client.callback_query(F.data == 'Меню')
async def menu_handler(callback: CallbackQuery):
    await callback.message.edit_text(MODULES_DESCRIPTION, reply_markup=KEYBOARD)
    await callback.answer()


@router_client.callback_query(F.data == 'Ассесмент')
async def assesment_handler(callback: CallbackQuery):
    await callback.message.answer_document(document='BQACAgIAAxkBAAIBdme134PbJysnSQkdYouvM3dnk_c8AAIxawACmT-wSf01bLvr5u_GNgQ', caption='https://auth.unionepro.ru/login')
    await callback.message.answer(MODULES_DESCRIPTION, reply_markup=KEYBOARD)
    await callback.answer()