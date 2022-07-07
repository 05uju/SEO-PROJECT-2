CREATE DATABASE IF NOT EXISTS weather_data;

CREATE TABLE catalog(
    address VARCHAR(255) default NULL,
    temp VARCHAR(255) default NULL,
    date DATE() default NULL
) AUTO_INCREMENT=1;