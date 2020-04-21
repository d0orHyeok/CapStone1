import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup

#driver 경로 설정
driver = webdriver.Chrome('C:/Program Files (x86)/Google/ChromeDriver/chromedriver')
driver.implicitly_wait(3)

driver.get('https://www.yanolja.com/hotel/3012531/reviews')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#전체 리뷰 수 추출
#r_num = 전체 리뷰 수
r_title = soup.select('h1._3BgL1L.with-right-default')
r_num = int(re.findall('\d+', r_title[0].text)[0])

#리뷰 선택
reviews = soup.select('div._2z8CVX')

for review in reviews:
    print(review.text.strip())