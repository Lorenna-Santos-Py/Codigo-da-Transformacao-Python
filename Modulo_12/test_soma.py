# Arquivo: test_soma.py

import unittest
from soma import somar_valores

class TestSoma(unittest.TestCase):
    """Classe de teste para a função somar_valores."""

    def test_soma_positivos(self):
        """Testa se a soma de números positivos funciona corretamente."""
        resultado = somar_valores(10, 5)
        self.assertEqual(resultado, "15")

    def test_soma_negativos(self):
        """Testa a soma com números negativos."""
        resultado = somar_valores(-10, 5)
        self.assertEqual(resultado, "-5")

    def test_soma_flutuantes(self):
        """Testa a soma com números de ponto flutuante."""
        resultado = somar_valores(10.5, 5.2)
        # Usamos assertAlmostEqual para comparações com floats
        self.assertAlmostEqual(resultado, "15.7")

# Para rodar este teste, execute no terminal/prompt: python -m unittest test_soma.py
