import requests # type: ignore

API_KEY = 'SUA_CHAVE_DE_API_AQUI'

def buscar_filmes_populares(api_key):
    """Busca e exibe informações de filmes populares usando a API do TMDB."""
    url = f"api.themoviedb.org{api_key}&language=pt-BR"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        filmes = dados.get('results', [])

        print("--- Filmes Populares (TMDB) ---")
        for i, filme in enumerate(filmes[:5]): # Exibe os 5 primeiros filmes
            titulo = filme.get('title')
            sinopse = filme.get('overview')
            data_lancamento = filme.get('release_date')
            
            print(f"\n# {i+1}. **{titulo}**")
            print(f"Lançamento: {data_lancamento}")
            print(f"Sinopse: {sinopse[:200]}...") # Limita a sinopse para brevidade

    except requests.exceptions.RequestException as e:
        print(f"**Erro de conexão com a API do TMDB:** {e}")

# Substitua 'SUA_CHAVE_DE_API_AQUI' pela sua chave real antes de rodar
buscar_filmes_populares(API_KEY)
