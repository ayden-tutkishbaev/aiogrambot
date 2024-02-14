import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, CommandObject

import keyboards

from dotenv import load_dotenv
from os import getenv

import random


load_dotenv()
bot = Bot(getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Good part of the day, <b>{message.from_user.first_name}</b>!", parse_mode='HTML',
                         reply_markup=keyboards.kb)


@dp.message(Command(commands=['random', 'rnumber']))
async def randomnumber(message: Message, command: CommandObject):
    a,b = [int(c) for c in command.args.split('-')]
    number = random.randint(a,b)
    await message.reply(f'OK - {number}', reply_markup=keyboards.spec_kb)


@dp.message(Command(commands=['we']))
async def we(message: Message):
    await message.reply(f'Here we are:', reply_markup=keyboards.inline_kb)


@dp.message(Command(commands=['calc']))
async def we(message: Message):
    await message.reply(f'Here it is:', reply_markup=keyboards.calc_kb())


@dp.message()
async def echo(message: Message):
    await message.answer('Wrong command!')
    

async def main():
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")



