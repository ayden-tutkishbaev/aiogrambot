import asyncio

from aiogram import Bot, Dispatcher

from handlers import bot_messages, user_commands
from callbacks import pagination

from dotenv import dotenv_values

config = dotenv_values()


async def main():
    bot = Bot(config['TOKEN'])
    dp = Dispatcher()
    dp.include_routers(
        user_commands.rt,
        pagination.rt,
        bot_messages.rt
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")
