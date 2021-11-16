from .utils import BOT
import asyncio
from .modules import bot
from pyrogram import idle
from os import system
import logging


logging.getLogger('pyrogram').setLevel(logging.CRITICAL)

async def main():
    await BOT.start()
    system("cls")
    print("-- BOT INICIADO --")
    await idle()


if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        print("bye")