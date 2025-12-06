# Atividade 3: Manipulação de Arquivo CSV

import csv
import os

nome_arquivo_csv = "notas_alunos.csv"
cabecalho = ["Nome", "Nota1", "Nota2", "Media"]

def adicionar_nota():
    nome = input("Digite o nome do aluno: ")
    try:
        nota1 = float(input("Digite a Nota 1: "))
        nota2 = float(input("Digite a Nota 2: "))
        media = (nota1 + nota2) / 2
        novo_aluno = [nome, nota1, nota2, media]

        # Abre o arquivo em modo 'a' (append) para adicionar uma nova linha
        with open(nome_arquivo_csv, 'a', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            # Se o arquivo estiver vazio, escreve o cabeçalho primeiro (requer verificação mais robusta em um app real)
            if os.stat(nome_arquivo_csv).st_size == 0:
                 writer.writerow(cabecalho)
            writer.writerow(novo_aluno)
        print(f"Notas de {nome} adicionadas com sucesso.")
    except ValueError:
        print("Entrada de nota inválida. Use números.")
    except IOError as e:
        print(f"Erro ao escrever no arquivo CSV: {e}")


def exibir_notas():
    print(f"\n--- Exibindo dados de '{nome_arquivo_csv}' ---")
    try:
        with open(nome_arquivo_csv, 'r', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                print(linha)
    except FileNotFoundError:
        print("Nenhum arquivo de notas encontrado. Adicione a primeira nota primeiro.")
    except IOError as e:
        print(f"Erro ao ler o arquivo CSV: {e}")

# Menu interativo para testar
if __name__ == "__main__":
    while True:
        print("\nMenu CSV:")
        print("1. Adicionar nova nota de aluno")
        print("2. Visualizar todas as notas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_nota()
        elif opcao == '2':
            exibir_notas()
        elif opcao == '3':
            print("Saindo do sistema de notas.")
            break
        else:
            print("Opção inválida.")

