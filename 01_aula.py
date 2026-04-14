import requests
import pandas as pd
from datetime import datetime

url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/15?"

payload = {}
headers = {
  'x-api-key': '8e9efc99e71c8a6aa5a7d16621bbced983de1fafec822d8cc2b2d17e49ed31df'
}

response = requests.request("GET", url, headers=headers, data=payload)


transform_json = pd.DataFrame(response.json(), columns=['timestamp','high','low','bid'])  ## pego só as colunas que quero

transform_json['timestamp'] = pd.to_datetime(transform_json['timestamp'].astype(int), unit='s')   ## conversão da data

#lista_extraction = pd.DataFrame(response)

transform_json.to_excel('transform_json.xlsx', index=False)  ##index é para criar uma coluna de indice
