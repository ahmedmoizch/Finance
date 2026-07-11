"""
import requests

# 1. Use the correct endpoint for FreeCryptoAPI
url = "https://api.freecryptoapi.com/v1/getTop?top=3"

# 2. Set your query parameter (BTC for Bitcoin) and headers
query_params = {"symbol": "BTC"}
headers = {
    "Authorization": "texmif9xjpe0rbh7nui8"  # <-- Paste your actual FreeCryptoAPI key here
}

# 3. Fetch the data safely
response = requests.get(url, params=query_params, headers=headers)
print(response.json())
"""

import requests

# 1. Base URL for fetching the top 3 coins
url = "https://api.freecryptoapi.com/v1/getData"

# 2. Put your parameters and your token directly into query_params
query_params = {
    "symbol": "shib + BTC + ETH",
    "token": ""  # <-- Replace this string with your real API token
}

# 3. Fetch the data safely

response = requests.get(url, params=query_params)

# 4. Handle and display the data safely
if response.status_code == 200:
    data = response.json()
    
    # Check if the API returned an error structure
    if data.get('status') is False:
        print(f"API Error: {data.get('error')}")
    else:
        print("Success! Here is the top coins data:")
        print(data)
else:
    print(f"Server Connection Error. Code: {response.status_code}")


"""
# Debug step: check if the request was actually successful before parsing
if response.status_code == 200:
    data = response.json()
    print(f"Symbol: {data['symbol']}")
    print(f"Bitcoin Price: ${data['price']}")
    print(f"24h Change: {data['change_24h']}%")
else:
    print(f"Error Code: {response.status_code}")
    print(f"Server Response: {response.text}")
"""