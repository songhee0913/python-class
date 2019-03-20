import requests
import os
import sys
from bs4 import BeautifulSoup
from telegram.ext import Updater, Filters
from telegram.ext import MessageHandler
import calendar as cal
import tasks

Updater = Updater(token=TOKEN) #Token정보
dispatcher = Updater.dispatcher
Updater.start_polling()


def handler(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id

    if "실시간" in text:
        keyword_list = tasks.KeyWordList()
        response = '네이버 실시간 검색어입니다\n{}'.format(keyword_list)
    elif "구구단" in text:
        gugudan_list = tasks.GuguDanList()
        response = '구구단입니다\n{}'.format(gugudan_list)
    elif "부산대학교맛집" in text:
        naver_blog_search_list = list(tasks.naver_blog_search(text))
        response = '부산대학교 맛집리스트 입니다.\n{}'.format(naver_blog_search_list)
    elif "달력" in text:
        calendar_list = tasks.CalendarList()
        response = calendar_list
    else:
        response = '몰라'
    
    bot.send_message(chat_id=chat_id, text=response)

    

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)



