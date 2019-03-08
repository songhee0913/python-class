import os
import sys
import traceback
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler
import tasks

def start(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
    chat_id = update.message.chat_id # 대화방 ID
    text = update.message.text

    task_cls_list = [
        # tasks.YaTask,
        tasks.HelloTask,
        tasks.NaverBlogSearchTask,
    ]

    try:
        for task_cls_list in task_cls_list:
            task = task_cls(text)
            if task.is_valid():
                response = task.proc()
                break
            else:
                response = '무슨 말하는지 모르겠습니다.'
    except Exception as e:
        response = '처리 중 오류가 발생했습니다.'
        tracebacj.print_exc()

    bot.send_message(char_id=chat_id, text=response)

    def main(token):
        bot = Updater(token=TOKEN)

        handler = CommandHandler('start', start)
        bot.dispatcher.add_handler(handler)

        handler = MassageHandler(Filters.text, echo)
        bot.dispatcher.add_handler(handler)

        bot.start_polling()

        print('running telegram bot ...')
        bot.idle()





