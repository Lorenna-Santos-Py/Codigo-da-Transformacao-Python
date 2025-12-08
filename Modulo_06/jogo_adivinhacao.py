# Arquivo: jogo_adivinhacao.py

import random
import math # Importado conforme solicitado na atividade

def jogar_adivinhacao():
    # Gere um número aleatório inteiro entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    
    while True:
        try:
            palpite = int(input("Digite o seu palpite: "))
            tentativas += 1
            
            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou o número (**{numero_secreto}**) em **{tentativas}** tentativas.")
                break
            elif palpite < numero_secreto:
                print("Tente um número MAIOR.")
            else:
                print("Tente um número MENOR.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Inicia o jogo
if __name__ == "__main__":
    jogar_adivinhacao()
