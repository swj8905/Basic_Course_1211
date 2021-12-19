from selenium import webdriver
import time
from chromedriver_autoinstaller import install

hash_tag = input("해시태그 입력 >> ")
browser = webdriver.Chrome(install())
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
# 로그인 하기
id = browser.find_element_by_name("username")
id.send_keys("tutor_pyson") # 본인 계정 적어주세요.
pw = browser.find_element_by_name("password")
pw.send_keys("q1w2e3r4!@#$") # 본인 계정 PW 적어주세요.
button = browser.find_element_by_css_selector("div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB")
button.click()   #위에 띄어쓰기 되어 있을시 처음과 끝은 띄어씌기 제거, 그외는 띄어쓰기 줄이면서. 으로 대처한다
time.sleep(5)
# 해시태그 검색
url = "https://www.instagram.com/explore/tags/" + hash_tag
browser.get(url)
time.sleep(5)
# 첫번째 사진 클릭
first_photo = browser.find_element_by_css_selector("div._9AhH0")
first_photo.click()
time.sleep(7)
while True:
    like = browser.find_element_by_css_selector("section.ltpMr.Slqrh span > svg._8-yf5")
    value = like.get_attribute("aria-label")
    next = browser.find_element_by_css_selector("div.l8mY4.feth3 svg._8-yf5")
    if value == "좋아요":  # 좋아요가 안눌려있다면?
        like.click()
        time.sleep(30)
        next.click()
        time.sleep(30)
    else:  # 좋아요가 눌려있다면?
        next.click()
        time.sleep(30)