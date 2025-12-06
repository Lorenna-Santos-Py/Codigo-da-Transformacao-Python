# Atividade 3: Pares e Ímpares

print("\n--- Identificador de Números Pares e Ímpares ---")

# Conjunto de números a ser analisado
conjunto_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 21, 22]

pares = []
impares = []

# Loop para iterar sobre o conjunto de números
for numero in conjunto_numeros:
    # Usa o operador módulo (%) para verificar se o número é par
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Exibe os resultados
print(f"Conjunto original: {conjunto_numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")

