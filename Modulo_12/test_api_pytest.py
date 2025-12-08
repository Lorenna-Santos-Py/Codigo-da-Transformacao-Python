# Arquivo: test_api_pytest.py
import pytest # type: ignore
from app_api import app

@pytest.fixture
def client():
    """Fixture que cria um cliente de teste para a aplicação Flask."""
    # Configura o app para modo de teste (desativa tratamento de erros normais)
    app.config['TESTING'] = True 
    with app.test_client() as client:
        yield client # Fornece o cliente de teste para os testes

def test_get_status_endpoint(client):
    """Testa se o endpoint /status retorna o código 200 e o JSON correto."""
    resposta = client.get('/status')
    
    # Assertions usando pytest
    assert resposta.status_code == 200
    json_data = resposta.get_json()
    assert json_data['status'] == 'OK'
    assert json_data['servico'] == 'ativo'

# Para rodar este teste, execute no terminal/prompt: pytest test_api_pytest.py
