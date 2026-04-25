create database portfolio;
use portfolio;

-- Commodities Historic Prices
create table commodity_history(
symbol  varchar(65) NOT NULL,
time_stamp datetime DEFAULT NULL,
current_price decimal(10,2) DEFAULT NULL,commodity_history

KEY idx_symbol (symbol),
KEY idx_time_stamp (time_stamp),
KEY idx_time_symbol (symbol,time_stamp)

);


-- PSX Historic Prices
CREATE TABLE psx_history (
  symbol varchar(20) NOT NULL,
  time_stamp datetime DEFAULT NULL,
  current_price decimal(10,2) DEFAULT NULL,
  volume int DEFAULT NULL,
  KEY idx_symbol (symbol),
  KEY idx_time_stamp (time_stamp),
  KEY idx_time_symbol (symbol,time_stamp)
);

-- Commodity Cache
create table commodity_cache (
Symbol varchar(150) Primary Key Not Null,
Price decimal(10,2) DEFAULT NULL,
Day decimal(10,2) DEFAULT NULL,
Percentage DECIMAL(8,5),
Weekly DECIMAL(8,5),
Monthly DECIMAL(8,5),
YTD DECIMAL(8,5),
YoY DECIMAL(8,5),
Date_time datetime DEFAULT NULL
);



-- Com Cache 
create table fixtemp (
Symbol varchar(150) Primary Key Not Null,
`Price` decimal(10,2) DEFAULT NULL,
`Day` decimal(10,2) DEFAULT NULL,
`Percentage%` DECIMAL(5,4),
`Weekly%` DECIMAL(5,4),
`Monthly%` DECIMAL(5,4),
`YTD%` DECIMAL(5,4),
`YoY%` DECIMAL(5,4),
`Date_time` datetime DEFAULT NULL
);

-- Users
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,  
    email VARCHAR(115) UNIQUE NOT NULL,
    pass VARCHAR(255) NOT NULL
);

-- Assets
create table assets (
asset VARCHAR(65) PRIMARY KEY,
asset_name VARCHAR(120) Default Null,
category ENUM('PSX', 'COMMODITY', 'CRYPTO')

);