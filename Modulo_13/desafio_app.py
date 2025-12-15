from flask import Flask # type: ignore
from database import init_db
from routes import api_bp # type: ignore # Módulo anterior (saudacao, cadastrar)
from blog_routes import blog_bp # NOVO MÓDULO (posts, comments)

def create_app():
    """Função de fábrica para criar e configurar a aplicação Flask."""
    app = Flask(__name__)
    
    # 1. Inicializa o banco de dados (Criação de todas as tabelas)
    init_db()
    
    # 2. Registra os Blueprints (Conjuntos de Rotas)
    app.register_blueprint(api_bp)
    app.register_blueprint(blog_bp) # NOVO REGISTRO
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)