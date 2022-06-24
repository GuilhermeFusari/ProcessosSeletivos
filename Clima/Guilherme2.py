import requests
CEP = input("Digite seu CEP: ")
def get_temperature(cep):
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    address_data = request.json()
    cidade = address_data['localidade']

    API_KEY = "ChaveApi"
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link)

    dicionario = requisicao.json()

    Clima = dicionario['weather'][0]['description']
    Temperatura_kelvin= dicionario['main']['temp']
    Temperatura = int(Temperatura_kelvin)-273.15

    print("O clima em",cidade, "é",Clima,"\nA temperatura é de: ","%.2f" %Temperatura, "°C")
    return
get_temperature(CEP)
