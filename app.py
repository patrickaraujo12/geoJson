from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/json/piaui', methods=['GET'])
def piaui_file():
    # Abre e lê o arquivo JSON
    with open('piaui.json', 'r') as file:
        data = json.load(file)
    # Retorna o conteúdo do arquivo JSON como resposta
    return jsonify(data), 200

@app.route('/json/maranhao', methods=['GET'])
def maranhao_file():
    # Abre e lê o arquivo JSON
    with open('maranhao.json', 'r') as file:
        data = json.load(file)
    # Retorna o conteúdo do arquivo JSON como resposta
    return jsonify(data), 200

@app.route('/json/para', methods=['GET'])
def para_file():
    # Abre e lê o arquivo JSON
    with open('para.json', 'r') as file:
        data = json.load(file)
    # Retorna o conteúdo do arquivo JSON como resposta
    return jsonify(data), 200

@app.route('/json/alagoas', methods=['GET'])
def alogoas_file():
    # Abre e lê o arquivo JSON
    with open('alagos.json', 'r') as file:
        data = json.load(file)
    # Retorna o conteúdo do arquivo JSON como resposta
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)