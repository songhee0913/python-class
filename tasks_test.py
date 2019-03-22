import requests
from bs4 import BeautifulSoup 
import calendar as cal
from datetime import date

def CalendarList():
    today = date.today()
    yy = today.strftime('%Y')
    mm = today.strftime('%m')

    return cal.month(int(yy), int(mm))


def KeyWordList():
    res = requests.get("http://naver.com")
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    tag_list = soup.select('.PM_CL_realtimeKeyword_list_base .ah_k')
    keyword_list = [tag.text for tag in tag_list]

    return keyword_list


def GuguDanList():
    for number in range(2, 3):
        for i in range(1,10):

            gugudan_list = "%d x %d = %d" % (number,i,number*i)

    return gugudan_list

def Naver_blog_search(keyword):
    search_url = "https://search.naver.com/search.naver"
    params = {
        'where': 'post',
        'query': keyword,
    }

    res = requests.get(search_url, params=params)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    tag_list = soup.select('.sh_blog_title')
    
    for tag in tag_list:
        post_url = tag['href']
        post_title = tag['title']
        post = {
            'title': post_title,
            'url': post_url,
        }
        yield post





