import requests # type: ignore
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException # type: ignore

def testar_erros_conexao(url):
    """Testa tratamento de exceções para diferentes falhas de requisição."""
    try:
        # Aumentando o timeout para simular problemas de conexão lenta
        resposta = requests.get(url, timeout=5) 
        resposta.raise_for_status() # Lança HTTPError para respostas inválidas (4xx/5xx)
        
        print(f"Sucesso: Status {resposta.status_code}. Tamanho da resposta: {len(resposta.content)} bytes.")

    except Timeout:
        print("**Erro de Timeout:** A requisição demorou muito para responder (conexão lenta?).")
    except ConnectionError:
        print("**Erro de Conexão:** Falha ao estabelecer uma conexão de rede com o servidor (URL incorreta ou sem internet?).")
    except HTTPError as e:
        print(f"**Erro HTTP:** Resposta inválida do servidor: {e.response.status_code}.")
    except RequestException as e:
        # Captura quaisquer outros erros da biblioteca requests
        print(f"**Ocorreu um erro inesperado na requisição:** {e}")
    except Exception as e:
        # Captura erros genéricos do Python
        print(f"**Um erro geral ocorreu:** {e}")

# Exemplos de URL para testar:
URL_VALIDA = "api.github.com"
URL_INVALIDA_404 = "api.github.com"
URL_INEXISTENTE_HOST = "https://um.dominio.que.nao.existe.com"

print("--- Teste de URL Válida ---")
testar_erros_conexao(URL_VALIDA)

print("\n--- Teste de URL Inexistente (404) ---")
testar_erros_conexao(URL_INVALIDA_404)

print("\n--- Teste de Host Inexistente (ConnectionError) ---")
testar_erros_conexao(URL_INEXISTENTE_HOST)
