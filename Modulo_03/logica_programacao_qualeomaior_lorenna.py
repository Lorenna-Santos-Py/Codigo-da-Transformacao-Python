
# Atividade 2: Comparação de Número

print("\n--- Atividade 2: Comparação de Números ---")
try:
    # Solicita a entrada do usuário e converte para float
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Compara os números usando if-elif-else
    if num1 > num2:
        print(f"O primeiro número ({num1}) é maior que o segundo ({num2}).")
    elif num2 > num1:
        print(f"O segundo número ({num2}) é maior que o primeiro ({num1}).")
    else:
        print("Ambos os números são iguais.")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números.")

# Atividade 3: Classificação de Idade

print("\n--- Atividade 3: Classificação de Idade ---")
try:
    # Solicita a idade e converte para inteiro
    idade = int(input("Digite sua idade: "))

    # Classifica a idade
    if idade < 0:
        print("Idade inválida.")
    elif idade <= 12:
        print("Classificação: Criança")
    elif idade <= 17:
        print("Classificação: Adolescente")
    elif idade <= 59:
        print("Classificação: Adulto")
    else:
        print("Classificação: Idoso")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número inteiro para a idade.")

