from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    native_lang = State()
    will_learn_lang = State()
    level = State()
    quantity_words = State()

class New_quantity_words(StatesGroup):
    quantity_words = State()


class Learn_words(StatesGroup):
    repeat = State()
    info = State()
    now = State()
    after_30min = State()
    after_8h = State()
    after_1d = State()
    after_3d = State()

class CorrectAnswer(Learn_words):
    good = State()
    attempt = State()

class Exercise(CorrectAnswer):
    one = State()
    two = State()
    three = State()

class Repeat(StatesGroup):
    repeat_start = State()
    repeat_end = State()


class Mydict(StatesGroup):
    en_word = State()
    ru_word = State()
