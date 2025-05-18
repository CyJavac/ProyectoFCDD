from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que React se comunique con Flask

@app.route('/upload-image', methods=['POST'])
def upload_image():
    # Aquí va la lógica de Roboflow
    return jsonify({"mensaje": "Imagen recibida y procesada"})

@app.route('/update-inventory', methods=['POST'])
def update_inventory():
    data = request.get_json()
    # Guardar ingredientes
    return jsonify({"mensaje": "Inventario actualizado"})

@app.route('/recommend-recipes', methods=['GET'])
def recommend_recipes():
    # Lógica para sugerir 3 recetas
    return jsonify({"recetas": []})

@app.route('/tts/<id>', methods=['GET'])
def tts(id):
    # Lógica TTS
    return jsonify({"mensaje": "Audio generado"})

if __name__ == '__main__':
    app.run(debug=True)
