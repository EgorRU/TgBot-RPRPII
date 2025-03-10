from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message

router_module_2 = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции2'),
     InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ2')],

    [InlineKeyboardButton(text='Материалы сам. работ', callback_data='Материалы сам. работ2'),
     InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал2')],

    [InlineKeyboardButton(text='Файл с материалами', callback_data='Файл с материалами2'),
     InlineKeyboardButton(text='Тестирование', url='https://e.vyatsu.ru/mod/quiz/view.php?id=783180')],

    [InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')],
])

message_text = '2 модуль - Генеративный искусственный интеллект\nhttps://e.vyatsu.ru/course/view.php?id=33699'


async def send_module_2(message: Message):
    await message.answer(message_text, reply_markup=keyboard)


@router_module_2.callback_query(F.data == '2 модуль')
async def module_2(callback: CallbackQuery):
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()


@router_module_2.callback_query(F.data == 'Файл с материалами2')
async def file_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document='BQACAgIAAxkBAAIBHWeu1i73L7-Sxx_JJmWkj1deqeFXAAJ5XwACdx14Se3vpJ7unqV2NgQ')
        await callback.message.answer(message_text, reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/b002gdNXsXw'),
     InlineKeyboardButton(
         text='Видео 1 RT', url='https://rutube.ru/video/private/310867e4849c09250623cd0d5c0409f2/?p=lCKXMqrXnL2i5cQoLmzXOw'),
     InlineKeyboardButton(text='Материал 1', callback_data='Материал 21')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/Le_MI4LgODE'),
     InlineKeyboardButton(
         text='Видео 2 RT', url='https://rutube.ru/video/private/b70b6c08e33017a577c8b52a2ca6b532/?p=MDnKkciVhygnloYx8-s_7A'),
     InlineKeyboardButton(text='Материал 2', callback_data='Материал 22')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/HyS2ufuUUTo'),
     InlineKeyboardButton(
         text='Видео 3 RT', url='https://rutube.ru/video/private/76cec9adcac811024498ae82eb60ec45/?p=ACPKx5FgyNWmiPTebiK0Cw'),
     InlineKeyboardButton(text='Материал 3', callback_data='Материал 23')],

    [InlineKeyboardButton(text='Видео 4 YT', url='https://youtu.be/Ot5h-ZHejnA'),
     InlineKeyboardButton(
        text='Видео 4 RT', url='https://rutube.ru/video/private/1572e7ad8f7026376ce1afa2ea536ce6/?p=HveRFcOgWOArcd0AnTVhPA&r=plemwd'),
     InlineKeyboardButton(text='Материал 4', callback_data='Материал 24')],

    [InlineKeyboardButton(text='Видео 5 YT', url='https://youtu.be/YtyB6qHBbSc'),
     InlineKeyboardButton(
        text='Видео 5 RT', url='https://rutube.ru/video/private/fc074230990b360eb29909d8571b7bbc/?p=g9usodpL-cwMFCFfvPZJZA&r=plemwd'),
     InlineKeyboardButton(text='Материал 5', callback_data='Материал 25')],

    [InlineKeyboardButton(text='Назад', callback_data='2 модуль')]
])


@router_module_2.callback_query(F.data == 'Лекции2')
async def lect_2(callback: CallbackQuery):
    await callback.message.edit_text('Раздел лекций 2 модуля', reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_2.callback_query(F.data.startswith('Материал 2'))
async def material_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        number = int(callback.data[-1])
        match number:
            case 1:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOaZ6Da2TeARc22k_c38Xl7ElrYCdgAAqJlAAIO_AlJQ1sVaq8Gv_k2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAOcZ6Da3F5rqn1ZGFcAAakuHAnQR1kUAAKjZQACDvwJSRWmye02VtW2NgQ')
            case 2:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOeZ6DbAVB_XSg_QVgAAeCYrVpHk8noAAKqZQACDvwJSfbqTtv0jtT6NgQ')
                await callback.message.answer_document(document='BQACAgIAAxkBAAOgZ6DbBwmNOFsskBr0frZ4I-GOugEAAqtlAAIO_AlJcPuosiEjjg42BA')
            case 3:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOkZ6DbSq39oc8kxUvjW4g23j7yZh0AArRlAAIO_AlJKd4mtgVEwcM2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAOiZ6DbRxkQ8TwtGa-jSrQFZmgBtvwAArNlAAIO_AlJZeh7Hozupgw2BA')
            case 4:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOmZ6DbcpzHSqvmK6v65eekm-I73Z4AArllAAIO_AlJQdq8w74rrkA2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAOoZ6DbdWqSGHoCKWLJLJCzP4EGYAADumUAAg78CUm4BdhUIp6DEjYE')
            case 5:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOqZ6DblDzB0hmxrhzgYrRBoPt3vRUAAr1lAAIO_AlJ3wVG3mMhYpQ2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAOsZ6DbltGNT8tGTe5blaTYZdDR6XcAAr5lAAIO_AlJgyfPIItt9qk2BA')

        await callback.message.answer('Раздел лекций 2 модуля', reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/qcyceSWxwNQ'),
     InlineKeyboardButton(
         text='Видео 1 RT', url='https://rutube.ru/video/private/ddc246d3feba6ea19b0c588518c9ab18/?p=y3XqYZQpwhrjG-SNwNgh9g'),
     InlineKeyboardButton(text='Лаб. работа 1', callback_data='Лабораторная работа 21')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/wY8wv3AGrb4'),
     InlineKeyboardButton(
         text='Видео 2 RT', url='https://rutube.ru/video/private/8684564caa0df20ade4d38af4d838844/?p=1vCBZS9QcePAdftXI0gbUA'),
     InlineKeyboardButton(text='Лаб. работа 2', callback_data='Лабораторная работа 22')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/O28QU7yBjj4'),
     InlineKeyboardButton(
         text='Видео 3 RT', url='https://rutube.ru/video/private/3215ac6d83601e1379b250b47a6decfe/?p=Ybvz44OjWSZA-c_DWYYAww'),
     InlineKeyboardButton(text='Лаб. работа 3', callback_data='Лабораторная работа 23')],

    [InlineKeyboardButton(text='Назад', callback_data='2 модуль')]
])


@router_module_2.callback_query(F.data == 'Материал лаб. работ2')
async def lect_2(callback: CallbackQuery):
    await callback.message.edit_text('Раздел лабораторных работ 2 модуля', reply_markup=keyboard_labs)
    await callback.answer()


@router_module_2.callback_query(F.data.startswith('Лабораторная работа 2'))
async def lab_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        number = int(callback.data[-1])
        match number:
            case 1:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOuZ6DcCL56koCMej5TPuHDL7tQoLUAAtVlAAIO_AlJwI-3nlas_3U2BA')
            case 2:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOwZ6DcIO0B81W42R3sr4N2kSzCW8oAAthlAAIO_AlJrwAB1VFPQa3BNgQ')
            case 3:
                await callback.message.answer_document(document='BQACAgIAAxkBAAOyZ6DcNMWYaZye5wj33TjmRiD_BPMAAttlAAIO_AlJV0ftgb-Y9Cs2BA')
        await callback.message.answer('Раздел лабораторных работ 2 модуля', reply_markup=keyboard_labs)
        await callback.answer()


keyboard_self = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Голос в текст YT', url='https://youtu.be/wN_ZD8wVpuo'),
     InlineKeyboardButton(
         text='Голос в текст RT', url='https://rutube.ru/video/private/f01a347c8e63e6fe00b5d9f6f1eed0ed/?p=YnJUE3PeDT_tmoHHMve4wQ')],

    [InlineKeyboardButton(text='Разговор с ИИ YT', url='https://youtu.be/ebjlj95BnFo'),
     InlineKeyboardButton(
         text='Разговор с ИИ RT', url='https://rutube.ru/video/private/cb9afb70e2c5631de2115ebf60c56391/?p=hO3ZBiOCbLGAyn1Zm4xGZw')],

    [InlineKeyboardButton(text='Назад', callback_data='2 модуль')]
])


@router_module_2.callback_query(F.data == 'Материалы сам. работ2')
async def self_2(callback: CallbackQuery):
    await callback.message.edit_text('Раздел материалов для самостоятельной работы 2 модуля', reply_markup=keyboard_self)
    await callback.answer()


keyboard_add = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Человек vs ИИ',
                          url='https://vas3k.blog/blog/ai_alignment/')],
    [InlineKeyboardButton(text='Как работает ChatGPT',
                          url='https://habr.com/ru/companies/ods/articles/716918/')],
    [InlineKeyboardButton(text='Prompt Engineering Cheat Sheet',
                          url='https://big-picture.com/media/the_prompt_engineering_cheat_sheet.pdf')],
    [InlineKeyboardButton(text='A Systematic Survey',
                          url='https://arxiv.org/abs/2406.06608')],
    [InlineKeyboardButton(text='LLaMA-1/2, GPT-3.5/4',
                          url='https://arxiv.org/abs/2312.16171v2')],
    [InlineKeyboardButton(text='Generative AI',
                          url='https://ig.ft.com/generative-ai/')],
    [InlineKeyboardButton(text='Alice’s Adventures',
                          url='https://arxiv.org/pdf/2404.17625')],
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

    [InlineKeyboardButton(text='Назад', callback_data='2 модуль')]
])


@router_module_2.callback_query(F.data == 'Доп. материал2')
async def add_2(callback: CallbackQuery):
    await callback.message.edit_text('Раздел дополнительных материалов 2 модуля', reply_markup=keyboard_add)
    await callback.answer()
