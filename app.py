from flask import Flask, request, jsonify, send_from_directory, render_template
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Directorio para almacenar imágenes cargadas temporalmente
imagenes = 'static/images/'
app.config['imagenes'] = imagenes

# Asegúrate de que el directorio exista
os.makedirs(imagenes, exist_ok=True)

@app.route('/')
def index():
  # Usar render_template en lugar de send_static_file
  return render_template('index.html')

@app.route('/upload', methods=['POST'])
def cargar_imagen():
  if 'archivo' not in request.files:
    return jsonify({'error': 'No se encontró el archivo'})
  
  archivo = request.files['archivo']
  
  if archivo.filename == '':
    return jsonify({'error': 'No se cargó ninguna imagen'})
  
  if archivo:
    ruta_imagen = os.path.join(app.config['imagenes'], archivo.filename)
    archivo.save(ruta_imagen)

    # Cargar la imagen
    imagen_original = Image.open(ruta_imagen)

    # Convertir a blanco y negro
    imagen_blanco_negro = imagen_original.convert('L')

    # Guardar la imagen en blanco y negro
    imagen_blanco_negro_path = os.path.join(app.config['imagenes'], 'bn_' + archivo.filename)
    imagen_blanco_negro.save(imagen_blanco_negro_path)

    matriz_blanco_negro = np.array(imagen_blanco_negro)
    matriz_blanco_negro = matriz_blanco_negro.tolist()

    return jsonify({
      'Imagen_Original': archivo.filename,
      'Imagen_Blanco_Negro': 'bn_' + archivo.filename,
      'Matriz_de_Imagen': matriz_blanco_negro
    })

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['imagenes'], filename)

if __name__ == '__main__':
    app.run(debug=True)
