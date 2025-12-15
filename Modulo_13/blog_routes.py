import sqlite3
from flask import Blueprint, request, jsonify # type: ignore
from database import get_db_connection
from auth import token_required

blog_bp = Blueprint('blog_api', __name__, url_prefix='/blog')

# ----------------------------------------------------
# A. Gerenciamento de Posts
# ----------------------------------------------------

# Rota para Criar um Post (Requer Autenticação)
@blog_bp.route('/posts', methods=['POST'])
@token_required
def create_post(current_user):
    """Cria um novo post no blog."""
    dados = request.get_json()
    titulo = dados.get('titulo')
    conteudo = dados.get('conteudo')

    if not titulo or not conteudo:
        return jsonify({"erro": "Título e conteúdo são obrigatórios."}), 400

    conn = get_db_connection()
    try:
        cursor = conn.execute(
            "INSERT INTO posts (titulo, conteudo, autor_id) VALUES (?, ?, ?)",
            (titulo, conteudo, current_user['id'])
        )
        conn.commit()
        novo_id = cursor.lastrowid
        
        return jsonify({
            "mensagem": "Post criado com sucesso!",
            "id": novo_id,
            "titulo": titulo,
            "autor_id": current_user['id']
        }), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"erro": f"Erro ao criar post: {str(e)}"}), 500
    finally:
        conn.close()

# Rota para Listar Todos os Posts
@blog_bp.route('/posts', methods=['GET'])
def list_posts():
    """Lista todos os posts do blog."""
    conn = get_db_connection()
    posts = conn.execute("""
        SELECT p.id, p.titulo, p.conteudo, u.nome AS autor_nome
        FROM posts p JOIN usuarios u ON p.autor_id = u.id
    """).fetchall()
    conn.close()
    
    posts_list = [dict(post) for post in posts]
    return jsonify(posts_list)

# ----------------------------------------------------
# B. Gerenciamento de Comentários
# ----------------------------------------------------

# Rota para Adicionar Comentário a um Post (Requer Autenticação)
@blog_bp.route('/posts/<int:post_id>/comments', methods=['POST'])
@token_required
def add_comment(current_user, post_id):
    """Adiciona um comentário a um post específico."""
    dados = request.get_json()
    conteudo = dados.get('conteudo')

    if not conteudo:
        return jsonify({"erro": "O conteúdo do comentário é obrigatório."}), 400

    conn = get_db_connection()
    try:
        # 1. Verificar se o post existe
        post = conn.execute("SELECT id FROM posts WHERE id = ?", (post_id,)).fetchone()
        if not post:
            return jsonify({"erro": "Post não encontrado."}), 404

        # 2. Inserir o comentário
        cursor = conn.execute(
            "INSERT INTO comments (post_id, autor_id, conteudo) VALUES (?, ?, ?)",
            (post_id, current_user['id'], conteudo)
        )
        conn.commit()
        novo_id = cursor.lastrowid
        
        return jsonify({
            "mensagem": "Comentário adicionado com sucesso!",
            "id": novo_id,
            "post_id": post_id,
            "autor_id": current_user['id']
        }), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"erro": f"Erro ao adicionar comentário: {str(e)}"}), 500
    finally:
        conn.close()

# Rota para Listar Comentários de um Post
@blog_bp.route('/posts/<int:post_id>/comments', methods=['GET'])
def list_comments(post_id):
    """Lista todos os comentários de um post específico."""
    conn = get_db_connection()
    comments = conn.execute("""
        SELECT c.id, c.conteudo, u.nome AS autor_nome
        FROM comments c 
        JOIN usuarios u ON c.autor_id = u.id
        WHERE c.post_id = ?
    """, (post_id,)).fetchall()
    conn.close()

    if not comments and not conn.execute("SELECT id FROM posts WHERE id = ?", (post_id,)).fetchone():
        return jsonify({"erro": "Post não encontrado."}), 404
    
    comments_list = [dict(comment) for comment in comments]
    return jsonify(comments_list)