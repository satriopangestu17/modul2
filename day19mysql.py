    # Last login: Wed Nov 20 09:39:06 on ttys001
    # (base) MacBook-Pro:~ cindyboom$ cd /usr/local/mysql/bin
    # (base) MacBook-Pro:bin cindyboom$ ./mysql
    # ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)
    # (base) MacBook-Pro:bin cindyboom$ ./mysql -u root
    # ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)
    # (base) MacBook-Pro:bin cindyboom$ sudo ./mysql
    # Password:
    # ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)
    # (base) MacBook-Pro:bin cindyboom$ sudo ./mysql -u root
    # ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)
    # (base) MacBook-Pro:bin cindyboom$ cd /usr/local/mysql
    # (base) MacBook-Pro:mysql cindyboom$ sudo ./bin/mysqld_safe
    # Logging to '/usr/local/mysql-5.7.28-macos10.14-x86_64/data/MacBook-Pro.local.err'.
    # 2019-11-20T02:46:10.6NZ mysqld_safe Starting mysqld daemon with databases from /usr/local/mysql-5.7.28-macos10.14-x86_64/data
    # ^Z
    # [1]+  Stopped                 sudo ./bin/mysqld_safe
    # (base) MacBook-Pro:mysql cindyboom$ bg
    # [1]+ sudo ./bin/mysqld_safe &
    # (base) MacBook-Pro:mysql cindyboom$ ./mysql -u root
    # -bash: ./mysql: No such file or directory
    # (base) MacBook-Pro:mysql cindyboom$ cd /usr/local/mysql
    # (base) MacBook-Pro:mysql cindyboom$ cd bin
    # (base) MacBook-Pro:bin cindyboom$ ./mysql -u root
    # ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)
    # (base) MacBook-Pro:bin cindyboom$ ./mysql -u root -p 
    # Enter password: 
    # ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)
    # (base) MacBook-Pro:bin cindyboom$ ./mysql -u root -p
    # Enter password: 
    # Welcome to the MySQL monitor.  Commands end with ; or \g.
    # Your MySQL connection id is 4
    # Server version: 5.7.28

    # Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

    # Oracle is a registered trademark of Oracle Corporation and/or its
    # affiliates. Other names may be trademarks of their respective
    # owners.

    # Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    # mysql> show databases;
    # ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executing this statement.
    # mysql> alter user 'root'@'localhost' indentified by '12344321';
    # ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'indentified by '12344321'' at line 1
    # mysql> alter user 'root'@'localhost' identified by '12344321';
    # Query OK, 0 rows affected (0.01 sec)

    # mysql> show databases;
    # +--------------------+
    # | Database           |
    # +--------------------+
    # | information_schema |
    # | mysql              |
    # | performance_schema |
    # | sys                |
    # +--------------------+
    # 4 rows in set (0.01 sec)

    # mysql> create database tokoonlineku;
    # Query OK, 1 row affected (0.01 sec)

    # mysql> show databases;
    # +--------------------+
    # | Database           |
    # +--------------------+
    # | information_schema |
    # | mysql              |
    # | performance_schema |
    # | sys                |
    # | tokoonlineku       |
    # +--------------------+
    # 5 rows in set (0.00 sec)

    # mysql> create database if not exists tokoonlineku;
    # Query OK, 1 row affected, 1 warning (0.00 sec)

    # mysql> use tokoonlineku;
    # Database changed
    # mysql> select database();
    # +--------------+
    # | database()   |
    # +--------------+
    # | tokoonlineku |
    # +--------------+
    # 1 row in set (0.00 sec)

    # mysql> show tables;
    # Empty set (0.00 sec)

    # mysql> create table pedagang (
    #     -> no int,
    #     -> nama varchar(5)
    #     -> );
    # Query OK, 0 rows affected (0.03 sec)

    # mysql> show tables;
    # +------------------------+
    # | Tables_in_tokoonlineku |
    # +------------------------+
    # | pedagang               |
    # +------------------------+
    # 1 row in set (0.01 sec)

    # mysql> describe pedagang;
    # +-------+------------+------+-----+---------+-------+
    # | Field | Type       | Null | Key | Default | Extra |
    # +-------+------------+------+-----+---------+-------+
    # | no    | int(11)    | YES  |     | NULL    |       |
    # | nama  | varchar(5) | YES  |     | NULL    |       |
    # +-------+------------+------+-----+---------+-------+
    # 2 rows in set (0.01 sec)

    # mysql> select * from pedagang;
    # Empty set (0.00 sec)

    # mysql> insert into pedagang values (2, 'andi');
    # Query OK, 1 row affected (0.01 sec)

    # mysql> select * from pedagang;
    # +------+------+
    # | no   | nama |
    # +------+------+
    # |    2 | andi |
    # +------+------+
    # 1 row in set (0.00 sec)

    # mysql> insert into pedagang (nama)values (2, 'andi');
    # ERROR 1136 (21S01): Column count doesn't match value count at row 1
    # mysql> insert into pedagang (nama) values ('budi');
    # Query OK, 1 row affected (0.00 sec)

    # mysql> select * from pedagang;
    # +------+------+
    # | no   | nama |
    # +------+------+
    # |    2 | andi |
    # | NULL | budi |
    # +------+------+
    # 2 rows in set (0.00 sec)

    # mysql> insert into pedagang (nama, no) values ('caca', 25);
    # Query OK, 1 row affected (0.00 sec)

    # mysql> select * from pedagang;
    # +------+------+
    # | no   | nama |
    # +------+------+
    # |    2 | andi |
    # | NULL | budi |
    # |   25 | caca |
    # +------+------+
    # 3 rows in set (0.01 sec)

    # mysql> insert into pedagang values
    #     -> (3, 'dedi'),
    #     -> (6, 'euis'),
    #     -> (98, 'fafa');
    # Query OK, 3 rows affected (0.00 sec)
    # Records: 3  Duplicates: 0  Warnings: 0

    # mysql> select * from pedagang;
    # +------+------+
    # | no   | nama |
    # +------+------+
    # |    2 | andi |
    # | NULL | budi |
    # |   25 | caca |
    # |    3 | dedi |
    # |    6 | euis |
    # |   98 | fafa |
    # +------+------+
    # 6 rows in set (0.00 sec)

    # mysql> create table pembeli(
    #     -> no int not null auto_increment,
    #     -> nama varchar(100) not null default 'anonymous buyer'
    #     -> usia tinyint,
    #     -> berat float(3,1),
    #     -> sex enum('pria', 'wanita')
    #     -> bod date, 
    #     -> created_at timestamp default current_timestamp,
    #     -> primary key (no)
    #     -> );
    # ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'usia tinyint,
    # berat float(3,1),
    # sex enum('pria', 'wanita')
    # bod date,
    # created_at ' at line 4
    # mysql> create table pembeli(                                                                                                                                           -> no int not null auto_increment,
    #     -> nama varchar(100) not null default 'anonymous buyer',
    #     -> usia tinyint,
    #     -> berat float(3,1),
    #     -> sex enum('pria', 'wanita'),
    #     -> bod date,
    #     -> created_at timestamp default current_timestamp,
    #     -> primary key (no),
    #     -> );
    # ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ')' at line 10
    # mysql> create table pembeli( no int not null auto_increment, nama varchar(100) not null default 'anonymous buyer', usia tinyint, berat float(3,1), sex enum('pria', 'wanita'), bod date, created_at timestamp default current_timestamp, primary key (no) );
    # Query OK, 0 rows affected (0.03 sec)

    # mysql> describe pembeli;
    # +------------+-----------------------+------+-----+-------------------+----------------+
    # | Field      | Type                  | Null | Key | Default           | Extra          |
    # +------------+-----------------------+------+-----+-------------------+----------------+
    # | no         | int(11)               | NO   | PRI | NULL              | auto_increment |
    # | nama       | varchar(100)          | NO   |     | anonymous buyer   |                |
    # | usia       | tinyint(4)            | YES  |     | NULL              |                |
    # | berat      | float(3,1)            | YES  |     | NULL              |                |
    # | sex        | enum('pria','wanita') | YES  |     | NULL              |                |
    # | bod        | date                  | YES  |     | NULL              |                |
    # | created_at | timestamp             | NO   |     | CURRENT_TIMESTAMP |                |
    # +------------+-----------------------+------+-----+-------------------+----------------+
    # 7 rows in set (0.00 sec)

    # mysql> insert into pembeli (nama, usia, berat, sex, bod) values
    #     -> ('andi',22,77.8,'PRIA','1996-12-29'),
    #     -> ('budi',22,79.8,'WANITA','1995-12-29');
    # Query OK, 2 rows affected (0.01 sec)
    # Records: 2  Duplicates: 0  Warnings: 0

    # mysql> select * from pembeli;
    # +----+------+------+-------+--------+------------+---------------------+
    # | no | nama | usia | berat | sex    | bod        | created_at          |
    # +----+------+------+-------+--------+------------+---------------------+
    # |  1 | andi |   22 |  77.8 | pria   | 1996-12-29 | 2019-11-20 11:57:11 |
    # |  2 | budi |   22 |  79.8 | wanita | 1995-12-29 | 2019-11-20 11:57:11 |
    # +----+------+------+-------+--------+------------+---------------------+
    # 2 rows in set (0.01 sec)

    # mysql> describe pedagang;
    # +-------+------------+------+-----+---------+-------+
    # | Field | Type       | Null | Key | Default | Extra |
    # +-------+------------+------+-----+---------+-------+
    # | no    | int(11)    | YES  |     | NULL    |       |
    # | nama  | varchar(5) | YES  |     | NULL    |       |
    # +-------+------------+------+-----+---------+-------+
    # 2 rows in set (0.00 sec)

    # mysql> insert into pedagang (nama) values ('abcdefghij');
    # ERROR 1406 (22001): Data too long for column 'nama' at row 1
    # mysql> 
    # mysql> insert into pembeli (berat) values(100.2);
    # ERROR 1264 (22003): Out of range value for column 'berat' at row 1
    # mysql> insert into pembeli (berat) values(10.2);
    # Query OK, 1 row affected (0.01 sec)

    # mysql> insert into pembeli (berat) values(10.28);
    # Query OK, 1 row affected (0.01 sec)

    # mysql> select * from pembeli;
    # +----+-----------------+------+-------+--------+------------+---------------------+
    # | no | nama            | usia | berat | sex    | bod        | created_at          |
    # +----+-----------------+------+-------+--------+------------+---------------------+
    # |  1 | andi            |   22 |  77.8 | pria   | 1996-12-29 | 2019-11-20 11:57:11 |
    # |  2 | budi            |   22 |  79.8 | wanita | 1995-12-29 | 2019-11-20 11:57:11 |
    # |  3 | anonymous buyer | NULL |  10.2 | NULL   | NULL       | 2019-11-20 12:02:05 |
    # |  4 | anonymous buyer | NULL |  10.3 | NULL   | NULL       | 2019-11-20 12:02:51 |
    # +----+-----------------+------+-------+--------+------------+---------------------+
    # 4 rows in set (0.00 sec)

    # mysql> insert into pembeli (berat) values (99.9);
    # Query OK, 1 row affected (0.00 sec)

    # mysql> select * from pembeli;
    # +----+-----------------+------+-------+--------+------------+---------------------+
    # | no | nama            | usia | berat | sex    | bod        | created_at          |
    # +----+-----------------+------+-------+--------+------------+---------------------+
    # |  1 | andi            |   22 |  77.8 | pria   | 1996-12-29 | 2019-11-20 11:57:11 |
    # |  2 | budi            |   22 |  79.8 | wanita | 1995-12-29 | 2019-11-20 11:57:11 |
    # |  3 | anonymous buyer | NULL |  10.2 | NULL   | NULL       | 2019-11-20 12:02:05 |
    # |  4 | anonymous buyer | NULL |  10.3 | NULL   | NULL       | 2019-11-20 12:02:51 |
    # |  5 | anonymous buyer | NULL |  99.9 | NULL   | NULL       | 2019-11-20 12:05:54 |
    # +----+-----------------+------+-------+--------+------------+---------------------+
    # 5 rows in set (0.00 sec)

    # mysql> insert into pembeli (berat) values (99.9899);
    # ERROR 1264 (22003): Out of range value for column 'berat' at row 1
    # mysql> insert into pembeli (sex) values ('rahasia');
    # ERROR 1265 (01000): Data truncated for column 'sex' at row 1
    # mysql> insert into pembeli (sex) values ('laki-laki');
    # ERROR 1265 (01000): Data truncated for column 'sex' at row 1
    # mysql> insert into pembeli (bod) values ('1998-12-21');
    # Query OK, 1 row affected (0.01 sec)

    # mysql> insert into pembeli (bod) values ('12-12-1998');
    # ERROR 1292 (22007): Incorrect date value: '12-12-1998' for column 'bod' at row 1
    # mysql> select * from pembeli;
    # +----+-----------------+------+-------+--------+------------+---------------------+
    # | no | nama            | usia | berat | sex    | bod        | created_at          |
    # +----+-----------------+------+-------+--------+------------+---------------------+
    # |  1 | andi            |   22 |  77.8 | pria   | 1996-12-29 | 2019-11-20 11:57:11 |
    # |  2 | budi            |   22 |  79.8 | wanita | 1995-12-29 | 2019-11-20 11:57:11 |
    # |  3 | anonymous buyer | NULL |  10.2 | NULL   | NULL       | 2019-11-20 12:02:05 |
    # |  4 | anonymous buyer | NULL |  10.3 | NULL   | NULL       | 2019-11-20 12:02:51 |
    # |  5 | anonymous buyer | NULL |  99.9 | NULL   | NULL       | 2019-11-20 12:05:54 |
    # |  6 | anonymous buyer | NULL |  NULL | NULL   | 1998-12-21 | 2019-11-20 12:08:20 |
    # +----+-----------------+------+-------+--------+------------+---------------------+
    # 6 rows in set (0.00 sec)

    # mysql> 
