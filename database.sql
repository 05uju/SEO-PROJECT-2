CREATE DATABASE IF NOT EXISTS weather_data;
USE weather_data;

CREATE TABLE catalog(
    city VARCHAR(255) default NULL,
    temp VARCHAR(255) default NULL,
    date DATE() default NULL
) AUTO_INCREMENT=1;

INSERT INTO catalog(city, temp, date)
VALUES ("Kennesaw", 65, 07-06-2022);
SELECT * FROM catalog;