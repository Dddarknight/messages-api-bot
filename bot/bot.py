import os
import sys
import requests
from telegram.ext import Updater, MessageHandler, filters
from telegram.ext.commandhandler import CommandHandler
from dotenv import load_dotenv

from logger import setup_logging


logger = setup_logging()


load_dotenv()

API_TOKEN = os.getenv('TG_API_TOKEN')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
URL = f"http://{HOST}:{PORT}/api/messages/tg-token/"


def start(update, context):
    update.message.reply_text('Please provide token')


def is_command(data):
    return data.startswith('/')


def handle_user_input(update, context):
    token = update.message.text
    if not is_command(token):
        data = {'tg_token': token, 'chat_id': update.message.chat.id}
        requests.put(URL, data=data)


def handle_error(update, context):
    sys.stderr.write(f"ERROR: {context.error} caused by {update}")
    pass


def main():
    updater = Updater(API_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(
        MessageHandler(filters.Filters.text, handle_user_input))
    updater.dispatcher.add_error_handler(handle_error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()