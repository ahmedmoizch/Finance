import pandas as pd
from bs4 import BeautifulSoup
import requests
import io
import datetime
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'portfolio'
}

datetime = datetime.datetime.now()
print(datetime)

url = "https://www.investing.com/commodities/metals"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}


response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, "html.parser")

#commodities = soup.find(class_="min-h-[50px] datatable-v2_table__93S4Y dynamic-table-v2_dynamic-table__iz42m datatable-v2_table--mobile-basic__uC0U0 datatable-v2_table--freeze-column__uGXoD undefined")
commodities = soup.find(class_="min-h-[50px] datatable-v2_table__93S4Y dynamic-table-v2_dynamic-table__iz42m datatable-v2_table--mobile-basic__uC0U0 datatable-v2_table--freeze-column__uGXoD undefined")

html_data = io.StringIO(str(commodities))
df = pd.read_html(html_data)
dfs = df[0]
#dfs.to_csv('commodities_current.csv', index=False)

data_sql = pd.read_csv('commodities_current.csv')
selected_columns = ['Name', 'Last']
data_sql = data_sql[selected_columns]

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

cursor.execute("INSERT INTO COMMODITY_HISTORY (SYMBOL, TIME_STAMP, CURRENT_PRICE)"
               "VALUES (%s, %s, %s)" ())

#with open("gold.html", 'w', encoding="utf-8") as file:
#    file.write(commodities.prettify())