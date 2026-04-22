import mysql.connector
import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# time Now
now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")

url = "https://dps.psx.com.pk/market-watch"

# IMPORTING AND STORING DATA IN CSV FILE
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
for element in soup.find_all(class_=['tag tag--skim tag--def', 'tag tag--skim tag--xd', 'tag tag--skim tag--def']):
    element.decompose()

"""
percent_cols = ['CHANGE (%)']
for col in percent_cols:
    if col in soup.columns:
        df[col] = (df[col].astype(str).str.replace('%', '').astype(float) / 100).round(4)
"""

html_data = io.StringIO(str(soup))
df = pd.read_html(html_data)
dfs = df[0]
percent_cols = ['CHANGE (%)']
for col in percent_cols:
    if col in dfs.columns:
        dfs[col] = (dfs[col].astype(str).str.replace('%', '').astype(float) / 100).round(4)

dfs.to_csv('psx_current.csv', index=False)


#Local DataBase
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'portfolio'
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

df_sql = pd.read_csv('psx_current.csv')
df_sql = df_sql.replace({float('nan'): None})
data = df_sql[['SYMBOL','SECTOR','LISTED IN','LDCP','OPEN','HIGH','LOW','CURRENT','CHANGE','CHANGE (%)','VOLUME']]

for index, row in data.iterrows():
    symbol = row['SYMBOL']
    sector = row['SECTOR']
    current = row['CURRENT']
    listedin = row['LISTED IN']
    ldcp = row['LDCP']
    open = row['OPEN']
    high = row['HIGH']
    low = row['LOW']
    current = row['CURRENT']
    change = row['CHANGE']
    current_per = row['CHANGE (%)']
    volume = row['VOLUME']
    cursor.execute("INSERT INTO psx_cache (Symbol,Sector,`listed In`,LDCP,`Open`,High,Low,`Change`,Current,`Change (%)`,Volume,Date_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (symbol,sector,listedin,ldcp,open,high,low,change,current,current_per,volume,time,))


#insert into historic_data_psx values
connection.commit()

cursor.close()
connection.close()
