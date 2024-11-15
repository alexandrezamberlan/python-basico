import requests

def get_exchange_rate(base_currency, target_currency):
    # Substitua pelo seu endpoint da API (Exemplo: ExchangeRate-API)
    api_url = f"https://v6.exchangerate-api.com/v6/64b07c933c8d4d2936e1e05d/latest/{base_currency}"
    
    # Enviando a requisição GET
    response = requests.get(api_url)
    
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        
        # Verificando se a moeda alvo está presente
        if target_currency in data['conversion_rates']:
            return data['conversion_rates'][target_currency]
        else:
            return f"Moeda alvo ({target_currency}) não encontrada."
    else:
        return "Erro ao buscar dados da API."

# Função para buscar cotações do dólar, euro e libra
def get_all_exchange_rates():
    base_currency = "USD"  # Dólar Americano
    
    # Códigos das moedas
    currencies = ["EUR", "GBP"]
    
    print(f"Cotações base: {base_currency}")
    
    for currency in currencies:
        rate = get_exchange_rate(base_currency, currency)
        print(f"{currency}: {rate}")

if __name__ == "__main__":
    get_all_exchange_rates()
