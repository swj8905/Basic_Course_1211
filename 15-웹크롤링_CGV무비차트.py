import urllib.request as req
from bs4 import BeautifulSoup

# 서버로부터 HTML 코드 받아오기
code = req.urlopen("http://www.cgv.co.kr/movies/?lt=1&ft=0")
# print(code.read())

# HTML 코드 이쁘게 정리하기
soup = BeautifulSoup(code, "html.parser")
# print(soup)

# 내가 원하는 요소 알려주기
# title = soup.select_one("strong.title")
title = soup.select("strong.title")
# 요소 내용 꺼내오기
# print(title.text) # 복습용 강의에서는 .string을 쓰지만,
                  # .text를 써주세요. .text가 더 좋습니다.
cnt = 1
for i in title:
    print(f"{cnt}위 : {i.text}")
    cnt += 1

# 위 코드 다른 방법 1.
# for i in title:
#     print(f"{title.index(i) + 1}위 : {i.text}")
#
# # 위 코드 다른 방법 2.
# for i in range(len(title)):
#     print(f"{i + 1}위 : {title[i].text}")