# Arquivo: sistema_tarefas.py

import sqlite3
from sqlite3 import Error

DATABASE_TAREFAS = "tarefas.db"

def criar_conexao_tarefas(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def setup_db_tarefas(conn):
    """Configura a tabela de tarefas."""
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS Tarefas (
                                    id integer PRIMARY KEY,
                                    descricao text NOT NULL,
                                    concluida integer NOT NULL DEFAULT 0
                                );"""
    try:
        c = conn.cursor()
        c.execute(sql_create_tasks_table)
        print("Tabela 'Tarefas' configurada.")
    except Error as e:
        print(e)

def adicionar_tarefa(conn, descricao):
    """Adiciona uma nova tarefa."""
    sql = '''INSERT INTO Tarefas(descricao) VALUES(?)'''
    cur = conn.cursor()
    cur.execute(sql, (descricao,))
    conn.commit()
    print(f"Tarefa '**{descricao}**' adicionada.")
    return cur.lastrowid

def visualizar_tarefas(conn):
    """Visualiza todas as tarefas."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM Tarefas ORDER BY id ASC")
    rows = cur.fetchall()
    print("\n--- Lista de Tarefas ---")
    if not rows:
        print("Nenhuma tarefa encontrada.")
    for row in rows:
        status = "[X]" if row[2] else "[ ]"
        print(f"{status} ID **{row[0]}**: {row[1]}")
    print("------------------------")

def excluir_tarefa(conn, id_tarefa):
    """Exclui uma tarefa pelo ID."""
    sql = 'DELETE FROM Tarefas WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id_tarefa,))
    conn.commit()
    if cur.rowcount > 0:
        print(f"Tarefa ID **{id_tarefa}** excluída.")
    else:
        print(f"Tarefa ID **{id_tarefa}** não encontrada.")


# --- Exemplo de Uso do Desafio Extra ---
if __name__ == '__main__':
    conn = criar_conexao_tarefas(DATABASE_TAREFAS)
    if conn:
        setup_db_tarefas(conn)

        # Adicionar tarefas
        add1 = adicionar_tarefa(conn, "Estudar Python e SQLite")
        add2 = adicionar_tarefa(conn, "Fazer compras no mercado")
        
        # Visualizar tarefas
        visualizar_tarefas(conn)

        # Excluir uma tarefa
        if add2:
            excluir_tarefa(conn, add2)

        # Visualizar novamente para confirmar exclusão
        visualizar_tarefas(conn)

        conn.close()
