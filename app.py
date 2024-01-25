from flask import Flask, render_template, request
from openai import OpenAI
import json
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

    # Lógica para conectarte a OpenAI y obtener una respuesta
    client = OpenAI(api_key="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")
    prompt = f"Como parte de la creación de una plataforma de diseño web, necesito asistencia para identificar los esquemas de colores ideales para diferentes elementos de la interfaz relacionados con un concepto. Por favor, genera una paleta de colores correspondiente al siguiente tema clave y descripción de una página web, descripción: {descripcion}, tema clave: {opcion_seleccionada}. Los colores solicitados deben adaptarse a elementos como botones, barras de navegación, tarjetas, pie de página, colores de texto y fondo, entre otros componentes relevantes para una estética armoniosa y atractiva. Se requieren los mejores 22 colores, presentados en un diccionario donde la clave sea desde 'col1-1' hasta 'col6-3' habiendo 3 de cada co y el valor sea un diccionario con el 'nombre' correspondiente del color y su valor 'hexadecimal'. Esto contribuirá significativamente a mejorar la experiencia visual de los usuarios en estas páginas web y promoverá la coherencia en el diseño."
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    print(completion)
    
    # Obtén el texto generado por OpenAI
    texto_generado = completion.choices[0].message.content
    print(texto_generado)

    # Procesa la cadena JSON correctamente
    inicio_json = texto_generado.find("{")
    fin_json = texto_generado.rfind("}") + 1
    texto_json = texto_generado[inicio_json:fin_json]
    texto_json = texto_json.replace("'", '"').replace("None", "null").replace("True", "true").replace("False", "false").replace("},}","}}")

    # Imprimir el contenido del JSON limpio
    print(texto_json)

    # Puedes utilizar 'texto_json' en tu aplicación, por ejemplo, pasándolo al generador de HTML
    colores = json.loads(texto_json)

    html_generado = generar_html(colores)
    return render_template('pintoria.html', html_generado=html_generado)


if __name__ == '__main__':
    app.run(debug=True)
