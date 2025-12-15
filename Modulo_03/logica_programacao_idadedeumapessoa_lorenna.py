

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

