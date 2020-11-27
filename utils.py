from telebot import types

HELP_INFO = """Для начала работы с ботом введите /start
Для того, чтобы перейти к выбору песни введите любой символ"""


def generate_markup(buttons):
    buttons = [types.KeyboardButton(f'{i}') for i in buttons]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                       one_time_keyboard=True)
    markup.add(*buttons)
    return markup