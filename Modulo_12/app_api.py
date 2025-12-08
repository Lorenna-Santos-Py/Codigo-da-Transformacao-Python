# Arquivo: app_api.py
from flask import Flask, jsonify # type: ignore

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK", "servico": "ativo"}), 200

if __name__ == '__main__':
    # Em um ambiente real, você não rodaria o servidor assim, mas sim com 'flask run'
    pass 
