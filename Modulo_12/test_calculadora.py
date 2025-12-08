# Arquivo: test_calculadora.py

import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    """Classe de teste para a classe Calculadora."""

    def setUp(self):
        """Método executado antes de cada teste para inicializar a calculadora."""
        self.calc = Calculadora()

    # Testes para somar, subtrair, multiplicar (Atividade 2)
    def test_operacoes_basicas(self):
        self.assertEqual(self.calc.somar(10, 5), "15")
        self.assertEqual(self.calc.subtrair(10, 5), "5")
        self.assertEqual(self.calc.multiplicar(10, 5), "50")
        self.assertAlmostEqual(self.calc.dividir(10, 5), "2.0")

    # Teste de validação de entrada inválida (Atividade 3)
    def test_divisao_por_zero(self):
        """Verifica se a divisão por zero levanta a exceção esperada."""
        # O gerenciador de contexto 'self.assertRaises' verifica se o erro ocorre
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(10, 0)

# Para rodar este teste, execute no terminal/prompt: python -m unittest test_calculadora.py
