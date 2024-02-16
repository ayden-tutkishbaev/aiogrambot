from aiogram.types import InlineKeyboardButton

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class Pagination(CallbackData, prefix='pack'):
    action: str
    page: int


def paginator(page: int=0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='◀', callback_data=Pagination(action='previous', page=page).pack()),
        InlineKeyboardButton(text='▶', callback_data=Pagination(action='next', page=page).pack()),
        width=2
    )
    return builder.as_markup()

