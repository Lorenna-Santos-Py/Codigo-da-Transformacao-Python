# Desafio Extra: Agenda de Contatos

print("\n--- Agenda de Contatos (Dicionário) ---")

agenda = {}

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    agenda[nome] = telefone
    print(f"Contato '{nome}' adicionado.")

def remover_contato():
    nome = input("Digite o nome do contato a ser removido: ")
    if nome in agenda:
        del agenda[nome]
        print(f"Contato '{nome}' removido.")
    else:
        print(f"Contato '{nome}' não encontrado.")

def buscar_contato():
    nome = input("Digite o nome do contato a ser buscado: ")
    if nome in agenda:
        print(f"Telefone de '{nome}': {agenda[nome]}")
    else:
        print(f"Contato '{nome}' não encontrado.")

def visualizar_agenda():
    print("\nLista de Contatos:")
    if not agenda:
        print("A agenda está vazia.")
    for nome, telefone in agenda.items():
        print(f"Nome: {nome} | Telefone: {telefone}")

while True:
    print("\nMenu Agenda:")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Visualizar agenda")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_contato()
    elif opcao == '2':
        remover_contato()
    elif opcao == '3':
        buscar_contato()
    elif opcao == '4':
        visualizar_agenda()
    elif opcao == '5':
        print("Fechando agenda. Até mais!")
        break
    else:
        print("Opção inválida.")

