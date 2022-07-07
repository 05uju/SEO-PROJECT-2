CREATE DATABASE IF NOT EXISTS weather_data;
USE weather_data;

CREATE TABLE catalogg (
    City VARCHAR(255) default NULL,
    Temperature VARCHAR(255) default NULL,
    Dates DATE default NULL
) AUTO_INCREMENT=1;

INSERT INTO catalogg(City, Temperature, Dates)
