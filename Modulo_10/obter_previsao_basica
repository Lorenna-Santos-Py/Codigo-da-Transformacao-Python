import requests # type: ignore
import json

API_KEY = 'SUA_CHAVE_DE_API_AQUI' 
CIDADE = 'Sao Paulo'

def obter_previsao_basica(cidade, api_key):
    """Obtém temperatura e condições climáticas básicas."""
    url = f"api.openweathermap.org{cidade}&appid={api_key}&units=metric&lang=pt_br"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status() # Lança um erro para status HTTP ruins (4xx ou 5xx)
        dados = resposta.json()
        
        temperatura = dados['main']['temp']
        condicoes = dados['weather'][0]['description']
        
        print(f"--- Previsão do Tempo para {cidade} ---")
        print(f"Temperatura atual: **{temperatura}°C**")
        print(f"Condições climáticas: **{condicoes.capitalize()}**")

    except requests.exceptions.RequestException as e:
        print(f"**Erro de conexão:** {e}")
    except json.JSONDecodeError:
        print("**Erro ao decodificar a resposta JSON da API.**")
    except KeyError as e:
        print(f"**Erro ao processar dados:** Chave ausente no JSON: {e}")

# Substitua 'SUA_CHAVE_DE_API_AQUI' pela sua chave real antes de rodar
obter_previsao_basica(CIDADE, API_KEY)
