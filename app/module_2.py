from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_2 = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции2'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ2')],
    [InlineKeyboardButton(text='Тест', url='https://www.vyatsu.ru/')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами2')],
    [InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_2.callback_query(F.data == '2 модуль')
async def module_2(callback: CallbackQuery):
    await update_BD(callback, "2 модуль")
    await callback.answer("В разработке ...", show_alert=True)
    return
    await callback.message.edit_text("Модуль 2", reply_markup=keyboard)
    await callback.answer()