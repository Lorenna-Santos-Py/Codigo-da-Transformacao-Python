# Arquivo: main_veiculos.py

from veiculos import Carro, CarroEletrico

# Criação e uso de objetos Carro e CarroEletrico
carro_gasolina = Carro("Ford", "Focus")
carro_eletrico = CarroEletrico("Tesla", "Model 3", 500)

print("# Carro a Gasolina:")
print(f"Via método exibir_info(): **{carro_gasolina.exibir_info()}**")
# Uso do método especial __str__ (chamado implicitamente pelo print)
print(f"Via print direto (str): **{carro_gasolina}**") 

print("\n# Carro Elétrico:")
print(f"Via método exibir_info(): **{carro_eletrico.exibir_info()}**")
# Uso do método especial __str__ herdado
print(f"Via print direto (str): **{carro_eletrico}**")
