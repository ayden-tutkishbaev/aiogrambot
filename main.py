import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.exceptions import TelegramBadRequest

from contextlib import suppress


import keyboards

from dotenv import load_dotenv
from os import getenv

import random

load_dotenv()
bot = Bot(getenv('TOKEN'))
dp = Dispatcher()

smiles = [
    ['㊙', 'А что это значит?'],
    ['☮', 'Пусть всегда будет солнце'],
    ['♉', 'Я телец'],
    ['⚠', 'DANGER'],
]


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Good part of the day, <b>{message.from_user.first_name}</b>!", parse_mode='HTML',
                         reply_markup=keyboards.kb)


@dp.callback_query(keyboards.Pagination.filter(F.action.in_(['prev', 'next'])))
async def pagination_handler(call: CallbackQuery, callback_data: keyboards.Pagination):
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == 'next':
        page = page_num + 1 if page_num < (len(smiles)-1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f'{smiles[page][0]} {smiles[page][1]}',
            reply_markup=keyboards.paginator(page)
        )

    await call.answer()


@dp.message(Command(commands=['random', 'rnumber']))
async def randomnumber(message: Message, command: CommandObject):
    a, b = [int(c) for c in command.args.split('-')]
    number = random.randint(a, b)
    await message.reply(f'OK - {number}', reply_markup=keyboards.spec_kb)


@dp.message(Command(commands=['we']))
async def we(message: Message):
    await message.reply(f'Here we are:', reply_markup=keyboards.inline_kb)


@dp.message(Command(commands=['calc']))
async def we(message: Message):
    await message.reply(f'Here it is:', reply_markup=keyboards.calc_kb())


# @dp.message(Command(commands=['Main menu']))
# async def smiles(message: Message):
#     await message.reply(f'{smiles[0][0]} {smiles[0][1]}', reply_markup=keyboards.paginator())


@dp.message()
async def echo(message: Message):

    msg = message.text.lower()

    # await message.answer('wrong command!')
    #
    # msg = message.text.lower()

    if msg == 'main menu':
        await message.answer(f'{smiles[0][0]} {smiles[0][1]}', reply_markup=keyboards.paginator())

    elif msg == 'links':
        await message.answer(f'We: ', reply_markup=keyboards.inline_kb)

    elif msg == 'calculator':
        await message.reply(f'Here it is:', reply_markup=keyboards.calc_kb())


    # elif msg == 'Links'



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")
