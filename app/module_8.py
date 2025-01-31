from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router_module_8 = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции8'),
     InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ8')],

    [InlineKeyboardButton(text='Материалы сам. работ', callback_data='Материалы сам. работ8'),
     InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал8')],

    [InlineKeyboardButton(text='Файл с материалами', callback_data='Файл с материалами8'),
     InlineKeyboardButton(text='Тестирование', url='https://vyatsu.ru')],

    [InlineKeyboardButton(text='Расписание', url='https://vyatsu.ru')],
    
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')],
])

message_text = '8 модуль - Практика в профильной сфере'


@router_module_8.callback_query(F.data == '8 модуль')
async def module_8(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    return
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()
