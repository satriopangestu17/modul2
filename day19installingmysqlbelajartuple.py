# my sql
# download: MySQL Community Server 8.0.18 

#buka terminal #*command di terminal:
# cd /usr/local/mysql
# cd bin  #* lokasi file di bin
# ./mysql -u root -p  #*untuk aktivasi root=(user)
#Enter password: (password dari mysql root@:) #jgn lupa difoto passwordnya
# mysql> show databases; #*apabila langsung show databases akan muncul tulisan dibawah:
# ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executing this statement.
# mysql> alter user 'root'@'localhost' identified by '12344321';
# mysql workbench bisa dipakai juga
#kalao di terminal belum lengkap tinggal lanjutin yang belum lengkapnya

#* show databases: #* ini adalah query

#use tokoonlineku;
#select database(); #* cek lagi di database mana
#untuk pindah tinggal ketik: use mysql #*contohnya
#liat tipe2 di w3school. string, numeric, and type
#NULL isinya YES artinya boleh kosong
# extra, misal data masuk berubah gitu misalnya
#* untuk menghapus:
# drop database tokoonlineku;
# drop table tokoonlineku;
#select * from pedagang; (untuk liat semua kolom)
#masukin data ke table database jangan ke database
# untuk cancel misal salah tulis, ketik control C. atau ga tutup aja dengan titik koma

# primary key (no), suatu yang unik. jadi tiap buyer punya nomor yang beda

# create table pembeli(                                                                                                                                           -> no int not null auto_increment,
    # -> nama varchar(100) not null default 'anonymous buyer',  #* nama orangnya cuma bisa sampe 100 orang
    # -> usia tinyint,
    # -> berat float(3,1),  ## maksimal 2 digit di depan koma dan pembulatan 1 angka dibelakang koma. misal (99,989) tidak bisa karena angka jadi 100 yang di show
    # -> sex enum('pria', 'wanita'),
    # -> bod date,   #* bith of date
    # -> created_at timestamp default current_timestamp,
    # -> primary key (no)
    # -> );

    #delete from pembeli; untuk hapus seluruh data

    #backend lintang, 06sql no 9
gli = []
gtup = ()
gambar = ('link1', 'link2')
for i in range(0, len(gambar), 1):
    for j in range(1, len(gambar), 1):
        gtup = gtup + gambar[i:i+1]
        gtupn = gtup[i:i+1]
        gli.append(gtupn)
print(gli)

# gambar = ('link1', 'link2')
a = ('andi', 'budi', 'caca', 'gani', 'rio', 'abang')
# print(a[0:3])
li = []
tup = ()
for i in range(0,len(a),3): 
    tup = tup + a[i:i+3] 
    tupn = tup[i:i+3]
    # gab = tupn +gtup[i:j+1]
    li.append(tupn)
print(li)
    # print(gab)

listlgabung = []
for i in range(len(li)):
    lin = li[i]
    glin = gli[i]
    lgabung = lin +glin
    listlgabung.append(lgabung)
print(listlgabung)



# gli = []
# gtup = ()
# gambar = ('link1', 'link2')
# for i in range(0, len(gambar), 1):
#     gtup = gtup + gambar[i:i+1]
#     gtupn = gtup[i:i+1]
#     gli.append(gtupn)
# print(gli)

# for i in range(0, len(gambar), 1):
#     libaru = li[i:i+1] + gli[i:i+1]
# print(libaru)


# for i in range(len(gambar)):
#     gabungin = list(zip(li, gli))
# print(gabungin)

# a = ('andi', 'budi', 'caca', 'gani', 'rio', 'abang')
# # print(a[0:3])
# li = []
# for i in range(0,len(a),3):
#     li.append(a[i:i+3])
# # print(tup)
# print(li)


# a = ('andi', 'budi', 'caca', 'gani', 'rio', 'abang')
# # print(a[0:3])
# li = []
# for i in a:
#     li.append(i)
# print(li)

# gli = []
# gtup = ()
# gambar = ('link1', 'link2')
# for i in range(0, len(gambar), 1):
#     gtup = gtup + gambar[i:i+1]
#     gtupn = gtup[i:i+1]
#     gli.append(gtupn)
# print(gli)


# a = ('andi', 'budi', 'caca', 'gani', 'rio', 'abang')
# # print(a[0:3])
# li = []
# tup = ()
# for i in range(0,len(a),3):
#     tup = tup + a[i:i+3]
#     tupn = tup[i:i+3]
#     li.append(tupn)
# # print(tup)
# print(li)

# gli = []
# gtup = ()
# gambar = ('link1', 'link2')
# for i in gambar:
#     gli.append(i)
# print(gli)

# for i in range(len(gambar)):
#     gabungin = list(zip(li, gli))
# print(gabungin)

# ltup = []
# tuplenew =('\xa0341', 'rio', '\xa012', 'gani')
# for i in range(0,len(tuplenew),2):
#     ltup.append(tuplenew[i][1:4])
# # print(tuplenew[0][0:4])
# print(ltup)

