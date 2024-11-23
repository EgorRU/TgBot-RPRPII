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

    [InlineKeyboardButton(text='Пароли контеста', url='https://docs.google.com/spreadsheets/d/1txobkH1PnhA3IymxDsDsAWcpxGr0tSVh/edit?gid=276852599#gid=276852599'),
    InlineKeyboardButton(text='Номера телефонов', url=PD)],

    [InlineKeyboardButton(text='Расписание РППО', url='https://docs.google.com/spreadsheets/d/1C338-QN87vqeSjIJq8BAmM-4OVOcMOvlRXxa4UcM9Cg/edit?gid=0#gid=0'),
    InlineKeyboardButton(text='Расписание РПРПИИ', url='https://docs.google.com')],

     [InlineKeyboardButton(text='Расписание РППО ФУЛ', url='https://docs.google.com/spreadsheets/d/1V5A5f4RgQGX4zewEA4XaTqF2LdXYfSYJ2SA5Jv0sODg/edit?gid=0#gid=0'),
    InlineKeyboardButton(text='Расписание РПРПИИ ФУЛ', url='https://docs.google.com')],

    [InlineKeyboardButton(text='Курс РППО', url='https://e.vyatsu.ru/course/view.php?id=31975'),
    InlineKeyboardButton(text='Курс РПРПИИ', url='https://e.vyatsu.ru/course/view.php?id=31976')],
    ])


@router_admin.message(F.text == '/info')
async def info(message: Message):
    if message.from_user.id == ADMIN_API:
        await message.answer("Данные", reply_markup=keyboard)
    else:
        await message.answer("Недостаточно прав")