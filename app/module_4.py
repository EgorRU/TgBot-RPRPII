from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router_module_4 = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции4'),
     InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ4')],

    [InlineKeyboardButton(text='Материалы сам. работ', callback_data='Материалы сам. работ4'),
     InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал4')],

    [InlineKeyboardButton(text='Файл с материалами', callback_data='Файл с материалами4'),
     InlineKeyboardButton(text='Тестирование', url='https://vyatsu.ru')],

    [InlineKeyboardButton(text='Расписание', url='https://vyatsu.ru')],
    
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')],
])

message_text = '4 модуль - Программирование искусственного интелекта'


@router_module_4.callback_query(F.data == '4 модуль')
async def module_4(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    return
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()
