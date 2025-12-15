# =================================================================
#  PARTE 1: Demonstração da Atividade 2 (Comandos Básicos)
#  Estes comandos seriam tipicamente executados no interpretador (REPL)
# =================================================================

print("--- DEMONSTRAÇÃO ATIVIDADE 2 (Comandos Básicos) ---")

# Comando print(): Usado para exibir mensagens (strings) na tela
print("Olá, este é um teste de mensagem com a função print().")

# Comando print(): Também pode exibir resultados de cálculos
print("O resultado de 5 + 3 é:", 5 + 3)

# Comando type(): Usado para identificar o tipo de dado de uma variável ou valor
# O resultado é exibido automaticamente no interpretador, mas usaremos print() para exibi-lo no script
print("O tipo de 'Python' é:", type("Python")) # Deve retornar <class 'str'> (string/texto)
print("O tipo de 150 é:", type(150))           # Deve retornar <class 'int'> (inteiro)
print("O tipo de 9.99 é:", type(9.99))         # Deve retornar <class 'float'> (decimal)

print("\n") # Linha em branco para separar as seções


# =================================================================
#  PARTE 2: Atividade 3 e Desafio Extra (Saudação Personalizada)
# =================================================================

# Importa o módulo (biblioteca) 'datetime' do Python, necessário para trabalhar com datas e horas.
# Este é um passo essencial para o Desafio Extra.
import datetime

print("--- INÍCIO DO PROGRAMA DE SAUDAÇÃO PERSONALIZADA (Atividade 3 & Desafio Extra) ---")

# --- Atividade 3: Interação com o Usuário ---

# A função input() pausa a execução e espera que o usuário digite algo,
# armazenando o texto digitado na variável 'nome'.
nome_usuario = input("Por favor, digite seu nome: ")

# --- Desafio Extra: Capturar e Formatar a Hora Atual ---

# datetime.datetime.now() obtém a data e hora exatas do sistema no momento da execução.
hora_e_data_agora = datetime.datetime.now()

# O método strftime() formata o objeto datetime em uma string legível.
# "%H" = Hora (24h), "%M" = Minuto, "%S" = Segundo.
hora_formatada = hora_e_data_agora.strftime("%H:%M:%S")

# --- Exibição do Resultado ---

# Utilizamos f-strings (strings formatadas) para inserir (interpolar) o valor
# da variável 'nome_usuario' diretamente na mensagem.
mensagem_final = f"Olá, {nome_usuario}! Seja muito bem-vindo(a)."

# Exibe a saudação personalizada (Atividade 3)
print("\n" + "=" * 50)
print(mensagem_final)

# Exibe a hora atual como complemento (Desafio Extra)
print(f"A hora atual do sistema é: {hora_formatada}")
print("=" * 50)

print("--- FIM DO PROGRAMA ---")