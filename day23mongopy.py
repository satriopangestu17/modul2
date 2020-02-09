#pip3 install pymongo, mongo tetap aktif #user:pass@
import pymongo
url = 'mongodb://localhost:27017/'
mymongo = pymongo.MongoClient(url)

# untuk lihat ada database apa saja:
dbs = mymongo.list_database_names()
print(dbs)

#untuk bekerja di database mana:
mydb = mymongo['pymongodb']
##untuk table/collection yang mana:
mycol = mydb['colmong']

alldata = list(mycol.find({'nama':'Andi'}, {'nama':1}))    ##harus di list suapay ga cursorobject
print(alldata)

# mydb = mymongo['pymongodb']
# mycol = mydb['colmong']
# alldata = list(mycol.find({'usia' : {'$gt':24}}))    ##harus di list suapay ga cursorobject
# print(alldata)

# mydb = mymongo['pymongodb']
# mycol = mydb['colmong']
# mydata = {
#     'nama': 'Deni', 'usia': 18, 'kota': 'kediri'
# }
# mycol.insert_one(mydata)

# mydb = mymongo['pymongodb']
# mycol = mydb['colmong']
# mydata = [{'nama': 'Euis', 'usia': 35, 'kota': 'Denpasar'},
# {'nama': 'Fafa', 'usia': 29, 'kota': 'Jakarta'},
# {'nama': 'Gian', 'usia': 22, 'kota': 'Sorong'}]
# mycol.insert_many(mydata)

# x = mycol.insert_many(mydata)
# print(x.inserted_ids)

# nama = ['Andi', 'Euis', 'Fafa']
# print(list(mycol.find({'nama':{'$in': nama}})))

# x = mycol.insert_one({'nama':'Nino'})
# print(x.inserted_id)
# print(list(mycol.find({'_id': x.inserted_id})))


#menghapus satu fafa di collection colmong
# mydb = mymongo['pymongodb']
# mycol = mydb['colmong']

# x = {'nama': 'Fafa'}
# mycol.delete_one(x)

#menghapus semua Gian
# mydb = mymongo['pymongodb']
# mycol = mydb['colmong']

# x = {'nama': 'Gian'}
# mycol.delete_many(x)

#menghapus semuanya
# mydb = mymongo['pymongodb']
# mycol = mydb['colmong']

# mycol.delete_many({})


# mydata = [{'nama': 'Euis', 'usia': 35, 'kota': 'Denpasar'},
# {'nama': 'Fafa', 'usia': 29, 'kota': 'Jakarta'},
# {'nama': 'Gian', 'usia': 22, 'kota': 'Sorong'}]
# mydb = mymongo['pymongodb']
# mycol = mydb['colmong']
# x = mycol.insert_many(mydata)

# mydb = mymongo['pymongodb']
# mycol = mydb['colmong']
# data = {'nama': 'Euis'}
# new = {'nama': 'Gus De'}
# mycol.update_one(data, {'$set': new})

# mydb = mymongo['pymongodb']
# mycol = mydb['colmong']

# data = {'$and': [{'usia':{'$gt':25}},
# {'usia':{'$lt':30}},]}
# new = {'nama': 'Youngman'}
# mycol.update_many(data, {'$set': new})

import datetime
mydb = mymongo['hahaha']
mycol = mydb['hahaha1']
# mycol.insert_one({'nama':'Budi', 'waktu': datetime.datetime.now()})  ##tidak bagus apabila di beda2 bagian waktu bakal beda2


# print(list(mycol.find()))
# print(list(mycol.find({'nama':'Budi'}, {'waktu':1})))
# query = mycol.find({'nama':'Budi'}, {'waktu':1})
# print(list(query)[0]['waktu'])

# mycol.insert_one({'nama':'Deni', 'waktu': datetime.datetime.utcnow()})  ##agar waktu dalam satu satuan di london GMT +0

# print(list(mycol.find()))
# print(list(mycol.find({'nama':'Deni'}, {'waktu':1})))
# query = mycol.find({'nama':'Deni'}, {'waktu':1})  
# print(list(query)[0]['waktu'])

# query = mycol.find({'nama':'Deni'}, {'waktu':1})  
# import pytz  ##untuk memberitahu selisih waktu #pip3 install pytz
# jkt = pytz.timezone('Asia/Jakarta')
# mycol.insert_one({'nama':'Deni', 'waktu':1})
# print(jkt.localize(list(query)[0]['waktu']))