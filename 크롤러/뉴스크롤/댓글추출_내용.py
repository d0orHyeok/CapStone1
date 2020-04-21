from selenium import webdriver
import time

def get_replys(url,imp_time=5,delay_time=0.1):

    #웹 드라이버
    driver = webdriver.Chrome('c:/xd/chromedriver.exe')
    driver.implicitly_wait(imp_time)
    driver.get(url)

    #더보기 계속 클릭하기
    while True:
        try:
            더보기 = driver.find_element_by_css_selector('a.u_cbox_btn_more')
            더보기.click()
            time.sleep(delay_time)
        except:
            break

    html = driver.page_source
    # print(html)

    # 모듈 참조
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml') #html.parser

    # 댓글추출
    contents = soup.select('span.u_cbox_contents')
    contents = [content.text for content in contents]

    # 취합
    replys = list(zip(contents))

    driver.quit()
    return replys

if __name__ == '__main__':
    from datetime import datetime
    start = datetime.now()

    url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=052&aid=0001418989&m_view=1'
    reply_data = get_replys(url,5,0.1)

    import pandas as pd #pandas, openpyxl
    col =['내용']
    data_frame = pd.DataFrame(reply_data,columns=col)
    data_frame.to_excel('news.xlsx',sheet_name='test',startrow=0,header=True)
    data_frame.to_csv("filename.csv", mode='w')

    end = datetime.now()
    print(end-start)