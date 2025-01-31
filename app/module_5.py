from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router_module_5 = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции5'),
     InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ5')],

    [InlineKeyboardButton(text='Материалы сам. работ', callback_data='Материалы сам. работ5'),
     InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал5')],

    [InlineKeyboardButton(text='Файл с материалами', callback_data='Файл с материалами5'),
     InlineKeyboardButton(text='Тестирование', url='https://vyatsu.ru')],

    [InlineKeyboardButton(text='Расписание', url='https://vyatsu.ru')],
    
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')],
])

message_text = '5 модуль - Моделирование бизнес-процессов'


@router_module_5.callback_query(F.data == '5 модуль')
async def module_5(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    return
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()
