#pip install install requests

import requests

def pega_valor_moeda_web(moeda_padrao, moeda_destino):
    # Substitua pelo seu endpoint da API (Exemplo: ExchangeRate-API)
    api_url = f"https://v6.exchangerate-api.com/v6/64b07c933c8d4d2936e1e05d/latest/{moeda_padrao}"
    
    # Enviando a requisição GET
    resposta = requests.get(api_url)
    
    # Verificando se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        dados = resposta.json()
        
        # Verificando se a moeda alvo está presente
        if moeda_destino in dados['conversion_rates']:
            return dados['conversion_rates'][moeda_destino]
        else:
            return f"Moeda alvo ({moeda_destino}) não encontrada."
    else:
        return "Erro ao buscar dados da API."

# Função para buscar cotações do dólar, euro e libra
def pegar_valores_moedas():
    moeda_padrao = "USD"  
    
    # Códigos das moedas
    moedas = ["EUR", "GBP", "BRL"]
    
    print(f"Cotações base: {moeda_padrao}")
    
    for moeda in moedas:
        valor_moeda = pega_valor_moeda_web(moeda_padrao, moeda)
        print(f"{moeda}: {valor_moeda}")


#forma tradicional do python para começar um sistema
if __name__ == "__main__":
    pegar_valores_moedas()
