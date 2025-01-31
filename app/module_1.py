from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router_module_1 = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции1'),
     InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ1')],

    [InlineKeyboardButton(text='Материалы сам. работ', callback_data='Материалы сам. работ1'),
     InlineKeyboardButton(text='Доп. материал', callback_data='Доп. материал1')],

    [InlineKeyboardButton(text='Файл с материалами', callback_data='Файл с материалами1'),
     InlineKeyboardButton(text='Тестирование', url='https://e.vyatsu.ru/mod/quiz/view.php?id=771800')],

    [InlineKeyboardButton(text='Выбор модуля', callback_data='Меню')],
])

message_text = '1 модуль - Принципы функционирования нейронных сетей\nhttps://e.vyatsu.ru/course/view.php?id=33681'


@router_module_1.callback_query(F.data == '1 модуль')
async def module_1(callback: CallbackQuery):
    await callback.message.edit_text(message_text, reply_markup=keyboard)
    await callback.answer()


@router_module_1.callback_query(F.data == 'Файл с материалами1')
async def file_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer_document(document='BQACAgIAAxkBAAMaZ50vH3snoqMPOnGdkRddINLb5EAAAottAALX4ulILUe9B8TiAfk2BA')
        await callback.message.answer(message_text, reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/OSXpXOqKiGU'),
     InlineKeyboardButton(
         text='Видео 1 RT', url='https://rutube.ru/video/private/1e77666d3cb68406e6c05b599c4598f7/?p=DCflDPEpn6AH1KioMWZcJg'),
     InlineKeyboardButton(text='Материал 1', callback_data='Материал 11')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/KgPuIZ-HBvA'),
     InlineKeyboardButton(
         text='Видео 2 RT', url='https://rutube.ru/video/private/cbe72d0aa511b3a5d5266a9c02a97e79/?p=ICxvKISFS52id8xxfOdK9w'),
     InlineKeyboardButton(text='Материал 2', callback_data='Материал 12')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/ZV5K9AikLL4'),
     InlineKeyboardButton(
         text='Видео 3 RT', url='https://rutube.ru/video/private/7f8987f5485adde4db28341fe99fa738/?p=iSG6TCb_8KcK3MpZE__eZA'),
     InlineKeyboardButton(text='Материал 3', callback_data='Материал 13')],

    [InlineKeyboardButton(text='Видео 4 YT', url='https://youtu.be/ixk86HiLCzk'),
     InlineKeyboardButton(
        text='Видео 4 RT', url='https://rutube.ru/video/private/e12b5dca3c321b012f1e32f8df1da8e4/?p=5PEHTGOQl7-MPG4YQPbJcA'),
     InlineKeyboardButton(text='Материал 4', callback_data='Материал 14')],

    [InlineKeyboardButton(text='Видео 5 YT', url='https://youtu.be/r0tFiOkuBHs'),
     InlineKeyboardButton(
        text='Видео 5 RT', url='https://rutube.ru/video/private/a044287441c1b35d9fb59a41a48299eb/?p=TVT-lhVBGl5C3L-zOFfEaQ'),
     InlineKeyboardButton(text='Материал 5', callback_data='Материал 15')],

    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
])


@router_module_1.callback_query(F.data == 'Лекции1')
async def lect_1(callback: CallbackQuery):
    await callback.message.edit_text('Раздел лекций 1 модуля', reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_1.callback_query(F.data.startswith('Материал 1'))
async def material_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        number = int(callback.data[-1])
        match number:
            case 1:
                await callback.message.answer_document(document='BQACAgIAAxkBAAMsZ50wBT0tyarMCUr8kVaVy6R_atMAApVtAALX4ulIhZN3KTxS76k2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAMuZ50wCLitPFBRuTm4VvsJBzqtU0gAApZtAALX4ulIfFO2xI6J-hg2BA')
            case 2:
                await callback.message.answer_document(document='BQACAgIAAxkBAAMwZ50wLW8NidKL9AnrKkMIvelRdNsAAphtAALX4ulIq_5IQ4Z62342BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAMyZ50wMKQn4o7dyKQN9UFy2lyIhPwAApltAALX4ulISRH6Wqml1SU2BA')
            case 3:
                await callback.message.answer_document(document='BQACAgIAAxkBAAM0Z50wTY97VcbxERV-gLUS7SSpg3gAApptAALX4ulIqIoQKNAtcKI2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAM2Z50wUMhpySvCov7u1o6BTQABWiRjAAKbbQAC1-LpSIcFTznYzGWkNgQ')
            case 4:
                await callback.message.answer_document(document='BQACAgIAAxkBAAM4Z50wblCgCfhjMx778kbiW064FqcAAp1tAALX4ulIQhhG6pp4AVw2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAM6Z50wceSVLzsxc2J3qO5CFI9MklYAAp5tAALX4ulIX6Bc-I7FqNI2BA')
            case 5:
                await callback.message.answer_document(document='BQACAgIAAxkBAAM8Z50wkBzwEnNQSJ3gmR50orazZ5sAAp9tAALX4ulIiYHi5DTVyVQ2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAAM-Z50wlUpVWu1FxBG3Hwaa_RzOSnEAAqBtAALX4ulI83IpNdUBVQQ2BA')
                await callback.message.answer_document(document='BQACAgIAAxkBAANAZ50wlhyMv8FB-As5pAboLQw0kpIAAqFtAALX4ulIV2HalSlwaq42BA')

        await callback.message.answer('Раздел лекций 1 модуля', reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1 YT', url='https://youtu.be/_WEejmL6ogc'),
     InlineKeyboardButton(
         text='Видео 1 RT', url='https://rutube.ru/video/private/ad2a6bce041274809af5accf5d50b350/?p=3P6lrHAoZX3hbI-kmY209g'),
     InlineKeyboardButton(text='Лаб. работа 1', callback_data='Лабораторная работа 11')],

    [InlineKeyboardButton(text='Видео 2 YT', url='https://youtu.be/saD6WFgA0n4'),
     InlineKeyboardButton(
         text='Видео 2 RT', url='https://rutube.ru/video/private/4278982a1f0f6313c8fd8b4944b985ea/?r=wd&p=VoWNY1u7y3G8BTa79QAlcA'),
     InlineKeyboardButton(text='Лаб. работа 2', callback_data='Лабораторная работа 12')],

    [InlineKeyboardButton(text='Видео 3 YT', url='https://youtu.be/YdUithseiGg'),
     InlineKeyboardButton(
         text='Видео 3 RT', url='https://rutube.ru/video/private/65354c258bb04857e0dbcc0c6939eccf/?r=wd&p=UpVDPM4q4UFeU0rpE981DA'),
     InlineKeyboardButton(text='Лаб. работа 3', callback_data='Лабораторная работа 13')],

    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
])


@router_module_1.callback_query(F.data == 'Материал лаб. работ1')
async def lect_1(callback: CallbackQuery):
    await callback.message.edit_text('Раздел лабораторных работ 1 модуля', reply_markup=keyboard_labs)
    await callback.answer()


@router_module_1.callback_query(F.data.startswith('Лабораторная работа 1'))
async def lab_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        number = int(callback.data[-1])
        match number:
            case 1:
                await callback.message.answer_document(document='BQACAgIAAxkBAANUZ50xFMG6U9c0FNpOWpnFnhjY0E0AAqZtAALX4ulI1OErKc9x94s2BA')
            case 2:
                await callback.message.answer_document(document='BQACAgIAAxkBAANWZ50xF1qVYH5LqhL0qYya8wt5i_IAAqdtAALX4ulIFiKow8LQ0dE2BA')
            case 3:
                await callback.message.answer_document(document='BQACAgIAAxkBAANYZ50xGuQnC4h48Za7wMWMEvkTwv8AAqhtAALX4ulIZSxAv2ZuvCw2BA')
        await callback.message.answer('Раздел лабораторных работ 1 модуля', reply_markup=keyboard_labs)
        await callback.answer()


keyboard_self = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Правила разговора YT', url='https://youtu.be/zjOfNjTwGxw'),
     InlineKeyboardButton(
         text='Правила разговора RT', url='https://rutube.ru/video/private/1eee339244e1903b76439dd578e16cc9/?p=W5EmclUp76OG5_EFoTUe3A')],

    [InlineKeyboardButton(text='Обучай быстрее YT', url='https://youtu.be/GRo9UPf4T4g'),
     InlineKeyboardButton(
         text='Обучай быстрее RT', url='https://rutube.ru/video/private/dd54d16205c05c41645829240a3a27d8/?p=niFHlkb-aQBFvkJIN7ni0Q')],

    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
])


@router_module_1.callback_query(F.data == 'Материалы сам. работ1')
async def self_1(callback: CallbackQuery):
    await callback.message.edit_text('Раздел материалов для самостоятельной работы 1 модуля', reply_markup=keyboard_self)
    await callback.answer()


keyboard_add = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекция. Генеративные модели, автоэнкодеры',
                          url='https://youtu.be/6qVfC7P9dEc')],
    [InlineKeyboardButton(text='Учебник по NLP',
                          url='https://lena-voita.github.io/nlp_course.html')],
    [InlineKeyboardButton(text='Раздел по нейронным сетям',
                          url='https://education.yandex.ru/handbook/ml/article/nejronnye-seti')],
    [InlineKeyboardButton(text='Руковоство по промпт-иинжирингу',
                          url='https://www.promptingguide.ai/ru')],
    [InlineKeyboardButton(text='Про RAG',
                          url='https://python.langchain.com/v0.1/docs/use_cases/question_answering/')],
    [InlineKeyboardButton(text='Распознавание почтовых индексов',
                          url='http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf')],
    [InlineKeyboardButton(text='Статья про GAN',
                          url='https://arxiv.org/abs/1406.2661')],
    [InlineKeyboardButton(text='Статья про трансформеры',
                          url='https://arxiv.org/abs/1706.03762')],
    [InlineKeyboardButton(text='Статья про Bert',
                          url='https://arxiv.org/abs/1810.04805')],
    [InlineKeyboardButton(text='Статья про T5',
                          url='https://arxiv.org/abs/1910.10683')],
    [InlineKeyboardButton(text='Статья про GPT-3',
                          url='https://arxiv.org/pdf/2005.14165')],
    [InlineKeyboardButton(text='Статья про GPT-4',
                          url='https://arxiv.org/pdf/2303.08774')],
    [InlineKeyboardButton(text='Статья про LLaMA-2',
                          url='https://arxiv.org/abs/2307.09288')],
    [InlineKeyboardButton(text='Объяснение работы трансформера',
                          url='https://jalammar.github.io/illustrated-transformer/')],
    [InlineKeyboardButton(text='Проект CycleGAN',
                          url='https://junyanz.github.io/CycleGAN/')],
    [InlineKeyboardButton(text='Fisher Iris',
                          url='https://www.kaggle.com/datasets/uciml/iris')],
    [InlineKeyboardButton(text='MNIST',
                          url='https://www.kaggle.com/datasets/oddrationale/mnist-in-csv')],
    [InlineKeyboardButton(text='Russian SuperGLUE',
                          url='https://russiansuperglue.com/')],
    [InlineKeyboardButton(text='RuCoLa',
                          url='https://rucola-benchmark.com/')],
    [InlineKeyboardButton(text='TAPE',
                          url='https://tape-benchmark.com/')],
    [InlineKeyboardButton(text='MERA',
                          url='https://mera.a-ai.ru/ru')],

    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
])


@router_module_1.callback_query(F.data == 'Доп. материал1')
async def add_1(callback: CallbackQuery):
    await callback.message.edit_text('Раздел дополнительных материалов 1 модуля', reply_markup=keyboard_add)
    await callback.answer()
