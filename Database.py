create database db;
 
use db;
 
create table books(bid varchar(10) primary key,
  title varchar(50) Not null,
  author varchar(50) Not null,
  available varchar(5) Default ‘YES’,  
  );
 
create table issue(bid varchar(10) primary key,
 studentName varchar(50) Not null,
 foreign key(bid) references books(bid)
 );
 
desc books;
desc issue;
