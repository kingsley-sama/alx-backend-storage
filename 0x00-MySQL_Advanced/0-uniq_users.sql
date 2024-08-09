-- script that creates a table users if not already exist
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
	`id` int PRIMARY KEY NOT NULL,
	`email` varchar(255) NOT NULL UNIQUE,
   	`name`  varchar(255)
);
