import time
import re
import pyautogui
from selenium import webdriver
from bs4 import BeautifulSoup


def scroll_page():
    ### 자동 스크롤링
    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 추가 로드를 위한 마우스 스크롤 직접 동작
        pyautogui.scroll(-100)
        pyautogui.scroll(100)

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def get_review_num():
    totalReview = driver.find_element_by_class_name('_2HRMT3')  # 후기 (N)개 부분 추출
    numTexts = re.findall("\d+", totalReview.text)  # 텍스트중 숫자 추출

    #정수변환
    if len(numTexts) == 1:              # 리뷰가 1000개 미만일 경우
        numOfReview = int(numTexts[0])
    else:
        numOfReview = int(numTexts[0]) * 1000 + int(numTexts[1])

    return numOfReview


#driver 경로 설정
driver = webdriver.Chrome('C:/Program Files (x86)/Google/ChromeDriver/chromedriver')
driver.implicitly_wait(3)

#수집 진행 url 접속
driver.get('https://www.yanolja.com/hotel/3020210/reviews')

numOfReview = get_review_num()
print(numOfReview)

while True:
    scroll_page()

    reviews = driver.find_elements_by_class_name('_2z8CVX')
    if numOfReview == len(reviews) :
        break

for review in reviews:
    print(len(review))