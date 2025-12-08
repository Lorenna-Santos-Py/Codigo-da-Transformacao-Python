# Arquivo: calculadora.py

class Calculadora:
    """
    Classe que realiza operações matemáticas básicas.
    Inclui lógica para lançar exceção na divisão por zero (Atividade 3).
    """

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            # Lança uma exceção para entradas inválidas, conforme solicitado na Atividade 3
            raise ZeroDivisionError("Não é possível dividir por zero")
        return a / b
