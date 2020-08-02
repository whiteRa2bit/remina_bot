import logging
import os
from aiogram import Bot, types, md
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage, SendPhoto, EditMessageText
from aiogram.utils.executor import start_webhook


_TOKEN = os.environ['TOKEN']

_WEBHOOK_HOST = 'https://reminabot.herokuapp.com'  # name your app
_WEBHOOK_PATH = '/webhook/'
_WEBHOOK_URL = f"{_WEBHOOK_HOST}{_WEBHOOK_PATH}"

_WEBAPP_HOST = '0.0.0.0'
_WEBAPP_PORT = os.environ.get('PORT')

logging.basicConfig(level=logging.INFO)

_bot = Bot(token=TOKEN)
_dp = Dispatcher(_bot)
_dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dp):
    await _bot.set_webhook(_WEBHOOK_URL)


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    # insert code here to run it before shutdown
    await _bot.delete_webhook()

    # Close DB connection (if used)
    await _dp.storage.close()
    await _dp.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(dispatcher=_dp, webhook_path=_WEBHOOK_PATH,
                  on_startup=on_startup, on_shutdown=on_shutdown,
                  host=_WEBAPP_HOST, port=_WEBAPP_PORT)
