from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMIN_API, TOKEN_WORK_BOT, PD
from other import update_BD
import sqlite3


router_admin = Router()


@router_admin.message(F.document)
async def get_document(message: Message):
    if message.from_user.id == ADMIN_API:
        await message.answer(message.document.file_id)


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Свод', url='https://docs.google.com/spreadsheets/d/103yQ11buqGyzOK8GupOHXAx15rZW8wVXxhPH5D12iX4/edit?gid=1691697565#gid=1691697565')],

    [InlineKeyboardButton(text='Пароли контеста', url='https://docs.google.com/spreadsheets/d/1txobkH1PnhA3IymxDsDsAWcpxGr0tSVh'),
    InlineKeyboardButton(text='Номера телефонов', url=PD)],

    [InlineKeyboardButton(text='Расписание РППО', url='https://docs.google.com/spreadsheets/d/1C338-QN87vqeSjIJq8BAmM-4OVOcMOvlRXxa4UcM9Cg'),
    InlineKeyboardButton(text='Расписание РПРПИИ', url='https://docs.google.com/spreadsheets/d/13qO88kp1xIbzywqB4gQq_-J0pxk4YGRRGFBANYnXNV8')],

     [InlineKeyboardButton(text='Расписание РППО ФУЛ', url='https://docs.google.com/spreadsheets/d/1V5A5f4RgQGX4zewEA4XaTqF2LdXYfSYJ2SA5Jv0sODg'),
    InlineKeyboardButton(text='Расписание РПРПИИ ФУЛ', url='https://docs.google.com/spreadsheets/d/1o4Zxf3q6acrXpGMXrF4j15s6GUR-36Jsc8Kdcl19Tl0')],

    [InlineKeyboardButton(text='Курс РППО', url='https://e.vyatsu.ru/course/view.php?id=31975'),
    InlineKeyboardButton(text='Курс РПРПИИ', url='https://e.vyatsu.ru/course/view.php?id=31976')],

    [InlineKeyboardButton(text='Инфа о себе', url='https://docs.google.com/forms/d/e/1FAIpQLSfCw43nH6g7aUGdao2rTBLmq5u2LsLsoLDhKTAD7W-83i2v6w/viewform'),
    InlineKeyboardButton(text='Папка с фото', url='https://drive.google.com/drive/folders/1ItF2qXCmOpBUd3AWUtAnkerX9EUT-EO5')],
    ])


@router_admin.message(F.text == '/info')
async def info(message: Message):
    if message.from_user.id == ADMIN_API:
        await message.answer("Данные", reply_markup=keyboard)
    else:
        await message.answer("Недостаточно прав")