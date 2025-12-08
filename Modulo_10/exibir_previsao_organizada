import requests # type: ignore

API_KEY = 'SUA_CHAVE_DE_API_AQUI'
CIDADE = 'Rio de Janeiro'

def exibir_previsao_organizada(cidade, api_key):
    """Filtra e exibe dados relevantes da API em formato organizado."""
    url = f"api.openweathermap.org{cidade}&appid={api_key}&units=metric&lang=pt_br"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        
        # Filtrando dados relevantes
        nome_cidade = dados.get('name')
        pais = dados.get('sys', {}).get('country')
        temp_atual = dados.get('main', {}).get('temp')
        temp_max = dados.get('main', {}).get('temp_max')
        temp_min = dados.get('main', {}).get('temp_min')
        sensacao = dados.get('main', {}).get('feels_like')
        umidade = dados.get('main', {}).get('humidity')
        condicao_desc = dados.get('weather', [{}])[0].get('description')

        # Exibindo em um formato organizado
        print(f"--- Detalhes do Clima: {nome_cidade}, {pais} ---")
        print(f"Condição: **{condicao_desc.capitalize()}**")
        print(f"Temperatura Atual: **{temp_atual}°C**")
        print(f"Sensação Térmica: **{sensacao}°C**")
        print(f"Mínima do Dia: **{temp_min}°C**")
        print(f"Máxima do Dia: **{temp_max}°C**")
        print(f"Umidade do Ar: **{umidade}%**")

    except requests.exceptions.RequestException as e:
        print(f"**Erro de conexão ou HTTP:** {e}")

# Substitua 'SUA_CHAVE_DE_API_AQUI' pela sua chave real antes de rodar
exibir_previsao_organizada(CIDADE, API_KEY)
