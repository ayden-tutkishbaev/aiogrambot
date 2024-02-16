from aiogram.utils.keyboard import ReplyKeyboardBuilder

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