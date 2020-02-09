'''
1. get API sportdb, daftar pemain dari sebuah klub
2. input : klub apa? -> X
3. daftar pemain : nama, posisi, usia, negara
save as x. xls & json & csv
'''
import requests

klub = input('ketik nama klub: ')
ur1 = f"https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}"
data = requests.get(ur1)
players = data.json()['player']
headerdict = ['nama', 'posisi', 'usia', 'negara']
nama = []
posisi = []
usia = []
negara = []
gabung = []
for p in players:
    nama.append(p['strPlayer'])
    posisi.append(p['strPosition'])
    usia.append(2019 - (int(p['dateBorn'][0:4])))
    negara.append(p['strNationality'])
    kombinasi = list(zip(nama, posisi, usia, negara))
    print(kombinasi)
for i in range(len(kombinasi)):
    x = dict(zip(headerdict, kombinasi[i]))
    gabung.append(x)

print(gabung)


# import csv

# with open(f'{klub}.csv', 'w',newline='') as x:
#     kolom = headerdict
#     a = csv.DictWriter(x, fieldnames=kolom, delimiter=',')
#     a.writeheader()
#     a.writerows(gabung)  ###untuk mengubah ke json harus dibentuk jadi dictionary in list, berati pakai variable gabung

# import json
# with open (f'{klub}.json', 'w') as y:
#     json.dump(gabung, y)

import xlsxwriter
filebarcelona = xlsxwriter.Workbook(f'{klub}.xlsx')
barcelonasheet = filebarcelona.add_worksheet('data')
for i in range(len(headerdict)):  ##row0, column i,headernya dulu
    barcelonasheet.write(0, i, headerdict[i])
for i in range(len(kombinasi)):
    for j in range(len(headerdict)):
        barcelonasheet.write(i+1, j, kombinasi[i][j] )  ##[i] artinya mengikuti row, [j] mengikuti column tiap componen
filebarcelona.close()  















# ##**buat belajar
# # header = ['nama', 'usia', 'nama makanan']
# # nama = ['satrio', 'ratu', 'gilang', 'oi']
# # usia = ['25', '24', '27', '26']
# # makanan = ['pizza', 'spagheti', 'salad', 'kentang']
# # gabung = list(zip(nama, usia, makanan))
# # print(gabung)
# # komgab = dict(zip(header, gabung)) ##sama kayak yang bawah kombinasi
# # print(komgab)
# # for i in range(len(gabung)):
# #     new = dict(zip(header, gabung[i])) ##dengan adanya [i] maka akan sendiri2 komponen dari list gabung, yaitu nama, usia, makanan
# #     print(new)


# # kombinasi = dict(zip(header, gabung)) ##kalau gabung saja ga pake [i] maka akan semua list(nama, usia, makanan) keluar di loopin
# # print(kombinasi)

