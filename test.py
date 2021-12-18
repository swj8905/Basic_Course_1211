from selenium import webdriver
from chromedriver_autoinstaller import install
import time

browser = webdriver.Chrome(install()) # 크롬브라우저를 연다.
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
# 로그인 하기
id = browser.find_element_by_css_selector("input#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("input#pw")
pw.send_keys("1q2w3e!@#")
button = browser.find_element_by_css_selector("button.btn_login")
button.click()
time.sleep(3) # 로그인이 다 될 때까지 기다리기