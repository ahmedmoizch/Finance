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



url = "https://www.fxempire.com/commodities"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}


#response = requests.get(url, headers = headers)
#soup = BeautifulSoup(response.text, "html.parser")

#wanted = soup.find(class_= "sc-742a2147-0 iUWeVF")

#with open("fxempire.html", 'w', encoding='utf-8') as file:
#    file.write(wanted.prettify())



df = pd.read_html('fxempire.html')
print(df)
