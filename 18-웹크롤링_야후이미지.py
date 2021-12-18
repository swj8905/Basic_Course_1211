from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par
import os

if not os.path.exists("./이미지수집"):
    os.mkdir("./이미지수집")

keyword = input("키워드 입력 >> ")

if not os.path.exists(f"./이미지수집/{keyword}"):
    os.mkdir(f"./이미지수집/{keyword}")

encoded = par.quote(keyword) # 한글 --> 특수한 문자열
code = req.urlopen(f"https://images.search.yahoo.com/search/images;_ylt=Awr9F683M71heuAASJGJzbkF;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X1MDOTYwNjI4NTcEX3IDMgRhY3RuA2NsawRjc3JjcHZpZANaNXpPRFRFd0xqSXA2SXpUWVguUDlBT0dNVEUwTGdBQUFBQTJ3RWlHBGZyA3lmcC10BGZyMgNzYS1ncARncHJpZANkc3JZbVZvbVFiSzBqOVBRRG1yemRBBG5fc3VnZwMxMARvcmlnaW4DaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMEcXN0cmwDMjcEcXVlcnkDJUVDJTk1JTg0JUVDJTlEJUI0JUVEJThGJUIwBHRfc3RtcAMxNjM5Nzg5NDQ1?p={encoded}&fr=yfp-t&fr2=sb-top-images.search&ei=UTF-8&x=wrt")
soup = BeautifulSoup(code, "html.parser")
img = soup.select("a.img > img")
cnt = 1
for i in img:
    img_url = i.attrs["data-src"] # .text : 요소의 내용 / .attrs : 요소의 속성
    req.urlretrieve(img_url, f"./이미지수집/{keyword}/{cnt}.png")
    print(f"{keyword} 이미지 저장 완료 {cnt}")
    cnt += 1