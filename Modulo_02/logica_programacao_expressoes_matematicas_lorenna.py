# Atividade 1: Operadores Aritméticos

print("--- Atividade 1: Operadores Aritméticos ---")
try:
    # Solicita a entrada do usuário e converte para float
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realiza as operações
    soma = num1 + num2
    diferenca = num1 - num2
    multiplicacao = num1 * num2
    # Trata divisão por zero
    if num2 != 0:
        divisao = num1 / num2
        resto = num1 % num2
        print(f"Soma: {soma}")
        print(f"Diferença: {diferenca}")
        print(f"Multiplicação: {multiplicacao}")
        print(f"Divisão: {divisao}")
        print(f"Resto da divisão: {resto}")
    else:
        print("Divisão e resto por zero não são possíveis.")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números.")

