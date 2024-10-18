import PyPDF2

# Abrir los archivos PDF
with open('ejemplo2.pdf', 'rb') as archivo_pdf, open('archivo1.pdf', 'rb') as marca_agua_pdf:
    lector_pdf = PyPDF2.PdfReader(archivo_pdf)
    lector_marca_agua = PyPDF2.PdfReader(marca_agua_pdf)
    escritor_pdf = PyPDF2.PdfWriter()

    # Obtener la primera (y única) página de la marca de agua
    pagina_marca_agua = lector_marca_agua.pages[0]

    # Añadir la marca de agua a cada página del PDF original
    for pagina in lector_pdf.pages:
        pagina.merge_page(pagina_marca_agua)  # Fusionar con la marca de agua
        escritor_pdf.add_page(pagina)

    # Guardar el nuevo archivo con la marca de agua
    with open('archivo_con_marca_agua.pdf', 'wb') as archivo_salida:
        escritor_pdf.write(archivo_salida)

    print("Marca de agua añadida correctamente.")