import requests

link_api_current_weather = "ttp://api.weatherapi.com/v1/current.json"
api_key = "f21b27a8e2bd467fa8b130113262803"

resposta = requests.get(link_api_current_weather)

print(resposta.status_code)