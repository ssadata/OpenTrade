# load libraries
import pandas as pd
import requests, json

# available tables
tables = json.loads(requests.get("https://api.tradestatistics.io/tables").text)
pd.DataFrame.from_dict(tables, orient='columns')

# bilateral and product detailed data
trade = json.loads(requests.get("https://api.tradestatistics.io/yrpc?y=2018&r=chl&p=arg").text)
pd.DataFrame.from_dict(trade, orient='columns')

# detailed products 
products = json.loads(requests.get("https://api.tradestatistics.io/products").text)
pd.DataFrame.from_dict(products, orient='columns')
