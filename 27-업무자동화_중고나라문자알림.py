from selenium import webdriver
import time
from chromedriver_autoinstaller import install

browser = webdriver.Chrome(install())
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
id = browser.find_element_by_css_selector("#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)
browser.get("http://cafe.daum.net/talingpython")
time.sleep(3)
# 중고나라 게시판 클릭
browser.switch_to.frame("down")
browser.find_element_by_css_selector("#fldlink_rRa6_347").click()

try:
    f = open("./중고나라.txt", "r")
    ref = f.readlines()
except:
    f = open("./중고나라.txt", "w")
    ref = []
f.close()

title = browser.find_elements_by_css_selector("a.txt_item")
new_one = 0
for i in title:
    if (i.text+"\n") not in ref: # 최신 글이라면?
        f = open("./중고나라.txt", "a")
        f.write(i.text + "\n")
        f.close()
        if "마우스" in i.text:
            new_one += 1
print(f"마우스 관련 글이 {new_one}개 올라왔습니다.")
browser.close()

if new_one >= 1:
    import os
    from twilio.rest import Client

    account_sid = "ACefe43744d5ca8b39d239f2a622c277e0"
    auth_token = "0c6ddcf60a65c9b708693ed60d39c9c7"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=f"마우스 관련 글이 {new_one}개 올라왔습니다. https://cafe.daum.net/talingpython/rRa6",
                         from_='+18109578577',
                         to='+821095518905'
                     )