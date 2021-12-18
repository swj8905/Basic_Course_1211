from selenium import webdriver
from chromedriver_autoinstaller import install
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(install())
browser.get("https://www.youtube.com/watch?v=95ULYjyiFLQ")
time.sleep(5)

# 스크롤 살짝 내리기
browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN)
time.sleep(5) # 댓글 생성 기다리기
comments = browser.find_elements_by_css_selector("#content-text")
idx = 0
while True:
    try:
        print(comments[idx].text)
    except:
        print("======= 크롤링 완료 ===========")
        break
    idx += 1
    if idx % 20 == 0: # (== idx가 20의 배수라면?)
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(4)
        comments = browser.find_elements_by_css_selector("#content-text")

