# Arquivo: gestao_clientes_db.py

import sqlite3
from sqlite3 import Error

DATABASE = "clientes.db"

def criar_conexao(db_file):
    """Cria uma conexão com o banco de dados SQLite especificado."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conn

def criar_tabela(conn):
    """Cria a tabela Clientes com colunas id, nome, email."""
    sql_create_clientes_table = """CREATE TABLE IF NOT EXISTS Clientes (
                                    id integer PRIMARY KEY,
                                    nome text NOT NULL,
                                    email text NOT NULL UNIQUE
                                );"""
    try:
        c = conn.cursor()
        c.execute(sql_create_clientes_table)
        print("Tabela 'Clientes' configurada com sucesso.")
    except Error as e:
        print(f"Erro ao criar tabela: {e}")

def inserir_cliente(conn, cliente):
    """Operação CREATE (Inserir): Insere um novo cliente na tabela."""
    sql = '''INSERT INTO Clientes(nome,email) VALUES(?,?)'''
    cur = conn.cursor()
    try:
        cur.execute(sql, cliente)
        conn.commit()
        return cur.lastrowid
    except sqlite3.IntegrityError:
        print(f"Erro: Email '{cliente}' já existe.")
        return None

def selecionar_todos_clientes(conn):
    """Operação READ (Consultar): Consulta todos os registros da tabela."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM Clientes")
    rows = cur.fetchall()
    print("\n--- Todos os Clientes Registrados ---")
    for row in rows:
        print(row)
    return rows

def atualizar_cliente(conn, id_cliente, novo_email):
    """Operação UPDATE (Atualizar): Atualiza o email de um cliente específico."""
    sql = '''UPDATE Clientes SET email = ? WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (novo_email, id_cliente))
    conn.commit()
    print(f"\nCliente ID **{id_cliente}** atualizado com novo email: **{novo_email}**.")

def deletar_cliente(conn, id_cliente):
    """Operação DELETE (Deletar): Deleta um cliente pelo ID."""
    sql = 'DELETE FROM Clientes WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id_cliente,))
    conn.commit()
    print(f"\nCliente ID **{id_cliente}** deletado.")

def filtrar_clientes_por_nome(conn, prefixo_nome):
    """Filtragem de Dados: Seleciona clientes com nome começando em um prefixo."""
    sql = "SELECT * FROM Clientes WHERE nome LIKE ? || '%'"
    cur = conn.cursor()
    cur.execute(sql, (prefixo_nome,))
    rows = cur.fetchall()
    print(f"\n--- Clientes com nome começando em '{prefixo_nome}' ---")
    for row in rows:
        print(row)
    return rows

# --- Exemplo de Uso do Módulo Principal ---
if __name__ == '__main__':
    conn = criar_conexao(DATABASE)
    if conn:
        criar_tabela(conn)

        # Inserindo dados de exemplo (CREATE)
        id1 = inserir_cliente(conn, ('Alice Silva', 'alice@exemplo.com'))
        id2 = inserir_cliente(conn, ('Bob Santos', 'bob@exemplo.com'))
        id3 = inserir_cliente(conn, ('Ana Paula', 'ana.paula@exemplo.com'))

        # Consultando todos os dados (READ)
        selecionar_todos_clientes(conn)

        # Atualizando um registro (UPDATE)
        if id2:
            atualizar_cliente(conn, id2, 'bob_santos@novaempresa.com')
        
        # Filtrando dados (Atividade 3)
        filtrar_clientes_por_nome(conn, 'A')

        # Deletando um registro (DELETE)
        if id1:
            deletar_cliente(conn, id1)

        selecionar_todos_clientes(conn)
        
        conn.close()
