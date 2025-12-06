# Define a função 'calcular_media' que aceita notas como parâmetros
def calcular_media(nota1, nota2, nota3):
    """Calcula a média de três notas e retorna o resultado e o status (Aprovado/Reprovado)."""
    media = (nota1 + nota2 + nota3) / 3
    
    if media >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"
        
    # Retorna múltiplos valores (média e status)
    return media, status

# Exemplo de uso da função
print("\n# 2. Calcular Média e Status")

# Aluno aprovado
media_aluno1, status_aluno1 = calcular_media(8.0, 9.0, 7.5)
print(f"Média do Aluno 1: {media_aluno1:.2f} | Status: {status_aluno1}")

# Aluno reprovado
media_aluno2, status_aluno2 = calcular_media(5.0, 6.5, 4.0)
print(f"Média do Aluno 2: {media_aluno2:.2f} | Status: {status_aluno2}")
