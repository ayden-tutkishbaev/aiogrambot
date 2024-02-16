from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)

main = ReplyKeyboardMarkup(
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
