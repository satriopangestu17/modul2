import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd= '12344321',
    database = 'ptabc'
)

# c = db.cursor()
# query='select nama from karyawan'
# c.execute(query)
# out = c.fetchall()
# print(out)
# print(list(map(lambda x: x[0], out)))

# c = db.cursor(dictionary=True) #untuk jadi json lebih enak
# query='select * from karyawan'
# c.execute(query)
# out = c.fetchall()
# print(out)
# # print(list(map(lambda x: x[0], out)))


#**#untuk masukin data di column
# c = db.cursor(dictionary=True) #untuk jadi json lebih enak
# query='insert into karyawan (nama) values(%s)'
# data = ('andi',)
# c.execute(query, data)
# db.commit()


#hapus data row
# c = db.cursor(dictionary=True) #untuk jadi json lebih enak
# query='delete from karyawan where nama = %s'
# data = ('andi',)
# c.execute(query, data)
# db.commit()

#ngubah nama ani jadi hani
# c = db.cursor(dictionary=True) #untuk jadi json lebih enak
# query='update karyawan set nama = %s where nama =%s'
# data = ('hani', 'ani')
# c.execute(query, data)
# db.commit()

#ngubah gaji dana nama id_kar 11, menjadi 11 juta
# c = db.cursor(dictionary=True) #untuk jadi json lebih enak
# query='update karyawan set nama = %s, gaji=%s where id_kar=%s'
# data = ('zizi', 20000000, 11)
# c.execute(query, data)
# db.commit()


c = db.cursor(dictionary=True) #untuk jadi json lebih enak
query='alter table karyawan add column hobby varchar(255)'
# data = ('zizi', 20000000, 11)
c.execute(query)
# db.commit()  #kalau cuma untuk liat2 dan nambah column data gaperlu commmit tp ga papa commit juga


#nama foreign key antar table beda boleh

# mysql> select username, namabagian from
#     -> tabelA inner join tabelB
#     -> using (id_bagian);
##kalau untuk koneksiin inner join apabila nama column sama

#sub query didalam kurung

#* right join akan memunculkan seluruh yang di tabelB dab yang beririsan dengan tabelA. right join akan memunculkan tabel yang ditulis dikanan akan dimunculkan
# mysql> select username, namabagian from
#     -> tabelA right join tabelB
#     -> on tabelA.id_bagian = tabelB.id_bagian;
#
# Hal diatas akan sama dengan: 
# mysql> select username, namabagian from
#     -> tabelB left join tabelB
#     -> on tabelB.id_bagian = tabelA.id_bagian;


#munculin fafa aja yang null nama bagian
#mysql> select username, namabagian from 
#     -> tabelA left join tabelB
#     -> on tabelA.id_bagian =tabelB.id_bagian
#     -> where tabelB.id_bagian is null;  #* atau bisa where namabagian is null;
# +----------+------------+

#untuk memunculkan bagian yang ga punya karyawan
# mysql> select username, namabagian from
#     -> tabelA right join tabelB
#     -> on tabelA.id_bagian = tabelB.id_bagian 
#     -> where tabelA.username is null;

##untuk kombinasi permutasi, probability
# mysql> select username, namabagian from
#     -> tabelA cross join tabelB;
# +----------+----------------+


#untuk menggabungkan seluruh bagian tabela dan tabelb:
# mysql> select username, namabagian from
#     -> tabelA left outer join tabelB
#     -> using (id_bagian)
#     -> union
#     -> select username, namabagian from
#     -> tabelA right outer join tabelB  ##* outer join sama dengan join biasa
#     -> using (id_bagian);
# +----------+----------------+


#memunculkan tabel dengan mengurangi yang irisan tabela dengan tabelb:
# mysql> select username, namabagian from
#     -> tabelA left outer join tabelB
#     -> using (id_bagian)
#     -> where tabelB.id_bagian is null
#     -> union
#     -> select username, namabagian from
#     -> tabelA right outer join tabelB
#     -> using (id_bagian)
#     -> where tabelA.id_bagian is null;

# -- select city.name, country.name from
# -- city inner join country
# -- on city.countrycode = country.code
# -- where country.code = 'idn'

# mysql> select * from
#     -> tabela inner join tabelab
#     -> on tabela.id_user = tabelab.user_id
#     -> inner join tabelab
#     -> on tabelb.id_bagian = tabelab.bagian_id;


# mysql> create database world;
# Query OK, 1 row affected (0.01 sec)

#mysql> exit
# Bye
# (base) MacBook-Pro:bin cindyboom$ mysql -u user -p world < world.sql
# -bash: mysql: command not found
# (base) MacBook-Pro:bin cindyboom$ ./mysql -u user -p world < world.sql
# Enter password: 
# ERROR 1045 (28000): Access denied for user 'user'@'localhost' (using password: YES)
# (base) MacBook-Pro:bin cindyboom$ sudo ./mysql -u user -p world < world.sql
# Password:
# Enter password: 
# ERROR 1045 (28000): Access denied for user 'user'@'localhost' (using password: YES)
# (base) MacBook-Pro:bin cindyboom$ sudo ./mysql -u root -p world < world.sql
# Enter password: 
# (base) MacBook-Pro:bin cindyboom$ ./mysql -u root -p
# Enter password: 
# Welcome to the MySQL monitor.  Commands end with ; or \g.
# Your MySQL connection id is 25
# Server version: 5.7.28 MySQL Community Server (GPL)



# mysql> select * from tabela 
#     -> inner join tabelab
#     -> on tabela.id_user = tabelab.user_id
#     -> inner join tabelab
#     -> on tabelb.id_bagian = tabelab.bagian_id;

# mysql> select a.username, ab.namabagian from   #* pakai alian a.usernama dan ab.namabagian
#     -> tabela a, tabelab ab, tabelb b
#     -> where a.id_user = ab.user_id and b.id_bagian = ab.bagian_id;
## khusus untuk innerjoin, kebanyakan yang dilkaukan innerjoin
