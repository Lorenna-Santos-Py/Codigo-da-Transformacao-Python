# Arquivo: veiculos.py

class Carro:
    """
    Representa um carro genérico.
    Atividade 1: Atributos marca, modelo e método exibir_info().
    Atividade 3: Uso de __init__ e __str__.
    """
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        """Exibe as informações básicas do carro."""
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

    def __str__(self):
        """Método especial para representação em string."""
        return self.exibir_info()

class CarroEletrico(Carro):
    """
    Representa um carro elétrico, herdando de Carro.
    Atividade 2: Implementa herança e adiciona autonomia_bateria.
    """
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        """Sobrescreve o método para incluir a autonomia."""
        info_basica = super().exibir_info()
        return f"{info_basica}, Autonomia da Bateria: {self.autonomia_bateria} km"

    # __str__ é herdado, então ele usará o novo exibir_info()
