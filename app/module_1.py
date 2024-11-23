from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_1 = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции1'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ1')],
    [InlineKeyboardButton(text='Тест', url='https://www.vyatsu.ru/')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами1')],
    [InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_1.callback_query(F.data == '1 модуль')
async def module_1(callback: CallbackQuery):
    await update_BD(callback, "1 модуль")
    await callback.message.edit_text("Модуль 1\nhttps://e.vyatsu.ru/course/view.php?id=33681", reply_markup=keyboard)
    await callback.answer()


@router_module_1.callback_query(F.data == 'Файл со всеми материалами1')
async def file_1(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами1")
    await callback.answer("В разработке", show_alert=True)
    return
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-P2T_damrDjh6J3kKqJL8Hdii0KR-AALNOQACunMBSAMv4wvs7V9eMAQ")
        await callback.message.answer("Модуль 1", reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/OSXpXOqKiGU'),
    InlineKeyboardButton(text='Видео 1 RT', url='https://rutube.ru/video/private/1e77666d3cb68406e6c05b599c4598f7/?p=DCflDPEpn6AH1KioMWZcJg'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 11')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/KgPuIZ-HBvA'),
    InlineKeyboardButton(text='Видео 2 RT', url='https://rutube.ru/video/private/cbe72d0aa511b3a5d5266a9c02a97e79/?p=ICxvKISFS52id8xxfOdK9w'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 12')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/ZV5K9AikLL4'),
    InlineKeyboardButton(text='Видео 3 RT', url='https://rutube.ru/video/private/7f8987f5485adde4db28341fe99fa738/?p=iSG6TCb_8KcK3MpZE__eZA'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 13')],
    
    [InlineKeyboardButton(text='Видео 4 YT', url='https://youtu.be/ixk86HiLCzk'),
    InlineKeyboardButton(text='Видео 4 RT', url='https://rutube.ru/video/private/16c1fcd82aedbd043decedf9a9e8243d/?p=ZnDPCoSSDutMQ65n0L0GFg'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 14')],

    [InlineKeyboardButton(text='Видео 5 YT', url='https://youtu.be/r0tFiOkuBHs'),
    InlineKeyboardButton(text='Видео 5 RT', url='https://rutube.ru/video/private/a044287441c1b35d9fb59a41a48299eb/?p=TVT-lhVBGl5C3L-zOFfEaQ'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 15')],

    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
    ])


@router_module_1.callback_query(F.data == 'Лекции1')
async def lect_1(callback: CallbackQuery):
    await update_BD(callback, "Лекции1")
    await callback.message.edit_text("Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_1.callback_query(F.data == 'Материал 11')
async def material_11(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document="BQACAgIAAxkBAANAZ0GrS-u7BDVRajYIbyiflNDoyB8AAo5kAALOyghKVnYlqqtqO102BA")
        await callback.message.answer_document(document="BQACAgIAAxkBAAMQZ0Gqi7P632msRBvDEgzaqb3JIqsAAnhkAALOyghKeDxoG3t4-xk2BA")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


@router_module_1.callback_query(F.data == 'Материал 12')
async def material_12(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document="BQACAgIAAxkBAAMTZ0GqpgYBDS13R-ADa-Lh--FBEGUAAntkAALOyghKwKvzkChJwwc2BA")
        await callback.message.answer_document(document="BQACAgIAAxkBAAMUZ0Gqpq5iGeu0BFwGKD3IBWgWcK4AAnxkAALOyghKMpM2PHm0rwg2BA")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_1.callback_query(F.data == 'Материал 13')
async def material_13(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document="BQACAgIAAxkBAAMYZ0Gqu8m_5iMj_Xd5_0s7iyh0N9cAAn9kAALOyghK2peOMpaYJmE2BA")
        await callback.message.answer_document(document="BQACAgIAAxkBAAMXZ0GquyEAAWyuTtFwBF08xxKV7PeSAAJ-ZAACzsoISoLchAaqWwjbNgQ")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_1.callback_query(F.data == 'Материал 14')
async def material_14(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document="BQACAgIAAxkBAAMcZ0Gq1MK5Ii391_YETby_UbKIE40AAoJkAALOyghKl5jo6jRHcxE2BA")
        await callback.message.answer_document(document="BQACAgIAAxkBAAMbZ0Gq1Io2Bpr4nXvvAAGR0550bxxgAAKBZAACzsoISg3Ck3Abj5rWNgQ")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_1.callback_query(F.data == 'Материал 15')
async def material_15(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document="BQACAgIAAxkBAAMgZ0Gq7OsCR2iZ3pEJBQig6b7uNe0AAoVkAALOyghK3QxuiZsE3Sg2BA")
        await callback.message.answer_document(document="BQACAgIAAxkBAAMfZ0Gq7LdEWBXH3KzLJjr3bOjlCw8AAoRkAALOyghKsjvY1PR5MpE2BA")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/_WEejmL6ogc'),
    InlineKeyboardButton(text='Видео 1 RT', url='https://rutube.ru/video/private/ad2a6bce041274809af5accf5d50b350/?p=3P6lrHAoZX3hbI-kmY209g'),
    InlineKeyboardButton(text='Лаба 1', callback_data='Лабораторная работа 11')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/saD6WFgA0n4'),
    InlineKeyboardButton(text='Видео 2 RT', url='https://rutube.ru/video/private/4278982a1f0f6313c8fd8b4944b985ea/?r=wd&p=VoWNY1u7y3G8BTa79QAlcA'),
    InlineKeyboardButton(text='Лаба 2', callback_data='Лабораторная работа 12')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/YdUithseiGg'),
    InlineKeyboardButton(text='Видео 3 RT', url='https://rutube.ru/video/private/65354c258bb04857e0dbcc0c6939eccf/?r=wd&p=UpVDPM4q4UFeU0rpE981DA'),
    InlineKeyboardButton(text='Лаба 3', callback_data='Лабораторная работа 13')],

    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
    ])


@router_module_1.callback_query(F.data == 'Материал лаб. работ1')
async def lect_1(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ1")
    await callback.message.edit_text("Раздел лабораторных работ 1 модуля", reply_markup=keyboard_labs)
    await callback.answer()
    
   
@router_module_1.callback_query(F.data == 'Лабораторная работа 11')
async def lab_11(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document="BQACAgIAAxkBAANXZ0GrgREpNCQDVbeYvljN0XdPTsUAApRkAALOyghKNKDPc4upY2Q2BA")
        await callback.message.answer("Раздел лабораторных работ 1 модуля", reply_markup=keyboard_labs)
        await callback.answer()


@router_module_1.callback_query(F.data == 'Лабораторная работа 12')
async def lab_12(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document="BQACAgIAAxkBAANZZ0Grj8i4zTgxxNQFJ6XpvYUd7wIAApZkAALOyghK3VDilmHt4b82BA")
        await callback.message.answer("Раздел лабораторных работ 1 модуля", reply_markup=keyboard_labs)
        await callback.answer()
        

@router_module_1.callback_query(F.data == 'Лабораторная работа 13')
async def lab_13(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document="BQACAgIAAxkBAANbZ0GroLaLZh4usTFw08owx_EwJ1gAAphkAALOyghKXu6jFE8scNo2BA")
        await callback.message.answer("Раздел лабораторных работ 1 модуля", reply_markup=keyboard_labs)
        await callback.answer()