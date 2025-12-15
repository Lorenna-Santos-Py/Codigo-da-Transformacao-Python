# =================================================================
#  ATIVIDADE 3: Programa de Saudação Personalizada
# =================================================================

# 1. Receber o nome do usuário:
# A função 'input()' exibe o prompt (pergunta) e espera o usuário digitar.
# O texto digitado é então armazenado na variável 'nome_usuario'.
nome_usuario = input("Qual é o seu nome? Por favor, digite aqui: ")

# 2. Exibir a mensagem personalizada:
# Usamos a função 'print()' e uma f-string (string formatada) para
# incorporar o conteúdo da variável 'nome_usuario' na saudação.
print(f"Olá, {nome_usuario}! É um prazer tê-lo(a) por aqui. Seja bem-vindo(a)!")

# Mensagem de encerramento (opcional)
print("-" * 40)
print("Fim do programa de saudação.")