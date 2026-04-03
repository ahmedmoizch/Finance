import pandas as pd
from bs4 import BeautifulSoup
import requests
import io
import mysql.connector
from datetime import datetime

now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M")


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'portfolio',
    'auth_plugin': 'mysql_native_password'
}



url = "https://tradingeconomics.com/commodities"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}


a = 2
if a == 1:
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")

    #commodities = soup.find(class_="min-h-[50px] datatable-v2_table__93S4Y dynamic-table-v2_dynamic-table__iz42m datatable-v2_table--mobile-basic__uC0U0 datatable-v2_table--freeze-column__uGXoD undefined")
    commodities = soup.find_all("table")
    target_table = commodities[1]

    with open("TEcommodity.html", "w", encoding="utf-8") as file:
        file.write(target_table.prettify())


"""
#html_data = ("exa00mple.html"
df = pd.read_html("TEcommodity.html")
dfs = df[0]
path = "TEcommodity.csv"
dfs.to_csv(path, index=False)
"""

data = pd.read_csv('TEcommodity.csv')


connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

for index, row in data.iterrows():
    Symbol = row['Metals']
    Price = row['Price']
    Day = row['Day']
    Percentage = row['%']
    Weekly = row['Weekly']
    Monthly = row['Monthly']
    YTD = row['YTD']
    YoY = row['YoY']
    cursor.execute("INSERT INTO COMMODITY_CACHE VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (Symbol, Price, Day, Percentage, Weekly, Monthly, YTD, YoY, time,))



connection.commit()
cursor.close()
connection.close()


#for element in commodities.find_all(class_=("datatable-v2_cell--name__derived__L4iTy md:hidden")):
#    element.decompose()

#html_data = io.StringIO(str(commodities))
#df = pd.read_html(html_data)
#dfs = df[0]
#dfs.to_csv('commodities_current2.csv', index=False)

#data_sql = pd.read_csv('commodities_current2.csv')


#selected_columns = ['Name', 'Last']
#data_sql = data_sql[selected_columns]
"""
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

for index, row in data_sql.iterrows():
    symbol = row['Name']
    last = row['Last']
    cursor.execute("INSERT INTO COMMODITY_HISTORY (symbol, time_stamp, current_price) VALUES (%s, %s, %s)", (symbol, time, last, ))

connection.commit()
connection.close()
cursor.close()
"""