# Arquivo 2: programa_principal.py (O Programa Principal)

import utilidades # Importa o módulo criado

# Utilizando as funções importadas
num1 = 10
num2 = 5
base_val = 2
exp_val = 3

res_soma = utilidades.soma(num1, num2)
res_sub = utilidades.subtracao(num1, num2)
res_pot = utilidades.potencia(base_val, exp_val)

print(f"Soma de {num1} e {num2}: **{res_soma}**")
print(f"Subtração de {num1} e {num2}: **{res_sub}**")
print(f"Potência de {base_val} elevado a {exp_val}: **{res_pot}**")
