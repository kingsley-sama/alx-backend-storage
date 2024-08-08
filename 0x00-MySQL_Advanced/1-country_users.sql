-- script that creates a table users if not already exist
CREATE TABLE IF NOT EXISTS users (
id INT PRIMARY KEY NOT NULL AUTO_INCREAMENT,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255)
country ENUM('US','CO','TN') NOT NULL DEFAUTL 'US'
);
