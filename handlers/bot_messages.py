from aiogram import Router, F
from aiogram.types import Message

from keyboards import reply, inline, builder, fabric
from data.subloader import get_json

rt = Router()


@rt.message()
async def echo(message: Message):

    msg = message.text.lower()

    smiles = await get_json('smiles.json')

    # await message.answer('wrong command!')
    #
    # msg = message.text.lower()

    if msg == 'main menu':
        await message.answer(f'{smiles[0][0]} {smiles[0][1]}', reply_markup=fabric.paginator())

    elif msg == 'links':
        await message.answer(f'We: ', reply_markup=inline.inline)

    elif msg == 'calculator':
        await message.reply(f'Here it is:', reply_markup=builder.calc_kb())