from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router_module_2 = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции2'),
     InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ2')],

    [InlineKeyboardButton(text='Материалы сам. работ', callback_data='Материалы сам. работ2'),
     InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал2')],

    [InlineKeyboardButton(text='Файл с материалами', callback_data='Файл с материалами2'),
     InlineKeyboardButton(text='Тестирование', url='https://vyatsu.ru')],

    [InlineKeyboardButton(text='Расписание', url='https://vyatsu.ru')],

    [InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')],
])

message_text = '2 модуль - Генеративный искусственный интеллект'


@router_module_2.callback_query(F.data == '2 модуль')
async def module_2(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    return
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()
