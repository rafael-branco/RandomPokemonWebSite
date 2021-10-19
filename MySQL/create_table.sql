CREATE database if NOT EXISTS pokebase;
USE pokebase;
CREATE TABLE  if NOT EXISTS pokemon(
	id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type01 VARCHAR(255) NOT NULL,
    type02 VARCHAR(255),
    sprite VARCHAR(300) NOT NULL
);
