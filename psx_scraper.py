import mysql.connector
import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# time Now
now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M")

url = "https://dps.psx.com.pk/market-watch"

# IMPORTING AND STORING DATA IN CSV FILE
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

html_data = io.StringIO(str(soup))
df = pd.read_html(html_data)
dfs = df[0]
dfs.to_csv('psx_cache.csv', index=False)

#Local DataBase
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'portfolio'
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

df_sql = pd.read_csv('psx_cache.csv')
data = df_sql[['SYMBOL','CURRENT','VOLUME']]

for index, row in data.iterrows():
    symbol = row['SYMBOL']
    current = row['CURRENT']
    volume = row['VOLUME']
    cursor.execute("INSERT INTO psx_history (symbol, time_stamp, current_price, volume) VALUES (%s, %s,%s ,%s)", (symbol,time,current,volume))


#insert into historic_data_psx values
connection.commit()

cursor.close()
connection.close()