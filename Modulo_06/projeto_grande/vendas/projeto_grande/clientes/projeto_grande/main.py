# Arquivo: projeto_grande/main.py

# Importa funções específicas dos módulos dentro dos pacotes
from vendas.calculos import calcular_total
from clientes.cadastro import cadastrar_novo_cliente

# Exemplo de uso das funcionalidades de diferentes pacotes
lista_itens = [
    {'preco': 50.00, 'quantidade': 3},
    {'preco': 12.50, 'quantidade': 10}
]

# Usa a função do pacote 'vendas'
valor_total = calcular_total(lista_itens)
print(f"O valor total da venda é: **R$ {valor_total:.2f}**")

# Usa a função do pacote 'clientes'
status_cadastro = cadastrar_novo_cliente("Mariana Silva", "mariana.s@exemplo.com")
print(f"Status do cadastro: **{status_cadastro}**")
