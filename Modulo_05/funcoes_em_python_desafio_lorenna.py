# Define a função 'validar_login' e usa um dicionário para armazenar dados de login
def validar_login(usuario_digitado, senha_digitada):
    """Valida o usuário e senha com base em um dicionário de usuários autorizados."""
    
    # Dicionário de usuários autorizados (chave=usuario, valor=senha)
    usuarios_autorizados = {
        "admin": "senha123",
        "joao": "python456",
        "maria": "abc!@#def"
    }
    
    # Verifica se o usuário existe no dicionário
    if usuario_digitado in usuarios_autorizados:
        # Verifica se a senha corresponde à senha armazenada para aquele usuário
        if usuarios_autorizados[usuario_digitado] == senha_digitada:
            return True # Login bem-sucedido
        else:
            return False # Senha incorreta
    else:
        return False # Usuário não encontrado

# Exemplo de uso do sistema de login
print("\n# Desafio Extra: Sistema de Login")
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if validar_login(usuario, senha):
    print(f"Login bem-sucedido! Bem-vindo(a), {usuario}.")
else:
    print("Erro: Usuário ou senha incorretos.")

