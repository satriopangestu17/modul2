from bs4 import BeautifulSoup  ##untuk webscrapping
import requests #untuk memanggil page, kalau disini dari url

url = 'http://digidb.io/digimon-list/'
web = requests.get(url)
data = BeautifulSoup(web.content, 'html.parser')
# print(data)

# image = []
# for i in data.find_all('img'):
#     image.append(i['src'])
# imagedone = image[2:343]
# print(imagedone)
# timage = tuple(imagedone)
# print(timage)

# tupleim = ()
# lim = []
# for i in range(0,len(timage),1):
#     tupleim = tupleim + timage[i:i+1]  ##masukin ke bentuk tuple dulu semua yang ingin dimasukkan, sama aja sebenrnya kaya diatas; timage = tuple(imagedone)
#     tupleimn = tupleim[i:i+1]
#     lim.append(tupleimn)
# print(lim)

# ftd = data.find_all('td')
# digimon = []
# for i in data.find_all('td'):
#     digimon.append(i.text)
# print(digimon)

# tdigimon = tuple(digimon)
# print(tdigimon)

# tupledig = ()
# lig = []
# for i in range(0, len(tdigimon), 13):
#     tupledig = tupledig + tdigimon[i:i+13]  ##ga perlu sebenarnya
#     tupledign = tupledig[i:i+13]
#     lig.append(tupledign)
# # print(lig)

# gabungan = []
# for i in range(len(lig)):
#     imn = lim[i]
#     gin = lig[i]
#     gab = gin + imn
#     gabungan.append(gab)
# print(gabungan)

# # listtdigimon = []
# # listtnomor = []
# # for i in range(0, len(tdigimon),13):
# #     listtnomor.append(tdigimon[i][1:4])
# #     listtdigimon.append(tdigimon[i+1][1:])
# # print(listtnomor)
# # print(listtdigimon)
# # tlistdigimon = tuple(listtdigimon)
# # tlistnomor = tuple(listtnomor)
# # # print(tlistdigimon )
# # # print(tlistnomor )

# # tuplelistdigimon = ()
# # tuplelistnomor = ()
# # for i in range(0,len(tlistdigimon),1):
# #     tuplelistdigimon += tlistdigimon[i:i+1]
# #     tuplelistdigimonn = tuplelistdigimon[i:i+1]
# #     tuplelistnomor += tlistnomor[i:i+1]
# #     tuplelistnomorn = tuplelistnomor[i:i+1]
# # # print(tuplelistdigimonn)
# # # print(tuplelistnomorn)


# # tuplegab = ()
# # gabungdigi = []
# # for i in range(1,len(tdigimon),13):
# #     tuplegab = tuplegab + tdigimon[i:i+13]
# #     tuplegabn = tuplegab[i:i+13]
# #     fullgab = tuplelistnomorn + tuplelistdigimonn + tuplegabn + tupleimn
# #     gabungdigi.append(fullgab)
# # print(gabungdigi)



# # for i in range(0,len(digimon),13):
# #     gabungdigi.append(digimon[i:i+13])
# # # print(gabungdigi)

# # headercol = []
# # for i in data.find_all('th'):
# #     headercol.append(i.text)
# # # print(headercol)
# # headercol [0] = 'no'
# # headercol.insert(14, 'Image')
# # # print(headercol)


# # print(data.find_all('img'))
# # image = []
# # for i in data.find_all('img'):
# #     image.append(i['src'])
# # imagedone = image[2:343]
# # print(imagedone)

# # for i in range(len(imagedone)): #kalo ga pake len image[i] ga bakal bisa
# #     gabungdigi[i].insert(14,image[i])
# # print(gabungdigi)

# # for i in gabungdigi:
# #     totgabung = dict(zip(headercol, i))
# # # print (totgabung)

# # # valu = ()
# # # for i in range(len(headercol)):
# # #     valu += '%s'
# # # print(valu)

# import mysql.connector

# db = mysql.connector.connect(
#     host = 'localhost',
#     port = 3306,
#     user = 'root',
#     passwd = '12344321',
#     database = 'digi'
#       # jadi ga usah pake ketik use database PT ABC
# )

# c = db.cursor()
# # db.commit()
# # wsql = 'create database digi'
# # c.execute(wsql)
# # wsql = 'create table d(no bigint not null, digimon varchar(20) default "nonim")' 
# # c.execute(wsql)

# # wsql = 'alter table d add column spd int(3)'

# # c.execute(wsql)

# wsql = 'insert into karyawan (no, digimon, stage, type, attribute, memory, equip_slots, HP, SP, atk, def, intel, spd, image) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
# val = gabungan
# c.executemany(wsql, val)
# db.commit()
# # print(c.rowcount, 'data tersimpan')




    




















# # td = ['agumon', 'api', 'monmon', 'air', 'minmin', 'tanah', 'manman', 'angin']
# # list = []
# # # print(len(list))
# # list_OL = []
# # for i in range(0,len(td),2):   ## dengan for akan muncul semua yang didalam 'td' dilist ke bawah
# #    list.append(td[i:i+2])
# #     # if len(list) == 0:
# #     #     list.append(i)
# #     #     if len(list) == 4:
# #     #         list_OL.append(list)
# #     #         list = []  ##??
# # print(list)