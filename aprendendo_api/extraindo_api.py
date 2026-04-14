

import requests
import pprint

link_api_current_weather = "http://api.weatherapi.com/v1/current.json"    ### precisa do link
api_key = "37165db9f3c94069a7f141515262803"                               ### precisa da key

parametros = {                                ### Existem parametros obrigatórios e não obrigatórios, opcionais ou não opcionais, isso tudo vai estar dentro da documentação.
    "key": api_key,
    "q": "Tijucas",
    "lang": "pt"
}

resposta = requests.get(link_api_current_weather, params=parametros)

print(resposta.status_code)  
print(resposta.content)   
### 200 = Deu certo
### 300 =  Redirecionada 
### 400 = Não conseguiu fazer a Requisição 
### 500 = Deu erro no Sistema

if resposta.status_code == 200:
    dados_requisicao = resposta.json()
    pprint.pprint(dados_requisicao)
    
    temp = dados_requisicao["current"]["temp_c"]
    localizacao = dados_requisicao["location"]["country"]
    cidade = dados_requisicao["location"]["name"]
    condicao = dados_requisicao["current"]["condition"]["text"]
    
    print(localizacao," ",cidade," ", temp," ",condicao)
    print("A temperatura em {},{} é de {}, condição do clima é de {}".format(localizacao,cidade,temp, condicao))