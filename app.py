import numpy as np
from flask import Flask, render_template, abort
from PIL import Image

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    image_path = 'static/hola.jpg'
    try:
        original_image = Image.open(image_path)
    except FileNotFoundError:
        abort(404, description="Archivo de imagen no encontrado.")
    except Exception as e:
        abort(500, description=str(e))
    
    # Definir las matrices de transformación
    theta = np.radians(30)  # 30 grados a radianes
    tx, ty = 50, 30         # Traslación
    sx, sy = 0.5, 0.5       # Escalamiento
    shearX, shearY = 0.5, 0.2  # Sisayado

    # Matriz de Rotación
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

    # Matriz de Traslación
    translation_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

    # Matriz de Escalamiento
    scaling_matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

    # Matriz de Sisayado
    shear_matrix = np.array([
        [1, shearX, 0],
        [shearY, 1, 0],
        [0, 0, 1]
    ])

    # Componer todas las matrices
    transformation_matrix = translation_matrix @ scaling_matrix @ shear_matrix @ rotation_matrix

    # Mostrar las matrices por consola
    print("Matriz de Rotación:\n", rotation_matrix)
    print("Matriz de Traslación:\n", translation_matrix)
    print("Matriz de Escalamiento:\n", scaling_matrix)
    print("Matriz de Sisayado:\n", shear_matrix)
    print("Matriz de Transformación Compuesta:\n", transformation_matrix)

    # Renderizar la página HTML transformada
    try:
        return render_template('transformed.html')
    except Exception as e:
        abort(500, description="Error al renderizar la plantilla HTML: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
