create database if not exists pokebase;
use pokebase;
create table  if not exists pokemon(
	id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type01 varchar(255) NOT NULL,
    type02 varchar(255),
    sprite varchar(300) NOT NULL
);
