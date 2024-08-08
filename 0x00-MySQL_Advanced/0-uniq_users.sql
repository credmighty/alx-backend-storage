-- script for db that creates table users with col id email name
CREATE TABLE IF NOT EXIST users (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
);
