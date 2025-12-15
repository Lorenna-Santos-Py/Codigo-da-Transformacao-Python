# Atividade 1: Lista de Compras

print("--- Gerenciador de Lista de Compras ---")

lista_compras = []

while True:
    print("\nOpções:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Visualizar lista")
    print("4. Sair")
    
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        item = input("Digite o item a ser adicionado: ")
        lista_compras.append(item)
        print(f"'{item}' adicionado à lista.")
    elif opcao == '2':
        item = input("Digite o item a ser removido: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"'{item}' removido da lista.")
        else:
            print(f"'{item}' não encontrado na lista.")
    elif opcao == '3':
        print("\nLista de Compras Atual:")
        if not lista_compras:
            print("A lista está vazia.")
        for i, item in enumerate(lista_compras, 1):
            print(f"{i}. {item}")
    elif opcao == '4':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")

