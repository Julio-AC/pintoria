import streamlit as st
from openai import OpenAI
import json
import os
from static.py.cambiar_colores import generar_html

def main():
    st.title("Generador de Paletas de Colores")
    key = os.environ.get("OPENAI_API_KEY")
    # Formulario en Streamlit
    descripcion = st.text_input("Ingrese la descripción:")
    
    opciones_colores = [
        "Tienda en línea", "Blog Personal", "Portfolio en línea", "Sitio web de Restaurante",
        "Blog de Viajes", "Página de Negocio Local", "Sitio web Educativo", "Sitio Inmobiliario",
        "Portal de Noticias", "Sitio web Musical", "Sitio de Salud y Bienestar", "Blog de Tecnología",
        "Sitio de Gestión de Eventos", "Sitio de Moda", "Plataforma Comunitaria", "Portal Deportivo",
        "Sitio de Arte y Cultura", "Página de Aterrizaje (Landing Page)", "Red Social", "Galería de Fotos en línea"
    ]

    opcion_seleccionada = st.selectbox("Seleccione la opción:", opciones_colores)

    if st.button("Generar Paleta de Colores"):
        # Lógica para conectarte a OpenAI y obtener una respuesta
        client = OpenAI(api_key=key)
        prompt = f"Como parte de la creación de una plataforma de diseño web, necesito asistencia para identificar los esquemas de colores ideales para diferentes elementos de la interfaz relacionados con un concepto. Por favor, genera una paleta de colores correspondiente al siguiente tema clave y descripción de una página web, descripción: {descripcion}, tema clave: {opcion_seleccionada}. Los colores solicitados deben adaptarse a elementos como botones, barras de navegación, tarjetas, pie de página, colores de texto y fondo, entre otros componentes relevantes para una estética armoniosa y atractiva. Se requieren los mejores 22 colores, presentados en un diccionario donde la clave sea desde 'col1-1' hasta 'col6-3' habiendo 3 de cada co y el valor sea un diccionario con el 'nombre' correspondiente del color y su valor 'hexadecimal'. Esto contribuirá significativamente a mejorar la experiencia visual de los usuarios en estas páginas web y promoverá la coherencia en el diseño."
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )

        # Obtén el texto generado por OpenAI
        texto_generado = completion.choices[0].message.content

        # Procesa la cadena JSON correctamente
        inicio_json = texto_generado.find("{")
        fin_json = texto_generado.rfind("}") + 1
        texto_json = texto_generado[inicio_json:fin_json]
        texto_json = texto_json.replace("'", '"').replace("None", "null").replace("True", "true").replace("False", "false").replace("},}","}}")

        # Puedes utilizar 'texto_json' en tu aplicación, por ejemplo, pasándolo al generador de HTML
        colores_generados = json.loads(texto_json)
        html_generado = generar_html(colores_generados)

        # Mostrar resultado en Streamlit
        st.write(f"Descripción: {descripcion}")
        st.write(f"Opción seleccionada: {opcion_seleccionada}")
        st.write("HTML Generado:")
        st.markdown(html_generado, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
