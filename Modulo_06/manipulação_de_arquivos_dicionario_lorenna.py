# Atividade 2: Manipulação de Arquivo JSON

import json

nome_arquivo_json = "clientes.json"

dados_clientes = {
    "cliente1": {"nome": "Alice", "idade": 30, "ativo": True},
    "cliente2": {"nome": "Bruno", "idade": 45, "ativo": False},
    "cliente3": {"nome": "Carla", "idade": 22, "ativo": True}
}

# 1. Salvar o dicionário em um arquivo JSON
print(f"--- Salvando dicionário em '{nome_arquivo_json}' ---")
try:
    with open(nome_arquivo_json, 'w', encoding='utf-8') as arquivo_json:
        json.dump(dados_clientes, arquivo_json, indent=4, ensure_ascii=False)
    print("Dados JSON salvos com sucesso.")
except IOError as e:
    print(f"Erro ao salvar o arquivo JSON: {e}")

# 2. Carregar e exibir os dados do arquivo JSON
print(f"\n--- Carregando dados de '{nome_arquivo_json}' ---")
try:
    with open(nome_arquivo_json, 'r', encoding='utf-8') as arquivo_json:
        dados_carregados = json.load(arquivo_json)
    print("Dados JSON carregados:")
    print(dados_carregados)
    # Exemplo de acesso a um dado específico
    print(f"\nIdade do cliente1: {dados_carregados['cliente1']['idade']}")
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo_json}' não foi encontrado.")
except json.JSONDecodeError:
    print("Erro ao decodificar o JSON. O arquivo pode estar corrompido.")
except IOError as e:
    print(f"Erro ao ler o arquivo JSON: {e}")
