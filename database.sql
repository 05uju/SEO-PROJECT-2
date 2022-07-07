CREATE DATABASE IF NOT EXISTS weather;
USE weather;

CREATE TABLE catalog(
    City VARCHAR(255) default NULL,
    Temperature VARCHAR(255) default NULL,
    Dates DATE default NULL
) AUTO_INCREMENT=1;

INSERT INTO catalog(City, Temperature, Dates)
