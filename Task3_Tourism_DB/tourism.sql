CREATE DATABASE tourism_db;
USE tourism_db;

CREATE TABLE Countries (
    country_id INT PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(100) NOT NULL
);

CREATE TABLE Cities (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    city_name VARCHAR(100) NOT NULL,
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES Countries(country_id)
);

CREATE TABLE TourTypes (
    type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(80) NOT NULL,
    description TEXT
);

CREATE TABLE Hotels (
    hotel_id INT PRIMARY KEY AUTO_INCREMENT,
    hotel_name VARCHAR(150) NOT NULL,
    city_id INT,
    stars INT,
    FOREIGN KEY (city_id) REFERENCES Cities(city_id)
);

CREATE TABLE Tours (
    tour_id INT PRIMARY KEY AUTO_INCREMENT,
    tour_name VARCHAR(200) NOT NULL,
    type_id INT,
    hotel_id INT,
    price DECIMAL(10,2),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (type_id) REFERENCES TourTypes(type_id),
    FOREIGN KEY (hotel_id) REFERENCES Hotels(hotel_id)
);
