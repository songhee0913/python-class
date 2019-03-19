import requests
import os
import sys
from bs4 import BeautifulSoup
from telegram.ext import Updater, Filters
from telegram.ext import MessageHandler
import tasks

Updater = Updater(token='') # TOKEN 
dispatcher = Updater.dispatcher
Updater.start_polling()


def handler(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id

    res = requests.get("http://naver.com")
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    tag_list = soup.select('.PM_CL_realtimeKeyword_list_base .ah_k')
    keyword_list = [tag.text for tag in tag_list]

    if "실시간" in text:
        response = '네이버 실시간 검색어입니다\n{}'.format(keyword_list)
    else:
        response = '몰라'
    
    bot.send_message(chat_id=chat_id, text=response)

    




echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)



