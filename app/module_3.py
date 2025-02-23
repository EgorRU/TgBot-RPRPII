from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router_module_3 = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции3'),
     InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ3')],

    [InlineKeyboardButton(text='Материалы сам. работ', callback_data='Материалы сам. работ3'),
     InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал3')],

    [InlineKeyboardButton(text='Файл с материалами', callback_data='Файл с материалами3'),
     InlineKeyboardButton(text='Тестирование', url='https://e.vyatsu.ru/course/view.php?id=33700&sectionid=2691200')],

    [InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')],
])

message_text = '3 модуль - Анализ данных\nhttps://e.vyatsu.ru/course/view.php?id=33700'


@router_module_3.callback_query(F.data == '3 модуль')
async def module_3(callback: CallbackQuery):
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()

@router_module_3.callback_query(F.data == 'Файл с материалами3')
async def file_3(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    return
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document='BQACAgIAAxkBAAIBHWeu1i73L7-Sxx_JJmWkj1deqeFXAAJ5XwACdx14Se3vpJ7unqV3NgQ')
        await callback.message.answer(message_text, reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/ZHpMUlr5pyA'),
     InlineKeyboardButton(
         text='Видео 1 RT', url='https://rutube.ru/video/private/526309d7ec51bb3af065050f26a740cd/?p=Sv-ES0cxRgk1XMEQAynQkA'),
     InlineKeyboardButton(text='Материал 1', callback_data='Материал 31')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/KWlWJkSMByQ'),
     InlineKeyboardButton(
         text='Видео 2 RT', url='https://rutube.ru/video/private/e57f1713467ff9cb1c87ce0725a871aa/?p=-_WIkZGCQGrFydvseAt4WA'),
     InlineKeyboardButton(text='Материал 2', callback_data='Материал 32')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/G7IuOrpNZiw'),
     InlineKeyboardButton(
         text='Видео 3 RT', url='https://rutube.ru/video/private/f99add599b753285b77e7ac1720d27c7/?p=ulOCEKzw5VnmtPmm9DDOEw'),
     InlineKeyboardButton(text='Материал 3', callback_data='Материал 33')],

    [InlineKeyboardButton(text='Видео 4 YT', url='https://youtu.be/A-SG4-r6igA'),
     InlineKeyboardButton(
        text='Видео 4 RT', url='https://rutube.ru/video/private/bc3e60660856ec7a7a4dbb8e0ac711d3/?p=HxMw5xerr85esFpa7WGCTg'),
     InlineKeyboardButton(text='Материал 4', callback_data='Материал 34')],

    [InlineKeyboardButton(text='Видео 5 YT', url='https://youtu.be/-5Q5duCKYIQ'),
     InlineKeyboardButton(
        text='Видео 5 RT', url='https://rutube.ru/video/private/f911e3239c49a4d574092dff41737fca/?p=QII84qgureykV9hPCoIX2w'),
     InlineKeyboardButton(text='Материал 5', callback_data='Материал 35')],

    [InlineKeyboardButton(text='Назад', callback_data='3 модуль')]
])


@router_module_3.callback_query(F.data == 'Лекции3')
async def lect_3(callback: CallbackQuery):
    await callback.message.edit_text('Раздел лекций 3 модуля', reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_3.callback_query(F.data.startswith('Материал 3'))
async def material_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        number = int(callback.data[-1])
        match number:
            case 1:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOaZ6Da3TeARc33k_c38Xl7ElrYCdgAAqJlAAIO_AlJQ1sVaq8Gv_k3BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAOcZ6Da3F5rqn1ZGFcAAakuHAnQR1kUAAKjZQACDvwJSRWmye03VtW3NgQ')
            case 2:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOeZ6DbAVB_XSg_QVgAAeCYrVpHk8noAAKqZQACDvwJSfbqTtv0jtT6NgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAOgZ6DbBwmNOFsskBr0frZ4I-GOugEAAqtlAAIO_AlJcPuosiEjjg43BA')
            case 3:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOkZ6DbSq39oc8kxUvjW4g33j7yZh0AArRlAAIO_AlJKd4mtgVEwcM3BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAOiZ6DbRxkQ8TwtGa-jSrQFZmgBtvwAArNlAAIO_AlJZeh7Hozupgw3BA')
            case 4:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOmZ6DbcpzHSqvmK6v65eekm-I73Z4AArllAAIO_AlJQdq8w74rrkA3BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAOoZ6DbdWqSGHoCKWLJLJCzP4EGYAADumUAAg78CUm4BdhUIp6DEjYE')
            case 5:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOqZ6DblDzB0hmxrhzgYrRBoPt3vRUAAr1lAAIO_AlJ3wVG3mMhYpQ3BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAOsZ6DbltGNT8tGTe5blaTYZdDR6XcAAr5lAAIO_AlJgyfPIItt9qk3BA')

        await callback.message.answer('Раздел лекций 3 модуля', reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/djuHlDYccCU'),
     InlineKeyboardButton(
         text='Видео 1 RT', url='https://rutube.ru/video/private/b87bc86b6101cd49abbcfc03b3355f3e/?p=JWevZJGZuZ7XRH0GeCKynQ'),
     InlineKeyboardButton(text='Лаб. работа 1', callback_data='Лабораторная работа 31')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/p_jBR4y351g'),
     InlineKeyboardButton(
         text='Видео 2 RT', url='https://rutube.ru/video/private/e9fe6e259825b5db610d131fcf56eb48/?p=audV016PzsnKeWMqJIUqfg'),
     InlineKeyboardButton(text='Лаб. работа 2', callback_data='Лабораторная работа 32')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/ut2GMNxxpC4'),
     InlineKeyboardButton(
         text='Видео 3 RT', url='https://rutube.ru/video/private/3911932e826c329ba939c6119eb5c1dc/?p=SDrzpYxjKmEabm5qYxWL0g'),
     InlineKeyboardButton(text='Лаб. работа 3', callback_data='Лабораторная работа 33')],

    [InlineKeyboardButton(text='Назад', callback_data='3 модуль')]
])


@router_module_3.callback_query(F.data == 'Материал лаб. работ3')
async def lect_3(callback: CallbackQuery):
    await callback.message.edit_text('Раздел лабораторных работ 3 модуля', reply_markup=keyboard_labs)
    await callback.answer()


@router_module_3.callback_query(F.data.startswith('Лабораторная работа 3'))
async def lab_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        number = int(callback.data[-1])
        match number:
            case 1:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOuZ6DcCL56koCMej5TPuHDL7tQoLUAAtVlAAIO_AlJwI-3nlas_3U3BA')
            case 3:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOwZ6DcIO0B81W43R3sr4N3kSzCW8oAAthlAAIO_AlJrwAB1VFPQa3BNgQ')
            case 3:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOyZ6DcNMWYaZye5wj33TjmRiD_BPMAAttlAAIO_AlJV0ftgb-Y9Cs3BA')
        await callback.message.answer('Раздел лабораторных работ 3 модуля', reply_markup=keyboard_labs)
        await callback.answer()


keyboard_self = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Работа с markdown YT', url='https://youtu.be/ypq1N3Ulugs'),
     InlineKeyboardButton(
         text='Работа с markdown RT', url='https://rutube.ru/video/private/d1572250a127303ba46bd6084a1ca967/?p=QUT0xQvJXoBjIVaClRiuYg&r=plemwd')],

    [InlineKeyboardButton(text='Назад', callback_data='3 модуль')]
])


@router_module_3.callback_query(F.data == 'Материалы сам. работ3')
async def self_3(callback: CallbackQuery):
    await callback.message.edit_text('Раздел материалов для самостоятельной работы 3 модуля', reply_markup=keyboard_self)
    await callback.answer()


keyboard_add = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Человек vs ИИ',
                          url='https://vas3k.blog/blog/ai_alignment/')],
    [InlineKeyboardButton(text='Как работает ChatGPT',
                          url='https://habr.com/ru/companies/ods/articles/716918/')],
    [InlineKeyboardButton(text='Prompt Engineering Cheat Sheet',
                          url='https://big-picture.com/media/the_prompt_engineering_cheat_sheet.pdf')],
    [InlineKeyboardButton(text='A Systematic Survey',
                          url='https://arxiv.org/abs/3406.06608')],
    [InlineKeyboardButton(text='LLaMA-1/3, GPT-3.5/4',
                          url='https://arxiv.org/abs/3313.16171v3')],
    [InlineKeyboardButton(text='Generative AI',
                          url='https://ig.ft.com/generative-ai/')],
    [InlineKeyboardButton(text='Alice’s Adventures',
                          url='https://arxiv.org/pdf/3404.17635')],
    [InlineKeyboardButton(text='What is a GPT?',
                          url='https://youtu.be/wjZofJX0v4M')],
    [InlineKeyboardButton(text='Визуализация внимания',
                          url='https://youtu.be/eMlx5fFNoYc')],
    [InlineKeyboardButton(text='Как учатся с ИИ',
                          url='https://youtu.be/TMVVvU4K91Y')],
    [InlineKeyboardButton(text='@neurogen-news',
                          url='https://www.youtube.com/@neurogen-news')],
    [InlineKeyboardButton(text='@StableDiff',
                          url='https://www.youtube.com/@StableDiff')],
    [InlineKeyboardButton(text='Intro to LLM',
                          url='https://youtu.be/zjkBMFhNj_g')],
    [InlineKeyboardButton(text='What’s the future for generative AI?',
                          url='https://youtu.be/b76gsOSkHB4')],

    [InlineKeyboardButton(text='Назад', callback_data='3 модуль')]
])


@router_module_3.callback_query(F.data == 'Доп. материал3')
async def add_3(callback: CallbackQuery):
    await callback.message.edit_text('Раздел дополнительных материалов 3 модуля', reply_markup=keyboard_add)
    await callback.answer()
