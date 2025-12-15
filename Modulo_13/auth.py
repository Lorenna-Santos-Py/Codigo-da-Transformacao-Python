from functools import wraps
from flask import request, jsonify # type: ignore
from database import get_db_connection

def get_user_by_id(user_id):
    """Busca um usuário no banco de dados pelo ID."""
    conn = get_db_connection()
    user = conn.execute("SELECT id, nome, email FROM usuarios WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    return dict(user) if user else None

def token_required(f):
    """Decorator para proteger rotas. Requer 'User-ID' no header."""
    @wraps(f)
    def decorated(*args, **kwargs):
        # Para fins de simulação simples, usamos o 'User-ID' como token
        user_id = request.headers.get('User-ID')

        if not user_id:
            return jsonify({'mensagem': 'Token de autenticação (User-ID) ausente.'}), 401
        
        try:
            user_id = int(user_id)
        except ValueError:
             return jsonify({'mensagem': 'User-ID deve ser um número inteiro.'}), 401

        current_user = get_user_by_id(user_id)
        
        if not current_user:
            return jsonify({'mensagem': 'Token de autenticação (User-ID) inválido.'}), 401

        # Passa o objeto do usuário logado para a função da rota
        return f(current_user, *args, **kwargs)

    return decorated