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


-- PSX Cache
CREATE TABLE `psx_cache` (
  `Symbol` varchar(149) NOT NULL,
  `Sector` smallint DEFAULT NULL,
  `listed In` varchar(350) DEFAULT NULL,
  `LDCP` decimal(10,2) DEFAULT NULL,
  `Open` decimal(10,2) DEFAULT NULL,
  `High` decimal(10,2) DEFAULT NULL,
  `Low` decimal(10,2) DEFAULT NULL,
  `Change` decimal(10,2) DEFAULT NULL,
  `Current` decimal(10,2) DEFAULT NULL,
  `Change (%)` decimal(5,4) DEFAULT NULL,
  `Volume` decimal(15,2) DEFAULT NULL,
  `Date_time` datetime DEFAULT NULL,
  PRIMARY KEY (`Symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Holdings Table
create table holdings(
holding_id INT auto_increment primary key,
user_id INT not Null,
asset_symbol varchar(70) Not Null,
asset_quantity DECIMAL(15,4) Not null,
buy_price decimal(15,4) not null,
comission decimal(10,2) default 0,
purchase_date datetime default current_timestamp,

-- Relationship (FK)
Constraint fk_user FOREIGN KEY (user_id) references users(user_id) ON delete cascade,
Constraint fk_symbol FOREIGN KEY (asset_symbol) references assets(asset)
);