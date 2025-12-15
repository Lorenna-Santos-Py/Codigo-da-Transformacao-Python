import random
import string

def gerar_senha(comprimento=12):
    """
    Gera uma senha aleatória com caracteres misturados.

    Argumentos:
        comprimento (int): O tamanho desejado para a senha. Padrão é 12.

    Retorna:
        str: A senha gerada.
    """
    # Define o conjunto de caracteres que podem ser usados na senha
    caracteres = string.ascii_letters  # Letras maiúsculas e minúsculas
    caracteres += string.digits        # Números (0-9)
    caracteres += string.punctuation   # Símbolos (!"#$%&'...)

    # Gera a senha escolhendo aleatoriamente os caracteres
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

# Bloco principal para executar o gerador
if __name__ == "__main__":
    print("--- Gerador de Senhas Seguras ---")

    # Gera uma senha de 12 caracteres (padrão)
    senha_curta = gerar_senha()
    print(f"Senha de 12 caracteres: {senha_curta}")

    # Gera uma senha de 18 caracteres
    senha_longa = gerar_senha(comprimento=18)
    print(f"Senha de 18 caracteres: {senha_longa}")

    # Gera uma senha curta
    senha_muito_curta = gerar_senha(comprimento=6)
    print(f"Senha de 6 caracteres: {senha_muito_curta}")