# from bs4 import BeautifulSoup
# import requests

# url = 'http://digidb.io/digimon-list/'
# web = requests.get(url)
# data = BeautifulSoup(web.content, 'html.parser')
# listnya = []
# listoflist = []
# td = data.find_all('td')
# for i in td:
#     if len(listnya) == 0:
#         listnya.append(i.text[1:])
#     elif len(listnya) == 1:
#         listnya.append(i.text[2:])
#     else:
#         listnya.append(i.text)
#         if len(listnya) == 13:
#             listoflist.append(listnya)
#             listnya = []

# td_img = data.find_all('img')
# td_img = td_img[2:-2]
# for i in td_img:
#     listoflist[td_img.index(i)].insert(2, i['src'])

# #bikin colom
# col = []





# a = 'abcde'  ##contoh  buat belajar
# a = a[2:-2]
# print(a)

b = []
list = ['bata', 'butu', 'baku', 'makan']
b.append(list)
# list = []
print(len(list))
print(b)
print(list[1:])