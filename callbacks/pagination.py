from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from contextlib import suppress

from keyboards import fabric
from data.subloader import get_json


rt = Router()


@rt.callback_query(fabric.Pagination.filter(F.action.in_(['prev', 'next'])))
async def pagination_handler(call: CallbackQuery, callback_data: fabric.Pagination):
    smiles = await get_json('smiles.json')
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == 'next':
        page = page_num + 1 if page_num < (len(smiles)-1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f'{smiles[page][0]} {smiles[page][1]}',
            reply_markup=fabric.paginator(page)
        )

    await call.answer()