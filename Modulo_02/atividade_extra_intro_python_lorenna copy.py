# =================================================================
#  DESAFIO EXTRA: Exibir a hora atual junto com a saudação
#  (Combinado com a Atividade 3)
# =================================================================

# PASSO 1: Importar a biblioteca datetime
# Este é o módulo padrão do Python para lidar com datas e horas.
import datetime

# --- ATIVIDADE 3: Interação com o Usuário ---
# Pede o nome do usuário e armazena o que foi digitado.
nome_usuario = input("Por favor, digite seu nome: ")

# --- DESAFIO EXTRA: Obter a Hora Atual ---

# Obtém um objeto que contém a data e hora exata do sistema no momento.
momento_atual = datetime.datetime.now()

# Formata o objeto 'momento_atual' para extrair e exibir apenas a hora, minuto e segundo.
# %H = Hora (24h), %M = Minuto, %S = Segundo.
hora_formatada = momento_atual.strftime("%H:%M:%S")

# --- Exibição Final ---

# Linhas de separação para melhorar a leitura da saída.
print("\n" + "=" * 50)

# 1. Mensagem de saudação personalizada (Atividade 3)
print(f"Olá, {nome_usuario}! É uma alegria te receber.")

# 2. Exibição da hora atual (Desafio Extra)
print(f"Informação extra: O horário exato de agora é: {hora_formatada}")

# Linhas de separação
print("=" * 50)