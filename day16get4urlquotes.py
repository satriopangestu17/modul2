import requests

# ur3 = 'https://quotes.rest/qod'
# data = requests.get(ur3)
# data = data.json()
# print(data)
# print(data['content'])

# appid = '&appid=484888fe633fb1f6af79f51a0e4c86e2'
# kota = input('ketik kota ')
# # https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=484888fe633fb1f6af79f51a0e4c86e2
# ur4 = f'https://api.openweathermap.org/data/2.5/weather?q={kota}{appid}'
# data = requests.get(ur4)
# data = data.json()
# print(data['sys']['sunrise'])
# sunrise = data['sys']['sunrise']

# #pip3 install python-dateutil

# from datetime import datetime
# from dateutil import tz
# myzone = tz.gettz('Asia/Jakarta')
# waktu = datetime.utcfromtimestamp(int(sunrise))
# print(waktu)


#get api sportsdb, daftar pemain suatu klub
# input: klub apa? contoh:X
# daftar pemain: nama, posisi, usia, negara
# save jadi excel, json, csv. namanya sesuai yang diinput: X.xlsx, X.json, X.csv
# [ {'nama':, 'posisi', 'usia', 'negara'},
# {'nama':'posisi', 'usia', 'negara}]

klub = input('ketik nama klub: ')
url = f'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}'
data = requests.get(url)
players = data.json()['player']
# print(players)
import datetime as dt
x = dt.datetime.today()
age = data.json()['player'][1]['dateBorn']
print(age)
splitage = age.split('-')
# joinage = ''.join(splitage)
print(splitage)
tahun = int(splitage[0])
print(tahun)
print(type(tahun))

# for player in players:
    # print(f"{player['strPlayer']} ({player['strPosition']}) ({player['strPosition']})")


'''
1. get API sportdb, daftar pemain dari sebuah klub
2. input : klub apa? -> X
3. daftar pemain : nama, posisi, usia, negara
save as x. xls & json & csv
'''
import requests
import json
import xlsxwriter
import csv
#Source
klub = input("Ketik nama klub : ")
url = f"https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}"
data = requests.get(url)
players = data.json()["player"]
header = ["nama", "posisi", "usia", "negara"]
nama = []
posisi = []
usia = []
negara = []
hasilAkhir = []
for player in players:
    nama.append(player["strPlayer"])
    posisi.append(player["strPosition"])
    usia.append(2019 - (int(player["dateBorn"][:4])))
    negara.append(player["strNationality"])
kombi = list(zip(nama, posisi, usia, negara))
for i in range(len(kombi)):
    X = dict(zip(header, kombi[i]))
    hasilAkhir.append(X)
# print(X)

#create csv
with open(f'{klub}.csv',"w",newline="") as x:
    kolom = header
    a = csv.DictWriter(x, fieldnames=kolom, delimiter=",")
    a.writeheader()
    a.writerows(hasilAkhir)

#create json  ##pretifier json control + shift + p, cari json pretifier. 
# untuk file json harus dictionary dalam list
with open (f'{klub}.json', "w") as y:
    json.dump(hasilAkhir,y)

#create excel
newfile = xlsxwriter.Workbook(f"{klub}.xlsx")
newsheet = newfile.add_worksheet("Data Pemain")
for i in range(len(header)):
    newsheet.write(0, i, header[i])
for i in range(len(kombi)):
    for j in range(len(header)):
        newsheet.write(i+1, j, kombi[i][j])
newfile.close()
