from bs4 import BeautifulSoup
import requests

url = 'http://digidb.io/digimon-list/'
web = requests.get(url)
data = BeautifulSoup(web.content, 'html.parser')
# print(data)

title = ['no', 'digimon', 'stage', 'type', 'attribute',
'memory', 'equip slots', 'hp', 'sp', 'atk', 'def', 'int',
'spd']
digi = []
new_digi = [] #untuk memasukkan nama digimon (temp)
for i in data.find_all('td'):
    digi.append(i.text)
print(digi)

panjang = data.find_all('img') # hasil yang akan keluar berupa list
print(len(panjang)) # hasil yang akan keluar berupa list
gambar = [] #masukin url gambar, dipisah
for i in data.find_all('img'):  #di loop keluar dari list
    # print(i)
    gambar.append(i['src'])  ##1[src],2[src] ....
gambar1 = gambar[2:343] #agar hasil tidak ke loop di mundurin sebelum loop
# print(gambar)

for i in range(0,len(digi),13):
    d = digi[i:i+13]   ## untuk nge cut keperluan tiap range untuk satu digimon
    new_digi.append(d)
print(new_digi)


for i in range(len(gambar1)):
    new_digi[i].insert(2,gambar[i])


c = []
for i in new_digi:
    c.append(dict(zip(title,i)))  #udah sebaris paketan untuk 1 digimon maka tinggal di dict(zip())
print(c)





import csv
with open('dfile.csv', 'w', newline='') as x:
    kolom = title
    a = csv.DictWriter(x, fieldnames=kolom, delimiter=',')
    a.writeheader()
    a.writerows(c)


# b = 'satrio'
# print('\xa01 satrio, gani', '\xa02 pokok')





