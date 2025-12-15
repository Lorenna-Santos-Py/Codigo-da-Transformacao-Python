# Arquivo: gerador_dados_falsos.py

from faker import Faker # type: ignore

# Cria um objeto Faker, opcionalmente configurando o idioma para português do Brasil
fake = Faker('pt_BR')

# Gerando e imprimindo dados falsos
print("--- Gerador de Dados Falsos ---")
print(f"Nome: **{fake.name()}**")
print(f"Endereço: **{fake.address()}**")
print(f"E-mail profissional: **{fake.company_email()}**")
print(f"Profissão: **{fake.job()}**")
