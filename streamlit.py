import streamlit as st
from openai import OpenAI
import json
from static.py.cambiar_colores import generar_html
import os

def main():
    st.title("Generador de Paletas de Colores")

    # Barra de navegación
    st.sidebar.title("Navegación")
    selected_page = st.sidebar.radio("Selecciona una opción", ["Cómo utilizar la aplicación", "Generar Paleta de Colores"])

    if selected_page == "Cómo utilizar la aplicación":
        st.title("Cómo Utilizar la Aplicación")

        # Descripción
        st.write("1. **Título de la Aplicación:**")
        st.write("- Al ingresar a la aplicación, identificarás un encabezado que proclama 'Generador de Paletas de Colores'. Este título encapsula el objetivo fundamental de la aplicación.")

        # Descripción
        st.write("2. **Descripción:**")
        st.write("- En la sección superior de la interfaz, te toparás con un área de texto con la indicación 'Ingresa la descripción:'. Aquí, tu tarea consiste en proporcionar una sinopsis concisa de la página web para la cual deseas generar una paleta de colores. Puedes incluir detalles sobre el tema, la audiencia, o cualquier otro aspecto pertinente.")

        # Selección del Tipo de Web
        st.write("3. **Selección del Tipo de Web:**")
        st.write("- Justo después de la descripción, te encontrarás con un menú desplegable denominado 'Selecciona el tipo de web:'. En este espacio, puedes elegir el tipo de página web para la cual deseas crear una paleta de colores. Las opciones abarcan desde 'Tienda en línea' y 'Blog Personal' hasta 'Portfolio en línea', entre otras.")

        # Generación de Paleta de Colores
        st.write("4. **Generación de Paleta de Colores:**")
        st.write("- Una vez ingresada la descripción y seleccionado el tipo de web, descubrirás un botón que indica 'Generar Paleta de Colores'. Al hacer clic en este botón, la aplicación empleará la inteligencia artificial de OpenAI para producir una paleta de colores adecuada para la página web que estás describiendo.")

        # Resultado
        st.write("5. **Resultado:**")
        st.write("- Después de hacer clic en el botón, la aplicación te presentará el resultado. Verás la descripción que ingresaste, la opción de tipo de web seleccionada y, lo más crucial, la paleta de colores generada. Los colores se presentan en un formato visualmente atractivo para que puedas visualizar cómo se integrarían en tu página web.")

        # Barra de Navegación - Cómo Utilizar la Aplicación
        st.write("6. **Barra de Navegación - Cómo Utilizar la Aplicación:**")
        st.write("- Si buscas obtener más información sobre el funcionamiento de la aplicación, dirígete a la barra de navegación situada en la esquina superior izquierda de la pantalla. Aquí, encontrarás dos opciones: 'Cómo utilizar la aplicación' y 'Quién es el creador'. Puedes explorar estas opciones para obtener más detalles sobre la aplicación y su operatividad.")

        # Barra de Navegación - Quién es el Creador
        st.write("7. **Barra de Navegación - Quién es el Creador:**")
        st.write("- Dentro de la barra de navegación, también existe la opción de conocer más acerca de 'Quién es el creador'. Haz clic en esta opción para obtener información sobre la persona responsable de la creación de la aplicación y el propósito que la impulsó.")

        # Agrega aquí la información sobre cómo utilizar la aplicación
    else:
        # Formulario en Streamlit
        descripcion = st.text_input("Ingrese la descripción:")
        
        opciones_colores = [
            "Tienda en línea", "Blog Personal", "Portfolio en línea", "Sitio web de Restaurante",
            "Blog de Viajes", "Página de Negocio Local", "Sitio web Educativo", "Sitio Inmobiliario",
            "Portal de Noticias", "Sitio web Musical", "Sitio de Salud y Bienestar", "Blog de Tecnología",
            "Sitio de Gestión de Eventos", "Sitio de Moda", "Plataforma Comunitaria", "Portal Deportivo",
            "Sitio de Arte y Cultura", "Página de Aterrizaje", "Red Social", "Galería de Fotos en línea"
        ]

        opcion_seleccionada = st.selectbox("Seleccione tipo de web:", opciones_colores)

        if st.button("Generar Paleta de Colores"):
            # Lógica para conectarte a OpenAI y obtener una respuesta
            openai_api_key = os.environ.get("OPENAI_KEY")
            client = OpenAI(api_key=openai_api_key)
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

            # Pasándolo al generador de HTML
            colores_generados = json.loads(texto_json)
            html_generado = generar_html(colores_generados)

            # Mostrar resultado en Streamlit
            st.write(f"Descripción: {descripcion}")
            st.write(f"Opción seleccionada: {opcion_seleccionada}")
            st.write("Colores Generados:")
            st.markdown(html_generado, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
