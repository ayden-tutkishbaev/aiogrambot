import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, CommandObject

from dotenv import load_dotenv
from os import getenv


load_dotenv()
bot = Bot(getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Good part of the day!")
    
    

async def main():
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")
    

