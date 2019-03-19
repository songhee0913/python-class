import os
import sys
import traceback
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler


def start(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
    chat_id = update.message.chat_id # 대화방 ID
    text = update.message.text

    if '뭐해?' in text:
        response = '일함'
    else:
        response = '니가 무슨 말 하는 지 모르겠어. :('

    bot.send_message(char_id=chat_id, text=response)

def main(token):
    bot = Updater(token=TOKEN)

    handler = CommandHandler('start', start)
    bot.dispatcher.add_handler(handler)

    handler = MessageHandler(Filters.text, echo)
    bot.dispatcher.add_handler(handler)

    bot.start_polling()

    print('running telegram bot ...')
    bot.idle()

if __name__ =='__main__':

    TOKEN = "715709804:AAFor5ahRJ4YL91xhMTrJSQ4-ovvMI8DZvw"
    if TOKEN is None:
        print('ERROR) TELEGRAM_TOKEN을 지정해 주세요.', file=sys.stderr)
        sys.exit(1)
    main(TOKEN)



