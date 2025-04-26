from aiogram import Router, types, F
from aiogram.filters import Command
import text_ru as text
import keyboards_ru as keyboards
import db
import asyncio
from aiogram.fsm.context import FSMContext
from utils import Registration, New_quantity_words, Learn_words, CorrectAnswer, Exercise, Repeat, Mydict
from openai import OpenAI
import random as r
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import json


router = Router()
users = db.Users('users')
study_words_user = db.User_study_words('study_words_user')
usa = db.DataBase_words_language('usa')
rus = db.DataBase_words_language('rus')
client = OpenAI(
  api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjQxMGEwYzQ5LWY4ZTUtNDhmNS04Y2Y5LWFmMWY4YWE3NTcxYiIsImlzRGV2ZWxvcGVyIjp0cnVlLCJpYXQiOjE3Mjk2MDk1NTksImV4cCI6MjA0NTE4NTU1OX0.FhQBjXT-hrTOhTwclY1yKPXs4M-dCLsx3MLlKi2TjjE',
  base_url='https://bothub.chat/api/v2/openai/v1')

@router.message(Command('start'))
async def start_handler(msg, state: FSMContext):
    await msg.answer(text=text.choose_language.format(name=msg.from_user.first_name),
                     reply_markup=keyboards.will_learn_lang())


@router.callback_query(F.data == 'ru_native')
async def ru_native(callback, state: FSMContext):
    await state.update_data(native_lang='русский')
    await callback.message.edit_text(text=text.choose_language,
                                     reply_markup=keyboards.will_learn_lang())


@router.callback_query(F.data == 'en_native')
async def en_native(callback, state: FSMContext):
    await state.update_data(native_lang='english')
    await callback.message.edit_text(text=text.choose_language,
                                     reply_markup=keyboards.will_learn_lang())


@router.callback_query(F.data == 'usa')
async def will_learn_lang_usa(callback, state: FSMContext):
    await state.update_data(native_lang='русский')
    await state.update_data(will_learn_lang='usa')
    await callback.message.edit_text(text=text.level,
                                     reply_markup=keyboards.level())


@router.callback_query(F.data == 'spain')
async def will_learn_lang_spain(callback, state: FSMContext):
    await state.update_data(native_lang='русский')
    await state.update_data(will_learn_lang='spain')
    await callback.message.edit_text(text=text.level,
                                     reply_markup=keyboards.level())


@router.callback_query(F.data == 'rus')
async def will_learn_lang_spain(callback, state: FSMContext):
    await state.update_data(will_learn_lang='rus')
    await callback.message.edit_text(text=text.level,
                                     reply_markup=keyboards.level())


@router.callback_query(F.data == 'A0')
async def level0(callback, state: FSMContext):
    await state.update_data(level='A1')
    await state.set_state(Registration.quantity_words)
    await callback.message.edit_text(text=text.range_learn_words)


@router.callback_query(F.data == 'A1')
async def level1(callback, state: FSMContext):
    await state.update_data(level='A1')
    await state.set_state(Registration.quantity_words)
    await callback.message.edit_text(text=text.range_learn_words)


@router.callback_query(F.data == 'A2')
async def level2(callback, state: FSMContext):
    await state.update_data(level='A2')
    await state.set_state(Registration.quantity_words)
    await callback.message.edit_text(text=text.range_learn_words)


@router.callback_query(F.data == 'B1')
async def level3(callback, state: FSMContext):
    await state.update_data(level='B1')
    await state.set_state(Registration.quantity_words)
    await callback.message.edit_text(text=text.range_learn_words)


@router.callback_query(F.data == 'B2')
async def level4(callback, state: FSMContext):
    await state.update_data(level='B2')
    await state.set_state(Registration.quantity_words)
    await callback.message.edit_text(text=text.range_learn_words)


@router.callback_query(F.data == 'C1')
async def level5(callback, state: FSMContext):
    await state.update_data(level='C1')
    await state.set_state(Registration.quantity_words)
    await callback.message.edit_text(text=text.range_learn_words)


@router.callback_query(F.data == 'C2')
async def level6(callback, state: FSMContext):
    await state.update_data(level='C2')
    await state.set_state(Registration.quantity_words)
    await callback.message.edit_text(text=text.range_learn_words)


@router.message(Registration.quantity_words)
async def quantity_words(msg, state: FSMContext):
    if 4 < int(msg.text) < 31:
        await state.update_data(quantity_words=int(msg.text))
        await msg.answer(text.success)
        await msg.answer(text=text.menu,
                         reply_markup=keyboards.menu_ru())
        data = await state.get_data()
        await state.clear()
        user_id = msg.from_user.id
        if user_id not in users.get_users_ids():
            users.add_user_info(user_id, data)
            level = users.get_level(user_id)
            db.Users_words(user_id)
            if data['will_learn_lang'] == 'usa':
                words = usa.get_words_level(level)
                study_words_user.add_words_study_level(user_id, words)
            elif data['will_learn_lang'] == 'spain':
                pass
            elif data['will_learn_lang'] == 'rus':
                words = rus.get_words_level(level)
                study_words_user.add_words_study_level(user_id, words)
    else:
        await msg.answer(text=text.range_learn_words_2)


@router.message(F.text.startswith('/'))
async def start_handler_02(msg):
    await msg.answer(text=text.menu,
                     reply_markup=keyboards.menu_ru())


@router.callback_query(F.data == 'info_lang')
async def info_lang(callback):
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboards.info_lang())


@router.callback_query(F.data == 'back_to_settings')
async def back_to_settings(callback):
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboards.settings())


@router.callback_query(F.data == 'back')
async def back(callback):
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboards.menu_ru())


@router.callback_query(F.data == 'level_info')
async def level_info(callback, bot):
    user_id = callback.from_user.id
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboards.menu_ru())
    info = study_words_user.get_percent_of_level(user_id)
    await bot.send_message(chat_id=user_id,
                           text=text.level_info.format(num=info))


@router.callback_query(F.data == 'settings')
async def settings(callback):
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboards.settings())


@router.callback_query(F.data == 'choose_theme')
async def settings(callback):
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboards.choose_theme())


@router.callback_query(F.data == 'change_level')
async def change_level(callback):
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboards.change_level())


@router.callback_query(F.data == 'my_dict')
async def my_dict(callback):
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboards.my_dict())


@router.callback_query(F.data == 'change_language')
async def change_language(callback):
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboards.will_learn_lang_for_ru())


@router.callback_query(F.data == 'update_quantity_words')
async def update_quantity_words(callback, bot, state: FSMContext):
    await bot.send_message(chat_id=callback.from_user.id,
                           text=text.range_learn_words)
    await state.set_state(New_quantity_words.quantity_words)
    await callback.answer()


@router.callback_query(F.data == 'print_my_words')
async def print_my_words(callback, bot, state: FSMContext):
    user_id = callback.from_user.id
    db.Users_dicts(user_id)
    words = db.Users_dicts.get_words('table_' + str(user_id))
    if words:
        await bot.send_message(chat_id=user_id,
                               text='Ваши слова:\n\n' + words)
        await callback.answer()
    else:
        await bot.send_message(chat_id=user_id,
                               text=text.empty_dict)
        await callback.answer()


@router.callback_query(F.data == 'learn_my_words')
async def learn_my_words(callback, bot, state: FSMContext):
    user_id = callback.from_user.id
    db.Users_dicts(user_id)
    words = db.Users_dicts.get_words('table_' + str(user_id))
    await callback.answer()
    if words:
        study_words_user.update_words_study_level(user_id, words)
        await start_learn(callback, state, bot)
    else:
        await bot.send_message(chat_id=user_id,
                               text=text.empty_dict)


@router.callback_query(F.data == 'add_word')
async def add_word(callback, bot, state: FSMContext):
    user_id = callback.from_user.id
    db.Users_dicts(user_id)
    await bot.send_message(chat_id=callback.from_user.id,
                           text=text.enter_u_word1)
    await state.set_state(Mydict.en_word)
    await callback.answer()


@router.message(Mydict.en_word)
async def en_word(msg, state: FSMContext, bot):
    user_id = msg.from_user.id
    await state.update_data(en_word=msg.text.lower())
    await state.set_state(Mydict.ru_word)
    await bot.send_message(chat_id=user_id,
                           text=text.enter_u_word2)


@router.message(Mydict.ru_word)
async def ru_word(msg, state: FSMContext, bot):
    user_id = msg.from_user.id
    await state.update_data(ru_word=msg.text.lower())
    data = await state.get_data()
    await state.clear()
    word = data['en_word'] + '-' + data['ru_word']
    db.Users_dicts.add_word('table_' + str(user_id), word)
    await bot.send_message(chat_id=user_id,
                           text=text.enter_u_word3)


@router.message(New_quantity_words.quantity_words)
async def new_quantity_words(msg, state: FSMContext, bot):
    if 4 < int(msg.text) < 31:
        user_id = msg.from_user.id
        users.new_quantity_words(user_id, int(msg.text))
        await bot.send_message(chat_id=user_id,
                               text=text.successfully)
        await bot.send_message(chat_id=user_id,
                               text=text.menu,
                               reply_markup=keyboards.menu_ru())
    else:
        await msg.answer(text=text.range_learn_words_2)


@router.callback_query(F.data == 'up_level')
async def up_level(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    lang = users.get_learn_lang(user_id)
    level = users.get_level(user_id)
    if level in ('C1',):
        await callback.answer(text=text.maximum)
        await bot.send_message(chat_id=user_id,
                               text=text.menu,
                               reply_markup=keyboards.menu_ru())
    else:
        users.increase_level(user_id)
        level = users.get_level(user_id)
        if lang == 'usa':
            words = usa.get_words_level(level)
            study_words_user.update_words_study_level(user_id, words)
        elif lang == 'spain':
            pass
        elif lang == 'rus':
            words = rus.get_words_level(level)
            study_words_user.update_words_study_level(user_id, words)
        await callback.answer(text=text.raised.format(level=level))
        await bot.send_message(chat_id=user_id,
                               text=text.menu,
                               reply_markup=keyboards.menu_ru())


@router.callback_query(F.data == 'down_level')
async def down_level(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    lang = users.get_learn_lang(user_id)
    level = users.get_level(user_id)
    if level in ('A1',):
        await callback.answer(text=text.minimum)
        await bot.send_message(chat_id=user_id,
                               text=text.menu,
                               reply_markup=keyboards.menu_ru())
    else:
        users.reduce_level(user_id)
        level = users.get_level(user_id)
        if lang == 'usa':
            words = usa.get_words_level(level)
            study_words_user.update_words_study_level(user_id, words)
        elif lang == 'spain':
            pass
        elif lang == 'rus':
            words = rus.get_words_level(level)
            study_words_user.update_words_study_level(user_id, words)
        await callback.answer(text=text.lowered.format(level=level))
        await bot.send_message(chat_id=user_id,
                                   text=text.menu,
                                             reply_markup=keyboards.menu_ru())


@router.callback_query(F.data == '5000')
async def l5000(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    lang = users.get_learn_lang(user_id)
    users.update_theme(user_id, '5000')
    if lang == 'usa':
        words = usa.get_words_level('5000')
        study_words_user.update_words_study_level(user_id, words)
        await callback.answer(text=text.successfully)
        await bot.send_message(chat_id=user_id,
                               text=text.menu,
                               reply_markup=keyboards.menu_ru())
    else:
        await bot.send_message(user_id, text=text.sorry)


@router.callback_query(F.data == 'agro')
async def agro(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    lang = users.get_learn_lang(user_id)
    users.update_theme(user_id, 'agro')
    if lang == 'usa':
        words = usa.get_words_level('agro')
        study_words_user.update_words_study_level(user_id, words)
        await callback.answer(text=text.successfully)
        await bot.send_message(chat_id=user_id,
                               text=text.menu,
                               reply_markup=keyboards.menu_ru())
    else:
        await bot.send_message(user_id, text=text.sorry)


@router.callback_query(F.data == 'сontinue_to_study_the_words')
async def сontinue_to_study_the_words(callback, state: FSMContext, bot):
    data = await state.get_data()
    user_id = callback.from_user.id
    lang = users.get_learn_lang(user_id)
    level = users.get_level(user_id)
    if lang == 'usa':
        words = usa.get_words_level(level)
        study_words_user.update_words_study_level(user_id, words)
        await callback.answer()
        await bot.send_message(chat_id=user_id,
                               text=text.menu,
                               reply_markup=keyboards.menu_ru())
    elif lang == 'rus':
        words = rus.get_words_level(level)
        study_words_user.update_words_study_level(user_id, words)
        await callback.answer()
        await bot.send_message(chat_id=user_id,
                               text=text.menu,
                               reply_markup=keyboards.menu_ru())
    else:
        await bot.send_message(user_id, text.sorry)


@router.callback_query(F.data == 'start_learn')
async def start_learn(callback, state: FSMContext, bot):
    await state.update_data(quantity_words_2=None)
    user_id = callback.from_user.id
    words = study_words_user.get_words(user_id)
    db.Users_words(user_id)
    await callback.message.delete()
    if not words:
        await bot.send_message(chat_id=user_id,
                               text=text.all_words_learned)
    else:
        number = len(words)
        quantity = users.get_quantity_words(user_id)
        if number <= quantity:
            await state.update_data(quantity_words_2=number)
            data = await state.get_data()
            quantity = data['quantity_words_2']
            for i in range(quantity):
                word, translate = words[i].split('-', maxsplit=1)
                await bot.send_message(chat_id=user_id,
                                       text=text.translates.format(word=word, translate=translate),
                                       reply_markup=keyboards.word())
        else:
            for _ in range(quantity):
                word, translate = words[r.randint(0, number - 1)].split('-', maxsplit=1)
                await bot.send_message(chat_id=user_id,
                                       text=text.translates.format(word=word, translate=translate),
                                       reply_markup=keyboards.word())


@router.callback_query(F.data == 'know')
async def know(callback, state: FSMContext, bot):
    data = await state.get_data()
    user_id = callback.from_user.id
    word = '-'.join(callback.message.text.split(text.word_split))
    study_words_user.add_learnt_word(user_id, word)
    if data['quantity_words_2']:
        await state.update_data(quantity_words_2=data['quantity_words_2'] - 1)
        await callback.message.delete()
        words = study_words_user.get_words(user_id)
        if not words:
            await bot.send_message(chat_id=user_id,
                                   text=text.all_words_learned)
    else:
        words = study_words_user.get_words(user_id)
        number = len(words)
        await callback.message.delete()
        word, translate = words[r.randint(0, number)].split('-', maxsplit=1)
        await bot.send_message(chat_id=user_id,
                                   text=text.translates.format(word=word, translate=translate),
                                   reply_markup=keyboards.word())


@router.callback_query(F.data == 'learn_word')
async def learn_word(callback, state: FSMContext, bot):
    data = await state.get_data()
    user_id = callback.from_user.id
    word = '-'.join(callback.message.text.split(text.word_split))
    study_words_user.add_learning_word(user_id, word)
    study_words_user.add_word_in_process(user_id, word)
    if data['quantity_words_2']:
        quantity = data['quantity_words_2']
    else:
        quantity = users.get_quantity_words(user_id)
    quantity_learning_words = study_words_user.get_len_learning_words(user_id)
    await callback.message.delete()
    if quantity_learning_words == quantity:
        words = study_words_user.get_learning_words(user_id)
        all_words = words.copy()
        timer = 0
        study_words_user.delete_learning_words(user_id)
        await bot.send_message(chat_id=user_id,
                               text=text.Exercise_1)
        await starting_learn_words_1(timer, user_id, quantity, words, all_words, bot, state)


async def starting_learn_words_3(timer, bot, user_id, quantity, words, all_words, state):
    if words:
        word, translation = words.pop(r.randint(0, len(words) - 1)).split('-')
        await state.update_data(good=(word, translation, timer, bot, user_id, quantity, words, all_words, state))
        message  = await bot.send_message(user_id, text.write.format(translation=translation))
        await state.update_data(attempt=message)
        await state.set_state(Exercise.three)
    else:
        await state.clear()
        if timer > 3:
            await bot.send_message(chat_id=user_id,
                                   text=text.Congratulations)
            study_words_user.delete_words_in_process(user_id, len(words))
            await bot.send_message(chat_id=user_id,
                                   text=text.menu,
                                   reply_markup=keyboards.menu_ru())
            for word in words:
                study_words_user.add_learnt_word(user_id, word)
        else:
            level = users.get_level(user_id)
            response = client.chat.completions.create(
                messages=[
                    {'role': 'system',
                     'content': 'Ты — учитель английского языка.'},
                    {
                        'role': 'user',
                        'content': f"Напиши по одной фразе использования слова из списка {all_words} на английсков языке если бы твой уровень владения английским был бы уровня {level}. Напиши только фразу и через дефис перевод без лишних слов.",
                    }
                ],
                model='deepseek-chat-v3-0324:free',
            )
            await bot.send_message(chat_id=user_id,
                                   text=f"Примеры использования изученных слов!\n\n{response.choices[0].message.content}")
            await bot.send_message(chat_id=user_id,
                                   text=text.reminder)
            await bot.send_message(chat_id=user_id,
                                   text=text.menu,
                                   reply_markup=keyboards.menu_ru())
            words = all_words.copy()
            if timer == 0:
                info = (timer + 1, bot, user_id, quantity, words, all_words)
                await repeat_1(*info, state=state)
            elif timer == 1:
                info = (timer + 1, bot, user_id, quantity, words, all_words)
                await repeat_2(*info, state=state)
            elif timer == 2:
                info = (timer + 1, bot, user_id, quantity, words, all_words)
                await repeat_3(*info, state=state)
            elif timer == 3:
                info = (timer + 1, bot, user_id, quantity, words, all_words)
                await repeat_4(*info, state=state)


async def repeat_1(timer, bot, user_id, quantity, words, all_words, state: FSMContext):
    info = json.dumps((timer, user_id, quantity, words, all_words))
    db.Users_words.add_user_info('table_' + str(user_id), info, timer)
    await asyncio.sleep(1800) #1800 = 30 minutes
    await bot.send_message(chat_id=user_id,
                           text=text.Repeat,
                           reply_markup=keyboards.repeat1())


async def repeat_2(timer, bot, user_id, quantity, words, all_words, state: FSMContext):
    info = json.dumps((timer, user_id, quantity, words, all_words))
    info_old = json.dumps((timer - 1, user_id, quantity, words, all_words))
    db.Users_words.update_words('table_' + str(user_id), info_old, info,2)
    await asyncio.sleep(28800)  # 28800 8hours
    await bot.send_message(chat_id=user_id,
                           text=text.Repeat,
                           reply_markup=keyboards.repeat2())


async def repeat_3(timer, bot, user_id, quantity, words, all_words, state: FSMContext):
    info = json.dumps((timer, user_id, quantity, words, all_words))
    info_old = json.dumps((timer - 1, user_id, quantity, words, all_words))
    db.Users_words.update_words('table_' + str(user_id), info_old, info, 3)
    await asyncio.sleep(86400)  # 86400 24hours
    await bot.send_message(chat_id=user_id,
                           text=text.Repeat,
                           reply_markup=keyboards.repeat3())


async def repeat_4(timer, bot, user_id, quantity, words, all_words, state: FSMContext):
    info = json.dumps((timer, user_id, quantity, words, all_words))
    info_old = json.dumps((timer - 1, user_id, quantity, words, all_words))
    db.Users_words.update_words('table_' + str(user_id), info_old, info,4)
    await asyncio.sleep(259200) #259200 3days
    await bot.send_message(chat_id=user_id,
                           text=text.Repeat,
                           reply_markup=keyboards.repeat4())


@router.callback_query(F.data == 'repeat1')
async def repeat1(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    info = json.loads(db.Users_words.get_info('table_' + str(user_id), 1))
    await callback.message.delete()
    await starting_learn_words_1(*info, bot, state)


@router.callback_query(F.data == 'repeat2')
async def repeat2(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    info = json.loads(db.Users_words.get_info('table_' + str(user_id), 2))
    await callback.message.delete()
    await starting_learn_words_1(*info, bot, state)


@router.callback_query(F.data == 'repeat3')
async def repeat3(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    info = json.loads(db.Users_words.get_info('table_' + str(user_id), 3))
    await callback.message.delete()
    await starting_learn_words_1(*info, bot, state)


@router.callback_query(F.data == 'repeat4')
async def repeat4(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    info = json.loads(db.Users_words.get_info('table_' + str(user_id), 4))
    db.Users_words.delete_info('table_' + str(user_id), json.dumps(info), 4)
    await callback.message.delete()
    await starting_learn_words_1(*info, bot, state)


async def starting_learn_words_2(timer, user_id, quantity, words, all_words, bot, state):
    if words:
        d = {}
        for word in all_words:
            k, v = word.split('-')
            d.setdefault(v, k)
        translation, word = words.pop(r.randint(0, len(words) - 1)).split('-')
        await state.update_data(good=(word, translation, timer, bot, user_id, quantity, words, all_words, state))
        values_list = list(d.values())
        values_list.remove(translation)
        r.shuffle(values_list)
        buttons = [KeyboardButton(text=option) for option in values_list[:3]]
        correct_button = KeyboardButton(text=translation)
        buttons.insert(r.randint(0, 3), correct_button)
        if not words:
            message = await bot.send_message(user_id, f"{word} - ?",
                                             reply_markup=ReplyKeyboardMarkup(keyboard=[buttons[:2], buttons[2:]],
                                                                              resize_keyboard=True,
                                                                              one_time_keyboard=True))
        else:
            message  = await bot.send_message(user_id, f"{word} - ?",
                                              reply_markup=ReplyKeyboardMarkup(keyboard=[buttons[:2], buttons[2:]],
                                                                               resize_keyboard=True,
                                                                               one_time_keyboard=False))
        await state.update_data(attempt=(message, buttons))
        await state.set_state(Exercise.two)
    else:
        await bot.send_message(chat_id=user_id,
                               text=text.Exercise_3)
        words = all_words.copy()
        await starting_learn_words_3(timer, bot, user_id, quantity, words, all_words, state)


async def starting_learn_words_1(timer, user_id, quantity, words, all_words, bot, state):
    if words:
        d = {}
        for word in all_words:
            k, v = word.split('-')
            d.setdefault(k, v)
        word, translation = words.pop(r.randint(0, len(words) - 1)).split('-')
        await state.update_data(good=(word, translation,  timer, bot, user_id, quantity, words, all_words, state))
        values_list = list(d.values())
        values_list.remove(translation)
        r.shuffle(values_list)
        buttons = [KeyboardButton(text=option) for option in values_list[:3]]
        correct_button = KeyboardButton(text=translation)
        buttons.insert(r.randint(0, 3), correct_button)
        message  = await bot.send_message(user_id, f"{word} - ?",
                               reply_markup=ReplyKeyboardMarkup(keyboard=[buttons[:2], buttons[2:]],
                                                                resize_keyboard=True,
                                                                one_time_keyboard=False)                                          )
        await state.update_data(attempt=(message, buttons))
        await state.set_state(Exercise.one)
    else:
        await bot.send_message(chat_id=user_id,
                               text=text.Exercise_2)
        words = all_words.copy()
        await starting_learn_words_2(timer, user_id, quantity, words, all_words, bot, state)


@router.message(Exercise.one, F.text)
async def attempt(msg, state: FSMContext):
    data = await state.get_data()
    word, translation, timer, bot, user_id, quantity, words, all_words, state = data['good']
    message, buttons = data['attempt']
    if translation == msg.text:
        await msg.answer(r.choice(text.good_attempt))
        await starting_learn_words_1(timer, user_id, quantity, words, all_words, bot, state)
    else:
        await msg.answer(r.choice(text.bad_attempt))
        await bot.send_message(user_id, message.text,
                               reply_markup=ReplyKeyboardMarkup(keyboard=[buttons[:2], buttons[2:]],
                                                                resize_keyboard=True,
                                                                one_time_keyboard=False))
        await state.set_state(Exercise.one)


@router.message(Exercise.two, F.text)
async def attempt(msg, state: FSMContext):
    data = await state.get_data()
    word, translation, timer, bot, user_id, quantity, words, all_words, state = data['good']
    message, buttons = data['attempt']
    if translation == msg.text:
        await msg.answer(r.choice(text.good_attempt))
        await starting_learn_words_2(timer, user_id, quantity, words, all_words, bot, state)
    else:
        await msg.answer(r.choice(text.bad_attempt))
        if not words:
            await bot.send_message(user_id, message.text,
                                   reply_markup=ReplyKeyboardMarkup(keyboard=[buttons[:2], buttons[2:]],
                                                                resize_keyboard=True,
                                                                one_time_keyboard=True))
        else:
            await bot.send_message(user_id, message.text,
                                   reply_markup=ReplyKeyboardMarkup(keyboard=[buttons[:2], buttons[2:]],
                                                            resize_keyboard=True,
                                                            one_time_keyboard=False))
        await state.set_state(Exercise.two)


@router.message(Exercise.three, F.text)
async def attempt(msg, state: FSMContext):
    data = await state.get_data()
    word, translation, timer, bot, user_id, quantity, words, all_words, state = data['good']
    message = data['attempt']
    if word == msg.text.lower():
        await msg.answer(r.choice(text.good_attempt))
        await starting_learn_words_3(timer, bot, user_id, quantity, words, all_words, state)
    else:
        await msg.answer(r.choice(text.bad_attempt))
        await bot.send_message(user_id, message.text)
        await state.set_state(Exercise.three)


@router.message(F.text)
async def any_text(msg):
    await msg.answer(text.incomprehensible_set_of_characters)
