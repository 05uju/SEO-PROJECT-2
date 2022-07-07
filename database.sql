CREATE DATABASE IF NOT EXISTS weather;
USE weather;

CREATE TABLE catalog(
    address VARCHAR(255) default NULL,
    temp VARCHAR(255) default NULL,
    date DATE default NULL
) AUTO_INCREMENT=1;

