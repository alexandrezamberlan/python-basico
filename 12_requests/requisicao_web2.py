#pip install install requests

import requests

# Função para buscar o clima de uma cidade
def pegar_clima(cidade, api_key):
    # URL da API do OpenWeatherMap com o parâmetro 'q' para cidade e 'appid' para chave de API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade},GBP&appid={api_key}&units=metric&lang=pt_br"
    
    # Enviar a requisição GET
    resposta = requests.get(url)
    
    # Verificar se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        dados = resposta.json()
        
        # Extrair os dados relevantes
        main = dados['main']
        weather = dados['weather'][0]
        wind = dados['wind']
        
        # Exibir as informações
        print(f"Cidade: {cidade.capitalize()}")
        print(f"Temperatura: {main['temp']}°C")
        print(f"Temperatura Mínima: {main['temp_min']}°C")
        print(f"Temperatura Máxima: {main['temp_max']}°C")
        print(f"Condição: {weather['description'].capitalize()}")
        print(f"Umidade: {main['humidity']}%")
        print(f"Velocidade do vento: {wind['speed']} m/s")
        print('-' * 40)
    else:
        print(f"Erro ao obter dados para {cidade}: {resposta.status_code}")

# Função para obter o clima de várias cidades
def pegar_clima_cidades(cidades, api_key):
    for cidade in cidades:
        pegar_clima(cidade, api_key)

if __name__ == "__main__":
    # Substitua 'YOUR_API_KEY' pela chave que você obteve ao se registrar na API do OpenWeatherMap
    api_key = '57f02dc11685a9611b42a5a22012380c'

    # Lista de cidades brasileiras para as quais você deseja obter o clima
    cidades = ['Santa Maria', 'São Paulo', 'Brasília']

    # Buscar o clima para as cidades
    pegar_clima_cidades(cidades, api_key)
