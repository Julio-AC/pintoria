def generar_html(colores):
    html = '\t<h3>Colores</h3>\n'

    for i in range(1, 6):
        html += f'\t<div class="row" id="row{i}">\n'
        for j in range(1, 4):
            col_id = f'col{i}-{j}'
            color_info = colores.get(col_id, {'nombre': 'nombre_color', 'hexadecimal': '#codigo_hexadecimal'})
            nombre_color = color_info['nombre']
            hexadecimal = color_info['hexadecimal']
            color_texto = '#000' if es_color_claro(hexadecimal) else '#fff'
            html += f'\t\t<div class="col-4" id="{col_id}" style="background-color:{hexadecimal}; color:{color_texto};">{nombre_color}</div>\n'
        html += '\t</div>\n'

    html += '\t<h3>Extras</h3>\n'
    html += '\t<div class="row" id="row6">\n'
    
    for i in range(1, 4):
        col_id = f'col6-{i}'
        color_info = colores.get(col_id, {'nombre': 'nombre_color', 'hexadecimal': '#codigo_hexadecimal'})
        nombre_color = color_info['nombre']
        hexadecimal = color_info['hexadecimal']
        color_texto = '#000' if es_color_claro(hexadecimal) else '#fff'
        html += f'\t\t<div class="col-4" id="{col_id}" style="background-color:{hexadecimal}; color:{color_texto};">{nombre_color}</div>\n'

    html += '\t</div>\n'
    html += '</div>'
    
    return html


def es_color_claro(hexadecimal):
    # Convierte el código hexadecimal a RGB
    r, g, b = int(hexadecimal[1:3], 16), int(hexadecimal[3:5], 16), int(hexadecimal[5:7], 16)
    
    # Calcula el brillo (luminancia) según la fórmula
    brillo = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    
    # Si el brillo es mayor que 0.5, consideramos que el color es claro
    return brillo > 0.5
