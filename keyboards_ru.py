from aiogram import types



def choose_native_lang():
    buttons = [
        [types.InlineKeyboardButton(text='Русский', callback_data='ru_native')],
        ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def will_learn_lang():
    buttons = [
        [types.InlineKeyboardButton(text='🇺🇸 English', callback_data='usa')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def word():
    buttons = [
        [types.InlineKeyboardButton(text='Учим!', callback_data='learn_word')],
        [types.InlineKeyboardButton(text='Знаю', callback_data='know')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def repeat1():
    buttons = [
        [types.InlineKeyboardButton(text="Поехали!", callback_data='repeat1')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def repeat2():
    buttons = [
        [types.InlineKeyboardButton(text="Поехали!", callback_data='repeat2')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def repeat3():
    buttons = [
        [types.InlineKeyboardButton(text="Поехали!", callback_data='repeat3')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def repeat4():
    buttons = [
        [types.InlineKeyboardButton(text="Поехали!", callback_data='repeat4')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def menu_ru():
    buttons = [
        [types.InlineKeyboardButton(text='Информация', callback_data='info_lang')],
        [types.InlineKeyboardButton(text='Настройки', callback_data='settings')],
        [types.InlineKeyboardButton(text='Мой словарь', callback_data='my_dict')],
        [types.InlineKeyboardButton(text='Начать!', callback_data='start_learn')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def my_dict():
    buttons = [
        [types.InlineKeyboardButton(text='Назад', callback_data='back')],
        [types.InlineKeyboardButton(text='Добавить словосочетание', callback_data='add_word')],
        [types.InlineKeyboardButton(text='Вывести список в чат', callback_data='print_my_words')],
        [types.InlineKeyboardButton(text='Учить мои слова', callback_data='learn_my_words')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def level():
    buttons = [
        [types.InlineKeyboardButton(text="Я начинающий", callback_data='A0')],
        [types.InlineKeyboardButton(text='A1', callback_data='A1'),
        types.InlineKeyboardButton(text='A2', callback_data='A2')],
        [types.InlineKeyboardButton(text='B1', callback_data='B1'),
        types.InlineKeyboardButton(text='B2', callback_data='B2')],
        [types.InlineKeyboardButton(text='C1', callback_data='C1')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def info_lang():
    buttons = [
        [types.InlineKeyboardButton(text='Назад', callback_data='back')],
        [types.InlineKeyboardButton(text='% изучения уровня', callback_data='level_info')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def settings():
    buttons = [
        [types.InlineKeyboardButton(text='Назад', callback_data='back')],
        [types.InlineKeyboardButton(text='Изменить уровень', callback_data='change_level')],
        [types.InlineKeyboardButton(text='Выбрать тематику слов', callback_data='choose_theme')],
        [types.InlineKeyboardButton(text='Изменить число изучаемых слов за сеанс', callback_data='update_quantity_words')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def change_level():
    buttons = [
        [types.InlineKeyboardButton(text='Назад', callback_data='back_to_settings')],
        [types.InlineKeyboardButton(text='Повысить уровень', callback_data='up_level')],
        [types.InlineKeyboardButton(text='Понизить уровень', callback_data='down_level')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choose_theme():
    buttons = [
        [types.InlineKeyboardButton(text='Назад', callback_data='back_to_settings')],
        [types.InlineKeyboardButton(text='Сельское хозяйство', callback_data='agro')],
        [types.InlineKeyboardButton(text='Продолжить изучать слова текущего уровня',
                                    callback_data='сontinue_to_study_the_words')],
        [types.InlineKeyboardButton(text='Я просто хочу выучить 5000 слов', callback_data='5000')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
