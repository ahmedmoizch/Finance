import pandas as pd
import mysql.connector

df = pd.read_csv('psx_current.csv')
category = "PSX"
name = "Null"

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'portfolio'
}
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

for index, row in df.iterrows():
    symbol = row['SYMBOL']
    cursor.execute("INSERT INTO ASSETS (ASSET, ASSET_NAME, CATEGORY) VALUES (%s,%s,%s)", (symbol, name, category,))

connection.commit()
cursor.close()
connection.close()

print("Commit Sucessfull")