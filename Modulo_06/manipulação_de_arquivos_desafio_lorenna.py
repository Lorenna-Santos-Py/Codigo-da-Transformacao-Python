# Desafio Extra: Sistema de Backup Automático

import shutil
import os
import time

# Define os diretórios de origem e destino
DIR_ORIGEM = "./pasta_origem"
DIR_DESTINO = "./pasta_backup"

def criar_diretorios():
    """Garante que os diretórios de origem e destino existam."""
    os.makedirs(DIR_ORIGEM, exist_ok=True)
    os.makedirs(DIR_DESTINO, exist_ok=True)
    print(f"Diretórios garantidos: Origem='{DIR_ORIGEM}', Destino='{DIR_DESTINO}'")

def criar_arquivos_teste():
    """Cria arquivos de exemplo na pasta de origem para testar o backup."""
    with open(os.path.join(DIR_ORIGEM, "doc_importante_1.txt"), "w") as f:
        f.write("Conteúdo do documento 1.")
    with open(os.path.join(DIR_ORIGEM, "planilha_dados.csv"), "w") as f:
        f.write("col1,col2\n1,2")
    print("Arquivos de teste criados na pasta de origem.")

def realizar_backup():
    """Copia todos os arquivos da origem para o destino."""
    print(f"\nIniciando backup de '{DIR_ORIGEM}' para '{DIR_DESTINO}'...")
    try:
        # Itera sobre os arquivos na pasta de origem
        for nome_arquivo in os.listdir(DIR_ORIGEM):
            caminho_origem = os.path.join(DIR_ORIGEM, nome_arquivo)
            caminho_destino = os.path.join(DIR_DESTINO, nome_arquivo)
            
            # Copia o arquivo (mantém metadados)
            shutil.copy2(caminho_origem, caminho_destino)
            print(f"  Copiado: {nome_arquivo}")
            
        print("Backup concluído com sucesso!")
    except FileNotFoundError:
        print("Erro: Um dos diretórios não existe.")
    except Exception as e:
        print(f"Ocorreu um erro durante o backup: {e}")


# Execução principal do script
if __name__ == "__main__":
    criar_diretorios()
    criar_arquivos_teste()
    # Pequena pausa para garantir que timestamps sejam diferentes (para fins de teste)
    time.sleep(1) 
    realizar_backup()

