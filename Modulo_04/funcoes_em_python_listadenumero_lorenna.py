# Define a função 'maior_menor' que aceita uma lista de números
def maior_menor(lista_de_numeros):
    """Recebe uma lista de números e retorna o maior e o menor valor da lista."""
    if not lista_de_numeros:
        return None, None # Retorna None se a lista for vazia
        
    # Python possui funções integradas eficientes para isso
    maior_valor = max(lista_de_numeros)
    menor_valor = min(lista_de_numeros)
    
    # Retorna o maior e o menor valor
    return maior_valor, menor_valor

# Exemplo de uso da função
print("\n# 3. Maior e Menor Valor da Lista")
minha_lista = [15, 2, 80, 42, 5, 99, 1]

maior_num, menor_num = maior_menor(minha_lista)

print(f"Lista fornecida: {minha_lista}")
print(f"Maior valor: {maior_num}")
print(f"Menor valor: {menor_num}")
