# Arquivo: projeto_grande/vendas/calculos.py

def calcular_total(itens):
    """Calcula o valor total de uma lista de itens de compra."""
    return sum(item['preco'] * item['quantidade'] for item in itens)
