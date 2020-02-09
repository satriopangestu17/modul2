# mysql workbench ver gui
#nama  varchar(5) default 'nonim' #* defaultnya (kalau ga diisi) harus 5 karakter
# sex set('pria', 'wanita') harus diisi pria atau wanita  #kalau set bisa diisi 'pria,wanita'
# gaji int default 5000000, kalau ga diisi 5 juta automatis
# created_at timestamp default current_timestamp, automatis isi hari ini
# not null untuk null jadi no

# select nama, gaji, 0.03 * gaji from karyawan; kolum ini tidak ada di database cm info tambahan
# select nama, gaji, 0.03 * gaji as pot_bpjs from karyawan;
#select * from karyawan order by nama desc, created_at; jadi nama descending, created_at ascending (dari kecil kebesar) menngikuti nama apabila ada yg sama
#insert into karyawan (nama, gaji) values ('anna', 12000000);
#select * from karyawan;
# select * from karyawan order by nama desc, gaji;

# select * from karyawan where nama = 'anna';  select * from karyawan where gaji > 8000000;
# select count(*) from karyawan; * diseluruh table
# select count(nama) from karyawan where nama = 'anna'; itung dari kolom nama
#rata-rata gaji karyawan yg gajinya < rata-rata gaji seluruh karyawan
# select * from karyawan where gaji < (select avg(gaji) from karyawan);
# 
# select avg(gaji) from karyawan where gaji < (select avg(gaji) from karyawan); atau bisa cara panjang seperti dibawah
# select avg(gaji) from (select * from karyawan where gaji < (select avg(gaji) from karyawan)) as myq;
#  alter table karyawan #untuk nambah column
    # -> add column
    # -> alanat text;
# alter table karyawan  ##hapus tabel
    # -> drop column alanat;

##** kalau mau rename nama columnnya tidak bisa
# alter table `karyawan` change column `sex` `gender` set('pria','wanita')