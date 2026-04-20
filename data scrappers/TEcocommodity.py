import pandas as pd
from bs4 import BeautifulSoup
import requests
import io
import mysql.connector
from datetime import datetime




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
if a == 2:
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")

    commodities = soup.find_all("table")
    target_table = commodities[1]
    df = pd.read_html(io.StringIO(target_table.prettify()))[0]
    #target_table['Monthly'] = target_table['Monthly'].str.replace('%', '').astype(float) / 100

    #with open("TEcommodity.html", "w", encoding="utf-8") as file:
    #    file.write(df)

    percent_cols = ['%', 'Weekly', 'Monthly', 'YTD', 'YoY']
    for col in percent_cols:
        if col in df.columns:
            df[col] = (df[col].astype(str).str.replace('%', '').astype(float) / 100).round(4)


df.to_csv('TEcommodity.csv', index=False)
data = pd.read_csv("TEcommodity.csv")


connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")

def database():
    # MAKE TABLE EMPTY
    cursor.execute("TRUNCATE TABLE commodity_cache")


    for index, row in data.iterrows():
        Symbol = row['Metals']
        Price = row['Price']
        Day = row['Day']
        Percentage = row['%']
        Weekly = row['Weekly']
        Monthly = row['Monthly']
        YTD = row['YTD']
        YoY = row['YoY']
        cursor.execute("INSERT INTO commodity_cache values (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (Symbol, Price, Day, Percentage, Weekly, Monthly, YTD, YoY, time,))



    connection.commit()
    cursor.close()
    connection.close()

database()