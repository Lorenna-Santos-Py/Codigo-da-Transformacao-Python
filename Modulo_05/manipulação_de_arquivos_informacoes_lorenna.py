# Atividade 1: Manipulação de Arquivo TXT

nome_arquivo_txt = "informacoes.txt"
conteudo_a_gravar = "Esta é a primeira linha.\nEsta é a segunda linha.\nÉ útil para armazenar dados simples."

# 1. Gravar informações no arquivo TXT
print(f"--- Gravando dados em '{nome_arquivo_txt}' ---")
try:
    with open(nome_arquivo_txt, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo_a_gravar)
    print("Dados gravados com sucesso.")
except IOError as e:
    print(f"Erro ao gravar o arquivo: {e}")

# 2. Ler e exibir as informações do arquivo TXT
print(f"\n--- Lendo dados de '{nome_arquivo_txt}' ---")
try:
    with open(nome_arquivo_txt, 'r', encoding='utf-8') as arquivo:
        conteudo_lido = arquivo.read()
    print("Conteúdo lido:")
    print(conteudo_lido)
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo_txt}' não foi encontrado.")
except IOError as e:
    print(f"Erro ao ler o arquivo: {e}")
