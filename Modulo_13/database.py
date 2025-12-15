import sqlite3

DATABASE = 'banco_de_dados_usuarios.db'

def get_db_connection():
    # ... (Função inalterada)
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializa o banco de dados, criando as tabelas 'usuarios', 'posts' e 'comments'."""
    conn = get_db_connection()
    try:
        # Tabela 1: Usuários (Já existia)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """)
        
        # Tabela 2: Posts (Novidade do Desafio Extra)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                conteudo TEXT NOT NULL,
                autor_id INTEGER NOT NULL,
                FOREIGN KEY (autor_id) REFERENCES usuarios (id)
            );
        """)
        
        # Tabela 3: Comentários (Novidade do Desafio Extra)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                post_id INTEGER NOT NULL,
                autor_id INTEGER NOT NULL,
                conteudo TEXT NOT NULL,
                FOREIGN KEY (post_id) REFERENCES posts (id),
                FOREIGN KEY (autor_id) REFERENCES usuarios (id)
            );
        """)

        conn.commit()
        print("Banco de dados e tabelas (usuarios, posts, comments) inicializados com sucesso.")
    except Exception as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        conn.close()

# Note: As outras funções permanecem iguais.