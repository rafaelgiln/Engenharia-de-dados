# This example uses Python 2.7 and the python-request library.

# %%
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

tabela = []

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'a81eae65-6516-4d6d-88dd-c22a10be1065',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    tabela = pd.json_normalize(data)
    print(tabela.head(10))
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

# %%
