# Atividade 2: Dados do Aluno

print("\n--- Cadastro de Aluno ---")

# Cria um dicionário com as informações do aluno
dados_aluno = {
    "nome": "João Silva",
    "idade": 16,
    "notas": [8.5, 9.0, 7.5],
    "média": 8.33
}

# Exibe os dados armazenados no console
print("\nDados do Aluno:")
print(f"Nome: {dados_aluno['nome']}")
print(f"Idade: {dados_aluno['idade']} anos")
print(f"Notas: {dados_aluno['notas']}")
print(f"Média: {dados_aluno['média']}")

# Iterando sobre o dicionário para mostrar chaves e valores
print("\nDados detalhados (Chave: Valor):")
for chave, valor in dados_aluno.items():
    print(f"{chave.capitalize()}: {valor}")

