import requests
import json

url = "https://s2.coinmarketcap.com/generated/search/quick_search.json"
r = requests.get(url)
cont = r.json()
print(cont)
