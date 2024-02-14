from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Main menu'),
            KeyboardButton(text='Links')
        ],
        [
            KeyboardButton(text='F&Q')
        ],
        [
            KeyboardButton(text='Calculator')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Choose option'
)

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Willie', url='https://t.me/damnwlh'),
            InlineKeyboardButton(text='Umi', url='https://t.me/GQFAS')
        ],
        [
            InlineKeyboardButton(text='Idk', url='https://t.me/eventsmarvel')
        ]
    ]
)


spec_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ТИ ГДЕ ЖЫВЁШ?', request_location=True)
        ],
        [
            KeyboardButton(text='BACK')
        ]
    ],
    resize_keyboard=True
)


def calc_kb():
    items = [
        '1', '2', '3', '/',
        '4', '5', '6', '*',
        '7', '8', '9', '+',
        '=', '0', 'C', '-',
    ]
    builder = ReplyKeyboardBuilder()
    # for item in items:
    #     builder.button(text=item)
    [builder.button(text=item) for item in items]
    builder.button(text='Back')
    builder.adjust(4, 4, 4, 4, 1)

    return builder.as_markup(resize_keyboard=True)