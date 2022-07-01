-- (docker run -d --name=galenadb -e POSTGRES_PASSWORD=abc123 -p 5432:5432 postgres)

create database galenadb;

use galenadb;

create table candidate(
    id int not null,
    email varchar(50) not null,
    name varchar(50) not null,
    grup int not null,
    grupName varchar(20) not null,
    cpf varchar(14) not null,
    phone varchar(13) not null,
    birthday date not null,
    adress varchar(100) not null,
    primary key (id));

INSERT INTO candidate (id,email,"name",grup,grupname,cpf,phone,birthday,adress) VALUES
	 (1,'fdf','nath',3,'fdfd','4545','4545','1998-06-22','fdfdfdfdf'),
	 (2,'fdf','bruno',4,'fdfd','4545','66666','1998-06-23','fdfdfdfdf'),
	 (3,'@gm','mari',5,'eee','999','55555','1998-06-21','dsdsssssss');
