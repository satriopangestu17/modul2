from bs4 import BeautifulSoup
import requests

url = 'http://digidb.io/digimon-list/'
web = requests.get(url)
data = BeautifulSoup(web.content, 'html.parser')

#DIGIMON
td = data.find_all('td')
print(td)

list = []
List_OL = []
for i in td:   ## dengan for akan muncul semua yang didalam 'td' dilist ke bawah
    if len(list) == 0:
        list.append(i.text[1:])  ## pake text biar td nya ga ikut
    elif len(list) == 1:
        list.append(i.text[2:])
    else:
        list.append(i.text)
        if len(list) == 13:
            List_OL.append(list)
            list = []  ##??
# print(List_OL)

td_img = data.find_all('img')
# print(td_img)
td_img = td_img[2:-2] #biar index ga out of range. *** karena 2 image diawal dan 3 image di akhir tidak dipakai
# print(td_img)  #jadi mulai dari dua stop juga di dua ?
for i in td_img:
    List_OL[td_img.index(i)].insert(14, i['src'])  ##gabung semua sampai link image
# print(List_OL)


#untuk column title nya. digimon, 
col = []
th = data.find_all('th')
for i in th:
    col.append(i.text)
    # print(col)
col[0] = 'No'
# col.append('Image') #* hasil akan sama dengan yg bawah
col.insert(13, 'Image') #kalau pakai insert bisa diurutan keberapa, misal 14
print(col)

listData = []
for i in List_OL:
    data = dict(zip(col, i))
    listData.append(data)


import csv
with open('digimon.csv', 'w', newline='') as file:
    tulis = csv.DictWriter(file, fieldnames=col)
    tulis.writeheader()
    tulis.writerows(listData)


import json
with open ('digimon.json', 'w') as y:
    json.dump(listData, y)

import xlsxwriter  
filebarcelona = xlsxwriter.Workbook('digimon.xlsx')
barcelonasheet = filebarcelona.add_worksheet('dig')
for i in range(len(col)):  ##row0, column i,headernya dulu
    barcelonasheet.write(0, i, col[i])
for i in range(len(List_OL)):  #yang penting panjang kebawah row nya ga peduli list or tuple di dalam list
    for j in range(len(col)): #sama yang penting panjang column ke kanannya
        barcelonasheet.write(i+1, j, List_OL[i][j] )  ##[i] artinya mengikuti row, [j] mengikuti column tiap componen
filebarcelona.close()  
