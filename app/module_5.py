from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_5 = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции5'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ5')],
    [InlineKeyboardButton(text='Тест', url='https://www.vyatsu.ru/')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами5')],
    [InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_5.callback_query(F.data == '5 модуль')
async def module_5(callback: CallbackQuery):
    await update_BD(callback, "5 модуль")
    await callback.answer("В разработке ...", show_alert=True)
    return
    await callback.message.edit_text("Модуль 5", reply_markup=keyboard)
    await callback.answer()