import requests
from bs4 import BeautifulSoup 
import calendar as cal
from datetime import date

class KeyWordList:
    def __init__(self, text):
        self.text = text

    def is_valid(self): 
        if '실시간' in self.text: 
            return True 
        else: 
            return False 

    def proc(self):
        keyword_list = ""
        res = requests.get("http://naver.com")
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        tag_list = soup.select('.PM_CL_realtimeKeyword_list_base .ah_k')
        keyword_list = [tag.text for tag in tag_list]
        keyword_list = '네이버 실시간 검색어입니다\n{}'.format(keyword_list)

        return keyword_list

class NaverBlogSearchTask:
    def __init__(self, text):
        self.text = text

    def is_valid(self): 
        if '부산대학교맛집' in self.text: 
            return True 
        else: 
            return False 

    def proc(self):
        naver_blog_search_list = "" 
        search_url = "https://search.naver.com/search.naver"
        params = {
            'where': 'post',
            'query': self.text,
        }

        res = requests.get(search_url, params=params)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')

        tag_list = soup.select('.sh_blog_title')
        
        for tag in tag_list:
            post_url = tag['href']
            post_title = tag['title']
            post = {'title': post_title,
                'url': post_url,}

            naver_blog_search_list += '{}'.format(post) + '\n' 
                
        naver_blog_search_list = '부산대학교 맛집리스트 입니다\n'+naver_blog_search_list + '\n' 
        return naver_blog_search_list

class CalendarTask:
    def __init__(self, text):
        self.text = text

    def is_valid(self): 
        if '달력' in self.text: 
            return True 
        else: 
            return False 
    def proc(self):
        today = date.today()
        yy = today.strftime('%Y')
        mm = today.strftime('%m')

        return cal.month(int(yy), int(mm))

class GuguDanTask:
    def __init__(self, text):
        self.text = text

    def is_valid(self): 
        if '구구단' in self.text: 
            return True 
        else: 
            return False 
    def proc(self):
        gugudan_list = ""
        for number in range(2, 3):
            for i in range(1,10):
                gugudan_list += "%d x %d = %d\n" % (number,i,number*i)

        return gugudan_list
        
class AcademyInfoList:
    def __init__(self, text):
        self.text = text

    def is_valid(self): 
        if '정보공시' in self.text: 
            return True 
        else: 
            return False 
    def proc(self):
        academy_info_list = "" 
        search_url = "http://www.academyinfo.go.kr/popup/pubinfo1690/list.do?schlId=0000014"

        res = requests.get(search_url)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')

        soup = BeautifulSoup(res.content, 'html.parser')
        title_data = soup.find_all(class_='stitle')
        count_data = soup.find_all(class_='count')
        
        for num in range(len(title_data)):
            academy_info_list += title_data[num].get_text().strip()+':  '+count_data[num].get_text().strip()+'\n'
        return academy_info_list





