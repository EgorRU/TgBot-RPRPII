from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router_module_7 = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции7'),
     InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ7')],

    [InlineKeyboardButton(text='Материалы сам. работ', callback_data='Материалы сам. работ7'),
     InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал7')],

    [InlineKeyboardButton(text='Файл с материалами', callback_data='Файл с материалами7'),
     InlineKeyboardButton(text='Тестирование', url='https://vyatsu.ru')],

    [InlineKeyboardButton(text='Расписание', url='https://vyatsu.ru')],
    
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')],
])

message_text = '7 модуль - Работа со структурированными данными'


@router_module_7.callback_query(F.data == '7 модуль')
async def module_7(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    return
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()
