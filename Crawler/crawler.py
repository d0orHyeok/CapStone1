import time
import pyautogui
from selenium import webdriver
from bs4 import BeautifulSoup

#driver 경로 설정
driver = webdriver.Chrome('C:/Program Files (x86)/Google/ChromeDriver/chromedriver')
driver.implicitly_wait(3)

driver.get('https://www.yanolja.com/hotel/3012531/reviews')


SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    pyautogui.scroll(-100)
    pyautogui.scroll(100)

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#리뷰 선택
reviews = soup.select('div._2z8CVX')

print(len(reviews))

#or review in reviews:
 #   print(review.text.strip())