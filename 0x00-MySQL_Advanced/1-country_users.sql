/* script that creates a table users if not already exist */
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
	   `id` int PRIMARY KEY NOT NULL AUTO_INCREAMENT,
	   `email` varchar(255) NOT NULL UNIQUE,
	   `name` varchar(255),
	   `country` ENUM('US','CO','TN') NOT NULL DEFAUTL 'US'
);
