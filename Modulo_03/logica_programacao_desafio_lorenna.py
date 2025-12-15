
# Desafio Extra: Menu Interativo

print("\n--- Desafio Extra: Menu Interativo ---")

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

while True:
    print("\nEscolha uma opção:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Sair")
    
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '3':
        print("Saindo do programa. Até logo!")
        break # Sai do loop while

    if opcao in ('1', '2'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                resultado = soma(num1, num2)
                print(f"Resultado da Soma: {resultado}")
            elif opcao == '2':
                resultado = subtracao(num1, num2)
                print(f"Resultado da Subtração: {resultado}")
        except ValueError:
            print("Entrada inválida. Digite números válidos para a operação.")
    else:
        print("Opção inválida. Tente novamente.")

