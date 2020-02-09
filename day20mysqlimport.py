# pip3 install MySQL-connector-python
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '12344321',
    # auth_plugin = 'mysql_native_password', #kalo yg gagal usenya
    database = 'PTABC'  # jadi ga usah pake ketik use database PT ABC
)

# c = db.cursor()
# sql = 'insert into karyawan (nama, gaji) values (%s, %s)'
# val = ('andi', 15000000)
# # c.execute('show databases')
# c.execute(sql, val)
# db.commit() #agar ada perubahan ke database: delete update insert
# print(c.rowcount, 'data tersimpan')

# sql = 'create database x'
# c.execute(sql)

c = db.cursor()
sql = 'insert into karyawan (nama, alamat, gaji) values (%s, %s, %s)' #%snya ada 2 untuk nambah di column nama dan gaji
val = [('cici', 'jalan100' ,15000000), ('caca', 'jalan50',15000000)]
# c.execute('show databases')
c.executemany(sql, val)
db.commit() #agar ada perubahan ke database: delete update insert
print(c.rowcount, 'data tersimpan')


# x = c.fetchall()
# print(x)

# for i in x:
#     print(i)

##tugas scraping web digimon, lalu masukin ke mysql

