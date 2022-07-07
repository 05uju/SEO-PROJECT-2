CREATE DATABASE IF NOT EXISTS weather_data;
USE weather_data;

CREATE TABLE catalog(
    address VARCHAR(255) default NULL,
    temp VARCHAR(255) default NULL,
    date DATE() default NULL
) AUTO_INCREMENT=1;

INSERT INTO catalog(address, temp, date)
VALUES ("Kennesaw", 65, 07-06-2022);