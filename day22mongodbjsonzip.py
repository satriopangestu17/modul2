# macos. mongodb  $ gausa diketik artinya masuk
# # cd Downloads
# $ tar -zxvf mongodb-osx-xxxxx.tgz  ##*wajib tar untuk extract, ga bisa cara extract biasa
# $ sudo mkdir -p /data/db   #untuk bikin folder. cuma sekali aja
# $ cd mongodb-osx-xxx/bin

##lebih baik buka 2 terminal untuk tau apakah ada yg salah
#aktivasi server
# #cdm => server
# cd Downloads/mongodb-macos-x86_64-4.2.1/bin
# sudo ./mongod
#kemudian masukkan password

## untuk tempat bekerjanya
## cmd => work
# cd Downloads/mongodb-macos-x86_64-4.2.1/bin
# ./mongo
#show dbs

# db  : untuk liat lg didatabase ada dimana.
# misal use tokoonline, ketika di show dbs ga akan muncul kalau ga diisi tapi tokoonline sudah ada. jadi ga usa create database?

# di mongodb bukan table namanya, tapi collection
#db.pelapak.drop()

# disetiap database server

# $gt = greater than, $gte, $lt, $lte

# w3resource.com/mongodb-exercises/

#masukin file json ke dbs mongo db, pertama ubah ke  bentuk json dulu. #yang file restaurant
#comand a, option + shift + i  ##cara edit nambahin koma di setiap akhir row

# kemudia pindahin file json ke bin mongodb. nanti bisa di