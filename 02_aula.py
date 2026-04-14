import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv   ##serve para bloquear as senhas, precisa criar um arquivo .env
import os

load_dotenv()

url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/15?"
token = os.getenv("API_TOKEN")             ##chamo o token que defino no arquivo .env

payload = {}
headers = {
  'x-api-key': token           ##serve para armazenar a senha
}

response = requests.request("GET", url, headers=headers, data=payload)


transform_json = pd.DataFrame(response.json(), columns=['timestamp','high','low','bid'])  ## pego só as colunas que quero

transform_json['timestamp'] = pd.to_datetime(transform_json['timestamp'].astype(int), unit='s')   ## conversão da data

#lista_extraction = pd.DataFrame(response)

print(transform_json)
