##live server
#supaya bisa masukin postman

#beautifulsoup4
#pip3 install beautifulsoup4
# import bs4 ;atau
from bs4 import BeautifulSoup

#web scraping from html file
data = BeautifulSoup(open('coba.html', 'r'), 'html.parser')
print(data)
# print(data.prettify())
print(data.title.text)
# print(data.title.name) #untuk ngambil tagnya
# print(data.title.string) #mirip kyk text 
# print(data.title)
# print(data.h1.text)

# print(data.ul.text)
# print(data.ul.string)

# print(data.find_all('li'))
# print(type(data.find_all('li')[0]))

# ul = data.ul
# # print(ul)
# for i in ul.find_all('li'):
#     print(i.text)

# for x in data.find_all('li'):
#     print(x.text)

# print(data.find('li', class_ = 'minuman'))
# ul =data.ul
# for i in ul.find_all('li', class_ = 'minuman'):
#     print(i.text)

# for i in ul.find_all('li', id = 'person'):
#     print(i['id'])

# import requests

# #web scraping dari url
# web = requests.get('http://127.0.0.1:5500/modul2/coba.html')
# data = BeautifulSoup(web.content, 'html.parser')
# print(data)

# ul = data.ul
# for i in ul.find_all('li', id = 'person'):
#     print(i.text)

title = data.find('p')
# print(title)
title1 = data.find_all('p')
print(title1)
listp = []
for i in title1:
    # print(i.text)   ##find.all harus pakai for untuk dapet text nya
    listp.append (i.text)
print(listp)