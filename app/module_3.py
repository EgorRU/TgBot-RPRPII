from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router_module_3 = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции3'),
     InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ3')],

    [InlineKeyboardButton(text='Материалы сам. работ', callback_data='Материалы сам. работ3'),
     InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал3')],

    [InlineKeyboardButton(text='Файл с материалами', callback_data='Файл с материалами3'),
     InlineKeyboardButton(text='Тестирование', url='https://vyatsu.ru')],

    [InlineKeyboardButton(text='Расписание', url='https://vyatsu.ru')],
    
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')],
])

message_text = '3 модуль - Анализ данных'


@router_module_3.callback_query(F.data == '3 модуль')
async def module_3(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    return
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()
