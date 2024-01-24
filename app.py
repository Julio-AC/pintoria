from flask import Flask, render_template, request
import openai
from static.py.cambiar_colores import generar_html
app = Flask(__name__)

@app.route('/')
def index():
    # Diccionario con ejemplos de colores primarios
    colores = {
        'col1-1': {'nombre': 'azul', 'hexadecimal': '#0000FF'},
        'col1-2': {'nombre': 'rojo', 'hexadecimal': '#FF0000'},
        'col1-3': {'nombre': 'verde', 'hexadecimal': '#00FF00'},
        'col2-1': {'nombre': 'amarillo', 'hexadecimal': '#FFFF00'},
        'col2-2': {'nombre': 'naranja', 'hexadecimal': '#FFA500'},
        'col2-3': {'nombre': 'morado', 'hexadecimal': '#800080'},
        'col3-1': {'nombre': 'rosa', 'hexadecimal': '#FFC0CB'},
        'col3-2': {'nombre': 'celeste', 'hexadecimal': '#00FFFF'},
        'col3-3': {'nombre': 'marrón', 'hexadecimal': '#A52A2A'},
        'col4-1': {'nombre': 'gris', 'hexadecimal': '#808080'},
        'col4-2': {'nombre': 'blanco', 'hexadecimal': '#FFFFFF'},
        'col4-3': {'nombre': 'negro', 'hexadecimal': '#000000'},
        'col5-1': {'nombre': 'dorado', 'hexadecimal': '#FFD700'},
        'col5-2': {'nombre': 'plateado', 'hexadecimal': '#C0C0C0'},
        'col5-3': {'nombre': 'verde oscuro', 'hexadecimal': '#006400'},
        'col6-1': {'nombre': 'azul marino', 'hexadecimal': '#000080'},
        'col6-2': {'nombre': 'rojo oscuro', 'hexadecimal': '#8B0000'},
        'col6-3': {'nombre': 'verde oliva', 'hexadecimal': '#808000'}
    }
    html_generado = generar_html(colores)
    return render_template('pintoria.html', html_generado=html_generado)

@app.route('/', methods=['POST'])
def procesar_formulario():
    descripcion = request.form['descripcion']
    opcion_seleccionada = request.form['opcion']

    # Aquí deberías agregar la lógica para conectarte con OpenAI utilizando la descripción y la opción seleccionada
    colores = {
        'col1-1': {'nombre': 'azu123l', 'hexadecimal': '#0000FF'},
        'col1-2': {'nombre': 'ro23jo', 'hexadecimal': '#FF0000'},
        'col1-3': {'nombre': 've234rde', 'hexadecimal': '#00FF00'},
        'col2-1': {'nombre': 'am234arillo', 'hexadecimal': '#FFFF00'},
        'col2-2': {'nombre': 'nar2anja', 'hexadecimal': '#FFA500'},
        'col2-3': {'nombre': 'mora243do', 'hexadecimal': '#800080'},
        'col3-1': {'nombre': 'rosa', 'hexadecimal': '#FFC0CB'},
        'col3-2': {'nombre': 'celeste', 'hexadecimal': '#00FFFF'},
        'col3-3': {'nombre': 'marrón', 'hexadecimal': '#A52A2A'},
        'col4-1': {'nombre': 'gris', 'hexadecimal': '#808080'},
        'col4-2': {'nombre': 'blanco', 'hexadecimal': '#FFFFFF'},
        'col4-3': {'nombre': 'negro', 'hexadecimal': '#000000'},
        'col5-1': {'nombre': 'dorado', 'hexadecimal': '#FFD700'},
        'col5-2': {'nombre': 'plateado', 'hexadecimal': '#C0C0C0'},
        'col5-3': {'nombre': 'verde oscuro', 'hexadecimal': '#006400'},
        'col6-1': {'nombre': 'azul marino', 'hexadecimal': '#000080'},
        'col6-2': {'nombre': 'rojo oscuro', 'hexadecimal': '#8B0000'},
        'col6-3': {'nombre': 'verde oliva', 'hexadecimal': '#808000'}
    }
    html_generado = generar_html(colores)
    return render_template('pintoria.html', html_generado=html_generado)

if __name__ == '__main__':
    app.run(debug=True)
