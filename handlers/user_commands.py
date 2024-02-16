from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart

from keyboards import reply, builder, inline

import random

rt = Router()


@rt.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Good part of the day, <b>{message.from_user.first_name}</b>!", parse_mode='HTML',
                         reply_markup=reply.main)



@rt.message(Command(commands=['random', 'rnumber']))
async def randomnumber(message: Message, command: CommandObject):
    a, b = [int(c) for c in command.args.split('-')]
    number = random.randint(a, b)
    await message.reply(f'OK - {number}', reply_markup=reply.spec_kb)


@rt.message(Command(commands=['we']))
async def we(message: Message):
    await message.reply(f'Here we are:', reply_markup=inline.inline)


@rt.message(Command(commands=['calc']))
async def we(message: Message):
    await message.reply(f'Here it is:', reply_markup=builder.calc_kb())

