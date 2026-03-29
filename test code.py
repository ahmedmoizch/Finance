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

for element in soup.find_all(class_=['tag tag--skim tag--def', 'tag tag--skim tag--xd', 'tag tag--skim tag--def']):
    element.decompose()