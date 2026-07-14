import requests
import json


url = "https://api.freecryptoapi.com/v1/getData"


query_params = {
    "symbol": "BTC + Eth",
    "token": ""  
}


response = requests.get(url, params=query_params)
data = response.json()
print(data)

with open('crypto.json', 'w', encoding="utf-8") as j_file:
    json.dump(data, j_file, indent=4, ensure_ascii=False)

