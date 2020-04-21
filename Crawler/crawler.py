#-*- coding: utf-8 -*-

import time
import re
import pyautogui
from selenium import webdriver
from bs4 import BeautifulSoup


class ReviewCrawler(object):
    def __init__(self):
        chromedriver = 'C:/Program Files (x86)/Google/ChromeDriver/chromedriver'
        self.driver = webdriver.Chrome(chromedriver)

    def get_url(self, url):
        self.driver.get(url)

    def crawl_reviews(self):
        self.scroll_page()

        reviews = self.driver.find_elements_by_class_name('_2z8CVX')

        return reviews

    def scroll_page(self):

        numOfReview = self.get_review_num()

        SCROLL_PAUSE_TIME = 1

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # 추가 로드를 위한 마우스 스크롤 직접 동작
            pyautogui.scroll(-100)
            pyautogui.scroll(100)

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                reviews = self.driver.find_elements_by_class_name('_2z8CVX')
                if numOfReview == len(reviews):
                    break
            last_height = new_height

    def get_review_num(self):
        totalReview = self.driver.find_element_by_class_name('_2HRMT3')  # 후기 (N)개 부분 추출
        numTexts = re.findall("\d+", totalReview.text)  # 텍스트중 숫자 추출

        # 정수변환
        if len(numTexts) == 1:  # 리뷰가 1000개 미만일 경우
            numOfReview = int(numTexts[0])
        else:
            numOfReview = int(numTexts[0]) * 1000 + int(numTexts[1])

        return numOfReview


url = 'https://www.yanolja.com/hotel/3020210/reviews'

crawler = ReviewCrawler()

crawler.get_url(url)

reviews = crawler.crawl_reviews()

print(len(reviews))

with open('review.txt', 'w', -1, "utf-8")  as file:
    for review in reviews:
        file.write(review.text)

