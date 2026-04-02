create table psx_live (
symbol varchar(50) primary key not null,
sector int,
listedin varchar(255),
ldcp Float,
open Float,
high Float,
low Float,
current Float,
change float,
change%
)

# Commodities Historic Prices

create table commodity_history(
symbol  varchar(65) NOT NULL,
time_stamp datetime DEFAULT NULL,
current_price decimal(10,2) DEFAULT NULL,commodity_history

KEY idx_symbol (symbol),
KEY idx_time_stamp (time_stamp),
KEY idx_time_symbol (symbol,time_stamp)

);


# PSX Historic Prices
CREATE TABLE psx_history (
  symbol varchar(20) NOT NULL,
  time_stamp datetime DEFAULT NULL,
  current_price decimal(10,2) DEFAULT NULL,
  volume int DEFAULT NULL,
  KEY idx_symbol (symbol),
  KEY idx_time_stamp (time_stamp),
  KEY idx_time_symbol (symbol,time_stamp)
);

# Commodity Cache
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


Metals,Price,Day,%,Weekly,Monthly,YTD,YoY,Date